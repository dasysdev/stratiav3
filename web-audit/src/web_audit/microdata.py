"""Microdata of a document (WHATWG HTML, 5.2): items, their properties by the algorithm of 5.2.5
(with itemref and its microdata errors) and the entities of the graph.

The value of a property is that of 5.2.4 (meta: content; img and the media elements: src; a, area
and link: href; object: data; data and meter: value; time: datetime or its text; an element with
itemscope: the item; anything else: its text). As the methods of the reference say for the
ratings («el atributo content si lo hay y, si no, el texto del elemento»), and as consumers read
it, a content attribute on any element gives its value.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from urllib.parse import urljoin

from . import vocab
from .graph import Entity, Lit
from .html import Document, Element

URL_ELEMENTS = {"a", "area", "audio", "embed", "iframe", "img", "link", "object", "source", "track", "video"}
SRC = {"audio", "embed", "iframe", "img", "source", "track", "video"}
HREF = {"a", "area", "link"}


def tokens(value: str | None) -> list[str]:
    return (value or "").split()


@dataclass(eq=False)
class Item:
    element: Element
    types: list[str]
    properties: list[Element] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)


def properties(doc: Document, root: Element) -> tuple[list[Element], list[str]]:
    """Properties of the item of `root` (5.2.5) and the microdata errors found on the way."""
    results, errors = [], []
    memory = {id(root)}
    pending = [c for c in root.children if isinstance(c, Element)]
    for token in tokens(root.get("itemref")):
        target = doc.ids.get(token)
        if target is not None:
            pending.append(target)
    while pending:
        current = pending.pop()
        if id(current) in memory:
            errors.append(f"{current.where()} se alcanza dos veces desde {root.where()}")
            continue
        memory.add(id(current))
        if not current.has("itemscope"):
            pending.extend(c for c in current.children if isinstance(c, Element))
        if tokens(current.get("itemprop")):
            results.append(current)
    order = {id(e): i for i, e in enumerate(doc.root.iter())}
    results.sort(key=lambda e: order.get(id(e), 0))
    return results, errors


def items(doc: Document) -> list[Item]:
    return [Item(el, tokens(el.get("itemtype")), *properties(doc, el)) for el in doc.all() if el.has("itemscope")]


def value(el: Element, base: str):
    """(value, kind) of a property element that is not an item."""
    if el.has("content"):
        return el.get("content"), "text"
    tag = el.tag
    if tag == "meta":
        return el.get("content", ""), "text"
    if tag in SRC:
        return urljoin(base, el.get("src", "").strip()), "url"
    if tag in HREF:
        return urljoin(base, el.get("href", "").strip()), "url"
    if tag == "object":
        return urljoin(base, el.get("data", "").strip()), "url"
    if tag in ("data", "meter"):
        return el.get("value", ""), "text"
    if tag == "time" and el.has("datetime"):
        return el.get("datetime"), "text"
    return el.text(), "text"


def _type(token: str) -> str:
    return vocab.short(token) or token


def _prop(token: str) -> str:
    return vocab.short(token) or token


def entities(doc: Document, base: str, page_id: str | None = None) -> list[Entity]:
    found = items(doc)
    by_element = {id(it.element): it for it in found}
    as_property = {id(p) for it in found for p in it.properties}
    made: dict[int, Entity] = {}
    for it in found:
        el = it.element
        itemid = el.get("itemid")
        ident = urljoin(base, itemid.strip()) if itemid is not None and itemid.strip() else None
        top = id(el) not in as_property
        made[id(el)] = Entity([_type(t) for t in it.types], "microdata", f"Microdata {el.where()}", ident, top,
                              page=page_id)
    for it in found:
        entity = made[id(it.element)]
        for prop_el in it.properties:
            if id(prop_el) in by_element:
                v = made[id(prop_el)]
            else:
                text, kind = value(prop_el, base)
                v = Lit(text, kind, f"Microdata {prop_el.where()}")
            for token in dict.fromkeys(tokens(prop_el.get("itemprop"))):
                entity.add(_prop(token), v)
    return list(made.values())


def loose(doc: Document) -> list[Element]:
    """Elements with itemprop that are a property of no item (ws-serialization/036)."""
    reached = {id(p) for it in items(doc) for p in it.properties}
    return [el for el in doc.all() if el.has("itemprop") and id(el) not in reached]


def cycles(doc: Document) -> list[str]:
    """Cycles of the graph of items (an edge per property whose value is an item)."""
    found = items(doc)
    by_element = {id(it.element): it for it in found}
    edges = {id(it.element): [id(p) for p in it.properties if id(p) in by_element] for it in found}
    out, state = [], {}

    def visit(node, path):
        state[node] = 1
        for nxt in edges.get(node, []):
            if state.get(nxt) == 1:
                out.append(" → ".join(by_element[n].element.where() for n in path + [nxt]))
            elif nxt not in state:
                visit(nxt, path + [nxt])
        state[node] = 2

    for it in found:
        if id(it.element) not in state:
            visit(id(it.element), [id(it.element)])
    return out


def schema_org(doc: Document) -> bool:
    """Microdata with Schema.org: some itemtype token contains «schema.org»."""
    return any("schema.org" in t for el in doc.all() if el.has("itemtype") for t in tokens(el.get("itemtype")))
