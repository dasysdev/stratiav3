import json
import re

import pytest

from info_audit import schema
from info_audit.records import check

TEXT = "# Edredón nórdico\nComposición: 100 % algodón\nEnvío gratis desde 50 €"


@pytest.fixture
def files(tmp_path):
    rep = tmp_path / "alfa.json"
    rep.write_text(json.dumps({"filter": "alfa", "version": 1, "ficha": "audit-bb-x", "title": "Edredón | BB",
                               "text": TEXT, "fragments": []}), encoding="utf-8")
    model = tmp_path / "model.json"
    model.write_text(json.dumps({"case": "bb-x", "scope": "Contenido", "sheet": "content@0.2", "units": [
        {"id": "gen/01", "pertinent": True},
        {"id": "gen/02", "pertinent": True, "comparison": {"mark": "no", "case": "a", "reason": "…"}},
        {"id": "gen/03", "pertinent": True},
        {"id": "gen/04", "pertinent": False},
    ]}), encoding="utf-8")
    return tmp_path


def header(files, kind):
    return {"schema": f"info-audit/{kind}", "version": 1, "audit": "piloto-bb", "scope": "Contenido",
            "representation": {"profile": "audit-es", "reader": "alfa/1", "page": "audit-bb-x",
                               "captured_at": "2026-10-30T00:40:00+01:00", "file": str(files / "alfa.json")},
            "model": {"case": "bb-x", "sheet": "content@0.2", "file": str(files / "model.json")}}


COVERAGE = {"objetivo": "plazo de entrega", "regiones_inspeccionadas": ["texto entero"], "metodos": ["lectura", "plazo|días"],
            "alternativas_verificadas": ["entrega en 24/48 h"], "resultados": "sin candidatos", "candidatos_pendientes": [],
            "limitaciones": [], "diagnostico": "no_publicado", "conclusion": "no se publica el plazo"}


def availability(files):
    return header(files, "availability") | {
        "universo_examinable": {"regiones": ["título", "texto"], "entidades": ["producto"], "limitaciones": []},
        "evidencias": [
            {"evidencia_id": "E-001", "tipo": "presencia", "localizador": {"posicion": [TEXT.index("Comp"), TEXT.index("\nEnv")]},
             "contenido_original": "Composición: 100 % algodón", "resultado_observado": "composición publicada"},
            {"evidencia_id": "E-002", "tipo": "presencia", "localizador": {"ruta": "title"},
             "contenido_original": "Edredón | BB", "resultado_observado": "denominación"},
        ],
        "unidades": [
            {"ri_id": "gen/01", "estado_disponibilidad": "determinada", "disponibilidad_efectiva": 1,
             "pertinencia": "denominación", "evidencias": ["E-002"]},
            {"ri_id": "gen/02", "estado_disponibilidad": "determinada", "disponibilidad_efectiva": 1,
             "pertinencia": "composición", "evidencias": ["E-001"]},
            {"ri_id": "gen/03", "estado_disponibilidad": "determinada", "disponibilidad_efectiva": 0, "ir": 0,
             "pertinencia": "ningún candidato", "evidencias": [], "cobertura": COVERAGE},
        ]}


def assessment(files, phase1):
    path = files / "availability.json"
    path.write_text(json.dumps(phase1), encoding="utf-8")
    six = [{"criterio": c, "estado": "valorado", "gsc": 2, "evidencias": ["E-001"], "justificacion": "…",
            "propiedades_consideradas": [{"propiedad": "P06", "efecto": "sin defecto"}], "pistas_usadas": ["PV-1"]}
           for c in ("Concreción", "Precisión", "Aplicabilidad", "Comparabilidad", "Fiabilidad", "Justificación")]
    return header(files, "assessment") | {"availability": str(path), "lote": "gen", "evidencias": [], "hallazgos": [],
                                          "unidades": [{"ri_id": "gen/02", "disponibilidad_efectiva": 1, "valoraciones": six}]}


def errors_of(record, needle):
    errors = check(record)
    assert any(needle in e for e in errors), errors


def test_valid_records(files):
    phase1 = availability(files)
    assert check(phase1) == []
    assert check(assessment(files, phase1)) == []


# --- What bin/audit validate rejects (T-097) -------------------------------------------------------

def test_rejects_quote_not_literal(files):
    record = availability(files)
    record["evidencias"][0]["contenido_original"] = "Composición: algodón 100 %"
    errors_of(record, "no está literal")


def test_rejects_quote_outside_its_position(files):
    record = availability(files)
    record["evidencias"][0]["localizador"]["posicion"] = [0, 10]
    errors_of(record, "no está en la posición")


def test_rejects_quote_not_literal_in_phase_2(files):
    record = assessment(files, availability(files))
    record["evidencias"] = [{"evidencia_id": "E-003", "tipo": "presencia", "localizador": {},
                             "contenido_original": "Envío gratis", "resultado_observado": "…"},
                            {"evidencia_id": "E-004", "tipo": "presencia", "localizador": {},
                             "contenido_original": "Envío en 24 h", "resultado_observado": "…"}]
    errors = check(record)
    assert len(errors) == 1 and "E-004" in errors[0]


def test_absence_evidence_is_not_a_quote(files):
    record = availability(files)
    record["evidencias"].append({"evidencia_id": "E-003", "tipo": "ausencia", "localizador": {},
                                 "contenido_original": "búsqueda de «plazo» sin resultados", "resultado_observado": "…"})
    assert check(record) == []


def test_rejects_zero_without_coverage(files):
    record = availability(files)
    del record["unidades"][2]["cobertura"]
    errors_of(record, "sin registro de cobertura")


def test_rejects_ac_with_availability_zero(files):
    record = assessment(files, availability(files))
    record["unidades"][0]["ri_id"] = "gen/03"
    errors_of(record, "AC valorados con disponibilidad 0")


def test_rejects_ac_with_availability_inconclusive(files):
    phase1 = availability(files)
    phase1["unidades"][1] |= {"estado_disponibilidad": "inconclusa", "disponibilidad_efectiva": None,
                              "comprobacion_fallida": {"comprobacion": "lectura", "motivo": "…"}}
    errors_of(assessment(files, phase1), "AC valorados con disponibilidad inconclusa")


def test_rejects_availability_zero_in_phase_2_record(files):
    record = assessment(files, availability(files))
    record["unidades"][0]["disponibilidad_efectiva"] = 0
    errors_of(record, "disponibilidad_efectiva: debe ser 1")


def test_comparability_na_only_with_the_mark(files):
    phase1 = availability(files)
    record = assessment(files, phase1)
    record["unidades"][0]["valoraciones"][3] |= {"estado": "NA", "gsc": None}
    assert check(record) == []  # gen/02 is marked as not a comparison dimension
    record["unidades"][0]["ri_id"] = "gen/01"
    errors_of(record, "NA de criterio solo en Comparabilidad")


def test_rejects_na_of_other_criterion(files):
    record = assessment(files, availability(files))
    record["unidades"][0]["valoraciones"][4] |= {"estado": "NA", "gsc": None}
    errors_of(record, "NA de criterio solo en Comparabilidad")


@pytest.mark.parametrize("gsc", [3, -1, "2", True, 1.5])
def test_rejects_gsc_outside_scale(files, gsc):
    record = assessment(files, availability(files))
    record["unidades"][0]["valoraciones"][0]["gsc"] = gsc
    errors_of(record, "gsc")


def test_ne_needs_the_failed_check(files):
    record = assessment(files, availability(files))
    record["unidades"][0]["valoraciones"][0] |= {"estado": "NE", "gsc": None}
    errors_of(record, "NE sin la comprobación que falló")
    record["unidades"][0]["valoraciones"][0]["comprobacion_fallida"] = {"comprobacion": "c", "motivo": "m"}
    assert check(record) == []


# --- Other rules -----------------------------------------------------------------------------------

def test_no_third_value_of_availability(files):
    record = availability(files)
    record["unidades"][0]["disponibilidad_efectiva"] = 2
    errors_of(record, "no está en")
    record["unidades"][0] |= {"disponibilidad_efectiva": None}
    errors_of(record, "inconclusa va sin valor")


def test_phase_1_covers_every_pertinent_ri(files):
    record = availability(files)
    record["unidades"].pop(0)
    errors_of(record, "gen/01: RI pertinente sin disponibilidad")
    record = availability(files)
    record["unidades"].append(record["unidades"][0] | {"ri_id": "gen/04"})
    errors_of(record, "gen/04: no es un RI pertinente")


def test_six_criteria_once_each(files):
    record = assessment(files, availability(files))
    record["unidades"][0]["valoraciones"][5]["criterio"] = "Concreción"
    errors_of(record, "los seis AC")


def test_scope_reads_its_representation(files):
    record = availability(files)
    record["scope"] = "Marcado"
    errors_of(record, "Marcado se lee con markup/1")


def test_model_of_the_old_scope_names_rejected(files):
    # D-220: the model is composed with the sheet of Contenido; Web is not an equivalent any more
    model = json.loads((files / "model.json").read_text(encoding="utf-8"))
    (files / "model.json").write_text(json.dumps(model | {"scope": "Web"}), encoding="utf-8")
    errors_of(availability(files), "no es de bb-x en Contenido")


def test_cited_evidence_must_exist(files):
    record = availability(files)
    record["unidades"][0]["evidencias"] = ["E-009"]
    errors_of(record, "cita E-009")


def test_unknown_fields_rejected(files):
    record = assessment(files, availability(files))
    record["unidades"][0]["gsc_global"] = 2
    errors_of(record, "campo no previsto gsc_global")


# --- Invariants 4, 5 and 7 -------------------------------------------------------------------------

FORBIDDEN = re.compile(r"peso|weight|media|mean|average|promedio|global|total|score|formula|fórmula|suma", re.I)


def test_schemas_have_no_weights_means_global_gsc_or_ir_formula():
    names = set()
    for path in schema.SCHEMAS.glob("*.json"):
        names |= schema.property_names(json.loads(path.read_text(encoding="utf-8")))
    assert names and not [n for n in names if FORBIDDEN.search(n)]
    # IR only as the closing value of availability 0
    assert schema.load("availability.v1.json")["properties"]["unidades"]["items"]["properties"]["ir"] == {
        "description": "Solo con disponibilidad 0 (invariante 3). Sin fórmula de IR.", "const": 0}
    assert "ir" not in schema.property_names(schema.load("assessment.v1.json"))
