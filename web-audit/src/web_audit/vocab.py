"""Schema.org at the release the reference pins (30.1, D-130), read from references.

Terms are short names (`Product`, `offers`): the IRI `https://schema.org/Product` (or http) without
its namespace. What the methods of the reference need from the release: whether a term is a class,
a property or an enumeration member; the subclasses of a class (transitive rdfs:subClassOf); the
expected types (rangeIncludes) and domains of a property; and the type of each enumeration member.
"""
from __future__ import annotations

import functools
import json
import re

from references.store import pinned

SOURCE = "schemaorg"
SCHEMA_IRI = re.compile(r"^https?://schema\.org/", re.I)


def short(iri: str) -> str | None:
    """`https://schema.org/Product`, `http://schema.org/Product`, `schema:Product` → `Product`;
    anything else → None."""
    if not isinstance(iri, str):
        return None
    iri = iri.strip()
    if iri.startswith("schema:"):
        return iri[7:] or None
    m = SCHEMA_IRI.match(iri)
    return iri[m.end():] or None if m else None


def _ids(value) -> list[str]:
    values = value if isinstance(value, list) else [value] if value else []
    return [v["@id"] if isinstance(v, dict) else v for v in values]


class Vocabulary:
    def __init__(self, graph: list, context: dict) -> None:
        self.classes: set[str] = set()
        self.properties: set[str] = set()
        self.members: dict[str, set[str]] = {}   # enumeration member → its types
        self.parents: dict[str, set[str]] = {}
        self.ranges: dict[str, set[str]] = {}
        self.domains: dict[str, set[str]] = {}
        self.inverse: dict[str, str] = {}
        self.context = context
        for node in graph:
            term = short(node.get("@id", ""))
            if not term:
                continue
            kinds = {short(t) or t for t in _ids(node.get("@type"))}
            if "rdfs:Class" in kinds:
                self.classes.add(term)
                self.parents[term] = {short(p) for p in _ids(node.get("rdfs:subClassOf")) if short(p)}
            if "rdf:Property" in kinds:
                self.properties.add(term)
                self.ranges[term] = {short(t) for t in _ids(node.get("schema:rangeIncludes")) if short(t)}
                self.domains[term] = {short(t) for t in _ids(node.get("schema:domainIncludes")) if short(t)}
                inv = [short(t) for t in _ids(node.get("schema:inverseOf")) if short(t)]
                if inv:
                    self.inverse[term] = inv[0]
            if "rdfs:Class" not in kinds and "rdf:Property" not in kinds:
                self.members[term] = kinds
        # Classes may be declared after their members: keep only real types
        self.members = {m: {t for t in ts if t in self.classes} for m, ts in self.members.items()}

    @functools.cache
    def ancestors(self, term: str) -> frozenset[str]:
        out, todo = set(), [term]
        while todo:
            for parent in self.parents.get(todo.pop(), ()):
                if parent not in out:
                    out.add(parent)
                    todo.append(parent)
        return frozenset(out)

    def is_a(self, term: str, cls: str) -> bool:
        """`term` is `cls` or a subclass of it (transitive rdfs:subClassOf)."""
        return term == cls or cls in self.ancestors(term)

    def is_class(self, term: str) -> bool:
        return term in self.classes

    def is_property(self, term: str) -> bool:
        return term in self.properties


@functools.cache
def load() -> Vocabulary:
    folder = pinned(SOURCE)
    graph = json.loads((folder / "schemaorg-current-https.jsonld").read_text(encoding="utf-8"))["@graph"]
    context = json.loads((folder / "schemaorgcontext.jsonld").read_text(encoding="utf-8"))["@context"]
    return Vocabulary(graph, context)
