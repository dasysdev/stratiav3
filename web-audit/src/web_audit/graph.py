"""The entities of the markup of a page, in the three syntaxes, as one graph.

Method common to Marcado (reference/README.md): every entity counts, also those of related
products (point 2); nodes with the same identifier are one entity, across blocks and syntaxes
(points 2 and 4); a link is followed by nesting or by identifier, and a reference whose entity is
not on the page stays unresolved (`Ref`): what depends on it is NE (point 4). The rules of a type
apply to its subtypes, except ProductGroup for Product and AggregateOffer for Offer, which have
their own (point 3).

Terms of Schema.org are short names (`Product`, `offers`); other terms keep their IRI or their key.
"""
from __future__ import annotations

from dataclasses import dataclass, field

from . import vocab

# Rules of a type that do not apply to one of its subtypes (method common, point 3)
OWN_RULES = {"Product": ("ProductGroup",), "Offer": ("AggregateOffer",)}
# Types the review snippet guide accepts for the object of a review (method common, point 3)
VALUED = ("Book", "Course", "CreativeWorkSeason", "CreativeWorkSeries", "Episode", "Event", "Game", "HowTo",
          "LocalBusiness", "MediaObject", "Movie", "MusicPlaylist", "MusicRecording", "Organization",
          "Product", "Recipe", "SoftwareApplication")


@dataclass(eq=False)
class Lit:
    """A literal value: `kind` is json-string, json-number, json-boolean, value-object (with its
    `datatype`), text (Microdata or RDFa content) or url (a URL property element)."""
    value: object
    kind: str
    where: str = ""
    datatype: str | None = None

    def text(self) -> str:
        v = self.value
        if isinstance(v, bool):
            return "true" if v else "false"
        return "" if v is None else str(v)


@dataclass(eq=False)
class Ref:
    """A reference by identifier to an entity that the page does not define."""
    id: str
    where: str = ""

    def text(self) -> str:
        return self.id


@dataclass(eq=False)
class Entity:
    types: list[str]
    syntax: str
    where: str
    id: str | None = None
    top: bool = False
    props: dict[str, list] = field(default_factory=dict)
    page: str | None = None
    places: list[str] = field(default_factory=list)
    parents: list[tuple["Entity", str]] = field(default_factory=list)

    def add(self, prop: str, value) -> None:
        self.props.setdefault(prop, []).append(value)

    def values(self, prop: str) -> list:
        return self.props.get(prop, [])

    def has(self, prop: str) -> bool:
        """At least one value, not an empty text."""
        return any(not (isinstance(v, Lit) and (v.value is None or (isinstance(v.value, str) and not v.value.strip())))
                   for v in self.values(prop))

    def label(self) -> str:
        t = "/".join(self.types) or "(sin tipo)"
        return f"{t} {self.id or ''} [{self.syntax} {self.where}]".replace("  ", " ")

    def text(self) -> str:
        return self.label()


def is_type(entity, cls: str, voc=None) -> bool:
    """`entity` is of `cls` or a subtype, minus the subtypes with their own rules."""
    if not isinstance(entity, Entity):
        return False
    voc = voc or vocab.load()
    excluded = OWN_RULES.get(cls, ())
    for t in entity.types:
        if voc.is_a(t, cls) and not any(voc.is_a(t, x) for x in excluded):
            return True
    return False


def is_valued(entity, voc=None) -> bool:
    """Valued entity of the review snippet guide (method common, point 3), ProductGroup and
    OnlineStore included."""
    voc = voc or vocab.load()
    return isinstance(entity, Entity) and any(voc.is_a(t, v) for t in entity.types for v in VALUED)


def fingerprint(value, depth: int = 0) -> tuple:
    """What a value says, regardless of where it is written: a literal by its text, an entity
    with identifier by it, an anonymous entity by its types and values."""
    if isinstance(value, Lit):
        return ("lit", value.text())
    if isinstance(value, Ref):
        return ("id", value.id)
    if value.id is not None or depth > 6:
        return ("id", value.id or id(value))
    return ("node", tuple(sorted(value.types)),
            tuple(sorted((p, tuple(sorted(fingerprint(v, depth + 1) for v in vs))) for p, vs in value.props.items())))


class Graph:
    """All the entities of a page (or of a site, for the general view)."""

    def __init__(self, entities: list[Entity]) -> None:
        self.entities = entities

    @classmethod
    def link(cls, nodes: list[Entity]) -> "Graph":
        """One entity per identifier (types and values merged) and every reference resolved to
        it when the page defines it: a node with types or values other than its identifier."""
        by_id: dict[str, Entity] = {}
        merged: dict[int, Entity] = {}
        for node in nodes:
            if node.id is None:
                continue
            defined = bool(node.types or node.props)
            first = by_id.get(node.id)
            if first is None:
                if defined:
                    by_id[node.id] = node
                continue
            if defined:
                for t in node.types:
                    if t not in first.types:
                        first.types.append(t)
                for prop, values in node.props.items():
                    mine = first.props.setdefault(prop, [])
                    known = {fingerprint(v) for v in mine}
                    for v in values:
                        if fingerprint(v) not in known:  # the same triple, or the same anonymous node seen again
                            known.add(fingerprint(v))
                            mine.append(v)
                first.top = first.top or node.top
                first.places.append(node.where)
                merged[id(node)] = first
        out = []
        seen = set()
        for node in nodes:
            canon = merged.get(id(node), node)
            if node.id is not None and not (node.types or node.props) and node.id in by_id:
                continue  # a bare reference node, not an entity of its own
            if id(canon) not in seen:
                seen.add(id(canon))
                out.append(canon)
        for entity in out:
            for prop, values in entity.props.items():
                for i, v in enumerate(values):
                    if isinstance(v, Ref) and v.id in by_id:
                        values[i] = by_id[v.id]
                    elif isinstance(v, Entity) and id(v) in merged:
                        values[i] = merged[id(v)]
                    elif isinstance(v, Entity) and v.id is not None and not (v.types or v.props):
                        values[i] = by_id.get(v.id) or Ref(v.id, v.where)
        for entity in out:
            entity.parents = []
        for entity in out:
            for prop, values in entity.props.items():
                for v in values:
                    if isinstance(v, Entity):
                        v.parents.append((entity, prop))
        return cls(out)

    def of(self, cls: str) -> list[Entity]:
        return [e for e in self.entities if is_type(e, cls)]

    def top_of(self, cls: str) -> list[Entity]:
        """Top level entities of `cls`: not the nested value of another property; a top node of a
        block or of a @graph counts even if another node references it by identifier."""
        return [e for e in self.of(cls) if e.top]

    def valued(self) -> list[Entity]:
        return [e for e in self.entities if is_valued(e)]
