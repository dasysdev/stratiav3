"""Execution of the demand model (D-041, D-044, D-045): blocks for a class, runtime blocks and assembly.

Usage:
  model blocks CATEGORY_ID [...]      catalog blocks of the classes and their ancestors, with their
                                      requirements (id, trait, question), the general layer and the
                                      categories that have no block yet
  model register BLOCK.json [--replace]
                                      register a block generated at runtime (status «no compilado»);
                                      a category that already has a runtime block is refused (another
                                      case of the batch generated it), unless --replace
  model register --empty CATEGORY_ID  register a category without requirements of its own
  model check OUTPUT.json             assemble in memory and report what is missing (for the classifier)
  model check --catalog               check every block of the catalog and the general layer: ids, traits,
                                      origins and sources, and the resolving information of each requirement
  model assemble OUTPUT.json          build the demand model from a classifier output (rulebook v2 or v3):
                                      writes <case>.model.json and <case>.model.md next to it and
                                      appends what was used without compiling to the queue
  model show MODEL.json               print the readable version of an assembled model
  model hints check                   check the catalog of assessment hints (fields, id, origin, destination,
                                      same destination and property) and the comparison marks (D-136, D-139)
  model hints find REQ_ID [...]       hints of each requirement by its tags (type, source, id), code only (D-134)

The classifier decides the composition, specializations, inferred questions, application
and votes (importance and, from rulebook v3, trait), and says which contribution of the
resolving information each declared fact is; everything else is deterministic: blocks come
from the catalog, importance from the compiled rules (an exception by requirement and class
first; the vote only where no rule applies), the resolving information from the catalog
and the compiled observations, and the key and name from the blocks.
"""
import datetime
import fcntl
import json
import sys
from contextlib import contextmanager
from pathlib import Path

from ..refs import pins
from . import hints, resolving
from .catalog import (CAT_DIR, COMPILED, ROOT, DOUBTFUL, ESP_ORDER, EMPTY, LEVELS, NO_RULE, NOT_RELEVANT, QUEUE,
                      RUNTIME_DIR, UNCOMPILED, VOTES, blocks_by_node, category_name, chain, class_nodes_for, depth,
                      load_blocks, load_empty, load_gen, load_resolving, load_rules, load_traits, protected, read_json,
                      relevance, requirement_trait, resolve, trait_index, write_json)

EXCLUDED_ROLES = ("estético", "promocional", "beneficio reclamado")  # declared facts that need no question (D-045)


def cmd_blocks(ids: list) -> None:
    blocks, empty = load_blocks(), load_empty()
    by_node = blocks_by_node(blocks)
    src_traits, voted = trait_index()
    gen, rules, compiled = load_gen(), load_rules(), load_resolving()
    traits = load_traits()
    print("RASGOS: " + ", ".join(traits["vocabulary"]) + (f" · propuestos: {', '.join(traits.get('proposed', {}))}"
                                                           if traits.get("proposed") else ""))
    print("\nCAPA GENERAL (fija; no se vota)")
    for b in gen["blocks"]:
        trigger = f" · si {b['trigger']}" if b.get("trigger") else ""
        print(f"  [{b['id']}{trigger}]")
        for r in b["requirements"]:
            print(f"    {r['id']}: {r['question']}")
            print_resolving(r, compiled, "      ")
    missing = []
    for node in sorted({n for c in ids for n in chain(c)}, key=lambda n: (depth(n), n)):
        b = by_node.get(node)
        role = "categoría" if node in ids else "sector"
        if b is None:
            state = {"catálogo": "sin requisitos propios", "ejecución": "sin requisitos propios (ejecución)"}.get(empty.get(node))
            if state is None:
                missing.append(node)
                state = "FALTA EL BLOQUE: genéralo (paso 4 del reglamento)"
            print(f"\n{node} {category_name(node)} ({role}) — {state}")
            continue
        print(f"\n{node} {category_name(node)} ({role}) — {b['id']}@{b.get('version')} · {b.get('status')} · {b['_where']}")
        for r in b["requirements"]:
            trait, _ = requirement_trait(r, src_traits, voted)
            excluded, _ = relevance(r["id"], class_nodes_for(node, ids), rules)
            print(f"  {r['id']} [{trait or '?'}] {r['question']}" + ("  [excluido en esta clase: vótalo igualmente]" if excluded else ""))
            print_resolving(r, compiled, "    ")
    if missing:
        print(f"\nCategorías sin bloque: {' '.join(missing)}")


def print_resolving(r: dict, compiled: dict, indent: str) -> None:
    """The contributions of a requirement, for the classifier to name the one each declared fact is (D-063)."""
    items = resolving.for_model(r, compiled)
    if items:
        print(f"{indent}aportaciones: " + " · ".join(f"{c['contribution']} [{c.get('component') or '—'}]" for c in items))


@contextmanager
def registering():
    """Agents of a batch register blocks in parallel: one at a time (T-026)."""
    lock = ROOT / "var" / "register.lock"
    lock.parent.mkdir(parents=True, exist_ok=True)
    with open(lock, "w") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        yield


def cmd_register(args: list) -> None:
    with registering():
        register([a for a in args if a != "--replace"], "--replace" in args)


def register(args: list, replace: bool) -> None:
    traits = load_traits()
    src_traits = traits["sources"]
    blocks = load_blocks()
    by_node = blocks_by_node(blocks)
    if args[0] == "--empty":
        node = args[1]
        if node in by_node:
            sys.exit(f"model: {node} ya tiene el bloque {by_node[node]['id']}")
        data = read_json(EMPTY) if EMPTY.exists() else {"catalog": [], "runtime": []}
        if node not in data["catalog"] + data["runtime"]:
            data["runtime"].append(node)
            write_json(EMPTY, data)
        print(f"{node}: registrada sin requisitos propios (ejecución)")
        return
    block = read_json(Path(args[0]))
    errors = []
    proposed = {p.get("name"): p for p in block.get("proposed_traits", [])}
    for name, p in proposed.items():
        if not name or not p.get("definition"):
            errors.append(f"rasgo propuesto «{name}» sin nombre o sin definición")
    vocabulary = set(traits["vocabulary"]) | set(traits.get("proposed", {})) | set(proposed)
    bid = block.get("id", "")
    if not bid.startswith("cat.") or not block.get("shopify"):
        errors.append("el bloque necesita id «cat.<nombre>» y «shopify»")
    if bid in blocks and blocks[bid]["_where"] == "catálogo":
        errors.append(f"{bid} ya existe en el catálogo")
    current = by_node.get(block.get("shopify"))
    if current and current["id"] != bid:
        errors.append(f"la categoría {block.get('shopify')} ya tiene el bloque {current['id']}")
    elif current and current["_where"] == "ejecución" and not replace:
        errors.append(f"la categoría {block.get('shopify')} ya tiene el bloque {bid}, generado en ejecución (quizá por "
                      "otro caso del lote): no lo redactes de nuevo; vuelve a «bin/model blocks» y vota sus requisitos. "
                      "--replace solo para corregir un bloque que registraste tú")
    if block.get("shopify") in load_empty():
        errors.append(f"la categoría {block.get('shopify')} está registrada sin requisitos propios")
    overridden = []
    for i, r in enumerate(block.get("requirements", []), 1):
        r.setdefault("id", f"{bid}/{i:02d}")
        if not r["id"].startswith(bid + "/"):
            errors.append(f"{r['id']}: el identificador no es del bloque")
        if not r.get("question"):
            errors.append(f"{r['id']}: falta la pregunta")
        if r.get("trait") not in vocabulary:
            errors.append(f"{r['id']}: rasgo «{r.get('trait')}» fuera del vocabulario (propón uno nuevo en «proposed_traits», "
                          "con su definición)")
        errors += [f"{r['id']}: {e}" for e in resolving_errors(r.get("resolving_info", []), ("referencias", "inferida"))]
        if r.get("vote") not in VOTES:
            errors.append(f"{r['id']}: voto «{r.get('vote')}» no válido")
        trait, origin = requirement_trait(r, src_traits)
        if origin == "fuente" and trait != r.get("trait"):
            overridden.append(f"{r['id']}: {r.get('trait')} → {trait} (rasgo de sus fuentes)")
            r["trait"] = trait
    if errors:
        sys.exit("model: bloque no registrado:\n  " + "\n  ".join(errors))
    block.update({"type": "categoría", "status": UNCOMPILED, "version": "0",
                  "generated": datetime.date.today().isoformat()})
    path = RUNTIME_DIR / f"{bid.removeprefix('cat.')}.json"
    write_json(path, block)
    print(f"{bid}: registrado en {path.relative_to(CAT_DIR.parent.parent)} ({len(block['requirements'])} requisitos, no compilado)")
    for line in overridden:
        print(f"  {line}")


def resolving_errors(items: list, origins: tuple) -> list:
    """What is wrong in a list of resolving information (D-063): each contribution with its component and origin."""
    errors = []
    for c in items:
        if not (c.get("contribution") or "").strip() or not (c.get("component") or "").strip():
            errors.append(f"aportación sin nombre o sin componente: {c}")
        elif c.get("origin") not in origins:
            errors.append(f"aportación «{c['contribution']}»: origen «{c.get('origin')}» no válido ({', '.join(origins)})")
    return errors


def supported(items: list, sources: list) -> list:
    """A contribution with a source origin is supported only by the requirement's own sources; an inferred one by none."""
    errors = []
    for c in items:
        if c.get("origin") == "inferida":
            if c.get("support"):
                errors.append(f"aportación «{c.get('contribution')}»: una inferida no lleva respaldo")
        elif not c.get("support"):
            errors.append(f"aportación «{c.get('contribution')}»: sin respaldo")
        elif set(c["support"]) - set(sources):
            errors.append(f"aportación «{c.get('contribution')}»: respaldo fuera de las fuentes del requisito")
    return errors


def block_problems(block: dict, vocabulary: set) -> list:
    """What is wrong in a category block of the catalog: ids of the block, question, trait, importance, origin and
    sources (an inferred question has none), and the resolving information of each requirement (D-060, D-063)."""
    problems, bid = [], block.get("id", "")
    for r in block.get("requirements", []):
        rid = r.get("id", "?")
        errors = []
        if not rid.startswith(bid + "/"):
            errors.append("el identificador no es del bloque")
        if not r.get("question"):
            errors.append("falta la pregunta")
        if r.get("trait") not in vocabulary:
            errors.append(f"rasgo «{r.get('trait')}» fuera del vocabulario")
        if (r.get("importance") or r.get("vote")) not in LEVELS:
            errors.append("sin importancia ni voto válidos")
        if r.get("origin") == "inferida" and r.get("sources"):
            errors.append("cuestión inferida con fuentes")
        elif r.get("origin") in ("referencias", "normativa", "paa") and not r.get("sources"):
            errors.append(f"origen «{r['origin']}» sin fuentes")
        elif r.get("origin") == "paa" and not all(s.startswith("paa-q:") for s in r["sources"]):
            # D-097: a requirement that enters only through PAA has its questions as sources
            errors.append("origen «paa» con fuentes que no son preguntas PAA (paa-q:)")
        elif r.get("origin") not in ("referencias", "normativa", "inferida", "paa"):
            errors.append(f"origen «{r.get('origin')}» no válido")
        items = r.get("resolving_info") or []
        if not items:
            errors.append("sin información resolutiva")
        errors += resolving_errors(items, ("referencias", "inferida")) + supported(items, r.get("sources", []))
        problems += [f"{rid}: {e}" for e in errors]
    return problems


def gen_problems(gen: dict) -> list:
    """The resolving information of the general layer: «marco» from the law that is a source of each requirement,
    approved by the user, and inferred contributions where there is no law (D-063, D-065)."""
    problems = []
    for b in gen["blocks"]:
        for r in b["requirements"]:
            items = r.get("resolving_info") or []
            errors = [] if items else ["sin información resolutiva"]
            errors += resolving_errors(items, ("marco", "referencias", "inferida")) + supported(items, r.get("sources", []))
            problems += [f"{r['id']}: {e}" for e in errors]
    return problems


def cmd_check_catalog() -> None:
    blocks, traits = load_blocks(), load_traits()
    vocabulary = set(traits["vocabulary"]) | set(traits.get("proposed", {}))
    problems, seen = [], {}
    for b in blocks.values():
        problems += block_problems(b, vocabulary | {p.get("name") for p in b.get("proposed_traits", [])})
        for r in b["requirements"]:
            if r.get("id") in seen:
                problems.append(f"{r['id']}: repetido en {seen[r['id']]} y {b['id']}")
            seen[r.get("id")] = b["id"]
    problems += gen_problems(load_gen())
    contributions = sum(len(r.get("resolving_info", [])) for b in blocks.values() for r in b["requirements"])
    print(f"catálogo: {len(blocks)} bloques, {len(seen)} requisitos, {contributions} aportaciones; capa general incluida")
    print("  correcto" if not problems else "  problemas:\n    " + "\n    ".join(problems))
    if problems:
        sys.exit(1)


def requirement_entry(r: dict, trait: str, classes: list, rules: dict, vote, trait_vote=None, compiled=None) -> dict:
    """Relevance first (D-050), then importance (D-045, D-058: the exception of the requirement in its class
    first). Doubt does not exclude: a «no relevante» vote without a compiled rule keeps the requirement as
    complementary and marks it."""
    sources = r.get("sources", [])
    excluded, rel_rule = relevance(r["id"], classes, rules)
    if excluded and protected(trait, r.get("origin"), sources):
        excluded, rel_rule = False, "marco:no-excluible"
    level, rule = resolve(trait, classes, rules, sources, r["id"])
    provisional = level is None
    if provisional:
        fallback = vote if vote in LEVELS else r.get("vote") if r.get("vote") in LEVELS else r.get("importance")
        level, rule = ("complementario" if vote == NOT_RELEVANT else fallback), NO_RULE
    doubtful = vote == NOT_RELEVANT and not excluded and not protected(trait, r.get("origin"), sources)
    return {"id": r["id"], "question": r.get("question"), "dimension": r.get("dimension"), "entity": r.get("entity"),
            "trait": trait, "importance": level, "rule": rule, "vote": vote, "trait_vote": trait_vote,
            "provisional": provisional or doubtful, "doubtful": doubtful, "excluded": excluded, "relevance_rule": rel_rule,
            "classes": classes, "origin": r.get("origin"), "sources": sources,
            "applicability": r.get("applicability"),
            "resolving_info": resolving.for_model(r, compiled or {})}


def split(entries: list) -> tuple:
    return [e for e in entries if not e["excluded"]], [e for e in entries if e["excluded"]]


def assemble(out_path: Path) -> dict:
    out = read_json(out_path)
    blocks, empty = load_blocks(), load_empty()
    by_node = blocks_by_node(blocks)
    src_traits, voted = trait_index()
    rules, gen, compiled = load_rules(), load_gen(), load_resolving()
    cats = out.get("composition", {}).get("categories", [])
    classes = [c["shopify"] for c in cats if not c.get("alias")]
    aliases = [c["shopify"] for c in cats if c.get("alias")]
    votes, trait_votes = out.get("votes", {}), out.get("trait_votes", {})
    model_blocks, missing = [], []
    for node in sorted({n for c in classes for n in chain(c)}, key=lambda n: (depth(n), n)):
        b = by_node.get(node)
        if b is None:
            if node not in empty:
                missing.append(node)
            continue
        scope = class_nodes_for(node, classes)
        reqs = []
        for r in b["requirements"]:
            trait, _ = requirement_trait(r, src_traits, voted)
            reqs.append(requirement_entry(r, trait, scope, rules, votes.get(r["id"]), trait_votes.get(r["id"]), compiled))
        kept, excluded = split(reqs)
        model_blocks.append({"id": b["id"], "type": "categoría", "position": "categoría" if node in classes else "sector",
                             "name": b.get("name"), "shopify": node, "version": b.get("version"), "status": b.get("status"),
                             "where": b["_where"], "requirements": kept, "excluded": excluded})
    for e in out.get("specializations", []):
        reqs = []
        for i, r in enumerate(e.get("requirements", []), 1):
            r.setdefault("id", f"{e['id']}/{i:02d}")
            reqs.append(requirement_entry(r, r.get("trait"), classes, rules, r.get("vote"), r.get("trait"), compiled))
        model_blocks.append({"id": e["id"], "type": "especialización", "name": e.get("name"), "order": e.get("order"),
                             "trigger": e.get("trigger"), "support": e.get("support", []), "version": "0",
                             "status": UNCOMPILED, "where": "ejecución", "requirements": reqs})
    inferred = []
    for i, r in enumerate(out.get("inferred", []), 1):
        r.setdefault("id", f"inf/{i:02d}")
        host = next((b for b in model_blocks if b["id"] == r.get("block")), None)
        scope = class_nodes_for(host.get("shopify") if host else None, classes)
        entry = requirement_entry(r, r.get("trait"), scope, rules, r.get("vote"), r.get("trait"), compiled)
        # D-088: with a source the block neither asks nor excludes, it is a proposal to the block
        proposal = bool(r.get("sources"))
        entry.update({"block": r.get("block"), "origin": "referencias" if proposal else "inferida",
                      "rationale": r.get("rationale"), "block_proposal": proposal})
        inferred.append(entry)
    # D-047: the model goes with the product, the application with the offer; conditions that do
    # not hold in the offer stay greyed (NA); product-scope conditional blocks join the model.
    triggered = {a["block"] if isinstance(a, dict) else a for a in out.get("application", [])}
    scope_of = {b["id"]: b.get("scope", "oferta") for b in gen["blocks"] if b["id"] != "gen"}
    product_gen = sorted(a for a in triggered if scope_of.get(a) == "producto")
    application = sorted(a for a in triggered if scope_of.get(a, "oferta") == "oferta")
    short = {b["id"]: b.get("name", b["id"])[:1].lower() + b.get("name", b["id"])[1:] for b in gen["blocks"]}
    general = []
    for b in gen["blocks"]:
        scope = "universal" if b["id"] == "gen" else scope_of[b["id"]]
        if scope == "producto" and b["id"] not in triggered:
            continue
        applies = scope != "oferta" or b["id"] in triggered
        general.append({"id": b["id"], "name": b.get("name"), "version": b.get("version"), "scope": scope, "applies": applies,
                        "requirements": [{"id": r["id"], "question": r["question"], "entity": r.get("entity"),
                                          "importance": r.get("importance"), "rule": "marco:capa-general", "applies": applies,
                                          "applicability": r.get("applicability", "universal"), "origin": r.get("origin"),
                                          "resolving_info": resolving.for_model(r, compiled)}
                                         for r in b["requirements"]]})
    esp = sorted((b for b in model_blocks if b["type"] == "especialización"),
                 key=lambda b: (ESP_ORDER.index(b["order"]) if b.get("order") in ESP_ORDER else len(ESP_ORDER), b["id"]))
    versions = {b["id"]: b.get("version") for b in gen["blocks"]}
    key = {"model": [f"gen@{gen['version']}"] + [f"{b['id']}@{b['version']}" for b in model_blocks if b["type"] == "categoría"]
                    + [f"{b['id']}@{b['version']}" for b in esp] + [f"{g}@{versions[g]}" for g in product_gen]}
    offer = {"application": application, "label": ", ".join(short[a] for a in application) or "estándar"}
    # D-077: the name shows the whole composition; sectors go first, general to specific, those of
    # the same level joined with «+».
    levels = {}
    for b in model_blocks:
        if b.get("position") == "sector":
            levels.setdefault(depth(b["shopify"]), []).append(category_name(b["shopify"]))
    name = " › ".join([" + ".join(names) for _, names in sorted(levels.items())]
                      + [" + ".join(category_name(c) for c in classes)])
    if aliases:
        name += f" ({', '.join(category_name(a) for a in aliases)})"
    if esp or product_gen:
        name += " · " + ", ".join([b.get("name") or b["id"] for b in esp] + [short[g] for g in product_gen])
    ids = {r["id"] for b in model_blocks for r in b["requirements"]} | {r["id"] for r in inferred} \
        | {r["id"] for b in general for r in b["requirements"]}
    counted = [d for d in out.get("declared", []) if d.get("role") not in EXCLUDED_ROLES]
    gaps = [d for d in counted if d.get("answers") not in ids]
    contributions = [{"answers": d["answers"], **c} for d in counted if d.get("answers") in ids
                     for c in [resolving.contribution(d)] if c]
    provisional = [r["id"] for b in model_blocks for r in b["requirements"] if r["provisional"] and r["rule"] == NO_RULE] \
        + [r["id"] for r in inferred if r["provisional"] and r["rule"] == NO_RULE]
    doubtful = [r["id"] for b in model_blocks for r in b["requirements"] if r["doubtful"]] \
        + [r["id"] for r in inferred if r["doubtful"]]
    model = {
        "case": out.get("case"), "product": out.get("product"), "url": out.get("url"),
        "engine": {"rulebook": out.get("rulebook"), "rules": rules.get("version"), "refs": pins(),
                   "assembled": datetime.date.today().isoformat()},
        "key": key, "name": name, "offer": offer,
        "composition": {"classes": classes, "aliases": aliases},
        "general": general, "blocks": model_blocks, "inferred": inferred,
        "uncompiled": {"blocks": [b["id"] for b in model_blocks if b["status"] != COMPILED],
                       "inferred": [r["id"] for r in inferred], "without_rule": provisional, "doubtful_relevance": doubtful,
                       "missing_blocks": missing},
        "excluded": [{"id": r["id"], "block": b["id"], "question": r["question"], "rule": r["relevance_rule"]}
                     for b in model_blocks for r in b.get("excluded", [])],
        "coverage": {"declared_counted": len(counted), "answers": [d.get("answers") for d in counted],
                     "gaps": [{"feature": d.get("feature"), "evidence": d.get("evidence")} for d in gaps],
                     "contributions": contributions},
        "proposed_traits": out.get("proposed_traits", []),
        "doubts": out.get("doubts", []),
    }
    return model


def render(model: dict) -> str:
    lines = [f"# {model['name']}", "", f"- Oferta: **{model['offer']['label']}**", f"- Producto: {model.get('product')}",
             f"- URL: {model.get('url')}", f"- Clave del modelo: `{' '.join(model['key']['model'])}`",
             f"- Aplicación de la oferta: `{' '.join(model['offer']['application']) or 'estándar'}`",
             f"- Reglas: versión {model['engine'].get('rules')} · reglamento {model['engine'].get('rulebook')}", ""]
    count = {}
    for b in model["general"]:
        for r in b["requirements"]:
            if r.get("applies", True):
                count[r["importance"]] = count.get(r["importance"], 0) + 1
    for b in model["blocks"]:
        for r in b["requirements"]:
            count[r["importance"]] = count.get(r["importance"], 0) + 1
    lines.append("Requisitos: " + ", ".join(f"{count.get(level, 0)} {level}" for level in reversed(LEVELS))
                 + f" · {len(model['inferred'])} inferidos provisionales")
    lines += ["", "## Capa general", "", "| Requisito | Pregunta | Importancia | En esta oferta |", "|---|---|---|---|"]
    for b in model["general"]:
        for r in b["requirements"]:
            cond = r.get("applicability") or "universal"
            state = (f"no aplica (gris: no se declara «{b.get('name', b['id']).lower()}»)" if not r.get("applies", True)
                     else "aplica" if cond.startswith("universal") or b["id"] != "gen" else f"aplica {cond}")
            lines.append(f"| {r['id']} | {r['question']} | {r['importance'] or 'por fijar (OQ-45)'} | {state} |")
    for b in model["blocks"]:
        head = f"## {b['id']}@{b['version']} — {b.get('name')}"
        tag = b.get("position") or "especialización"
        lines += ["", head, "", f"{tag} · {b['status']} · {b['where']}" + (f" · disparador: {b['trigger']}" if b.get("trigger") else ""),
                  "", "| Requisito | Pregunta | Rasgo | Importancia | Regla |", "|---|---|---|---|---|"]
        for r in b["requirements"]:
            mark = f" ({DOUBTFUL})" if r.get("doubtful") else " (provisional)" if r["provisional"] else ""
            lines.append(f"| {r['id']} | {r['question']} | {r['trait']} | {r['importance']}{mark} | `{r['rule']}` |")
        if b.get("excluded"):
            lines += ["", "Excluidos en esta clase (no se auditan):", ""]
            lines += [f"- {r['id']} {r['question']} — `{r['relevance_rule']}`" for r in b["excluded"]]
    if model["inferred"]:
        lines += ["", "## Cuestiones inferidas (provisionales, fuera de la clave)", "",
                  "| Requisito | Bloque | Pregunta | Rasgo | Importancia | Regla |", "|---|---|---|---|---|---|"]
        for r in model["inferred"]:
            lines.append(f"| {r['id']} | {r.get('block')} | {r['question']} | {r['trait']} | {r['importance']} | `{r['rule']}` |")
    u = model["uncompiled"]
    lines += ["", "## Usado sin compilar", "",
              f"- Bloques: {', '.join(u['blocks']) or '—'}",
              f"- Requisitos sin regla (importancia del voto): {', '.join(u['without_rule']) or '—'}",
              f"- Relevancia dudosa (votados «no relevante», sin regla que los excluya): {', '.join(u.get('doubtful_relevance', [])) or '—'}",
              f"- Cuestiones inferidas: {len(u['inferred'])}",
              f"- Categorías sin bloque: {', '.join(u['missing_blocks']) or '—'}"]
    c = model["coverage"]
    lines += ["", "## Cobertura", "", f"Hechos declarados que cuentan: {c['declared_counted']} · sin pregunta en el modelo: {len(c['gaps'])}"]
    for g in c["gaps"]:
        lines.append(f"- {g['feature']}" + (f" — «{g['evidence']}»" if g.get("evidence") else ""))
    info = [(r["id"], r["resolving_info"]) for b in model["general"] for r in b["requirements"] if r.get("resolving_info")]
    info += [(r["id"], r["resolving_info"]) for b in model["blocks"] for r in b["requirements"] if r.get("resolving_info")]
    if info:
        lines += ["", "## Información resolutiva", "", "Aportaciones de cada requisito (origen; tiendas en que se han observado):", ""]
        for rid, items in info:
            lines.append(f"- {rid}: " + " · ".join(f"{c['contribution']} [{c.get('component') or '—'}] ({c.get('origin')}; "
                                                    f"{len(c.get('stores', []))})" for c in items))
    if model.get("doubts"):
        lines += ["", "## Dudas del clasificador", ""] + [f"- {d}" for d in model["doubts"]]
    return "\n".join(lines) + "\n"


def check(path: Path) -> tuple:
    """The model assembled in memory and what the classifier output still lacks."""
    out = read_json(path)
    problems = []
    for key in ("case", "composition", "declared", "specializations", "inferred", "application", "votes"):
        if key not in out:
            problems.append(f"falta la clave «{key}»")
    model = assemble(path)
    traits = load_traits()
    proposed = {p.get("name"): p for p in out.get("proposed_traits", [])}
    vocabulary = set(traits["vocabulary"]) | set(traits.get("proposed", {})) | set(proposed)
    v3 = out.get("rulebook") not in ("v0", "v1", "v2")
    if v3:
        problems += v3_problems(out, model, vocabulary, proposed)
    for b in model["blocks"]:
        for r in b["requirements"]:
            if b["type"] == "categoría" and r["vote"] is None:
                problems.append(f"{r['id']}: sin voto")
            if r["vote"] is not None and r["vote"] not in VOTES:
                problems.append(f"{r['id']}: voto «{r['vote']}» no válido")
        for r in b.get("excluded", []):
            if r["vote"] is None:
                problems.append(f"{r['id']}: sin voto (excluido en esta clase, pero se vota igualmente)")
            if r["trait"] not in vocabulary:
                problems.append(f"{r['id']}: rasgo «{r['trait']}» fuera del vocabulario")
            if r["importance"] not in LEVELS:
                problems.append(f"{r['id']}: sin importancia (falta el voto)")
    for r in model["inferred"]:
        if r["trait"] not in vocabulary or r["importance"] not in LEVELS:
            problems.append(f"{r['id']}: inferida sin rasgo o sin voto válidos")
        if r.get("block_proposal"):
            problems += [f"{r['id']}: {e}" for e in proposal_problems(r, model)]
    if model["uncompiled"]["missing_blocks"]:
        problems.append("categorías sin bloque: " + ", ".join(model["uncompiled"]["missing_blocks"])
                        + " (genera y registra el bloque, o regístrala con --empty)")
    return model, problems


def proposal_problems(r: dict, model: dict) -> list:
    """An inferred question with a source is a proposal to its block (D-088): the source must exist in the
    references, and neither the requirements of the model nor the exclusions of the block may already have it."""
    errors = []
    asked = {s: q["id"] for b in model["blocks"] for q in b["requirements"] + b.get("excluded", []) for s in q.get("sources", [])}
    host = load_blocks().get(r.get("block")) or {}
    excluded = {e.get("source") for e in host.get("excluded", [])}
    for s in r.get("sources", []):
        if resolving.reference_info(s) is None:
            errors.append(f"fuente «{s}» sin datos en las referencias")
        elif s in asked:
            errors.append(f"la fuente «{s}» ya la pregunta {asked[s]}: usa ese requisito")
        elif s in excluded:
            errors.append(f"la fuente «{s}» está excluida en {host['id']}: no se pregunta")
    items = [{k: v for k, v in c.items() if k != "stores"} for c in r.get("resolving_info", [])]
    return errors + resolving_errors(items, ("referencias", "inferida")) + supported(items, r.get("sources", []))


def v3_problems(out: dict, model: dict, vocabulary: set, proposed: dict) -> list:
    """Rulebook v3: a trait vote for each category requirement voted (D-056) and, for each declared fact that a
    requirement answers, the contribution of its resolving information it is, or a new one (D-063)."""
    problems = []
    if "trait_votes" not in out:
        problems.append("falta la clave «trait_votes»")
    for name, p in proposed.items():
        if not name or not p.get("definition"):
            problems.append(f"rasgo propuesto «{name}» sin nombre o sin definición")
    trait_votes = out.get("trait_votes", {})
    for b in model["blocks"]:
        for r in b["requirements"] + b.get("excluded", []):
            if b["type"] == "categoría" and r["vote"] is not None and r["id"] not in trait_votes:
                problems.append(f"{r['id']}: sin voto de rasgo")
            if r.get("trait_vote") and r["trait_vote"] not in vocabulary:
                problems.append(f"{r['id']}: rasgo «{r['trait_vote']}» fuera del vocabulario (propónlo en «proposed_traits», "
                                "con su definición)")
    lists = {r["id"]: r.get("resolving_info", []) for b in model["general"] for r in b["requirements"]}
    lists.update({r["id"]: r.get("resolving_info", []) for b in model["blocks"] for r in b["requirements"]})
    lists.update({r["id"]: r.get("resolving_info", []) for r in model["inferred"]})
    for d in out.get("declared", []):
        if d.get("role") in EXCLUDED_ROLES or d.get("answers") not in lists:
            continue
        c = d.get("contribution")
        if c is None:
            problems.append(f"«{d.get('feature')}» ({d['answers']}): falta «contribution», la aportación que es")
        elif isinstance(c, str):
            if not any(resolving.same(c, item["contribution"]) for item in lists[d["answers"]]):
                problems.append(f"«{d.get('feature')}» ({d['answers']}): «{c}» no está en sus aportaciones; propón una nueva "
                                "como {\"new\": nombre, \"component\": parte de la pregunta}")
        elif not resolving.contribution(d) or not resolving.contribution(d)["component"]:
            problems.append(f"«{d.get('feature')}» ({d['answers']}): la aportación nueva necesita «new» y «component»")
    return problems


def cmd_check(path: Path) -> None:
    model, problems = check(path)
    print(f"{model['name']} — oferta {model['offer']['label']}")
    print(f"  clave: {' '.join(model['key']['model'])}")
    print(f"  hechos sin pregunta: {len(model['coverage']['gaps'])} de {model['coverage']['declared_counted']}")
    print("  correcto" if not problems else "  problemas:\n    " + "\n    ".join(problems))


def cmd_assemble(path: Path) -> None:
    model = assemble(path)
    stem = path.name.removesuffix(".json")
    model_path, md_path = path.with_name(f"{stem}.model.json"), path.with_name(f"{stem}.model.md")
    write_json(model_path, model)
    md_path.write_text(render(model), encoding="utf-8")
    u = model["uncompiled"]
    QUEUE.parent.mkdir(parents=True, exist_ok=True)
    kept = [line for line in (QUEUE.read_text(encoding="utf-8").splitlines() if QUEUE.exists() else [])
            if json.loads(line).get("model") != str(model_path)]  # re-assembling replaces the entry
    if any(u.values()):
        kept.append(json.dumps({"date": datetime.date.today().isoformat(), "case": model["case"], "url": model["url"],
                                "model": str(model_path), **u}, ensure_ascii=False))
    QUEUE.write_text("".join(line + "\n" for line in kept), encoding="utf-8")
    print(f"{model['name']} — oferta {model['offer']['label']}")
    print(f"  clave: {' '.join(model['key']['model'])}")
    print(f"  sin compilar: {len(u['blocks'])} bloques, {len(u['without_rule'])} requisitos sin regla, "
          f"{len(u['inferred'])} inferidas, {len(u['missing_blocks'])} categorías sin bloque")
    print(f"  cobertura: {len(model['coverage']['gaps'])} hechos sin pregunta de {model['coverage']['declared_counted']}")
    print(f"  → {model_path} y {md_path}")


def main() -> None:
    args = sys.argv[1:]
    if not args or args[0] not in ("blocks", "register", "check", "assemble", "show", "hints"):
        sys.exit(__doc__)
    if args[0] == "hints" and args[1:] == ["check"]:
        hints.cmd_check()
        return
    if args[0] == "hints" and len(args) > 2 and args[1] == "find":
        hints.cmd_find(args[2:])
        return
    if args[0] == "blocks" and len(args) > 1:
        cmd_blocks(args[1:])
    elif args[0] == "register" and len([a for a in args if a != "--replace"]) > 1:
        cmd_register(args[1:])
    elif args[0] == "check" and args[1:] == ["--catalog"]:
        cmd_check_catalog()
    elif args[0] == "check" and len(args) == 2:
        cmd_check(Path(args[1]))
    elif args[0] == "assemble" and len(args) == 2:
        cmd_assemble(Path(args[1]))
    elif args[0] == "show" and len(args) == 2:
        print(render(read_json(Path(args[1]))), end="")
    else:
        sys.exit(__doc__)
