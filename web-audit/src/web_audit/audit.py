"""The technical audit of an audit of capture: the technical dossier of Contenido and Marcado.

Each requirement of the reference gives its cases (D-161): one for the site if its view is general,
and one per page of the audit whose type is in its page_types if it is particular. The check of
each case (checks/) gives its state with its evidence; the cases that need a judgement or the
visible content of the page stay `pendiente` for an agent (skill /web-audit), which writes its
judgements; `finish` validates them and writes the dossier with the rate of D-166.

The access to the images of the markup (ws-consumer/004, 005, 185, 186, 334, 335) reads the
responses that capture recorded (capture.resources, T-086): `images` gives capture the list of
image URLs of the markup of the pages, before `run`.

  web-audit/var/audits/<audit>/
    cases.json       every case, as the code decided it (pending ones included)
    pending.json     the pending cases, with what the agent needs to judge each one
    judgments.json   the agent's judgements (written by the agent)
    dossier.json     the technical dossier: every case with its final state, and the rates
    report.md        the dossier for a person

Rate (D-166, scoring-systems): one per scope and view, and in the particular view per page type,
counting the cases requirement × page; satisfied / evaluated, with evaluated = pertinent − NA − NE;
the same by nature; coverage = evaluated / (pertinent − NA) (D-169). No weights, thresholds or states derived
from it. Contenido and Marcado are never added together.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import traceback
from datetime import datetime
from pathlib import Path
from urllib.parse import urljoin, urlsplit

from . import ROOT
from .checks import NA, NE, PENDING, SAT, STATES, UNSAT, Case, Result, load_all
from .site import PAGE_TYPES, Site

REQUIREMENTS = Path(os.environ.get("REFERENCE_DIR") or ROOT / "reference") / "requirements"
OUT = Path(os.environ.get("WEB_AUDIT_VAR") or ROOT / "var") / "audits"
SCOPES = ("Contenido", "Marcado")
NATURES = ("obligatoria", "recomendada")
NO_DOCUMENT = "No se dispone del documento de la página (outcome {}): no se puede examinar su marcado."


def requirements() -> list[dict]:
    out = []
    for path in sorted(REQUIREMENTS.glob("*.json")):
        out += json.loads(path.read_text(encoding="utf-8"))["requirements"]
    return out


def _json(data) -> str:
    return json.dumps(data, ensure_ascii=False, indent=1, default=str)


# --- Evaluation ---------------------------------------------------------------------------------

def evaluate(site: Site, reqs: list[dict] | None = None) -> list[dict]:
    registry = load_all()
    reqs = reqs or requirements()
    cases = []
    for req in reqs:
        fn = registry.get(req["id"])
        if fn is None:
            raise LookupError(f"{req['id']}: sin comprobación en checks/")
        targets = [None] if req["view"] == "general" else \
            [p for p in site.pages if p.page_type in req.get("page_types", [])]
        for page in targets:
            case = Case(site, page, req)
            if page is not None and req["scope"] == "Marcado" and page.doc is None:
                result = Result(NE, {"outcome": page.outcome}, NO_DOCUMENT.format(page.outcome))
            elif page is None and req["scope"] == "Marcado" and not any(p.doc is not None for p in site.pages):
                result = Result(NE, None, "No se dispone del documento de ninguna página de la auditoría.")
            else:
                try:
                    result = fn(case)
                except Exception as exc:  # a bug of the auditor, not an incident of the audit
                    raise RuntimeError(f"{req['id']} en {page.id if page else 'el sitio'}: {exc}\n"
                                       f"{traceback.format_exc()}") from exc
            if result.state not in STATES + (PENDING,):
                raise ValueError(f"{req['id']}: estado desconocido {result.state}")
            cases.append({"req": req["id"], "scope": req["scope"], "view": req["view"], "nature": req["nature"],
                          "page": page.id if page else None, "page_type": page.page_type if page else None,
                          "state": result.state, "by": "código", "evidence": result.evidence, "reason": result.reason})
    return cases


def pending_tasks(site: Site, cases: list[dict], reqs: dict) -> list[dict]:
    out = []
    for c in cases:
        if c["state"] != PENDING:
            continue
        req = reqs[c["req"]]
        page = site.page(c["page"]) if c["page"] else None
        out.append({"req": c["req"], "page": c["page"], "url": page.url_final if page else site.url,
                    "question": c["reason"], "evidence": c["evidence"], "condition": req["condition"],
                    "method": req["method"], "applicability": req["applicability"]})
    return out


# --- Rate (D-166, D-169) -------------------------------------------------------------------------------------

def counts(cases: list[dict]) -> dict:
    n = {s: sum(1 for c in cases if c["state"] == s) for s in STATES}
    pertinent = len(cases)
    applicable = pertinent - n[NA]
    evaluated = applicable - n[NE]
    return {"pertinentes": pertinent, "NA": n[NA], "NE": n[NE], "evaluados": evaluated, "satisfechos": n[SAT],
            "no satisfechos": n[UNSAT],
            "tasa": round(n[SAT] / evaluated, 4) if evaluated else None,
            "cobertura": round(evaluated / applicable, 4) if applicable else None}


def rate(cases: list[dict]) -> dict:
    def block(group: list[dict]) -> dict:
        return {"total": counts(group), **{n: counts([c for c in group if c["nature"] == n]) for n in NATURES}}

    out = {}
    for scope in SCOPES:
        mine = [c for c in cases if c["scope"] == scope]
        general = [c for c in mine if c["view"] == "general"]
        entry = {"general": block(general) if general else None, "particular": {}}
        for page_type in PAGE_TYPES.values():
            group = [c for c in mine if c["view"] == "particular" and c["page_type"] == page_type]
            if not group:
                continue
            pages = sorted({c["page"] for c in group})
            by_req = {}
            for req_id in sorted({c["req"] for c in group}):
                rc = [c for c in group if c["req"] == req_id]
                ev = [c for c in rc if c["state"] in (SAT, UNSAT)]
                by_req[req_id] = {"páginas evaluadas": len(ev), "satisfecho en": sum(1 for c in ev if c["state"] == SAT),
                                  "proporción": round(sum(1 for c in ev if c["state"] == SAT) / len(ev), 4) if ev else None}
            entry["particular"][page_type] = {
                **block(group), "páginas": {p: counts([c for c in group if c["page"] == p]) for p in pages},
                "por requisito": by_req}
        out[scope] = entry
    return out


# --- Judgements of the agent -------------------------------------------------------------------------

def validate(pending: list[dict], judgments: list) -> list[str]:
    errors = []
    if not isinstance(judgments, list):
        return ["judgments.json ha de ser una lista"]
    wanted = {(p["req"], p["page"]) for p in pending}
    seen = set()
    for i, j in enumerate(judgments):
        where = f"juicio {i + 1}"
        if not isinstance(j, dict):
            errors.append(f"{where}: ha de ser un objeto")
            continue
        key = (j.get("req"), j.get("page"))
        if key not in wanted:
            errors.append(f"{where}: {key} no es un caso pendiente")
        if key in seen:
            errors.append(f"{where}: {key} repetido")
        seen.add(key)
        if j.get("state") not in STATES:
            errors.append(f"{where}: estado {j.get('state')!r} (ha de ser uno de {', '.join(STATES)})")
        if not (isinstance(j.get("evidence"), str) and j["evidence"].strip()):
            errors.append(f"{where}: falta la evidencia")
        if j.get("state") in (NA, NE) and not (isinstance(j.get("reason"), str) and j["reason"].strip()):
            errors.append(f"{where}: un {j.get('state')} lleva su motivo (reason)")
        extra = set(j) - {"req", "page", "state", "evidence", "reason"}
        if extra:
            errors.append(f"{where}: campos no admitidos {sorted(extra)}")
    missing = wanted - seen
    errors += [f"falta el juicio de {req} en {page or 'el sitio'}" for req, page in sorted(missing, key=str)]
    return errors


# --- Report ------------------------------------------------------------------------------------------------

def _pct(x) -> str:
    return "—" if x is None else f"{x * 100:.1f} %".replace(".", ",")


def _row(label: str, c: dict) -> str:
    return (f"| {label} | {c['pertinentes']} | {c['NA']} | {c['NE']} | {c['evaluados']} | {c['satisfechos']} | "
            f"{_pct(c['tasa'])} | {_pct(c['cobertura'])} |")


HEADER = "| | Pertinentes | NA | NE | Evaluados | Satisfechos | Tasa | Cobertura |\n|---|---|---|---|---|---|---|---|"


def report(dossier: dict, reqs: dict) -> str:
    lines = [f"# Expediente técnico · {dossier['audit']}", "",
             f"Sitio: {dossier['site']} · auditoría de capture: `capture/var/audits/{dossier['audit']}` · "
             f"generado el {dossier['generated_at']}.", "",
             "Tasa de cumplimiento técnico (D-166, D-169): satisfechos / evaluados, con evaluados = pertinentes − NA − NE; "
             "cobertura = evaluados / (pertinentes − NA). Sin pesos ni umbrales. Contenido y Marcado no se suman.", ""]
    for scope, entry in dossier["rate"].items():
        lines += [f"## {scope}", ""]
        if entry["general"]:
            lines += ["### Vista general", "", HEADER]
            lines += [_row(k if k != "total" else "**todas**", v) for k, v in entry["general"].items()]
            lines.append("")
        for page_type, block in entry["particular"].items():
            lines += [f"### Vista particular · {page_type}", "", HEADER]
            lines += [_row(k if k != "total" else "**todas**", block[k]) for k in ("total",) + NATURES]
            lines += ["", "Por página:", "", HEADER]
            lines += [_row(p, c) for p, c in block["páginas"].items()]
            lines.append("")
    failed = [c for c in dossier["cases"] if c["state"] == UNSAT]
    lines += ["## No satisfechos", "", "| Requisito | Naturaleza | Página | Condición |", "|---|---|---|---|"]
    lines += [f"| {c['req']} | {c['nature']} | {c['page'] or 'sitio'} | {reqs[c['req']]['condition']} |" for c in failed]
    ne = [c for c in dossier["cases"] if c["state"] == NE]
    lines += ["", "## Incidencias (NE)", "", "| Requisito | Página | Motivo |", "|---|---|---|"]
    lines += [f"| {c['req']} | {c['page'] or 'sitio'} | {c['reason']} |" for c in ne]
    by_agent = [c for c in dossier["cases"] if c["by"] == "agente"]
    if by_agent:
        lines += ["", "## Decididos por el agente", "", "| Requisito | Página | Estado | Evidencia |", "|---|---|---|---|"]
        lines += [f"| {c['req']} | {c['page'] or 'sitio'} | {c['state']} | {c['evidence']} |" for c in by_agent]
    return "\n".join(lines) + "\n"


# --- Commands ---------------------------------------------------------------------------------------------

def folder(audit_id: str) -> Path:
    return OUT / audit_id


def finish(audit_id: str) -> dict:
    out = folder(audit_id)
    cases = json.loads((out / "cases.json").read_text(encoding="utf-8"))
    pending = json.loads((out / "pending.json").read_text(encoding="utf-8"))
    judgments = []
    if pending:
        path = out / "judgments.json"
        if not path.exists():
            raise SystemExit(f"audit: faltan los juicios de {len(pending)} casos pendientes ({path})")
        judgments = json.loads(path.read_text(encoding="utf-8"))
        errors = validate(pending, judgments)
        if errors:
            raise SystemExit("audit: juicios no válidos:\n  " + "\n  ".join(errors))
    by_key = {(j["req"], j["page"]): j for j in judgments}
    final = []
    for c in cases:
        if c["state"] == PENDING:
            j = by_key[(c["req"], c["page"])]
            c = {**c, "state": j["state"], "by": "agente", "question": c["reason"],
                 "evidence": j["evidence"], "facts": c["evidence"], "reason": j.get("reason")}
        final.append(c)
    manifest = json.loads((out / "run.json").read_text(encoding="utf-8"))
    dossier = {**manifest, "generated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
               "rate": rate(final), "cases": final}
    reqs = {r["id"]: r for r in requirements()}
    (out / "dossier.json").write_text(_json(dossier), encoding="utf-8")
    (out / "report.md").write_text(report(dossier, reqs), encoding="utf-8")
    return dossier


def run(audit_id: str) -> tuple[list, list]:
    site = Site(audit_id)
    reqs = requirements()
    cases = evaluate(site, reqs)
    pending = pending_tasks(site, cases, {r["id"]: r for r in reqs})
    out = folder(audit_id)
    out.mkdir(parents=True, exist_ok=True)
    (out / "run.json").write_text(_json({
        "audit": audit_id, "site": site.url, "capture": str(site.folder.relative_to(ROOT.parent)) if site.folder.is_relative_to(ROOT.parent)
        else str(site.folder),
        "evaluated_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "pages": [{"id": p.id, "type": p.page_type, "url": p.url, "outcome": p.outcome, "status": p.status}
                  for p in site.pages],
        "not_located": {k: v for k, v in (site.manifest.get("policies") or {}).items() if v.get("status") != "located"},
        "breadcrumbs": {p["page"]: p.get("breadcrumbs", {}).get("status") for p in site.manifest.get("products", [])},
        "requirements": len(reqs)}), encoding="utf-8")
    (out / "cases.json").write_text(_json(cases), encoding="utf-8")
    (out / "pending.json").write_text(_json(pending), encoding="utf-8")
    stale = out / "judgments.json"
    if stale.exists() and pending:
        stale.rename(out / f"judgments.{datetime.now():%Y%m%dT%H%M%S}.old.json")
    return cases, pending


def image_list(site: Site) -> list[str]:
    """The http(s) image URLs of the markup of every page of the audit (ws-consumer/185)."""
    from .checks.consumer import markup_images
    urls = []
    for page in site.pages:
        if page.doc is not None:
            urls += markup_images(page.graph, lambda e, u, page=page: urljoin(page.url_final, u))
    return [u for u in dict.fromkeys(urls) if urlsplit(u).scheme in ("http", "https")]


def _summary(cases: list[dict]) -> str:
    by = {s: sum(1 for c in cases if c["state"] == s) for s in STATES + (PENDING,)}
    return " · ".join(f"{k} {v}" for k, v in by.items())


def cmd_run(args) -> None:
    cases, pending = run(args.audit)
    print(f"{args.audit}: {len(cases)} casos ({_summary(cases)})")
    if pending:
        print(f"{len(pending)} pendientes de juicio: {folder(args.audit) / 'pending.json'}; "
              f"los juicios, en judgments.json, y después `audit finish {args.audit}`")
    else:
        finish(args.audit)
        print(f"expediente: {folder(args.audit) / 'report.md'}")


def cmd_finish(args) -> None:
    dossier = finish(args.audit)
    print(f"{args.audit}: {len(dossier['cases'])} casos ({_summary(dossier['cases'])})")
    print(f"expediente: {folder(args.audit) / 'report.md'}")


def cmd_check(args) -> None:
    out = folder(args.audit)
    pending = json.loads((out / "pending.json").read_text(encoding="utf-8"))
    path = out / "judgments.json"
    judgments = json.loads(path.read_text(encoding="utf-8")) if path.exists() else []
    errors = validate(pending, judgments)
    if errors:
        raise SystemExit("audit: juicios no válidos:\n  " + "\n  ".join(errors))
    print(f"correcto · {len(judgments)} juicios")


def cmd_text(args) -> None:
    """The visible text of a page of the audit (what the agent reads to judge)."""
    page = Site(args.audit).page(args.page)
    if page.doc is None:
        raise SystemExit(f"audit: {args.page} no tiene documento (outcome {page.outcome})")
    body = page.doc.body()
    print(page.doc.visible_text(body) if body is not None else "")


def cmd_images(args) -> None:
    urls = image_list(Site(args.audit))
    if args.list:
        print("\n".join(urls))
        return
    print(f"{args.audit}: {len(urls)} URL de imagen del marcado; las pide capture (pages resources)", flush=True)
    if urls:
        done = subprocess.run([str(ROOT.parent / "capture/bin/pages"), "resources", args.audit, "--from", "-"],
                              input="\n".join(urls) + "\n", text=True)
        raise SystemExit(done.returncode)


def cmd_pending(args) -> None:
    pending = json.loads((folder(args.audit) / "pending.json").read_text(encoding="utf-8"))
    for p in pending:
        print(f"{p['req']} · {p['page'] or 'sitio'} · {p['question']}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="audit", description="Auditado técnico de Contenido y Marcado (expediente técnico).")
    sub = parser.add_subparsers(dest="cmd", required=True)
    for name, fn, help_text in (("run", cmd_run, "evaluar una auditoría de capture"),
                                ("check", cmd_check, "validar los juicios del agente (judgments.json)"),
                                ("finish", cmd_finish, "validar los juicios del agente y escribir el expediente"),
                                ("pending", cmd_pending, "los casos pendientes de juicio")):
        p = sub.add_parser(name, help=help_text)
        p.add_argument("audit")
        p.set_defaults(func=fn)
    p = sub.add_parser("images", help="pasar a capture las URL de imagen del marcado (antes de run)")
    p.add_argument("audit")
    p.add_argument("--list", action="store_true", help="solo escribir la lista, sin pedirla")
    p.set_defaults(func=cmd_images)
    p = sub.add_parser("text", help="el texto visible de una página de la auditoría")
    p.add_argument("audit")
    p.add_argument("page")
    p.set_defaults(func=cmd_text)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
