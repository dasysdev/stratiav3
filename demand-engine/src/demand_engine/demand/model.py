"""Execution of the demand model (D-041, D-044, D-045): blocks for a class, runtime blocks and assembly.

Usage:
  model blocks CATEGORY_ID [...]      catalog blocks of the classes and their ancestors, with their
                                      requirements (id, trait, question), the general layer and the
                                      categories that have no block yet
  model register BLOCK.json           register a block generated at runtime (status «no compilado»)
  model register --empty CATEGORY_ID  register a category without requirements of its own
  model check OUTPUT.json             assemble in memory and report what is missing (for the classifier)
  model assemble OUTPUT.json          build the demand model from a classifier output (rulebook v2):
                                      writes <case>.model.json and <case>.model.md next to it and
                                      appends what was used without compiling to the queue
  model show MODEL.json               print the readable version of an assembled model

The classifier decides the composition, specializations, inferred questions, application
and votes; everything else is deterministic: blocks come from the catalog, importance
from the compiled rules (the vote only where no rule applies) and the key and name from
the blocks.
"""
import datetime
import json
import sys
from pathlib import Path

from ..refs import pins
from .catalog import (CAT_DIR, COMPILED, DOUBTFUL, ESP_ORDER, EMPTY, LEVELS, NO_RULE, NOT_RELEVANT, QUEUE,
                      RUNTIME_DIR, UNCOMPILED, VOTES, blocks_by_node, category_name, chain, class_nodes_for, depth,
                      load_blocks, load_empty, load_gen, load_rules, load_traits, protected, read_json, relevance,
                      requirement_trait, resolve, write_json)

EXCLUDED_ROLES = ("estético", "promocional", "beneficio reclamado")  # declared facts that need no question (D-045)


def cmd_blocks(ids: list) -> None:
    blocks, empty = load_blocks(), load_empty()
    by_node = blocks_by_node(blocks)
    src_traits = load_traits()["sources"]
    gen, rules = load_gen(), load_rules()
    print("CAPA GENERAL (fija; no se vota)")
    for b in gen["blocks"]:
        trigger = f" · si {b['trigger']}" if b.get("trigger") else ""
        print(f"  [{b['id']}{trigger}]")
        for r in b["requirements"]:
            print(f"    {r['id']}: {r['question']}")
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
            trait, _ = requirement_trait(r, src_traits)
            excluded, _ = relevance(r["id"], class_nodes_for(node, ids), rules)
            print(f"  {r['id']} [{trait or '?'}] {r['question']}" + ("  [excluido en esta clase: vótalo igualmente]" if excluded else ""))
    if missing:
        print(f"\nCategorías sin bloque: {' '.join(missing)}")


def cmd_register(args: list) -> None:
    traits = load_traits()
    vocabulary, src_traits = traits["vocabulary"], traits["sources"]
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
    bid = block.get("id", "")
    if not bid.startswith("cat.") or not block.get("shopify"):
        errors.append("el bloque necesita id «cat.<nombre>» y «shopify»")
    if bid in blocks and blocks[bid]["_where"] == "catálogo":
        errors.append(f"{bid} ya existe en el catálogo")
    if block.get("shopify") in by_node and by_node[block["shopify"]]["id"] != bid:
        errors.append(f"la categoría {block.get('shopify')} ya tiene el bloque {by_node[block['shopify']]['id']}")
    overridden = []
    for i, r in enumerate(block.get("requirements", []), 1):
        r.setdefault("id", f"{bid}/{i:02d}")
        if not r["id"].startswith(bid + "/"):
            errors.append(f"{r['id']}: el identificador no es del bloque")
        if not r.get("question"):
            errors.append(f"{r['id']}: falta la pregunta")
        if r.get("trait") not in vocabulary:
            errors.append(f"{r['id']}: rasgo «{r.get('trait')}» fuera del vocabulario")
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


def requirement_entry(r: dict, trait: str, classes: list, rules: dict, vote) -> dict:
    """Relevance first (D-050), then importance (D-045). Doubt does not exclude: a «no relevante» vote
    without a compiled rule keeps the requirement as complementary and marks it."""
    sources = r.get("sources", [])
    excluded, rel_rule = relevance(r["id"], classes, rules)
    if excluded and protected(trait, r.get("origin"), sources):
        excluded, rel_rule = False, "marco:no-excluible"
    level, rule = resolve(trait, classes, rules, sources)
    provisional = level is None
    if provisional:
        fallback = vote if vote in LEVELS else r.get("vote") if r.get("vote") in LEVELS else r.get("importance")
        level, rule = ("complementario" if vote == NOT_RELEVANT else fallback), NO_RULE
    doubtful = vote == NOT_RELEVANT and not excluded and not protected(trait, r.get("origin"), sources)
    return {"id": r["id"], "question": r.get("question"), "dimension": r.get("dimension"), "entity": r.get("entity"),
            "trait": trait, "importance": level, "rule": rule, "vote": vote, "provisional": provisional or doubtful,
            "doubtful": doubtful, "excluded": excluded, "relevance_rule": rel_rule,
            "classes": classes, "origin": r.get("origin"), "sources": sources,
            "applicability": r.get("applicability")}


def split(entries: list) -> tuple:
    return [e for e in entries if not e["excluded"]], [e for e in entries if e["excluded"]]


def assemble(out_path: Path) -> dict:
    out = read_json(out_path)
    blocks, empty = load_blocks(), load_empty()
    by_node = blocks_by_node(blocks)
    src_traits = load_traits()["sources"]
    rules, gen = load_rules(), load_gen()
    cats = out.get("composition", {}).get("categories", [])
    classes = [c["shopify"] for c in cats if not c.get("alias")]
    aliases = [c["shopify"] for c in cats if c.get("alias")]
    votes = out.get("votes", {})
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
            trait, _ = requirement_trait(r, src_traits)
            reqs.append(requirement_entry(r, trait, scope, rules, votes.get(r["id"])))
        kept, excluded = split(reqs)
        model_blocks.append({"id": b["id"], "type": "categoría", "position": "categoría" if node in classes else "sector",
                             "name": b.get("name"), "shopify": node, "version": b.get("version"), "status": b.get("status"),
                             "where": b["_where"], "requirements": kept, "excluded": excluded})
    for e in out.get("specializations", []):
        reqs = []
        for i, r in enumerate(e.get("requirements", []), 1):
            r.setdefault("id", f"{e['id']}/{i:02d}")
            reqs.append(requirement_entry(r, r.get("trait"), classes, rules, r.get("vote")))
        model_blocks.append({"id": e["id"], "type": "especialización", "name": e.get("name"), "order": e.get("order"),
                             "trigger": e.get("trigger"), "support": e.get("support", []), "version": "0",
                             "status": UNCOMPILED, "where": "ejecución", "requirements": reqs})
    inferred = []
    for i, r in enumerate(out.get("inferred", []), 1):
        r.setdefault("id", f"inf/{i:02d}")
        host = next((b for b in model_blocks if b["id"] == r.get("block")), None)
        scope = class_nodes_for(host.get("shopify") if host else None, classes)
        entry = requirement_entry(r, r.get("trait"), scope, rules, r.get("vote"))
        entry.update({"block": r.get("block"), "origin": "inferida", "rationale": r.get("rationale")})
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
                                          "applicability": r.get("applicability", "universal"), "origin": r.get("origin")}
                                         for r in b["requirements"]]})
    esp = sorted((b for b in model_blocks if b["type"] == "especialización"),
                 key=lambda b: (ESP_ORDER.index(b["order"]) if b.get("order") in ESP_ORDER else len(ESP_ORDER), b["id"]))
    versions = {b["id"]: b.get("version") for b in gen["blocks"]}
    key = {"model": [f"gen@{gen['version']}"] + [f"{b['id']}@{b['version']}" for b in model_blocks if b["type"] == "categoría"]
                    + [f"{b['id']}@{b['version']}" for b in esp] + [f"{g}@{versions[g]}" for g in product_gen]}
    offer = {"application": application, "label": ", ".join(short[a] for a in application) or "estándar"}
    name = " + ".join(category_name(c) for c in classes)
    if aliases:
        name += f" ({', '.join(category_name(a) for a in aliases)})"
    if esp or product_gen:
        name += " · " + ", ".join([b.get("name") or b["id"] for b in esp] + [short[g] for g in product_gen])
    ids = {r["id"] for b in model_blocks for r in b["requirements"]} | {r["id"] for r in inferred} \
        | {r["id"] for b in general for r in b["requirements"]}
    counted = [d for d in out.get("declared", []) if d.get("role") not in EXCLUDED_ROLES]
    gaps = [d for d in counted if d.get("answers") not in ids]
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
                     "gaps": [{"feature": d.get("feature"), "evidence": d.get("evidence")} for d in gaps]},
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
    if model.get("doubts"):
        lines += ["", "## Dudas del clasificador", ""] + [f"- {d}" for d in model["doubts"]]
    return "\n".join(lines) + "\n"


def cmd_check(path: Path) -> None:
    out = read_json(path)
    problems = []
    for key in ("case", "composition", "declared", "specializations", "inferred", "application", "votes"):
        if key not in out:
            problems.append(f"falta la clave «{key}»")
    model = assemble(path)
    vocabulary = load_traits()["vocabulary"]
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
    if model["uncompiled"]["missing_blocks"]:
        problems.append("categorías sin bloque: " + ", ".join(model["uncompiled"]["missing_blocks"])
                        + " (genera y registra el bloque, o regístrala con --empty)")
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
    if not args or args[0] not in ("blocks", "register", "check", "assemble", "show"):
        sys.exit(__doc__)
    if args[0] == "blocks" and len(args) > 1:
        cmd_blocks(args[1:])
    elif args[0] == "register" and len(args) > 1:
        cmd_register(args[1:])
    elif args[0] == "check" and len(args) == 2:
        cmd_check(Path(args[1]))
    elif args[0] == "assemble" and len(args) == 2:
        cmd_assemble(Path(args[1]))
    elif args[0] == "show" and len(args) == 2:
        print(render(read_json(Path(args[1]))), end="")
    else:
        sys.exit(__doc__)
