"""One demand model and one sheet per scope (D-155, D-220); the recommended properties of Google Search as support (D-145)."""
import json

from demand_engine.demand import scopes
from demand_engine.demand.scopes import (NO_DESCRIPTION, NO_MARK, NO_RESOLVING, attribute_support, components, compose,
                                         exception, google_problems, handles, localization, profile, sheet_problems)

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
SHEET = {"id": "markup", "scope": "Marcado", "version": "0.2",
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


def loc(unit: dict) -> list:
    return unit["profile"]["expresiones_ejemplo"]


def test_a_category_requirement_is_supported_through_the_shopify_attributes_it_cites():
    assert handles(["shopify-attr:color=Rojo@v2026-08", "shopify-attr:fabric", "amazon-ptd-prop:BOOT.color"]) == {"color", "fabric"}
    assert attribute_support(["shopify-attr:color=Negro"], GOOGLE) == [COLOR]
    assert attribute_support(["shopify-attr:outsole-material"], GOOGLE) == [MATERIAL]   # a pattern covers the parts
    assert attribute_support(["shopify-attr:material-firmness", "amazon-ptd-prop:BOOT.color"], GOOGLE) == []


def test_every_requirement_is_pertinent_and_the_localization_comes_from_the_catalog_and_the_sheet():
    composed = compose(MODEL, SHEET, GEN, GOOGLE)
    assert composed["sheet"] == "markup@0.2" and composed["scope"] == "Marcado"
    units = {u["id"]: u for u in composed["units"]}
    assert set(units) == {"gen/02", "gen/10", "cat.botas/01", "cat.botas/02", "cat.botas/03"}   # what does not apply is out
    assert all(u["pertinent"] for u in units.values())
    assert loc(units["gen/02"]) == [{"source": BRAND, "contribution": "marca del producto"},
                                     {"source": NAME, "contribution": "marca del producto"}]
    assert loc(units["cat.botas/01"]) == [{"source": COLOR, "contribution": None}]
    assert loc(units["gen/10"]) == loc(units["cat.botas/03"]) == []   # no property is not a reason for NA


def test_the_content_sheet_does_not_take_the_localization_of_markup():
    content = {"id": "content", "scope": "Contenido", "version": "0.2", "pertinence": {"exceptions": []},
               "localization": {"note": "Sin localización (D-220)."}}
    composed = compose(MODEL, content, GEN, GOOGLE)
    assert composed["sheet"] == "content@0.2" and composed["scope"] == "Contenido"
    assert all(u["pertinent"] and loc(u) == [] for u in composed["units"])
    including = {**content, "localization": {"include": ["markup"]}}   # a sheet never takes another's (D-220)
    assert all(loc(u) == [] for u in compose(MODEL, including, GEN, GOOGLE)["units"])
    assert sheet_problems(including, GEN) == ["content: la localización incluye otra ficha; un ámbito no usa la de otro (D-220)"]


def test_the_catalog_has_the_sheets_of_content_and_markup_and_scope_writes_one_file_each(tmp_path, monkeypatch):
    assert scopes.scope_names() == ["content", "markup"]
    content, markup = scopes.load_sheet("content"), scopes.load_sheet("markup")
    assert (content["scope"], markup["scope"]) == ("Contenido", "Marcado")
    assert set(content["localization"]) == {"note"} and markup["localization"]["properties"]
    monkeypatch.setattr("demand_engine.demand.catalog.load_gen", lambda: GEN)
    monkeypatch.setattr(scopes, "load_google", lambda: GOOGLE)
    path = tmp_path / "bota.model.json"
    path.write_text(json.dumps(MODEL), encoding="utf-8")
    scopes.cmd_scope(path, [])
    assert sorted(p.name for p in tmp_path.iterdir()) == [
        "bota.content.json", "bota.content.md", "bota.markup.json", "bota.markup.md", "bota.model.json"]
    assert json.loads((tmp_path / "bota.content.json").read_text(encoding="utf-8"))["sheet"] == "content@0.2"


def test_an_exception_is_a_rule_by_entity_or_by_component_with_its_reason():
    rules = [{"entity": "vendedor", "reason": "La función del ámbito no incluye al vendedor (hipotético)."},
             {"component": "medios de pago", "reason": "Hipotético."}]
    assert exception({"entity": "vendedor"}, rules) == rules[0]
    assert exception(MODEL["general"][0]["requirements"][1], rules) == rules[1]
    assert exception(MODEL["general"][0]["requirements"][0], rules) is None
    sheet = {**SHEET, "pertinence": {"exceptions": rules}}
    units = {u["id"]: u for u in compose(MODEL, sheet, GEN, GOOGLE)["units"]}
    assert not units["gen/10"]["pertinent"] and units["gen/10"]["na_reason"] == "Hipotético." and loc(units["gen/10"]) == []


def test_the_profile_takes_components_description_and_hints_from_the_model():
    hint = {"id": "PV-1", "pista": "Suma 100 %.", "propiedad": ["P14"], "ac": ["Fiabilidad"], "origen": {"tipo": "marco"}}
    r = {"id": "gen/25", "description": "A qué zonas envía. Lo responde la tarifa. No lo responde gen/05.", "hints": [hint],
         "comparison": {"mark": "sí", "reason": "Cambia de una oferta a otra."},
         "resolving_info": [{"contribution": "tarifa por zona", "component": "coste", "origin": "marco"},
                            {"contribution": "zonas de envío", "component": "zonas", "origin": "marco"},
                            {"contribution": "envío gratis desde un importe", "component": "coste", "origin": "inferida",
                             "status": "provisional"}]}
    p = profile(r, [{"source": ORIGIN, "contribution": "zonas de envío"}])
    assert p["objeto"] == p["alcance"] == p["casos_frontera"] == r["description"]   # the whole text, not cut (D-177)
    assert p["componentes_respuesta"] == [
        {"componente": "coste", "aportaciones": [{"aportacion": "tarifa por zona", "origen": "marco"},
                                                 {"aportacion": "envío gratis desde un importe", "origen": "inferida",
                                                  "estado": "provisional"}]},
        {"componente": "zonas", "aportaciones": [{"aportacion": "zonas de envío", "origen": "marco"}]}]
    assert p["pistas_valoracion"] == [hint] and p["expresiones_ejemplo"] == [{"source": ORIGIN, "contribution": "zonas de envío"}]
    assert p["pendientes_de_definicion"] == []
    assert components([]) == []


def test_what_the_model_lacks_is_pointed_out_and_not_filled_in():
    units = {u["id"]: u for u in compose(MODEL, SHEET, GEN, GOOGLE)["units"]}
    assert units["gen/02"]["profile"]["pendientes_de_definicion"] == [NO_DESCRIPTION, NO_MARK]
    bare = units["cat.botas/01"]["profile"]
    assert bare["pendientes_de_definicion"] == [NO_RESOLVING, NO_DESCRIPTION, NO_MARK]
    assert bare["objeto"] is bare["alcance"] is bare["casos_frontera"] is None and bare["componentes_respuesta"] == []


def test_each_unit_carries_the_comparison_mark_of_the_model_without_deciding_it():
    """D-126: the mark is the model's; scope passes it to the unit, NA or not, and never gives a default (D-139)."""
    no = {"mark": "no", "case": "c", "reason": "Identifica la oferta."}
    paa = {"id": "paa/N1/botas", "question": "¿Para qué temporada es?", "entity": "producto", "sources": [],
           "comparison": {"mark": "sí", "reason": "Cambia.", "origin": "paa", "status": "no compilado"}, "block": "cat.botas"}
    marked = {**MODEL, "blocks": [{**MODEL["blocks"][0], "requirements": [
        {**MODEL["blocks"][0]["requirements"][0], "comparison": no}, *MODEL["blocks"][0]["requirements"][1:]]}],
        "paa": {"set": "botas", "requirements": [paa]}}
    sheet = {**SHEET, "pertinence": {"exceptions": [{"entity": "producto", "reason": "Hipotético."}]}}
    units = {u["id"]: u for u in compose(marked, sheet, GEN, GOOGLE)["units"]}
    assert units["cat.botas/01"]["comparison"] == no and not units["cat.botas/01"]["pertinent"]
    assert units["cat.botas/02"]["comparison"] is None and NO_MARK in units["cat.botas/02"]["profile"]["pendientes_de_definicion"]
    assert units["paa/N1/botas"]["block"] == "cat.botas" and units["paa/N1/botas"]["comparison"]["origin"] == "paa"
    text = scopes.render_units(compose(marked, SHEET, GEN, GOOGLE))
    assert "- Marca de comparación (del modelo, D-126): 1 se compara · 1 no se compara · 4 sin marca (pendiente, D-139)" \
        in text.splitlines()


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
        "markup: excepción sin entidad ni componente, o sin fundamento: {'entity': 'vendedor'}",
        "markup: localización desde «otro.json» desconocida",
        f"markup: {NAME} → aportación «nombre» que gen/02 no tiene",
        f"markup: {NAME} → requisito «cat.botas/01» fuera de la capa general"]


def test_the_catalog_is_clean():
    from demand_engine.demand.catalog import load_gen
    assert scopes.catalog_problems(load_gen()) == []
