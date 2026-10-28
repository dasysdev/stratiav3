"""Versions cited by the catalog against the pinned ones in references (T-061)."""
from demand_engine.demand import citations
from demand_engine.demand.citations import check, tags
from references.store import RefsError

REGISTRY = {
    "shopify": {"kind": "shopify-taxonomy", "uses": ["demand-engine"]},
    "amazon-ptd": {"kind": "amazon-ptd", "uses": ["demand-engine"]},
    "guide": {"kind": "document", "uses": ["web-audit", "demand-engine"]},
    "schemaorg": {"kind": "schemaorg", "uses": ["web-audit"]},
}
PINNED = {"shopify": "v2026-08", "amazon-ptd": "2026-10-24", "guide": "2026-10-27", "schemaorg": "30.1"}
BLOCK = {"id": "cat.sabanas", "refs": ["shopify:hg-15@v2026-08", "amazon-ptd:SHEET@2026-10-24", "ley:TRLGDCU-97.1@2026-02-28"],
         "requirements": [{"id": "cat.sabanas/01", "sources": ["shopify-attr:fabric", "amazon-ptd-prop:SHEET.color@2026-10-24"],
                           "resolving_info": [{"support": ["amazon-ptd-prop:SHEET.color@2026-10-24"],
                                               "source": "amazon-ptd-prop:SHEET.size"}],
                           "question": "¿De qué tejido es? (no es una cita: question no es un campo de citas)"}]}


def run(*found, resolve=None, monkeypatch=None):
    if monkeypatch:
        monkeypatch.setattr(citations, "property_citation", resolve or (lambda tag: [{}]))
    return check([("cat/x.json", *f) for f in found], REGISTRY, PINNED)


def test_tags_takes_the_citation_fields_with_the_sources_of_their_block():
    found = list(tags({"blocks": [BLOCK], "hints": [{"para": {"fuente": "shopify-attr:color"}, "origen": {"apoyo": ["D-122"]}}]}))
    assert [t for _, t, _ in found] == ["shopify:hg-15@v2026-08", "amazon-ptd:SHEET@2026-10-24", "ley:TRLGDCU-97.1@2026-02-28",
                                        "shopify-attr:fabric", "amazon-ptd-prop:SHEET.color@2026-10-24",
                                        "amazon-ptd-prop:SHEET.color@2026-10-24", "amazon-ptd-prop:SHEET.size",
                                        "shopify-attr:color"]
    assert found[3][2] == {"shopify", "amazon-ptd", "ley"}    # the sources the block's refs cite with a version
    assert found[-1][2] == frozenset()                         # a hint has no block


def test_the_current_versions_are_clean_and_the_rest_is_reported_apart():
    result = check([("cat/x.json", *f) for f in tags(BLOCK)] + [("hints.json", "fuente", "shopify-attr:color", frozenset())],
                   REGISTRY, PINNED)
    assert result == {"errors": [], "unregistered": {"ley": 1}, "by_block": {"shopify-attr": 1, "amazon-ptd-prop": 1},
                      "unversioned": {"shopify-attr": 1}}


def test_a_version_that_is_not_the_pinned_one_is_an_error():
    result = run(("support", "amazon-ptd-prop:SHEET.color@2026-09-01", frozenset()), ("refs", "shopify:hg@v2026-02", frozenset()))
    assert result["errors"] == [
        "cat/x.json (support) amazon-ptd-prop:SHEET.color@2026-09-01: la versión fijada de amazon-ptd es 2026-10-24",
        "cat/x.json (refs) shopify:hg@v2026-02: la versión fijada de shopify es v2026-08"]


def test_a_source_that_demand_engine_does_not_use_is_an_error():
    assert run(("sources", "schemaorg:schema:gtin@30.1", frozenset()))["errors"] == [
        "cat/x.json (sources) schemaorg:schema:gtin@30.1: schemaorg no tiene demand-engine en uses (references/sources.json)"]


def test_a_property_of_a_document_must_exist_in_its_version(monkeypatch):
    def resolve(tag):
        if "nope" in tag:
            raise RefsError(f"{tag}: guide 2026-10-27 no tiene la propiedad nope de Product")
        return [{}]
    result = run(("sources", "guide:Product.audience@2026-10-27", frozenset()),
                 ("sources", "guide:Product.nope@2026-10-27", frozenset()), resolve=resolve, monkeypatch=monkeypatch)
    assert result["errors"] == ["cat/x.json (sources): guide:Product.nope@2026-10-27: guide 2026-10-27 no tiene la propiedad nope de Product"]
    assert run(("sources", "guide:Product.audience@2026-11-02", frozenset()), monkeypatch=monkeypatch)["errors"] == [
        "cat/x.json (sources) guide:Product.audience@2026-11-02: la versión fijada de guide es 2026-10-27"]


def test_a_citation_of_a_law_names_its_source_by_the_code_and_must_resolve(monkeypatch):
    registry = {**REGISTRY, "es-trlgdcu": {"kind": "law", "cite": "TRLGDCU", "uses": ["demand-engine"]}}
    pinned = {**PINNED, "es-trlgdcu": "2026-02-28"}

    def resolve(tag, codes):
        if "97.9" in tag:
            raise RefsError(f"{tag}: es-trlgdcu 2026-02-28: el artículo 97 no tiene 9")
        return {}
    monkeypatch.setattr(citations, "law_citation", resolve)
    found = [("cat/x.json", "sources", "ley:TRLGDCU-97.1.e@2026-02-28", frozenset()),
             ("cat/x.json", "sources", "ley:TRLGDCU-97.9@2026-02-28", frozenset()),
             ("cat/x.json", "support", "ley:TRLGDCU-97.1.e@2007-11-30", frozenset()),
             ("hints.json", "apoyo", "ley:TRLGDCU-97.1.e", frozenset({"es-trlgdcu"})),
             ("cat/x.json", "sources", "ley:LOCM-20.1@2022-03-30", frozenset())]
    result = check(found, registry, pinned)
    assert result["errors"] == [
        "cat/x.json (sources): ley:TRLGDCU-97.9@2026-02-28: es-trlgdcu 2026-02-28: el artículo 97 no tiene 9",
        "cat/x.json (support) ley:TRLGDCU-97.1.e@2007-11-30: la versión fijada de es-trlgdcu es 2026-02-28"]
    assert result["by_block"] == {"ley": 1} and result["unregistered"] == {"ley": 1}
    block = {"refs": ["ley:TRLGDCU-97.1@2026-02-28"], "sources": ["ley:TRLGDCU-97.1.e"]}
    assert [b for _, _, b in tags(block, laws={"TRLGDCU": "es-trlgdcu"})] == [{"es-trlgdcu"}] * 2
