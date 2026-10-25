"""Training of the demand model, first version (D-044, D-045): importance rules induced along the Shopify tree.

Usage:
  train index                     rebuild the trait index of the sources (catalog/traits.json) and,
                                  if missing, the list of categories without a block of their own
  train induce [RUN_DIR ...]      induce candidate importance rules from the catalog and the votes
                                  of the models assembled in the runs (catalog/rules/importance.candidate.json)
  train compile [RUN_DIR ...]     validate the candidate against the current rules (no metric worse,
                                  one better) and, if accepted, publish it and compile the catalog,
                                  including the blocks generated at runtime
  train report RUN_A [RUN_B] [--out FILE]
                                  aggregated report: metrics (control coverage, declared facts without
                                  question, stability between runs, coherence), rules, votes against
                                  the framework, what was used without compiling and divergences
                                  (written to training/reports/NAME-report.md unless --out)

A rule lives in a class and climbs to the parent only if at least two children with data
share it and none contradicts it; within a class it is the weighted majority (a tie goes to
the higher level). Rules never climb above the Shopify verticals. Whether identity and
content are critical is decided by a global rule; fixed measures and the general layer are
the framework and are not induced.
"""
import datetime
import json
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

from .catalog import (CAT_DIR, CATALOG, COMPILED, CRITICAL_TRAITS, EMPTY, FIXED, LEVELS, NO_RULE, NOT_RELEVANT, ROOT,
                      RULES, RUNTIME_DIR, TRAITS, UNCOMPILED, VOTES, blocks_by_node, category_name, chain, depth,
                      load_blocks, load_empty, load_rules, load_traits, majority, parent, protected, rank, read_json,
                      relevance, requirement_trait, resolve, save_block, write_json)
from ..refs import pins
from .text import covers, match_names, stems

CANDIDATE = CATALOG / "rules" / "importance.candidate.json"
CASES = ROOT / "cases"
REPORTS = ROOT / "training" / "reports"  # results of the training: versioned, unlike the runs


# Index

def cmd_index() -> None:
    traits = load_traits()
    seen = defaultdict(Counter)
    for b in load_blocks().values():
        for r in b["requirements"]:
            if r.get("trait"):
                for s in r.get("sources", []):
                    seen[s][r["trait"]] += 1
    traits["sources"] = {s: c.most_common(1)[0][0] for s, c in sorted(seen.items()) if len(c) == 1}
    write_json(TRAITS, traits)
    ambiguous = {s: dict(c) for s, c in seen.items() if len(c) > 1}
    print(f"índice de rasgos: {len(traits['sources'])} fuentes; {len(ambiguous)} con rasgos distintos según el requisito")
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


def catalog_points(blocks: dict, src_traits: dict) -> list:
    points = []
    for b in blocks.values():
        for r in b["requirements"]:
            trait, _ = requirement_trait(r, src_traits)
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


def vote_points(models: dict) -> list:
    points = []
    for run, cases in models.items():
        for case, model in cases.items():
            for r in model_requirements(model):
                if r.get("vote") in LEVELS and r.get("trait") and r.get("classes"):
                    for node in r["classes"]:
                        points.append({"trait": r["trait"], "node": node, "label": r["vote"], "w": 1 / len(r["classes"]),
                                       "ref": f"{case}:{r['id']}", "from": run})
    return points


# Induction

def induce(points: list) -> dict:
    glob, violations = {}, []
    for t in CRITICAL_TRAITS:
        pts = [p for p in points if p["trait"] == t]
        if pts:
            crit = sum(p["w"] for p in pts if p["label"] == "crítico")
            glob[t] = "crítico" if crit and crit >= sum(p["w"] for p in pts) - crit else "no crítico"
    direct = defaultdict(lambda: defaultdict(Counter))
    for p in points:
        t, label = p["trait"], p["label"]
        if t in FIXED or (t in CRITICAL_TRAITS and glob.get(t) == "crítico"):
            continue
        if label == "crítico":
            if t not in CRITICAL_TRAITS:
                violations.append(p)
            label = "principal"
        direct[t][p["node"]][label] += p["w"]
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
    for t, value in sorted(glob.items()):
        rules.append({"id": f"imp:{t}@*", "trait": t, "node": "*", "importance": value, "kind": "global"})
    return {"global": glob, "tree": tree, "rules": rules,
            "violations": [{"ref": p["ref"], "trait": p["trait"], "node": p["node"], "from": p["from"]} for p in violations]}


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
    src_traits = load_traits()["sources"]
    models = load_models(run_dirs)
    points = catalog_points(blocks, src_traits) + vote_points(models)
    candidate = induce(points)
    rel_table, rel_rules, rel_conflicts = induce_relevance(relevance_points(blocks, models), blocks)
    candidate.update({"relevance": rel_table, "relevance_conflicts": rel_conflicts})
    candidate["rules"] += rel_rules
    current = load_rules()
    candidate.update({"version": str(int(current.get("version", "0")) + 1), "induced": datetime.date.today().isoformat(),
                      "points": {"catalog": sum(1 for p in points if p["from"] == "catálogo"),
                                 "votes": sum(1 for p in points if p["from"] != "catálogo")},
                      "runs": [str(d) for d in run_dirs], "refs": pins()})
    write_json(CANDIDATE, candidate)
    kinds = Counter(r["kind"] for r in candidate["rules"])
    print(f"candidata {candidate['version']}: {len(candidate['rules'])} reglas ({', '.join(f'{v} {k}' for k, v in kinds.items())}) "
          f"de {candidate['points']['catalog']} etiquetas del catálogo y {candidate['points']['votes']} votos; "
          f"{len(candidate['violations'])} votos críticos fuera de los rasgos que lo admiten")
    added = set(candidate["tree"].items()) - set(current.get("tree", {}).items())
    removed = set(current.get("tree", {}).items()) - set(candidate["tree"].items())
    print(f"  frente a la versión {current.get('version', '0')}: {len(added)} reglas nuevas o cambiadas, {len(removed)} retiradas")
    return candidate


# Metrics

def catalog_levels(blocks: dict, src_traits: dict, rules: dict) -> list:
    out = []
    for b in blocks.values():
        for r in b["requirements"]:
            trait, _ = requirement_trait(r, src_traits)
            level, rule = resolve(trait, [b["shopify"]], rules, r.get("sources", []))
            out.append((b["shopify"], trait, level or seed_label(r), rule or NO_RULE, r))
    return out


def model_level(r: dict, rules: dict) -> str:
    level, _ = resolve(r.get("trait"), r.get("classes", []), rules, r.get("sources", []))
    return level or r.get("vote") or r.get("importance")


def incoherence(groups: dict) -> int:
    """Requirements whose importance differs from the majority of their group (same class and trait)."""
    return sum(len(levels) - Counter(levels).most_common(1)[0][1] for levels in groups.values() if levels)


def coherence(blocks: dict, src_traits: dict, models: dict, rules: dict) -> dict:
    cat_groups, model_groups = defaultdict(list), defaultdict(list)
    for node, trait, level, _, _ in catalog_levels(blocks, src_traits, rules):
        cat_groups[(node, trait)].append(level)
    for run, cases in models.items():
        for case, model in cases.items():
            for r in model_requirements(model):
                model_groups[(run, case, tuple(r.get("classes", [])), r.get("trait"))].append(model_level(r, rules))
    return {"catalog": incoherence(cat_groups), "models": incoherence(model_groups),
            "catalog_requirements": sum(len(v) for v in cat_groups.values()),
            "catalog_without_rule": sum(1 for *_, rule, _ in catalog_levels(blocks, src_traits, rules) if rule == NO_RULE)}


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
    runs = list(models)
    if len(runs) < 2:
        return []
    a, b = models[runs[0]], models[runs[1]]
    return [(case, a[case], b[case]) for case in sorted(a.keys() & b.keys())]


def stability(models: dict, rules: dict) -> dict:
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
        out["same_importance"] += sum(model_level(ra[i], rules) == model_level(rb[i], rules) for i in common)
    return dict(out)


def better_or_equal(cur: dict, cand: dict) -> tuple:
    worse, better = [], []
    for name, c, n, lower_is_better in (
            ("coherencia del catálogo", cur["coherence"]["catalog"], cand["coherence"]["catalog"], True),
            ("coherencia de los modelos", cur["coherence"]["models"], cand["coherence"]["models"], True),
            ("estabilidad de la importancia", cur["stability"].get("same_importance", 0), cand["stability"].get("same_importance", 0), False),
            ("requisitos del catálogo sin regla", cur["coherence"]["catalog_without_rule"], cand["coherence"]["catalog_without_rule"], True),
            ("coherencia de relevancia", cur["relevance"]["incoherence"], cand["relevance"]["incoherence"], True),
            ("hechos declarados sin pregunta", cur["relevance"]["coverage_gaps"], cand["relevance"]["coverage_gaps"], True)):
        if n == c:
            continue
        ((better if n < c else worse) if lower_is_better else (better if n > c else worse)).append(f"{name}: {c} → {n}")
    return worse, better


def evaluate(rules: dict, blocks: dict, src_traits: dict, models: dict) -> dict:
    return {"coherence": coherence(blocks, src_traits, models, rules), "stability": stability(models, rules),
            "relevance": relevance_metrics(models, rules)}


# Compile

def family(rules: dict, name: str) -> dict:
    """The part of a rule set that belongs to one family: importance (tree and global) or relevance."""
    if name == "importancia":
        return {"global": rules.get("global", {}), "tree": rules.get("tree", {}), "violations": rules.get("violations", []),
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
    blocks, src_traits, models = load_blocks(), load_traits()["sources"], load_models(run_dirs)
    m_cur = evaluate(current, blocks, src_traits, models)
    first = current.get("version", "0") == "0"
    parts, decisions = {}, {}
    for name in ("importancia", "relevancia"):
        cur_part, cand_part = family(current, name), family(candidate, name)
        other = family(current, "relevancia" if name == "importancia" else "importancia")
        trial = combine(cand_part, other) if name == "importancia" else combine(other, cand_part)
        unchanged = {k: v for k, v in cand_part.items() if k != "rules"} == {k: v for k, v in cur_part.items() if k != "rules"}
        m_trial = evaluate(trial, blocks, src_traits, models)
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
                             "metrics": evaluate(rules, blocks, src_traits, models)}
        write_json(RULES, rules)
        print(f"reglas {rules['version']} publicadas ({'; '.join(candidate['decision']['better']) or 'primera versión'})")
    changed = 0
    for b in blocks.values():
        before = json.dumps(b["requirements"], ensure_ascii=False) + str(b.get("status"))
        for r in b["requirements"]:
            r.setdefault("seed_importance", seed_label(r))
            trait, _ = requirement_trait(r, src_traits)
            level, rule = resolve(trait, [b["shopify"]], rules, r.get("sources", []))
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
    rules, blocks, src_traits = load_rules(), load_blocks(), load_traits()["sources"]
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
    st = stability(models, rules)
    if st:
        lines += ["", "### Estabilidad entre ejecuciones", "", "| Medida | Resultado |", "|---|---|",
                  f"| Composición (categorías y alias) | {st['composition']}/{st['cases']} |",
                  f"| Clave del modelo | {st['key']}/{st['cases']} |",
                  f"| Especializaciones | {st['specializations']}/{st['cases']} |",
                  f"| Aplicación de la oferta | {st['application']}/{st['cases']} |",
                  f"| Importancia en los requisitos de categoría comunes | {st['same_importance']}/{st['common']} |"]
    coh = coherence(blocks, src_traits, models, rules)
    lines += ["", "### Coherencia", "",
              f"Requisitos con el mismo rasgo y la misma clase e importancia distinta: {coh['catalog']} en el catálogo "
              f"({coh['catalog_requirements']} requisitos) y {coh['models']} en los modelos.", ""]
    # rules
    decided = Counter(rule for _, _, _, rule, _ in catalog_levels(blocks, src_traits, rules))
    lines += ["## Reglas de importancia", ""]
    imp_rules = [r for r in rules.get("rules", []) if r["kind"] != "relevancia"]
    rel_rules = [r for r in rules.get("rules", []) if r["kind"] == "relevancia"]
    if imp_rules:
        kinds = Counter(r["kind"] for r in imp_rules)
        plural = {"general": "generales", "específica": "específicas", "global": "globales"}
        lines.append(f"{len(imp_rules)} reglas: " + ", ".join(f"{v} {plural.get(k, k)}" for k, v in kinds.items())
                     + f". Etiquetas del catálogo: {rules.get('points', {}).get('catalog', 0)}; votos: {rules.get('points', {}).get('votes', 0)}.")
        if rules.get("accepted", {}).get("better"):
            lines.append(f"Aceptada porque mejora: {'; '.join(rules['accepted']['better'])}.")
        lines += ["", "| Regla | Rasgo | Clase | Importancia | Tipo | Requisitos del catálogo que decide |", "|---|---|---|---|---|---|"]
        for r in sorted(imp_rules, key=lambda r: (r["trait"], depth(r["node"]) if r["node"] != "*" else -1, r["node"])):
            node = "todas" if r["node"] == "*" else f"{category_name(r['node'])} ({r['node']})"
            lines.append(f"| `{r['id']}` | {r['trait']} | {node} | {r['importance']} | {r['kind']}"
                         f"{' (sube desde las hijas)' if r.get('climbed') else ''} | {decided.get(r['id'], 0)} |")
        fixed = {k: v for k, v in decided.items() if k.startswith("marco:")}
        lines += ["", "Reglas del marco: " + (", ".join(f"`{k}` ({v})" for k, v in sorted(fixed.items())) or "—")
                  + f" · requisitos sin regla: {decided.get(NO_RULE, 0)}."]
        if rules.get("violations"):
            lines += ["", f"Votos críticos en rasgos que no lo admiten (cuentan como principal): {len(rules['violations'])}."]
            for v in rules["violations"][:15]:
                lines.append(f"- {v['ref']} ({v['trait']}, {v['from']})")
    else:
        lines.append("Sin reglas compiladas todavía.")
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
    # vote agreement
    agree = total = 0
    against = Counter()
    for run, cases in models.items():
        for m in cases.values():
            for r in model_requirements(m):
                if r.get("vote") in LEVELS and not r.get("provisional"):
                    total += 1
                    if r["vote"] == r["importance"]:
                        agree += 1
                    else:
                        against[(r["rule"], r["vote"])] += 1
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


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    cmd, rest = args[0], args[1:]
    if cmd == "index":
        cmd_index()
    elif cmd == "induce":
        cmd_induce([Path(a) for a in rest])
    elif cmd == "compile":
        cmd_compile([Path(a) for a in rest])
    elif cmd == "report" and rest:
        cmd_report(rest)
    else:
        sys.exit(__doc__)
