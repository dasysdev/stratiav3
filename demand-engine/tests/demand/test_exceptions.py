"""Exceptions by requirement and class (D-055, D-058): any requirement may have its own rule where its votes contradict
the rule of its trait, critical included; the framework is never lowered."""
from demand_engine.demand.catalog import resolve
from demand_engine.demand.train import induce_exceptions, requirement_coherence

COLOR = "cat.mobiliario/01"


def block(req=COLOR, trait="estetica", seed="complementario", node="fr-22", sources=()):
    return {req: {"id": req.split("/")[0], "shopify": node,
                  "requirements": [{"id": req, "trait": trait, "seed_importance": seed, "sources": list(sources)}]}}


def models(*votes, req=COLOR, trait="estetica"):
    """One model per vote: (class, level)."""
    out = {}
    for i, (node, level) in enumerate(votes):
        out[f"c{i}"] = {"blocks": [{"type": "categoría", "requirements": [
            {"id": req, "trait": trait, "vote": level, "classes": [node]}]}]}
    return {"run": out}


TREE = {"estetica@fr-22": "complementario"}


def test_votes_against_the_trait_rule_make_an_exception_in_their_class():
    table, rules = induce_exceptions(block(), models(("fr-22-7", "principal"), ("fr-22-7", "principal")), TREE, {})
    assert table == {f"{COLOR}@fr-22-7": "principal"}  # 2 votes against the catalog's starting vote
    assert rules[0]["id"] == f"imp:{COLOR}@fr-22-7" and rules[0]["kind"] == "excepción"
    assert resolve("estetica", ["fr-22-7"], {"tree": TREE, "requirements": table}, req=COLOR)[0] == "principal"
    assert resolve("estetica", ["fr-22-4"], {"tree": TREE, "requirements": table}, req=COLOR)[0] == "complementario"
    assert resolve("estetica", ["fr-22-7"], {"tree": TREE, "requirements": table})[0] == "complementario"  # trait rule only


def test_one_critical_vote_against_the_catalog_is_a_tie_and_keeps_the_rule():
    table, _ = induce_exceptions(block(seed="principal"), models(("fr-22-7", "crítico")), TREE, {})
    assert table == {}


def test_any_property_can_be_critical_by_its_votes():
    votes = models(("fr-22-7", "crítico"), ("fr-22-7", "crítico"))
    table, _ = induce_exceptions(block(seed="principal"), votes, TREE, {})
    assert table == {f"{COLOR}@fr-22-7": "crítico"}


def test_exception_climbs_only_when_two_children_agree():
    votes = models(("fr-22-7", "principal"), ("fr-22-7", "principal"), ("fr-22-4", "principal"), ("fr-22-4", "principal"))
    table, rules = induce_exceptions(block(node="fr"), votes, {"estetica@fr": "complementario"}, {})
    assert table == {f"{COLOR}@fr-22": "principal"}
    assert rules[0]["climbed"]


def test_votes_that_agree_with_the_rule_make_no_exception():
    table, _ = induce_exceptions(block(), models(("fr-22-7", "complementario"), ("fr-22-7", "complementario")), TREE, {})
    assert table == {}


def test_framework_is_never_lowered():
    low = models(("aa-8-3", "complementario"), ("aa-8-3", "complementario"), req="cat.calzado/01")
    table, _ = induce_exceptions(block("cat.calzado/01", "medida-que-fija", "crítico", "aa-8"), low, {}, {})
    assert table == {}
    table, _ = induce_exceptions(block("cat.calzado/01", "medida", "principal", "aa-8"), low, {}, {})
    assert table == {}  # the descriptive measure stays principal
    high = models(("hg-15-1-4", "crítico"), ("hg-15-1-4", "crítico"), req="cat.ropa-de-cama/02")
    table, _ = induce_exceptions(block("cat.ropa-de-cama/02", "medida", "principal", "hg-15-1"), high, {}, {})
    assert table == {"cat.ropa-de-cama/02@hg-15-1-4": "crítico"}  # but its votes can make it critical (D-055)
    rules = {"tree": {}, "requirements": table}
    assert resolve("medida", ["hg-15-1-4"], rules, req="cat.ropa-de-cama/02") == ("crítico", "imp:cat.ropa-de-cama/02@hg-15-1-4")
    assert resolve("medida", ["hg-15-1-2"], rules, req="cat.ropa-de-cama/02")[0] == "principal"
    textile = ["ley:UE-1007/2011-16.1@2011-10-18"]
    assert resolve("material", ["hg-15"], {"tree": {"material@hg-15": "complementario"}}, textile)[0] == "principal"


def test_exception_wins_over_a_more_specific_trait_rule_and_pieces_take_the_highest():
    rules = {"tree": {"estetica@fr-22-7": "complementario"}, "requirements": {f"{COLOR}@fr-22": "principal"}}
    assert resolve("estetica", ["fr-22-7"], rules, req=COLOR) == ("principal", f"imp:{COLOR}@fr-22")
    rules = {"tree": {"estetica@fr-22": "complementario"}, "requirements": {f"{COLOR}@fr-22-7": "crítico"}}
    assert resolve("estetica", ["fr-22-4", "fr-22-7"], rules, req=COLOR)[0] == "crítico"


def test_requirement_coherence_counts_clear_majorities_against_the_importance():
    votes = models(("fr-22-7", "principal"), ("fr-22-7", "principal"), ("fr-22-4", "principal"), ("fr-22-4", "complementario"))
    before = requirement_coherence(votes, {"tree": TREE})
    assert before["against"] == 1 and before["pairs"] == 2  # fr-22-4 is a tie: no majority
    table, _ = induce_exceptions(block(), votes, TREE, {})
    after = requirement_coherence(votes, {"tree": TREE, "requirements": table})
    assert after["against"] == 0
