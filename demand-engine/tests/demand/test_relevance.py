"""Learned relevance filter (D-050): rules by requirement and class; doubt does not exclude."""
from demand_engine.demand.catalog import protected, relevance
from demand_engine.demand.train import induce_relevance

COLOR = "cat.productos-para-mascotas/02"
BLOCKS = {COLOR: {"id": "cat.productos-para-mascotas", "shopify": "ap-2",
                  "requirements": [{"id": COLOR, "trait": "estetica", "origin": "referencias", "sources": []}]}}


def vote(node, label, w=1.0, req=COLOR):
    return {"req": req, "node": node, "label": label, "w": w, "from": "test", "ref": f"{node}:{req}"}


def seed():
    return vote("ap-2", "relevante")


def test_exclusion_stays_in_the_class_that_votes_it():
    table, _, _ = induce_relevance([seed(), vote("ap-2-3-3", "no relevante"), vote("ap-2-3-3", "no relevante")], BLOCKS)
    assert table == {f"{COLOR}@ap-2-3-3": "excluido"}
    assert relevance(COLOR, ["ap-2-3-3"], {"relevance": table}) == (True, f"rel:{COLOR}@ap-2-3-3")
    assert relevance(COLOR, ["ap-2-3-2"], {"relevance": table}) == (False, None)  # a collar keeps the colour


def test_tie_keeps_the_requirement():
    table, _, _ = induce_relevance([seed(), vote("ap-2-3-3", "no relevante"), vote("ap-2-3-3", "relevante")], BLOCKS)
    assert table == {}


def test_no_votes_against_means_no_rules():
    table, rules, _ = induce_relevance([seed(), vote("ap-2-3-3", "relevante")], BLOCKS)
    assert table == {} and rules == []


def test_exclusion_climbs_only_when_all_children_agree():
    pts = [seed(), vote("ap-2-3-3", "no relevante"), vote("ap-2-3-7", "no relevante"), vote("ap-2-3-2", "relevante")]
    table, _, _ = induce_relevance(pts, BLOCKS)
    assert "cat.productos-para-mascotas/02@ap-2-3" not in table
    pts = [seed(), vote("ap-2-3-3", "no relevante"), vote("ap-2-3-7", "no relevante")]
    table, _, _ = induce_relevance(pts, BLOCKS)
    assert table == {f"{COLOR}@ap-2-3": "excluido"}


def test_piece_sets_keep_what_any_piece_needs():
    rules = {"relevance": {f"{COLOR}@ap-2-3-3": "excluido"}}
    assert relevance(COLOR, ["ap-2-3-3", "ap-2-3-2"], rules)[0] is False


def test_framework_requirements_are_never_excluded():
    assert protected("medida-que-fija", "referencias")
    assert protected("material", "normativa")
    assert protected("material", "referencias", ["ley:UE-1007/2011-16.1@2011-10-18"])
    blocks = {"x": {"id": "cat.x", "shopify": "hg-15", "requirements": [
        {"id": "cat.x/01", "trait": "material", "origin": "normativa", "sources": []}]}}
    table, _, conflicts = induce_relevance([vote("hg-15-1", "no relevante", req="cat.x/01")], blocks)
    assert table == {} and len(conflicts) == 1
