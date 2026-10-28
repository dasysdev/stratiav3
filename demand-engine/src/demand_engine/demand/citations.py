"""Versions cited by the catalog (T-061): every citation source:…@version of the catalog against the version pinned
in references (D-149). A pin changed by another system (refs pin) leaves the citations of demand-engine on the
previous version: they are listed here for review, with the source's changes in «refs diff».

Citations live in the block refs, the requirement sources, the support and source of the resolving information and
the hints by source and their support («fuente», «apoyo»). A tag names a source by its id or by a part of it
(amazon-ptd-prop: a property of a PTD; shopify-attr: a Shopify attribute); a citation of a law, by its code
(ley:TRLGDCU-97.1.e@2026-02-28 names the law whose «cite» is TRLGDCU). A citation of a property table of a document
(google-search-merchant-listing:Product.audience@2026-10-27) must also exist in that version, and the article and
apartado a citation of a law names, in its version (T-062).

Reported apart, without error: citations to sources without a registry and citations without a version. Most
attributes and properties carry none: the version is that of the source in the refs of their block.
"""
import re
import sys

from references.read import LAW, law_citation, law_codes, law_reference, property_citation
from references.store import RefsError, pins, sources

from .catalog import CATALOG, read_json

SYSTEM = "demand-engine"
FIELDS = ("refs", "sources", "support", "source", "fuente", "apoyo")
PARTS = {"amazon-ptd-prop": "amazon-ptd", "shopify-attr": "shopify"}   # tags that name a part of a source
TAG = re.compile(r"^([a-z][a-z0-9]*(?:-[a-z0-9]+)*):(.+)$")


def source_of(tag: str, laws: dict) -> str:
    """The source a tag names; the prefix itself for a law without a registry (`laws`: code → source)."""
    prefix = TAG.match(tag)[1]
    if prefix == LAW:
        found = law_reference(tag, laws)
        return found[0] if found else LAW
    return PARTS.get(prefix, prefix)


def tags(node, field=None, block=frozenset(), laws=None):
    """(field, tag, block) of each citation in a JSON node: strings with a prefix in one of FIELDS. `block` holds the
    sources that the refs of the nearest enclosing block cite with a version."""
    laws = laws or {}
    if isinstance(node, dict):
        if isinstance(node.get("refs"), list):
            block = frozenset(source_of(t, laws) for t in node["refs"] if isinstance(t, str) and TAG.match(t) and "@" in t)
        for k, v in node.items():
            yield from tags(v, k, block, laws)
    elif isinstance(node, list):
        for v in node:
            yield from tags(v, field, block, laws)
    elif isinstance(node, str) and field in FIELDS and TAG.match(node):
        yield field, node, block


def catalog_citations() -> list:
    """(file, field, tag, block) of every citation of the catalog."""
    laws = law_codes()
    return [(str(path.relative_to(CATALOG)), *found) for path in sorted(CATALOG.rglob("*.json"))
            for found in tags(read_json(path), laws=laws)]


def check(citations: list, registry: dict, pinned: dict) -> dict:
    """Problems (a version that is not the pinned one, a source that demand-engine does not use, a property that the
    document does not have, a passage that the law does not have) and what is reported apart, by prefix: citations to unregistered sources, without a
    version of their own but with that of their block, and without any."""
    out = {"errors": [], "unregistered": {}, "by_block": {}, "unversioned": {}}
    laws = law_codes(registry)
    for where, field, tag, block in citations:
        prefix, body = TAG.match(tag).groups()
        source = source_of(tag, laws)
        apart = ("unregistered" if source not in registry else None if "@" in body
                 else "by_block" if source in block else "unversioned")
        if apart:
            out[apart][prefix] = out[apart].get(prefix, 0) + 1
            continue
        version = body.rsplit("@", 1)[1]
        at = f"{where} ({field}) {tag}"
        if SYSTEM not in registry[source]["uses"]:
            out["errors"].append(f"{at}: {source} no tiene {SYSTEM} en uses (references/sources.json)")
        elif version != pinned.get(source):
            out["errors"].append(f"{at}: la versión fijada de {source} es {pinned.get(source, 'ninguna')}")
        else:
            try:
                if registry[source]["kind"] == "law":
                    law_citation(tag, laws)
                elif registry[source]["kind"] == "document" and source == prefix:
                    property_citation(tag)
            except RefsError as e:
                out["errors"].append(f"{where} ({field}): {e}")
    return out


def cmd_check() -> None:
    citations = catalog_citations()
    result = check(citations, sources(), pins())
    apart = lambda counts: ", ".join(f"{p}: {n}" for p, n in sorted(counts.items())) or "ninguna"
    print(f"citas del catálogo: {len(citations)}; {len(result['errors'])} errores")
    for line in result["errors"]:
        print(f"  ERROR {line}")
    print(f"  sin registro en references: {apart(result['unregistered'])}")
    print(f"  sin versión propia, con la de refs de su bloque: {apart(result['by_block'])}")
    print(f"  sin versión: {apart(result['unversioned'])}")
    if result["errors"]:
        sys.exit(1)
