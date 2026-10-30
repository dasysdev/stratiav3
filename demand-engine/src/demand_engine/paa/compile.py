"""The PAA pass into the catalog (T-092; D-178, D-180): paa compile [SET ...] [--duplicates].

First the possible duplicates between sets need a decision (T-110, D-178): two requirement entries (candidates or
confirmed inferred questions) of different sets, with the same trait, that enter the same block or a block and one of
its ancestors in the catalog (the Shopify tree). The pairs that share an entry make one group; the entries of one set
are not compared. A reviewer decides each group in training/reports/paa/merges.json:
  {"groups": [{"entries": ["SET:N1@BLOCK", ...], "same": true | false, "keep": "SET:N1@BLOCK", "reason": "..."}]}
If «same», only «keep» enters, with the sources of all the entries, and the others are merged into it; «keep» must be
in the highest block (the block of every entry, or an ancestor of it). A group of several facts is split into several
decisions whose entries cover the group once. If a group lacks a valid decision, nothing is written: the pending
groups go to their draft, var/paa/compile/duplicates.json.
Then the control of all the case sets decides (control.decide, D-180). If it accepts, what each classified set
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

from pathlib import Path

from capture.files import now, read_json, write_json

from .. import ROOT
from ..demand import catalog
from . import control
from .store import var_root
from .text import norm

MERGES = ROOT / "training/reports/paa/merges.json"  # the reviewer's decisions on the possible duplicates: versioned


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


def key(set_id: str, e: dict) -> str:
    """The name of a requirement entry in the decisions: SET:N1@BLOCK."""
    return f"{set_id}:{e['from']}@{e['block']}"


def above(a: dict, b: dict) -> bool:
    """Block a is block b or one of its ancestors in the catalog (the Shopify tree)."""
    return a["id"] == b["id"] or bool(a.get("shopify") and b.get("shopify")) and catalog.under(b["shopify"], a["shopify"])


def possible(items: dict, blocks: dict, results: dict) -> list[dict]:
    """The possible duplicates between sets (T-110): requirement entries of different sets with the same trait, in the
    same block or in a block and one of its ancestors. Pairs that share an entry make one group, highest block first."""
    found = [(s, e) for s, es in items.items() for e in es if e["kind"] == "requirement" and e["block"] in blocks]
    head = list(range(len(found)))

    def root(i: int) -> int:
        while head[i] != i:
            i = head[i]
        return i

    for i, (s, e) in enumerate(found):
        for j, (t, f) in enumerate(found[:i]):
            a, b, trait = blocks[e["block"]], blocks[f["block"]], e["requirement"].get("trait")
            if s != t and trait and trait == f["requirement"].get("trait") and (above(a, b) or above(b, a)):
                head[root(i)] = root(j)
    members: dict[int, list] = {}
    for i in range(len(found)):
        members.setdefault(root(i), []).append(found[i])
    texts = {s: {q["source"]: q["q"] for q in r["questions"]} for s, r in results.items() if r}
    groups = []
    for rows in members.values():
        if len(rows) < 2:
            continue
        rows.sort(key=lambda x: (catalog.depth(blocks[x[1]["block"]].get("shopify") or ""), key(*x)))
        groups.append({"trait": rows[0][1]["requirement"]["trait"], "entries": [key(*x) for x in rows],
                       "detail": {key(s, e): {"block": e["block"], "question": e["requirement"]["question"],
                                              "paa": [texts[s].get(t, t) for t in e["sources"]]} for s, e in rows}})
    return sorted(groups, key=lambda g: (catalog.depth(blocks[g["detail"][g["entries"][0]]["block"]].get("shopify") or ""),
                                         g["entries"][0]))


def problems(group: dict, mine: list[dict], blocks: dict) -> list[str]:
    """What the decisions on a group lack or get wrong (empty: decided). They must cover each entry once."""
    if not mine:
        return ["sin decisión"]
    members = set(group["entries"])
    block = {k: blocks[group["detail"][k]["block"]] for k in members}
    out, covered = [], []
    for d in mine:
        es = d.get("entries") or []
        covered += es
        if set(es) - members:
            out.append(f"entradas fuera del grupo: {', '.join(sorted(set(es) - members))}")
        if not isinstance(d.get("same"), bool):
            out.append(f"sin decisión: {', '.join(es)}")
            continue
        if not str(d.get("reason") or "").strip():
            out.append(f"sin motivo: {', '.join(es)}")
        if not d["same"]:
            continue
        keep = d.get("keep")
        if len(set(es)) < 2:
            out.append(f"el mismo hecho necesita dos entradas: {', '.join(es)}")
        elif keep not in es or keep not in members:
            out.append(f"«keep» no es una entrada de la decisión: {keep}")
        elif not all(above(block[keep], block[k]) for k in es if k in members):
            out.append(f"{keep} no está en el bloque más alto de lo que funde (el bloque de cada entrada o su antepasado)")
    twice = sorted({k for k in covered if covered.count(k) > 1})
    if twice:
        out.append(f"en dos decisiones: {', '.join(twice)}")
    missing = [k for k in group["entries"] if k not in covered]
    if missing:
        out.append(f"sin decisión: {', '.join(missing)}")
    return out


def review(groups: list[dict], decisions: list[dict], blocks: dict) -> list[dict]:
    """Each group with the decisions of the reviewer that cite one of its entries, and their problems."""
    for g in groups:
        mine = [d for d in decisions if set(d.get("entries") or []) & set(g["entries"])]
        g["decisions"] = [{k: d.get(k) for k in ("entries", "same", "keep", "reason")} for d in mine]
        g["problems"] = problems(g, mine, blocks)
    return groups


def pending(dup: dict) -> list[dict]:
    return [g for g in dup["groups"] if g["problems"]]


def draft_path() -> Path:
    return var_root() / "compile" / "duplicates.json"


def prepare(set_ids: list[str]) -> tuple[dict, dict, dict, dict]:
    """(blocks, classified sets, their entries, their possible duplicates). The pending groups go to their draft, in
    var/: nothing else is written."""
    blocks = catalog.load_blocks()
    results = {s: read_json(var_root() / "sets" / s / "classified.json") for s in set_ids}
    items = {s: entries(r, model_of(r)) for s, r in results.items() if r}
    decisions = (read_json(MERGES, {}) or {}).get("groups", [])
    groups = review(possible(items, blocks, results), decisions, blocks)
    cited = {k for g in groups for k in g["entries"]}
    dup = {"groups": groups, "orphans": [d for d in decisions if not set(d.get("entries") or []) & cited],
           "draft": str(draft_path())}
    write_json(draft_path(), {"at": now(), "decide": "training/reports/paa/merges.json (README de PAA, Posibles duplicados)",
                              "groups": [{"entries": g["entries"], "same": None, "keep": None, "reason": "",
                                          "trait": g["trait"], "problems": g["problems"], "detail": g["detail"]}
                                         for g in pending(dup)]})
    return blocks, results, items, dup


def merge(items: dict, groups: list[dict]) -> None:
    """The decided merges, on the entries of the sets (in place): «keep» takes the sources of every entry it merges;
    the others go «into» it and do not enter."""
    by_key = {key(s, e): e for s, es in items.items() for e in es if e["kind"] == "requirement"}
    for g in groups:
        for d in g["decisions"]:
            if not d["same"]:
                continue
            keep, others = by_key[d["keep"]], [k for k in d["entries"] if k != d["keep"]]
            keep["sources"] = sorted(set(keep["sources"]).union(*(by_key[k]["sources"] for k in others)))
            keep["merged"] = others
            for k in others:
                by_key[k]["into"] = d["keep"]


def apply(blocks: dict, set_id: str, items: list[dict], rules: dict, src_traits: dict, voted: dict) -> dict:
    """Add the entries of a set to the blocks (in memory). {"added", "skipped", "merged": [...], "touched": {ids}}."""
    by_req = {r["id"]: (b, r) for b in blocks.values() for r in b["requirements"]}
    added, skipped, merged, touched = [], [], [], set()
    for e in items:
        if e["kind"] == "requirement":
            if e.get("into"):  # the reviewer merged it into another entry (T-110)
                merged.append(f"{e['from']}@{e['block']}: fundido en {e['into']}")
                continue
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
            note = f"; fundido con {', '.join(e['merged'])}" if e.get("merged") else ""
            r["rationale"] = f"{r.get('rationale') or ''} Pasada de PAA, conjunto {set_id} ({e['from']}{note}; D-178).".strip()
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
            added.append(f"{r['id']} ← {e['from']}: {q}" + (f" (fundido con {', '.join(e['merged'])})" if note else ""))
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
    return {"added": added, "skipped": skipped, "merged": merged, "touched": touched}


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
    blocks, results, items, dup = prepare(set_ids)
    passed = {"at": now(), "duplicates": dup, "sets": {}}
    if pending(dup):  # a possible duplicate without a decision: the control does not run and nothing enters
        return passed
    out, data = control.run(control.case_ids())
    decision = data["decision"]
    passed.update(control=str(out), decision=decision)
    if not decision["accepted"]:
        return passed
    rules = catalog.load_rules()
    src_traits, voted = catalog.trait_index()
    texts = read_json(catalog.PAA_QUESTIONS, {})
    merge(items, dup["groups"])
    touched = set()
    for set_id in set_ids:
        result = results[set_id]
        if not result:
            passed["sets"][set_id] = {"added": [], "skipped": ["sin classified.json"], "merged": []}
            continue
        done = apply(blocks, set_id, items[set_id], rules, src_traits, voted)
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
    if not touched:  # nothing new enters: the accepted pass and what entered with it stay (D-180)
        return passed
    write_json(control.ACCEPTED, {"at": passed["at"], "control": str(out), "sets": {k: v["summary"] for k, v in
               data["sets"].items()}, "total": data["total"], "entered": passed["sets"]})
    write_json(var_root() / "compile" / (passed["at"].replace(":", "")[:17] + ".json"), passed)
    return passed


def classified_ids() -> list[str]:
    root = var_root() / "sets"
    return sorted(p.parent.name for p in root.glob("*/classified.json")) if root.exists() else []
