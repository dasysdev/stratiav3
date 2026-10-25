import sys

import pytest

from demand_engine import blocks

PTD = {"zz-1": {"ptd": "SHEET", "node": "123", "relation": "prueba"}}


def test_each_attribute_goes_to_the_most_general_category(fake_refs):
    plan = {b["shopify"]: b for b in blocks.plan(["zz-1-2"], PTD)["blocks"]}
    own = {c: [a["source"] for a in b["attributes"]] for c, b in plan.items()}
    assert own == {"zz": ["shopify-attr:color"], "zz-1": ["shopify-attr:fabric"],
                   "zz-1-2": ["shopify-attr:bedding-size"]}
    assert plan["zz-1-2"]["parent"] == "zz-1" and plan["zz"]["children_in_plan"] == ["zz-1"]
    assert plan["zz-1-2"]["refs"] == ["shopify:zz-1-2@v1", "google:2541@g1"]


def test_amazon_candidates_go_to_the_mapped_category(fake_refs):
    plan = {b["shopify"]: b for b in blocks.plan(["zz-1-2"], PTD)["blocks"]}
    assert "amazon-ptd:SHEET@p1" in plan["zz-1"]["refs"] and "amazon-btg:123@b1" in plan["zz-1"]["refs"]
    sources = [c["source"] for c in plan["zz-1"]["amazon"]]
    # color repeats a Shopify attribute, brand is administrative, battery is not descriptive
    assert sources == ["amazon-ptd-prop:SHEET.thread_count", "amazon-ptd-prop:SHEET.compliance_fabric",
                       "amazon-ptd-prop:SHEET.fabric_weight", "amazon-ptd-prop:SHEET.special_feature=Antiarrugas"]


def test_unknown_ptd_is_a_clean_error(fake_refs, monkeypatch):
    monkeypatch.setattr(sys, "argv", ["blocks", "plan", "zz-1-2", "--ptd", "zz-1=NOPE"])
    with pytest.raises(SystemExit, match="blocks: no existe el PTD NOPE"):
        blocks.main()
