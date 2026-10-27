"""Open trait vocabulary (D-056) and resolving information (D-062 to D-064)."""
from collections import Counter

from demand_engine.demand import resolving
from demand_engine.demand.catalog import requirement_trait
from demand_engine.demand.train import choose_trait, proposed_traits


def test_most_voted_trait_wins_and_a_tie_keeps_the_current_one():
    assert choose_trait(Counter({"sabor": 3, "material": 1}), "material") == "sabor"
    assert choose_trait(Counter({"sabor": 2, "identidad": 2}), "material") == "material"


def test_voted_trait_prevails_over_the_sources():
    r = {"id": "cat.alimentos/06", "trait": "material", "sources": ["shopify-attr:flavor"]}
    assert requirement_trait(r, {"shopify-attr:flavor": "material"}) == ("material", "fuente")
    assert requirement_trait(r, {"shopify-attr:flavor": "material"}, {"cat.alimentos/06": "sabor"}) == ("sabor", "votos")


def test_proposed_traits_need_a_definition():
    models = {"run": {"c1": {"proposed_traits": [{"name": "sabor", "definition": "Sabor o variedad del alimento."},
                                                 {"name": "otro"}]}}}
    found = proposed_traits(models, {})
    assert list(found) == ["sabor"] and found["sabor"]["proposed_by"] == ["c1"]


GEN11 = {"id": "gen/11", "question": "¿Se puede desistir o devolver, en qué condiciones y plazo, con qué coste de "
                                     "devolución, y cuándo no procede?",
         "resolving_info": [{"contribution": "plazo para desistir o devolver", "component": "plazo", "origin": "marco"},
                            {"contribution": "modelo de formulario de desistimiento", "component": "condiciones",
                             "origin": "marco"}]}


def model(url, *contributions):
    return {"url": url, "coverage": {"contributions": [{"answers": "gen/11", **c} for c in contributions]}}


def new(name, component):
    return {"contribution": name, "component": component, "new": True}


def test_a_new_contribution_enters_with_two_different_stores_and_a_component():
    listed = {"contribution": "plazo para desistir o devolver", "component": None, "new": False}
    models = {"a": {"c1": model("https://www.tienda-a.es/p/1", listed, new("remisión a una página de condiciones", "condiciones")),
                    "c2": model("https://tienda-a.es/p/2", new("remisión a la página de condiciones", "condiciones")),
                    "c3": model("https://tienda-b.es/p/3", new("remisión a una página de condiciones", "condiciones"),
                                new("reembolso completo", "condiciones")),
                    "c4": model("https://tienda-c.es/p/4", new("plazo de cambio", None))}}
    result = resolving.induce({"gen/11": GEN11}, models)["gen/11"]
    assert result["observed"] == {"plazo para desistir o devolver": ["tienda-a.es"]}
    assert [a["contribution"] for a in result["accepted"]] == ["remisión a una página de condiciones"]
    assert result["accepted"][0]["stores"] == ["tienda-a.es", "tienda-b.es"]
    assert [a["contribution"] for a in result["proposed"]] == ["reembolso completo"]  # one store: pending
    assert [a["contribution"] for a in result["rejected"]] == ["plazo de cambio"]  # no component of the question
    assert result["never_observed"] == ["modelo de formulario de desistimiento"]  # never withdrawn


def test_two_pages_of_one_store_are_not_enough():
    models = {"a": {"c1": model("https://tienda-a.es/1", new("reembolso completo", "condiciones")),
                    "c2": model("https://www.tienda-a.es/2", new("reembolso completo", "condiciones"))}}
    result = resolving.induce({"gen/11": GEN11}, models)["gen/11"]
    assert not result["accepted"] and result["proposed"][0]["stores"] == ["tienda-a.es"]


def test_model_gets_the_list_and_the_accepted_contributions_with_their_stores():
    compiled = {"requirements": {"gen/11": {"observed": {"plazo para desistir o devolver": ["a.es", "b.es"]},
                                            "accepted": [{"contribution": "remisión a una página de condiciones",
                                                          "component": "condiciones", "stores": ["a.es", "c.es"],
                                                          "cases": ["c1", "c3"]}]}}}
    items = resolving.for_model(GEN11, compiled)
    assert [(c["contribution"], c["origin"], c["stores"]) for c in items] == [
        ("plazo para desistir o devolver", "marco", ["a.es", "b.es"]),
        ("modelo de formulario de desistimiento", "marco", []),
        ("remisión a una página de condiciones", "fichas", ["a.es", "c.es"])]


def test_declared_contribution_is_normalised():
    assert resolving.contribution({"contribution": " plazo "}) == {"contribution": "plazo", "component": None, "new": False}
    assert resolving.contribution({"contribution": {"new": "canal", "component": "condiciones"}})["new"] is True
    assert resolving.contribution({"contribution": {"component": "x"}}) is None
    assert resolving.store("https://www.Tienda.es/x") == "tienda.es"


def test_check_v3_asks_for_trait_votes_and_contributions():
    from demand_engine.demand.model import v3_problems
    model = {"general": [{"requirements": [dict(GEN11)]}], "inferred": [],
             "blocks": [{"type": "categoría", "requirements": [
                 {"id": "cat.alimentos/06", "vote": "principal", "trait_vote": None, "resolving_info": []},
                 {"id": "cat.alimentos/07", "vote": "principal", "trait_vote": "sabor", "resolving_info": []}]}]}
    out = {"trait_votes": {"cat.alimentos/07": "sabor"}, "proposed_traits": [{"name": "sabor"}],
           "declared": [{"feature": "14 días", "role": "condición de oferta", "answers": "gen/11",
                         "contribution": "plazo para desistir o devolver"},
                        {"feature": "devolución en tienda", "role": "condición de oferta", "answers": "gen/11",
                         "contribution": "canal de devolución"},
                        {"feature": "sin coste", "role": "condición de oferta", "answers": "gen/11",
                         "contribution": {"new": "coste de la devolución"}},
                        {"feature": "fresa", "role": "valor", "answers": "cat.alimentos/06"},
                        {"feature": "bonito", "role": "estético", "answers": "cat.alimentos/06"}]}
    problems = v3_problems(out, model, {"material"}, {"sabor": {"name": "sabor"}})
    joined = "\n".join(problems)
    assert "rasgo propuesto «sabor» sin nombre o sin definición" in joined
    assert "cat.alimentos/06: sin voto de rasgo" in joined
    assert "«canal de devolución» no está en sus aportaciones" in joined
    assert "la aportación nueva necesita «new» y «component»" in joined
    assert "«fresa» (cat.alimentos/06): falta «contribution»" in joined
    assert "14 días" not in joined and "bonito" not in joined


def test_catalog_check_wants_resolving_information_supported_by_the_sources():
    from demand_engine.demand.model import block_problems
    ok = {"contribution": "material del relleno", "component": "material", "origin": "referencias",
          "support": ["shopify-attr:filler-material"]}
    block = {"id": "cat.cojines", "requirements": [
        {"id": "cat.cojines/01", "question": "¿Con qué material está relleno?", "trait": "material",
         "importance": "principal", "origin": "referencias", "sources": ["shopify-attr:filler-material"],
         "resolving_info": [ok, {"contribution": "ficha técnica del relleno", "component": "material", "origin": "inferida",
                                 "support": []}]},
        {"id": "cat.cojines/02", "question": "¿Qué firmeza tiene?", "trait": "prestacion", "vote": "complementario",
         "origin": "referencias", "sources": ["shopify-attr:filler-support"], "resolving_info": [ok]},
        {"id": "cat.cojines/03", "question": "¿Es reversible?", "trait": "construccion", "importance": "complementario",
         "origin": "inferida", "sources": ["amazon-ptd-prop:PILLOW.special_feature=Reversible"], "resolving_info": []},
        {"id": "cat.otro/04", "question": "¿?", "trait": "sabor", "importance": "principal", "origin": "inferida",
         "sources": [], "resolving_info": [{"contribution": "x", "component": "", "origin": "inferida", "support": []}]}]}
    joined = "\n".join(block_problems(block, {"material", "prestacion", "construccion"}))
    assert "cat.cojines/01" not in joined
    assert "cat.cojines/02: aportación «material del relleno»: respaldo fuera de las fuentes del requisito" in joined
    assert "cat.cojines/03: cuestión inferida con fuentes" in joined and "cat.cojines/03: sin información resolutiva" in joined
    assert "cat.otro/04: el identificador no es del bloque" in joined and "rasgo «sabor» fuera del vocabulario" in joined
    assert "aportación sin nombre o sin componente" in joined


def test_paa_origin_takes_its_questions_as_sources():
    from demand_engine.demand.model import block_problems
    inferred = [{"contribution": "declaración de resistencia a las arrugas", "component": "arrugas", "origin": "inferida",
                 "support": []}]
    req = {"question": "¿Se arruga el tejido?", "trait": "prestacion", "vote": "complementario", "resolving_info": inferred}
    block = {"id": "cat.sabanas", "requirements": [
        {**req, "id": "cat.sabanas/05", "origin": "paa", "sources": ["paa-q:sabanas:se-arruga-mucho-el-lino"]},
        {**req, "id": "cat.sabanas/06", "origin": "paa", "sources": []},
        {**req, "id": "cat.sabanas/07", "origin": "paa", "sources": ["shopify-attr:fabric"]},
        {**req, "id": "cat.sabanas/08", "origin": "mpir", "sources": ["x"]}]}
    joined = "\n".join(block_problems(block, {"prestacion"}))
    assert "cat.sabanas/05" not in joined
    assert "cat.sabanas/06: origen «paa» sin fuentes" in joined
    assert "cat.sabanas/07: origen «paa» con fuentes que no son preguntas PAA (paa-q:)" in joined
    assert "cat.sabanas/08: origen «mpir» no válido" in joined


def test_general_layer_admits_framework_contributions_from_its_law():
    from demand_engine.demand.model import gen_problems
    law = "ley:TRLGDCU-97.1.j@2026-02-28"
    gen = {"blocks": [{"requirements": [
        {"id": "gen/11", "sources": [law], "resolving_info": [
            {"contribution": "plazo para desistir o devolver", "component": "plazo", "origin": "marco", "support": [law]},
            {"contribution": "coste de la devolución", "component": "coste", "origin": "marco",
             "support": ["ley:TRLGDCU-97.1.k@2026-02-28"]}]},
        {"id": "gen/15", "sources": [], "resolving_info": [
            {"contribution": "opiniones de compradores", "component": "opiniones", "origin": "inferida", "support": []}]},
        {"id": "gen/16", "sources": [], "resolving_info": []}]}]}
    assert gen_problems(gen) == ["gen/11: aportación «coste de la devolución»: respaldo fuera de las fuentes del requisito",
                                 "gen/16: sin información resolutiva"]


def proposal(sources, question="¿Lleva adornos?", vote="complementario"):
    return {"id": "inf/01", "block": "cat.mantas", "question": question, "trait": "estetica", "vote": vote,
            "sources": sources, "resolving_info": [{"contribution": "adornos", "component": "adornos",
                                                     "origin": "referencias", "support": sources, "stores": []}]}


def test_block_proposals_skip_what_the_block_asks_or_excludes_and_keep_one_per_source():
    from demand_engine.demand.train import block_proposals
    blocks = {"cat.mantas": {"id": "cat.mantas", "requirements": [{"id": "cat.mantas/01", "sources": ["a:asked"]}],
                             "excluded": [{"source": "a:excluded", "reason": "…"}]}}
    models = {"run-a": {"c1": {"inferred": [proposal(["a:asked"]), proposal(["a:excluded"]), proposal(["a:new"]),
                                            proposal([])]}},
              "run-b": {"c1": {"inferred": [proposal(["a:new"], "¿Tiene flecos?")]}}}
    found = block_proposals(models, blocks)
    assert [(p["block"], p["case"], p["requirement"]["sources"]) for p in found] == [("cat.mantas", "c1", ["a:new"])]


def test_a_proposal_enters_its_block_with_a_new_id_and_origin_references():
    from demand_engine.demand.train import add_block_proposals
    block = {"id": "cat.mantas", "requirements": [{"id": "cat.mantas/12", "sources": ["a:asked"]}],
             "excluded": [{"id": "cat.mantas/13", "reason": "retirado"}]}
    added = add_block_proposals({"cat.mantas": block}, {"run-a": {"c1": {"inferred": [proposal(["a:new"])]}}})
    assert added == ["cat.mantas/14"]
    r = block["requirements"][-1]
    assert r["origin"] == "referencias" and r["sources"] == ["a:new"] and r["seed_importance"] == "complementario"
    assert "stores" not in r["resolving_info"][0]
