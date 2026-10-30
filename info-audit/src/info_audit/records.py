"""The rules of the records that the schemas cannot say (D-153, QA-15, gsc-decision.md).

Availability (phase 1) and assessment (phase 2) records are checked against their schema and then
against what they cite: the representation of the scope (the literal quotes, QA-15), the demand
model composed with the scope sheet (the pertinent RI and the comparison mark, D-126) and, for an
assessment, the availability record of the same page × scope (GSC-01).

Paths inside a record are relative to the root of the repository (an absolute path also works).
"""
from __future__ import annotations

import json
from pathlib import Path

from . import ROOT
from .schema import validate

REPO = ROOT.parent
SCHEMAS = {"info-audit/availability": "availability.v1.json", "info-audit/assessment": "assessment.v1.json"}
READERS = {"Contenido": "alfa/1", "Marcado": "markup/1"}
CRITERIA = ("Concreción", "Precisión", "Aplicabilidad", "Comparabilidad", "Fiabilidad", "Justificación")
NOT_LITERAL = {"ausencia", "limitacion_acceso"}  # their contenido_original is the result of a check


class RecordError(Exception):
    pass


def _load(path: str | Path, what: str):
    full = REPO / path
    try:
        return json.loads(full.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        raise RecordError(f"no se puede leer {what} ({path}): {e}") from e


# --- Representation of the scope ------------------------------------------------------------------

class Representation:
    """The literal text that a quote must be in: Alfa's title and text, or the markup blocks."""

    def __init__(self, data: dict, reader: str):
        self.text = None
        if reader == "alfa/1":
            if data.get("filter") != "alfa" or data.get("version") != 1:
                raise RecordError("la representación no es una salida de alfa/1")
            self.page = data.get("ficha")
            self.text = data.get("text") or ""
            self.literals = [data.get("title") or "", self.text]
        else:  # markup/1 (its reader is pending: T-098)
            if data.get("reader") != "markup" or data.get("version") != 1:
                raise RecordError("la representación no es una salida de markup/1")
            self.page = data.get("ficha")
            self.literals = [b.get("text") or "" for b in data.get("blocks", [])]

    def check(self, evidence: dict) -> list[str]:
        if evidence["tipo"] in NOT_LITERAL:
            return []
        eid, quote = evidence["evidencia_id"], evidence["contenido_original"]
        if not any(quote in literal for literal in self.literals):
            return [f"{eid}: el contenido original no está literal en la representación: «{quote[:80]}»"]
        span = evidence["localizador"].get("posicion")
        if span and self.text is not None:
            start, end = span
            if not start < end <= len(self.text):
                return [f"{eid}: posición {span} fuera del texto ({len(self.text)} caracteres)"]
            if quote not in self.text[start:end]:
                return [f"{eid}: el contenido original no está en la posición {span}"]
        return []


# --- Common checks ---------------------------------------------------------------------------------

def _context(record: dict) -> tuple[Representation, dict]:
    """The representation and the pertinent units of the model, after checking that they match."""
    scope, rep = record["scope"], record["representation"]
    if rep["reader"] != READERS[scope]:
        raise RecordError(f"{scope} se lee con {READERS[scope]}, no con {rep['reader']} (D-220, D-223)")
    representation = Representation(_load(rep["file"], "la representación"), rep["reader"])
    if representation.page and representation.page != rep["page"]:
        raise RecordError(f"la representación es de {representation.page}, no de {rep['page']}")
    model = _load(record["model"]["file"], "el modelo del ámbito")
    if model.get("case") != record["model"]["case"] or model.get("scope") != scope:   # the scope of the sheet (D-220)
        raise RecordError(f"el modelo {record['model']['file']} no es de {record['model']['case']} en {scope}")
    if model.get("sheet") != record["model"]["sheet"]:
        raise RecordError(f"el modelo usa la ficha {model.get('sheet')}, no {record['model']['sheet']}")
    units = {u["id"]: u for u in model.get("units", []) if u.get("pertinent")}
    return representation, units


def _evidence_ids(evidences: list[dict], taken: set[str] = frozenset()) -> tuple[set[str], list[str]]:
    ids, errors = set(), []
    for e in evidences:
        if e["evidencia_id"] in ids or e["evidencia_id"] in taken:
            errors.append(f"{e['evidencia_id']}: id repetido")
        ids.add(e["evidencia_id"])
    return ids, errors


def _cited(where: str, cited: list[str], known: set[str]) -> list[str]:
    return [f"{where}: cita {x}, que no existe" for x in cited if x not in known]


# --- Availability (phase 1) ------------------------------------------------------------------------

def check_availability(record: dict) -> list[str]:
    representation, units = _context(record)
    ids, errors = _evidence_ids(record["evidencias"])
    errors += [m for e in record["evidencias"] for m in representation.check(e)]
    seen = set()
    for u in record["unidades"]:
        ri, value, state = u["ri_id"], u["disponibilidad_efectiva"], u["estado_disponibilidad"]
        if ri not in units:
            errors.append(f"{ri}: no es un RI pertinente del modelo del ámbito")
        if ri in seen:
            errors.append(f"{ri}: repetido")
        seen.add(ri)
        errors += _cited(ri, u["evidencias"] + u.get("cobertura", {}).get("evidencias", []), ids)
        if (value is None) != (state == "inconclusa"):
            errors.append(f"{ri}: una comprobación inconclusa va sin valor y un valor va con estado determinada")
        if value == 0:
            if "cobertura" not in u:
                errors.append(f"{ri}: disponibilidad 0 sin registro de cobertura (CO-08, QA-15)")
            if u.get("ir") != 0:
                errors.append(f"{ri}: disponibilidad 0 cierra con ir = 0")
        elif "ir" in u:
            errors.append(f"{ri}: ir solo con disponibilidad 0 (no hay fórmula de IR)")
        if value == 1 and not u["evidencias"]:
            errors.append(f"{ri}: disponibilidad 1 sin evidencia")
        if value is None and "comprobacion_fallida" not in u:
            errors.append(f"{ri}: comprobación inconclusa sin la comprobación que falló")
        if value is not None and "comprobacion_fallida" in u:
            errors.append(f"{ri}: comprobacion_fallida solo en una comprobación inconclusa")
    errors += [f"{ri}: RI pertinente sin disponibilidad (la fase 1 los cubre todos, D-153)"
               for ri in units if ri not in seen]
    return errors


# --- Assessment (phase 2) --------------------------------------------------------------------------

def check_assessment(record: dict) -> list[str]:
    representation, units = _context(record)
    phase1 = _load(record["availability"], "el registro de la fase 1")
    if phase1.get("schema") != "info-audit/availability":
        raise RecordError(f"{record['availability']} no es un registro de disponibilidad")
    for key in ("audit", "scope"):
        if phase1.get(key) != record[key]:
            raise RecordError(f"la fase 1 es de {key} {phase1.get(key)}, no {record[key]}")
    if phase1.get("representation", {}).get("page") != record["representation"]["page"]:
        raise RecordError("la fase 1 es de otra ficha")
    availability = {u["ri_id"]: u["disponibilidad_efectiva"] for u in phase1.get("unidades", [])}
    old = {e["evidencia_id"] for e in phase1.get("evidencias", [])}
    new, errors = _evidence_ids(record["evidencias"], old)
    errors += [m for e in record["evidencias"] for m in representation.check(e)]
    evidences = old | new
    findings = {h["hallazgo_id"] for h in record["hallazgos"]}
    if len(findings) != len(record["hallazgos"]):
        errors.append("hallazgos: id repetido")
    for h in record["hallazgos"]:
        errors += _cited(h["hallazgo_id"], h["evidencias"], evidences)
    seen = set()
    for u in record["unidades"]:
        ri = u["ri_id"]
        if ri in seen:
            errors.append(f"{ri}: repetido")
        seen.add(ri)
        value = availability.get(ri, "missing")
        if value != 1:
            state = {0: "0", None: "inconclusa"}.get(value, "sin registro")
            errors.append(f"{ri}: AC valorados con disponibilidad {state} en la fase 1 (GSC-01)")
        criteria = [v["criterio"] for v in u["valoraciones"]]
        if sorted(criteria) != sorted(CRITERIA):
            errors.append(f"{ri}: los seis AC, una vez cada uno ({', '.join(criteria)})")
        mark = (units.get(ri, {}).get("comparison") or {}).get("mark")
        for v in u["valoraciones"]:
            where = f"{ri} · {v['criterio']}"
            errors += _cited(where, v.get("evidencias", []), evidences)
            errors += _cited(where, v.get("hallazgos", []), findings)
            if v["estado"] == "valorado":
                if v["gsc"] is None:
                    errors.append(f"{where}: valorado sin GSC 0/1/2")
                if not v.get("evidencias"):
                    errors.append(f"{where}: GSC sin evidencias (GSC-12)")
            elif v["gsc"] is not None:
                errors.append(f"{where}: {v['estado']} va con gsc null")
            if v["estado"] == "NE" and "comprobacion_fallida" not in v:
                errors.append(f"{where}: NE sin la comprobación que falló")
            if v["estado"] != "NE" and "comprobacion_fallida" in v:
                errors.append(f"{where}: comprobacion_fallida solo en una NE")
            if v["estado"] == "NA" and not (v["criterio"] == "Comparabilidad" and mark == "no"):
                errors.append(f"{where}: NA de criterio solo en Comparabilidad de un requisito que el modelo "
                              f"marca como no dimensión de comparación (D-126)")
    return errors


# --- Entry point -----------------------------------------------------------------------------------

def check(record) -> list[str]:
    """Every error of a record: its schema first, then its rules."""
    if not isinstance(record, dict) or record.get("schema") not in SCHEMAS:
        return [f"$.schema: debe ser uno de {', '.join(SCHEMAS)}"]
    errors = validate(record, SCHEMAS[record["schema"]])
    if errors:
        return errors
    try:
        rules = check_availability if record["schema"] == "info-audit/availability" else check_assessment
        return rules(record)
    except RecordError as e:
        return [str(e)]
