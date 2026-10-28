"""Primitives over the graph of the markup, for the checks of Web Schema.org.

A path selects entities: its first step is a type (`Product`: entities of Product or a subtype,
minus those with their own rules, method common point 3), `^Organization` (top level only) or
`@valued` (valued entities of the review snippet guide); each next step follows a property to the
entities that are its values, optionally of a type (`hasShippingService:ShippingService`). Links
are followed by nesting or by identifier (method common, point 4): a reference whose entity the
page does not define is kept apart (`refs`), and a check with nothing else to decide on is NE.

The primitives are the forms most requirements take: each entity has a property, at most one
value, each value passes a test, none has, not both, conditional presence, the type of a value.
Applicability is what their requirements say: «El marcado contiene al menos una X con Y» is NA
when no X has Y.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from .. import vocab
from ..graph import Entity, Lit, Ref, is_type
from . import NA, NE, SAT, UNSAT, Case, Result, capped

REF_NE = "Una referencia por @id no se resuelve en el marcado de la página (método común, punto 4)."


@dataclass
class Sel:
    entities: list = field(default_factory=list)
    refs: list = field(default_factory=list)   # unresolved references met on the way


def _start(graph, step: str) -> list:
    if step == "@valued":
        return graph.valued()
    if step.startswith("^"):
        return graph.top_of(step[1:])
    if step == "*":
        return list(graph.entities)
    return graph.of(step)


def select(case: Case, path: str) -> Sel:
    """The entities of a path, or of several joined with `|` (each entity once)."""
    if "|" in path:
        out = Sel()
        for part in path.split("|"):
            sel = select(case, part)
            out.entities += [e for e in sel.entities if all(e is not x for x in out.entities)]
            out.refs += sel.refs
        return out
    steps = path.split(">")
    sel = Sel(_start(case.graph, steps[0]))
    for step in steps[1:]:
        prop, _, cls = step.partition(":")
        out, seen = [], set()
        for e in sel.entities:
            for v in e.values(prop):
                if isinstance(v, Ref):
                    sel.refs.append(v)
                elif isinstance(v, Entity) and (not cls or is_type(v, cls)) and id(v) not in seen:
                    seen.add(id(v))
                    out.append(v)
        sel = Sel(out, sel.refs)
    return sel


def text(v) -> str:
    """The text of a value: a literal's, or the identifier of an entity or a reference."""
    if isinstance(v, Lit):
        return v.text()
    if isinstance(v, (Entity, Ref)):
        return v.id or ""
    return str(v)


def enum_name(v) -> str:
    """An enumeration value by its short name: `https://schema.org/InStock`, `schema:InStock` or
    `InStock` → `InStock`."""
    t = text(v).strip()
    return vocab.short(t) or t


def label(e) -> str:
    return e.label() if isinstance(e, Entity) else f"{text(e)!r} [{getattr(e, 'where', '')}]"


def _result(failures: list, examined: int, refs: list, what: str, extra=None) -> Result:
    ev = {"examinadas": examined, what: capped(failures)}
    if extra:
        ev.update(extra)
    if failures:
        return Result(UNSAT, ev)
    if refs:
        ev["sin resolver"] = capped(r.id for r in refs)
        return Result(NE, ev, REF_NE)
    return Result(SAT, ev)


def has(path: str, *props: str, universal: bool = False, where=None):
    """Each entity of the path has a non-empty value of one of `props`. NA without entities, or
    no satisfecho if the requirement is universal («Si el marcado no contiene ninguna…»)."""
    def run(case: Case) -> Result:
        sel = select(case, path)
        es = [e for e in sel.entities if where is None or where(e)]
        if not es:
            if sel.refs:
                return Result(NE, {"sin resolver": capped(r.id for r in sel.refs)}, REF_NE)
            if universal:
                return Result(UNSAT, {"examinadas": 0}, f"El marcado no contiene ninguna entidad de {path}.")
            return Result(NA, None, f"El marcado no contiene ninguna entidad de {path}.")
        missing = [label(e) for e in es if not any(e.has(p) for p in props)]
        return _result(missing, len(es), sel.refs, f"sin {' ni '.join(props)}")
    return run


def at_most_one(path: str, prop: str, key=None):
    """Each entity of the path has at most one value of `prop` (or one distinct `key(value)`).
    NA if none has it."""
    def run(case: Case) -> Result:
        sel = select(case, path)
        es = [e for e in sel.entities if e.has(prop)]
        if not es:
            return Result(NA, None, f"Ninguna entidad de {path} tiene {prop}.")
        bad = []
        for e in es:
            values = [v for v in e.values(prop) if text(v).strip() or isinstance(v, Entity)]
            if key is not None:
                values = {k for k in (key(v) for v in values) if k}
            if len(values) > 1:
                bad.append(f"{label(e)}: {len(values)} valores")
        return _result(bad, len(es), [], f"con más de un {prop}")
    return run


def values_ok(path: str, prop: str, test, describe: str, literal_only: bool = False, where=None):
    """Each value of `prop` of the entities of the path passes `test` (True / False; None leaves
    the value out). NA without values."""
    def run(case: Case) -> Result:
        sel = select(case, path)
        pairs = [(e, v) for e in sel.entities if where is None or where(e) for v in e.values(prop)
                 if not (literal_only and not isinstance(v, Lit))]
        judged = [(e, v, test(v)) for e, v in pairs]
        judged = [(e, v, r) for e, v, r in judged if r is not None]
        if not judged:
            if sel.refs:
                return Result(NE, {"sin resolver": capped(r.id for r in sel.refs)}, REF_NE)
            return Result(NA, None, f"El marcado no contiene valores de {prop} en {path}.")
        bad = [f"{label(e)}: {prop} = {text(v)!r}" for e, v, r in judged if not r]
        ok = [f"{text(v)!r}" for e, v, r in judged if r]
        return _result(bad, len(judged), sel.refs, f"que no son {describe}", {"válidos": capped(ok)})
    return run


def enum(path: str, prop: str, allowed, where=None):
    allowed = set(allowed)
    return values_ok(path, prop, lambda v: enum_name(v) in allowed, f"uno de {', '.join(sorted(allowed))}",
                     where=where)


def none_has(path: str, prop: str, where=None):
    """No entity of the path has `prop`. NA without entities."""
    def run(case: Case) -> Result:
        sel = select(case, path)
        es = [e for e in sel.entities if where is None or where(e)]
        if not es:
            return Result(NA, None, f"El marcado no contiene ninguna entidad de {path} que cumpla la condición.")
        bad = [label(e) for e in es if e.has(prop)]
        return _result(bad, len(es), sel.refs, f"con {prop}")
    return run


def not_both(path: str, a: str, b: str):
    """No entity of the path has both `a` and `b`. NA if none has either."""
    def run(case: Case) -> Result:
        sel = select(case, path)
        es = [e for e in sel.entities if e.has(a) or e.has(b)]
        if not es:
            return Result(NA, None, f"Ninguna entidad de {path} tiene {a} o {b}.")
        bad = [label(e) for e in es if e.has(a) and e.has(b)]
        return _result(bad, len(es), [], f"con {a} y {b}")
    return run


def value_types(path: str, prop: str, ok, describe: str):
    """Each value of `prop` is an entity for which `ok(entity)` holds (a literal never is)."""
    def run(case: Case) -> Result:
        sel = select(case, path)
        pairs = [(e, v) for e in sel.entities for v in e.values(prop)]
        if not pairs:
            return Result(NA, None, f"Ninguna entidad de {path} tiene {prop}.")
        bad = [f"{label(e)}: {prop} = {label(v)}" for e, v in pairs if not isinstance(v, Ref) and not ok(v)]
        refs = [v for e, v in pairs if isinstance(v, Ref)]
        return _result(bad, len(pairs), refs, f"que no son {describe}")
    return run


def prop_is(prop: str, *names: str):
    """Predicate: the entity has a value of `prop` that is one of the enumeration `names`."""
    names = set(names)
    return lambda e: any(enum_name(v) in names for v in e.values(prop))


def of_type(*classes: str):
    return lambda v: any(is_type(v, c) for c in classes)


# --- Value tests ---------------------------------------------------------------------------

DATE = r"\d{4}-\d{2}-\d{2}"
TIME = r"\d{2}:\d{2}(:\d{2}(\.\d+)?)?"
ZONE = r"(Z|[+-]\d{2}:?\d{2})"
ISO_DATE = re.compile(rf"^{DATE}$")
ISO_DATETIME = re.compile(rf"^{DATE}T{TIME}{ZONE}?$")
ISO_DATETIME_ZONE = re.compile(rf"^{DATE}T{TIME}{ZONE}$")
ISO_TIME = re.compile(rf"^{TIME}{ZONE}?$")
INTEGER = re.compile(r"^[+-]?\d+$")
NUMBER = re.compile(r"^[+-]?(\d+(\.\d*)?|\.\d+)$")
RESERVED_COUNTRIES = {"EU", "IC", "CP", "CQ"}


def _valid_date(s: str) -> bool:
    import datetime
    try:
        datetime.date.fromisoformat(s[:10])
        return True
    except ValueError:
        return False


def iso_date_or_datetime(v) -> bool:
    s = text(v).strip()
    return bool((ISO_DATE.match(s) or ISO_DATETIME.match(s)) and _valid_date(s))


def iso_datetime_with_zone(v) -> bool:
    s = text(v).strip()
    return bool(ISO_DATETIME_ZONE.match(s) and _valid_date(s))


def iso_time(v) -> bool:
    return bool(ISO_TIME.match(text(v).strip()))


def non_negative_integer(v) -> bool:
    if isinstance(v, Lit) and isinstance(v.value, bool):
        return False
    if isinstance(v, Lit) and isinstance(v.value, (int, float)):
        return float(v.value).is_integer() and v.value >= 0
    s = text(v).strip()
    return bool(re.match(r"^\+?\d+$", s))


def is_number(v) -> bool:
    if isinstance(v, Lit) and isinstance(v.value, bool):
        return False
    if isinstance(v, Lit) and isinstance(v.value, (int, float)):
        return True
    return bool(NUMBER.match(text(v).strip()))


def number(v) -> float | None:
    if isinstance(v, Lit) and isinstance(v.value, (int, float)) and not isinstance(v.value, bool):
        return float(v.value)
    s = text(v).strip()
    return float(s) if NUMBER.match(s) else None


def currency(v) -> bool:
    from references.read import currency_codes
    return text(v).strip().upper() in currency_codes()


def country(v) -> bool | None:
    """An assigned ISO 3166-1 alpha-2 code; an entity (a Country) is left out."""
    if isinstance(v, (Entity, Ref)):
        return None
    from references.read import country_codes
    code = text(v).strip().upper()
    return len(code) == 2 and code in country_codes() and code not in RESERVED_COUNTRIES
