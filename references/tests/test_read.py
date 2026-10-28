import gzip
import json

import pytest

from references import ROOT, read, store

G = "gid://shopify/TaxonomyCategory/"


def write_gz(path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(gzip.compress(json.dumps(obj).encode("utf-8")))


def category(cid, name, full, handles, ancestors=()):
    return {"id": G + cid, "name": name, "full_name": full, "attributes": [{"handle": h} for h in handles],
            "parent_id": G + ancestors[0] if ancestors else None}


def freeze(root, source: str, version: str, files: dict) -> None:
    folder = root / source / version
    for name, data in files.items():
        (folder / name).parent.mkdir(parents=True, exist_ok=True)
        (folder / name).write_bytes(data)
    (folder / "MANIFEST.json").write_text(json.dumps({"files": [{"path": n} for n in files]}), encoding="utf-8")


@pytest.fixture
def taxonomy(refs_dir):
    """Pinned versions of the taxonomy sources (a sheet under bedding)."""
    write_gz(refs_dir / "shopify/v1/categories.es.json.gz", {"verticals": [{"categories": [
        category("zz", "Hogar", "Hogar", ["color"]),
        category("zz-1", "Ropa de cama", "Hogar > Ropa de cama", ["color", "fabric"], ["zz"]),
        category("zz-1-2", "Sábanas", "Hogar > Ropa de cama > Sábanas", ["color", "fabric"], ["zz-1", "zz"]),
    ]}]})
    write_gz(refs_dir / "shopify/v1/attributes.es.json.gz", {"attributes": [
        {"id": G + "a1", "handle": "color", "name": "Color"},
        {"id": G + "a2", "handle": "fabric", "name": "Tejido"},
    ]})
    write_gz(refs_dir / "shopify-google/v1/integrations.google.shopify_x.en.json.gz", {"mappings": [{"rules": [
        {"input": {"category": {"id": G + "zz-1-2", "full_name": "Home > Bedding > Sheets"}},
         "output": {"category": [{"id": "2541", "full_name": "Home > Linens > Sheets"}]}}]}]})
    (refs_dir / "google/g1").mkdir(parents=True)
    (refs_dir / "google/g1" / read.GOOGLE_FILE).write_text(
        "# Google_Product_Taxonomy_Version: 2021-09-21\n2541 - Casa > Ropa de cama > Sábanas\n", encoding="utf-8")
    write_gz(refs_dir / "amazon-ptd/p1/schemas/SHEET.schema.json.gz", {"properties": {
        "color": {"title": "Color"},
        "thread_count": {"title": "Número de hilos", "items": {"enum": ["200", "400"]}},
        "size": {"items": {"enum": ["s", "m"], "enumNames": ["Pequeña", "Mediana"]}},
    }})
    (refs_dir / "amazon-ptd/p1/definitions").mkdir(parents=True)
    (refs_dir / "amazon-ptd/p1/definitions/SHEET.json").write_text(json.dumps({"displayName": "Sábana"}), encoding="utf-8")
    (refs_dir / "amazon-btg/b1").mkdir(parents=True)
    store.save_pins({"shopify": "v1", "shopify-google": "v1", "google": "g1", "amazon-ptd": "p1", "amazon-btg": "b1"})
    return refs_dir


def test_taxonomy(taxonomy):
    assert list(read.shopify_categories()) == ["zz", "zz-1", "zz-1-2"]
    assert read.shopify_attributes()["fabric"]["name"] == "Tejido"
    assert read.google_mapping()["zz-1-2"] == ("Home > Bedding > Sheets", [("2541", "Home > Linens > Sheets")])
    assert read.google_names() == {"2541": "Casa > Ropa de cama > Sábanas"}
    assert read.short(G + "zz-1") == "zz-1"
    assert read.browse_tree() == taxonomy / "amazon-btg/b1" / read.BTG_FILE


def test_amazon_ptd(taxonomy):
    props, definition = read.ptd("SHEET")
    assert definition["displayName"] == "Sábana"
    assert read.enum_values(props["thread_count"]) == ["200", "400"]
    assert read.enum_values(props["size"]) == ["Pequeña", "Mediana"]       # display names when present
    with pytest.raises(store.RefsError, match="no existe el PTD NOPE"):
        read.ptd("NOPE")


def test_a_source_not_pinned_is_reported(taxonomy):
    store.save_pins({})
    with pytest.raises(store.RefsError, match="shopify no está fijada"):
        read.shopify_categories()


TEXT = """# Merchant listing {#top}

## Structured data type definitions {#definitions}

You must include the required properties to be eligible.

### Product {#product-properties}

| Required properties |
| offers | Offer A nested Offer to sell the product. |

```
# not a heading
```

#### Identifiers

We recommend that the sku value only contain ASCII characters.

## Examples {#examples}

### Example

First.

### Example

An example.
"""

VOCABULARY = {"@context": {}, "@graph": [
    {"@id": "schema:gtin", "@type": "rdf:Property",
     "rdfs:comment": "A Global Trade Item Number.\n\nA correct [[gtin]] value should be a valid GTIN."},
    {"@id": "schema:name", "rdfs:comment": [{"@value": "The name"}, "of the item."]},
]}


@pytest.fixture
def documents(refs_dir):
    freeze(refs_dir, "guide", "2026-10-27", {"page.html": b"<html></html>", "text.md": TEXT.encode()})
    freeze(refs_dir, "schemaorg", "30.1", {read.VOCABULARY: json.dumps(VOCABULARY).encode()})
    freeze(refs_dir, "spec-pdf", "2026-10-27", {"document.pdf": b"%PDF-1.4"})
    store.save_pins({"guide": "2026-10-27", "schemaorg": "30.1", "spec-pdf": "2026-10-27"})
    return refs_dir


def test_sections_of_a_document(documents):
    assert [h[2:] for h in read.headings(TEXT)][:3] == [
        ("Merchant listing", "top"), ("Structured data type definitions", "definitions"), ("Product", "product-properties")]
    section = read.section_text("guide", "document", "#product-properties")
    assert section.startswith("### Product") and "We recommend" in section     # with its subsections
    assert "## Examples" not in section and "# not a heading" in section        # code is no heading
    assert read.section_text("guide", "document", "#examples").endswith("An example.")
    assert read.section_text("guide", "document", "Identifiers").startswith("#### Identifiers\n")
    with pytest.raises(store.RefsError, match="hay 2 encabezados «Example»"):
        read.section_text("guide", "document", "Example")
    with pytest.raises(store.RefsError, match="no existe la sección #nope"):
        read.section_text("guide", "document", "#nope")
    with pytest.raises(store.RefsError, match="no tiene texto citable"):
        read.section_text("spec-pdf", "document", "#x")


def test_terms_of_a_vocabulary(documents):
    assert read.section_text("schemaorg", "schemaorg", "schema:gtin").endswith("should be a valid GTIN.")
    assert read.vocabulary(documents / "schemaorg/30.1" / read.VOCABULARY)["schema:name"] == "The name of the item."
    with pytest.raises(store.RefsError, match="no existe el término schema:nope"):
        read.section_text("schemaorg", "schemaorg", "schema:nope")


# --- Property tables ------------------------------------------------------------

PROPERTIES = """# Merchant shipping policy (ShippingService) structured data {#top}

## How to add structured data {#add-structured-data}

| Required properties |
| outside | Text Not in the type definitions. |

## Structured data type definitions {#structured-data-type-definitions}

| Recommended properties |
| name | Text A unique name for your shipping service. |

### Product information {#product-information}

#### Product {#product-properties}

| Required properties |
| price or priceSpecification.price | Number The current price. |
| Recommended properties |
| gtin | gtin8 | isbn | Text Include all applicable global identifiers. |
| suggestedMaxAge (or suggestedAge.maxValue) | Number The suggested maximum age. |
| itemReviewed (if review is not a Nested Review) | One of the valid types The item. |
| Choose either addressRegion or postalCode | Identifies the region. |

#### Certification {#certification-properties}

| Required properties |
| issuedBy | Organization The certification body. |
name
Text

The name of the certification.
| Recommended properties |
| certificationRating | Rating The value of the certification. |

#### QuantitativeValue (for unit pricing) {#unit-pricing}

| Required properties |
| unitCode | Text or URL The unit of measurement. |
If both are used, the price specification is ignored.

### MerchantReturnPolicy (nested under Organization using the hasMerchantReturnPolicy property) {#returns}

| Recommended properties |
| returnFees | ReturnFeesEnumeration The default type of return fee. |

#### Finite or unlimited return windows {#windows}

| Required properties (choose the option that best suits your use case) |
| Option A |
| merchantReturnDays | Integer The number of days. |
| Option B |
| merchantReturnLink | URL Specify the URL. |

#### QuantitativeValue (for shipping times) {#shipping-times}

| Required properties |
| unitCode | Text The units. |

## Troubleshooting {#troubleshooting}

| Required properties |
| after | Text Not in the type definitions. |
"""


def row(rows, owner, prop, heading=None):
    found = [r for r in rows if r["type"] == owner and r["property"] == prop and heading in (None, r["heading"])]
    assert len(found) == 1, (owner, prop, found)
    return found[0]


def test_property_rows():
    rows = read.property_rows(PROPERTIES)
    assert {r["property"] for r in rows} >= {"name", "price", "gtin"} and not {"outside", "after"} & {r["property"] for r in rows}
    name = row(rows, "ShippingService", "name")                          # the single type of the H1
    assert (name["table"], name["heading"], name["expects"]) == ("recommended", "#structured-data-type-definitions", "Text")
    price = row(rows, "Product", "price")
    assert (price["names"], price["table"], price["expects"]) == (["price", "priceSpecification.price"], "required", "Number")
    assert row(rows, "Product", "gtin")["names"] == ["gtin", "gtin8", "isbn"]
    assert row(rows, "Product", "gtin")["text"] == "Text Include all applicable global identifiers."
    assert row(rows, "Product", "suggestedMaxAge")["names"] == ["suggestedMaxAge", "suggestedAge.maxValue"]
    assert row(rows, "Product", "itemReviewed")["expects"] is None
    assert row(rows, "Product", None)["label"] == "Choose either addressRegion or postalCode"   # prose: no names
    assert row(rows, "Certification", "name")["text"] == "Text The name of the certification."  # row without <tr>
    assert row(rows, "Certification", "name")["table"] == "required"
    assert row(rows, "Certification", "certificationRating")["table"] == "recommended"
    assert row(rows, "QuantitativeValue", "unitCode", "#unit-pricing")["expects"] == "Text or URL"
    returns = row(rows, "MerchantReturnPolicy", "merchantReturnLink")   # no type in the heading: the ancestor's
    assert (returns["table"], returns["group"], returns["heading"]) == ("required", "Option B", "#windows")
    assert row(rows, "MerchantReturnPolicy", "returnFees")["heading"] == "#returns"
    assert read.property_rows("# Guide\n\n| Required properties |\n| name | Text The name. |\n") == []


@pytest.fixture
def tables(refs_dir):
    freeze(refs_dir, "guide", "2026-10-27", {"page.html": b"", "text.md": PROPERTIES.encode()})
    freeze(refs_dir, "guide", "2026-11-02", {"page.html": b"", "text.md": PROPERTIES.replace("certificationRating", "rating").encode()})
    freeze(refs_dir, "spec-pdf", "2026-10-27", {"document.pdf": b"%PDF-1.4"})
    store.save_pins({"guide": "2026-10-27", "spec-pdf": "2026-10-27"})
    return refs_dir


def test_properties_of_the_pinned_version(tables):
    rows = read.properties("guide")
    assert {(r["source"], r["version"]) for r in rows} == {("guide", "2026-10-27")}
    assert "certificationRating" in {r["property"] for r in rows}
    assert "rating" in {r["property"] for r in read.properties("guide", "2026-11-02")}
    with pytest.raises(store.RefsError, match="guide: no existe la versión 2020-01-01"):
        read.properties("guide", "2020-01-01")
    with pytest.raises(store.RefsError, match="no es una página con text.md"):
        read.properties("spec-pdf")


def test_property_citation(tables):
    [found] = read.property_citation("guide:Certification.certificationRating@2026-10-27")
    assert (found["table"], found["version"]) == ("recommended", "2026-10-27")
    assert read.property_citation("guide:Product.gtin8@2026-10-27")[0]["property"] == "gtin"   # any name of the row
    assert len(read.property_citation("guide:QuantitativeValue.unitCode@2026-10-27")) == 2     # two tables of the type
    with pytest.raises(store.RefsError, match="2026-11-02 no tiene la propiedad certificationRating de Certification"):
        read.property_citation("guide:Certification.certificationRating@2026-11-02")
    with pytest.raises(store.RefsError, match="no existe la versión 2020-01-01"):
        read.property_citation("guide:Product.price@2020-01-01")
    with pytest.raises(store.RefsError, match="ha de ser fuente:Tipo.propiedad@versión"):
        read.property_citation("guide:price@2026-10-27")


FROZEN = ROOT / "var"


@pytest.mark.parametrize("source, count, required", [
    ("google-search-merchant-listing", 75, 25), ("google-search-organization", 30, 0),
    ("google-search-product-snippet", 21, 9), ("google-search-product-variants", 11, 1),
    ("google-search-return-policy", 23, 5), ("google-search-review-snippet", 15, 10),
    ("google-search-shipping-policy", 44, 8), ("google-search-javascript", 0, 0)])
def test_frozen_google_search_tables(source, count, required):
    """The tables of the frozen text.md (version 2026-10-27, which never changes)."""
    path = FROZEN / source / "2026-10-27/text.md"
    if not path.exists():
        pytest.skip(f"sin {path}")
    rows = read.property_rows(path.read_text(encoding="utf-8"))
    assert (len(rows), sum(r["table"] == "required" for r in rows)) == (count, required)
    assert all(r["type"] and r["table"] for r in rows)
    if source == "google-search-merchant-listing":
        audience = row(rows, "Product", "audience")
        assert (audience["table"], audience["expects"]) == ("recommended", "PeopleAudience")
        assert row(rows, "Certification", "name")["table"] == "required"
