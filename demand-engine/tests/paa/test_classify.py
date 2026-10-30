"""Classification of the questions of a set: input, check of the agent's output, result and contrasts (no browser)."""
import json

import pytest

from demand_engine.paa import classify
from demand_engine.paa.store import SeedSet, StoreError

QUESTIONS = ["¿Qué es una sábana encimera?", "¿Se arruga mucho el lino?", "¿Qué se arruga más, satén o percal?",
             "¿Cuál es la mejor marca de sábanas?", "¿Qué almohada es mejor?", "¿Cuánto mide una encimera de 150?",
             "¿Cada cuánto se cambian las sábanas?", "¿La microfibra es plástico?"]
OK = {"ok": True, "why": "porque sí"}
NO = {"ok": False, "why": "porque no"}
LIST_SOURCES = ["amazon-ptd-prop:PILLOWCASE.special_feature=Resistente a las arrugas",
                "amazon-ptd-prop:PILLOWCASE.special_feature=Resistente al encogimiento"]


CURRENT = {"cat.ropa-de-casa/01": {
    "hints": [{"id": "PV-3", "key": "fuente", "pista": "La composición usa el nombre legal de cada fibra.",
               "propiedad": ["P09"], "ac": ["Precisión"]}],
    "comparison": {"mark": "sí", "reason": "Se elige por la fibra."}},
    "cat.ropa-de-cama/02": {"hints": [], "comparison": {"mark": "sí", "reason": "dudoso"}}}


SPECS = {"esp.juego": {"id": "esp.juego", "name": "juego", "order": "juego", "trigger": "varias piezas",
                        "status": "compilado", "anchors": [], "requirements": [
                            {"id": "esp.juego/01", "question": "¿Qué piezas incluye?", "trait": "contenido"}]},
         "esp.otra": {"id": "esp.otra", "name": "de otra rama", "order": "uso", "trigger": "t", "status": "compilado",
                      "anchors": ["zz-1"], "requirements": []}}


@pytest.fixture
def seedset(paa_dirs, monkeypatch):
    monkeypatch.setattr(classify, "current", lambda: CURRENT)      # what the catalog has today, not the real one
    monkeypatch.setattr(classify.demand_catalog, "load_specializations", lambda: SPECS)
    model = {"key": {"model": ["gen@0.5", "cat.ropa-de-cama@2", "cat.sabanas@2"]},
             "general": [{"id": "gen", "requirements": [{"id": "gen/01", "question": "¿Qué es el producto?",
                                                         "applicability": "universal", "origin": "normativa"}]}],
             "blocks": [{"id": "cat.ropa-de-cama", "name": "Ropa de cama", "type": "categoría", "requirements": [
                            {"id": "cat.ropa-de-cama/02", "question": "¿Qué medidas tiene?", "trait": "medida"}]},
                        {"id": "cat.ropa-de-casa", "name": "Ropa de casa", "type": "categoría", "requirements": [
                            {"id": "cat.ropa-de-casa/01", "question": "¿De qué materiales está hecho?", "trait": "material",
                             "resolving_info": [{"contribution": "composición en fibras"}]}]},
                        {"id": "cat.sabanas", "name": "Sábanas", "type": "categoría", "requirements": []},
                        {"id": "cat.fundas-de-almohada", "name": "Fundas", "type": "categoría", "requirements": [
                            {"id": "cat.fundas-de-almohada/06", "question": "¿Qué resistencia tiene (arrugas…)?",
                             "trait": "prestacion", "sources": LIST_SOURCES}]}],
             "inferred": [{"id": "inf/01", "block": "cat.sabanas", "question": "¿Qué abrigo da?", "trait": "prestacion"}]}
    (paa_dirs / "m.model.json").write_text(json.dumps(model), encoding="utf-8")
    (paa_dirs / "sets" / "s.json").write_text(json.dumps({"class": "Sábanas", "model": str(paa_dirs / "m.model.md"),
                                                          "seeds": [{"q": "sábanas"}]}), encoding="utf-8")
    s = SeedSet("s")
    s.dir.mkdir(parents=True)
    (s.dir / "questions.json").write_text(json.dumps({"set": "s", "at": "2026-10-27T10:00:00+01:00", "questions": [
        {"q": q, "seeds": [{"query": "sábanas de lino" if "lino" in q else "sábanas", "group": "núcleo",
                            "position": i, "via": None, "at": "x"}]} for i, q in enumerate(QUESTIONS, 1)]}),
        encoding="utf-8")
    return s


def entry(n, perimeter="dentro", obj="clase", answered=(), criterion=None, candidate=None, fails=None):
    return {"n": n, "perimeter": perimeter, "object": obj, "answered_by": list(answered), "criterion": criterion,
            "candidate": candidate, "fails": fails}


def good_output():
    return {
        "questions": [
            entry(1, answered=["gen/01"]),
            entry(2, criterion="arrugas", candidate="N1"),
            entry(3, obj="valorativa", criterion="arrugas"),
            entry(4, obj="marca", criterion="marca"),
            entry(5, perimeter="fuera", obj=None),
            entry(6, answered=["cat.ropa-de-cama/02"]),
            entry(7, fails="C2"),
            entry(8, answered=["cat.ropa-de-casa/01"])],
        "criteria": [
            {"id": "arrugas", "name": "Arrugas", "verdict": "genera", "covered_by": [], "candidates": ["N1"],
             "conditions": {"C1": OK, "C2": OK, "C3": OK, "C4": OK}},
            {"id": "marca", "name": "Marca", "verdict": "no-genera", "covered_by": [], "candidates": [],
             "conditions": {"C1": OK, "C2": OK, "C3": OK, "C4": NO}}],
        "candidates": [
            {"id": "N1", "question": "¿Qué resistencia a las arrugas tiene?", "description": "Si se arruga.",
             "blocks": ["cat.sabanas", "cat.fundas-de-almohada"], "trait": "prestacion", "vote": "complementario",
             "applicability": "universal", "from": "criterio", "conditions": {"C1": OK, "C2": OK, "C3": OK, "C4": OK},
             "rationale": "r", "resolving_info": [{"contribution": "declaración antiarrugas", "component": "arrugas"}]}],
        "revisions": [
            {"id": "R1", "target": "cat.fundas-de-almohada/06", "action": "separar", "proposal": "Sacar las arrugas.",
             "questions": [2, 3], "into": ["N1"], "tests": {"a": OK, "b": OK}}],
        "contributions": [
            {"target": "cat.ropa-de-casa/01", "contribution": "denominación legal de la fibra", "component": "materiales",
             "kind": "precisión", "questions": [8]}],
        "hints": [
            {"target": "cat.ropa-de-casa/01", "pista": "Una fibra artificial se nombra por su fibra, no por su marca.",
             "propiedad": ["P09"], "ac": ["Precisión"], "questions": [8], "note": "otra cosa que PV-3"},
            {"target": "N1", "pista": "Se compara la declaración antiarrugas, no se deduce del tejido.",
             "propiedad": ["P08"], "ac": ["Comparabilidad"], "questions": [3]}],
        "marks": [
            {"target": "N1", "mark": "sí", "reason": "Se prefiere la que menos se arruga.", "questions": [3]},
            {"target": "cat.ropa-de-cama/02", "mark": "no", "case": "b", "reason": "Filtro por la cama.",
             "questions": [6]}],
        "proposed_traits": [],
        "doubts": ["una duda"]}


def write_output(seedset, output):
    (classify.folder(seedset) / "output.json").write_text(json.dumps(output), encoding="utf-8")


def test_prepare_takes_the_catalog_of_the_class_from_the_model(seedset):
    out = classify.prepare(seedset)
    spec = json.loads((out / "input.json").read_text(encoding="utf-8"))
    assert [q["n"] for q in spec["questions"]] == list(range(1, 9))
    assert spec["questions"][1]["seeds"] == ["sábanas de lino"]
    assert {r["id"] for r in spec["catalog"]} == {"gen/01", "cat.ropa-de-cama/02", "cat.ropa-de-casa/01",
                                                  "cat.fundas-de-almohada/06", "inf/01", "esp.juego/01"}
    assert [x["id"] for x in spec["specializations"]] == ["esp.juego"]   # not one of another branch
    assert "prestacion" in spec["traits"]
    md = (out / "input.md").read_text(encoding="utf-8")
    assert "### cat.fundas-de-almohada" in md and "| 2 | ¿Se arruga mucho el lino? | sábanas de lino |" in md
    assert "special_feature=Resistente a las arrugas" in md and "composición en fibras" in md
    assert "| `cat.sabanas` | Sábanas | — |" in md                  # no Shopify id: no daughters


def test_prepare_needs_the_questions_and_the_model(seedset, paa_dirs):
    (paa_dirs / "m.model.json").unlink()
    with pytest.raises(StoreError):
        classify.prepare(seedset)


def test_a_good_output_is_correct(seedset):
    classify.prepare(seedset)
    write_output(seedset, good_output())
    assert classify.check(*classify.load(seedset)) == []


def test_check_finds_what_breaks_the_rulebook(seedset):
    classify.prepare(seedset)
    out = good_output()
    out["questions"].pop()                                       # question 8 missing
    out["questions"][6].update(fails=None)                       # class question with no outcome
    out["questions"][2].update(criterion=None)                   # value question with no criterion
    out["questions"][3].update(candidate="N1")                   # a brand question proposes nothing
    out["questions"][4].update(object="clase")                   # out of the perimeter with an object
    out["questions"][5].update(answered_by=["cat.x/01"])         # not in the catalog
    out["criteria"][1].update(verdict="genera")                  # C4 fails
    out["candidates"][0].update(blocks=["cat.otra"], trait="sabor", question="Arrugas", description="")
    out["candidates"][0]["conditions"]["C2"] = NO
    write_output(seedset, out)
    joined = "\n".join(classify.check(*classify.load(seedset)))
    assert "faltan 1 preguntas: 8" in joined
    assert "pregunta 7: una pregunta de clase lleva exactamente uno" in joined
    assert "pregunta 3: una valorativa lleva su criterio de elección" in joined
    assert "pregunta 4: una pregunta de marca no propone requisitos (D-099)" in joined
    assert "pregunta 5: fuera del perímetro no lleva objeto" in joined
    assert "pregunta 6: «cat.x/01» no está en el catálogo de la clase" in joined
    assert "criterio «marca»: «genera» exige C1–C4 cumplidas y al menos un candidato" in joined
    assert "candidato «N1»: un candidato cumple C1–C4" in joined
    assert "candidato «N1»: el bloque «cat.otra» no es de la clave" in joined
    assert "candidato «N1»: rasgo «sabor» fuera del vocabulario" in joined
    assert "candidato «N1»: la pregunta va entre ¿ y ?" in joined
    assert "candidato «N1»: falta «description» (D-092)" in joined


def test_check_of_revisions_contributions_and_ac_evidence(seedset):
    classify.prepare(seedset)
    out = good_output()
    out["revisions"][0]["tests"]["b"] = NO                       # separating needs both tests
    out["revisions"].append({"id": "R2", "target": "inf/01", "action": "reformular", "proposal": "Dos polos.",
                             "questions": [99], "tests": {"a": OK, "b": OK}})
    out["revisions"].append({"id": "R3", "target": "cat.x/09", "action": "fusionar", "proposal": "", "questions": [1]})
    out["contributions"][0].update(kind="otra", questions=[])
    out["criteria"][1].update(intermediate=True)                 # an intermediate criterion is covered
    write_output(seedset, out)
    joined = "\n".join(classify.check(*classify.load(seedset)))
    assert "revisión «R1»: «separar» exige las dos pruebas (a y b) cumplidas" in joined
    assert "revisión «R2»: la pregunta 99 no existe" in joined and "revisión «R2»: solo «separar» lleva «tests»" in joined
    assert "revisión «R3»: «cat.x/09» no está en el catálogo" in joined and "acción «fusionar» no válida" in joined
    assert "revisión «R3»: falta «proposal»" in joined
    assert "aportación 1: «kind» ha de ser precisión o sustento" in joined
    assert "aportación 1: faltan las preguntas que lo apoyan" in joined
    assert "criterio «marca»: un criterio intermedio queda «cubierto» (D-104)" in joined


def test_check_of_hints_and_marks(seedset):
    classify.prepare(seedset)
    out = good_output()
    out["ac_evidence"] = []                                      # the old step 8
    out["hints"][0].pop("note")                                  # same property and AC as PV-3, unexplained
    out["hints"].append({"target": "cat.x/01", "id": "PV-9", "pista": "Una. Dos. Tres.", "propiedad": ["P15"],
                         "ac": ["Rapidez"], "questions": []})
    out["hints"].append({"target": "cat.ropa-de-cama/02", "pista": "Mismas medidas.", "propiedad": ["P13"],
                         "ac": ["Comparabilidad"], "questions": [6]})
    out["marks"][0].update(target="cat.ropa-de-casa/01", case="a")    # N1 left without a mark; «sí» with a case
    out["marks"][1].update(questions=[])
    out["marks"].append({"target": "cat.ropa-de-cama/02", "mark": "no", "reason": "x", "questions": [6]})
    write_output(seedset, out)
    joined = "\n".join(classify.check(*classify.load(seedset)))
    assert "«ac_evidence» ya no existe (OQ-59, superada)" in joined
    assert "pista 1: misma propiedad y AC que PV-3 en «cat.ropa-de-casa/01»" in joined
    assert "pista 3: «cat.x/01» no es un requisito ni un candidato" in joined
    assert "pista 3: sin «id» ni «origen»" in joined
    assert "pista 3: la pista ha de ser una o dos frases breves (3 frases" in joined
    assert "pista 3: propiedad fuera de P06–P18 (sin P15): ['P15']" in joined
    assert "pista 3: AC no válido" in joined and "pista 3: faltan las preguntas que lo apoyan" in joined
    assert "candidato «N1»: falta su marca de comparación (D-139" in joined
    assert "marca de «cat.ropa-de-cama/02»: repetida" in joined
    assert "marca de «cat.ropa-de-casa/01»: «sí» no lleva caso" in joined
    assert "marca de «cat.ropa-de-cama/02»: faltan las preguntas que lo apoyan" in joined
    assert "marca de «cat.ropa-de-cama/02»: «no» lleva su caso (a, b o c)" in joined
    assert "marca de «cat.ropa-de-cama/02»: no se compara y lleva pistas solo de Comparabilidad: 4" in joined


def test_prepare_shows_the_current_hints_and_marks(seedset):
    md = (classify.prepare(seedset) / "input.md").read_text(encoding="utf-8")
    assert "- **cat.ropa-de-casa/01** · se compara: Se elige por la fibra." in md
    assert "  - PV-3 (fuente; P09; Precisión): La composición usa el nombre legal de cada fibra." in md


def test_a_drafted_hint_of_a_runtime_block_has_no_number(monkeypatch):
    draft = {"pista": "El abrigo se declara con su escala.", "propiedad": ["P09"], "ac": ["Precisión"],
             "origen": {"tipo": "inferida"}}   # numbered when the block is compiled (D-201)
    req = {"id": "cat.colchas/01", "question": "¿Qué abrigo da?", "hints": [draft]}
    monkeypatch.setattr(classify.catalog_hints, "requirements", lambda: [req])
    monkeypatch.setattr(classify.catalog_hints, "load_hints", lambda: {"hints": []})
    monkeypatch.setattr(classify.catalog_hints, "find", lambda r, pool: [("propia", h) for h in r["hints"]])
    assert classify.current()["cat.colchas/01"]["hints"][0]["id"] is None


def test_taking_a_value_out_needs_no_questions_and_mirrors_must_exist(seedset):
    classify.prepare(seedset)
    out = good_output()
    out["revisions"].append({"id": "R2", "target": "cat.fundas-de-almohada/06", "action": "sacar",
                             "proposal": "El dobladillo es confección."})
    out["candidates"][0]["mirrors"] = "cat.fundas-de-almohada/06"
    write_output(seedset, out)
    assert classify.check(*classify.load(seedset)) == []
    out["candidates"][0]["mirrors"] = "cat.x/06"
    out["revisions"][1]["action"] = "mover"
    write_output(seedset, out)
    joined = "\n".join(classify.check(*classify.load(seedset)))
    assert "candidato «N1»: «mirrors» (cat.x/06) no es un requisito del catálogo (D-109)" in joined
    assert "revisión «R2»: faltan las preguntas que lo apoyan" in joined


def test_a_proposed_trait_is_accepted_with_its_definition(seedset):
    classify.prepare(seedset)
    out = good_output()
    out["candidates"][0]["trait"] = "sensorial"
    write_output(seedset, out)
    assert "rasgo «sensorial» fuera del vocabulario" in "\n".join(classify.check(*classify.load(seedset)))
    out["proposed_traits"] = [{"name": "sensorial", "definition": "Tipo de tacto."}]
    write_output(seedset, out)
    assert classify.check(*classify.load(seedset)) == []


def test_covered_verdict_needs_c1_failed(seedset):
    classify.prepare(seedset)
    out = good_output()
    out["criteria"][1].update(verdict="cubierto", conditions={"C1": OK, "C2": OK, "C3": OK, "C4": NO})
    write_output(seedset, out)
    assert "criterio «marca»: «cubierto» exige C1 no cumplida y «covered_by»" in classify.check(*classify.load(seedset))


def test_report_gives_sources_and_contrasts(seedset, paa_dirs):
    classify.prepare(seedset)
    write_output(seedset, good_output())
    manual = paa_dirs / "manual.json"
    manual.write_text(json.dumps([{"q": "¿Se arruga mucho el lino?", "code": "arrugas"},
                                  {"q": "¿Qué se arruga más, satén o percal?", "code": "arrugas"},
                                  {"q": "¿Qué almohada es mejor?", "code": "OTRA"},
                                  {"q": "¿Otra que no está?", "code": "MKT"}]), encoding="utf-8")
    previous = paa_dirs / "previous.json"
    previous.write_text(json.dumps({"rulebook": "classifier/paa.md", "at": "antes", "criteria": [], "candidates": [],
                                    "questions": [{"q": QUESTIONS[0], "perimeter": "dentro", "object": "clase",
                                                   "answered_by": [], "candidate": None, "fails": "C2"}]}),
                        encoding="utf-8")
    result = classify.finish(seedset, manual, previous)
    n1 = result["candidates"][0]
    assert n1["origin"] == "paa" and n1["support"] == [2, 3]
    assert n1["sources"] == ["paa-q:s:se-arruga-mucho-el-lino", "paa-q:s:que-se-arruga-mas-saten-o-percal"]
    saved = json.loads((seedset.dir / "classified.json").read_text(encoding="utf-8"))
    assert saved["questions"][1]["seeds"][0]["query"] == "sábanas de lino" and saved["revisions"][0]["id"] == "R1"
    md = (seedset.dir / "report.md").read_text(encoding="utf-8")
    assert "| fuera | 1 |" in md and "| clase · respondida | 3 |" in md and "| clase · no genera (C2) | 1 |" in md
    assert "- Bloques: `cat.sabanas`, `cat.fundas-de-almohada`" in md and "- Sale de: criterio arrugas, revisión R1" in md
    assert "### R1 · separar `cat.fundas-de-almohada/06`" in md and "- Crea: N1 «¿Qué resistencia a las arrugas tiene?»" in md
    assert "| `cat.ropa-de-casa/01` «¿De qué materiales está hecho?» | denominación legal de la fibra |" in md
    hint = saved["hints"][0]
    assert "id" not in hint and hint["origen"] == {"tipo": "paa", "apoyo": ["paa-q:s:la-microfibra-es-plastico"]}
    assert [(m["target"], m["status"]) for m in saved["marks"]] == [("N1", "nueva"),
                                                                    ("cat.ropa-de-cama/02", "contradice: duda")]
    assert "| `cat.ropa-de-casa/01` «¿De qué materiales está hecho?» | Una fibra artificial se nombra" in md
    assert "| `cat.ropa-de-cama/02` «¿Qué medidas tiene?» | no (b) | Filtro por la cama. | contradice: duda | 1:" in md
    assert "- clase · no genera (C2) → clase · respondida (1): «¿Qué es una sábana encimera?»" in md
    assert "4 preguntas; 3 comunes" in md
    assert "| arrugas | 2 | 0 | 1 | 0 | 0 | 1 | N1 (1); criterio arrugas → N1 (1) |" in md
    assert "| OTRA | 1 | 1 | 0 | 0 | 0 | 0 | fuera (1) |" in md


def with_specialization(out):
    """Question 2 is about a specialization the catalog lacks (D-218); question 1, about one it has."""
    out["specializations"] = [{"id": "S1", "name": "de lino lavado", "order": "material", "trigger": "lino lavado"}]
    out["questions"][1]["specialization"] = "S1"
    out["questions"][0]["specialization"] = "esp.juego"
    out["candidates"][0]["blocks"] = ["S1"]
    return out


def test_a_question_goes_to_a_specialization_of_the_catalog_or_a_proposed_one(seedset):
    classify.prepare(seedset)
    write_output(seedset, with_specialization(good_output()))
    assert classify.check(*classify.load(seedset)) == []
    result = classify.finish(seedset)
    assert result["specializations"] == [{"id": "S1", "name": "de lino lavado", "order": "material",
                                          "trigger": "lino lavado", "status": "no compilada", "origin": "paa",
                                          "questions": [2]}]
    assert result["questions"][1]["specialization"] == "S1"
    md = (seedset.dir / "report.md").read_text(encoding="utf-8")
    assert "### S1 · de lino lavado (material)" in md and "«¿Se arruga mucho el lino?»" in md


def test_a_question_goes_to_a_specialization_of_the_key(seedset):
    classify.prepare(seedset)
    output = good_output()
    output["questions"][0]["specialization"] = "esp.juego"
    write_output(seedset, output)
    spec, output = classify.load(seedset)
    spec["blocks"].append({"id": "esp.juego", "name": "juego", "type": "especialización", "shopify": None})
    spec["specializations"] = [s for s in spec["specializations"] if s["id"] != "esp.juego"]
    assert classify.check(spec, output) == []


def test_check_of_specializations(seedset):
    classify.prepare(seedset)
    out = with_specialization(good_output())
    out["specializations"] += [{"id": "esp.juego", "name": "juego", "order": "forma", "trigger": ""},
                               {"id": "S2", "name": "sin preguntas", "order": "uso", "trigger": "t"}]
    out["questions"][4]["specialization"] = "S9"                 # out of the perimeter, and unknown
    write_output(seedset, out)
    problems = classify.check(*classify.load(seedset))
    for expected in ("pregunta 5: la especialización «S9» no es del catálogo",
                     "pregunta 5: una pregunta de una especialización va dentro",
                     "especialización «esp.juego»: el id de una especialización propuesta es S1",
                     "especialización «esp.juego»: ya está en el catálogo; usa su id",
                     "especialización «esp.juego»: falta «trigger»",
                     "especialización «esp.juego»: orden «forma» no válido",
                     "especialización «S2»: ninguna pregunta la lleva"):
        assert any(p.startswith(expected) for p in problems), expected


def test_report_refuses_an_output_with_problems(seedset):
    classify.prepare(seedset)
    out = good_output()
    out["questions"].pop()
    write_output(seedset, out)
    with pytest.raises(StoreError):
        classify.finish(seedset)
