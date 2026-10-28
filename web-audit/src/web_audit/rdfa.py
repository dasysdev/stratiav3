"""RDFa of a document, as RDFa Lite 1.1 (vocab, typeof, property, resource, prefix) plus the
attributes that give a value (content, href, src, datetime): the subset that Schema.org uses.

An element with typeof starts an entity (its identifier: resource, about, href or src); an element
with property adds a value to the current entity: the new entity if it also has typeof, else
content, datetime (time), an IRI (resource, href, src) or its text, kept as it is. Terms expand
with vocab, with a prefix in scope (prefix, xmlns:) or as absolute IRIs. A term that does not
expand is not RDFa for this purpose: Open Graph `property="og:…"` without its prefix declared
does not make the page RDFa with Schema.org.
"""
from __future__ import annotations

import re
from urllib.parse import urljoin

from . import vocab
from .graph import Entity, Lit
from .html import Document, Element

SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:")
PREFIX_PAIR = re.compile(r"(\S+):\s+(\S+)")


def prefixes_of(el: Element) -> dict:
    out = {}
    for name, value in el.attrs.items():
        if name.startswith("xmlns:"):
            out[name[6:]] = value
    for prefix, iri in PREFIX_PAIR.findall(el.get("prefix", "")):
        out[prefix] = iri
    return out


def expand(term: str, vocab_iri: str | None, prefixes: dict) -> str | None:
    term = term.strip()
    if term.startswith("[") and term.endswith("]"):
        term = term[1:-1]
    if ":" in term:
        prefix, suffix = term.split(":", 1)
        if prefix in prefixes and not suffix.startswith("//"):
            return prefixes[prefix] + suffix
        if SCHEME.match(term):
            return term
        return None
    return vocab_iri + term if vocab_iri else None


def _literal(el: Element, base: str):
    if el.has("content"):
        return el.get("content"), "text"
    if el.tag == "time" and el.has("datetime"):
        return el.get("datetime"), "text"
    for attr in ("resource", "href", "src"):
        if el.has(attr):
            return urljoin(base, el.get(attr).strip()), "url"
    return el.text(), "text"


def entities(doc: Document, base: str, page_id: str | None = None) -> list[Entity]:
    out: list[Entity] = []

    def walk(el: Element, vocab_iri, prefixes, subject: Entity | None):
        if el.has("vocab"):
            vocab_iri = el.get("vocab").strip() or None
        own = prefixes_of(el)
        if own:
            prefixes = {**prefixes, **own}
        props = [p for p in (expand(t, vocab_iri, prefixes) for t in el.get("property", "").split()) if p]
        new = None
        if el.has("typeof"):
            types = [expand(t, vocab_iri, prefixes) for t in el.get("typeof").split()]
            ident = next((el.get(a) for a in ("resource", "about") if el.has(a)), None)
            if ident is None and not props:
                ident = next((el.get(a) for a in ("href", "src") if el.has(a)), None)
            new = Entity([vocab.short(t) or t for t in types if t], "rdfa", f"RDFa {el.where()}",
                         urljoin(base, ident.strip()) if ident else None, top=not (props and subject), page=page_id)
            out.append(new)
        if props and subject is not None:
            if new is not None:
                v = new
            else:
                text, kind = _literal(el, base)
                v = Lit(text, kind, f"RDFa {el.where()}")
            for p in props:
                subject.add(vocab.short(p) or p, v)
        for child in el.children:
            if isinstance(child, Element):
                walk(child, vocab_iri, prefixes, new or subject)

    walk(doc.root, None, {}, None)
    return out


def schema_org(doc: Document) -> bool:
    """RDFa with Schema.org: some typeof or property that resolves to an IRI of Schema.org."""
    found = []

    def walk(el: Element, vocab_iri, prefixes):
        if el.has("vocab"):
            vocab_iri = el.get("vocab").strip() or None
        own = prefixes_of(el)
        if own:
            prefixes = {**prefixes, **own}
        for attr in ("typeof", "property"):
            for t in el.get(attr, "").split():
                if vocab.short(expand(t, vocab_iri, prefixes) or ""):
                    found.append(el)
        for child in el.children:
            if isinstance(child, Element):
                walk(child, vocab_iri, prefixes)

    walk(doc.root, None, {})
    return bool(found)
