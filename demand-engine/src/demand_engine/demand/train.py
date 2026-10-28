"""Training of the demand model, first version (D-044, D-045): rules induced along the Shopify tree.

Usage:
  train discover SPEC             legitimacy of the store and every product URL of its sitemaps, with
                                  the capture engine (in the container; from the host it delegates)
  train select SPEC [DISCOVERY]   training catalog: a few pages of each product type, as many types
                                  as possible, drawn with the spec's seed (training/selection/STORE-DATE.json)
  train capture SELECTION [--pilot] [--max N] [--ignore-hours] [--status]
                                  capture what is pending of a selection in one batch, at the pace of its
                                  spec (container; from the host it delegates); --status: what is captured
  train batch plan SELECTION RUN_DIR [--pilot] [--only ID ...]
                                  batch of captured pages to classify with Claude Code agents (D-054):
                                  phase 1, one case per type (generates the missing blocks); phase 2,
                                  the rest in parallel (RUN_DIR/batch.json); prints the status
  train batch status RUN_DIR      state of each case (pending, with problems, checked, assembled) and
                                  the tokens used, by case, by phase and in total
  train batch usage RUN_DIR ID TRANSCRIPT
                                  record the tokens of the agent that classified a case, summed over
                                  the requests of its transcript (the output file of the agent)
  train batch assemble RUN_DIR    assemble, one after another, the checked cases not yet assembled
  train index [RUN_DIR ...]       rebuild the trait index (catalog/traits.json): each catalog requirement
                                  takes the trait most voted in the runs (a tie keeps the current one),
                                  a proposed trait enters the vocabulary when it wins in a requirement,
                                  and a source keeps its starting trait only if all its requirements
                                  agree (D-056); if missing, the list of categories without a block
  train induce [RUN_DIR ...]      induce candidate rules from the catalog and the votes of the models
                                  assembled in the runs: by trait, exceptions by requirement and class,
                                  relevance (catalog/rules/importance.candidate.json)
  train compile [RUN_DIR ...]     validate the candidate against the current rules (no metric worse,
                                  one better) and, if accepted, publish it and compile the catalog,
                                  including the blocks generated at runtime; compile the resolving
                                  information observed in the runs (catalog/rules/resolving.json); the
                                  runs go in pairs (A and B of each cycle) for the stability
  train resolving refs SOURCE|BLOCK|REQ ...
                                  titles, descriptions, parts and values of reference sources (given
                                  directly or those of catalog requirements), to draft their
                                  resolving information (D-063)
  train report RUN_A [RUN_B ...] [--out FILE]
                                  aggregated report: metrics (control coverage, declared facts without
                                  question, stability between runs, coherence), rules, votes against
                                  the framework, what was used without compiling and divergences
                                  (written to training/reports/NAME-report.md unless --out)

A rule lives in a class and climbs to the parent only if at least two children with data
share it and none contradicts it; within a class it is the weighted majority (a tie goes to
the higher level). Rules never climb above the Shopify verticals. The rule of a trait decides
between principal and complementary; where the votes of a requirement in a class contradict
it, the requirement has its own rule, its exception, which may be critical (D-055, D-058).
Fixed measures and the general layer are the framework and are not induced.
"""
import datetime
import json
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

from references.store import pins

from . import resolving
from .catalog import (CAT_DIR, CATALOG, COMPILED, EMPTY, FIXED, LEVELS, NO_RULE, NOT_RELEVANT, RESOLVING, ROOT,
                      RULES, RUNTIME_DIR, TRAITS, UNCOMPILED, VOTES, blocks_by_node, category_name, chain, depth, floor,
                      load_blocks, load_empty, load_gen, load_resolving, load_rules, load_traits, majority, parent,
                      protected, rank, read_json, relevance, requirement_trait, resolve, save_block, trait_index,
                      write_json)
from .text import covers, match_names, stems

CANDIDATE = CATALOG / "rules" / "importance.candidate.json"
CASES = ROOT / "cases"
REPORTS = ROOT / "training" / "reports"  # results of the training: versioned, unlike the runs


# Index

def trait_votes(models: dict) -> dict:
    """Trait votes of the catalog requirements in the assembled models: {requirement: Counter} (D-056)."""
    votes = defaultdict(Counter)
    for cases in models.values():
        for model in cases.values():
            for b in model["blocks"]:
                if b["type"] == "categoría":
                    for r in b["requirements"] + b.get("excluded", []):
                        if r.get("trait_vote"):
                            votes[r["id"]][r["trait_vote"]] += 1
    return votes


def proposed_traits(models: dict, blocks: dict) -> dict:
    """Traits proposed by the agents, with a definition, in the classifier outputs and the generated blocks."""
    out = {}
    found = [(case, p) for cases in models.values() for case, m in cases.items() for p in m.get("proposed_traits", [])]
    found += [(b["id"], p) for b in blocks.values() for p in b.get("proposed_traits", [])]
    for who, p in found:
        if p.get("name") and p.get("definition"):
            entry = out.setdefault(p["name"], {"label": p.get("label") or p["name"], "definition": p["definition"],
                                               "proposed_by": []})
            entry["proposed_by"].append(who)
    return out


def choose_trait(votes: Counter, current: str) -> str:
    """The most voted trait; a tie keeps the current one (D-056)."""
    top = max(votes.values())
    winners = [t for t, n in votes.items() if n == top]
    return winners[0] if len(winners) == 1 else current


def cmd_index(run_dirs: list) -> None:
    traits = load_traits()
    blocks, models = load_blocks(), load_models(run_dirs)
    src, voted = trait_index()
    vocabulary, proposed = traits["vocabulary"], traits.get("proposed", {})
    for name, p in proposed_traits(models, blocks).items():
        if name not in vocabulary:
            entry = proposed.setdefault(name, {"label": p["label"], "definition": p["definition"], "proposed_by": []})
            entry["proposed_by"] = sorted(set(entry["proposed_by"]) | set(p["proposed_by"]))
    reqs = {r["id"]: r for b in blocks.values() for r in b["requirements"]}
    chosen, approved, undefined, changed = dict(traits.get("requirements", {})), [], [], []
    for req, votes in sorted(trait_votes(models).items()):
        if req not in reqs:
            continue
        current, _ = requirement_trait(reqs[req], src, voted)
        winner = choose_trait(votes, current)
        if winner not in vocabulary:
            if winner in proposed:
                vocabulary[winner] = {"label": proposed[winner]["label"], "definition": proposed[winner]["definition"],
                                      "origin": "propuesto", "approved": datetime.date.today().isoformat(), "first": req}
                approved.append(winner)
                proposed.pop(winner)
            else:
                undefined.append(f"{req}: {winner}")
                winner = current
        if winner != current:
            changed.append(f"{req}: {current} → {winner}")
        chosen[req] = {"trait": winner, "votes": dict(votes)}
    seen = defaultdict(Counter)
    for req, r in reqs.items():
        trait = chosen[req]["trait"] if req in chosen else r.get("trait")
        if trait:
            for s in r.get("sources", []):
                seen[s][trait] += 1
    traits.update({"sources": {s: c.most_common(1)[0][0] for s, c in sorted(seen.items()) if len(c) == 1},
                   "requirements": chosen, "proposed": proposed})
    write_json(TRAITS, traits)
    ambiguous = {s: dict(c) for s, c in seen.items() if len(c) > 1}
    print(f"índice de rasgos: {len(traits['sources'])} fuentes; {len(ambiguous)} con rasgos distintos según el requisito; "
          f"{len(chosen)} requisitos con votos de rasgo, {len(changed)} cambian; {len(approved)} rasgos aprobados; "
          f"{len(proposed)} propuestos sin ganar")
    for line in changed:
        print(f"  {line}")
    for name in approved:
        print(f"  aprobado: {name} — {vocabulary[name]['definition']}")
    for line in undefined:
        print(f"  sin definición (no entra): {line}")
    for s, c in sorted(ambiguous.items()):
        print(f"  {s}: {c}")
    if not EMPTY.exists():
        skeleton = read_json(CATALOG / "skeleton.json")
        nodes = blocks_by_node(load_blocks())
        empty = [b["shopify"] for b in skeleton["blocks"] if b["shopify"] not in nodes]
        write_json(EMPTY, {"note": "Categorías sin requisitos propios (D-043, criterio 7).", "catalog": empty, "runtime": []})
        print(f"categorías sin bloque propio: {', '.join(empty)}")


# Points: labelled importances by trait and class

def seed_label(r: dict):
    return r.get("seed_importance") or r.get("vote") or r.get("importance")


def effective_traits(blocks: dict, src_traits: dict, voted: dict) -> dict:
    """The current trait of each catalog requirement: votes, else sources, else its tag (D-056)."""
    return {r["id"]: requirement_trait(r, src_traits, voted)[0] for b in blocks.values() for r in b["requirements"]}


def catalog_points(blocks: dict, src_traits: dict, voted: dict = None) -> list:
    points = []
    for b in blocks.values():
        for r in b["requirements"]:
            trait, _ = requirement_trait(r, src_traits, voted)
            label = seed_label(r)
            if trait and label in LEVELS:
                points.append({"trait": trait, "node": b["shopify"], "label": label, "w": 1.0, "ref": r["id"], "from": "catálogo"})
    return points


def load_models(run_dirs: list) -> dict:
    """Assembled models by run and case."""
    return {str(d): {p.name.removesuffix(".model.json"): read_json(p) for p in sorted(Path(d).glob("*.model.json"))}
            for d in run_dirs}


def model_requirements(model: dict) -> list:
    return [r for b in model["blocks"] for r in b["requirements"]] + model.get("inferred", [])


def vote_points(models: dict, effective: dict = None) -> list:
    """Importance votes as points of their trait: for a catalog requirement, its current trait (D-056)."""
    effective = effective or {}
    points = []
    for run, cases in models.items():
        for case, model in cases.items():
            for r in model_requirements(model):
                trait = effective.get(r["id"], r.get("trait"))
                if r.get("vote") in LEVELS and trait and r.get("classes"):
                    for node in r["classes"]:
                        points.append({"trait": trait, "node": node, "label": r["vote"], "w": 1 / len(r["classes"]),
                                       "ref": f"{case}:{r['id']}", "from": run})
    return points


# Induction

def induce(points: list) -> dict:
    """Rules by trait along the tree (D-045). They decide between principal and complementary: a critical vote counts
    as principal, because the critical level is decided by requirement and class (D-055, D-058). The measures fixed by
    the framework are not induced."""
    direct = defaultdict(lambda: defaultdict(Counter))
    for p in points:
        if p["trait"] in FIXED:
            continue
        direct[p["trait"]][p["node"]]["principal" if p["label"] == "crítico" else p["label"]] += p["w"]
    tree, rules = {}, []
    for t, by_node in sorted(direct.items()):
        nodes = {n for node in by_node for n in chain(node)}
        eff = {}
        for n in sorted(nodes, key=depth, reverse=True):
            if by_node.get(n):
                eff[n] = majority(by_node[n])
            else:
                kids = [c for c in nodes if parent(c) == n]
                vals = [eff.get(c) for c in kids]
                if len(kids) >= 2 and None not in vals and len(set(vals)) == 1:
                    eff[n] = vals[0]
        for n in sorted(eff, key=lambda n: (depth(n), n)):
            a = parent(n)
            while a and a not in eff:
                a = parent(a)
            if a and eff[a] == eff[n]:
                continue
            tree[f"{t}@{n}"] = eff[n]
            above = a is not None
            rules.append({"id": f"imp:{t}@{n}", "trait": t, "node": n, "importance": eff[n],
                          "kind": "específica" if above else "general", "climbed": not by_node.get(n)})
    return {"tree": tree, "rules": rules}


# Exceptions by requirement and class (D-055, D-058)

def plurality(weights: Counter):
    """The most voted level, or None on a tie: a tie keeps what was there (D-058)."""
    if not weights:
        return None
    top = max(weights.values())
    winners = [level for level, w in weights.items() if abs(w - top) < 1e-9]
    return winners[0] if len(winners) == 1 else None


def exception_votes(models: dict) -> dict:
    """Importance votes of the catalog requirements by class: {requirement: {class: Counter}}."""
    by_req = defaultdict(lambda: defaultdict(Counter))
    for cases in models.values():
        for model in cases.values():
            for b in model["blocks"]:
                if b["type"] == "categoría":
                    for r in b["requirements"] + b.get("excluded", []):
                        if r.get("vote") in LEVELS and r.get("classes"):
                            for node in r["classes"]:
                                by_req[r["id"]][node][r["vote"]] += 1 / len(r["classes"])
    return by_req


def induce_exceptions(blocks: dict, models: dict, tree: dict, src_traits: dict, voted: dict = None) -> tuple:
    """Exceptions by requirement and class (D-058): where the votes of a requirement in a class contradict the rule
    of its trait, the requirement has its own rule, imp:<requirement>@<class>. It is the majority of its votes in the
    class with the importance of the catalog as the starting vote; a tie keeps the trait rule. It climbs to the parent
    with the structural minimum of the trait rules and never above the verticals. Any requirement may be critical
    this way (D-055), but the framework is never lowered: the measure that fixes what is sold has no exceptions, and
    the descriptive measure and the textile composition do not go below principal."""
    info = {r["id"]: (requirement_trait(r, src_traits, voted)[0], r.get("sources", []), seed_label(r))
            for b in blocks.values() for r in b["requirements"]}
    trait_rules = {"tree": tree}
    table, rules = {}, []
    for req, by_node in sorted(exception_votes(models).items()):
        if req not in info:
            continue
        trait, sources, seed = info[req]
        if trait == "medida-que-fija":
            continue
        fixed = floor(trait, sources)[0]
        counts = {n: c + Counter({seed: 1.0}) if seed in LEVELS else c for n, c in by_node.items()}
        nodes = {n for node in counts for n in chain(node)}
        eff = {}
        for n in sorted(nodes, key=depth, reverse=True):
            if counts.get(n):
                eff[n] = plurality(counts[n])
            else:
                kids = [c for c in nodes if parent(c) == n]
                vals = [eff.get(c) for c in kids]
                if len(kids) >= 2 and None not in vals and len(set(vals)) == 1:
                    eff[n] = vals[0]
        emitted = {}
        for n in sorted(eff, key=lambda n: (depth(n), n)):
            level = eff[n]
            if level is None or (fixed and rank(level) < rank(fixed)):
                continue
            a = parent(n)
            while a and a not in emitted:
                a = parent(a)
            base = emitted[a] if a else resolve(trait, [n], trait_rules, sources)[0]
            if level == base:
                continue
            emitted[n] = level
            table[f"{req}@{n}"] = level
            rules.append({"id": f"imp:{req}@{n}", "requirement": req, "trait": trait, "node": n, "importance": level,
                          "kind": "excepción", "climbed": n not in counts,
                          "votes": {k: round(v, 2) for k, v in counts.get(n, {}).items()}})
    return table, rules


# Relevance (D-050): rules by requirement and class; doubt does not exclude

def relevance_points(blocks: dict, models: dict) -> list:
    points = [{"req": r["id"], "node": b["shopify"], "label": "relevante", "w": 1.0, "from": "catálogo", "ref": r["id"]}
              for b in blocks.values() for r in b["requirements"]]
    for run, cases in models.items():
        for case, model in cases.items():
            for b in model["blocks"]:
                if b["type"] != "categoría":
                    continue
                for r in b["requirements"] + b.get("excluded", []):
                    if r.get("vote") in VOTES and r.get("classes"):
                        label = "no relevante" if r["vote"] == NOT_RELEVANT else "relevante"
                        points += [{"req": r["id"], "node": n, "label": label, "w": 1 / len(r["classes"]), "from": run,
                                    "ref": f"{case}:{r['id']}"} for n in r["classes"]]
    return points


def induce_relevance(points: list, blocks: dict) -> tuple:
    info = {r["id"]: (r.get("trait"), r.get("origin"), r.get("sources", [])) for b in blocks.values() for r in b["requirements"]}
    by_req, conflicts = defaultdict(lambda: defaultdict(Counter)), []
    for p in points:
        if p["label"] == "no relevante" and p["req"] in info and protected(*info[p["req"]]):
            conflicts.append({"ref": p["ref"], "from": p["from"]})
            continue
        by_req[p["req"]][p["node"]][p["label"]] += p["w"]
    table, rules = {}, []
    for req, by_node in sorted(by_req.items()):
        if not any(c["no relevante"] for c in by_node.values()):
            continue
        nodes = {n for node in by_node for n in chain(node)}
        eff = {}
        for n in sorted(nodes, key=depth, reverse=True):
            if by_node.get(n):
                c = by_node[n]
                eff[n] = "no relevante" if c["no relevante"] > c["relevante"] else "relevante"  # a tie keeps it
            else:
                kids = [c for c in nodes if parent(c) == n]
                vals = [eff.get(c) for c in kids]
                if len(kids) >= 2 and None not in vals and len(set(vals)) == 1:
                    eff[n] = vals[0]
        for n in sorted(eff, key=lambda n: (depth(n), n)):
            a = parent(n)
            while a and a not in eff:
                a = parent(a)
            if eff[n] == (eff[a] if a else "relevante"):
                continue
            value = "excluido" if eff[n] == "no relevante" else "incluido"
            table[f"{req}@{n}"] = value
            rules.append({"id": f"rel:{req}@{n}", "requirement": req, "node": n, "relevance": value, "kind": "relevancia"})
    return table, rules, conflicts


def cmd_induce(run_dirs: list) -> dict:
    blocks = load_blocks()
    src_traits, voted = trait_index()
    models = load_models(run_dirs)
    points = catalog_points(blocks, src_traits, voted) + vote_points(models, effective_traits(blocks, src_traits, voted))
    candidate = induce(points)
    exc_table, exc_rules = induce_exceptions(blocks, models, candidate["tree"], src_traits, voted)
    candidate["requirements"] = exc_table
    candidate["rules"] += exc_rules
    rel_table, rel_rules, rel_conflicts = induce_relevance(relevance_points(blocks, models), blocks)
    candidate.update({"relevance": rel_table, "relevance_conflicts": rel_conflicts})
    candidate["rules"] += rel_rules
    current = load_rules()
    candidate.update({"version": str(int(current.get("version", "0")) + 1), "induced": datetime.date.today().isoformat(),
                      "points": {"catalog": sum(1 for p in points if p["from"] == "catálogo"),
                                 "votes": sum(1 for p in points if p["from"] != "catálogo")},
                      "runs": [str(d) for d in run_dirs], "refs": pins("demand-engine")})
    write_json(CANDIDATE, candidate)
    kinds = Counter(r["kind"] for r in candidate["rules"])
    print(f"candidata {candidate['version']}: {len(candidate['rules'])} reglas ({', '.join(f'{v} {k}' for k, v in kinds.items())}) "
          f"de {candidate['points']['catalog']} etiquetas del catálogo y {candidate['points']['votes']} votos")
    old = set(current.get("tree", {}).items()) | set(current.get("requirements", {}).items())
    new = set(candidate["tree"].items()) | set(candidate["requirements"].items())
    added, removed = new - old, old - new
    print(f"  frente a la versión {current.get('version', '0')}: {len(added)} reglas nuevas o cambiadas, {len(removed)} retiradas")
    return candidate


# Metrics

def catalog_levels(blocks: dict, src_traits: dict, rules: dict, voted: dict = None, exceptions: bool = True) -> list:
    out = []
    for b in blocks.values():
        for r in b["requirements"]:
            trait, _ = requirement_trait(r, src_traits, voted)
            level, rule = resolve(trait, [b["shopify"]], rules, r.get("sources", []), r["id"] if exceptions else None)
            out.append((b["shopify"], trait, level or seed_label(r), rule or NO_RULE, r))
    return out


def model_level(r: dict, rules: dict, exceptions: bool = True, trait: str = None) -> str:
    level, _ = resolve(trait or r.get("trait"), r.get("classes", []), rules, r.get("sources", []),
                       r["id"] if exceptions else None)
    return level or r.get("vote") or r.get("importance")


def incoherence(groups: dict) -> int:
    """Requirements whose importance differs from the majority of their group (same class and trait)."""
    return sum(len(levels) - Counter(levels).most_common(1)[0][1] for levels in groups.values() if levels)


def coherence(blocks: dict, src_traits: dict, models: dict, rules: dict, voted: dict = None) -> dict:
    """What the rules by trait decide: an exception by requirement is not incoherence (D-058)."""
    cat_groups, model_groups = defaultdict(list), defaultdict(list)
    for node, trait, level, _, _ in catalog_levels(blocks, src_traits, rules, voted, exceptions=False):
        cat_groups[(node, trait)].append(level)
    effective = effective_traits(blocks, src_traits, voted)
    for run, cases in models.items():
        for case, model in cases.items():
            for r in model_requirements(model):
                trait = effective.get(r["id"], r.get("trait"))
                model_groups[(run, case, tuple(r.get("classes", [])), trait)].append(
                    model_level(r, rules, exceptions=False, trait=trait))
    return {"catalog": incoherence(cat_groups), "models": incoherence(model_groups),
            "catalog_requirements": sum(len(v) for v in cat_groups.values()),
            "catalog_without_rule": sum(1 for *_, rule, _ in catalog_levels(blocks, src_traits, rules, voted) if rule == NO_RULE)}


def requirement_coherence(models: dict, rules: dict, effective: dict = None) -> dict:
    """Coherence by requirement (D-055, D-058): pairs of a catalog requirement and a class whose importance contradicts
    the clear majority of its votes there (a tie is no majority; without a rule, the vote decides and nothing
    contradicts it). It must go down."""
    effective = effective or {}
    votes, level = defaultdict(Counter), {}
    for cases in models.values():
        for model in cases.values():
            for b in model["blocks"]:
                if b["type"] != "categoría":
                    continue
                for r in b["requirements"] + b.get("excluded", []):
                    if r.get("vote") not in LEVELS:
                        continue
                    trait = effective.get(r["id"], r.get("trait"))
                    for node in r.get("classes", []):
                        votes[(r["id"], node)][r["vote"]] += 1
                        level[(r["id"], node)] = resolve(trait, [node], rules, r.get("sources", []), r["id"])[0]
    against = [k for k, c in votes.items() if level[k] and plurality(c) not in (None, level[k])]
    return {"against": len(against), "pairs": len(votes), "list": sorted(f"{r}@{n}" for r, n in against)}


def relevance_metrics(models: dict, rules: dict) -> dict:
    """Relevance incoherence (requirements kept with a majority of «no relevante» votes in their class) and the
    coverage safeguard (declared facts whose only question the rules exclude)."""
    votes, kept_pairs, gaps = defaultdict(Counter), set(), 0
    for run, cases in models.items():
        for case, model in cases.items():
            kept = set()
            for b in model["blocks"]:
                for r in b["requirements"] + b.get("excluded", []):
                    excluded, _ = relevance(r["id"], r.get("classes", []), rules)
                    if excluded and protected(r.get("trait"), r.get("origin"), r.get("sources", [])):
                        excluded = False
                    key = (r["id"], tuple(r.get("classes", [])))
                    if not excluded:
                        kept.add(r["id"])
                        kept_pairs.add(key)
                    if r.get("vote") in VOTES:
                        votes[key]["no" if r["vote"] == NOT_RELEVANT else "sí"] += 1
            other = {r["id"] for r in model.get("inferred", [])} | {r["id"] for g in model["general"] for r in g["requirements"]}
            gaps += sum(1 for a in model["coverage"].get("answers", []) if a not in kept | other)
    return {"incoherence": sum(1 for k in kept_pairs if votes[k]["no"] > votes[k]["sí"]), "coverage_gaps": gaps}


def pairs(models: dict) -> list:
    """Cases run twice: the runs go in pairs, in the order given (A and B of each cycle, e.g. training and control)."""
    runs = list(models)
    out = []
    for ra, rb in zip(runs[0::2], runs[1::2]):
        a, b = models[ra], models[rb]
        out += [(case, a[case], b[case]) for case in sorted(a.keys() & b.keys())]
    return out


def stability(models: dict, rules: dict, effective: dict = None) -> dict:
    effective = effective or {}
    out = Counter()
    for case, a, b in pairs(models):
        out["cases"] += 1
        out["composition"] += (set(a["composition"]["classes"]), set(a["composition"]["aliases"])) == \
                              (set(b["composition"]["classes"]), set(b["composition"]["aliases"]))
        out["key"] += a["key"] == b["key"]
        ea = [x["name"] or x["id"] for x in a["blocks"] if x["type"] == "especialización"]
        eb = [x["name"] or x["id"] for x in b["blocks"] if x["type"] == "especialización"]
        matched, extra = match_names(ea, eb)
        out["specializations"] += all(o for _, o in matched) and not extra
        out["application"] += a["offer"]["application"] == b["offer"]["application"]
        ra = {r["id"]: r for x in a["blocks"] if x["type"] == "categoría" for r in x["requirements"]}
        rb = {r["id"]: r for x in b["blocks"] if x["type"] == "categoría" for r in x["requirements"]}
        common = ra.keys() & rb.keys()
        out["common"] += len(common)
        out["same_importance"] += sum(model_level(ra[i], rules, trait=effective.get(i)) ==
                                      model_level(rb[i], rules, trait=effective.get(i)) for i in common)
    return dict(out)


def better_or_equal(cur: dict, cand: dict) -> tuple:
    worse, better = [], []
    for name, c, n, lower_is_better in (
            ("coherencia del catálogo", cur["coherence"]["catalog"], cand["coherence"]["catalog"], True),
            ("coherencia de los modelos", cur["coherence"]["models"], cand["coherence"]["models"], True),
            ("coherencia por requisito", cur["requirement"]["against"], cand["requirement"]["against"], True),
            ("estabilidad de la importancia", cur["stability"].get("same_importance", 0), cand["stability"].get("same_importance", 0), False),
            ("requisitos del catálogo sin regla", cur["coherence"]["catalog_without_rule"], cand["coherence"]["catalog_without_rule"], True),
            ("coherencia de relevancia", cur["relevance"]["incoherence"], cand["relevance"]["incoherence"], True),
            ("hechos declarados sin pregunta", cur["relevance"]["coverage_gaps"], cand["relevance"]["coverage_gaps"], True)):
        if n == c:
            continue
        ((better if n < c else worse) if lower_is_better else (better if n > c else worse)).append(f"{name}: {c} → {n}")
    return worse, better


def evaluate(rules: dict, blocks: dict, src_traits: dict, models: dict, voted: dict = None) -> dict:
    effective = effective_traits(blocks, src_traits, voted)
    return {"coherence": coherence(blocks, src_traits, models, rules, voted), "stability": stability(models, rules, effective),
            "requirement": requirement_coherence(models, rules, effective), "relevance": relevance_metrics(models, rules)}


# Compile

def family(rules: dict, name: str) -> dict:
    """The part of a rule set that belongs to one family: importance (by trait and exceptions by requirement) or relevance."""
    if name == "importancia":
        return {"tree": rules.get("tree", {}), "requirements": rules.get("requirements", {}),
                "rules": [r for r in rules.get("rules", []) if r["kind"] != "relevancia"]}
    return {"relevance": rules.get("relevance") or {}, "relevance_conflicts": rules.get("relevance_conflicts") or [],
            "rules": [r for r in rules.get("rules", []) if r["kind"] == "relevancia"]}


def combine(importance: dict, relevance: dict) -> dict:
    out = {k: v for k, v in importance.items() if k != "rules"}
    out.update({k: v for k, v in relevance.items() if k != "rules"})
    out["rules"] = importance["rules"] + relevance["rules"]
    return out


def cmd_compile(run_dirs: list) -> None:
    """Validate each family of the candidate (importance, relevance) against the current rules: a family is
    accepted if no metric gets worse and at least one improves (D-045), so one family cannot block the other."""
    if not CANDIDATE.exists():
        sys.exit("train: no hay reglas candidatas; ejecuta antes «train induce»")
    candidate, current = read_json(CANDIDATE), load_rules()
    blocks, models = load_blocks(), load_models(run_dirs)
    src_traits, voted = trait_index()
    m_cur = evaluate(current, blocks, src_traits, models, voted)
    first = current.get("version", "0") == "0"
    parts, decisions = {}, {}
    for name in ("importancia", "relevancia"):
        cur_part, cand_part = family(current, name), family(candidate, name)
        other = family(current, "relevancia" if name == "importancia" else "importancia")
        trial = combine(cand_part, other) if name == "importancia" else combine(other, cand_part)
        unchanged = {k: v for k, v in cand_part.items() if k != "rules"} == {k: v for k, v in cur_part.items() if k != "rules"}
        m_trial = evaluate(trial, blocks, src_traits, models, voted)
        worse, better = better_or_equal(m_cur, m_trial)
        accepted = not unchanged and not worse and (bool(better) or first)
        parts[name] = cand_part if accepted else cur_part
        decisions[name] = {"accepted": accepted, "unchanged": unchanged, "worse": worse, "better": better, "metrics": m_trial}
        state = "sin cambios" if unchanged else "aceptada" if accepted else "descartada"
        print(f"{name}: {state}" + (f" — empeora: {'; '.join(worse)}" if worse else "") + (f" — mejora: {'; '.join(better)}" if better else ""))
    candidate["decision"] = {"date": datetime.date.today().isoformat(), "against": current.get("version", "0"),
                             "accepted": any(d["accepted"] for d in decisions.values()),
                             "worse": [w for d in decisions.values() for w in d["worse"]],
                             "better": [b for d in decisions.values() if d["accepted"] for b in d["better"]],
                             "families": decisions, "metrics": {"current": m_cur}}
    write_json(CANDIDATE, candidate)
    if not candidate["decision"]["accepted"]:
        print("ninguna familia se acepta: se compila el catálogo con la versión vigente")
        rules = current
    else:
        rules = combine(parts["importancia"], parts["relevancia"])
        rules.update({"version": candidate["version"], "induced": candidate.get("induced"), "points": candidate.get("points"),
                      "runs": candidate.get("runs"), "refs": candidate.get("refs")})
        rules["accepted"] = {"date": datetime.date.today().isoformat(), "better": candidate["decision"]["better"],
                             "families": {k: v["accepted"] for k, v in decisions.items()},
                             "metrics": evaluate(rules, blocks, src_traits, models, voted)}
        write_json(RULES, rules)
        print(f"reglas {rules['version']} publicadas ({'; '.join(candidate['decision']['better']) or 'primera versión'})")
    added = add_block_proposals(blocks, models)
    if added:
        print(f"propuestas al bloque incorporadas (D-088): {', '.join(added)}")
    changed = 0
    for b in blocks.values():
        before = json.dumps(b["requirements"], ensure_ascii=False) + str(b.get("status"))
        for r in b["requirements"]:
            r.setdefault("seed_importance", seed_label(r))
            trait, _ = requirement_trait(r, src_traits, voted)
            level, rule = resolve(trait, [b["shopify"]], rules, r.get("sources", []), r["id"])
            r["trait"], r["importance"], r["rule"] = trait, level or seed_label(r), rule or NO_RULE
        b["status"] = COMPILED
        if json.dumps(b["requirements"], ensure_ascii=False) + COMPILED != before:
            changed += 1
            v = b.get("version", "0")
            b["version"] = str(int(float(v)) + 1)
        b["compiled_by"] = f"reglas {rules['version']}"
        if b["_where"] == "ejecución":
            new_path = CAT_DIR / Path(b["_path"]).name
            b["_path"], b["_where"] = str(new_path), "catálogo"
            Path(b["_path"]).parent.mkdir(parents=True, exist_ok=True)
            save_block(b)
            (RUNTIME_DIR / new_path.name).unlink(missing_ok=True)
        else:
            save_block(b)
    if EMPTY.exists():
        data = read_json(EMPTY)
        data["catalog"] = sorted(set(data["catalog"]) | set(data.get("runtime", [])))
        data["runtime"] = []
        write_json(EMPTY, data)
    print(f"catálogo compilado: {len(blocks)} bloques, {changed} con versión nueva")
    compile_resolving(blocks, models, rules, run_dirs)


# Proposals to the block (D-088)

def block_proposals(models: dict, blocks: dict) -> list:
    """Inferred questions with a source that their block neither asks nor excludes (D-088): omissions of the block.
    One per source; the first one seen is kept."""
    out, taken = [], set()
    for run, cases in models.items():
        for case, m in cases.items():
            for r in m.get("inferred", []):
                host, sources = blocks.get(r.get("block")), set(r.get("sources") or [])
                if not host or not sources:
                    continue
                known = {s for q in host["requirements"] for s in q.get("sources", [])} | \
                        {e.get("source") for e in host.get("excluded", [])}
                if sources & (known | taken):
                    continue
                taken |= sources
                out.append({"block": host["id"], "case": case, "run": run, "requirement": r})
    return out


def add_block_proposals(blocks: dict, models: dict) -> list:
    """Add each proposal to its block with a new id, never one the block has used, origin «referencias» and the vote
    of the agent as the starting label; the compilation decides its trait and importance (D-088)."""
    added = []
    for p in block_proposals(models, blocks):
        b, r = blocks[p["block"]], p["requirement"]
        used = [int(x["id"].rsplit("/", 1)[1]) for x in b["requirements"] + b.get("excluded", [])
                if str(x.get("id", "")).startswith(b["id"] + "/")]
        rid = f"{b['id']}/{max(used, default=0) + 1:02d}"
        b["requirements"].append({
            "id": rid, "question": r["question"], "dimension": r.get("dimension"), "trait": r.get("trait"),
            "entity": r.get("entity"), "origin": "referencias", "sources": sorted(r["sources"]),
            "applicability": r.get("applicability") or "universal",
            "rationale": f"{r.get('rationale') or ''} Propuesta al bloque (D-088) desde {p['case']} ({Path(p['run']).name}).".strip(),
            "seed_importance": r.get("vote") if r.get("vote") in LEVELS else "complementario",
            "resolving_info": [{k: v for k, v in c.items() if k != "stores"} for c in r.get("resolving_info", [])]})
        added.append(rid)
    return added


def compile_resolving(blocks: dict, models: dict, rules: dict, run_dirs: list) -> None:
    """The resolving information observed in the runs (D-063): not validated by metrics, its rule is fixed."""
    questions = {r["id"]: r for b in blocks.values() for r in b["requirements"]}
    questions.update({r["id"]: r for g in load_gen()["blocks"] for r in g["requirements"]})
    found = resolving.induce(questions, models)
    write_json(RESOLVING, {"version": rules.get("version"), "compiled": datetime.date.today().isoformat(),
                           "runs": [str(d) for d in run_dirs], "min_stores": resolving.MIN_STORES, "requirements": found})
    count = Counter()
    for e in found.values():
        count["observed"] += len(e["observed"])
        for k in ("accepted", "proposed", "rejected", "never_observed"):
            count[k] += len(e[k])
    print(f"información resolutiva: {len(found)} requisitos; {count['observed']} aportaciones de las listas observadas, "
          f"{count['never_observed']} nunca observadas; propuestas desde las fichas: {count['accepted']} aceptadas, "
          f"{count['proposed']} pendientes (una tienda), {count['rejected']} rechazadas")


# Resolving information (D-063)

def print_reference(source: str, indent: str = "  ") -> None:
    info = resolving.reference_info(source)
    if info is None:
        print(f"{indent}{source}: sin datos en las referencias")
        return
    print(f"{indent}{source}: {info['title']}" + (f" — {info['description']}" if info.get("description") else ""))
    for part in info["parts"]:
        print(f"{indent}  · {part['name']}: {part['title']}" + (f" — {part['description']}" if part.get("description") else ""))
    if info["values"]:
        shown = info["values"][:12]
        print(f"{indent}  valores: {', '.join(map(str, shown))}" + (f" … +{len(info['values']) - 12}" if len(info["values"]) > 12 else ""))


def cmd_resolving_refs(ids: list) -> None:
    """Print what the references say about sources (given directly, or those of catalog requirements or blocks),
    to draft their contributions (D-063)."""
    sources = [i for i in ids if ":" in i]
    for source in sources:
        print_reference(source, "")
    wanted = [i for i in ids if ":" not in i]
    if not wanted:
        return
    reqs = [r for b in load_blocks().values() for r in b["requirements"]
            if any(r["id"] == i or b["id"] == i for i in wanted)]
    if not reqs:
        sys.exit(f"train: no hay requisitos de {' '.join(wanted)} en el catálogo")
    for r in reqs:
        print(f"\n{r['id']} · {r['question']}")
        for source in r.get("sources", []):
            print_reference(source)


# Report

def expected_questions(case: dict) -> list:
    exp = case["expected"]
    qs = [q for s in exp["specializations"] for q in s.get("questions", [])]
    qs += [q for f in exp.get("features", []) for q in f.get("questions", [])
           if f.get("role", "").startswith(("valor que condiciona", "requisito", "cuestión", "respuesta"))]
    return qs


def control(model: dict, case: dict) -> dict:
    exp = case["expected_v1"]
    res = {"composition": set(model["composition"]["classes"]) == set(exp["categories"])
           and set(model["composition"]["aliases"]) == set(exp["alias"])}
    esp = [f"{b.get('name', '')} {b.get('trigger', '')} {b['id']}".replace(".", " ").replace("-", " ")
           for b in model["blocks"] if b["type"] == "especialización"]
    matched, extra = match_names([s["name"] for s in exp["specializations"]], esp)
    res["specializations"] = all(o for _, o in matched) and not extra
    res["esp_detail"] = [(e, o) for e, o in matched] + [(None, o) for o in extra]
    questions = [r["question"] for r in model_requirements(model)] + [r["question"] for b in model["general"] for r in b["requirements"]]
    qs = expected_questions(case)
    hit = [q for q in qs if any(covers(q, x) for x in questions)]
    res["questions"], res["questions_all"], res["missing_questions"] = len(hit), len(qs), [q for q in qs if q not in hit]
    if exp.get("application") is not None:
        res["application"] = set(exp["application"]) <= set(model["offer"]["application"])
    groups = exp.get("inferred_any_of") or []
    if groups:
        inferred = [r["question"] for r in model.get("inferred", [])]
        res["inferred"] = any(all(set(stems(w)) <= stems(q) for w in g) for g in groups for q in inferred)
    return res


def framework_votes(models: dict, effective: dict) -> list:
    """Votes that contradict the framework (D-043, D-058): the measure that fixes what is sold below critical, the
    descriptive measure or the textile composition below principal. The general layer is not voted."""
    found = Counter()
    for cases in models.values():
        for model in cases.values():
            for b in model["blocks"]:
                if b["type"] != "categoría":
                    continue
                for r in b["requirements"] + b.get("excluded", []):
                    vote = r.get("vote")
                    if vote not in LEVELS:
                        continue
                    trait = effective.get(r["id"], r.get("trait"))
                    base = floor(trait, r.get("sources", []))[0]
                    if base and rank(vote) < rank(base):
                        found[(r["id"], trait, vote)] += 1
    lines = ["", "### Votos que contradicen el marco", ""]
    if not found:
        return lines + ["Ninguno."]
    lines.append(f"{sum(found.values())} votos (no cuentan para bajar lo que fija el marco):")
    lines += [f"- {req} ({trait}): {n} votos «{vote}»" for (req, trait, vote), n in found.most_common(15)]
    return lines


def traits_section(models: dict) -> list:
    """Trait votes, traits chosen by the votes, and proposed and approved traits (D-056)."""
    traits = load_traits()
    votes = trait_votes(models)
    chosen = traits.get("requirements", {})
    approved = {k: v for k, v in traits["vocabulary"].items() if v.get("origin") == "propuesto"}
    lines = ["", "## Rasgos", "",
             f"Requisitos del catálogo con votos de rasgo en estas ejecuciones: {len(votes)} · con rasgo elegido por los votos "
             f"en el índice: {len(chosen)} · rasgos propuestos sin ganar: {len(traits.get('proposed', {}))} · aprobados: {len(approved)}."]
    for name, t in sorted(approved.items()):
        lines.append(f"- Aprobado **{name}** ({t.get('approved')}, primero en {t.get('first')}): {t['definition']}")
    for name, t in sorted(traits.get("proposed", {}).items()):
        lines.append(f"- Propuesto **{name}** (por {', '.join(t['proposed_by'][:4])}): {t['definition']}")
    return lines


def resolving_section() -> list:
    """The resolving information compiled from the runs (D-063)."""
    data = load_resolving()
    reqs = data.get("requirements", {})
    lines = ["", "## Información resolutiva", ""]
    if not reqs:
        return lines + ["Sin aportaciones observadas ni listas en el catálogo todavía."]
    count = Counter()
    for e in reqs.values():
        count["observed"] += len(e["observed"])
        for k in ("accepted", "proposed", "rejected", "never_observed"):
            count[k] += len(e[k])
    lines.append(f"{len(reqs)} requisitos (mínimo de aceptación: {data.get('min_stores')} tiendas distintas). Aportaciones de las "
                 f"listas observadas: {count['observed']} · nunca observadas: {count['never_observed']}. Propuestas desde las "
                 f"fichas: {count['accepted']} aceptadas, {count['proposed']} pendientes (una tienda), {count['rejected']} rechazadas.")
    for kind, title in (("accepted", "Aceptadas"), ("proposed", "Pendientes"), ("rejected", "Rechazadas")):
        items = [(req, a) for req, e in sorted(reqs.items()) for a in e[kind]]
        if items:
            lines += ["", f"{title}:", ""]
            lines += [f"- {req}: {a['contribution']} (componente: {a.get('component') or '—'}; tiendas: {', '.join(a['stores'])})"
                      + (f" — {a['reason']}" if a.get("reason") else "") for req, a in items[:30]]
    never = [(req, name) for req, e in sorted(reqs.items()) for name in e["never_observed"]]
    if never:
        lines += ["", "Nunca observadas: " + "; ".join(f"{req}: {name}" for req, name in never[:40]) + "."]
    return lines


def cmd_report(args: list) -> None:
    out_file = None
    if "--out" in args:
        i = args.index("--out")
        out_file = Path(args[i + 1])
        args = args[:i] + args[i + 2:]
    run_dirs = [Path(a) for a in args]
    if out_file is None:
        # A cycle is a pair of runs NAME-a and NAME-b: its report is training/reports/NAME-report.md
        stem = run_dirs[0].name
        stem = stem[:-2] if stem.endswith(("-a", "-b")) else stem
        out_file = REPORTS / f"{stem}-report.md"
        out_file.parent.mkdir(parents=True, exist_ok=True)
    models = load_models(run_dirs)
    rules, blocks = load_rules(), load_blocks()
    src_traits, voted = trait_index()
    effective = effective_traits(blocks, src_traits, voted)
    lines = [f"# Informe del entrenamiento · reglas {rules.get('version', '0')} · {datetime.date.today().isoformat()}", "",
             f"Ejecuciones: {', '.join(str(d) for d in run_dirs)}.", ""]
    # control set
    ctrl = defaultdict(lambda: Counter())
    rows = []
    for run, cases in models.items():
        for case_id, model in cases.items():
            path = CASES / f"{case_id}.json"
            if not path.exists():
                continue
            res = control(model, read_json(path))
            c = ctrl[run]
            c["cases"] += 1
            for k in ("composition", "specializations", "application", "inferred"):
                if k in res:
                    c[k] += res[k]
                    c[k + "_all"] += 1
            c["questions"] += res["questions"]
            c["questions_all"] += res["questions_all"]
            rows.append((run, case_id, res))
    lines += ["## Métricas", "", "### Cobertura en el conjunto de control", "",
              "| Ejecución | Casos | Composición | Especializaciones | Cuestiones clave | Aplicación | Inferida esperada |",
              "|---|---|---|---|---|---|---|"]
    for run, c in ctrl.items():
        pct = f" ({100 * c['questions'] / c['questions_all']:.0f} %)" if c["questions_all"] else ""
        lines.append(f"| {Path(run).name} | {c['cases']} | {c['composition']}/{c['composition_all']} | "
                     f"{c['specializations']}/{c['specializations_all']} | {c['questions']}/{c['questions_all']}{pct} | "
                     f"{c['application']}/{c['application_all']} | {c['inferred']}/{c['inferred_all']} |")
    lines += ["", "### Cobertura por hechos declarados", "", "| Ejecución | Hechos que cuentan | Sin pregunta en el modelo |", "|---|---|---|"]
    gaps = Counter()
    for run, cases in models.items():
        counted = sum(m["coverage"]["declared_counted"] for m in cases.values())
        missing = sum(len(m["coverage"]["gaps"]) for m in cases.values())
        for m in cases.values():
            for g in m["coverage"]["gaps"]:
                gaps[g["feature"]] += 1
        lines.append(f"| {Path(run).name} | {counted} | {missing} |")
    st = stability(models, rules, effective)
    if st:
        lines += ["", "### Estabilidad entre ejecuciones", "", "| Medida | Resultado |", "|---|---|",
                  f"| Composición (categorías y alias) | {st['composition']}/{st['cases']} |",
                  f"| Clave del modelo | {st['key']}/{st['cases']} |",
                  f"| Especializaciones | {st['specializations']}/{st['cases']} |",
                  f"| Aplicación de la oferta | {st['application']}/{st['cases']} |",
                  f"| Importancia en los requisitos de categoría comunes | {st['same_importance']}/{st['common']} |"]
    coh = coherence(blocks, src_traits, models, rules, voted)
    req_coh = requirement_coherence(models, rules, effective)
    lines += ["", "### Coherencia", "",
              f"Requisitos con el mismo rasgo y la misma clase e importancia distinta (lo que deciden las reglas por rasgo; "
              f"una excepción por requisito no cuenta): {coh['catalog']} en el catálogo ({coh['catalog_requirements']} "
              f"requisitos) y {coh['models']} en los modelos.", "",
              f"Coherencia por requisito: {req_coh['against']} de {req_coh['pairs']} pares de requisito de categoría y clase "
              f"tienen una mayoría clara de votos contra su importancia.", ""]
    # rules
    decided = Counter(rule for _, _, _, rule, _ in catalog_levels(blocks, src_traits, rules, voted))
    lines += ["## Reglas de importancia", ""]
    trait_rules = [r for r in rules.get("rules", []) if r["kind"] in ("general", "específica")]
    exc_rules = [r for r in rules.get("rules", []) if r["kind"] == "excepción"]
    rel_rules = [r for r in rules.get("rules", []) if r["kind"] == "relevancia"]
    if trait_rules or exc_rules:
        kinds = Counter(r["kind"] for r in trait_rules + exc_rules)
        plural = {"general": "generales", "específica": "específicas", "excepción": "excepciones por requisito y clase"}
        lines.append(f"{len(trait_rules) + len(exc_rules)} reglas: " + ", ".join(f"{v} {plural.get(k, k)}" for k, v in kinds.items())
                     + f". Etiquetas del catálogo: {rules.get('points', {}).get('catalog', 0)}; votos: {rules.get('points', {}).get('votes', 0)}.")
        if rules.get("accepted", {}).get("better"):
            lines.append(f"Aceptada porque mejora: {'; '.join(rules['accepted']['better'])}.")
        lines += ["", "### Por rasgo", "", "| Regla | Rasgo | Clase | Importancia | Tipo | Requisitos del catálogo que decide |",
                  "|---|---|---|---|---|---|"]
        for r in sorted(trait_rules, key=lambda r: (r["trait"], depth(r["node"]), r["node"])):
            lines.append(f"| `{r['id']}` | {r['trait']} | {category_name(r['node'])} ({r['node']}) | {r['importance']} | {r['kind']}"
                         f"{' (sube desde las hijas)' if r.get('climbed') else ''} | {decided.get(r['id'], 0)} |")
        fixed = {k: v for k, v in decided.items() if k.startswith("marco:")}
        lines += ["", "Reglas del marco: " + (", ".join(f"`{k}` ({v})" for k, v in sorted(fixed.items())) or "—")
                  + f" · requisitos sin regla: {decided.get(NO_RULE, 0)}."]
        lines += ["", "### Excepciones por requisito y clase", ""]
        if exc_rules:
            critical = sum(1 for r in exc_rules if r["importance"] == "crítico")
            lines += [f"{len(exc_rules)} excepciones, {critical} de crítico. Votos de la clase, con el del catálogo como voto de partida.",
                      "", "| Regla | Requisito | Rasgo | Clase | Importancia | Votos |", "|---|---|---|---|---|---|"]
            for r in sorted(exc_rules, key=lambda r: (r["requirement"], depth(r["node"]), r["node"])):
                votes = ", ".join(f"{k} {v:g}" for k, v in sorted(r.get("votes", {}).items(), key=lambda kv: -kv[1])) or "de las hijas"
                lines.append(f"| `{r['id']}` | {r['requirement']} | {r['trait']} | {category_name(r['node'])} ({r['node']}) | "
                             f"{r['importance']} | {votes} |")
        else:
            lines.append("Ninguna.")
    else:
        lines.append("Sin reglas compiladas todavía.")
    lines += framework_votes(models, effective)
    lines += traits_section(models)
    lines += resolving_section()
    pending = block_proposals(models, blocks)
    lines += ["", "## Propuestas al bloque", "",
              f"Cuestiones inferidas con fuente que su bloque ni pregunta ni excluye (D-088), pendientes de compilar: {len(pending)}."]
    lines += [f"- {p['block']} ← {', '.join(p['requirement']['sources'])}: {p['requirement']['question']} ({p['case']})"
              for p in pending]
    lines += ["", "## Relevancia", ""]
    doubtful = sum(len(m["uncompiled"].get("doubtful_relevance", [])) for cases in models.values() for m in cases.values())
    excluded = sum(len(m.get("excluded", [])) for cases in models.values() for m in cases.values())
    rel = relevance_metrics(models, rules)
    lines.append(f"Reglas de exclusión: {len(rel_rules)} · requisitos excluidos en los modelos: {excluded} · con relevancia dudosa "
                 f"(votados «no relevante» sin regla): {doubtful} · coherencia de relevancia: {rel['incoherence']} · "
                 f"hechos declarados sin pregunta con estas reglas: {rel['coverage_gaps']}.")
    if rel_rules:
        lines += ["", "| Regla | Requisito | Clase | Decisión |", "|---|---|---|---|"]
        lines += [f"| `{r['id']}` | {r['requirement']} | {category_name(r['node'])} ({r['node']}) | {r['relevance']} |" for r in rel_rules]
    if rules.get("relevance_conflicts"):
        lines.append(f"Votos «no relevante» en requisitos que el marco no deja excluir: {len(rules['relevance_conflicts'])}.")
    if CANDIDATE.exists():
        cand = read_json(CANDIDATE)
        d = cand.get("decision")
        if d and d.get("families"):
            lines += ["", f"Candidata {cand['version']} ({cand['points']['votes']} votos), validada por familias frente a la versión {d['against']}:", ""]
            for name, f in d["families"].items():
                state = "sin cambios" if f["unchanged"] else "aceptada" if f["accepted"] else "**descartada**"
                lines.append(f"- {name}: {state}" + (f"; empeora: {'; '.join(f['worse'])}" if f["worse"] else "")
                             + (f"; mejora: {'; '.join(f['better'])}" if f["better"] else "") + ".")
        elif d and cand.get("version") != rules.get("version"):
            added = (set(cand["tree"].items()) | set(cand.get("relevance", {}).items())) - (set(rules.get("tree", {}).items()) | set((rules.get("relevance") or {}).items()))
            removed = (set(rules.get("tree", {}).items()) | set((rules.get("relevance") or {}).items())) - (set(cand["tree"].items()) | set(cand.get("relevance", {}).items()))
            lines += ["", f"Candidata {cand['version']} ({len(cand['rules'])} reglas, {cand['points']['votes']} votos; "
                      f"{len(added)} reglas nuevas o cambiadas y {len(removed)} retiradas frente a la versión {d['against']}): "
                      + ("aceptada" if d["accepted"] else "**descartada**") + ". "
                      + (f"Empeora: {'; '.join(d['worse'])}. " if d["worse"] else "")
                      + (f"Mejora: {'; '.join(d['better'])}." if d["better"] else "")]
    # vote agreement, against the current rules (a run assembled with older rules keeps its old importances)
    agree = total = 0
    against = Counter()
    for run, cases in models.items():
        for m in cases.values():
            for r in model_requirements(m):
                if r.get("vote") in LEVELS and not r.get("provisional"):
                    level, rule = resolve(effective.get(r["id"], r.get("trait")), r.get("classes", []), rules,
                                          r.get("sources", []), r["id"])
                    if not level:
                        continue
                    total += 1
                    if r["vote"] == level:
                        agree += 1
                    else:
                        against[(rule, r["vote"])] += 1
    if total:
        lines += ["", f"Votos de los agentes que coinciden con la regla: {agree}/{total}. Reglas con más votos en contra:", ""]
        for (rule, vote), n in against.most_common(8):
            lines.append(f"- `{rule}`: {n} votos «{vote}»")
    # uncompiled
    lines += ["", "## Usado sin compilar", "", "| Ejecución | Caso | Bloques | Sin regla | Inferidas | Categorías sin bloque |", "|---|---|---|---|---|---|"]
    for run, cases in models.items():
        for case_id, m in cases.items():
            u = m["uncompiled"]
            lines.append(f"| {Path(run).name} | {case_id} | {', '.join(u['blocks']) or '—'} | {len(u['without_rule'])} | "
                         f"{len(u['inferred'])} | {', '.join(u['missing_blocks']) or '—'} |")
    # divergences
    lines += ["", "## Divergencias de las decisiones no inducidas", ""]
    for run, case_id, res in rows:
        issues = []
        if not res["composition"]:
            m = models[run][case_id]
            issues.append(f"composición {sorted(m['composition']['classes'])} alias {sorted(m['composition']['aliases'])}")
        if not res["specializations"]:
            issues.append("especializaciones " + "; ".join(f"{e or '—'} ↔ {o or '—'}" for e, o in res["esp_detail"]))
        if res["missing_questions"]:
            issues.append("faltan " + ", ".join(res["missing_questions"]))
        if res.get("application") is False:
            issues.append("aplicación incompleta")
        if res.get("inferred") is False:
            issues.append("falta la inferida esperada")
        if issues:
            lines.append(f"- **{Path(run).name} · {case_id}:** " + " · ".join(issues))
    for case, a, b in pairs(models):
        if a["key"] != b["key"]:
            lines.append(f"- **Modelo inestable · {case}:** {' '.join(a['key']['model'])} | {' '.join(b['key']['model'])}")
        if a["offer"] != b["offer"]:
            lines.append(f"- **Oferta inestable · {case}:** {a['offer']['label']} | {b['offer']['label']}")
    if gaps:
        lines += ["", "Hechos declarados sin pregunta más repetidos: " + "; ".join(f"{f} ({n})" for f, n in gaps.most_common(12)) + "."]
    text = "\n".join(lines) + "\n"
    if out_file:
        out_file.write_text(text, encoding="utf-8")
        print(f"informe → {out_file}")
    else:
        print(text, end="")


def cmd_discover(spec_path: Path) -> None:
    from capture import pages
    from . import selection
    if not pages.engine_available():
        # On the host: the capture engine (Chrome, websockets) runs in the container
        spec = spec_path.resolve().relative_to(ROOT.parent)
        code = subprocess.call([str(ROOT.parent / "bin/run"), "dev", "exec", "python", "-m",
                                "demand_engine.demand.train", "discover", str(spec)])
        if code:
            print("train: discover se ejecuta en el contenedor; si no está levantado: bin/run dev up", file=sys.stderr)
        sys.exit(code)
    try:
        folder = selection.discover(selection.read_spec(spec_path))
    except selection.SelectionError as e:
        sys.exit(f"train: {e}")
    meta = read_json(folder / "discovery.json")
    for kind in ("products", "categories"):
        if kind in meta:
            print(f"{kind}: {meta[kind]['urls']} URL de {len(meta[kind]['sitemaps'])} sitemaps"
                  f" ({len(meta[kind]['pending_sitemaps'])} sin leer)")
    for flag in meta["flags"]:
        print(f"  aviso: {flag}")
    print(f"descubrimiento → {folder.relative_to(ROOT)}")


def cmd_select(spec_path: Path, discovery: Path | None) -> None:
    from . import selection
    try:
        spec = selection.read_spec(spec_path)
        result = selection.select(spec, discovery or selection.latest_discovery(spec["store"]))
    except selection.SelectionError as e:
        sys.exit(f"train: {e}")
    out = selection.write_selection(spec_path, result)
    c = result["counts"]
    print(f"{c['urls']} URL → {c['products']} productos ({c.get('variant', 0)} variantes, "
          f"{c.get('excluded_department', 0)} de departamentos excluidos, {c.get('disallowed', 0)} excluidas por robots.txt)")
    print(f"{c['types']} tipos, {c['eligible_types']} con productos suficientes en {c['departments']} departamentos")
    print(f"seleccionados: {c['selected_types']} tipos de {c['selected_departments']} departamentos, "
          f"{c['pages']} fichas (piloto: {c['pilot_pages']})")
    print(f"selección → {out.relative_to(ROOT)}")


def cmd_capture(args: list) -> None:
    from capture import pages
    from . import collect, selection
    path, flags = Path(args[0]), args[1:]
    pilot = "--pilot" in flags
    sel = json.loads(path.read_text(encoding="utf-8"))
    if "--status" in flags:
        st = collect.status(sel, path, pilot)
        for kind, (n, target) in st["types"].items():
            print(f"  {kind:45} {n}/{target}")
        print(f"capturadas {st['captured']}/{st['target']} · " +
              ", ".join(f"{k} {v}" for k, v in sorted(st["outcomes"].items())))
        return
    if not pages.engine_available():
        # On the host: the capture engine (Chrome, websockets) runs in the container
        code = subprocess.call([str(ROOT.parent / "bin/run"), "dev", "exec", "python", "-m", "demand_engine.demand.train",
                                "capture", str(path.resolve().relative_to(ROOT.parent)), *flags])
        if code:
            print("train: capture se ejecuta en el contenedor; si no está levantado: bin/run dev up", file=sys.stderr)
        sys.exit(code)
    max_visits = int(flags[flags.index("--max") + 1]) if "--max" in flags else None
    try:
        spec = selection.read_spec(ROOT / sel["spec"])
        records = collect.capture(spec, path, pilot, max_visits, "--ignore-hours" in flags,
                                  out=lambda m: print(m, flush=True))
    except selection.SelectionError as e:
        sys.exit(f"train: {e}")
    print(f"{len(records)} resultados en esta ejecución; estado: train capture {args[0]} --status"
          + (" --pilot" if pilot else ""))


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    cmd, rest = args[0], args[1:]
    if cmd == "discover" and len(rest) == 1:
        cmd_discover(Path(rest[0]))
    elif cmd == "select" and len(rest) in (1, 2):
        cmd_select(Path(rest[0]), Path(rest[1]) if len(rest) == 2 else None)
    elif cmd == "capture" and rest:
        cmd_capture(rest)
    elif cmd == "batch":
        from .batch import main as batch_main
        batch_main(rest)
    elif cmd == "index":
        cmd_index([Path(a) for a in rest])
    elif cmd == "resolving" and rest[:1] == ["refs"] and rest[1:]:
        cmd_resolving_refs(rest[1:])
    elif cmd == "induce":
        cmd_induce([Path(a) for a in rest])
    elif cmd == "compile":
        cmd_compile([Path(a) for a in rest])
    elif cmd == "report" and rest:
        cmd_report(rest)
    else:
        sys.exit(__doc__)


if __name__ == "__main__":
    main()
