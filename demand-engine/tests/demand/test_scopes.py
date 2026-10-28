"""One demand model and one sheet per scope (D-155); the recommended properties of Google Search as support (D-145)."""
from demand_engine.demand import scopes
from demand_engine.demand.scopes import (attribute_support, compose, exception, google_problems, handles, localization,
                                         sheet_problems)

COLOR = "google-search-merchant-listing:Product.color@2026-10-27"
MATERIAL = "google-search-merchant-listing:Product.material@2026-10-27"
BRAND = "google-search-merchant-listing:Product.brand.name@2026-10-27"
NAME = "google-search-merchant-listing:Product.name@2026-10-27"
ORIGIN = "google-search-shipping-policy:ShippingConditions.shippingOrigin@2026-10-27"
GOOGLE = {"version": "0.1",
          "retired": {"requirements": [{"id": "ws-consumer/015", "source": BRAND}, {"id": "ws-consumer/022", "source": COLOR},
                                       {"id": "ws-consumer/272", "source": ORIGIN}]},
          "attributes": [{"source": COLOR, "shopify": ["color"]}, {"source": MATERIAL, "shopify": ["material", "*-material"]}],
          "candidates": [{"question": "¿Desde dónde se envía?", "entity": "entrega", "block": "gen", "status": "propuesto",
                          "sources": [ORIGIN], "rationale": "Ninguna cuestión pregunta por el origen."}]}
GEN = {"blocks": [{"id": "gen", "requirements": [
    {"id": "gen/02", "question": "¿Qué marca es?", "entity": "producto", "sources": ["ley:UE-2023/988-19.a@2026-05-29", BRAND],
     "resolving_info": [{"contribution": "marca del producto", "component": "marca", "support": [BRAND]}]},
    {"id": "gen/10", "question": "¿Qué medios de pago se aceptan?", "entity": "oferta", "sources": [],
     "resolving_info": [{"contribution": "medios de pago aceptados", "component": "medios de pago", "support": []}]}]}]}
SHEET = {"id": "web-schema-org", "scope": "Web Schema.org", "version": "0.1",
         "pertinence": {"default": "pertinente", "exceptions": []},
         "localization": {"from": ["gen.json", "google-search.json"],
                          "properties": [{"source": NAME, "requirement": "gen/02", "contribution": "marca del producto"}]}}
MODEL = {"case": "bota", "key": {"model": ["gen@0.8", "cat.botas@4"]},
         "general": [{"id": "gen", "requirements": [{**r, "applies": True} for r in GEN["blocks"][0]["requirements"]]},
                     {"id": "gen.descuento", "requirements": [{"id": "gen.descuento/01", "applies": False}]}],
         "blocks": [{"id": "cat.botas", "requirements": [
             {"id": "cat.botas/01", "question": "¿De qué color es?", "entity": "producto", "sources": ["shopify-attr:color=Negro"]},
             {"id": "cat.botas/02", "question": "¿De qué es la suela?", "entity": "producto",
              "sources": ["shopify-attr:outsole-material", "amazon-ptd-prop:BOOT.sole_material"]},
             {"id": "cat.botas/03", "question": "¿Qué tipo de bota es?", "entity": "producto", "sources": ["shopify-attr:boot-style"]}]}],
         "inferred": []}


def test_a_category_requirement_is_supported_through_the_shopify_attributes_it_cites():
    assert handles(["shopify-attr:color=Rojo@v2026-08", "shopify-attr:fabric", "amazon-ptd-prop:BOOT.color"]) == {"color", "fabric"}
    assert attribute_support(["shopify-attr:color=Negro"], GOOGLE) == [COLOR]
    assert attribute_support(["shopify-attr:outsole-material"], GOOGLE) == [MATERIAL]   # a pattern covers the parts
    assert attribute_support(["shopify-attr:material-firmness", "amazon-ptd-prop:BOOT.color"], GOOGLE) == []


def test_every_requirement_is_pertinent_and_the_localization_comes_from_the_catalog_and_the_sheet(monkeypatch):
    monkeypatch.setattr(scopes, "load_sheet", lambda scope: SHEET)
    composed = compose(MODEL, SHEET, GEN, GOOGLE)
    assert composed["sheet"] == "web-schema-org@0.1" and composed["scope"] == "Web Schema.org"
    units = {u["id"]: u for u in composed["units"]}
    assert set(units) == {"gen/02", "gen/10", "cat.botas/01", "cat.botas/02", "cat.botas/03"}   # what does not apply is out
    assert all(u["pertinent"] for u in units.values())
    assert units["gen/02"]["localization"] == [{"source": BRAND, "contribution": "marca del producto"},
                                               {"source": NAME, "contribution": "marca del producto"}]
    assert units["cat.botas/01"]["localization"] == [{"source": COLOR, "contribution": None}]
    assert units["gen/10"]["localization"] == units["cat.botas/03"]["localization"] == []   # no property is not a reason for NA


def test_an_including_sheet_takes_the_localization_of_the_included_one(monkeypatch):
    monkeypatch.setattr(scopes, "load_sheet", lambda scope: SHEET)
    web = {"id": "web", "scope": "Web", "version": "0.1", "pertinence": {"exceptions": []},
           "localization": {"include": ["web-schema-org"]}}
    units = {u["id"]: u for u in compose(MODEL, web, GEN, GOOGLE)["units"]}
    assert units["gen/02"]["localization"] and units["cat.botas/01"]["localization"] == [{"source": COLOR, "contribution": None}]


def test_an_exception_is_a_rule_by_entity_or_by_component_with_its_reason():
    rules = [{"entity": "vendedor", "reason": "La función del ámbito no incluye al vendedor (hipotético)."},
             {"component": "medios de pago", "reason": "Hipotético."}]
    assert exception({"entity": "vendedor"}, rules) == rules[0]
    assert exception(MODEL["general"][0]["requirements"][1], rules) == rules[1]
    assert exception(MODEL["general"][0]["requirements"][0], rules) is None
    sheet = {**SHEET, "pertinence": {"exceptions": rules}}
    units = {u["id"]: u for u in compose(MODEL, sheet, GEN, GOOGLE)["units"]}
    assert not units["gen/10"]["pertinent"] and units["gen/10"]["na_reason"] == "Hipotético." and units["gen/10"]["localization"] == []


def test_the_localization_takes_the_google_support_of_each_contribution_only_when_the_sheet_says_so():
    assert localization({"localization": {}}, GEN) == {}
    assert localization(SHEET, GEN)["gen/02"][0] == {"source": BRAND, "contribution": "marca del producto"}


def test_every_retired_property_is_covered_and_the_contract_matches_web_audit():
    retired = [{"id": "ws-consumer/015", "reason": "modelo de demanda"}, {"id": "ws-consumer/022", "reason": "modelo de demanda"},
               {"id": "ws-consumer/272", "reason": "modelo de demanda"}, {"id": "ws-vocabulary/003", "reason": "no se audita"}]
    shopify = {"color": {}, "material": {}}
    assert google_problems(GOOGLE, GEN, shopify, retired) == []
    uncovered = {**GOOGLE, "candidates": []}
    assert google_problems(uncovered, GEN, shopify) == [f"ws-consumer/272 ({ORIGIN}): ni apoyo de la capa general, ni atributo, ni candidato"]
    assert google_problems(GOOGLE, GEN, shopify, retired + [{"id": "ws-consumer/999", "reason": "modelo de demanda"}]) == \
        ["ws-consumer/999: retirado al modelo de demanda en web-audit y fuera del contrato"]
    wrong = {**GOOGLE, "attributes": [{"source": COLOR, "shopify": ["colour"]}],
             "candidates": [{"status": "propuesto", "sources": [ORIGIN], "rationale": "x"}]}
    assert google_problems(wrong, GEN, shopify) == [f"{COLOR}: el atributo de Shopify «colour» no existe",
                                                    f"candidato {[ORIGIN]}: un propuesto necesita pregunta y entidad"]


def test_a_sheet_names_existing_contributions_and_grounds_its_exceptions():
    assert sheet_problems(SHEET, GEN) == []
    bad = {**SHEET, "pertinence": {"exceptions": [{"entity": "vendedor"}]},
           "localization": {"from": ["otro.json"], "properties": [{"source": NAME, "requirement": "gen/02", "contribution": "nombre"},
                                                                  {"source": NAME, "requirement": "cat.botas/01", "contribution": "color"}]}}
    assert sheet_problems(bad, GEN) == [
        "web-schema-org: excepción sin entidad ni componente, o sin fundamento: {'entity': 'vendedor'}",
        "web-schema-org: localización desde «otro.json» desconocida",
        f"web-schema-org: {NAME} → aportación «nombre» que gen/02 no tiene",
        f"web-schema-org: {NAME} → requisito «cat.botas/01» fuera de la capa general"]


def test_the_catalog_is_clean():
    from demand_engine.demand.catalog import load_gen
    assert scopes.catalog_problems(load_gen()) == []
