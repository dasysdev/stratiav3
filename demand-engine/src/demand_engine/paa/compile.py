"""The PAA pass into the catalog (T-092; D-178, D-180): paa compile [SET ...].

First the control of all the case sets decides (control.decide, D-180). If it accepts, what each classified set
holds enters the catalog, with origin «paa» and as a new version of each block it touches (D-178):
  candidates          a new requirement in each of its blocks, its questions as sources
  confirmed inferred  an inferred question of the set's model that a question answers, if no candidate revises it
                      (mirrors): a new requirement in its block, with the questions that answer it as sources (D-097)
  contributions       added to the resolving information of their target requirement (D-101)
The literal text of each question cited goes to catalog/paa-questions.json (D-178): var/ is disposable.
What is already in the block (the same question, or the same contribution) does not enter twice. A target that the
catalog lacks (the general layer, a block that is not there) is reported and left out.
The structural revisions are not written here: the taxo compilation reads them from classified.json (D-179).
"""
from __future__ import annotations

from capture.files import now, read_json, write_json

from .. import ROOT
from ..demand import catalog
from . import control
from .store import var_root
from .text import norm

def model_of(result: dict) -> dict:
    """The model the set was classified against (its inferred questions)."""
    path = ROOT.parent / result["model"]
    return read_json(path.with_name(path.name.replace(".model.md", ".model.json")), {})


def entries(result: dict, model: dict) -> list[dict]:
    """What a classified set brings to the catalog, in order: requirements (candidates and confirmed inferred
    questions) and contributions. Each with the tags of its questions."""
    tag = {q["n"]: q["source"] for q in result["questions"]}
    proposed = {t["name"]: t for t in result.get("proposed_traits") or []}
    out = []
    for c in result["candidates"]:
        for block in c["blocks"]:
            out.append({"kind": "requirement", "block": block, "from": c["id"], "sources": c["sources"],
                        "requirement": {k: c.get(k) for k in ("question", "dimension", "trait", "entity", "applicability",
                                                              "rationale", "resolving_info")},
                        "vote": c.get("vote")})
    revised = {c.get("mirrors") for c in result["candidates"]}
    for r in model.get("inferred", []):
        answered = [q["source"] for q in result["questions"] if r["id"] in (q.get("answered_by") or [])]
        if answered and r["id"] not in revised and r.get("block"):
            out.append({"kind": "requirement", "block": r["block"], "from": r["id"], "sources": answered,
                        "requirement": {k: r.get(k) for k in ("question", "dimension", "trait", "entity",
                                                              "applicability", "rationale", "resolving_info")},
                        "vote": r.get("vote")})
    for e in out:  # a trait outside the vocabulary goes with its proposal, as in a drafted block (D-056)
        if e["requirement"].get("trait") in proposed:
            e["proposed_trait"] = proposed[e["requirement"]["trait"]]
    for c in result["contributions"]:
        out.append({"kind": "contribution", "target": c["target"], "sources": [tag[n] for n in c.get("questions", [])],
                    "contribution": {"contribution": c["contribution"], "component": c["component"], "kind": c["kind"]}})
    return out


def apply(blocks: dict, set_id: str, items: list[dict], rules: dict, src_traits: dict, voted: dict) -> dict:
    """Add the entries of a set to the blocks (in memory). {"added": [...], "skipped": [...], "touched": {ids}}."""
    by_req = {r["id"]: (b, r) for b in blocks.values() for r in b["requirements"]}
    added, skipped, touched = [], [], set()
    for e in items:
        if e["kind"] == "requirement":
            b = blocks.get(e["block"])
            if not b:
                skipped.append(f"{e['from']}: el bloque {e['block']} no está en el catálogo")
                continue
            q = e["requirement"]["question"]
            if any(norm(r["question"]) == norm(q) or (r.get("origin") == "paa" and sorted(r.get("sources", [])) ==
                                                      sorted(e["sources"])) for r in b["requirements"]):
                continue
            r = {"id": catalog.next_requirement_id(b), **{k: v for k, v in e["requirement"].items() if k != "resolving_info"},
                 "origin": "paa", "sources": sorted(e["sources"])}
            r["applicability"] = r.get("applicability") or "universal"
            r["rationale"] = f"{r.get('rationale') or ''} Pasada de PAA, conjunto {set_id} ({e['from']}; D-178).".strip()
            r["seed_importance"] = e["vote"] if e["vote"] in catalog.LEVELS else "complementario"
            r["resolving_info"] = [{"contribution": c["contribution"], "component": c["component"], "origin": "paa",
                                    "support": r["sources"]} for c in e["requirement"].get("resolving_info") or []]
            trait, _ = catalog.requirement_trait(r, src_traits, voted)
            level, rule = catalog.resolve(trait, [b["shopify"]], rules, r["sources"], r["id"])
            r["trait"], r["importance"], r["rule"] = trait, level or r["seed_importance"], rule or catalog.NO_RULE
            b["requirements"].append(r)
            t = e.get("proposed_trait")
            if t and t["name"] not in {x.get("name") for x in b.get("proposed_traits", [])}:
                b.setdefault("proposed_traits", []).append(t)
            by_req[r["id"]] = (b, r)
            added.append(f"{r['id']} ← {e['from']}: {q}")
            touched.add(b["id"])
        else:
            if e["target"] not in by_req:
                skipped.append(f"aportación a {e['target']}: el requisito no está en un bloque del catálogo")
                continue
            b, r = by_req[e["target"]]
            c = e["contribution"]
            if any(norm(x["contribution"]) == norm(c["contribution"]) for x in r.setdefault("resolving_info", [])):
                continue
            r["resolving_info"].append({**c, "origin": "paa", "support": sorted(e["sources"])})
            added.append(f"{r['id']} · {c['kind']}: {c['contribution']}")
            touched.add(b["id"])
    return {"added": added, "skipped": skipped, "touched": touched}


def cited(blocks: dict) -> set[str]:
    """Every PAA question that the catalog cites: sources of the requirements and support of the contributions."""
    out = set()
    for b in blocks.values():
        for r in b["requirements"]:
            out |= {s for s in r.get("sources", []) if s.startswith("paa-q:")}
            for c in r.get("resolving_info") or []:
                out |= {s for s in c.get("support") or [] if s.startswith("paa-q:")}
    return out


def run(set_ids: list[str]) -> dict:
    out, data = control.run(control.case_ids())
    decision = data["decision"]
    passed = {"at": now(), "control": str(out), "decision": decision, "sets": {}}
    if not decision["accepted"]:
        return passed
    blocks, rules = catalog.load_blocks(), catalog.load_rules()
    src_traits, voted = catalog.trait_index()
    texts = read_json(catalog.PAA_QUESTIONS, {})
    touched = set()
    for set_id in set_ids:
        result = read_json(var_root() / "sets" / set_id / "classified.json")
        if not result:
            passed["sets"][set_id] = {"added": [], "skipped": ["sin classified.json"]}
            continue
        done = apply(blocks, set_id, entries(result, model_of(result)), rules, src_traits, voted)
        touched |= done.pop("touched")
        passed["sets"][set_id] = done
        for q in result["questions"]:
            texts.setdefault(q["source"], {"q": q["q"], "set": set_id, "at": result.get("questions_at")})
    for bid in sorted(touched):
        b = blocks[bid]
        b["version"] = str(int(float(b.get("version", "0"))) + 1)
        catalog.save_block(b)
    need = cited(blocks)
    write_json(catalog.PAA_QUESTIONS, {k: texts[k] for k in sorted(need) if k in texts})
    passed["touched"] = sorted(touched)
    write_json(control.ACCEPTED, {"at": passed["at"], "control": str(out), "sets": {k: v["summary"] for k, v in
               data["sets"].items()}, "total": data["total"], "entered": passed["sets"]})
    write_json(var_root() / "compile" / (passed["at"].replace(":", "")[:17] + ".json"), passed)
    return passed


def classified_ids() -> list[str]:
    root = var_root() / "sets"
    return sorted(p.parent.name for p in root.glob("*/classified.json")) if root.exists() else []
