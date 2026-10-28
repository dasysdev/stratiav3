"""Read access to the pinned versions, by format. The readers give the content of a source;
what it means for a system (catalog mappings, source cards, technical requirements) is that
system's own.

  taxonomy     Shopify categories and attributes, Shopify's mapping to Google, Google names
  Amazon PTD   properties and definition of a product type, values of its enums
  vocabulary   definition of each term of a vocabulary in JSON-LD (Schema.org, GS1)
  documents    sections of a text.md: a heading and everything under it
  properties   the property tables of a document (Google Search): each property of a type, in
               the table of required or of recommended properties, cited source:Type.property@version
  laws         the passage a citation ley:CODE-article.apartado@version names (an article, an
               apartado, a letter), in the text.md of that version of the law
  codes        ISO 4217 currency codes (SIX) and ISO 3166-1 alpha-2 country codes (EU Vocabularies)
"""
import functools
import gzip
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path

from .store import RefsError, natural, pinned, pins, refs_dir, sources, versions

SHOPIFY_CATEGORIES = "categories.es.json.gz"
SHOPIFY_ATTRIBUTES = "attributes.es.json.gz"
GOOGLE_FILE = "taxonomy-with-ids.es-ES.txt"
BTG_FILE = "browse_tree.es.xml.gz"
VOCABULARY = "schemaorg-current-https.jsonld"   # the vocabulary of a Schema.org release
HEADING = re.compile(r"^(#{1,6}) (.*?)(?: \{#([^}]*)\})?$")


def load_gz(path: Path):
    return json.loads(gzip.decompress(path.read_bytes()))


def short(gid: str) -> str:
    return gid.rsplit("/", 1)[-1] if gid else gid


# --- Taxonomy -----------------------------------------------------------------

def shopify_categories_in(folder: Path) -> dict:
    return {short(c["id"]): c for v in load_gz(folder / SHOPIFY_CATEGORIES)["verticals"] for c in v["categories"]}


def google_rules_in(folder: Path) -> dict:
    """Shopify category → (English full name, [(Google id, Google full name)]) of a shopify-google version."""
    out = {}
    for path in sorted(folder.glob("integrations.google.*.json.gz")):
        for mapping in load_gz(path)["mappings"]:
            for rule in mapping["rules"]:
                out[short(rule["input"]["category"]["id"])] = (
                    rule["input"]["category"]["full_name"],
                    [(o["id"], o["full_name"]) for o in rule["output"]["category"]],
                )
    return out


def google_names_in(folder: Path) -> dict:
    lines = (folder / GOOGLE_FILE).read_text(encoding="utf-8").splitlines()
    return dict(l.split(" - ", 1) for l in lines if " - " in l and not l.startswith("#"))


@functools.cache
def shopify_categories() -> dict:
    """Shopify categories of the pinned version, by short id."""
    return shopify_categories_in(pinned("shopify"))


@functools.cache
def shopify_attributes() -> dict:
    return {a["handle"]: a for a in load_gz(pinned("shopify") / SHOPIFY_ATTRIBUTES)["attributes"]}


@functools.cache
def google_mapping() -> dict:
    """Shopify's official mapping to Google, pinned version."""
    return google_rules_in(pinned("shopify-google"))


@functools.cache
def google_names() -> dict:
    return google_names_in(pinned("google"))


def browse_tree() -> Path:
    """The Amazon.es browse tree of the pinned version (XML, gzip)."""
    return pinned("amazon-btg") / BTG_FILE


# --- Amazon PTD ---------------------------------------------------------------

def ptd(product_type: str) -> tuple:
    """(properties of the JSON schema, definition) of an Amazon PTD, pinned version."""
    base = pinned("amazon-ptd")
    path = base / f"schemas/{product_type}.schema.json.gz"
    if not path.exists():
        raise RefsError(f"no existe el PTD {product_type}")
    definition = json.loads((base / f"definitions/{product_type}.json").read_text(encoding="utf-8"))
    return load_gz(path)["properties"], definition


def enum_values(node, out=None) -> list:
    """Every value of the enums in a JSON schema node (their display names when present)."""
    out = [] if out is None else out
    if isinstance(node, dict):
        if isinstance(node.get("enum"), list):
            out.extend(node.get("enumNames") or node["enum"])
        for v in node.values():
            enum_values(v, out)
    elif isinstance(node, list):
        for v in node:
            enum_values(v, out)
    return out


# --- Vocabularies in JSON-LD --------------------------------------------------

def literal(value) -> str:
    if isinstance(value, list):
        return " ".join(literal(v) for v in value)
    return value.get("@value", "") if isinstance(value, dict) else str(value)


def ids(value) -> list:
    values = value if isinstance(value, list) else [value] if value else []
    return [v["@id"] if isinstance(v, dict) else v for v in values]


@functools.lru_cache(maxsize=None)
def vocabulary(path: Path) -> dict:
    """Definition (rdfs:comment) of each term of a vocabulary in JSON-LD."""
    graph = json.loads(path.read_text(encoding="utf-8")).get("@graph", [])
    return {node["@id"]: literal(node.get("rdfs:comment", "")) for node in graph if "@id" in node}


# --- Documents ----------------------------------------------------------------

def headings(text: str) -> list:
    """(line, level, title, anchor) of each heading of a text.md, outside code blocks."""
    out, code = [], False
    for i, line in enumerate(text.splitlines()):
        if line.startswith("```"):
            code = not code
        elif not code and (m := HEADING.match(line)):
            out.append((i, len(m[1]), m[2], m[3]))
    return out


def document_section(text: str, section: str) -> str:
    """A heading and everything under it, up to the next heading of the same or a higher level.
    `section` is an anchor (#product-properties) or, for a heading without one, its text."""
    heads = headings(text)
    found = [h for h in heads if (h[3] == section[1:] if section.startswith("#") else h[2] == section)]
    if not found:
        raise RefsError(f"no existe la sección {section}")
    if len(found) > 1:
        raise RefsError(f"hay {len(found)} encabezados «{section}»; nombra la sección por su ancla")
    line, level = found[0][:2]
    end = next((h[0] for h in heads if h[0] > line and h[1] <= level), None)
    return "\n".join(text.splitlines()[line:end])


# --- Citable text of a source -------------------------------------------------

def citable(source: str, kind: str) -> Path:
    """The file of the pinned version of `source` that quotes come from: the vocabulary of a
    Schema.org release, the text of a page, or a vocabulary in JSON-LD. A PDF has none."""
    folder = pinned(source)
    if kind == "schemaorg":
        return folder / VOCABULARY
    names = [f["path"] for f in json.loads((folder / "MANIFEST.json").read_text(encoding="utf-8"))["files"]]
    name = "text.md" if "text.md" in names else names[0]
    if name != "text.md" and Path(name).suffix not in (".jsonld", ".json"):
        raise RefsError(f"{source}: {name} no tiene texto citable")
    return folder / name


def section_text(source: str, kind: str, section: str) -> str:
    """A section of the pinned version: of a text.md (see document_section) or a term of a
    vocabulary (schema:gtin), whose text is its definition."""
    path = citable(source, kind)
    if path.name == "text.md":
        return document_section(path.read_text(encoding="utf-8"), section)
    terms = vocabulary(path)
    if section not in terms:
        raise RefsError(f"no existe el término {section} en {path.name}")
    return terms[section]


# --- Property tables of a document (Google Search) ----------------------------

TYPE_DEFINITIONS = "structured-data-type-definitions"     # the section that holds the tables
TABLES = {"Required properties": "required", "Recommended properties": "recommended"}
TYPE_HEADING = re.compile(r"^([A-Z0-9][A-Za-z0-9]*)(?: \(.*\)| for .*)?$")  # Offer · QuantitativeValue (for unit pricing)
ROOT_TYPE = re.compile(r"\(([A-Z][A-Za-z0-9]*)\) structured data$")      # H1 that names a single type
NAME = re.compile(r"[a-z][A-Za-z0-9]*(?:\.[a-z][A-Za-z0-9]*)*")
TYPE = r"[A-Z0-9][A-Za-z0-9]*"
EXPECTS = re.compile(rf"(?:Repeated )?{TYPE}(?: or {TYPE})*(?: \([^)]*\))?")
CITATION = re.compile(r"^([a-z0-9]+(?:-[a-z0-9]+)*):([A-Z0-9][A-Za-z0-9]*)\.(\S+)@(\S+)$")


def cells(line: str) -> list:
    """Cells of a table row of a text.md. A cell of names may hold « | » (gtin | gtin8 | isbn):
    the names before the last cell belong to the first one."""
    parts = [c.strip() for c in line.strip().strip("|").split(" | ")]
    while len(parts) > 2 and NAME.fullmatch(parts[1]):
        parts[0:2] = [f"{parts[0]} | {parts[1]}"]
    return parts


def names(label: str) -> list:
    """The property names of a row: «price or priceSpecification.price», «gtin | gtin8»,
    «suggestedMaxAge (or suggestedAge.maxValue)». A row of prose («Choose either…») has none."""
    if not NAME.match(label):
        return []
    plain = re.sub(r" \((?!or )[^)]*\)", "", label)       # «itemReviewed (if review is not a Nested Review)»
    return [n for n in re.split(r" or | \| | \(or |\)", plain) if NAME.fullmatch(n)]


def expects(text: str):
    """The expected type that opens the description cell («Text or URL The unit…»), or None."""
    m = EXPECTS.match(text)
    return m[0] if m and re.match(r" [A-Z0-9\"(]", text[m.end():]) else None


def property_rows(text: str) -> list:
    """The rows of the property tables of a text.md, in the section of type definitions: type
    (that of the heading, or of the nearest ancestor heading that names one, or the single type
    of the H1), the property names, the table (required or recommended), the group inside it
    (Option A), the heading anchor, the expected type and the text of the description cell."""
    lines = text.splitlines()
    heads = headings(text)
    root = next((m[1] for h in heads if h[1] == 1 and (m := ROOT_TYPE.search(h[2]))), None)
    start = next((h for h in heads if h[3] == TYPE_DEFINITIONS), None)
    if start is None:
        return []
    end = next((h[0] for h in heads if h[0] > start[0] and h[1] <= start[1]), len(lines))
    by_line = {h[0]: h for h in heads}
    stack, table, group, anchor, rows = [], None, None, start[3], []
    i = start[0]
    while i < end:
        line = lines[i]
        if i in by_line:
            _, level, title, anchor = by_line[i]
            stack = [s for s in stack if s[0] < level] + [(level, m[1] if (m := TYPE_HEADING.match(title)) else None)]
            table = group = None
        elif line.startswith("|"):
            row = cells(line)
            if len(row) == 1:
                header = next((v for k, v in TABLES.items() if row[0].startswith(k)), None)
                table, group = (header, None) if header else (table, row[0])
            elif table:
                rows.append((row[0], row[1], table, group, anchor, stack))
        elif table and NAME.fullmatch(line) and i + 1 < end and EXPECTS.fullmatch(lines[i + 1]):
            # A row the page's HTML leaves without <tr> (Certification.name in merchant listing):
            # its cells come out as loose lines, up to the next row.
            j = next((k for k in range(i + 1, end) if lines[k].startswith("|") or k in by_line), end)
            body = " ".join(l.strip() for l in lines[i + 1:j] if l.strip())
            rows.append((line, body, table, group, anchor, stack))
            i = j
            continue
        i += 1
    out = []
    for label, body, table, group, anchor, stack in rows:
        owner = next((t for _, t in reversed(stack) if t), root)
        found = names(label)
        out.append({"type": owner, "property": found[0] if found else None, "names": found, "label": label,
                    "table": table, "group": group, "heading": f"#{anchor}", "expects": expects(body), "text": body})
    return out


def document_version(source: str, version: str = None) -> tuple:
    """(version, text of its text.md): the pinned version of `source`, or `version`."""
    if version is None:
        folder = pinned(source)
        version = folder.name
    elif version not in versions(source):
        raise RefsError(f"{source}: no existe la versión {version}")
    else:
        folder = refs_dir() / source / version
    path = folder / "text.md"
    if not path.exists():
        raise RefsError(f"{source} {version}: no es una página con text.md")
    return version, path.read_text(encoding="utf-8")


@functools.lru_cache(maxsize=None)
def _properties(source: str, version: str) -> tuple:
    version, text = document_version(source, version)
    return tuple(dict(r, source=source, version=version) for r in property_rows(text))


def properties(source: str, version: str = None) -> list:
    """The rows of the property tables of a document (see property_rows), each with its source
    and version: the pinned one, or `version`. Empty if the document has no tables."""
    return [dict(r) for r in _properties(source, version or pins().get(source) or pinned(source).name)]


def property_citation(tag: str) -> list:
    """The rows a citation source:Type.property@version names (google-search-merchant-listing:
    Product.audience@2026-10-27): the property among the names of a row of that type, in that
    version. A type can have more than one table (QuantitativeValue for unit pricing and for
    shipping times), so there may be several rows. Error if the citation names none."""
    m = CITATION.match(tag)
    if not m:
        raise RefsError(f"{tag}: la cita ha de ser fuente:Tipo.propiedad@versión")
    source, owner, prop, version = m.groups()
    found = [r for r in properties(source, version) if r["type"] == owner and prop in r["names"]]
    if not found:
        raise RefsError(f"{tag}: {source} {version} no tiene la propiedad {prop} de {owner}")
    return found


# --- Laws ---------------------------------------------------------------------

LAW = "ley"         # the prefix of a citation of a law: ley:TRLGDCU-97.1.e@2026-02-28
ARTICLE = re.compile(r"^## Art[íi]culo (\d+(?: ?[a-z]+)?)\b")      # Artículo 16 · Artículo 97. Título · 3 bis
MARK = re.compile(r"^(\d+|[a-zñ]{1,4})([.)º]) ")                     # 1. · e) · 8) · ii)


def law_codes(registry: dict = None) -> dict:
    """Code → source of each law (`cite` in sources.json)."""
    return {s["cite"]: sid for sid, s in (registry or sources()).items() if s["kind"] == "law"}


def law_reference(tag: str, codes: dict = None):
    """(source, code, path, version or None) of a citation ley:CODE[-article.apartado…][@version],
    or None if CODE is no registered law. The longest code wins; a path is the article and,
    after it, its apartados and letters (97.1.e → ["97", "1", "e"])."""
    if not tag.startswith(LAW + ":"):
        return None
    body, _, version = tag[len(LAW) + 1:].partition("@")
    codes = law_codes() if codes is None else codes
    found = [c for c in codes if body == c or body.startswith(c + "-")]
    if not found:
        return None
    code = max(found, key=len)
    rest = body[len(code) + 1:]
    return codes[code], code, rest.split(".") if rest else [], version or None


def mark_kind(m) -> tuple:
    """Siblings share a kind: numbered (1. or 8)), lettered (e)) or roman (ii))."""
    mark, punct = m[1], m[2]
    return ("number" if mark.isdigit() else "roman" if len(mark) > 1 and set(mark) <= set("ivxl") else "letter", punct)


def sections(lines: list) -> list:
    """(line, key) of each heading of a law's text.md: the number of an article (3 bis → 3bis),
    else the text of the heading (a division, a provision, an annex, the final formula)."""
    out = []
    for i, line in enumerate(lines):
        if line.startswith("## "):
            m = ARTICLE.match(line)
            out.append((i, m[1].replace(" ", "") if m else line[3:]))
    return out


def law_passage(text: str, path: list) -> str:
    """The passage of a law's text.md a path names: the whole text, an article (from its heading
    to the next heading) or, inside it, an apartado or a letter: the line its mark opens and the
    ones that follow, up to the next mark of the same kind."""
    lines = text.splitlines()
    if not path:
        return text
    heads = sections(lines)
    found = [i for i, key in heads if key == path[0] and ARTICLE.match(lines[i])]
    if not found:
        raise RefsError(f"no existe el artículo {path[0]}")
    if len(found) > 1:
        raise RefsError(f"hay {len(found)} artículos {path[0]}")
    end = next((i for i, _ in heads if i > found[0]), len(lines))
    span = lines[found[0]:end]
    for depth, token in enumerate(path[1:], 2):
        start = next((i for i, l in enumerate(span) if (m := MARK.match(l)) and m[1] == token.lower()), None)
        if start is None:
            raise RefsError(f"el artículo {path[0]} no tiene {'.'.join(path[1:depth])}")
        kind = mark_kind(MARK.match(span[start]))
        stop = next((j for j in range(start + 1, len(span)) if (m := MARK.match(span[j])) and mark_kind(m) == kind), len(span))
        span = span[start:stop]
    return "\n".join(span)


def law_citation(tag: str, codes: dict = None) -> dict:
    """The passage a citation of a law names, in its version (the pinned one if it has none):
    {source, code, path, version, text}. Error if the law is not registered, the version is not
    in references/var or the passage does not exist in it."""
    found = law_reference(tag, codes)
    if not found:
        raise RefsError(f"{tag}: no es una cita de una norma registrada (ley:CÓDIGO-artículo.apartado@versión)")
    source, code, path, version = found
    version, text = document_version(source, version)
    try:
        passage = law_passage(text, path)
    except RefsError as e:
        raise RefsError(f"{tag}: {source} {version}: {e}") from None
    return {"source": source, "code": code, "path": path, "version": version, "text": passage}


def law_parts(text: str) -> dict:
    """Key → text of each part of a law's text.md: what precedes the first heading («inicio»), and
    each heading with what follows it, by article number or heading (a repeated one, numbered)."""
    lines = text.splitlines()
    heads = sections(lines)
    bounds = [(0, "inicio")] + heads
    out, seen = {}, {}
    for n, (i, key) in enumerate(bounds):
        end = bounds[n + 1][0] if n + 1 < len(bounds) else len(lines)
        seen[key] = seen.get(key, 0) + 1
        out[key if seen[key] == 1 else f"{key} ({seen[key]})"] = "\n".join(lines[i:end])
    return out


def law_changes(source: str, old: str, new: str) -> list:
    """The parts of a law (articles, and the rest by heading) whose text differs between two
    versions, added or removed included: articles first, in their order."""
    before, after = (law_parts(document_version(source, v)[1]) for v in (old, new))
    changed = [k for k in before.keys() | after.keys() if before.get(k) != after.get(k)]
    return sorted(changed, key=lambda k: (not re.match(r"\d", k), natural(k)))


# --- Codes (ISO 4217, ISO 3166-1) ---------------------------------------------

SKOS = "{http://www.w3.org/2004/02/skos/core#}"
RDF = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}"
XML_LANG = "{http://www.w3.org/XML/1998/namespace}lang"
ALPHA_2 = "ISO_3166_1_ALPHA_2"


@functools.cache
def currency_codes(source: str = "iso-4217") -> dict:
    """Alphabetic code → {name, number, minor_units, entities} of the ISO 4217 list one (SIX),
    pinned version. A fund or a code without a country appears once per entity that uses it."""
    folder = pinned(source)
    path = next(folder.glob("*.xml"))
    out = {}
    for e in ET.parse(path).getroot().iter("CcyNtry"):
        code = e.findtext("Ccy")
        if code:
            item = out.setdefault(code, {"name": e.findtext("CcyNm"), "number": e.findtext("CcyNbr"),
                                         "minor_units": e.findtext("CcyMnrUnts"), "entities": []})
            item["entities"].append(e.findtext("CtryNm"))
    return out


@functools.cache
def country_codes(source: str = "iso-3166-1") -> dict:
    """ISO 3166-1 alpha-2 code → Spanish name of each concept of the EU Vocabularies country
    table that is not deprecated, pinned version. The table also holds a few codes that ISO
    keeps exceptionally reserved (EU, IC…): the source does not tell them apart."""
    folder = pinned(source)
    path = next(folder.glob("*.rdf"))
    out = {}
    for concept in ET.parse(path).getroot().iter(SKOS + "Concept"):
        if any(c.tag.endswith("}deprecated") and c.text == "true" for c in concept):
            continue
        name = next((l.text for l in concept.findall(SKOS + "prefLabel") if l.get(XML_LANG) == "es"), None)
        for n in concept.findall(SKOS + "notation"):
            if n.get(RDF + "datatype", "").endswith("#" + ALPHA_2):
                out[n.text] = name
    return out
