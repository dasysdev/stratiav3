"""The PAA phase of an execution in its model (D-224): model assemble OUTPUT.json --paa SET adds the classification of
the set of its key as provisional, «no compilado», out of the key, and queues it; the comparison mark of each
requirement, without a default (D-126, D-139), and the version of the catalog of hints (D-138)."""
import json

import pytest

from demand_engine.demand import model as engine
from demand_engine.paa.store import StoreError

NO = {"mark": "no", "case": "b", "reason": "Un filtro."}
SI = {"mark": "sí", "reason": "Cambia de una oferta a otra."}
BLOCK = {"id": "cat.fundas", "type": "categoría", "name": "Fundas", "shopify": "zz-1", "version": "3", "status": "compilado",
         "_where": "catálogo", "requirements": [
             {"id": "cat.fundas/01", "question": "¿De qué tejido es?", "trait": "material", "entity": "producto",
              "importance": "principal", "origin": "referencias", "sources": ["shopify-attr:fabric"], "comparison": NO,
              "resolving_info": [{"contribution": "tejido", "component": "tejido", "origin": "referencias",
                                  "support": ["shopify-attr:fabric"]}]},
             {"id": "cat.fundas/02", "question": "¿Qué medidas tiene?", "trait": "medida", "entity": "producto",
              "importance": "principal", "origin": "inferida", "sources": [],
              "resolving_info": [{"contribution": "medidas", "component": "medidas", "origin": "inferida", "support": []}]},
             {"id": "cat.fundas/03", "question": "¿Para qué temporada es?", "trait": "uso", "entity": "producto",
              "importance": "principal", "origin": "paa", "sources": ["paa-q:s:temporada"],
              "resolving_info": [{"contribution": "temporada", "component": "temporada", "origin": "paa",
                                  "support": ["paa-q:s:temporada"]}]},
             {"id": "cat.fundas/04", "question": "¿Qué gramaje tiene?", "trait": "magnitud", "entity": "producto",
              "importance": "complementario", "origin": "inferida", "sources": [],
              "resolving_info": [{"contribution": "gramaje", "component": "gramaje", "origin": "inferida", "support": []}]}]}
GEN = {"version": "0.10", "blocks": [{"id": "gen", "name": "General", "version": "0.10", "requirements": [
    {"id": "gen/01", "question": "¿Qué es?", "entity": "producto", "importance": "crítico", "origin": "normativa",
     "sources": [], "comparison": SI, "resolving_info": [{"contribution": "denominación", "component": "qué es",
                                                          "origin": "marco", "support": []}]}]}]}
OUT = {"case": "funda-1", "rulebook": "v5", "url": "https://tienda.example/p-1", "declared": [], "application": [],
       "composition": {"categories": [{"shopify": "zz-1", "alias": False}]}, "specializations": [],
       "inferred": [{"block": "cat.fundas", "question": "¿Cómo se cierra?", "trait": "construccion", "vote": "principal"}],
       "votes": {f"cat.fundas/0{i}": "principal" for i in range(1, 5)},
       "trait_votes": {f"cat.fundas/0{i}": t for i, t in enumerate(("material", "medida", "uso", "magnitud"), 1)}}


@pytest.fixture
def catalog(tmp_path, monkeypatch):
    """A tiny catalog: one category block (one requirement excluded in the class by relevance), the general layer,
    the catalog of hints 0.4 and the queue in tmp."""
    monkeypatch.setattr(engine, "load_blocks", lambda: {"cat.fundas": json.loads(json.dumps(BLOCK))})
    monkeypatch.setattr(engine, "load_empty", lambda: {"zz": "catálogo"})
    monkeypatch.setattr(engine, "trait_index", lambda: ({}, {}))
    monkeypatch.setattr(engine, "load_rules", lambda: {"version": "8", "tree": {"material@zz": "principal"},
                                                       "relevance": {"cat.fundas/04@zz-1": "excluido"}})
    monkeypatch.setattr(engine, "load_gen", lambda: json.loads(json.dumps(GEN)))
    monkeypatch.setattr(engine, "load_resolving", lambda: {"requirements": {}})
    monkeypatch.setattr(engine, "load_specializations", lambda: {})
    monkeypatch.setattr(engine, "load_traits", lambda: {"vocabulary": {t: {} for t in ("material", "medida", "uso", "magnitud",
                                                                                       "construccion")}})
    monkeypatch.setattr(engine.scopes, "load_google", lambda: {"version": "0.1", "attributes": []})
    monkeypatch.setattr(engine.hints, "load_hints", lambda: {"version": "0.4", "hints": []})
    monkeypatch.setattr(engine.pages, "PAGES", tmp_path / "pages")
    monkeypatch.setattr(engine, "QUEUE", tmp_path / "queue.jsonl")
    path = tmp_path / "funda-1.json"
    path.write_text(json.dumps(OUT), encoding="utf-8")
    return path


def classified(paa_dirs, model_path, key=("gen", "cat.fundas"), questions=None, **extra):
    """The set «s» of the key, classified against the model at `model_path`."""
    (paa_dirs / "sets" / "s.json").write_text(json.dumps({"class": "Fundas", "key": list(key), "seeds": [{"q": "fundas"}]}),
                                              encoding="utf-8")
    qs = questions or [{"n": 1, "q": "¿Qué funda abriga más?", "answered_by": ["cat.fundas/01", "inf/01"]},
                       {"n": 2, "q": "¿Se mueve el relleno?", "answered_by": []},
                       {"n": 3, "q": "¿Qué funda es de verano?", "answered_by": []}]
    qs = [{**q, "source": f"paa-q:s:{q['n']}"} for q in qs]
    result = {"set": "s", "model": str(model_path.with_name("funda-1.model.md")), "at": "2026-10-30T12:00:00+01:00",
              "rulebook_version": "classifier/paa.md v8", "questions": qs,
              "candidates": [{"id": "N1", "question": "¿Tiene sujeción interior?", "blocks": ["cat.fundas", "cat.otra"],
                              "trait": "construccion", "vote": "complementario", "applicability": "universal",
                              "description": "Si fija el relleno.", "rationale": "Pregunta 2.", "sources": ["paa-q:s:2"],
                              "resolving_info": [{"contribution": "sujeción interior", "component": "si la tiene"}]},
                             {"id": "N2", "question": "¿Para qué temporada es?", "blocks": ["cat.fundas"], "trait": "uso",
                              "vote": "principal", "sources": ["paa-q:s:temporada"], "resolving_info": []}],
              "contributions": [{"target": "cat.fundas/02", "contribution": "medida del relleno", "component": "medidas",
                                 "kind": "precisión", "questions": [1]},
                                {"target": "cat.fundas/02", "contribution": "Medidas", "component": "medidas",
                                 "kind": "precisión", "questions": [1]},
                                {"target": "cat.fundas/04", "contribution": "gramaje en g/m²", "component": "gramaje",
                                 "kind": "precisión", "questions": [3]}],
              "hints": [{"target": "N1", "pista": "Dice el tipo de sujeción.", "propiedad": ["P09"], "ac": ["Precisión"],
                         "origen": {"tipo": "paa", "apoyo": ["paa-q:s:2"]}, "questions": [2]},
                        {"target": "N2", "pista": "La temporada se declara.", "propiedad": ["P09"], "ac": ["Precisión"],
                         "origen": {"tipo": "paa", "apoyo": ["paa-q:s:3"]}, "questions": [3]}],
              "marks": [{"target": "cat.fundas/01", "mark": "sí", "reason": "Se elige por el tejido.", "questions": [1],
                         "sources": ["paa-q:s:1"]},
                        {"target": "cat.fundas/02", "mark": "no", "case": "b", "reason": "Un filtro.", "questions": [1],
                         "sources": ["paa-q:s:1"]},
                        {"target": "gen/01", "mark": "sí", "reason": "Cambia.", "questions": [1], "sources": ["paa-q:s:1"]},
                        {"target": "inf/07", "mark": "sí", "reason": "x", "questions": [1], "sources": ["paa-q:s:1"]}],
              "specializations": [{"id": "S1", "name": "de verano", "order": "uso"}],
              "revisions": [{"id": "R1", "target": "cat.fundas/01", "action": "reformular"}], **extra}
    folder = paa_dirs / "var" / "sets" / "s"
    folder.mkdir(parents=True)
    (folder / "classified.json").write_text(json.dumps(result), encoding="utf-8")
    (folder / "questions.json").write_text(json.dumps({"questions": [{"q": q["q"]} for q in qs]}), encoding="utf-8")
    return result


def by_id(model):
    return {r["id"]: r for b in model["general"] + model["blocks"] for r in b["requirements"]} | \
        {r["id"]: r for r in model["inferred"] + (model.get("paa") or {}).get("requirements", [])}


def test_without_the_paa_phase_the_model_carries_each_mark_and_points_out_the_missing_ones(catalog):
    m = engine.assemble(catalog)
    r = by_id(m)
    assert r["cat.fundas/01"]["comparison"] == NO and r["gen/01"]["comparison"] == SI   # blocks and general layer (D-126)
    assert r["cat.fundas/02"]["comparison"] is None and r["inf/01"]["comparison"] is None   # no default (D-139)
    assert m["pending_definition"] == {"comparison": ["cat.fundas/02", "cat.fundas/03", "inf/01"]}   # 04 is excluded
    assert m["engine"]["hints"] == "0.4"   # D-138
    assert "paa" not in m and "paa" not in m["uncompiled"]
    text = engine.render(m).splitlines()
    assert any(line.endswith("pistas 0.4") for line in text)
    assert "| cat.fundas/01 | ¿De qué tejido es? | material | principal | `imp:material@zz` | no (b) |" in text
    assert "- Sin marca de comparación (D-139: sin valor por defecto): 3 requisitos: cat.fundas/02, cat.fundas/03, inf/01" in text


def test_the_paa_phase_enters_the_model_as_provisional_out_of_the_key(catalog, paa_dirs):
    classified(paa_dirs, catalog)
    before = engine.assemble(catalog)
    m = engine.assemble(catalog, "s")
    assert m["key"] == before["key"]   # out of the key, like an inferred question (D-224)
    q = m["paa"]
    assert q["set"] == "s" and q["status"] == "no compilado" and q["rulebook"] == "classifier/paa.md v8"
    # candidates: one requirement in each block of the model; the one the block already has does not enter
    (n1,) = q["requirements"]
    assert n1["id"] == "paa/N1/fundas" and n1["block"] == "cat.fundas" and n1["origin"] == "paa"
    assert (n1["importance"], n1["rule"], n1["provisional"]) == ("complementario", "sin-regla:voto", True)
    assert n1["sources"] == ["paa-q:s:2"] and n1["status"] == "no compilado" and n1["description"] == "Si fija el relleno."
    assert n1["resolving_info"][0] | {"stores": []} == {"contribution": "sujeción interior", "component": "si la tiene",
                                                        "origin": "paa", "support": ["paa-q:s:2"], "status": "no compilado",
                                                        "stores": []}
    assert "paa/N1/fundas" not in {r["id"] for b in m["blocks"] for r in b["requirements"]}
    r = by_id(m)
    # confirmations of a requirement and of an inferred question
    assert r["cat.fundas/01"]["paa_confirmed"] == r["inf/01"]["paa_confirmed"] == ["paa-q:s:1"]
    # contributions: a new one, «no compilado»; the one the requirement already has does not enter twice
    added = [c for c in r["cat.fundas/02"]["resolving_info"] if c["origin"] == "paa"]
    assert [(c["contribution"], c["status"], c["support"]) for c in added] == [("medida del relleno", "no compilado", ["paa-q:s:1"])]
    # hints without PV-n; the hint of a compiled candidate reaches its requirement
    assert r["paa/N1/fundas"]["hints"][-1] == {"pista": "Dice el tipo de sujeción.", "propiedad": ["P09"], "ac": ["Precisión"],
                                              "origen": {"tipo": "paa", "apoyo": ["paa-q:s:2"]}, "status": "no compilado"}
    assert r["cat.fundas/03"]["hints"][-1]["pista"] == "La temporada se declara."
    # marks: new where there is none, a confirmation keeps it, a contradiction is a doubt («se compara», D-139)
    assert r["cat.fundas/02"]["comparison"] == {"mark": "no", "case": "b", "reason": "Un filtro.", "origin": "paa",
                                                "sources": ["paa-q:s:1"], "status": "no compilado"}
    assert r["gen/01"]["comparison"] == SI
    doubt = r["cat.fundas/01"]["comparison"]
    assert doubt["mark"] == "sí" and doubt["doubt"] and doubt["model"] == NO and doubt["paa"]["mark"] == "sí"
    assert [(x["target"], x["status"]) for x in q["marks"]] == [("cat.fundas/01", "contradice: duda"), ("cat.fundas/02", "nueva"),
                                                                ("gen/01", "confirma")]
    assert q["skipped"] == [
        "candidato N1 → cat.otra: el bloque no está en el modelo",
        "candidato N2 → cat.fundas: el bloque ya lo tiene (cat.fundas/03); no se repite",
        "aportación → cat.fundas/04: excluido por relevancia en esta clase",
        "marca → inf/07: cuestión inferida que este modelo no tiene",
        "especialización S1 «de verano»: la propone PAA; no entra en la ejecución (D-224)",
        "revisiones (1): no entran en la ejecución (las lista bin/train compile, D-179)"]
    # used without compiling and pending: the provisional mark fills the gap; the candidate has none
    assert m["uncompiled"]["paa"] == {"set": "s", "requirements": ["paa/N1/fundas"], "confirmed": ["cat.fundas/01", "inf/01"],
                                      "contributions": ["cat.fundas/02"], "hints": ["cat.fundas/03", "paa/N1/fundas"],
                                      "marks": ["cat.fundas/01", "cat.fundas/02", "gen/01"]}
    assert "paa/N1/fundas" in m["uncompiled"]["without_rule"]
    assert m["pending_definition"]["comparison"] == ["cat.fundas/03", "inf/01", "paa/N1/fundas"]
    text = engine.render(m)
    assert "## PAA (fase 2, provisional: no compilado, fuera de la clave)" in text
    assert "| paa/N1/fundas | cat.fundas | ¿Tiene sujeción interior? | construccion | complementario (provisional) |" in text


def test_assemble_with_the_paa_phase_writes_the_model_and_queues_it(catalog, paa_dirs):
    classified(paa_dirs, catalog)
    engine.cmd_assemble(catalog, "s")
    model = json.loads(catalog.with_name("funda-1.model.json").read_text(encoding="utf-8"))
    assert model["paa"]["set"] == "s"
    (line,) = engine.QUEUE.read_text(encoding="utf-8").splitlines()
    queued = json.loads(line)
    assert queued["case"] == "funda-1" and queued["paa"]["requirements"] == ["paa/N1/fundas"]
    engine.cmd_assemble(catalog)   # phase 1 again: the entry is replaced, without PAA
    assert "paa" not in json.loads(engine.QUEUE.read_text(encoding="utf-8").splitlines()[0])


def test_the_set_must_be_of_the_key_and_its_classification_must_cover_its_questions(catalog, paa_dirs):
    classified(paa_dirs, catalog, key=("gen", "cat.otra"))
    with pytest.raises(StoreError, match="de otra clave"):
        engine.assemble(catalog, "s")
    with pytest.raises(SystemExit, match="fase PAA: el conjunto s es de otra clave"):
        engine.cmd_assemble(catalog, "s")
    (paa_dirs / "var" / "sets" / "s" / "questions.json").write_text(
        json.dumps({"questions": [{"q": "¿Qué funda abriga más?"}, {"q": "¿Una nueva?"}]}), encoding="utf-8")
    with pytest.raises(StoreError, match="no tiene 1 preguntas"):
        engine.assemble(catalog, "s")
    (paa_dirs / "sets" / "otro.json").write_text(json.dumps({"class": "C", "seeds": [{"q": "x"}]}), encoding="utf-8")
    with pytest.raises(StoreError, match="no está clasificado"):
        engine.assemble(catalog, "otro")


def test_the_agent_of_a_later_classification_does_not_read_what_a_paa_phase_added(catalog, paa_dirs):
    from demand_engine.paa import classify
    classified(paa_dirs, catalog)
    m = engine.assemble(catalog, "s")
    reqs = {r["id"]: r for r in classify.catalog(m)}
    assert "paa/N1/fundas" not in reqs and reqs["cat.fundas/02"]["contributions"] == ["medidas"]
