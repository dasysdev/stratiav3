"""The PAA phase of an execution in its model (D-224): model assemble OUTPUT.json --paa SET.

What the classification of the set of the model's key proposes enters the model of that execution as provisional,
«no compilado», out of its key, like an inferred question (D-041), and goes to the queue with the rest of what was used
without compiling (D-044, D-045). The compiled catalog does not change: the PAA pass with the control is still the only
way into it (D-178, D-180).
  candidates      a requirement of origin «paa» in each block of the model that the candidate goes to (paa/N1/<block>);
                  importance from the rules or, without a rule, the agent's vote, provisional (D-045, D-094). One that
                  the block already has (the same question, or the same questions: a compiled PAA pass) does not enter
  confirmations   the PAA questions that answer a requirement or an inferred question of the model («paa_confirmed»)
  contributions   added to the resolving information of their requirement, with origin «paa» and their questions
  hints           added to the hints of their requirement, with origin «paa» and without PV-n (the system numbers a
                  hint when it keeps it)
  marks           the comparison mark of a requirement without one; one that contradicts the mark of the requirement
                  is a doubt: «se compara» while it is resolved (D-139)
Each of them carries «status»: «no compilado». A target that the model does not have (another block, a requirement
excluded in the class, an inferred question of another model) is left out and reported, and so are the
specializations and revisions that PAA proposes. The set must be of the model's key (D-116) and its classification
must cover every question it has.
Standard library only: it runs on the host.
"""
from __future__ import annotations

from pathlib import Path

from capture.files import read_json

from .. import ROOT
from ..demand.catalog import UNCOMPILED
from .compile import model_of
from .seeds import key_of
from .store import SeedSet, StoreError
from .text import norm

DOUBT = "Duda (D-139): {now} y PAA dice «{paa}»; se compara mientras se resuelve."


def load(set_id: str) -> dict:
    """The classified set: {set, result, set_model, path}. Its classification must cover all its questions."""
    seedset = SeedSet(set_id)
    path = seedset.dir / "classified.json"
    result = read_json(path)
    if not result:
        raise StoreError(f"{set_id}: no está clasificado (falta {path}; /paa-classify {set_id})")
    asked = {norm(q["q"]) for q in read_json(seedset.dir / "questions.json", {}).get("questions", [])}
    missing = asked - {norm(q["q"]) for q in result["questions"]}
    if missing:
        raise StoreError(f"{set_id}: la clasificación no tiene {len(missing)} preguntas de questions.json: clasifícalo de "
                         "nuevo (/paa-classify)")
    return {"set": seedset, "result": result, "set_model": model_of(result), "path": path}


def known(host: dict, c: dict) -> str | None:
    """The requirement of the block that is already the candidate: the same question, or a requirement of origin «paa»
    with its questions (a compiled PAA pass, D-178). None if there is none."""
    return next((r["id"] for r in host["requirements"] + host.get("excluded", [])
                 if norm(r["question"]) == norm(c["question"]) or
                 (r.get("origin") == "paa" and sorted(r.get("sources", [])) == sorted(c.get("sources", [])))), None)


def candidates(phase: dict, blocks: list, entry) -> tuple[list, list]:
    """The requirements of the candidates in the blocks of the model, and what is left out. `entry(r, host)` builds the
    requirement of the model as assemble does (relevance, importance from the rules or the vote). A candidate the block
    already has is that requirement for its hints and marks (phase["compiled"])."""
    result, hosts = phase["result"], {b["id"]: b for b in blocks}
    out, skipped = [], []
    phase["compiled"] = {}
    for c in result.get("candidates", []):
        for bid in c.get("blocks", []):
            host = hosts.get(bid)
            if host is None:
                skipped.append(f"candidato {c['id']} → {bid}: el bloque no está en el modelo")
                continue
            same = known(host, c)
            if same:
                phase["compiled"].setdefault(c["id"], []).append(same)
                skipped.append(f"candidato {c['id']} → {bid}: el bloque ya lo tiene ({same}); no se repite")
                continue
            r = {"id": f"paa/{c['id']}/{bid.split('.', 1)[-1]}", "origin": "paa", "sources": sorted(c.get("sources", [])),
                 **{k: c.get(k) for k in ("question", "dimension", "entity", "trait", "vote", "applicability")},
                 **({"description": c["description"]} if c.get("description") else {}),
                 "resolving_info": [{"contribution": x["contribution"], "component": x["component"], "origin": "paa",
                                     "support": sorted(c.get("sources", [])), "status": UNCOMPILED}
                                    for x in c.get("resolving_info") or []]}
            e = entry(r, host)
            e.update({"block": bid, "set": result["set"], "candidate": c["id"], "status": UNCOMPILED,
                      "rationale": c.get("rationale"), **({"mirrors": c["mirrors"]} if c.get("mirrors") else {})})
            out.append(e)
    return out, skipped


def label(mark: dict) -> str:
    case = f" ({mark['case']})" if mark.get("case") else ""
    return "se compara" if mark.get("mark") == "sí" else f"no se compara{case}"


def apply(model: dict, phase: dict, reqs: list, skipped: list) -> dict:
    """Put the confirmations, contributions, hints and marks of the set on the requirements of the model (the
    candidates already built in `reqs`) and return the «paa» part of the model."""
    result, seedset = phase["result"], phase["set"]
    theirs = seedset.definition().get("key") or (key_of(phase["set_model"]) if phase["set_model"] else None)
    if theirs and set(theirs) != set(key_of(model)):
        raise StoreError(f"el conjunto {seedset.id} es de otra clave (D-116): {' '.join(theirs)}")
    index, excluded = {}, set()
    for b in model["general"]:
        for r in b["requirements"]:
            index[r["id"]] = [r]
    for b in model["blocks"]:
        index.update({r["id"]: [r] for r in b["requirements"]})
        excluded |= {r["id"] for r in b.get("excluded", [])}
    index.update({r["id"]: [r] for r in model["inferred"]})
    for r in reqs:
        index.setdefault(r["candidate"], []).append(r)
    for cid, ids in phase.get("compiled", {}).items():
        index.setdefault(cid, []).extend(x for i in ids for x in index.get(i, []))
    # an inferred question of the set's model is the one of this model with the same question (ids are per case); a
    # set classified against this same case, whose model is not there any more, has the inferred questions of this one
    here = {norm(r["question"]): r["id"] for r in model["inferred"]}
    same_case = Path(result.get("model") or "").name.removesuffix(".model.md") == model.get("case")
    theirs_inferred = (phase["set_model"] or ({"inferred": model["inferred"]} if same_case else {})).get("inferred", [])
    inferred = {r["id"]: here.get(norm(r["question"])) for r in theirs_inferred}
    left = {}

    def reach(target: str, what: str) -> list:
        tid = inferred.get(target) if target.startswith("inf/") else target
        found = index.get(tid) if tid else None
        if not found:
            why = ("excluido por relevancia en esta clase" if tid in excluded else
                   "cuestión inferida que este modelo no tiene" if target.startswith("inf/") else "no está en el modelo")
            left.setdefault(f"{what} → {target}: {why}", None)
        return found or []

    tag = {q["n"]: q["source"] for q in result["questions"]}
    confirmed = {}
    for q in result["questions"]:
        for target in q.get("answered_by") or []:
            for r in reach(target, "confirmación"):
                if q["source"] not in r.setdefault("paa_confirmed", []):
                    r["paa_confirmed"].append(q["source"])
                confirmed[r["id"]] = r["paa_confirmed"]
    contributions = []
    for c in result.get("contributions", []):
        support = sorted({tag[n] for n in c.get("questions", []) if n in tag})
        for r in reach(c["target"], "aportación"):
            items = r.setdefault("resolving_info", [])
            if any(norm(x["contribution"]) == norm(c["contribution"]) for x in items):
                continue
            items.append({"contribution": c["contribution"], "component": c.get("component"), "kind": c.get("kind"),
                          "origin": "paa", "support": support, "stores": [], "status": UNCOMPILED})
            contributions.append({"target": r["id"], "contribution": c["contribution"], "kind": c.get("kind")})
    hints = []
    for h in result.get("hints", []):
        for r in reach(h["target"], "pista"):
            if any(norm(x.get("pista", "")) == norm(h["pista"]) for x in r.get("hints", [])):
                continue
            r.setdefault("hints", []).append({**{k: h[k] for k in ("pista", "propiedad", "ac", "origen")},
                                              **({"duda": h["duda"]} if h.get("duda") else {}), "status": UNCOMPILED})
            hints.append({"target": r["id"], "pista": h["pista"], "ac": h["ac"]})
    marks = []
    for m in result.get("marks", []):
        paa = {"mark": m["mark"], **({"case": m["case"]} if m.get("case") else {}), "reason": m["reason"],
               "origin": "paa", "sources": m.get("sources", []), "status": UNCOMPILED}
        for r in reach(m["target"], "marca"):
            now = r.get("comparison")
            if not now:
                r["comparison"], status = paa, "nueva"
            elif now.get("doubt") or now.get("mark") == m["mark"]:
                status = "duda" if now.get("doubt") else "confirma"
            else:
                r["comparison"] = {"mark": "sí", "doubt": True, "reason": DOUBT.format(now=f"el modelo dice «{label(now)}»",
                                                                                     paa=label(paa)),
                                   "model": now, "paa": paa, "status": UNCOMPILED}
                status = "contradice: duda"
            marks.append({"target": r["id"], "mark": m["mark"], "status": status})
    skipped = skipped + list(left)
    skipped += [f"especialización {s['id']} «{s.get('name')}»: la propone PAA; no entra en la ejecución (D-224)"
                for s in result.get("specializations") or []]
    if result.get("revisions"):
        skipped.append(f"revisiones ({len(result['revisions'])}): no entran en la ejecución (las lista bin/train compile, "
                       "D-179)")
    path = phase["path"]
    try:
        where = str(path.resolve().relative_to(ROOT.parent))
    except ValueError:
        where = str(path)
    return {"set": result["set"], "classified": where, "at": result.get("at"), "rulebook": result.get("rulebook_version"),
            "status": UNCOMPILED, "requirements": reqs, "confirmed": confirmed, "contributions": contributions,
            "hints": hints, "marks": marks, "skipped": skipped}


def queued(paa: dict) -> dict:
    """What the queue keeps of the PAA phase: the set and the requirements each kind of entry reached."""
    return {"set": paa["set"], "requirements": [r["id"] for r in paa["requirements"]], "confirmed": sorted(paa["confirmed"]),
            **{k: sorted({x["target"] for x in paa[k]}) for k in ("contributions", "hints", "marks")}}
