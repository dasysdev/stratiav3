"""Specializations induced by the training (D-190): synonyms, anchor along the tree, seed and proposals."""
import json

from demand_engine.demand import model as engine
from demand_engine.demand import specializations as S
from demand_engine.demand.train import FAMILIES, combine, family, stability


def obs(sid, name, classes, case="c1", run="r-a", requirements=()):
    return {"id": sid, "name": name, "order": "función", "trigger": "t", "support": ["shopify-attr:power-source"],
            "classes": list(classes), "store": "tienda.es", "run": run, "case": case, "requirements": list(requirements)}


def req(sid, n, question, dimension="d", vote="principal"):
    return {"id": f"{sid}/{n:02d}", "question": question, "dimension": dimension, "trait": "uso", "vote": vote,
            "sources": [], "resolving_info": [{"contribution": "x", "component": "y", "origin": "inferida", "support": []}]}


def test_synonyms_of_a_vertical_merge_into_the_most_observed():
    found = [obs("esp.a-bateria", "a batería", ["ha-15-59-3"]), obs("esp.bateria", "de batería", ["ha-15-59-3"]),
             obs("esp.bateria", "a batería", ["ha-15-59-3"], case="c2")]
    canon = S.synonyms(found, {})
    assert canon == {"esp.a-bateria": "esp.bateria", "esp.bateria": "esp.bateria"}


def test_same_words_in_another_vertical_are_not_synonyms():
    found = [obs("esp.luces", "luces", ["aa-8-11-5"]), obs("esp.luces-led", "luces led", ["hg-13"])]
    canon = S.synonyms(found, {})
    assert canon["esp.luces-led"] == "esp.luces-led"


def test_a_compiled_specialization_keeps_its_id_and_its_aliases():
    specs = {"esp.a-bateria": {"id": "esp.a-bateria", "name": "a batería", "anchors": ["ha-15-59"], "_where": "catálogo",
                               "aliases": ["esp.con-bateria"]}}
    found = [obs("esp.bateria", "de batería", ["ha-15-59-3"]), obs("esp.bateria", "de batería", ["ha-15-59-1"])]
    canon = S.synonyms(found, specs)
    assert canon["esp.bateria"] == "esp.a-bateria" and canon["esp.con-bateria"] == "esp.a-bateria"


def test_anchor_climbs_only_when_two_children_have_it():
    assert S.anchors(["ha-15-59-3"]) == ["ha-15-59-3"]
    assert S.anchors(["ha-15-59-3", "ha-15-59-1"]) == ["ha-15-59"]
    # a third child with data that does not have it below its own level blocks the climb
    assert S.anchors(["ha-15-59-3", "ha-15-59-1", "ha-15-59-2-1"]) == ["ha-15-59-1", "ha-15-59-2-1", "ha-15-59-3"]
    assert S.anchors(["ha-15-59-3"], kept=["ha-15-59-1"]) == ["ha-15-59"]  # a registered anchor counts


def test_anchor_never_climbs_above_the_verticals():
    assert S.anchors(["ha-15", "aa-8"]) == ["aa-8", "ha-15"]


def test_seed_is_the_first_proposal_and_new_needs_are_proposals_to_the_block():
    sid = "esp.bateria"
    seen = [obs(sid, "a batería", ["ha-15-59-3"], requirements=[
                req(sid, 1, "¿Qué tipo de batería usa y qué capacidades admite?", "tipo y capacidad de batería"),
                req(sid, 2, "¿Qué autonomía tiene con una carga y cuánto tarda en cargarse?", "autonomía y tiempo de carga")]),
            obs("esp.a-bateria", "a batería", ["ha-15-59-3"], case="c2", run="r-b", requirements=[
                req("esp.a-bateria", 1, "¿Con qué baterías es compatible (sistema, marca, tensión)?", "compatibilidad de batería"),
                req("esp.a-bateria", 2, "¿Qué autonomía tiene con una carga?", "autonomía")])]
    block = S.seed_block(sid, ["esp.a-bateria", sid], seen, {})
    assert [r["id"] for r in block["requirements"]] == ["esp.bateria/01", "esp.bateria/02", "esp.bateria/03"]
    added = block["requirements"][2]
    assert "compatible" in added["question"] and "Propuesta al bloque" in added["rationale"]
    assert added["seed_importance"] == "principal" and added["origin"] == "inferida"


def test_without_resolving_information_a_proposal_is_not_a_seed_nor_enters_the_block():
    sid = "esp.luces"
    old = req(sid, 1, "¿Cómo se alimentan las luces?")
    old["resolving_info"] = []  # drafted before D-063
    seen = [obs(sid, "luces", ["aa-8-11-5"], requirements=[old, req(sid, 2, "¿Cuánto duran las luces?")]),
            obs(sid, "luces", ["aa-8-11-5"], case="c2", requirements=[req(sid, 1, "¿Cómo se activan las luces?")]),
            obs(sid, "luces", ["aa-8-11-5"], case="c3", requirements=[dict(req(sid, 1, "¿Son reflectantes?"), resolving_info=[])])]
    block = S.seed_block(sid, [sid], seen, {})
    # c2 is the first complete proposal; from c1 only the requirement with resolving information enters
    assert [r["question"] for r in block["requirements"]] == ["¿Cómo se activan las luces?", "¿Cuánto duran las luces?"]
    assert S.framework_problems(dict(block, support=["s"])) == []


def test_a_registered_block_is_the_seed_with_the_id_of_its_specialization():
    specs = {"esp.a-bateria": {"id": "esp.a-bateria", "name": "a batería", "order": "función", "support": ["s"],
                               "anchors": ["ha-15-59-3"], "_where": "ejecución",
                               "requirements": [req("esp.a-bateria", 1, "¿Qué tipo de batería usa?")]}}
    block = S.seed_block("esp.bateria", ["esp.a-bateria", "esp.bateria"], [], specs)
    assert block["id"] == "esp.bateria" and block["requirements"][0]["id"] == "esp.bateria/01"


def test_induce_gives_one_rule_per_anchor_and_rejects_what_the_framework_does_not_admit(monkeypatch):
    sid = "esp.bateria"
    no_support = obs("esp.luces", "luces", ["aa-8-11-5"], requirements=[req("esp.luces", 1, "¿Cómo se alimentan?")])
    no_support["support"] = []
    found = [obs(sid, "a batería", ["ha-15-59-3"], requirements=[req(sid, 1, "¿Qué tipo de batería usa?")]),
             obs(sid, "a batería", ["ha-15-59-1"], case="c2"), no_support]
    monkeypatch.setattr(S, "observations", lambda m: found)  # the runs on disk are not needed here
    out = S.induce({}, {})
    assert out["table"][sid]["anchors"] == ["ha-15-59"]
    assert [r["id"] for r in out["rules"]] == ["esp:esp.bateria@ha-15-59"] and out["rules"][0]["climbed"]
    assert out["rejected"] == [{"id": "esp.luces", "problems": ["sin apoyo en las referencias (D-024)"], "cases": 1}]


def model(key, esp):
    return {"key": {"model": key}, "composition": {"classes": ["ha-15-59-3"], "aliases": []},
            "offer": {"application": []}, "blocks": [{"id": e, "type": "especialización", "requirements": []} for e in esp]}


def test_stability_compares_specializations_by_id_with_the_merged_synonyms():
    a = model(["gen@0.3", "cat.lijadoras@2", "esp.a-bateria@0"], ["esp.a-bateria"])
    b = model(["gen@0.3", "cat.lijadoras@2", "esp.bateria@0"], ["esp.bateria"])
    runs = {"r-a": {"c": a}, "r-b": {"c": b}}
    before = stability(runs, {})
    after = stability(runs, {"specializations": {"esp.bateria": {"aliases": ["esp.a-bateria"]}}})
    assert (before["key"], before["specializations"], before["esp_uncompiled"]) == (0, 0, 2)
    assert (after["key"], after["specializations"], after["esp_uncompiled"]) == (1, 1, 0)


def test_the_three_families_split_and_combine():
    rules = {"tree": {"uso@hg": "principal"}, "relevance": {"x@hg": "excluido"},
             "specializations": {"esp.juego": {"anchors": ["hg-15"], "aliases": []}},
             "rules": [{"kind": "general"}, {"kind": "relevancia"}, {"kind": "especialización"}]}
    parts = [family(rules, n) for n in FAMILIES]
    assert [len(p["rules"]) for p in parts] == [1, 1, 1]
    again = combine(*parts)
    assert again["specializations"] == rules["specializations"] and len(again["rules"]) == 3


def test_assembly_takes_the_specialization_from_the_catalog_by_id_or_synonym(tmp_path, monkeypatch):
    spec = {"id": "esp.bateria", "type": "especialización", "name": "a batería", "order": "función", "trigger": "batería",
            "support": ["shopify-attr:power-source"], "anchors": ["ha-15-59"], "aliases": ["esp.a-bateria"],
            "version": "1", "status": "compilado", "_where": "catálogo",
            "requirements": [dict(req("esp.bateria", 1, "¿Qué tipo de batería usa?"), seed_importance="principal",
                                  importance="principal", origin="inferida")]}
    monkeypatch.setattr(engine, "load_specializations", lambda: {"esp.bateria": spec})
    out = {"case": "x", "rulebook": "v4", "declared": [], "application": [], "inferred": [],
           "composition": {"categories": [{"shopify": "ha-15-59-3", "alias": False}]},
           "specializations": [{"id": "esp.a-bateria", "trigger": "funciona con batería"}, {"id": "esp.nueva"}],
           "votes": {"esp.bateria/01": "complementario"}, "trait_votes": {"esp.bateria/01": "uso"}}
    path = tmp_path / "x.json"
    path.write_text(json.dumps(out), encoding="utf-8")
    m = engine.assemble(path)
    block = next(b for b in m["blocks"] if b["type"] == "especialización")
    assert block["id"] == "esp.bateria" and block["version"] == "1" and block["anchors"] == ["ha-15-59"]
    assert block["requirements"][0]["vote"] == "complementario"
    assert "esp.bateria@1" in m["key"]["model"]
    assert m["uncompiled"]["missing_specializations"] == ["esp.nueva"]
