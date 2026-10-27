"""Classification of the PAA questions of a set by an agent (T-040, T-041; D-091, D-094, D-097, D-099, D-100 to D-107).

The agent follows classifier/paa.md; this module prepares what it reads, checks what it writes and builds the
result. Standard library only: it runs on the host. In the set's folder (var/paa/sets/<set>/):
  classify/input.md · input.json     numbered questions, the catalog of the class (from the set's model, with the
                                     sources and contributions of each requirement), the daughters of each block, traits
  classify/output.json               the agent's classification
  classified.json · report.md        the result: each question with its classification and provenance, the criteria
                                     of choice, the candidate requirements with their sources, the revisions of
                                     existing requirements, the proposed contributions and the evidence of AC relevance
"""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

from .. import ROOT
from ..capture.files import now, read_json, write_json
from ..refs import RefsError, shopify_categories
from .store import SeedSet, StoreError, slug
from .text import norm

RULEBOOK = ROOT / "classifier/paa.md"
TRAITS = ROOT / "catalog/traits.json"
PERIMETERS = ("dentro", "fuera")
OBJECTS = ("clase", "marca", "tienda", "valorativa")
VERDICTS = ("genera", "cubierto", "no-genera")
CONDITIONS = ("C1", "C2", "C3", "C4")
VOTES = ("crítico", "principal", "complementario")
ACTIONS = ("separar", "sacar", "partir-por-tema", "reformular", "mover")
KINDS = ("precisión", "sustento")
ACS = ("Concreción", "Precisión", "Aplicabilidad", "Comparabilidad", "Fiabilidad", "Justificación")


def folder(seedset: SeedSet) -> Path:
    return seedset.dir / "classify"


def source(set_id: str, question: str) -> str:
    """Source of a requirement of origin «paa» (D-097): the question, by its normalised text."""
    return f"paa-q:{set_id}:{slug(question)}"


# ---------------------------------------------------------------- prepare
def model_path(seedset: SeedSet) -> Path:
    model = seedset.definition().get("model")
    if not model:
        raise StoreError(f"{seedset.file}: falta «model», el modelo de demanda del que salen las semillas")
    path = ROOT.parent / model
    path = path.with_suffix(".json") if path.suffix == ".md" else path
    if not path.exists():
        raise StoreError(f"no existe el modelo {path}")
    return path


def requirement(r: dict, block: str | None) -> dict:
    return {"id": r["id"], "block": block, "question": r["question"], "trait": r.get("trait"),
            "applicability": r.get("applicability"), "origin": r.get("origin"), "sources": r.get("sources") or [],
            "contributions": [c["contribution"] for c in r.get("resolving_info") or [] if c.get("contribution")],
            "excluded": bool(r.get("excluded"))}


def catalog(model: dict) -> list[dict]:
    """Every requirement of the class: the general layer (also what this offer does not activate: PAA is about the
    class), the blocks of the key and the inferred questions."""
    out = [requirement(r, block["id"]) for block in model.get("general", []) for r in block.get("requirements", [])]
    out += [requirement(r, block["id"]) for block in model.get("blocks", []) for r in block.get("requirements", [])]
    out += [requirement(r, r.get("block")) for r in model.get("inferred", [])]
    return out


def daughters(shopify_id: str | None) -> list[str] | None:
    """Names of the daughters of a category in the pinned Shopify taxonomy (D-043, criterion 4), or None."""
    if not shopify_id:
        return None
    try:
        cat = shopify_categories().get(shopify_id)
    except RefsError:  # references not downloaded: the agent goes without the daughters
        return None
    return [h["name"] for h in cat["children"]] if cat else None


def prepare(seedset: SeedSet) -> Path:
    data = read_json(seedset.dir / "questions.json")
    if not data or not data.get("questions"):
        raise StoreError(f"{seedset.id}: no hay preguntas consolidadas (paa run / paa questions)")
    mpath = model_path(seedset)
    model = read_json(mpath)
    blocks = [{"id": b["id"], "name": b.get("name"), "type": b.get("type"), "shopify": b.get("shopify"),
               "daughters": daughters(b.get("shopify"))} for b in model.get("blocks", [])]
    vocabulary = read_json(TRAITS, {}).get("vocabulary", {})
    questions = [{"n": i, "q": q["q"], "seeds": sorted({s["query"] for s in q["seeds"]})}
                 for i, q in enumerate(data["questions"], 1)]
    spec = {"set": seedset.id, "class": seedset.definition().get("class"), "at": now(),
            "questions_at": data.get("at"), "model": seedset.definition()["model"],
            "key": model.get("key"), "blocks": blocks, "catalog": catalog(model), "traits": sorted(vocabulary),
            "questions": questions}
    out = folder(seedset)
    write_json(out / "input.json", spec)
    (out / "input.md").write_text(render_input(spec, vocabulary), encoding="utf-8")
    return out


def cell(text) -> str:
    return str(text or "").replace("|", "/").replace("\n", " ")


def render_input(spec: dict, vocabulary: dict) -> str:
    lines = [f"# Preguntas PAA · {spec['set']}", "",
             f"- Clase: {spec['class']}",
             f"- Modelo: `{spec['model']}`",
             f"- Reglamento: `{RULEBOOK.relative_to(ROOT)}`",
             f"- Salida: `{(Path('var/paa/sets') / spec['set'] / 'classify/output.json')}`",
             "", "## Bloques de la clave", "",
             "De la madre a la hija, con sus hijas en la taxonomía (D-043, criterio 4: un requisito sube a la madre solo "
             "si vale para todas sus hijas).", "", "| bloque | nombre | hijas en la taxonomía |", "|---|---|---|"]
    for b in spec["blocks"]:
        kids = "—" if b["daughters"] is None else (", ".join(b["daughters"]) or "ninguna")
        lines.append(f"| `{b['id']}` | {cell(b['name'])} | {cell(kids)} |")
    lines += ["", "## Catálogo de la clase"]
    current = None
    for r in spec["catalog"]:
        if r["block"] != current:
            current = r["block"]
            lines += ["", f"### {current}", "", "| id | pregunta | rasgo | origen | fuentes | aportaciones |",
                      "|---|---|---|---|---|---|"]
        extra = " (excluido por relevancia)" if r.get("excluded") else ""
        applies = f" [{r['applicability']}]" if r.get("applicability") not in (None, "universal") else ""
        lines.append(f"| {r['id']} | {cell(r['question'])}{applies}{extra} | {cell(r['trait'])} | {cell(r['origin'])} "
                     f"| {cell(', '.join(r['sources']))} | {cell('; '.join(r['contributions']))} |")
    lines += ["", "## Rasgos", ""]
    lines += [f"- `{k}`: {cell(v.get('definition'))}" for k, v in sorted(vocabulary.items())]
    lines += ["", f"## Preguntas ({len(spec['questions'])})", "", "| n | pregunta | semillas |", "|---|---|---|"]
    lines += [f"| {q['n']} | {cell(q['q'])} | {cell(', '.join(q['seeds']))} |" for q in spec["questions"]]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- check
def ok_why_problems(where: str, entries, keys) -> list:
    if not isinstance(entries, dict):
        return [f"{where}: faltan {', '.join(keys)}"]
    out = []
    for k in keys:
        entry = entries.get(k)
        if not isinstance(entry, dict) or not isinstance(entry.get("ok"), bool) or not (entry.get("why") or "").strip():
            out.append(f"{where}: {k} necesita «ok» (true/false) y «why»")
    return out


def all_ok(entries, keys) -> bool:
    return isinstance(entries, dict) and all((entries.get(k) or {}).get("ok") is True for k in keys)


def check(spec: dict, output: dict) -> list[str]:
    """What is missing or wrong in the agent's output (classifier/paa.md, §4)."""
    problems = []
    req_ids = {r["id"] for r in spec["catalog"]}
    block_ids = {b["id"] for b in spec["blocks"]}
    expected = {q["n"] for q in spec["questions"]}
    criteria = {c.get("id"): c for c in output.get("criteria", [])}
    candidates = {c.get("id"): c for c in output.get("candidates", [])}
    revisions = output.get("revisions", [])
    for name, items, index in (("criterios", output.get("criteria", []), criteria),
                               ("candidatos", output.get("candidates", []), candidates)):
        if len(index) != len(items):
            problems.append(f"{name} con el id repetido")
    if len({r.get("id") for r in revisions}) != len(revisions):
        problems.append("revisiones con el id repetido")

    def bad_questions(where: str, ns) -> list:
        if not ns or not isinstance(ns, list):
            return [f"{where}: faltan las preguntas que lo apoyan"]
        return [f"{where}: la pregunta {n} no existe" for n in ns if n not in expected]

    entries = output.get("questions", [])
    seen = Counter(e.get("n") for e in entries)
    missing = sorted(expected - set(seen))
    if missing:
        problems.append(f"faltan {len(missing)} preguntas: {', '.join(map(str, missing[:20]))}")
    problems += [f"pregunta {n}: repetida" for n, k in seen.items() if k > 1]
    problems += [f"pregunta {n}: no existe" for n in seen if n not in expected]

    used_criteria, used_candidates = set(), set()
    for e in entries:
        where = f"pregunta {e.get('n')}"
        answered = e.get("answered_by") or []
        crit, cand, fails, obj = e.get("criterion"), e.get("candidate"), e.get("fails"), e.get("object")
        problems += [f"{where}: «{r}» no está en el catálogo de la clase" for r in answered if r not in req_ids]
        if crit:
            used_criteria.add(crit)
            if crit not in criteria:
                problems.append(f"{where}: el criterio «{crit}» no está en «criteria»")
        if cand:
            used_candidates.add(cand)
            if cand not in candidates:
                problems.append(f"{where}: el candidato «{cand}» no está en «candidates»")
        if fails not in (None, "C2", "C3", "C4"):
            problems.append(f"{where}: «fails» ha de ser C2, C3, C4 o null")
        if e.get("perimeter") not in PERIMETERS:
            problems.append(f"{where}: perímetro «{e.get('perimeter')}» no válido ({', '.join(PERIMETERS)})")
        elif e["perimeter"] == "fuera":
            if obj or answered or crit or cand or fails:
                problems.append(f"{where}: fuera del perímetro no lleva objeto, requisitos, criterio, candidato ni «fails»")
        elif obj not in OBJECTS:
            problems.append(f"{where}: objeto «{obj}» no válido ({', '.join(OBJECTS)})")
        elif obj == "valorativa":
            if not crit:
                problems.append(f"{where}: una valorativa lleva su criterio de elección")
            if cand or fails:
                problems.append(f"{where}: una valorativa no lleva «candidate» ni «fails» (salen de su criterio)")
        elif obj in ("marca", "tienda"):
            if cand:
                problems.append(f"{where}: una pregunta de {obj} no propone requisitos (D-099)")
        elif sum((bool(answered), bool(cand), bool(fails))) != 1:
            problems.append(f"{where}: una pregunta de clase lleva exactamente uno de «answered_by», «candidate» o «fails»")

    for cid, c in criteria.items():
        where = f"criterio «{cid}»"
        problems += ok_why_problems(where, c.get("conditions"), CONDITIONS)
        if not (c.get("name") or "").strip():
            problems.append(f"{where}: falta «name»")
        if cid not in used_criteria:
            problems.append(f"{where}: ninguna pregunta lo apoya")
        verdict = c.get("verdict")
        conds = c.get("conditions") if isinstance(c.get("conditions"), dict) else {}
        ok = {k: (conds.get(k) or {}).get("ok") for k in CONDITIONS}
        covered = c.get("covered_by") or []
        problems += [f"{where}: «{x}» de «covered_by» no es un requisito, un criterio ni un candidato"
                     for x in covered if x not in req_ids | set(criteria) | set(candidates)]
        for x in c.get("candidates") or []:
            used_candidates.add(x)
            if x not in candidates:
                problems.append(f"{where}: el candidato «{x}» no está en «candidates»")
        if verdict not in VERDICTS:
            problems.append(f"{where}: veredicto «{verdict}» no válido ({', '.join(VERDICTS)})")
        elif verdict == "genera" and (not all(ok.values()) or not c.get("candidates")):
            problems.append(f"{where}: «genera» exige C1–C4 cumplidas y al menos un candidato")
        elif verdict == "cubierto" and (ok["C1"] is not False or not covered):
            problems.append(f"{where}: «cubierto» exige C1 no cumplida y «covered_by»")
        elif verdict == "no-genera" and (ok["C1"] is not True or all(ok.values())):
            problems.append(f"{where}: «no-genera» exige C1 cumplida y alguna de C2–C4 no")
        if verdict != "genera" and c.get("candidates"):
            problems.append(f"{where}: solo un criterio que genera lleva candidatos")
        if c.get("intermediate") and verdict != "cubierto":
            problems.append(f"{where}: un criterio intermedio queda «cubierto» (D-104)")

    for r in revisions:
        where = f"revisión «{r.get('id')}»"
        if r.get("target") not in req_ids:
            problems.append(f"{where}: «{r.get('target')}» no está en el catálogo de la clase")
        if r.get("action") not in ACTIONS:
            problems.append(f"{where}: acción «{r.get('action')}» no válida ({', '.join(ACTIONS)})")
        if not (r.get("proposal") or "").strip():
            problems.append(f"{where}: falta «proposal»")
        if r.get("action") != "sacar" or r.get("questions"):    # taking a value out needs no demand (D-109)
            problems += bad_questions(where, r.get("questions"))
        for x in r.get("into") or []:
            used_candidates.add(x)
            if x not in candidates:
                problems.append(f"{where}: el candidato «{x}» no está en «candidates»")
        if r.get("action") == "separar":
            problems += ok_why_problems(where, r.get("tests"), ("a", "b"))
            if not all_ok(r.get("tests"), ("a", "b")) or not r.get("into"):
                problems.append(f"{where}: «separar» exige las dos pruebas (a y b) cumplidas y un candidato en «into» (D-103)")
        elif r.get("tests"):
            problems.append(f"{where}: solo «separar» lleva «tests»")

    traits = set(spec["traits"])
    for t in output.get("proposed_traits") or []:
        if (t.get("name") or "").strip() and (t.get("definition") or "").strip():
            traits.add(t["name"])
        else:
            problems.append(f"rasgo propuesto sin nombre o sin definición: {t}")
    for nid, c in candidates.items():
        where = f"candidato «{nid}»"
        problems += ok_why_problems(where, c.get("conditions"), CONDITIONS)
        if not all_ok(c.get("conditions"), CONDITIONS):
            problems.append(f"{where}: un candidato cumple C1–C4")
        q = (c.get("question") or "").strip()
        if not (q.startswith("¿") and q.endswith("?")):
            problems.append(f"{where}: la pregunta va entre ¿ y ?")
        if not (c.get("description") or "").strip():
            problems.append(f"{where}: falta «description» (D-092)")
        blocks = c.get("blocks") or []
        if not blocks:
            problems.append(f"{where}: faltan «blocks»")
        problems += [f"{where}: el bloque «{b}» no es de la clave ({', '.join(sorted(block_ids))})"
                     for b in blocks if b not in block_ids]
        if c.get("mirrors") and c["mirrors"] not in req_ids:
            problems.append(f"{where}: «mirrors» ({c['mirrors']}) no es un requisito del catálogo (D-109)")
        if c.get("trait") not in traits:
            problems.append(f"{where}: rasgo «{c.get('trait')}» fuera del vocabulario y de «proposed_traits»")
        if c.get("vote") not in VOTES:
            problems.append(f"{where}: voto «{c.get('vote')}» no válido")
        if c.get("from") not in ("criterio", "pregunta"):
            problems.append(f"{where}: «from» ha de ser «criterio» o «pregunta»")
        if not (c.get("applicability") or "").strip():
            problems.append(f"{where}: falta «applicability»")
        items = c.get("resolving_info") or []
        if not items or not all((i.get("contribution") or "").strip() and (i.get("component") or "").strip() for i in items):
            problems.append(f"{where}: «resolving_info» con al menos una aportación, cada una con su componente")
        if nid not in used_candidates:
            problems.append(f"{where}: ninguna pregunta, criterio ni revisión lo apoya")

    for i, c in enumerate(output.get("contributions") or [], 1):
        where = f"aportación {i}"
        if c.get("target") not in req_ids | set(candidates):
            problems.append(f"{where}: «{c.get('target')}» no es un requisito ni un candidato")
        if not (c.get("contribution") or "").strip() or not (c.get("component") or "").strip():
            problems.append(f"{where}: falta «contribution» o «component»")
        if c.get("kind") not in KINDS:
            problems.append(f"{where}: «kind» ha de ser {' o '.join(KINDS)}")
        problems += bad_questions(where, c.get("questions"))
    for i, a in enumerate(output.get("ac_evidence") or [], 1):
        where = f"pertinencia de AC {i}"
        if a.get("requirement") not in req_ids | set(candidates):
            problems.append(f"{where}: «{a.get('requirement')}» no es un requisito ni un candidato")
        if a.get("ac") not in ACS:
            problems.append(f"{where}: «{a.get('ac')}» no es un criterio de aceptación ({', '.join(ACS)})")
        if not (a.get("why") or "").strip():
            problems.append(f"{where}: falta «why»")
        problems += bad_questions(where, a.get("questions"))
    return problems


# ---------------------------------------------------------------- result
def sources_of(nid: str, output: dict) -> list[int]:
    """Questions that support a candidate: those that propose it, those of the criteria that generate it and those of
    the revisions that create it."""
    via = {c["id"] for c in output.get("criteria", []) if nid in (c.get("candidates") or [])}
    ns = {e["n"] for e in output["questions"] if e.get("candidate") == nid or (e.get("criterion") and e["criterion"] in via)}
    for r in output.get("revisions", []):
        if nid in (r.get("into") or []):
            ns |= set(r.get("questions") or [])
    return sorted(ns)


def kind_of(q: dict) -> str:
    """The type of a question, with the outcome of a class question."""
    if q.get("perimeter") == "fuera":
        return "fuera"
    if q.get("object") != "clase":
        return q.get("object")
    if q.get("answered_by"):
        return "clase · respondida"
    return "clase · candidata" if q.get("candidate") else f"clase · no genera ({q.get('fails')})"


def target(e: dict, criteria: dict) -> str:
    """Where a question ends up, in a few words (for the tables and the contrast)."""
    if e.get("perimeter") == "fuera":
        return "fuera"
    obj = e.get("object")
    if obj in ("marca", "tienda"):
        return obj + (f" → {', '.join(e['answered_by'])}" if e.get("answered_by") else "")
    if obj == "valorativa":
        c = criteria.get(e["criterion"], {})
        return f"criterio {e['criterion']}" + (f" → {', '.join(c['candidates'])}" if c.get("candidates") else "")
    if e.get("candidate"):
        return e["candidate"]
    if e.get("answered_by"):
        return ", ".join(e["answered_by"])
    return f"no genera ({e.get('fails')})"


def build(seedset: SeedSet, spec: dict, output: dict) -> dict:
    by_n = {e["n"]: e for e in output["questions"]}
    raw = {norm(q["q"]): q for q in read_json(seedset.dir / "questions.json")["questions"]}
    questions = []
    for q in spec["questions"]:
        e = by_n[q["n"]]
        questions.append({"n": q["n"], "q": q["q"], "source": source(seedset.id, q["q"]),
                          **{k: e.get(k) for k in ("perimeter", "object", "answered_by", "criterion", "candidate",
                                                   "fails", "note")},
                          "seeds": raw.get(norm(q["q"]), {}).get("seeds", [])})
    candidates = []
    for c in output.get("candidates", []):
        support = sources_of(c["id"], output)
        candidates.append({**c, "origin": "paa", "support": support,
                           "sources": [source(seedset.id, spec["questions"][n - 1]["q"]) for n in support]})
    return {"set": seedset.id, "class": spec["class"], "model": spec["model"], "at": now(),
            "rulebook": str(RULEBOOK.relative_to(ROOT)), "questions_at": spec["questions_at"],
            "questions": questions, "criteria": output.get("criteria", []), "candidates": candidates,
            **{k: output.get(k, []) for k in ("revisions", "contributions", "ac_evidence", "proposed_traits", "doubts")}}


def quoted(ns, by_n: dict) -> str:
    return " · ".join(f"«{by_n[n]['q']}»" for n in ns)


def report(result: dict, spec: dict, manual: list | None = None, manual_name: str = "",
           previous: dict | None = None, previous_name: str = "") -> str:
    qs, by_n = result["questions"], {q["n"]: q for q in result["questions"]}
    criteria = {c["id"]: c for c in result["criteria"]}
    reqs = {r["id"]: r for r in spec["catalog"]}
    cands = {c["id"]: c for c in result["candidates"]}
    yes = lambda c, k: "sí" if (c.get("conditions", {}).get(k) or {}).get("ok") else "**no**"
    named = lambda x: f"`{x}` «{reqs[x]['question']}»" if x in reqs else (f"{x} «{cands[x]['question']}»" if x in cands else x)
    lines = [f"# Clasificación de las preguntas PAA · {result['set']}", "",
             f"- Clase: {result['class']}", f"- Modelo: `{result['model']}`",
             f"- Reglamento: `{result['rulebook']}` · preguntas consolidadas el {result['questions_at']}",
             f"- Clasificado: {result['at']}", "", "## Reparto", ""]
    kinds = Counter(kind_of(q) for q in qs)
    lines += ["| Tipo | Preguntas |", "|---|---|"]
    lines += [f"| {k} | {v} |" for k, v in sorted(kinds.items())]
    lines += [f"| **Total** | **{len(qs)}** |", ""]

    lines += ["## Criterios de elección", "",
              "| Criterio | Preguntas | C1 | C2 | C3 | C4 | Veredicto | Cubierto por · candidatos |", "|---|---|---|---|---|---|---|---|"]
    support = Counter(q["criterion"] for q in qs if q["criterion"])
    ordered = sorted(result["criteria"], key=lambda c: -support[c["id"]])
    for c in ordered:
        mark = " · intermedio" if c.get("intermediate") else ""
        lines.append(f"| {c['name']} (`{c['id']}`) | {support[c['id']]} | {yes(c, 'C1')} | {yes(c, 'C2')} | {yes(c, 'C3')} "
                     f"| {yes(c, 'C4')} | {c['verdict']}{mark} | {', '.join(c.get('covered_by') or c.get('candidates') or [])} |")
    lines.append("")
    for c in ordered:
        lines += [f"### {c['name']} · {c['verdict']}" + (" (intermedio)" if c.get("intermediate") else ""), ""]
        lines += [f"- {k}: {(c['conditions'].get(k) or {}).get('why', '')}" for k in CONDITIONS]
        lines += ["", "Preguntas: " + quoted([q["n"] for q in qs if q["criterion"] == c["id"]], by_n), ""]

    lines += ["## Requisitos candidatos", "",
              "Origen «paa» (D-097, D-099). La importancia la deciden las reglas del entrenamiento; el voto es orientativo.", ""]
    for c in result["candidates"]:
        crit = [k for k, v in criteria.items() if c["id"] in (v.get("candidates") or [])]
        revs = [r["id"] for r in result["revisions"] if c["id"] in (r.get("into") or [])]
        origin = ", ".join(filter(None, ["criterio " + ", ".join(crit) if crit else "",
                                         "revisión " + ", ".join(revs) if revs else ""])) or "preguntas de clase"
        lines += [f"### {c['id']} · {c['question']}", "",
                  f"- Bloques: {', '.join(f'`{b}`' for b in c['blocks'])} · rasgo `{c['trait']}` · voto {c['vote']} · "
                  f"aplicabilidad: {c['applicability']}",
                  f"- Sale de: {origin} ({c['from']})" + (f" · reproduce la lista {named(c['mirrors'])}" if c.get("mirrors") else ""),
                  f"- Descripción: {c.get('description', '')}"]
        lines += [f"- {k}: {(c['conditions'].get(k) or {}).get('why', '')}" for k in CONDITIONS]
        lines += [f"- Motivo: {c.get('rationale', '')}",
                  "- Información resolutiva: " + "; ".join(f"{i['contribution']} [{i['component']}]" for i in c["resolving_info"]),
                  f"- Apoyo ({len(c['support'])}): " + quoted(c["support"], by_n), ""]

    if result["revisions"]:
        lines += ["## Revisiones de requisitos existentes", ""]
        for r in result["revisions"]:
            lines += [f"### {r['id']} · {r['action']} {named(r['target'])}", "", f"- Propuesta: {r['proposal']}"]
            if r.get("into"):
                lines.append("- Crea: " + ", ".join(named(x) for x in r["into"]))
            if r.get("tests"):
                lines += [f"- Prueba {k}: {r['tests'][k]['why']}" for k in ("a", "b")]
            qs_r = r.get("questions") or []
            lines += [f"- Apoyo ({len(qs_r)}): " + (quoted(qs_r, by_n) or "ninguna pregunta: se justifica por el tema de la lista"), ""]

    if result["contributions"]:
        lines += ["## Aportaciones propuestas", "", "| Requisito | Aportación | Componente | Tipo | Preguntas |", "|---|---|---|---|---|"]
        lines += [f"| {named(c['target'])} | {cell(c['contribution'])} | {cell(c['component'])} | {c['kind']} "
                  f"| {cell(quoted(c['questions'], by_n))} |" for c in result["contributions"]]
        lines.append("")

    if result["ac_evidence"]:
        lines += ["## Pertinencia de los criterios de aceptación (propuesta, OQ-59)", "",
                  "| Requisito | AC | Por qué | Preguntas |", "|---|---|---|---|"]
        lines += [f"| {named(a['requirement'])} | {a['ac']} | {cell(a['why'])} | {len(a['questions'])}: "
                  f"{cell(quoted(a['questions'][:3], by_n))}{' …' if len(a['questions']) > 3 else ''} |"
                  for a in result["ac_evidence"]]
        lines.append("")

    if result["proposed_traits"]:
        lines += ["## Rasgos propuestos", ""] + [f"- `{t['name']}`: {t['definition']}" for t in result["proposed_traits"]] + [""]

    confirmed = Counter(r for q in qs for r in q["answered_by"] or [])
    lines += ["## Requisitos del catálogo que PAA confirma", "",
              "| Requisito | Pregunta | Preguntas PAA | Origen |", "|---|---|---|---|"]
    for rid, k in sorted(confirmed.items(), key=lambda x: (-x[1], x[0])):
        r = reqs[rid]
        mark = " → «paa» (D-097)" if rid.startswith("inf/") else ""
        lines.append(f"| `{rid}` | {cell(r['question'])} | {k} | {r.get('origin')}{mark} |")
    lines.append("")

    nogen = [q for q in qs if q["object"] == "clase" and q["fails"]]
    if nogen:
        lines += ["## Preguntas de clase que no generan", ""]
        for cond in ("C2", "C3", "C4"):
            group = [q["n"] for q in nogen if q["fails"] == cond]
            if group:
                lines += [f"- **{cond}** ({len(group)}): " + quoted(group, by_n)]
        lines.append("")

    if previous is not None:
        lines += against_previous(result, previous, previous_name)
    if manual is not None:
        lines += contrast(result, manual, manual_name)

    if result.get("usage"):
        u = result["usage"]
        lines += ["## Consumo del agente", "",
                  f"{u['tokens']} tokens (entrada {u['input']}, escritura de caché {u['cache_write']}, lectura de caché "
                  f"{u['cache_read']}, salida {u['output']}) en {u['requests']} peticiones y {u['duration_ms'] // 1000} s.", ""]

    if result["doubts"]:
        lines += ["## Dudas del agente", ""] + [f"- {d}" for d in result["doubts"]] + [""]
    return "\n".join(lines) + "\n"


def against_previous(result: dict, previous: dict, name: str) -> list[str]:
    """This classification against an earlier one of the same set (another rulebook or another run)."""
    old = {norm(q["q"]): q for q in previous["questions"]}
    pairs = [(old[norm(q["q"])], q) for q in result["questions"] if norm(q["q"]) in old]
    before, after = Counter(kind_of(q) for q in previous["questions"]), Counter(kind_of(q) for q in result["questions"])
    lines = ["## Contraste con la clasificación anterior", "",
             f"`{name}` (reglamento `{previous.get('rulebook')}`, {previous.get('at')}): {len(pairs)} preguntas comunes.", "",
             "| Tipo | Antes | Ahora |", "|---|---|---|"]
    lines += [f"| {k} | {before.get(k, 0)} | {after.get(k, 0)} |" for k in sorted(set(before) | set(after))]
    moves: dict[tuple, list] = {}
    for o, q in pairs:
        if kind_of(o) != kind_of(q):
            moves.setdefault((kind_of(o), kind_of(q)), []).append(q["q"])
    if moves:
        lines += ["", "Cambios de tipo:", ""]
        for (a, b), texts in sorted(moves.items(), key=lambda x: -len(x[1])):
            lines.append(f"- {a} → {b} ({len(texts)}): " + " · ".join(f"«{t}»" for t in texts[:4]) +
                         (" …" if len(texts) > 4 else ""))
    lines += ["", "Criterios: antes " + ", ".join(f"{c['id']} ({c['verdict']})" for c in previous["criteria"]) + ".",
              "", "Criterios: ahora " + ", ".join(f"{c['id']} ({c['verdict']})" for c in result["criteria"]) + ".", "",
              "Candidatos antes: " + " · ".join(f"{c['id']} {c['question']}" for c in previous["candidates"]), "",
              "Candidatos ahora: " + " · ".join(f"{c['id']} {c['question']}" for c in result["candidates"]), ""]
    return lines


def contrast(result: dict, manual: list, name: str) -> list[str]:
    """The agent's classification against a manual one ([{q, code}]) on the questions both have."""
    criteria = {c["id"]: c for c in result["criteria"]}
    ours = {norm(q["q"]): q for q in result["questions"]}
    common = [(m, ours[norm(m["q"])]) for m in manual if norm(m["q"]) in ours]
    lines = ["## Contraste con la clasificación manual", "",
             f"`{name}`: {len(manual)} preguntas; {len(common)} comunes con este conjunto "
             f"(de {len(result['questions'])}). Cada código manual, con el tipo y el destino que les da el agente.", "",
             "| Código manual | Comunes | Fuera | " + " | ".join(o.capitalize() for o in OBJECTS) +
             " | Destinos del agente (preguntas) |",
             "|---|---|---|---|---|---|---|---|"]
    by_code: dict[str, list] = {}
    for m, q in common:
        by_code.setdefault(m["code"], []).append(q)
    for code, group in sorted(by_code.items(), key=lambda x: -len(x[1])):
        kinds = Counter("fuera" if q["perimeter"] == "fuera" else q["object"] for q in group)
        dest = Counter(target(q, criteria) for q in group).most_common(4)
        lines.append(f"| {code} | {len(group)} | " + " | ".join(str(kinds.get(k, 0)) for k in ("fuera",) + OBJECTS) +
                     " | " + "; ".join(f"{d} ({k})" for d, k in dest) + " |")
    return lines + [""]


# ---------------------------------------------------------------- commands
def load(seedset: SeedSet) -> tuple[dict, dict]:
    spec = read_json(folder(seedset) / "input.json")
    if not spec:
        raise StoreError(f"{seedset.id}: falta la entrada; ejecuta «paa classify prepare {seedset.id}»")
    output = read_json(folder(seedset) / "output.json")
    if output is None:
        raise StoreError(f"{seedset.id}: falta la salida del agente ({folder(seedset) / 'output.json'})")
    return spec, output


def finish(seedset: SeedSet, compare: Path | None = None, previous: Path | None = None) -> dict:
    spec, output = load(seedset)
    problems = check(spec, output)
    if problems:
        raise StoreError(f"{seedset.id}: la salida tiene {len(problems)} problemas; ejecuta «paa classify check»")
    result = build(seedset, spec, output)
    if (folder(seedset) / "usage.json").exists():
        result["usage"] = read_json(folder(seedset) / "usage.json")
    manual = json.loads(compare.read_text(encoding="utf-8")) if compare else None
    before = read_json(previous) if previous else None
    if compare:
        result["contrast"] = str(compare)
    if previous:
        result["previous"] = str(previous)
    write_json(seedset.dir / "classified.json", result)
    (seedset.dir / "report.md").write_text(report(result, spec, manual, str(compare or ""), before, str(previous or "")),
                                           encoding="utf-8")
    return result
