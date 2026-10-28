"""Checks of the serialization level of Web Schema.org (reference/requirements/serialization.json):
JSON-LD (001–018, over the analysis of jsonld.analyze), Microdata (019–036) and RDFa (037–044).

The document examined is the HTTP response (method common, point 1).
"""
from __future__ import annotations

import re

from .. import microdata, rdfa, vocab
from ..jsonld import is_iri_ref
from . import NA, NE, SAT, UNSAT, Case, Result, capped, check

INVALID_NE = ("Algún bloque JSON-LD no es JSON válido (ws-serialization/001) y en los demás no hay incumplimientos: "
              "no se puede examinar todo el JSON-LD.")
REMOTE_NE = ("No se pudo obtener un contexto remoto referenciado por @context, necesario para reconocer alias de "
             "palabras clave o expandir claves y valores, y sin él no se puede decidir.")


def _document(case: Case) -> Result | None:
    if case.page.doc is None:
        return Result(NE, {"outcome": case.page.outcome}, f"No se dispone del documento de la respuesta "
                                                          f"(outcome {case.page.outcome}).")
    return None


# --- JSON-LD ---------------------------------------------------------------------------------

@check("ws-serialization/001")
def _json_valid(case: Case) -> Result:
    r = _document(case)
    if r:
        return r
    blocks = case.page.blocks
    if not blocks:
        return Result(NA, None, "La página no contiene ningún elemento script con type application/ld+json.")
    bad = [f"{b.where()}: {b.error}" for b in blocks if not b.ok]
    return Result(UNSAT if bad else SAT, {"bloques": len(blocks), "no válidos": bad})


def jsonld_check(problem: str, seen: str | None, na: str, remote: bool = True):
    """`problem`: the key of the problems of the analysis; `seen`: the key whose count makes the
    requirement applicable (None: any valid block)."""
    def run(case: Case) -> Result:
        r = _document(case)
        if r:
            return r
        report = case.page.jsonld
        if not report.valid:
            if report.invalid and seen is None:
                return Result(NE, {"no válidos": [b.where() for b in report.invalid]}, INVALID_NE)
            return Result(NA, None, "La página no contiene ningún bloque JSON-LD con JSON válido.")
        if seen is not None and not report.seen.get(seen):
            if report.invalid:
                return Result(NE, {"no válidos": [b.where() for b in report.invalid]}, INVALID_NE)
            return Result(NA, None, na)
        problems = report.problems.get(problem, [])
        ev = {"bloques válidos": len(report.valid), "incumplimientos": capped(problems)}
        if seen is not None:
            ev["examinados"] = report.seen.get(seen, 0)
        if problems:
            return Result(UNSAT, ev)
        if report.invalid:
            ev["no válidos"] = [b.where() for b in report.invalid]
            return Result(NE, ev, INVALID_NE)
        if remote and report.remote:
            ev["contextos remotos"] = capped(report.remote)
            return Result(NE, ev, REMOTE_NE)
        return Result(SAT, ev)
    return run


check("ws-serialization/002")(jsonld_check("root", None, ""))
check("ws-serialization/003")(jsonld_check("duplicates", None, "", remote=False))
check("ws-serialization/004")(jsonld_check("context", "context", "Ningún bloque JSON-LD contiene @context.", remote=False))
check("ws-serialization/005")(jsonld_check("context-language", "context-language",
                                           "Ninguna definición de contexto local contiene @language.", remote=False))
check("ws-serialization/006")(jsonld_check("id", "id", "Ningún objeto de nodo tiene @id."))
check("ws-serialization/007")(jsonld_check("type", "type", "Ningún objeto de nodo tiene @type."))
check("ws-serialization/008")(jsonld_check("graph", "graph", "Ningún bloque JSON-LD contiene @graph."))
check("ws-serialization/009")(jsonld_check("nested-array", None, ""))
check("ws-serialization/010")(jsonld_check("empty-top", None, ""))
check("ws-serialization/011")(jsonld_check("value-type-language", "value", "Ningún bloque contiene un objeto de valor."))
check("ws-serialization/012")(jsonld_check("value-keys", "value", "Ningún bloque contiene un objeto de valor."))
check("ws-serialization/013")(jsonld_check("value-value", "value", "Ningún bloque contiene un objeto de valor."))
check("ws-serialization/014")(jsonld_check("value-type", "value-type", "Ningún objeto de valor tiene @type."))
check("ws-serialization/015")(jsonld_check("value-language", "value-language", "Ningún objeto de valor tiene @language."))
check("ws-serialization/016")(jsonld_check("list-keys", "list", "Ningún bloque contiene un objeto de lista."))
check("ws-serialization/017")(jsonld_check("set-keys", "set", "Ningún bloque contiene un objeto de conjunto."))
check("ws-serialization/018")(jsonld_check("base", None, ""))


# --- Microdata ---------------------------------------------------------------------------------------

def _microdata(case: Case, extra=None, na: str = "") -> Result | None:
    r = _document(case)
    if r:
        return r
    doc = case.page.doc
    if not microdata.schema_org(doc):
        return Result(NA, None, "La página no contiene Microdata con Schema.org.")
    if extra is not None and not extra(doc):
        return Result(NA, None, na)
    return None


def md_check(test, describe: str, extra=None, na: str = ""):
    """`test(doc)` returns the problems found."""
    def run(case: Case) -> Result:
        r = _microdata(case, extra, na)
        if r:
            return r
        bad = test(case.page.doc)
        return Result(UNSAT if bad else SAT, {describe: capped(bad)})
    return run


def _attrs(doc, name):
    return [el for el in doc.all() if el.has(name)]


def _tokens(el, name):
    return el.get(name, "").split()


ABSOLUTE = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:\S+$")


def absolute_url(token: str) -> bool:
    if not ABSOLUTE.match(token) or not is_iri_ref(token):
        return False
    scheme = token.split(":", 1)[0].lower()
    return token[len(scheme) + 1:].startswith("//") if scheme in ("http", "https") else True


def _vocabulary_of(token: str) -> str:
    cut = max(token.rfind("/"), token.rfind("#"))
    base = token[:cut + 1]
    return re.sub(r"^https?://schema\.org/", "schema.org", base, flags=re.I)


SCHEMA_TOKEN = re.compile(r"^https?://schema\.org/", re.I)
check("ws-serialization/019")(md_check(lambda d: [el.where() for el in _attrs(d, "itemtype") if not _tokens(el, "itemtype")],
                                       "itemtype sin tokens"))
check("ws-serialization/020")(md_check(lambda d: [el.where() for el in _attrs(d, "itemtype")
                                                  if len(set(_tokens(el, "itemtype"))) < len(_tokens(el, "itemtype"))],
                                       "itemtype con tokens repetidos"))
check("ws-serialization/021")(md_check(lambda d: [f"{el.where()}: {t}" for el in _attrs(d, "itemtype")
                                                  for t in _tokens(el, "itemtype") if not absolute_url(t)],
                                       "tokens que no son URL absolutas"))
check("ws-serialization/022")(md_check(lambda d: [el.where() for el in _attrs(d, "itemtype")
                                                  if len({_vocabulary_of(t) for t in _tokens(el, "itemtype")}) > 1],
                                       "itemtype con varios vocabularios",
                                       lambda d: any(len(_tokens(el, "itemtype")) > 1 for el in _attrs(d, "itemtype")),
                                       "Ningún itemtype tiene más de un token."))


def _schema_tokens(doc):
    return [(el, t) for el in _attrs(doc, "itemtype") for t in _tokens(el, "itemtype") if SCHEMA_TOKEN.match(t)]


@check("ws-serialization/023")
def _types_defined(case: Case) -> Result:
    r = _document(case)
    if r:
        return r
    pairs = _schema_tokens(case.page.doc)
    if not pairs:
        return Result(NA, None, "Ningún token de itemtype empieza por http://schema.org/ o https://schema.org/.")
    voc = vocab.load()
    bad = [f"{el.where()}: {t}" for el, t in pairs if not voc.is_class(vocab.short(t) or "")]
    return Result(UNSAT if bad else SAT, {"examinados": len(pairs), "tipos no definidos en 30.1": capped(bad)})


check("ws-serialization/024")(md_check(lambda d: [el.where() for el in _attrs(d, "itemtype") if not el.has("itemscope")],
                                       "itemtype sin itemscope"))
check("ws-serialization/025")(md_check(lambda d: [f"{el.where()}: {el.get('itemid')!r}" for el in _attrs(d, "itemid")
                                                  if not is_iri_ref(el.get("itemid").strip(" \t\n\f\r"))],
                                       "itemid que no son URL válidas", lambda d: bool(_attrs(d, "itemid")),
                                       "Ningún elemento tiene itemid."))
check("ws-serialization/026")(md_check(lambda d: [el.where() for el in _attrs(d, "itemid")
                                                  if not (el.has("itemscope") and el.has("itemtype"))],
                                       "itemid sin itemscope e itemtype", lambda d: bool(_attrs(d, "itemid")),
                                       "Ningún elemento tiene itemid."))
HAS_ITEMREF = (lambda d: bool(_attrs(d, "itemref")), "Ningún elemento tiene itemref.")
check("ws-serialization/027")(md_check(lambda d: [el.where() for el in _attrs(d, "itemref")
                                                  if len(set(_tokens(el, "itemref"))) < len(_tokens(el, "itemref"))],
                                       "itemref con tokens repetidos", *HAS_ITEMREF))
check("ws-serialization/028")(md_check(lambda d: [f"{el.where()}: {t}" for el in _attrs(d, "itemref")
                                                  for t in _tokens(el, "itemref") if t not in d.ids],
                                       "tokens sin elemento con ese id", *HAS_ITEMREF))
check("ws-serialization/029")(md_check(lambda d: [el.where() for el in _attrs(d, "itemref") if not el.has("itemscope")],
                                       "itemref sin itemscope", *HAS_ITEMREF))
HAS_ITEMPROP = (lambda d: bool(_attrs(d, "itemprop")), "Ningún elemento tiene itemprop.")
check("ws-serialization/030")(md_check(lambda d: [el.where() for el in _attrs(d, "itemprop") if not _tokens(el, "itemprop")],
                                       "itemprop sin tokens", *HAS_ITEMPROP))
check("ws-serialization/031")(md_check(lambda d: [el.where() for el in _attrs(d, "itemprop")
                                                  if len(set(_tokens(el, "itemprop"))) < len(_tokens(el, "itemprop"))],
                                       "itemprop con tokens repetidos", *HAS_ITEMPROP))


def relevant_types(items) -> dict:
    """Relevant types of each item: its item types or, without them, those of the item whose
    property it is."""
    parent = {}
    for it in items:
        for p in it.properties:
            parent.setdefault(id(p), it)
    out = {}

    def types(it, depth=0):
        if id(it.element) in out:
            return out[id(it.element)]
        if it.types or depth > 50:
            result = it.types
        else:
            up = parent.get(id(it.element))
            result = types(up, depth + 1) if up is not None else []
        out[id(it.element)] = result
        return result
    for it in items:
        types(it)
    return out


def _schema_items(case):
    items = case.page.items
    rel = relevant_types(items)
    return [it for it in items if any(SCHEMA_TOKEN.match(t) for t in rel[id(it.element)])]


@check("ws-serialization/032")
def _props_defined(case: Case) -> Result:
    r = _document(case)
    if r:
        return r
    items = [it for it in _schema_items(case) if it.properties]
    if not items:
        return Result(NA, None, "Ningún item con tipos relevantes de Schema.org tiene propiedades.")
    voc = vocab.load()
    bad = [f"{p.where()}: {t}" for it in items for p in it.properties for t in _tokens(p, "itemprop")
           if not absolute_url(t) and not voc.is_property(t)]
    return Result(UNSAT if bad else SAT, {"items": len(items), "propiedades no definidas en 30.1": capped(bad)})


URL_TYPES = {"Text", "Number", "Boolean", "Date", "DateTime", "Time", "Integer", "Float", "CssSelectorType",
             "XPathType", "PronounceableText"}


@check("ws-serialization/033")
def _url_elements(case: Case) -> Result:
    r = _document(case)
    if r:
        return r
    voc = vocab.load()

    def url_only(term):
        ranges = voc.ranges.get(term, set())
        return "URL" in ranges and not (ranges & URL_TYPES)
    pairs = [(p, t) for it in _schema_items(case) for p in it.properties if not p.has("itemscope")
             for t in _tokens(p, "itemprop") if url_only(t)]
    if not pairs:
        return Result(NA, None, "Ninguna propiedad de rango solo URL en un elemento sin itemscope.")
    bad = [f"{p.where()}: {t}" for p, t in pairs if p.tag not in microdata.URL_ELEMENTS]
    return Result(UNSAT if bad else SAT, {"examinadas": len(pairs), "fuera de un elemento de propiedad URL": capped(bad)})


check("ws-serialization/034")(md_check(lambda d: [e for it in microdata.items(d) for e in it.errors],
                                       "errores de microdata", *HAS_ITEMREF))
check("ws-serialization/035")(md_check(lambda d: microdata.cycles(d), "ciclos", *HAS_ITEMREF))


@check("ws-serialization/036")
def _loose_itemprop(case: Case) -> Result:
    r = _document(case)
    if r:
        return r
    doc = case.page.doc
    loose = microdata.loose(doc)
    if not _attrs(doc, "itemprop") or not (microdata.schema_org(doc) or loose):
        return Result(NA, None, "La página no tiene itemprop con Microdata de Schema.org ni itemprop sueltos.")
    return Result(UNSAT if loose else SAT, {"itemprop sin item": capped(f"{el.where()}: {el.get('itemprop')}" for el in loose)})


# --- RDFa ----------------------------------------------------------------------------------------------

CURIE_ATTRS = ("about", "resource", "typeof", "property", "rel", "rev", "datatype")
# Prefixes of the initial contexts of RDFa 1.1 and HTML+RDFa 1.1 (not frozen in the reference)
INITIAL = {"as", "cat", "cc", "cnt", "csvw", "ctag", "dc", "dc11", "dcat", "dcterms", "dqv", "duv", "earl", "foaf",
           "gldp", "gr", "grddl", "ht", "ical", "ldp", "ma", "oa", "odrl", "og", "org", "owl", "prov", "ptr", "qb",
           "rdf", "rdfa", "rdfs", "rev", "rif", "rr", "rss", "schema", "sd", "sioc", "skos", "skosxl", "sosa", "ssn",
           "time", "v", "vcard", "void", "wdr", "wdrs", "xhv", "xml", "xsd"}
NCNAME = re.compile(r"^[A-Za-z_][\w.\-]*$")


def _rdfa(case: Case, extra=None, na: str = "") -> Result | None:
    r = _document(case)
    if r:
        return r
    if not rdfa.schema_org(case.page.doc):
        return Result(NA, None, "La página no contiene RDFa con Schema.org.")
    if extra is not None and not extra(case.page.doc):
        return Result(NA, None, na)
    return None


def rdfa_check(test, describe: str, extra=None, na: str = ""):
    """`test(doc)` returns the problems found."""
    def run(case: Case) -> Result:
        r = _rdfa(case, extra, na)
        if r:
            return r
        bad = test(case.page.doc)
        return Result(UNSAT if bad else SAT, {describe: capped(bad)})
    return run


def _scoped_prefixes(doc):
    """(element, prefixes in scope) for every element."""
    out = []

    def walk(el, prefixes):
        own = rdfa.prefixes_of(el)
        if own:
            prefixes = {**prefixes, **own}
        out.append((el, prefixes))
        for c in el.children:
            if not isinstance(c, str):
                walk(c, prefixes)
    walk(doc.root, {})
    return out


def _curies(doc):
    """(element, value, prefix, expansion or None if the prefix is only in an initial context)."""
    found = []
    for el, prefixes in _scoped_prefixes(doc):
        for attr in CURIE_ATTRS:
            for token in el.get(attr, "").split():
                safe = token.startswith("[") and token.endswith("]")
                t = token[1:-1] if safe else token
                if ":" not in t:
                    continue
                prefix, ref = t.split(":", 1)
                if prefix in prefixes:
                    found.append((el, token, prefix, prefixes[prefix] + ref))
                elif prefix in INITIAL and not ref.startswith("//"):
                    found.append((el, token, prefix, None))
    return found


@check("ws-serialization/037")
def _curie_iris(case: Case) -> Result:
    r = _rdfa(case, lambda d: bool(_curies(d)), "No hay CURIE en los atributos RDFa.")
    if r:
        return r
    curies = _curies(case.page.doc)
    bad = [f"{el.where()}: {t} → {exp}" for el, t, _, exp in curies if exp is not None and not is_iri_ref(exp)]
    initial = [f"{el.where()}: {t}" for el, t, _, exp in curies if exp is None]
    ev = {"CURIE": len(curies), "no válidos": capped(bad), "solo con prefijo del contexto inicial": capped(initial)}
    if bad:
        return Result(UNSAT, ev)
    if initial:
        return Result(NE, ev, "El CURIE usa un prefijo que solo definen los contextos iniciales de RDFa 1.1 o de "
                              "HTML+RDFa 1.1, que no están congelados en la referencia.")
    return Result(SAT, ev)


def _prefix_decls(doc):
    return [el for el in doc.all() if el.has("prefix") or any(a.startswith("xmlns:") for a in el.attrs)]


check("ws-serialization/038")(rdfa_check(lambda d: [el.where() for el in _prefix_decls(d) if "_" in rdfa.prefixes_of(el)],
                                         "prefijo _", lambda d: bool(_prefix_decls(d)), "No hay atributos prefix ni xmlns:."))


@check("ws-serialization/039")
def _literal_spaces(case: Case) -> Result:
    r = _rdfa(case)
    if r:
        return r
    from ..graph import Lit
    lits = [v for e in case.graph.entities if e.syntax == "rdfa" for vs in e.props.values() for v in vs
            if isinstance(v, Lit) and v.kind == "text"]
    if not lits:
        return Result(NA, None, "El marcado RDFa no tiene literales.")
    bad = [f"{v.where}: {v.text()[:60]!r}" for v in lits
           if re.match(r"^[ \t\r\n]|.*[ \t\r\n]$", v.text(), re.S) or re.search(r"[ \t\r\n]{2,}", v.text())]
    return Result(UNSAT if bad else SAT, {"literales": len(lits), "con espacio innecesario": capped(bad)})


check("ws-serialization/040")(rdfa_check(lambda d: [el.where() for el in d.all("meta") if el.has("property") and not el.has("content")],
                                         "meta sin content", lambda d: any(el.has("property") for el in d.all("meta")),
                                         "Ningún meta tiene property."))


def _xmlns(doc):
    return [(el, a) for el in doc.all() for a in el.attrs if a.startswith("xmlns:")]


check("ws-serialization/041")(rdfa_check(lambda d: [f"{el.where()}: {a}" for el, a in _xmlns(d) if not NCNAME.match(a[6:])],
                                         "nombres no válidos", lambda d: bool(_xmlns(d)), "No hay atributos xmlns:."))


@check("ws-serialization/042")
def _xmlns_lowercase(case: Case) -> Result:
    r = _rdfa(case, lambda d: bool(_xmlns(d)), "No hay atributos xmlns:.")
    if r:
        return r
    names = re.findall(r"<[^>]*?\s(xmlns:[^\s=/>]+)", case.page.doc.source, re.I)
    bad = [n for n in names if n != n.lower()]
    return Result(UNSAT if bad else SAT, {"atributos": capped(names), "con mayúsculas": bad})


PREFIX_VALUE = re.compile(r"^([A-Za-z_][\w.\-]*: +\S+)( +[A-Za-z_][\w.\-]*: +\S+)*$")
check("ws-serialization/043")(rdfa_check(lambda d: [f"{el.where()}: {el.get('prefix')!r}" for el in _attrs(d, "prefix")
                                                    if not PREFIX_VALUE.match(re.sub(r"\s+", " ", el.get("prefix").strip()))],
                                         "prefix mal formados", lambda d: bool(_attrs(d, "prefix")), "No hay atributos prefix."))
check("ws-serialization/044")(rdfa_check(lambda d: [el.where() for el in d.all()
                                                    if el.has("lang") and el.has("xml:lang") and el.get("lang") != el.get("xml:lang")],
                                         "lang y xml:lang distintos",
                                         lambda d: any(el.has("lang") and el.has("xml:lang") for el in d.all()),
                                         "Ningún elemento tiene lang y xml:lang."))
