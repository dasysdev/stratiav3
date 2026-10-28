"""Technical reference: source cards and technical requirements (reference/, format in its README).

reference/cards/<source>.json is the card of a registered source (sources.json): its class and
level in the canon, the version it cites, which must be the pinned one, and literal quotes, each
from a section of that version. reference/requirements/<level>.json holds the technical
requirements of one level of the Web Schema.org implementation profile: each names its
applicable specification (`spec`) and cites quotes of the cards (`source#qNN`). The canon
(docs/10-model/evaluation-scopes.md, D-129 to D-133) prevails: classes, levels, natures and
scopes are its own, and no other field is accepted, so no state, weight or score can be added.

A section is the anchor of a heading of text.md (`#product-properties`), or its text when the
heading has none; in a vocabulary in JSON-LD (the Schema.org release, gs1Voc.jsonld) it is a
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

from references.read import citable, headings, section_text, vocabulary
from references.store import RefsError, pins, sources, sources_file

from . import ROOT

REFERENCE = Path(os.environ.get("REFERENCE_DIR") or ROOT / "reference")

# Canon values (evaluation-scopes): the classes of source (D-132), the levels of the Web Schema.org
# profile with the file of each (D-130) and the natures, each with the terms that state it in the
# text of a specification. Web and Catálogos distribuidos have no profile yet (OQ-30).
APPLICABLE = "especificación aplicable"
CLASSES = (APPLICABLE, "instrumento del sistema", "principios generales", "método de comprobación",
           "práctica de terceros", "antecedente histórico", "datos comerciales distribuidos")
LEVELS = {"serialización": "serialization", "vocabulario": "vocabulary", "consumidor": "consumer"}
NATURES = {"obligatoria": re.compile(r"\b(must|required|shall)\b", re.I),
           "recomendada": re.compile(r"\b(should|recommend\w*)\b", re.I)}
SCOPES = ("Web Schema.org",)

CARD_KEYS = ({"source", "version", "class", "summary", "quotes"}, {"level", "note"})
QUOTE_KEYS = ({"id", "section", "text"}, {"note"})
FILE_KEYS = ({"level", "requirements"}, set())
REQUIREMENT_KEYS = ({"id", "scope", "spec", "condition", "nature", "quotes", "method", "evidence",
                     "applicability", "not_evaluable"}, {"rationale"})
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
    if cls == APPLICABLE and card.get("level") not in LEVELS:
        errors.append(f"{where}: una especificación aplicable lleva level ({', '.join(LEVELS)})")
    if cls != APPLICABLE and "level" in card:
        errors.append(f"{where}: level solo corresponde a una especificación aplicable")
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


def check_requirement(where: str, req: dict, level: str, cards: dict) -> list:
    errors = keys(where, req, REQUIREMENT_KEYS)
    if not isinstance(req, dict):
        return errors
    errors += text_fields(where, req, ("method", "evidence", "applicability", "rationale"))
    errors += one_condition(where, req.get("condition"))
    if req.get("scope") not in SCOPES:
        errors.append(f"{where}: scope «{req.get('scope')}» sin perfil de implementación en el canon "
                      f"({', '.join(SCOPES)}; el resto, OQ-30)")
    nature = req.get("nature")
    if nature not in NATURES:
        errors.append(f"{where}: nature «{nature}» no es del canon ({', '.join(NATURES)})")
    not_evaluable = req.get("not_evaluable")
    if not (isinstance(not_evaluable, list) and all(isinstance(c, str) and c.strip() for c in not_evaluable)):
        errors.append(f"{where}: not_evaluable ha de ser una lista de textos (vacía si no tiene causas propias)")
    spec = req.get("spec")
    card = cards.get(spec)
    if card is None:
        errors.append(f"{where}: spec «{spec}» no tiene ficha")
    elif card.get("class") != APPLICABLE:
        errors.append(f"{where}: {spec} no es una especificación aplicable (D-132)")
    elif card.get("level") != level:
        errors.append(f"{where}: {spec} es de nivel {card.get('level')}, no {level}")
    quotes = req.get("quotes")
    if not (isinstance(quotes, list) and quotes):
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
    if card is not None and card.get("class") == APPLICABLE and not from_spec:
        errors.append(f"{where}: ninguna cita es de su especificación ({spec})")
    elif nature in NATURES and from_spec and not any(NATURES[nature].search(t) for t in from_spec):
        errors.append(f"{where}: ninguna cita de {spec} contiene el término que fija la naturaleza "
                      f"{nature} ({NATURES[nature].pattern}); cita el texto que la fija")
    return errors


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
    files = {stem: level for level, stem in LEVELS.items()}
    seen, natures = set(), dict.fromkeys(NATURES, 0)
    for path in sorted((REFERENCE / "requirements").glob("*.json")):
        where = str(path.relative_to(REFERENCE))
        data, problems = load(path)
        problems = problems or keys(where, data, FILE_KEYS)
        if problems:
            errors += problems
            continue
        level = files.get(path.stem)
        if level is None:
            errors.append(f"{where}: el fichero ha de ser el de un nivel ({', '.join(files)})")
            continue
        if data["level"] != level:
            errors.append(f"{where}: level «{data['level']}» no coincide con el fichero ({level})")
        if not isinstance(data["requirements"], list):
            errors.append(f"{where}: requirements ha de ser una lista")
            continue
        for req in data["requirements"]:
            rid = req.get("id") if isinstance(req, dict) else None
            at = f"{where} {rid or '(requisito sin id)'}"
            if not re.fullmatch(rf"ws-{path.stem}/\d{{3}}", str(rid)):
                errors.append(f"{at}: el id ha de ser ws-{path.stem}/001, ws-{path.stem}/002…")
            elif rid in seen:
                errors.append(f"{at}: id repetido")
            seen.add(rid)
            errors += check_requirement(at, req, level, cards)
            if isinstance(req, dict) and req.get("nature") in natures:
                natures[req["nature"]] += 1
    quotes = sum(len(c.get("quotes") or []) for c in cards.values())
    applicable = sum(c.get("class") == APPLICABLE for c in cards.values())
    summary = [f"{len(cards)} fichas ({applicable} de especificaciones aplicables), {quotes} citas, "
               f"{len(seen)} requisitos (" + ", ".join(f"{n} {k}s" for k, n in natures.items()) + ")"]
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
        for _, level, title, anchor in headings(path.read_text(encoding="utf-8")):
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
