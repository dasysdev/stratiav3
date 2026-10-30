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


def a_pass(tmp_path, monkeypatch, blocks: dict, results: dict, model: dict) -> dict:
    """A catalog, the classified sets and an accepting control, all under tmp_path. The control's decision."""
    cat = tmp_path / "catalog"
    (cat / "cat").mkdir(parents=True)
    for name, b in blocks.items():
        (cat / "cat" / f"{name}.json").write_text(json.dumps(b), encoding="utf-8")
    monkeypatch.setattr(catalog, "CAT_DIR", cat / "cat")
    monkeypatch.setattr(catalog, "RUNTIME_DIR", cat / "runtime")
    monkeypatch.setattr(catalog, "PAA_QUESTIONS", cat / "paa-questions.json")
    monkeypatch.setattr(catalog, "load_rules", lambda: {})
    monkeypatch.setattr(catalog, "trait_index", lambda: ({}, {}))
    monkeypatch.setattr(control, "ACCEPTED", tmp_path / "accepted.json")
    monkeypatch.setattr(control, "case_ids", lambda: sorted(results))
    monkeypatch.setattr(paa_compile, "MERGES", tmp_path / "merges.json")
    monkeypatch.setattr(paa_compile, "model_of", lambda result: model)
    decision = {"accepted": True, "against": None, "worse": []}
    monkeypatch.setattr(control, "run", lambda ids: (tmp_path, {"decision": decision, "total": TOTAL,
                                                                "sets": {s: {"summary": TOTAL} for s in results}}))
    for set_id, result in results.items():
        sets = tmp_path / "var" / "sets" / set_id
        sets.mkdir(parents=True)
        (sets / "classified.json").write_text(json.dumps(result), encoding="utf-8")
    return decision


def test_run_writes_blocks_register_and_accepted_pass(tmp_path, monkeypatch):
    cat = tmp_path / "catalog"
    decision = a_pass(tmp_path, monkeypatch, {"calzado": block()}, {"botas": RESULT}, MODEL)

    passed = paa_compile.run(paa_compile.classified_ids())
    saved = json.loads((cat / "cat" / "calzado.json").read_text(encoding="utf-8"))
    assert saved["version"] == "4" and len(saved["requirements"]) == 3 and passed["touched"] == ["cat.calzado"]
    texts = json.loads((cat / "paa-questions.json").read_text(encoding="utf-8"))
    assert texts == {"paa-q:botas:como-saber": {"q": "¿Cómo saber si es cuero?", "set": "botas", "at": "2026-10-27"},
                     "paa-q:botas:se-estira": {"q": "¿Se estira el calzado de cuero?", "set": "botas", "at": "2026-10-27"}}
    accepted = json.loads((tmp_path / "accepted.json").read_text(encoding="utf-8"))
    assert accepted["total"] == TOTAL and "botas" in accepted["entered"]
    again = paa_compile.run(["botas"])   # nothing new: the accepted pass keeps what entered with it
    assert again["touched"] == [] and json.loads((tmp_path / "accepted.json").read_text(encoding="utf-8")) == accepted

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


# Possible duplicates between sets (T-110): the same trait, in the same block or in a block and one of its ancestors

def home_blocks() -> dict:
    tree = {"casa": "hg-15", "cama": "hg-15-1", "sabanas": "hg-15-1-2", "colchon": "hg-15-1-6", "almohada": "hg-15-1-8"}
    return {name: {"id": f"cat.{name}", "shopify": node, "version": "1", "status": "compilado", "requirements": []}
            for name, node in tree.items()}


def classified(set_id: str, *candidates) -> dict:
    """A classified set: each candidate (N, question, trait, blocks, slug of its PAA question)."""
    return {"set": set_id, "questions_at": "2026-10-30", "model": "demand-engine/var/runs/r/x.model.md",
            "questions": [{"n": i, "q": f"¿{slug}?", "source": f"paa-q:{set_id}:{slug}"}
                          for i, (_, _, _, _, slug) in enumerate(candidates, 1)],
            "candidates": [{"id": n, "question": q, "trait": trait, "blocks": blocks, "vote": "principal",
                            "rationale": "Pregunta.", "sources": [f"paa-q:{set_id}:{slug}"]}
                           for n, q, trait, blocks, slug in candidates],
            "contributions": []}


SETS = {
    "mantas": classified("mantas", ("N1", "¿De qué variedad es la fibra?", "material", ["cat.casa"], "merino")),
    "sabanas": classified("sabanas", ("N1", "¿Qué tacto tiene el tejido?", "sensorial", ["cat.sabanas", "cat.almohada"],
                                      "suaves"),
                          ("N5", "¿Qué variedad de fibra es?", "material", ["cat.casa"], "seda")),
    "fundas": classified("fundas", ("N3", "¿Qué tacto tiene la funda?", "sensorial", ["cat.cama"], "hotel"),
                         ("N4", "¿Para qué uso es?", "uso", ["cat.casa"], "uso"),
                         ("N5", "¿Para qué temporada es?", "uso", ["cat.casa"], "temporada")),
    "cubre": classified("cubre", ("N2", "¿Qué tacto tiene la superficie?", "sensorial", ["cat.colchon"], "fresco"),
                        ("N3", "¿Para qué uso es?", "uso", ["cat.otro"], "otro")),
}
FIBRE = ["mantas:N1@cat.casa", "sabanas:N5@cat.casa"]
FEEL = ["fundas:N3@cat.cama", "cubre:N2@cat.colchon", "sabanas:N1@cat.almohada", "sabanas:N1@cat.sabanas"]


def groups(decisions=()) -> list:
    blocks = {b["id"]: b for b in home_blocks().values()}
    items = {s: paa_compile.entries(r, {}) for s, r in SETS.items()}
    return paa_compile.review(paa_compile.possible(items, blocks, SETS), list(decisions), blocks)


def test_possible_duplicates_by_trait_and_tree():
    found = groups()
    # the same set is not compared (fundas N4 and N5); siblings are not related (cubre N2 and sabanas N1), but the
    # pairs that share an entry make one group; a block outside the catalog does not enter (cubre N3)
    assert [g["entries"] for g in found] == [FIBRE, FEEL]
    assert [g["trait"] for g in found] == ["material", "sensorial"]
    assert found[0]["detail"]["sabanas:N5@cat.casa"] == {"block": "cat.casa", "question": "¿Qué variedad de fibra es?",
                                                         "paa": ["¿seda?"]}
    assert all(g["problems"] == ["sin decisión"] for g in found)


def decided(entries, same, keep=None, reason="Prueba del mismo hecho."):
    return {"entries": entries, "same": same, "keep": keep, "reason": reason}


@pytest.mark.parametrize("decision,problem", [
    (decided(FEEL, True, "sabanas:N1@cat.sabanas"), "no está en el bloque más alto"),
    (decided(FEEL, True, "cubre:N9@cat.colchon"), "«keep» no es una entrada"),
    (decided(FEEL, True, "fundas:N3@cat.cama", reason=""), "sin motivo"),
    (decided(FEEL, None), "sin decisión"),
    (decided(FEEL[:3], False), "sin decisión: sabanas:N1@cat.sabanas"),
    (decided(FEEL + ["mantas:N1@cat.casa"], False), "entradas fuera del grupo: mantas:N1@cat.casa"),
])
def test_a_wrong_or_partial_decision_is_pending(decision, problem):
    feel = groups([decision])[1]
    assert any(problem in p for p in feel["problems"]), feel["problems"]


def test_a_group_of_several_facts_is_split_in_decisions():
    split = [decided(FEEL[:1] + FEEL[2:], True, "fundas:N3@cat.cama"), decided(FEEL[1:2], False, reason="Otro hecho.")]
    assert groups(split)[1]["problems"] == []
    assert any("en dos decisiones" in p for p in groups(split + [decided(FEEL[1:2], False)])[1]["problems"])


def test_merged_entries_enter_as_one_requirement_in_the_highest_block():
    decisions = [decided(FIBRE, True, "mantas:N1@cat.casa"),
                 decided(FEEL[:1] + FEEL[2:], True, "fundas:N3@cat.cama"), decided(FEEL[1:2], False)]
    blocks = {b["id"]: b for b in home_blocks().values()}
    items = {s: paa_compile.entries(r, {}) for s, r in SETS.items()}
    found = paa_compile.review(paa_compile.possible(items, blocks, SETS), decisions, blocks)
    paa_compile.merge(items, found)
    done = {s: paa_compile.apply(blocks, s, items[s], {}, {}, {}) for s in SETS}
    casa = {r["question"]: r for r in blocks["cat.casa"]["requirements"]}
    fibre = casa["¿De qué variedad es la fibra?"]
    assert "¿Qué variedad de fibra es?" not in casa
    assert fibre["sources"] == ["paa-q:mantas:merino", "paa-q:sabanas:seda"]
    assert fibre["rationale"].endswith("conjunto mantas (N1; fundido con sabanas:N5@cat.casa; D-178).")
    assert done["sabanas"]["merged"] == ["N1@cat.sabanas: fundido en fundas:N3@cat.cama",
                                         "N1@cat.almohada: fundido en fundas:N3@cat.cama",
                                         "N5@cat.casa: fundido en mantas:N1@cat.casa"]
    assert blocks["cat.sabanas"]["requirements"] == [] and blocks["cat.almohada"]["requirements"] == []
    [feel] = blocks["cat.cama"]["requirements"]
    assert feel["sources"] == ["paa-q:fundas:hotel", "paa-q:sabanas:suaves"]
    assert [r["sources"] for r in blocks["cat.colchon"]["requirements"]] == [["paa-q:cubre:fresco"]]  # not the same fact
    # the same set in the same block still enters twice (fundas N4 and N5): they are not compared
    assert {"¿Para qué uso es?", "¿Para qué temporada es?"} <= set(casa)


def test_different_facts_both_enter():
    blocks = {b["id"]: b for b in home_blocks().values()}
    items = {s: paa_compile.entries(r, {}) for s, r in SETS.items()}
    found = paa_compile.review(paa_compile.possible(items, blocks, SETS), [decided(FIBRE, False)], blocks)
    paa_compile.merge(items, found)
    for s in ("mantas", "sabanas"):
        paa_compile.apply(blocks, s, items[s], {}, {}, {})
    assert len(blocks["cat.casa"]["requirements"]) == 2


def test_run_writes_nothing_until_every_group_has_a_decision(tmp_path, monkeypatch):
    a_pass(tmp_path, monkeypatch, home_blocks(), SETS, {})
    before = {p.name: p.read_text(encoding="utf-8") for p in (tmp_path / "catalog" / "cat").glob("*.json")}
    ran = []
    real = control.run
    monkeypatch.setattr(control, "run", lambda ids: ran.append(ids) or real(ids))

    passed = paa_compile.run(paa_compile.classified_ids())
    assert [g["entries"] for g in paa_compile.pending(passed["duplicates"])] == [FIBRE, FEEL]
    assert ran == [] and "decision" not in passed  # the control does not run
    assert {p.name: p.read_text(encoding="utf-8") for p in (tmp_path / "catalog" / "cat").glob("*.json")} == before
    assert not (tmp_path / "accepted.json").exists() and not (tmp_path / "catalog" / "paa-questions.json").exists()
    draft = json.loads(paa_compile.draft_path().read_text(encoding="utf-8"))
    assert [(g["entries"], g["same"], g["keep"]) for g in draft["groups"]] == [(FIBRE, None, None), (FEEL, None, None)]

    (tmp_path / "merges.json").write_text(json.dumps({"groups": [
        decided(FIBRE, True, "sabanas:N5@cat.casa"), decided(FEEL, False, reason="Tacto de piezas distintas.")]}),
        encoding="utf-8")
    passed = paa_compile.run(paa_compile.classified_ids())
    assert len(ran) == 1 and passed["decision"]["accepted"] and "cat.casa" in passed["touched"]
    casa = json.loads((tmp_path / "catalog" / "cat" / "casa.json").read_text(encoding="utf-8"))
    fibre = [r for r in casa["requirements"] if r["trait"] == "material"]
    assert [(r["question"], r["sources"]) for r in fibre] == [("¿Qué variedad de fibra es?",
                                                              ["paa-q:mantas:merino", "paa-q:sabanas:seda"])]
    texts = json.loads((tmp_path / "catalog" / "paa-questions.json").read_text(encoding="utf-8"))
    assert {"paa-q:mantas:merino", "paa-q:sabanas:seda"} <= set(texts)
    accepted = json.loads((tmp_path / "accepted.json").read_text(encoding="utf-8"))
    assert accepted["entered"]["mantas"]["merged"] == ["N1@cat.casa: fundido en sabanas:N5@cat.casa"]
    assert json.loads(paa_compile.draft_path().read_text(encoding="utf-8"))["groups"] == []


def test_cli_lists_the_groups_and_stops_without_a_decision(tmp_path, monkeypatch, capsys):
    from demand_engine.paa.__main__ import main
    a_pass(tmp_path, monkeypatch, home_blocks(), SETS, {})
    with pytest.raises(SystemExit, match="2 posibles duplicados sin decisión válida; no se escribe nada"):
        main(["compile", "--duplicates"])
    out = capsys.readouterr().out
    assert "2 grupos, 2 sin decisión válida" in out and "   mantas:N1@cat.casa  ¿De qué variedad es la fibra?" in out
    with pytest.raises(SystemExit):
        main(["compile"])
    assert not (tmp_path / "accepted.json").exists()
    (tmp_path / "merges.json").write_text(json.dumps({"groups": [
        decided(FIBRE, True, "mantas:N1@cat.casa"), decided(FEEL, False)]}), encoding="utf-8")
    main(["compile", "--duplicates"])
    assert "= mismo hecho, queda mantas:N1@cat.casa" in capsys.readouterr().out
    main(["compile"])
    out = capsys.readouterr().out
    assert "2 grupos · fusiones: 1" in out and "  = N5@cat.casa: fundido en mantas:N1@cat.casa" in out
