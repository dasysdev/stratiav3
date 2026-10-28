"""An empty references directory (REFS_DIR) with a test registry (SOURCES_FILE), and a fake web."""
import json

import pytest

from references import net, read
from references.kinds import document

SYSTEMS = {"demand-engine": {"review": "entrenamiento"}, "web-audit": {"review": "web-audit/bin/reqs check"}}
SOURCES = [
    {"id": "shopify", "kind": "shopify-taxonomy", "title": "Taxonomy", "url": "https://github.com/s", "uses": ["demand-engine"]},
    {"id": "shopify-google", "kind": "shopify-google", "title": "Mapping", "url": "https://github.com/s", "uses": ["demand-engine"]},
    {"id": "google", "kind": "google-taxonomy", "title": "Google", "url": "https://example.org/taxonomy.txt", "uses": ["demand-engine"]},
    {"id": "amazon-btg", "kind": "amazon-browse-tree", "title": "Browse tree", "url": "https://example.org/btg", "uses": ["demand-engine"]},
    {"id": "amazon-ptd", "kind": "amazon-ptd", "title": "PTD", "url": "https://example.org/ptd", "uses": ["demand-engine"]},
    {"id": "schemaorg", "kind": "schemaorg", "title": "Vocabulary", "url": "https://github.com/x", "uses": ["web-audit"]},
    {"id": "guide", "kind": "document", "title": "Guide", "url": "https://example.org/guide",
     "uses": ["web-audit", "demand-engine"]},
    {"id": "spec-pdf", "kind": "document", "title": "Spec", "url": "https://example.org/spec/", "uses": ["web-audit"]},
    {"id": "es-trlgdcu", "kind": "law", "title": "TRLGDCU", "url": "https://www.boe.es/x", "uses": ["demand-engine"],
     "cite": "TRLGDCU", "boe": "BOE-A-2007-20555"},
    {"id": "eu-reg-1007-2011", "kind": "law", "title": "Textiles", "url": "https://eur-lex.europa.eu/x",
     "uses": ["demand-engine"], "cite": "UE-1007/2011", "celex": "32011R1007"},
    {"id": "iso-4217", "kind": "document", "title": "ISO 4217", "url": "https://example.org/list-one.xml", "uses": ["web-audit"]},
    {"id": "iso-3166-1", "kind": "eu-authority", "title": "Country", "url": "https://op.europa.eu/x", "uses": ["web-audit"],
     "authority": "country", "file": "countries-skos.rdf"},
]
CACHED = (read.shopify_categories, read.shopify_attributes, read.google_mapping, read.google_names, read.vocabulary,
          read._properties, read.currency_codes, read.country_codes)


@pytest.fixture
def refs_dir(tmp_path, monkeypatch):
    root = tmp_path / "refs"
    monkeypatch.setenv("REFS_DIR", str(root))
    monkeypatch.setenv("SOURCES_FILE", str(tmp_path / "sources.json"))
    (tmp_path / "sources.json").write_text(json.dumps({"systems": SYSTEMS, "sources": SOURCES}), encoding="utf-8")
    for fn in CACHED:
        fn.cache_clear()
    yield root
    for fn in CACHED:
        fn.cache_clear()


@pytest.fixture
def web(refs_dir, monkeypatch):
    """url → (body, headers): what net.download answers."""
    pages = {}
    monkeypatch.setattr(net, "download", lambda url, headers=None: (*pages[url], url))
    monkeypatch.setattr(document, "INTERVAL", 0)
    monkeypatch.setattr("references.cli.INTERVAL", 0)
    return pages
