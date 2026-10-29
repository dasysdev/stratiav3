"""The PAA pass into the catalog (D-178), its gate (D-180) and the revisions that taxo reads (D-179, D-213)."""
import copy
import json

import pytest

from demand_engine.demand import catalog, model, train
from demand_engine.paa import compile as paa_compile
from demand_engine.paa import control

SECTION = {"expected": 2, "found": 2, "agree": 2, "not_expected": 1, "regressions": 0, "new": 0}
TOTAL = {"out_expected": 3, "out_found": 3, "out_new": 0, **{k: dict(SECTION) for k in control.SECTIONS}}


def test_first_pass_is_accepted():
    assert control.decide(None, TOTAL) == {"accepted": True, "against": None, "worse": []}


def test_same_or_better_is_accepted():
    better = copy.deepcopy(TOTAL)
    better["candidates"]["found"], better["candidates"]["new"] = 3, 5  # new elements do not decide
    assert control.decide({"at": "ayer", "total": TOTAL}, better)["accepted"]


@pytest.mark.parametrize("section,key,value", [("criteria", "found", 1), ("revisions", "regressions", 1),
                                               (None, "out_found", 2)])
def test_worse_section_is_rejected(section, key, value):
    worse = copy.deepcopy(TOTAL)
    (worse[section] if section else worse)[key] = value
    d = control.decide({"at": "ayer", "total": TOTAL}, worse)
    assert not d["accepted"] and d["against"] == "ayer" and len(d["worse"]) == 1


def block():
    return {"id": "cat.calzado", "shopify": "aa-8", "version": "3", "status": "compilado", "requirements": [
        {"id": "cat.calzado/04", "question": "¿De qué material es el corte?", "trait": "composicion", "origin": "referencias",
         "sources": ["shopify-attr:upper-material"], "resolving_info": [
             {"contribution": "material del corte", "component": "material", "origin": "referencias",
              "support": ["shopify-attr:upper-material"]}]}],
        "excluded": [{"id": "cat.calzado/05", "source": "x"}]}


RESULT = {
    "set": "botas", "questions_at": "2026-10-27", "model": "demand-engine/var/runs/r/bota.model.md",
    "questions": [{"n": 1, "q": "¿Se estira el calzado de cuero?", "source": "paa-q:botas:se-estira", "answered_by": []},
                  {"n": 2, "q": "¿Cómo saber si es cuero?", "source": "paa-q:botas:como-saber", "answered_by": ["inf/01"]},
                  {"n": 3, "q": "¿Abrigan?", "source": "paa-q:botas:abrigan", "answered_by": ["inf/02"]}],
    "proposed_traits": [{"name": "sensorial", "definition": "Tipo de tacto."}],
    "candidates": [{"id": "N1", "question": "¿Se da de sí el corte con el uso?", "blocks": ["cat.calzado", "cat.otro"],
                    "mirrors": "inf/02", "trait": "sensorial", "vote": "complementario", "applicability": "universal",
                    "rationale": "Pregunta 1.", "sources": ["paa-q:botas:se-estira"],
                    "resolving_info": [{"contribution": "declaración de si el corte cede", "component": "adaptación"}]}],
    "contributions": [{"target": "cat.calzado/04", "contribution": "piel natural o sintética", "component": "material",
                       "kind": "precisión", "questions": [2]},
                      {"target": "gen/04", "contribution": "precio", "component": "precio", "kind": "precisión",
                       "questions": [1]}],
    "revisions": [{"id": "R1", "target": "cat.calzado/04", "action": "reformular", "proposal": "Ampliar.", "questions": [2]},
                  {"id": "R2", "target": "cat.calzado/99", "action": "separar", "proposal": "Partir.", "questions": []}],
}
MODEL = {"inferred": [
    {"id": "inf/01", "block": "cat.calzado", "question": "¿Tiene forro?", "trait": "construccion", "vote": "principal",
     "resolving_info": [{"contribution": "forro declarado", "component": "forro", "origin": "inferida", "support": []}]},
    {"id": "inf/02", "block": "cat.calzado", "question": "¿Abriga?", "trait": "prestacion", "vote": "principal"}]}


def compiled():
    blocks = {"cat.calzado": block()}
    done = paa_compile.apply(blocks, "botas", paa_compile.entries(RESULT, MODEL), {}, {}, {})
    return blocks, done


def test_candidates_inferred_and_contributions_enter():
    blocks, done = compiled()
    reqs = {r["id"]: r for r in blocks["cat.calzado"]["requirements"]}
    n1, inf = reqs["cat.calzado/06"], reqs["cat.calzado/07"]  # 05 is used by an excluded one
    assert n1["question"] == "¿Se da de sí el corte con el uso?" and n1["origin"] == "paa"
    assert n1["sources"] == ["paa-q:botas:se-estira"] and n1["seed_importance"] == "complementario"
    assert n1["resolving_info"] == [{"contribution": "declaración de si el corte cede", "component": "adaptación",
                                     "origin": "paa", "support": ["paa-q:botas:se-estira"]}]
    # the confirmed inferred question passes to origin «paa», with the questions that answer it (D-097)
    assert inf["question"] == "¿Tiene forro?" and inf["origin"] == "paa" and inf["sources"] == ["paa-q:botas:como-saber"]
    assert inf["resolving_info"][0]["origin"] == "paa"
    assert not any(r["question"] == "¿Abriga?" for r in reqs.values())  # revised by N1 (mirrors): N1 enters
    assert reqs["cat.calzado/04"]["resolving_info"][-1] == {
        "contribution": "piel natural o sintética", "component": "material", "kind": "precisión", "origin": "paa",
        "support": ["paa-q:botas:como-saber"]}
    assert blocks["cat.calzado"]["proposed_traits"] == [{"name": "sensorial", "definition": "Tipo de tacto."}]
    assert done["touched"] == {"cat.calzado"}
    assert any("cat.otro" in s for s in done["skipped"]) and any("gen/04" in s for s in done["skipped"])


def test_nothing_enters_twice():
    blocks, _ = compiled()
    again = paa_compile.apply(blocks, "botas", paa_compile.entries(RESULT, MODEL), {}, {}, {})
    assert again["added"] == [] and again["touched"] == set()
    assert len(blocks["cat.calzado"]["requirements"]) == 3


def test_catalog_check_wants_the_text_of_each_question():
    blocks, _ = compiled()
    b = blocks["cat.calzado"]
    for r in b["requirements"]:
        r["importance"] = "principal"
    assert model.block_problems(b, {"composicion", "construccion", "sensorial"}) == []
    texts = {"paa-q:botas:se-estira": {"q": "¿Se estira el calzado de cuero?"}}
    problems = model.paa_question_problems([b], texts)
    assert problems and all("paa-q:botas:como-saber" in p for p in problems)
    assert model.paa_question_problems([b], {**texts, "paa-q:botas:como-saber": {"q": "¿Cómo saber si es cuero?"}}) == []


def test_run_writes_blocks_register_and_accepted_pass(tmp_path, monkeypatch):
    cat = tmp_path / "catalog"
    (cat / "cat").mkdir(parents=True)
    (cat / "cat" / "calzado.json").write_text(json.dumps(block()), encoding="utf-8")
    monkeypatch.setattr(catalog, "CAT_DIR", cat / "cat")
    monkeypatch.setattr(catalog, "RUNTIME_DIR", cat / "runtime")
    monkeypatch.setattr(catalog, "PAA_QUESTIONS", cat / "paa-questions.json")
    monkeypatch.setattr(catalog, "load_rules", lambda: {})
    monkeypatch.setattr(catalog, "trait_index", lambda: ({}, {}))
    monkeypatch.setattr(control, "ACCEPTED", tmp_path / "accepted.json")
    monkeypatch.setattr(control, "case_ids", lambda: ["botas"])
    monkeypatch.setattr(paa_compile, "model_of", lambda result: MODEL)
    decision = {"accepted": True, "against": None, "worse": []}
    monkeypatch.setattr(control, "run", lambda ids: (tmp_path, {"decision": decision, "total": TOTAL,
                                                                "sets": {"botas": {"summary": TOTAL}}}))
    sets = tmp_path / "var" / "sets" / "botas"
    sets.mkdir(parents=True)
    (sets / "classified.json").write_text(json.dumps(RESULT), encoding="utf-8")

    passed = paa_compile.run(paa_compile.classified_ids())
    saved = json.loads((cat / "cat" / "calzado.json").read_text(encoding="utf-8"))
    assert saved["version"] == "4" and len(saved["requirements"]) == 3 and passed["touched"] == ["cat.calzado"]
    texts = json.loads((cat / "paa-questions.json").read_text(encoding="utf-8"))
    assert texts == {"paa-q:botas:como-saber": {"q": "¿Cómo saber si es cuero?", "set": "botas", "at": "2026-10-27"},
                     "paa-q:botas:se-estira": {"q": "¿Se estira el calzado de cuero?", "set": "botas", "at": "2026-10-27"}}
    accepted = json.loads((tmp_path / "accepted.json").read_text(encoding="utf-8"))
    assert accepted["total"] == TOTAL and "botas" in accepted["entered"]

    decision.update(accepted=False, against="ayer", worse=["criterios: esperados encontrados 1 (antes 2)"])
    assert paa_compile.run(["botas"])["decision"]["accepted"] is False
    assert json.loads((cat / "cat" / "calzado.json").read_text(encoding="utf-8"))["version"] == "4"


def test_taxo_compilation_reads_the_revisions(tmp_path, monkeypatch):
    sets = tmp_path / "sets" / "botas"
    sets.mkdir(parents=True)
    (sets / "classified.json").write_text(json.dumps(RESULT), encoding="utf-8")
    monkeypatch.setattr(train, "PAA_SETS", tmp_path / "sets")
    current, stale = train.paa_revisions({"cat.calzado": block()})
    assert [(r["action"], r["target"]) for r in current] == [("reformular", "cat.calzado/04")]
    assert current[0]["questions"] == ["¿Cómo saber si es cuero?"]
    assert [(r["action"], r["target"]) for r in stale] == [("separar", "cat.calzado/99")]
    lines = "\n".join(train.revisions_section({"cat.calzado": block()}))
    assert "reformular cat.calzado/04" in lines and "separar cat.calzado/99 (botas)" in lines
