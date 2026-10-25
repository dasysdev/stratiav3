"""A tiny frozen reference tree (pinned versions of every source) in a temporary directory."""
import gzip
import json

import pytest

from demand_engine import refs

G = "gid://shopify/TaxonomyCategory/"
CACHED = (refs.shopify_categories, refs.shopify_attributes, refs.google_mapping, refs.google_names)


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
    monkeypatch.setattr(refs, "REFS", root)
    monkeypatch.setattr(refs, "PINS", root / "pins.json")
    for fn in CACHED:
        fn.cache_clear()
    yield root
    for fn in CACHED:
        fn.cache_clear()
