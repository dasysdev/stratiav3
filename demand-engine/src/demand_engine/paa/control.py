"""A PAA classification against its control case (T-052; D-114, D-180): cases/paa/<set>.json.

The ids (N1, R2, the criterion ids) change from one run to another, so the comparison is by content:
  perimeter       the questions the case puts out, against those the classification puts out
  criteria        by the questions they share; then the verdict (and whether it is intermediate). The case holds the
                  criteria that generate or not: a covered one of the classification is not new
  candidates      by the questions that support them; failing that, by the words of their question
  revisions       by target and action
  contributions   by target and kind; among several, the closest wording
  specializations the new specializations PAA proposes (D-218), by the questions that go to them
An element with «expected: false» must not come back: if it does, it is a regression. What the classification
has and the case does not is reported as new: the case was reviewed against another rulebook and may lack it.
The decision (D-180), over the total of all the control sets, against the last accepted pass
(training/reports/paa/accepted.json): accepted if no section finds fewer expected elements nor has more regressions.
New elements and efficiency are reported, but do not decide. Without an accepted pass, the first one is accepted.
Standard library only: it runs on the host.
"""
from __future__ import annotations

import re
from pathlib import Path

from capture.files import now, read_json, write_json

from .. import ROOT
from .store import SeedSet, StoreError, var_root
from .text import norm

CASES = ROOT / "cases/paa"
ACCEPTED = ROOT / "training/reports/paa/accepted.json"  # the last accepted pass: versioned, unlike var/
SECTIONS = ("criteria", "candidates", "revisions", "contributions", "specializations")
NAMES = {"criteria": "Criterios", "candidates": "Candidatos", "revisions": "Revisiones", "contributions": "Aportaciones",
         "specializations": "Especializaciones"}
STOP = set("de del la las el los un una unos unas y o a en con por para que se es su sus al lo le les qué cuál "
           "cuáles cómo tiene tienen declara ofrece".split())
SIMILAR = 0.5  # share of the words of the shorter question for a candidate matched by its wording


def case_ids() -> list[str]:
    return sorted(p.stem for p in CASES.glob("*.json"))


def words(text: str) -> set[str]:
    return {w for w in re.findall(r"\w+", norm(text)) if w not in STOP and len(w) > 2}


def overlap(a: set, b: set) -> float:
    """Share of the smaller set that the other one has."""
    return len(a & b) / min(len(a), len(b)) if a and b else 0.0


def result_items(result: dict) -> dict:
    """The classification in the shape of the case: each element with its questions as normalised texts."""
    text = {q["n"]: norm(q["q"]) for q in result["questions"]}
    by_crit: dict[str, set] = {}
    for q in result["questions"]:
        if q.get("criterion"):
            by_crit.setdefault(q["criterion"], set()).add(norm(q["q"]))
    return {
        "criteria": [{"id": c["id"], "name": c["name"], "verdict": c["verdict"],
                      "intermediate": bool(c.get("intermediate")), "qs": by_crit.get(c["id"], set())}
                     for c in result["criteria"]],
        "candidates": [{"id": c["id"], "question": c["question"], "blocks": c.get("blocks", []), "trait": c.get("trait"),
                        "qs": {text[n] for n in c.get("support", [])}} for c in result["candidates"]],
        "revisions": [{"id": r["id"], "target": r["target"], "action": r["action"]} for r in result["revisions"]],
        "contributions": [{"id": f"A{i}", "target": c["target"], "kind": c["kind"], "contribution": c["contribution"]}
                          for i, c in enumerate(result["contributions"], 1)],
        "specializations": [{"id": x["id"], "name": x["name"], "qs": {text[n] for n in x.get("questions", [])}}
                            for x in result.get("specializations") or []],
    }


def score(section: str, want: dict, got: dict) -> float:
    """How well an element of the classification matches one of the case (0: not at all)."""
    if section in ("criteria", "specializations"):
        return overlap({norm(q) for q in want.get("questions", [])}, got["qs"])
    if section == "candidates":
        by_questions = overlap({norm(q) for q in want.get("questions", [])}, got["qs"])
        if by_questions:
            return 1 + by_questions  # the support decides before the wording
        by_words = overlap(words(want["question"]), words(got["question"]))
        return by_words if by_words >= SIMILAR else 0.0
    if section == "revisions":
        return 1.0 if (want["target"], want["action"]) == (got["target"], got["action"]) else 0.0
    if (want["target"], want["kind"]) != (got["target"], got["kind"]):
        return 0.0
    return 1 + overlap(words(want["contribution"]), words(got["contribution"]))


def pair(section: str, wanted: list, found: list) -> dict:
    """One to one, the best pairs first: {index in the case: element of the classification}."""
    scores = sorted(((score(section, w, g), i, j) for i, w in enumerate(wanted) for j, g in enumerate(found)),
                    reverse=True)
    out, used = {}, set()
    for s, i, j in scores:
        if s > 0 and i not in out and j not in used:
            out[i] = found[j]
            used.add(j)
    return out


def agrees(section: str, want: dict, got: dict) -> list[str]:
    """What differs in a matched element (empty: it agrees)."""
    diff = []
    if section == "criteria":
        if want["verdict"] != got["verdict"]:
            diff.append(f"veredicto {got['verdict']} (esperado {want['verdict']})")
        if bool(want.get("intermediate")) != got["intermediate"]:
            diff.append("intermedio" if got["intermediate"] else "no intermedio")
    if section == "candidates":
        if set(want.get("blocks", [])) != set(got["blocks"]):
            diff.append(f"bloques {', '.join(got['blocks'])}")
        if want.get("trait") != got["trait"]:
            diff.append(f"rasgo {got['trait']} (esperado {want.get('trait')})")
    return diff


def compare(case: dict, result: dict) -> dict:
    """Matches, misses, regressions and new elements of one set."""
    out_case = {norm(q) for q in case["perimeter"]["out"]}
    out_result = {norm(q["q"]) for q in result["questions"] if q["perimeter"] == "fuera"}
    asked = {norm(q["q"]) for q in result["questions"]}
    original = {norm(q): q for q in case["perimeter"]["out"]}
    found_text = {norm(q["q"]): q["q"] for q in result["questions"]}
    sets = {"perimeter": {
        "expected": len(out_case & asked), "found": len(out_case & out_result),
        "missed": sorted(original[q] for q in (out_case & asked) - out_result),
        "new": sorted(found_text[q] for q in out_result - out_case),
        "absent": len(out_case - asked)}}
    items = result_items(result)
    for section in SECTIONS:
        wanted = case.get(section, [])
        matched = pair(section, wanted, items[section])
        rows = []
        for i, w in enumerate(wanted):
            got = matched.get(i)
            appears = got is not None and (section != "criteria" or got["verdict"] == w["verdict"] or w["expected"])
            rows.append({"expected": w["expected"], "label": label(section, w), "found": got and got["id"],
                         "appears": appears, "diff": agrees(section, w, got) if got and w["expected"] else []})
        used = {g["id"] for g in matched.values()}
        # the case holds the criteria that generate or not, not the covered ones (T-042): those are not new
        new = [g for g in items[section] if g["id"] not in used and g.get("verdict") != "cubierto"]
        sets[section] = {"rows": rows, "new": [label(section, g) for g in new]}
    return sets


def label(section: str, x: dict) -> str:
    if section in ("criteria", "specializations"):
        return x["name"]
    if section == "candidates":
        return x["question"]
    if section == "revisions":
        return f"{x['action']} {x['target']}"
    return f"{x['target']} · {x['kind']}: {x['contribution']}"


def summary(sets: dict) -> dict:
    """The counts of one set (or of all of them, added up)."""
    s = {"out_expected": sets["perimeter"]["expected"], "out_found": sets["perimeter"]["found"],
         "out_new": len(sets["perimeter"]["new"])}
    for section in SECTIONS:
        rows = sets[section]["rows"]
        s[section] = {"expected": sum(r["expected"] for r in rows),
                      "found": sum(r["expected"] and r["appears"] for r in rows),
                      "agree": sum(r["expected"] and r["appears"] and not r["diff"] for r in rows),
                      "not_expected": sum(not r["expected"] for r in rows),
                      "regressions": sum(not r["expected"] and r["appears"] for r in rows),
                      "new": len(sets[section]["new"])}
    return s


def add(total: dict, s: dict) -> dict:
    for k, v in s.items():
        if isinstance(v, dict):
            add(total.setdefault(k, {}), v)
        else:
            total[k] = total.get(k, 0) + v
    return total


def pct(a: int, b: int) -> str:
    return f"{a}/{b} ({round(100 * a / b)} %)" if b else "—"


def decide(base: dict | None, total: dict) -> dict:
    """D-180: no section may find fewer expected elements nor have more regressions than the accepted pass."""
    if not base:
        return {"accepted": True, "against": None, "worse": []}
    was, worse = base["total"], []
    if total["out_found"] < was["out_found"]:
        worse.append(f"perímetro: fuera {total['out_found']} (antes {was['out_found']})")
    for section in SECTIONS:
        # a section the accepted pass did not have yet (specializations, D-218) starts from zero
        now_, before = total[section], was.get(section, {"found": 0, "regressions": 0})
        if now_["found"] < before["found"]:
            worse.append(f"{NAMES[section].lower()}: esperados encontrados {now_['found']} (antes {before['found']})")
        if now_["regressions"] > before["regressions"]:
            worse.append(f"{NAMES[section].lower()}: regresiones {now_['regressions']} (antes {before['regressions']})")
    return {"accepted": not worse, "against": base["at"], "worse": worse}


def run(set_ids: list[str]) -> tuple[Path, dict]:
    sets, total = {}, {}
    for set_id in set_ids:
        case = read_json(CASES / f"{set_id}.json")
        if not case:
            raise StoreError(f"no hay caso de control para «{set_id}» en {CASES}")
        result = read_json(SeedSet(set_id).dir / "classified.json")
        if not result:
            raise StoreError(f"{set_id}: falta classified.json («paa classify report {set_id}»)")
        detail = compare(case, result)
        s = summary(detail)
        sets[set_id] = {"rulebook": result.get("rulebook_version") or result.get("rulebook"), "at": result.get("at"),
                        "reviewed": case.get("reviewed", {}).get("rulebook"), "summary": s, "detail": detail}
        add(total, s)
    out = var_root() / "control" / now().replace(":", "")[:17]
    data = {"at": now(), "sets": sets, "total": total}
    # the rule is over the total of the control sets: a subset is reported, but does not decide
    data["decision"] = decide(read_json(ACCEPTED), total) if sorted(set_ids) == case_ids() else None
    write_json(out / "control.json", data)
    (out / "report.md").write_text(report(data), encoding="utf-8")
    return out, data


def report(data: dict) -> str:
    t = data["total"]
    lines = ["# Control de PAA contra cases/paa", "", f"- Fecha: {data['at']}",
             f"- Conjuntos: {len(data['sets'])}", "",
             "Comparación por contenido, no por ids. «Esperado»: lo que el caso marca como debe aparecer; «coincide»: "
             "además, sin diferencias (veredicto e intermedio en criterios; bloques y rasgo en candidatos). "
             "«Regresiones»: elementos marcados como no esperados que vuelven. «Nuevos»: lo que la clasificación tiene "
             "y el caso no (el caso se revisó con otro reglamento: puede faltarle).", "", "## Total", "",
             "| | Esperados encontrados | Coinciden | Regresiones | Nuevos |", "|---|---|---|---|---|",
             f"| Perímetro (fuera) | {pct(t['out_found'], t['out_expected'])} | — | — | {t['out_new']} |"]
    for section in SECTIONS:
        x = t[section]
        lines.append(f"| {NAMES[section]} | {pct(x['found'], x['expected'])} | {pct(x['agree'], x['expected'])} "
                     f"| {x['regressions']}/{x['not_expected']} | {x['new']} |")
    d = data.get("decision")
    lines += ["", "## Decisión (D-180)", ""]
    if d is None:
        lines.append("Sin decisión: la regla se aplica sobre el total de los conjuntos de control, no sobre una parte.")
    elif d["accepted"]:
        lines.append("Se acepta: " + (f"ningún apartado empeora frente a la pasada aceptada del {d['against']}."
                                      if d["against"] else "no hay pasada aceptada; es la primera."))
    else:
        lines += [f"Se rechaza frente a la pasada aceptada del {d['against']}:", ""] + [f"- {w}" for w in d["worse"]]
    lines += ["", "## Por conjunto", "",
              "| Conjunto | Reglamento | Fuera | " + " | ".join(NAMES[k] for k in SECTIONS) + " | Regresiones |",
              "|---|---|---|" + "---|" * len(SECTIONS) + "---|"]
    for set_id, x in data["sets"].items():
        s = x["summary"]
        cells = " | ".join(f"{s[k]['found']}/{s[k]['expected']} (+{s[k]['new']})" for k in SECTIONS)
        regressions = sum(s[k]["regressions"] for k in SECTIONS)
        lines.append(f"| {set_id} | {x['rulebook']} | {s['out_found']}/{s['out_expected']} (+{s['out_new']}) "
                     f"| {cells} | {regressions} |")
    lines += ["", "Cada celda: esperados encontrados / esperados (+ nuevos).", ""]
    for set_id, x in data["sets"].items():
        d = x["detail"]
        lines += [f"## {set_id}", "", f"Clasificado {x['at']} con `{x['rulebook']}`; caso revisado con `{x['reviewed']}`.", ""]
        p = d["perimeter"]
        if p["missed"]:
            lines += ["- Debían quedar fuera y están dentro: " + " · ".join(f"«{q}»" for q in p["missed"])]
        if p["new"]:
            lines += ["- Fuera y el caso no lo dice: " + " · ".join(f"«{q}»" for q in p["new"])]
        if p["absent"]:
            lines += [f"- {p['absent']} preguntas del caso no están en la clasificación (otra captura)."]
        for section in SECTIONS:
            rows, new = d[section]["rows"], d[section]["new"]
            bad = [r for r in rows if (r["expected"] and (not r["appears"] or r["diff"])) or
                   (not r["expected"] and r["appears"])]
            if not bad and not new:
                continue
            lines += ["", f"**{NAMES[section]}**", ""]
            for r in bad:
                if not r["expected"]:
                    lines.append(f"- Regresión ({r['found']}): {r['label']}")
                elif not r["appears"]:
                    lines.append(f"- Falta: {r['label']}")
                else:
                    lines.append(f"- Difiere ({r['found']}: {'; '.join(r['diff'])}): {r['label']}")
            lines += [f"- Nuevo: {n}" for n in new]
        lines.append("")
    return "\n".join(lines) + "\n"
