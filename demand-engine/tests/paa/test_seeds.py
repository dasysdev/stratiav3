"""Seeds of the PAA phase of an execution (D-224): one set per key, core and values from taxo, the calibrated trait only
in textiles (OQ-93)."""
import json

import pytest

from demand_engine.paa import seeds
from demand_engine.paa.store import SeedSet, StoreError

CATS = {"hg": {"name": "Casa", "attributes": [{"handle": "material"}]},
        "hg-1": {"name": "Ropa de cama", "attributes": []},
        "hg-1-5": {"name": "Fundas de nórdico", "attributes": [{"handle": "fabric"}, {"handle": "color"}]},
        "hg-1-8": {"name": "Fundas de almohada", "attributes": [{"handle": "fabric"}]},
        "hg-1-8-2": {"name": "Fundas de almohada estándar", "attributes": []},
        "fr": {"name": "Muebles", "attributes": [{"handle": "material"}, {"handle": "seat-upholstery-material"}]},
        "fr-22": {"name": "Sofás", "attributes": []}}
ATTRS = {"fabric": {"name": "Tejido", "values": [{"name": v} for v in ("Algodón", "Lino", "Franela", "Lino", "Tela de toalla")]},
         "fabric-weave": {"name": "Tipo de tejido", "values": [{"name": "Microfibra"}]},
         "material": {"name": "Material", "values": [{"name": "Madera"}]},
         "color": {"name": "Color", "values": [{"name": "Rojo"}]},
         "seat-upholstery-material": {"name": "Material de la tapicería", "values": []}}
CATS["hg-1-5"]["attributes"].append({"handle": "fabric-weave"})
LAW = "ley:UE-1007/2011-16.1@2018-02-15"


@pytest.fixture(autouse=True)
def taxo(monkeypatch):
    monkeypatch.setattr(seeds, "shopify_categories", lambda: CATS)
    monkeypatch.setattr(seeds, "shopify_attributes", lambda: ATTRS)
    monkeypatch.setattr(seeds, "category_name", lambda node: CATS[node]["name"])


def model(tmp_path, name, key, classes, blocks, sources=(LAW,)):
    m = {"name": name, "key": {"model": key}, "composition": {"classes": classes, "aliases": []},
         "general": [{"id": "gen", "requirements": []}], "inferred": [],
         "blocks": blocks + [{"id": "cat.casa", "type": "categoría", "shopify": "hg", "position": "sector",
                              "requirements": [{"id": "cat.casa/01", "question": "¿De qué?", "sources": list(sources)}]}]}
    path = tmp_path / "case.model.json"
    path.write_text(json.dumps(m), encoding="utf-8")
    return path


def bedding(tmp_path):
    blocks = [{"id": "cat.fundas-de-nordico", "type": "categoría", "shopify": "hg-1-5", "position": "categoría", "requirements": []},
              {"id": "cat.fundas-de-almohada", "type": "categoría", "shopify": "hg-1-8", "position": "sector", "requirements": []},
              {"id": "esp.juego", "type": "especialización", "name": "juego", "order": "juego", "requirements": []}]
    return model(tmp_path, "Casa › Fundas de nórdico + Fundas de almohada estándar · juego",
                 ["gen@0.10", "cat.casa@2", "cat.fundas-de-nordico@5", "cat.fundas-de-almohada@5", "esp.juego@1"],
                 ["hg-1-5", "hg-1-8-2"], blocks)


def test_the_core_comes_from_the_key_and_the_values_from_the_calibrated_trait_of_taxo(tmp_path, paa_dirs):
    path = bedding(tmp_path)
    p = seeds.plan(path)
    assert p["set"] == "fundas-de-nordico-fundas-de-almohada-estandar-juego" and p["existing"] is None
    # the nearest block of each class, the specialization from the first core seed; no sector of its own
    assert [(c["key"], c["q"]) for c in p["core"]] == [("cat.fundas-de-nordico", "fundas de nórdico"),
                                                       ("cat.fundas-de-almohada", "fundas de almohada"),
                                                       ("esp.juego", "juego de fundas de nórdico")]
    assert p["trait"] == "fabric" and "cat.casa/01" in p["why"] and p["taxo_values"] == ["Algodón", "Lino", "Franela", "Tela de toalla"]
    assert p["values"] == [] and [s["group"] for s in p["seeds"]] == ["núcleo"] * 3   # the values are a choice
    p = seeds.plan(path, values=["algodon", "Tela de toalla", "fabric-weave=Microfibra"],
                   seeds=["cat.fundas-de-nordico=fundas nórdicas", "esp.juego=juego de funda nórdica",
                          "Tela de toalla=fundas nórdicas de rizo"])
    out = seeds.write(p, path)
    data = json.loads(out.read_text(encoding="utf-8"))
    assert out == paa_dirs / "sets" / f"{p['set']}.json"
    assert data["key"] == ["gen", "cat.casa", "cat.fundas-de-nordico", "cat.fundas-de-almohada", "esp.juego"]
    assert data["trait"]["attribute"] == "fabric" and data["clicks"] == 8 and data["model"].endswith("case.model.md")
    assert [(s["q"], s["group"], s["from"]) for s in data["seeds"]] == [
        ("fundas nórdicas", "núcleo", "cat.fundas-de-nordico"),
        ("fundas de almohada", "núcleo", "cat.fundas-de-almohada"),
        ("juego de funda nórdica", "núcleo", "esp.juego"),
        ("fundas nórdicas de algodón", "tejido", "shopify-attr:fabric=Algodón"),
        ("fundas nórdicas de rizo", "tejido", "shopify-attr:fabric=Tela de toalla"),
        ("fundas nórdicas de microfibra", "tejido", "shopify-attr:fabric-weave=Microfibra")]
    assert SeedSet(p["set"]).definition()["seeds"][0]["q"] == "fundas nórdicas"
    assert '\n    {"q": "fundas nórdicas", "group": "núcleo", "from": "cat.fundas-de-nordico"},\n' in out.read_text(encoding="utf-8")


def test_a_key_that_has_a_set_uses_it_and_another_key_gets_its_own(tmp_path, paa_dirs):
    path = bedding(tmp_path)
    (paa_dirs / "sets" / "fundas.json").write_text(json.dumps({
        "class": "C", "key": ["gen", "cat.casa", "cat.fundas-de-nordico", "cat.fundas-de-almohada", "esp.juego"],
        "seeds": [{"q": "fundas nórdicas"}]}), encoding="utf-8")
    p = seeds.plan(path)
    assert (p["set"], p["existing"]) == ("fundas", "fundas") and "seeds" not in p   # D-116: one set per key
    with pytest.raises(StoreError, match="ya tiene el conjunto fundas"):
        seeds.plan(path, set_id="otro")
    (paa_dirs / "sets" / "fundas.json").write_text(json.dumps({"class": "C", "key": ["gen", "cat.otra"],
                                                               "seeds": [{"q": "x"}]}), encoding="utf-8")
    with pytest.raises(StoreError, match="de otra clave"):
        seeds.plan(path, set_id="fundas")
    (paa_dirs / "sets" / "fundas-de-nordico-fundas-de-almohada-estandar-juego.json").write_text(
        json.dumps({"class": "C", "key": ["gen", "cat.otra"], "seeds": [{"q": "x"}]}), encoding="utf-8")
    assert seeds.plan(path)["set"] == "fundas-de-nordico-fundas-de-almohada-estandar-juego-2"


def test_outside_textiles_the_code_does_not_choose_the_trait(tmp_path, paa_dirs):
    """OQ-93: a class without the textile regulation has no calibrated trait; only --trait gives it."""
    blocks = [{"id": "cat.sofas", "type": "categoría", "shopify": "fr-22", "position": "categoría", "requirements": []}]
    path = model(tmp_path, "Muebles › Sofás", ["gen@0.10", "cat.sofas@3"], ["fr-22"], blocks, sources=())
    p = seeds.plan(path, values=["Madera"])
    assert p["trait"] is None and "OQ-93" in p["why"] and [s["q"] for s in p["seeds"]] == ["sofás"]
    assert set(p["attributes"]) == {"material", "seat-upholstery-material"}
    p = seeds.plan(path, trait="material", values=["Madera"], seeds=["cat.sofas=sofás"])
    assert p["why"] == "--trait" and [s["q"] for s in p["seeds"]] == ["sofás", "sofás de madera"]
    with pytest.raises(StoreError, match="no es de las clases"):
        seeds.plan(path, trait="fabric")


def test_values_and_names_are_checked_against_taxo_and_seeds_do_not_repeat(tmp_path, paa_dirs):
    path = bedding(tmp_path)
    with pytest.raises(StoreError, match="no es un valor de «fabric»"):
        seeds.plan(path, values=["Seda"])
    with pytest.raises(StoreError, match="no es un valor de «pattern»"):
        seeds.plan(path, values=["pattern=Rayas"])
    with pytest.raises(StoreError, match="claves que no son"):
        seeds.plan(path, values=["Lino"], seeds=["Seda=fundas de seda"])
    with pytest.raises(StoreError, match="repetidas"):
        seeds.plan(path, values=["Lino"], seeds=["Lino=fundas de almohada"])


def test_the_plan_says_which_seeds_reuse_a_search_of_another_set(tmp_path, paa_dirs):
    other = paa_dirs / "sets" / "nordicas.json"
    other.write_text(json.dumps({"class": "C", "key": ["gen", "cat.x"], "seeds": [{"q": "fundas de nórdico"}]}),
                     encoding="utf-8")
    s = SeedSet("nordicas")
    s.save(s.seeds()[0], {"query": "fundas de nórdico", "outcome": "captured", "questions": [], "related": [],
                          "url": "https://www.google.es/search?q=x", "hl": "es", "gl": "es"}, "")
    p = seeds.plan(bedding(tmp_path), values=["Lino"])
    assert {x["q"]: x["_reuse"] for x in p["seeds"]} == {"fundas de nórdico": "nordicas", "fundas de almohada": None,
                                                         "juego de fundas de nórdico": None, "fundas de nórdico de lino": None}
