"""Technical reference: source cards and technical requirements (reference/, format in its README).

reference/cards/<source>.json is the card of a registered source (sources.json): its class and
level in the canon (and, for an applicable specification, the scopes whose profile includes it),
the version it cites, which must be the pinned one, and literal quotes, each from a section of
that version. reference/requirements/<file>.json holds the technical requirements of one level of
the implementation profile of a scope (Web Schema.org or Web; FILES): each names its applicable
specification (`spec`), or the decision of the canon that adopts it as a project condition
(`decision`, D-162), cites quotes of the cards (`source#qNN`) and says its view, general or
particular, with the page types a particular one applies to (D-161).
reference/retired.json keeps the requirements taken out of the technical evaluation, with their
reason: their ids are not reused, and their quotes stay citable (T-056 reads them). The canon
(docs/10-model/evaluation-scopes.md, D-129 to D-133 and D-159) prevails: classes, levels, natures and
scopes are its own, and no other field is accepted, so no state, weight or score can be added.

A section is the anchor of a heading of text.md (`#product-properties`), or its text when the
heading has none, and `#` is the text before the first heading; in a vocabulary in JSON-LD (the Schema.org release, gs1Voc.jsonld) it is a
term (`schema:gtin`) and a quote is part of its definition. A PDF has no citable text. Quotes are
compared with whitespace collapsed.

Usage:
  reqs check                       validate the cards and the requirements
  reqs section SOURCE [SECTION]    sections of the pinned version of a source, or the text of one
                                   as the check reads it (where quotes are copied from)

The frozen sources, their registry and the pinned versions are those of references/ (D-149): web-audit
checks the sources whose `uses` includes it, and reads their sections with references.read.

REFERENCE_DIR overrides the reference directory (tests); REFS_DIR and SOURCES_FILE, as in references.
"""
import argparse
import json
import os
import re
import sys
from pathlib import Path

from references.read import PREAMBLE, citable, document_section, headings, section_text, vocabulary
from references.store import RefsError, pins, sources, sources_file

from . import ROOT

REFERENCE = Path(os.environ.get("REFERENCE_DIR") or ROOT / "reference")

# Canon values (evaluation-scopes): the classes of source (D-132), the levels of the profile of each
# scope (Web Schema.org, D-130; Web, D-159), with the file of each level and the prefix of its ids,
# and the natures, each with the terms that state it in the text of a specification («minimum
# technical requirements» states what Google Search requires, D-159). Catálogos distribuidos has
# no profile yet (OQ-30).
APPLICABLE = "especificación aplicable"
CLASSES = (APPLICABLE, "instrumento del sistema", "principios generales", "método de comprobación",
           "práctica de terceros", "antecedente histórico", "datos comerciales distribuidos")
FILES = {  # requirements/<file>.json: (scope, level, prefix of its ids)
    "serialization": ("Web Schema.org", "serialización", "ws-serialization"),
    "vocabulary": ("Web Schema.org", "vocabulario", "ws-vocabulary"),
    "consumer": ("Web Schema.org", "consumidor", "ws-consumer"),
    "web-protocol": ("Web", "protocolo", "w-protocol"),
    "web-document": ("Web", "documento", "w-document"),
    "web-consumer": ("Web", "consumidor", "w-consumer"),
}
SCOPES = tuple(dict.fromkeys(scope for scope, _, _ in FILES.values()))
LEVELS = tuple(dict.fromkeys(level for _, level, _ in FILES.values()))
PROFILES = {(scope, level) for scope, level, _ in FILES.values()}
VIEWS = ("general", "particular")
PAGE_TYPES = ("ficha de producto", "categoría o listado", "políticas y contenido", "portada")
DECISIONS = ROOT.parent / "docs" / "30-governance" / "decisions.md"
NATURES = {"obligatoria": re.compile(r"\b(must|required|requirements?|shall)\b", re.I),
           "recomendada": re.compile(r"\b(should|recommend\w*)\b", re.I)}
# Why a requirement leaves requirements/: the triage of 2026-10-28 (not audited) or the frontier of
# D-145, D-147 and D-148 (presence of what the consumer only recommends, to the demand model).
REASONS = ("no se audita", "modelo de demanda")

CARD_KEYS = ({"source", "version", "class", "summary", "quotes"}, {"level", "scopes", "note"})
QUOTE_KEYS = ({"id", "section", "text"}, {"note"})
FILE_KEYS = ({"level", "requirements"}, set())
REQUIREMENT_KEYS = ({"id", "scope", "condition", "nature", "quotes", "method", "evidence", "applicability",
                     "not_evaluable", "view"}, {"spec", "decision", "page_types", "rationale"})
RETIRED_KEYS = ({"id", "scope", "spec", "condition", "nature", "quotes", "applicability", "reason",
                 "decision"}, {"note"})
QUOTE_ID = re.compile(r"^q\d{2,}$")
QUOTE_REF = re.compile(r"^([a-z0-9]+(?:-[a-z0-9]+)*)#(q\d{2,})$")
SENTENCE_BREAK = re.compile(r"[.!?]\s+\S")


def fail(msg: str) -> None:
    print(f"reqs: {msg}", file=sys.stderr)
    sys.exit(1)


def normalized(text: str) -> str:
    return " ".join(text.split())


# --- Check --------------------------------------------------------------------

def keys(where: str, obj, spec: tuple) -> list:
    """Missing and unknown fields: nothing outside the format is accepted."""
    if not isinstance(obj, dict):
        return [f"{where}: ha de ser un objeto"]
    required, optional = spec
    return ([f"{where}: falta {k}" for k in sorted(required - obj.keys())]
            + [f"{where}: campo no admitido «{k}»" for k in sorted(obj.keys() - required - optional)])


def text_fields(where: str, obj: dict, names: tuple) -> list:
    return [f"{where}: {k} ha de ser un texto no vacío" for k in names
            if k in obj and not (isinstance(obj[k], str) and obj[k].strip())]


def load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8")), []
    except json.JSONDecodeError as e:
        return None, [f"{path.relative_to(REFERENCE)}: JSON no válido ({e})"]


def check_card(path: Path, card: dict, registry: dict, pinned: dict) -> list:
    where = str(path.relative_to(REFERENCE))
    errors = keys(where, card, CARD_KEYS)
    if not isinstance(card, dict):
        return errors
    errors += text_fields(where, card, ("summary", "note"))
    source = card.get("source")
    if source != path.stem:
        errors.append(f"{where}: source «{source}» no coincide con el nombre del fichero")
    if source not in registry:
        return errors + [f"{where}: «{source}» no es una fuente de web-audit (uses en {sources_file()})"]
    cls = card.get("class")
    if cls not in CLASSES:
        errors.append(f"{where}: class «{cls}» no es una clase del canon ({', '.join(CLASSES)})")
    if cls == APPLICABLE:
        level, scopes = card.get("level"), card.get("scopes")
        if level not in LEVELS:
            errors.append(f"{where}: una especificación aplicable lleva level ({', '.join(LEVELS)})")
        if not (isinstance(scopes, list) and scopes and all(s in SCOPES for s in scopes)):
            errors.append(f"{where}: una especificación aplicable lleva scopes, los ámbitos de cuyo perfil "
                          f"es ({', '.join(SCOPES)})")
        elif level in LEVELS:
            errors += [f"{where}: el perfil de {s} no tiene nivel {level}" for s in scopes if (s, level) not in PROFILES]
    for key in ("level", "scopes"):
        if cls != APPLICABLE and key in card:
            errors.append(f"{where}: {key} solo corresponde a una especificación aplicable")
    pin = pinned.get(source)
    if not pin:
        return errors + [f"{where}: {source} no tiene versión fijada (references/bin/refs fetch {source})"]
    if card.get("version") != pin:
        errors.append(f"{where}: cita la versión {card.get('version')} y la fijada es {pin}; revisa las "
                      f"citas (references/bin/refs diff {source} {card.get('version')} {pin}) y actualiza version")
    quotes = card.get("quotes")
    if not isinstance(quotes, list):
        return errors + [f"{where}: quotes ha de ser una lista"]
    seen = set()
    for quote in quotes:
        qid = quote.get("id") if isinstance(quote, dict) else None
        at = f"{where} {qid or '(cita sin id)'}"
        problems = keys(at, quote, QUOTE_KEYS) or text_fields(at, quote, ("section", "text", "note"))
        if problems:
            errors += problems
            continue
        if not QUOTE_ID.match(str(qid)):
            errors.append(f"{at}: el id ha de ser q01, q02…")
        elif qid in seen:
            errors.append(f"{at}: id repetido")
        seen.add(qid)
        try:
            found = section_text(source, registry[source]["kind"], quote["section"])
        except (RefsError, OSError, ValueError) as e:
            errors.append(f"{at}: {e}")
            continue
        if normalized(quote["text"]) not in normalized(found):
            errors.append(f"{at}: la cita no está en {quote['section']} de {source} {pin} "
                          f"(web-audit/bin/reqs section {source} '{quote['section']}')")
    return errors


def one_condition(where: str, condition) -> list:
    """What a check can see of «una sola condición comprobable» (D-132): one sentence."""
    if not (isinstance(condition, str) and condition.strip()):
        return [f"{where}: condition ha de ser un texto no vacío"]
    if "\n" in condition or ";" in condition or SENTENCE_BREAK.search(condition.strip()):
        return [f"{where}: condition ha de ser una sola frase, sin «;» (una condición por requisito)"]
    return []


def decisions() -> set:
    """Ids of the decisions of the canon (### D-NNN in decisions.md)."""
    try:
        return set(re.findall(r"^### (D-\d{3})$", DECISIONS.read_text(encoding="utf-8"), re.M))
    except OSError:
        return set()


def check_view(where: str, req: dict) -> list:
    """The view of a requirement and, if particular, its page types (D-161)."""
    view, types = req.get("view"), req.get("page_types")
    if view not in VIEWS:
        return [f"{where}: view «{view}» ha de ser {' o '.join(VIEWS)} (D-161)"]
    if view == "general":
        return [f"{where}: page_types solo corresponde a la vista particular"] if "page_types" in req else []
    if not (isinstance(types, list) and types and all(t in PAGE_TYPES for t in types) and len(set(types)) == len(types)):
        return [f"{where}: la vista particular lleva page_types, tipos de página sin repetir ({', '.join(PAGE_TYPES)})"]
    return []


def check_requirement(where: str, req: dict, scope: str, level: str, cards: dict, adopted: set = frozenset()) -> list:
    errors = keys(where, req, REQUIREMENT_KEYS)
    if not isinstance(req, dict):
        return errors
    errors += check_view(where, req)
    if ("spec" in req) == ("decision" in req):
        return errors + [f"{where}: lo funda una especificación (spec) o una condición del proyecto (decision), "
                         f"una de las dos (D-162)"]
    errors += text_fields(where, req, ("method", "evidence", "applicability", "rationale"))
    errors += one_condition(where, req.get("condition"))
    if req.get("scope") not in SCOPES:
        errors.append(f"{where}: scope «{req.get('scope')}» sin perfil de implementación en el canon "
                      f"({', '.join(SCOPES)}; el resto, OQ-30)")
    elif req["scope"] != scope:
        errors.append(f"{where}: scope «{req['scope']}» no es el del fichero ({scope})")
    nature = req.get("nature")
    if nature not in NATURES:
        errors.append(f"{where}: nature «{nature}» no es del canon ({', '.join(NATURES)})")
    not_evaluable = req.get("not_evaluable")
    if not (isinstance(not_evaluable, list) and all(isinstance(c, str) and c.strip() for c in not_evaluable)):
        errors.append(f"{where}: not_evaluable ha de ser una lista de textos (vacía si no tiene causas propias)")
    spec, decision = req.get("spec"), req.get("decision")
    card = cards.get(spec)
    if decision is not None:
        if decision not in adopted:
            errors.append(f"{where}: decision «{decision}» no es una decisión del canon (### D-NNN en decisions.md)")
    elif card is None:
        errors.append(f"{where}: spec «{spec}» no tiene ficha")
    elif card.get("class") != APPLICABLE:
        errors.append(f"{where}: {spec} no es una especificación aplicable (D-132)")
    elif card.get("level") != level:
        errors.append(f"{where}: {spec} es de nivel {card.get('level')}, no {level}")
    elif scope not in (card.get("scopes") or []):
        errors.append(f"{where}: {spec} no es del perfil de {scope} (scopes de su ficha)")
    quotes = req.get("quotes")
    if not isinstance(quotes, list) or not (quotes or decision is not None):
        return errors + [f"{where}: quotes ha de ser una lista con al menos una cita"]
    from_spec = []
    for ref in quotes:
        m = QUOTE_REF.match(str(ref))
        if not m:
            errors.append(f"{where}: la cita «{ref}» ha de tener la forma fuente#q01")
            continue
        cited = cards.get(m[1]) or {}
        listed = cited.get("quotes") if isinstance(cited.get("quotes"), list) else []
        quote = next((q for q in listed if isinstance(q, dict) and q.get("id") == m[2]), None)
        if quote is None:
            errors.append(f"{where}: la cita {ref} no existe")
        elif cited.get("class") != APPLICABLE:
            errors.append(f"{where}: {ref} no es de una especificación aplicable (D-132)")
        elif m[1] == spec:
            from_spec.append(str(quote.get("text", "")))
    if decision is not None:
        return errors   # the decision fixes the nature: no quote of a specification states it
    if card is not None and card.get("class") == APPLICABLE and not from_spec:
        errors.append(f"{where}: ninguna cita es de su especificación ({spec})")
    elif nature in NATURES and from_spec and not any(NATURES[nature].search(t) for t in from_spec):
        errors.append(f"{where}: ninguna cita de {spec} contiene el término que fija la naturaleza "
                      f"{nature} ({NATURES[nature].pattern}); cita el texto que la fija")
    return errors


def check_retired(seen: set, cards: dict) -> tuple:
    """(errors, ids) of retired.json, if there is one: its ids are never reused in requirements/."""
    path = REFERENCE / "retired.json"
    if not path.exists():
        return [], {}
    data, problems = load(path)
    problems = problems or keys("retired.json", data, ({"retired"}, set()))
    if problems:
        return problems, {}
    errors, retired = [], {}
    prefixes = "|".join(prefix for _, _, prefix in FILES.values())
    for entry in data["retired"] if isinstance(data["retired"], list) else []:
        rid = entry.get("id") if isinstance(entry, dict) else None
        where = f"retired.json {rid or '(retirado sin id)'}"
        errors += keys(where, entry, RETIRED_KEYS)
        if not isinstance(entry, dict):
            continue
        errors += text_fields(where, entry, ("condition", "applicability", "decision", "note"))
        if not re.fullmatch(rf"({prefixes})/\d{{3}}", str(rid)):
            errors.append(f"{where}: el id ha de ser el de un requisito (ws-consumer/001…)")
        elif rid in retired:
            errors.append(f"{where}: id repetido")
        elif rid in seen:
            errors.append(f"{where}: el id sigue en requirements/; un id retirado no se reutiliza")
        if entry.get("reason") not in REASONS:
            errors.append(f"{where}: reason «{entry.get('reason')}» ha de ser {' o '.join(REASONS)}")
        elif entry["reason"] == "modelo de demanda" and entry.get("nature") != "recomendada":
            errors.append(f"{where}: solo lo recomendado pasa al modelo de demanda (D-145)")
        if entry.get("nature") not in NATURES:
            errors.append(f"{where}: nature «{entry.get('nature')}» no es del canon ({', '.join(NATURES)})")
        if entry.get("spec") not in cards:
            errors.append(f"{where}: spec «{entry.get('spec')}» no tiene ficha")
        for ref in entry.get("quotes") if isinstance(entry.get("quotes"), list) else []:
            m = QUOTE_REF.match(str(ref))
            listed = (cards.get(m[1]) or {}).get("quotes") if m else None
            if not (isinstance(listed, list) and any(isinstance(q, dict) and q.get("id") == m[2] for q in listed)):
                errors.append(f"{where}: la cita {ref} no existe")
        retired[rid] = entry.get("reason")
    if not isinstance(data["retired"], list):
        errors.append("retired.json: retired ha de ser una lista")
    return errors, retired


def check() -> tuple:
    """(errors, summary) of the whole reference."""
    registry = {sid: s for sid, s in sources().items() if "web-audit" in s["uses"]}
    pinned = pins("web-audit")
    errors, cards = [], {}
    for path in sorted((REFERENCE / "cards").glob("*.json")):
        card, problems = load(path)
        errors += problems or check_card(path, card, registry, pinned)
        if isinstance(card, dict):
            cards[path.stem] = card
    seen, natures, by_scope = set(), dict.fromkeys(NATURES, 0), dict.fromkeys(SCOPES, 0)
    by_view, adopted = dict.fromkeys(VIEWS, 0), decisions()
    for path in sorted((REFERENCE / "requirements").glob("*.json")):
        where = str(path.relative_to(REFERENCE))
        data, problems = load(path)
        problems = problems or keys(where, data, FILE_KEYS)
        if problems:
            errors += problems
            continue
        if path.stem not in FILES:
            errors.append(f"{where}: el fichero ha de ser el de un nivel ({', '.join(FILES)})")
            continue
        scope, level, prefix = FILES[path.stem]
        if data["level"] != level:
            errors.append(f"{where}: level «{data['level']}» no coincide con el fichero ({level})")
        if not isinstance(data["requirements"], list):
            errors.append(f"{where}: requirements ha de ser una lista")
            continue
        for req in data["requirements"]:
            rid = req.get("id") if isinstance(req, dict) else None
            at = f"{where} {rid or '(requisito sin id)'}"
            if not re.fullmatch(rf"{prefix}/\d{{3}}", str(rid)):
                errors.append(f"{at}: el id ha de ser {prefix}/001, {prefix}/002…")
            elif rid in seen:
                errors.append(f"{at}: id repetido")
            seen.add(rid)
            errors += check_requirement(at, req, scope, level, cards, adopted)
            by_scope[scope] += 1
            if isinstance(req, dict) and req.get("view") in by_view:
                by_view[req["view"]] += 1
            if isinstance(req, dict) and req.get("nature") in natures:
                natures[req["nature"]] += 1
    problems, retired = check_retired(seen, cards)
    errors += problems
    quotes = sum(len(c.get("quotes") or []) for c in cards.values())
    applicable = sum(c.get("class") == APPLICABLE for c in cards.values())
    summary = [f"{len(cards)} fichas ({applicable} de especificaciones aplicables), {quotes} citas, "
               f"{len(seen)} requisitos (" + ", ".join(f"{n} {k}s" for k, n in natures.items()) + ")",
               "por ámbito: " + ", ".join(f"{scope} {n}" for scope, n in by_scope.items())
               + " · por vista: " + ", ".join(f"{view} {n}" for view, n in by_view.items())]
    if retired:
        summary.append(f"retirados ({len(retired)}): " + ", ".join(
            f"{n} {r}" for r in REASONS if (n := list(retired.values()).count(r))))
    missing = [s for s in registry if s not in cards]
    if missing:
        summary.append(f"sin ficha ({len(missing)}): {', '.join(missing)}")
    return errors, summary


# --- Commands -----------------------------------------------------------------

def cmd_check(args) -> None:
    errors, summary = check()
    for line in errors:
        print(line)
    print(f"incorrecto: {len(errors)} problema(s)" if errors else "correcto", summary[0], sep=" · ")
    for line in summary[1:]:
        print(line)
    if errors:
        sys.exit(1)


def cmd_section(args) -> None:
    try:
        registry = sources()
    except RefsError as e:
        fail(str(e))
    if args.source not in registry:
        fail(f"fuente desconocida: {args.source} (ver {sources_file()})")
    kind = registry[args.source]["kind"]
    try:
        if args.section:
            print(section_text(args.source, kind, args.section))
            return
        path = citable(args.source, kind)
        if path.name != "text.md":
            print(f"{path.name}: {len(vocabulary(path))} términos; indica uno (p. ej. schema:gtin)")
            return
        text = path.read_text(encoding="utf-8")
        if document_section(text, PREAMBLE).strip():
            print(f"{PREAMBLE}  (texto antes del primer encabezado)")
        for _, level, title, anchor in headings(text):
            print("  " * (level - 1) + (f"#{anchor}  " if anchor else "") + title)
    except (RefsError, OSError, ValueError) as e:
        fail(str(e))


def main() -> None:
    parser = argparse.ArgumentParser(prog="reqs", description="Referencia técnica: fichas de fuente y requisitos técnicos.")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("check", help="validar fichas y requisitos").set_defaults(func=cmd_check)
    p = sub.add_parser("section", help="secciones de la versión fijada de una fuente, o el texto de una")
    p.add_argument("source")
    p.add_argument("section", nargs="?")
    p.set_defaults(func=cmd_section)
    args = parser.parse_args()
    (getattr(args, "func", None) or cmd_check)(args)


if __name__ == "__main__":
    main()
