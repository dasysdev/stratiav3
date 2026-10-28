"""A tiny frozen reference tree (pinned versions of every source of demand-engine) in a temporary
REFS_DIR, with its registry (SOURCES_FILE)."""
import gzip
import json

import pytest

from references import read

G = "gid://shopify/TaxonomyCategory/"
CACHED = (read.shopify_categories, read.shopify_attributes, read.google_mapping, read.google_names)
SOURCES = [{"id": sid, "kind": kind, "title": sid, "url": "https://example.org/" + sid, "uses": ["demand-engine"]}
           for sid, kind in (("shopify", "shopify-taxonomy"), ("shopify-google", "shopify-google"),
                             ("google", "google-taxonomy"), ("amazon-btg", "amazon-browse-tree"),
                             ("amazon-ptd", "amazon-ptd"))]


def write_gz(path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(gzip.compress(json.dumps(obj).encode("utf-8")))


def category(cid, name, full, handles, ancestors=(), children=()):
    return {"id": G + cid, "name": name, "full_name": full, "attributes": [{"handle": h} for h in handles],
            "ancestors": [{"id": G + a} for a in ancestors], "children": [{"id": G + c, "name": c} for c in children],
            "parent_id": G + ancestors[0] if ancestors else None}


@pytest.fixture
def fake_refs(tmp_path, monkeypatch):
    root = tmp_path / "refs"
    # Shopify lists inherited attributes in every category; ancestors go nearest first
    write_gz(root / "shopify/v1/categories.es.json.gz", {"verticals": [{"categories": [
        category("zz", "Hogar", "Hogar", ["color"], children=["zz-1"]),
        category("zz-1", "Ropa de cama", "Hogar > Ropa de cama", ["color", "fabric"], ["zz"], ["zz-1-2"]),
        category("zz-1-2", "Sábanas", "Hogar > Ropa de cama > Sábanas", ["color", "fabric", "bedding-size"],
                 ["zz-1", "zz"]),
    ]}]})
    write_gz(root / "shopify/v1/attributes.es.json.gz", {"attributes": [
        {"id": G + "a1", "handle": "color", "name": "Color", "values": [{"name": "Azul"}, {"name": "Blanco"}]},
        {"id": G + "a2", "handle": "fabric", "name": "Tejido", "values": [{"name": "Franela"}]},
        {"id": G + "a3", "handle": "bedding-size", "name": "Tamaño de cama", "values": [{"name": "90 cm"}]},
    ]})
    write_gz(root / "shopify-google/v1/integrations.google.shopify_x.en.json.gz", {"mappings": [{"rules": [
        {"input": {"category": {"id": G + "zz-1-2", "full_name": "Home > Bedding > Sheets"}},
         "output": {"category": [{"id": "2541", "full_name": "Home > Linens > Sheets"}]}}]}]})
    (root / "google/g1").mkdir(parents=True)
    (root / "google/g1/taxonomy-with-ids.es-ES.txt").write_text(
        "# Google_Product_Taxonomy_Version: 2021-09-21\n2541 - Casa > Ropa de cama > Sábanas\n", encoding="utf-8")
    write_gz(root / "amazon-ptd/p1/schemas/SHEET.schema.json.gz", {"properties": {
        "color": {"title": "Color"},
        "thread_count": {"title": "Número de hilos", "items": {"enum": ["200", "400"]}},
        "brand": {"title": "Marca"},
        "special_feature": {"title": "Característica especial", "items": {"enum": ["Antiarrugas"]}},
        "compliance_fabric": {"title": "Tejido declarado"},
        "fabric_weight": {"title": "Gramaje"},
        "battery": {"title": "Batería"},
    }})
    (root / "amazon-ptd/p1/definitions").mkdir(parents=True)
    (root / "amazon-ptd/p1/definitions/SHEET.json").write_text(json.dumps({"displayName": "Sábana", "propertyGroups": {
        "product_details": {"propertyNames": ["color", "thread_count", "brand", "special_feature"]},
        "safety_and_compliance": {"propertyNames": ["compliance_fabric", "fabric_weight", "battery"]},
    }}), encoding="utf-8")
    (root / "pins.json").write_text(json.dumps({"shopify": "v1", "shopify-google": "v1", "google": "g1",
                                                "amazon-ptd": "p1", "amazon-btg": "b1"}), encoding="utf-8")
    (tmp_path / "sources.json").write_text(json.dumps({"systems": {"demand-engine": {"review": "entrenamiento"}},
                                                      "sources": SOURCES}), encoding="utf-8")
    monkeypatch.setenv("REFS_DIR", str(root))
    monkeypatch.setenv("SOURCES_FILE", str(tmp_path / "sources.json"))
    for fn in CACHED:
        fn.cache_clear()
    yield root
    for fn in CACHED:
        fn.cache_clear()
