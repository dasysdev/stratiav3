"""Checks of the vocabulary level of Web Schema.org (reference/requirements/vocabulary.json), against
the release the reference pins (vocab: Schema.org 30.1)."""
from __future__ import annotations

import re
from urllib.parse import urljoin

from .. import vocab
from ..graph import Entity, Lit, Ref
from . import NA, Case, Result, capped, check
from .markup import country, label, text, values_ok, _result

GTINS = ("gtin", "gtin8", "gtin12", "gtin13", "gtin14")
GTIN_DIGITS = re.compile(r"^(\d{8}|\d{12}|\d{13}|\d{14})$")
DIGITAL_LINK = re.compile(r"^https?://[^/]+(/[^?#]*)?/01/(\d{8}|\d{12}|\d{13}|\d{14})(/|$|\?|#)")


def _value_types(v) -> list[str]:
    """Declared types of a value that is an entity, or of an enumeration member given by URL."""
    voc = vocab.load()
    if isinstance(v, Entity):
        types = list(v.types)
        for extra in v.values("additionalType"):
            short = vocab.short(text(extra))
            if short:
                types.append(short)
        return types
    if isinstance(v, (Lit, Ref)):
        t = text(v).strip()
        if re.match(r"^https?://schema\.org/", t, re.I):
            member = vocab.short(t)
            return sorted(voc.members.get(member, ()))
    return []


@check("ws-vocabulary/001")
def _expected_types(case: Case) -> Result:
    voc = vocab.load()
    pairs, outside = [], []
    for e in case.graph.entities:
        for prop, values in e.props.items():
            if not voc.is_property(prop):
                if values and any(isinstance(v, Entity) for v in values):
                    outside.append(f"{label(e)}: {prop}")
                continue
            for v in values:
                types = _value_types(v)
                if types:
                    pairs.append((e, prop, v, types))
    if not pairs:
        return Result(NA, None, "Ninguna propiedad de Schema.org 30.1 tiene como valor una entidad con tipo declarado.")

    def expected(prop, types):
        ranges = voc.ranges.get(prop, set())
        return any(voc.is_a(t, r) or voc.is_a(t, "Role") for t in types for r in ranges)
    bad = [f"{label(e)}: {prop} = {'/'.join(types)} (espera {', '.join(sorted(voc.ranges.get(prop, ())))})"
           for e, prop, v, types in pairs if not expected(prop, types)]
    return _result(bad, len(pairs), [], "de un tipo no esperado",
                   {"propiedades no definidas en 30.1": capped(dict.fromkeys(outside))} if outside else None)


@check("ws-vocabulary/002")
def _one_main_entity(case: Case) -> Result:
    page_url = case.page.url_final if case.page else case.site.url
    groups: dict[str, list] = {}
    used = False

    def key(x) -> str:
        if isinstance(x, (Entity, Ref)) and x.id:
            return x.id
        if isinstance(x, Lit):
            return urljoin(page_url, text(x).strip())
        return f"#{id(x)}"
    for e in case.graph.entities:
        for main in e.values("mainEntity"):
            used = True
            groups.setdefault(key(e), []).append(main)
        for page in e.values("mainEntityOfPage"):
            used = True
            groups.setdefault(key(page), []).append(e)
    if not used:
        return Result(NA, None, "El marcado no usa mainEntity ni mainEntityOfPage.")
    bad = []
    for page, mains in groups.items():
        distinct = {m.id if isinstance(m, (Entity, Ref)) and m.id else f"#{id(m)}" for m in mains}
        if len(distinct) > 1:
            bad.append(f"{page}: {len(distinct)} entidades principales")
    return _result(bad, len(groups), [], "con más de una entidad principal")


def _gtin_values(case: Case):
    return [(e, p, v) for e in case.graph.entities for p in GTINS for v in e.values(p)]


def _component(v) -> str | None:
    """The numeric component of a GTIN value: the value or the segment after 01 of a Digital Link."""
    if isinstance(v, Lit) and isinstance(v.value, (int, float)) and not isinstance(v.value, bool):
        s = str(int(v.value)) if float(v.value).is_integer() else str(v.value)
    else:
        s = text(v).strip()
    if GTIN_DIGITS.match(s):
        return s
    m = DIGITAL_LINK.match(s)
    return m.group(2) if m else None


@check("ws-vocabulary/005")
def _gtin_form(case: Case) -> Result:
    values = _gtin_values(case)
    if not values:
        return Result(NA, None, "El marcado no contiene valores de gtin, gtin8, gtin12, gtin13 ni gtin14.")
    bad = [f"{label(e)}: {p} = {text(v)!r}" for e, p, v in values if _component(v) is None]
    return _result(bad, len(values), [], "que no son 8, 12, 13 o 14 dígitos ni un GS1 Digital Link")


def check_digit(digits: str) -> bool:
    body, last = digits[:-1], int(digits[-1])
    total = sum(int(d) * (3 if i % 2 == 0 else 1) for i, d in enumerate(reversed(body)))
    return (10 - total % 10) % 10 == last


@check("ws-vocabulary/006")
def _gtin_check_digit(case: Case) -> Result:
    values = [(e, p, v, _component(v)) for e, p, v in _gtin_values(case)]
    values = [x for x in values if x[3]]
    if not values:
        return Result(NA, None, "Ningún valor de GTIN tiene 8, 12, 13 o 14 dígitos.")
    bad = [f"{label(e)}: {p} = {c}" for e, p, v, c in values if not check_digit(c)]
    return _result(bad, len(values), [], "con el dígito de control incorrecto")


@check("ws-vocabulary/007")
def _digital_link(case: Case) -> Result:
    es = list({id(e): e for e, p, v in _gtin_values(case) if DIGITAL_LINK.match(text(v).strip())}.values())
    if not es:
        return Result(NA, None, "Ningún valor de GTIN es una URL GS1 Digital Link.")
    bad = [label(e) for e in es if not e.has("hasGS1DigitalLink")]
    return _result(bad, len(es), [], "sin hasGS1DigitalLink")


@check("ws-vocabulary/008")
def _breadcrumb_positions(case: Case) -> Result:
    values = [(item, v) for b in case.graph.of("BreadcrumbList") for item in b.values("itemListElement")
              if isinstance(item, Entity) for v in item.values("position")]
    if not values:
        return Result(NA, None, "Ninguna BreadcrumbList tiene elementos con position.")

    def integer(v) -> bool:
        if isinstance(v, Lit) and isinstance(v.value, bool):
            return False
        if isinstance(v, Lit) and v.kind == "json-number":
            return isinstance(v.value, int)
        return bool(re.fullmatch(r"[+-]?\d+", text(v).strip()))
    bad = [f"{label(i)}: {text(v)!r}" for i, v in values if not integer(v)]
    return _result(bad, len(values), [], "que no son enteros")


@check("ws-vocabulary/009")
def _webpage_properties(case: Case) -> Result:
    voc = vocab.load()
    only_webpage = {p for p, d in voc.domains.items() if d == {"WebPage"}}
    uses = [(e, p) for e in case.graph.entities for p in e.props if p in only_webpage]
    loose = []
    if case.page is not None and case.page.doc is not None:
        from .. import microdata
        loose = [el for el in microdata.loose(case.page.doc) if set(el.get("itemprop", "").split()) & only_webpage]
    if not uses and not loose:
        return Result(NA, None, "El marcado no usa propiedades que en 30.1 tienen WebPage como único dominio.")
    bad = [f"{label(e)}: {p}" for e, p in uses if not any(voc.is_a(t, "WebPage") for t in e.types)]
    bad += [f"{el.where()}: {el.get('itemprop')} (sin item)" for el in loose]
    return _result(bad, len(uses) + len(loose), [], "fuera de una WebPage")


check("ws-vocabulary/010")(values_ok("*", "addressCountry", country, "códigos ISO 3166-1 alfa-2", literal_only=True))


def _numeric(v) -> bool:
    if isinstance(v, Lit) and isinstance(v.value, bool):
        return False
    if isinstance(v, Lit) and isinstance(v.value, (int, float)):
        return True
    if isinstance(v, Lit) and v.datatype and re.search(r"(integer|decimal|double|float|Number)$", v.datatype or ""):
        return True
    return bool(re.fullmatch(r"[+-]?(\d+(\.\d*)?|\.\d+)", text(v).strip()))


check("ws-vocabulary/011")(values_ok("QuantitativeValue|MonetaryAmount", "value", _numeric, "números"))
