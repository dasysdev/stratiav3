"""A classification against its control case, by content and not by ids (no browser)."""
import json

import pytest

from demand_engine.paa import control
from demand_engine.paa.store import SeedSet, StoreError

QUESTIONS = ["¿Qué calzado recomiendan los podólogos?", "¿Qué zapatillas están de moda?",
             "¿Cuál es la mejor zapatilla de casa?", "¿Se lavan en lavadora?", "¿Dónde comprar zapatillas de lana?"]


def q(n, perimeter="dentro", criterion=None):
    return {"n": n, "q": QUESTIONS[n - 1], "perimeter": perimeter, "criterion": criterion}


CASE = {
    "set": "s", "perimeter": {"out": [QUESTIONS[0]], "expected": True},
    "criteria": [{"name": "Moda", "verdict": "no-genera", "expected": True, "questions": [QUESTIONS[1]]},
                 {"name": "El mejor", "verdict": "cubierto", "intermediate": True, "expected": True,
                  "questions": [QUESTIONS[2]]},
                 {"name": "Salud del pie", "verdict": "genera", "expected": False, "questions": [QUESTIONS[0]]}],
    "candidates": [{"question": "¿Se puede lavar a máquina?", "blocks": ["cat.pantuflas"], "trait": "uso",
                    "expected": True, "questions": [QUESTIONS[3]]},
                   {"question": "¿Para qué afecciones del pie está indicado?", "blocks": ["cat.calzado"],
                    "trait": "uso", "expected": False, "questions": [QUESTIONS[0]]}],
    "revisions": [{"target": "cat.pantuflas/02", "action": "reformular", "summary": "x", "expected": True}],
    "contributions": [{"target": "cat.pantuflas/04", "contribution": "denominación legal de la fibra",
                       "kind": "precisión", "expected": True},
                      {"target": "cat.calzado/04", "contribution": "certificación de piel", "kind": "sustento",
                       "expected": False}],
}


def result(**changes):
    r = {"rulebook": "classifier/paa.md", "rulebook_version": "classifier/paa.md v5", "at": "hoy",
         "questions": [q(1, "fuera"), q(2, criterion="m"), q(3, criterion="b"), q(4), q(5)],
         "criteria": [{"id": "m", "name": "Tendencia", "verdict": "no-genera"},
                      {"id": "b", "name": "Preferencia", "verdict": "cubierto", "intermediate": True}],
         "candidates": [{"id": "N7", "question": "¿Admite lavado a máquina?", "blocks": ["cat.pantuflas"],
                         "trait": "uso", "support": [4]}],
         "revisions": [{"id": "R9", "target": "cat.pantuflas/02", "action": "reformular"}],
         "contributions": [{"target": "cat.pantuflas/04", "contribution": "nombre legal de cada fibra",
                            "kind": "precisión"}]}
    r.update(changes)
    return r


@pytest.fixture
def cases(tmp_path, paa_dirs, monkeypatch):
    monkeypatch.setattr(control, "CASES", tmp_path / "cases")
    (paa_dirs / "sets" / "s.json").write_text(json.dumps({"class": "Pantuflas", "seeds": []}), encoding="utf-8")
    (tmp_path / "cases").mkdir()
    (tmp_path / "cases" / "s.json").write_text(json.dumps(CASE), encoding="utf-8")
    SeedSet("s").dir.mkdir(parents=True)


def write(res):
    (SeedSet("s").dir / "classified.json").write_text(json.dumps(res), encoding="utf-8")


def test_a_classification_like_the_case_agrees_whatever_its_ids(cases):
    write(result())
    s = control.run(["s"])[1]["sets"]["s"]["summary"]
    assert (s["out_found"], s["out_expected"], s["out_new"]) == (1, 1, 0)
    for section in control.SECTIONS:
        assert s[section]["found"] == s[section]["expected"] == s[section]["agree"]
        assert s[section]["regressions"] == 0 and s[section]["new"] == 0


def test_misses_differences_regressions_and_new_ones(cases):
    res = result()
    res["questions"][0]["perimeter"] = "dentro"                       # a neighbour back inside
    res["questions"][4]["perimeter"] = "fuera"                        # out, and the case does not say so
    res["questions"][0]["criterion"] = "salud"
    res["criteria"][1]["verdict"] = "no-genera"                       # «el mejor» is intermediate (D-142)
    res["criteria"] += [{"id": "salud", "name": "Pies", "verdict": "genera"},
                        {"id": "c", "name": "Cubierto", "verdict": "cubierto"}]
    res["candidates"][0]["blocks"] = ["cat.calzado"]
    res["candidates"].append({"id": "N1", "question": "¿Para qué afecciones está indicado?", "blocks": ["cat.calzado"],
                              "trait": "uso", "support": [1]})
    res["revisions"] = [{"id": "R1", "target": "cat.pantuflas/02", "action": "separar"}]
    res["contributions"].append({"target": "cat.calzado/04", "contribution": "certificado de piel auténtica",
                                 "kind": "sustento"})
    write(res)
    out, data = control.run(["s"])
    s = data["sets"]["s"]["summary"]
    assert (s["out_found"], s["out_new"]) == (0, 1)
    assert s["criteria"]["found"] == 2 and s["criteria"]["agree"] == 1 and s["criteria"]["regressions"] == 1
    assert s["criteria"]["new"] == 0                                  # a covered criterion is not new
    assert s["candidates"]["agree"] == 0 and s["candidates"]["regressions"] == 1
    assert s["revisions"]["found"] == 0 and s["revisions"]["new"] == 1
    assert s["contributions"]["regressions"] == 1
    md = (out / "report.md").read_text(encoding="utf-8")
    assert "- Debían quedar fuera y están dentro: «¿Qué calzado recomiendan los podólogos?»" in md
    assert "- Difiere (b: veredicto no-genera (esperado cubierto); no intermedio): El mejor" not in md
    assert "- Difiere (b: veredicto no-genera (esperado cubierto)): El mejor" in md
    assert "- Regresión (N1): ¿Para qué afecciones del pie está indicado?" in md
    assert "- Difiere (N7: bloques cat.calzado): ¿Se puede lavar a máquina?" in md
    assert "- Falta: reformular cat.pantuflas/02" in md and "- Nuevo: separar cat.pantuflas/02" in md
    assert "| s | classifier/paa.md v5 |" in md


def test_a_candidate_without_shared_questions_matches_by_its_wording(cases):
    res = result()
    res["candidates"][0].update(question="¿Se puede lavar a máquina o a mano?", support=[5])
    write(res)
    assert control.run(["s"])[1]["sets"]["s"]["summary"]["candidates"]["agree"] == 1


def test_control_needs_the_case_and_the_classification(cases):
    with pytest.raises(StoreError):
        control.run(["s"])
    with pytest.raises(StoreError):
        control.run(["otro"])
