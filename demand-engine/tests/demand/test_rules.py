"""Importance rules by trait along the Shopify tree (D-045): induction and resolution."""
from demand_engine.demand.catalog import resolve
from demand_engine.demand.train import induce, pairs


def point(trait, node, label, w=1.0):
    return {"trait": trait, "node": node, "label": label, "w": w, "ref": f"{node}:{trait}", "from": "test"}


def test_rule_climbs_when_two_children_agree():
    rules = induce([point("estetica", "hg-15-1", "complementario"), point("estetica", "hg-15-4", "complementario")])
    assert rules["tree"] == {"estetica@hg-15": "complementario"}
    assert resolve("estetica", ["hg-15-9"], rules) == ("complementario", "imp:estetica@hg-15")


def test_single_child_does_not_climb_and_other_branches_get_no_rule():
    rules = induce([point("estetica", "hg-15-1", "complementario")])
    assert rules["tree"] == {"estetica@hg-15-1": "complementario"}
    assert resolve("estetica", ["hg-15-4"], rules) == (None, None)
    assert resolve("estetica", ["aa-8"], rules) == (None, None)


def test_exception_stays_in_its_class():
    rules = induce([point("estetica", "hg-15-1", "complementario"), point("estetica", "hg-15-4", "complementario"),
                    point("estetica", "hg-15-4", "complementario"), point("estetica", "hg-3-64", "principal")])
    assert rules["tree"]["estetica@hg-15"] == "complementario"
    assert rules["tree"]["estetica@hg-3-64"] == "principal"
    assert "estetica@hg" not in rules["tree"]


def test_contradicting_child_blocks_climbing():
    rules = induce([point("uso", "fr-22-7", "principal"), point("uso", "fr-22-4", "complementario")])
    assert "uso@fr-22" not in rules["tree"]
    assert rules["tree"]["uso@fr-22-7"] == "principal"


def test_rules_never_climb_above_verticals():
    rules = induce([point("cuidado", "hg", "complementario"), point("cuidado", "aa", "complementario")])
    assert resolve("cuidado", ["el-1"], rules) == (None, None)


def test_tie_goes_to_the_higher_level():
    rules = induce([point("material", "hg-15-1", "principal"), point("material", "hg-15-1", "complementario")])
    assert rules["tree"]["material@hg-15-1"] == "principal"


def test_trait_rules_never_give_critical():
    rules = induce([point("seguridad", "ap-2-3-7", "crítico"), point("contenido", "ap-2-3-3", "crítico")])
    assert rules["tree"]["seguridad@ap-2-3-7"] == "principal"  # a critical vote counts as principal (D-055, D-058)
    assert rules["tree"]["contenido@ap-2-3-3"] == "principal"
    assert "global" not in rules


def test_framework_rules_win():
    rules = induce([point("medida", "fr-22", "complementario")])
    assert resolve("medida-que-fija", ["fr-22"], rules)[0] == "crítico"
    assert resolve("medida", ["fr-22"], rules)[0] == "principal"
    assert resolve("material", ["hg-15"], rules, ["ley:UE-1007/2011-16.1@2011-10-18"])[0] == "principal"


def test_model_takes_highest_level_across_pieces():
    rules = induce([point("uso", "hg-15-1-2", "principal"), point("uso", "hg-15-1-8", "complementario")])
    assert resolve("uso", ["hg-15-1-2-1", "hg-15-1-8-2"], rules)[0] == "principal"


def test_runs_pair_in_order_given():
    models = {"t-a": {"x": 1, "y": 2}, "t-b": {"x": 3}, "c-a": {"z": 4}, "c-b": {"z": 5}, "odd": {"x": 6}}
    assert pairs(models) == [("x", 1, 3), ("z", 4, 5)]
