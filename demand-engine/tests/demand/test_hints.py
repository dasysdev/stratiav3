"""Assessment hints (D-134 to D-140) and the comparison mark (D-139): check and search by tags."""
from demand_engine.demand.hints import check, cites, find

REQS = [
    {"id": "cat.ropa-de-casa/01", "trait": "material", "entity": "producto",
     "sources": ["ley:UE-1007/2011-16.1@2011-10-18", "shopify-attr:fabric"]},
    {"id": "gen/04", "entity": "oferta", "sources": ["ley:TRLGDCU-97.1.e@2026-02-28"],
     "comparison": {"mark": "sí", "reason": "El comprador prefiere menos."}},
    {"id": "gen/12", "entity": "condiciones", "sources": ["ley:TRLGDCU-97.1.n@2026-02-28"],
     "comparison": {"mark": "no", "case": "a", "reason": "La fija la ley."}},
]
VOCABULARY = {"material", "magnitud"}


def hint(n, to=None, prop=("P09",), ac=("Precisión",), origin="marco", **extra):
    """A hint of the catalog (with «para») or, without «to», a requirement's own hint (D-140)."""
    h = {"id": f"PV-{n}", "pista": "Un criterio breve: dice su porqué.", "propiedad": list(prop), "ac": list(ac),
         "origen": {"tipo": origin, "apoyo": []}, **extra}
    return {**h, "para": to} if to is not None else h


def owning(req, *hints):
    return {**req, "hints": list(hints)}


def errors(*hints, reqs=REQS):
    return check({"hints": list(hints)}, reqs, VOCABULARY)[0]


def test_a_source_matches_by_the_beginning_of_the_tag_up_to_a_separator():
    assert cites("ley:UE-1007/2011", "ley:UE-1007/2011-16.1@2011-10-18")
    assert cites("ley:TRLGDCU-97.1", "ley:TRLGDCU-97.1.e@2026-02-28")
    assert not cites("ley:TRLGDCU-97.1", "ley:TRLGDCU-97.10@2026-02-28")
    assert cites("shopify-attr:fabric", "shopify-attr:fabric")
    assert not cites("shopify-attr:fabric", "shopify-attr:fabric-weave")
    assert cites("amazon-ptd-prop:TOWEL.special_feature", "amazon-ptd-prop:TOWEL.special_feature=Ligero")
    assert not cites("amazon-ptd-prop:TOWEL.fabric", "amazon-ptd-prop:TOWEL.fabric_weight")


def test_find_joins_type_source_and_own_hints_without_repeating_and_skips_retired():
    hints = [hint(1, {"rasgo": "material", "entidad": "producto"}), hint(2, {"entidad": "producto"}),
             hint(3, {"fuente": "ley:UE-1007/2011"}), hint(5, {"rasgo": "magnitud"})]
    req = owning(REQS[0], hint(4), hint(6, retirada={"fecha": "2026-10-27", "motivo": "x"}))
    assert [(k, h["id"]) for k, h in find(req, hints)] == [
        ("tipo", "PV-1"), ("tipo", "PV-2"), ("fuente", "PV-3"), ("requisito", "PV-4")]


def test_a_requirement_without_trait_gets_only_entity_hints_by_type():
    hints = [hint(1, {"rasgo": "material", "entidad": "oferta"}), hint(2, {"entidad": "oferta"})]
    assert [h["id"] for _, h in find(REQS[1], hints)] == ["PV-2"]


def test_a_valid_set_has_no_errors():
    reqs = [owning(REQS[1], hint(2, origin="paa")), *REQS[2:]]
    assert errors(hint(1, {"rasgo": "material", "entidad": "producto"}), reqs=[REQS[0], *reqs]) == []


def test_fields_id_origin_and_destination_are_checked():
    found = errors({"id": "PV-1", "pista": "x"}, hint("01", {"entidad": "oferta"}),
                   hint(3, {"rasgo": "magnitud"}), hint(4, {"fuente": "ley:UE-2023/988"}),
                   hint(5, {"rasgo": "sabor"}), hint(6, {"entidad": "oferta"}, origin="inferida", prop=("P10",)),
                   hint(7, {"requisito": "gen/04"}), hint(8, {"entidad": "oferta"}, prop=("P15",)))
    assert any(e.startswith("PV-1: campos que faltan") for e in found)
    assert any(e.startswith("PV-01: id") for e in found)
    assert any(e.startswith("PV-3: su destino no existe") for e in found)
    assert any(e.startswith("PV-4: su destino no existe") for e in found)
    assert any(e.startswith("PV-5: rasgo") for e in found)
    assert any(e.startswith("PV-6: origen") for e in found)
    assert any(e.startswith("PV-7: «para»") for e in found)
    assert any(e.startswith("PV-8: propiedad") for e in found)


def test_own_hints_have_no_para_and_ids_are_unique_across_catalog_and_requirements():
    reqs = [owning(REQS[1], hint(1), hint(2, to={"requisito": "gen/04"})), *REQS[2:]]
    found = errors(hint(1, {"entidad": "oferta"}, prop=("P13",)), reqs=reqs)
    assert "gen/04: PV-1: id repetido" in found
    assert any(e.startswith("gen/04: PV-2: campos") and "que sobran para" in e for e in found)


def test_same_destination_and_same_property_is_an_error_unless_marked_as_doubt():
    a, b = hint(1, {"entidad": "oferta"}, prop=("P09", "P13")), hint(2, {"entidad": "oferta"}, prop=("P13",))
    assert errors(a, b) == ["PV-1 y PV-2: mismo destino y misma propiedad (P13): ¿dicen lo mismo?"]
    assert errors(a, {**b, "duda": "contradice a PV-1"}) == []
    reqs = [owning(REQS[1], hint(3), hint(4)), *REQS[2:]]
    assert errors(reqs=reqs) == ["gen/04: PV-3 y PV-4: mismo destino (el requisito) y misma propiedad (P09): "
                                 "¿dicen lo mismo?"]


def test_a_long_hint_is_rejected():
    assert errors({**hint(1, {"entidad": "oferta"}), "pista": "Una. Dos. Tres."})


def test_comparison_mark_needs_reason_and_case_when_not_compared():
    reqs = [{**REQS[2], "comparison": {"mark": "no", "reason": "La fija la ley."}},
            {**REQS[1], "comparison": {"mark": "sí", "case": "b", "reason": "x"}},
            {**REQS[0], "comparison": {"mark": "quizá", "reason": "x"}}]
    assert len(errors(reqs=reqs)) == 3


def test_warnings_for_overlaps_across_keys_and_comparability_hints_on_a_non_compared_requirement():
    reqs = [REQS[0], REQS[1], owning(REQS[2], hint(2), hint(3, prop=("P13",), ac=("Comparabilidad",)))]
    warnings = check({"hints": [hint(1, {"entidad": "condiciones"})]}, reqs, VOCABULARY)[1]
    assert any("PV-1 y PV-2 le llegan por llaves distintas" in w for w in warnings)
    assert any(w.startswith("gen/12: no se compara") and "PV-3" in w for w in warnings)
