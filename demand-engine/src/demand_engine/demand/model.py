"""Execution of the demand model (D-041, D-044, D-045): blocks for a class, runtime blocks and assembly.

Usage:
  model blocks CATEGORY_ID [...]      catalog blocks of the classes and their ancestors, with their
                                      requirements (id, trait, question), the general layer, the
                                      specializations of their verticals and the categories that have
                                      no block yet
  model register BLOCK.json [--replace]
                                      register a block generated at runtime (status «no compilado»):
                                      a category block (cat.…) or a specialization (esp.…, anchored in
                                      the class of its «shopify»); a category that already has a runtime
                                      block, or a specialization that already exists, is refused (another
                                      case of the batch generated it), unless --replace
  model register --empty CATEGORY_ID  register a category without requirements of its own
  model check OUTPUT.json             assemble in memory and report what is missing (for the classifier)
  model check --catalog               check every block of the catalog and the general layer: ids, traits,
                                      origins and sources, and the resolving information of each requirement
  model assemble OUTPUT.json          build the demand model from a classifier output (rulebook v2 to v5):
                                      writes <case>.model.json and <case>.model.md next to it, with the
                                      frozen page of the case and its capture profile, and appends what
                                      was used without compiling to the queue
  model show MODEL.json               print the readable version of an assembled model
  model hints check                   check the catalog of assessment hints (fields, id, origin, destination,
                                      same destination and property) and the comparison marks (D-136, D-139)
  model hints find REQ_ID [...]       hints of each requirement by its tags (type, source, id), code only (D-134)
  model refs                          citations of the catalog whose version is not the pinned one in references
                                      (refs, sources, support, hints by source), with the citations to sources
                                      without a registry and without a version apart;
                                      a citation of a law (ley:) must name an article and apartado of its version
  model scope MODEL.json [SCOPE ...]  compose an assembled model with the sheet of each scope (D-155; all by
                                      default: content, markup; D-220): RI × scope units, NA by the rules of the
                                      sheet and localization; writes <case>.<scope>.json and .md next to it

The classifier decides the composition, specializations (from rulebook v4, a block of the catalog by
its id, or a new one it registers: D-190), inferred questions, application
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

from capture import pages
from references.store import pins

from . import citations, hints, resolving, scopes
from references.read import shopify_categories

from .catalog import (CAT_DIR, COMPILED, ROOT, DOUBTFUL, ESP_ORDER, ESP_RUNTIME_DIR, EMPTY, LEVELS, NO_RULE,
                      NOT_RELEVANT, PAA_QUESTIONS, QUEUE, RUNTIME_DIR, UNCOMPILED, VOTES, applies_to, blocks_by_node, category_name,
                      chain, class_nodes_for, depth, load_blocks, load_empty, load_gen, load_resolving, load_rules,
                      load_specializations, load_traits, protected, read_json, relevance, requirement_trait, resolve,
                      specialization_aliases, trait_index, vertical, write_json)

LEGACY_RULEBOOKS = ("v0", "v1", "v2", "v3")  # their specializations were drafted inline, in each run

EXCLUDED_ROLES = ("estético", "promocional", "beneficio reclamado")  # declared facts that need no question (D-045)



def cmd_blocks(ids: list) -> None:
    blocks, empty = load_blocks(), load_empty()
    by_node = blocks_by_node(blocks)
    src_traits, voted = trait_index()
    gen, rules, compiled = load_gen(), load_rules(), load_resolving()
    traits = load_traits()
    print("RASGOS: " + ", ".join(traits["vocabulary"]) + (f" · propuestos: {', '.join(traits.get('proposed', {}))}"
                                                           if traits.get("proposed") else ""))
    for name, t in {**traits["vocabulary"], **traits.get("proposed", {})}.items():
        print(f"  {name}: {t.get('definition')}")
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
                state = "FALTA EL BLOQUE: genéralo (paso 3 del reglamento)"
            print(f"\n{node} {category_name(node)} ({role}) — {state}")
            continue
        print(f"\n{node} {category_name(node)} ({role}) — {b['id']}@{b.get('version')} · {b.get('status')} · {b['_where']}")
        for r in b["requirements"]:
            trait, _ = requirement_trait(r, src_traits, voted)
            excluded, _ = relevance(r["id"], class_nodes_for(node, ids), rules)
            print(f"  {r['id']} [{trait or '?'}] {r['question']}" + ("  [excluido en esta clase: vótalo igualmente]" if excluded else ""))
            print_resolving(r, compiled, "    ")
    print_specializations(ids, src_traits, voted, rules, compiled)
    if missing:
        print(f"\nCategorías sin bloque: {' '.join(missing)}")


def print_specializations(ids: list, src_traits: dict, voted: dict, rules: dict, compiled: dict) -> None:
    """The specializations of the verticals of the classes, those that apply to them first (D-190); a set of pieces
    (order «juego») crosses the categories, so it is always shown (D-086)."""
    verticals = {vertical(c) for c in ids}
    shown = [s for s in load_specializations().values()
             if s.get("order") == "juego" or any(vertical(a) in verticals for a in s.get("anchors", []))]
    print("\nESPECIALIZACIONES (paso 4: si lo declarado dispara una, úsala por su id; si ninguna encaja, registra una nueva)")
    if not shown:
        print("  ninguna en esta vertical")
    for s in sorted(shown, key=lambda s: (not applies_to(s, ids), s["id"])):
        where = "de esta clase" if applies_to(s, ids) else "de otra rama: úsala si sus cuestiones valen aquí"
        print(f"\n  {s['id']}@{s.get('version')} {s.get('name')} ({s.get('order')}) — {s.get('status')} · {s['_where']} · "
              f"ancla {', '.join(s.get('anchors', []))} · {where}")
        print(f"    disparador: {s.get('trigger')}")
        if s.get("aliases"):
            print(f"    sinónimos fusionados: {', '.join(s['aliases'])}")
        for r in s["requirements"]:
            trait, _ = requirement_trait(r, src_traits, voted)
            excluded, _ = relevance(r["id"], ids, rules)
            cond = r.get("applicability") or "universal"
            print(f"    {r['id']} [{trait or '?'}] {r['question']}" + ("" if cond == "universal" else f" · {cond}")
                  + ("  [excluido en esta clase: vótalo igualmente]" if excluded else ""))
            print_resolving(r, compiled, "      ")


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
    if bid.startswith("esp."):
        register_specialization(block, replace, errors, vocabulary, src_traits)
        return
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
    overridden = draft_requirement_errors(block, errors, vocabulary, src_traits)
    if errors:
        sys.exit("model: bloque no registrado:\n  " + "\n  ".join(errors))
    block.update({"type": "categoría", "status": UNCOMPILED, "version": "0",
                  "generated": datetime.date.today().isoformat()})
    path = RUNTIME_DIR / f"{bid.removeprefix('cat.')}.json"
    write_json(path, block)
    print(f"{bid}: registrado en {path.relative_to(CAT_DIR.parent.parent)} ({len(block['requirements'])} requisitos, no compilado)")
    for line in overridden:
        print(f"  {line}")


def draft_requirement_errors(block: dict, errors: list, vocabulary: set, src_traits: dict) -> list:
    """Check the requirements of a drafted block (category or specialization) and append to `errors`; the trait of
    their sources prevails over the drafted one. Returns the traits overridden."""
    bid, overridden = block.get("id", ""), []
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
        errors += [f"{r['id']}: {e}" for e in hints.draft_errors(r)]
        if r.get("vote") not in VOTES:
            errors.append(f"{r['id']}: voto «{r.get('vote')}» no válido")
        trait, origin = requirement_trait(r, src_traits)
        if origin == "fuente" and trait != r.get("trait"):
            overridden.append(f"{r['id']}: {r.get('trait')} → {trait} (rasgo de sus fuentes)")
            r["trait"] = trait
    return overridden


def register_specialization(block: dict, replace: bool, errors: list, vocabulary: set, src_traits: dict) -> None:
    """Register a specialization drafted at runtime (D-190): «no compilado», anchored in the class where it is
    observed (`shopify`); the training merges its synonyms, moves its anchor along the tree and compiles it."""
    sid = block["id"]
    specs = load_specializations()
    alias = specialization_aliases(specs).get(sid)
    if not sid.removeprefix("esp.") or sid != sid.lower() or " " in sid:
        errors.append("el id es «esp.<nombre>», en español, con minúsculas y guiones")
    if alias:
        errors.append(f"{sid} es un sinónimo de {alias}: úsala por su id (bin/model blocks)")
    current = specs.get(sid)
    if current and (current["_where"] == "catálogo" or not replace):
        errors.append(f"{sid} ya existe ({current['_where']}; quizá la registró otro caso del lote): no la redactes de "
                      "nuevo; úsala por su id y vota sus requisitos. --replace solo para corregir una que registraste tú")
    if not block.get("name") or not block.get("trigger"):
        errors.append("faltan «name» o «trigger»")
    if block.get("order") not in ESP_ORDER:
        errors.append(f"orden «{block.get('order')}» no válido ({', '.join(ESP_ORDER)})")
    if not block.get("support"):
        errors.append("sin apoyo en las referencias («support», D-024)")
    if block.get("shopify") not in shopify_categories():
        errors.append("«shopify»: la categoría de la composición en la que se observa")
    if not block.get("requirements"):
        errors.append("sin requisitos")
    for r in block.get("requirements", []):
        r.setdefault("origin", "referencias" if r.get("sources") else "inferida")
    overridden = draft_requirement_errors(block, errors, vocabulary, src_traits)
    if errors:
        sys.exit("model: especialización no registrada:\n  " + "\n  ".join(errors))
    anchor = block.pop("shopify")
    block.update({"type": "especialización", "anchors": [anchor], "status": UNCOMPILED, "version": "0",
                  "generated": datetime.date.today().isoformat()})
    path = ESP_RUNTIME_DIR / f"{sid.removeprefix('esp.')}.json"
    write_json(path, block)
    print(f"{sid}: registrada en {path.relative_to(CAT_DIR.parent.parent)} ({len(block['requirements'])} requisitos, "
          f"no compilada)")
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
        elif c.get("origin") == "paa":
            # D-178: a contribution of PAA, to a requirement of any origin, is supported by its questions
            if not all(s.startswith("paa-q:") for s in c["support"]):
                errors.append(f"aportación «{c.get('contribution')}»: origen «paa» con respaldo que no son preguntas PAA")
            continue
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
        errors += resolving_errors(items, ("referencias", "inferida", "paa")) + supported(items, r.get("sources", []))
        problems += [f"{rid}: {e}" for e in errors]
    return problems


def paa_question_problems(blocks: list, texts: dict) -> list:
    """D-178: every PAA question that the catalog cites has its literal text in catalog/paa-questions.json."""
    problems = []
    for b in blocks:
        for r in b["requirements"]:
            tags = set(r.get("sources", [])) | {s for c in r.get("resolving_info") or [] for s in c.get("support") or []}
            problems += [f"{r['id']}: la pregunta «{t}» no tiene su texto en paa-questions.json"
                         for t in sorted(tags) if t.startswith("paa-q:") and not (texts.get(t) or {}).get("q")]
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
    specs = load_specializations()
    for b in list(blocks.values()) + list(specs.values()):
        problems += block_problems(b, vocabulary | {p.get("name") for p in b.get("proposed_traits", [])})
        for r in b["requirements"]:
            if r.get("id") in seen:
                problems.append(f"{r['id']}: repetido en {seen[r['id']]} y {b['id']}")
            seen[r.get("id")] = b["id"]
    paa_texts = PAA_QUESTIONS.exists() and read_json(PAA_QUESTIONS) or {}
    problems += paa_question_problems(list(blocks.values()) + list(specs.values()), paa_texts)
    gen = load_gen()
    problems += gen_problems(gen) + scopes.catalog_problems(gen)
    contributions = sum(len(r.get("resolving_info", [])) for b in list(blocks.values()) + list(specs.values())
                        for r in b["requirements"])
    print(f"catálogo: {len(blocks)} bloques y {len(specs)} especializaciones, {len(seen)} requisitos, {contributions} aportaciones; capa general, "
          f"propiedades de Google Search y fichas de ámbito ({', '.join(scopes.scope_names())}) incluidas")
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
            **({"description": r["description"]} if r.get("description") else {}),
            "resolving_info": resolving.for_model(r, compiled or {}), "hints": r.get("hints", [])}


def split(entries: list) -> tuple:
    return [e for e in entries if not e["excluded"]], [e for e in entries if e["excluded"]]


def frozen_page(case_id) -> dict | None:
    """The frozen page the case was classified on, with its capture profile. The case takes the ID of its
    page (taxo page fetch ID, /demand-model --page ID, the training). A page frozen before the profiles is
    a «reader» one; None if the store has no page of that ID."""
    path = pages.PAGES / f"{case_id}.json"   # the store of frozen pages (D-150)
    if not case_id or not path.exists():
        return None
    return {"id": case_id, "profile": read_json(path).get("profile") or "reader"}


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
    # D-190: a specialization is a block of the catalog, used by its id (a merged synonym leads to its block);
    # up to rulebook v3, the classifier drafted it inline in each run.
    specs = load_specializations()
    synonyms, missing_specs = specialization_aliases(specs), []
    for e in out.get("specializations", []):
        if out.get("rulebook") in LEGACY_RULEBOOKS:
            reqs = []
            for i, r in enumerate(e.get("requirements", []), 1):
                r.setdefault("id", f"{e['id']}/{i:02d}")
                reqs.append(requirement_entry(r, r.get("trait"), classes, rules, r.get("vote"), r.get("trait"), compiled))
            model_blocks.append({"id": e["id"], "type": "especialización", "name": e.get("name"), "order": e.get("order"),
                                 "trigger": e.get("trigger"), "support": e.get("support", []), "version": "0",
                                 "status": UNCOMPILED, "where": "ejecución", "inline": True, "requirements": reqs})
            continue
        spec = specs.get(synonyms.get(e.get("id"), e.get("id")))
        if spec is None:
            missing_specs.append(e.get("id"))
            continue
        reqs = []
        for r in spec["requirements"]:
            trait, _ = requirement_trait(r, src_traits, voted)
            reqs.append(requirement_entry(r, trait, classes, rules, votes.get(r["id"]), trait_votes.get(r["id"]), compiled))
        kept, excluded = split(reqs)
        model_blocks.append({"id": spec["id"], "type": "especialización", "name": spec.get("name"), "order": spec.get("order"),
                             "trigger": e.get("trigger") or spec.get("trigger"), "support": spec.get("support", []),
                             "anchors": spec.get("anchors", []), "version": spec.get("version"), "status": spec.get("status"),
                             "where": spec["_where"], "requirements": kept, "excluded": excluded})
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
                        "requirements": [{"id": r["id"], "question": r["question"],
                                          **({"description": r["description"]} if r.get("description") else {}),
                                          "entity": r.get("entity"),
                                          "importance": r.get("importance"), "rule": "marco:capa-general", "applies": applies,
                                          "applicability": r.get("applicability", "universal"), "origin": r.get("origin"),
                                          "sources": r.get("sources", []),
                                          "references": scopes.google_sources(r.get("sources", [])),
                                          "resolving_info": resolving.for_model(r, compiled),
                                          "hints": r.get("hints", [])}
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
    # D-192: a trait proposed by whoever drafts a block is used before it wins a vote: provisional and queued
    vocabulary = set(load_traits()["vocabulary"])
    provisional_traits = [r["id"] for b in model_blocks for r in b["requirements"] if r.get("trait") and r["trait"] not in vocabulary] \
        + [r["id"] for r in inferred if r.get("trait") and r["trait"] not in vocabulary]
    # D-155: the recommended properties of Google Search support category requirements through the Shopify
    # attributes they cite (catalog/google-search.json); those of the general layer are in its sources.
    google = scopes.load_google()
    for r in [r for b in model_blocks for r in b["requirements"] + b.get("excluded", [])] + inferred:
        r["references"] = scopes.attribute_support(r.get("sources", []), google)
    # D-135: the model keeps the resolved hints of each requirement (those of the catalog that reach it and its own);
    # the RI profile takes them in «pistas_valoracion»
    catalog_hints = hints.load_hints().get("hints", [])
    for r in [r for b in general + model_blocks for r in b["requirements"] + b.get("excluded", [])] + inferred:
        r["hints"] = [h for _, h in hints.find(r, catalog_hints)]
    model = {
        "case": out.get("case"), "product": out.get("product"), "url": out.get("url"),
        "page": frozen_page(out.get("case")),
        "engine": {"rulebook": out.get("rulebook"), "rules": rules.get("version"), "refs": pins("demand-engine"),
                   "google_search": google.get("version"), "assembled": datetime.date.today().isoformat()},
        "key": key, "name": name, "offer": offer,
        "composition": {"classes": classes, "aliases": aliases},
        "general": general, "blocks": model_blocks, "inferred": inferred,
        "uncompiled": {"blocks": [b["id"] for b in model_blocks if b["status"] != COMPILED],
                       "inferred": [r["id"] for r in inferred], "without_rule": provisional, "doubtful_relevance": doubtful,
                       "missing_blocks": missing, "missing_specializations": missing_specs,
                       "provisional_traits": provisional_traits},
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
    page = model.get("page")
    lines = [f"# {model['name']}", "", f"- Oferta: **{model['offer']['label']}**", f"- Producto: {model.get('product')}",
             f"- URL: {model.get('url')}",
             *([f"- Ficha: `{page['id']}` · perfil de captura `{page['profile']}`"] if page else []),
             f"- Clave del modelo: `{' '.join(model['key']['model'])}`",
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
              f"- Rasgos propuestos aún sin votos (provisionales, D-192): {', '.join(u.get('provisional_traits', [])) or '—'}",
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
    support = [(r["id"], r["references"]) for b in model["general"] for r in b["requirements"] if r.get("references")]
    support += [(r["id"], r["references"]) for b in model["blocks"] for r in b["requirements"] if r.get("references")]
    if support:
        lines += ["", "## Apoyo de Google Search", "",
                  "Propiedades que los consumidores del perfil de Marcado recomiendan sin exigir: apoyo de demanda con "
                  "origen «referencias», sin ámbito (D-145, D-155). La importancia no sale de aquí.", ""]
        lines += [f"- {rid}: " + ", ".join(f"`{c.removeprefix('google-search-')}`" for c in cites) for rid, cites in support]
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
            if not b.get("inline") and r["vote"] is None:
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
    if model["uncompiled"]["missing_specializations"]:
        problems.append("especializaciones sin bloque: " + ", ".join(model["uncompiled"]["missing_specializations"])
                        + " (usa una de «bin/model blocks» por su id, o redacta y registra la nueva)")
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
            if not b.get("inline") and r["vote"] is not None and r["id"] not in trait_votes:
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
    if not args or args[0] not in ("blocks", "register", "check", "assemble", "show", "hints", "refs", "scope"):
        sys.exit(__doc__)
    if args == ["refs"]:
        citations.cmd_check()
        return
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
    elif args[0] == "scope" and len(args) > 1:
        scopes.cmd_scope(Path(args[1]), args[2:])
    elif args[0] == "show" and len(args) == 2:
        print(render(read_json(Path(args[1]))), end="")
    else:
        sys.exit(__doc__)
