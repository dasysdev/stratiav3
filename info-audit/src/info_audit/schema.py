"""The JSON schemas of the records (D-199) and a validator of the subset of JSON Schema they use.

Standard library only, like web-audit. The schemas live in info-audit/schemas/<name>.v<N>.json and
refer to each other by $id ("common.v1.json#/$defs/evidence"). A keyword outside the subset is an
error of the schema, not ignored: the schemas cannot say more than the validator checks.
"""
from __future__ import annotations

import json
import re
from functools import cache

from . import ROOT

SCHEMAS = ROOT / "schemas"
KEYWORDS = {"$id", "$ref", "$defs", "title", "description", "type", "enum", "const", "required", "properties",
            "additionalProperties", "items", "minItems", "maxItems", "minLength", "pattern", "minimum"}
TYPES = {"object": dict, "array": list, "string": str, "integer": int, "number": (int, float),
         "boolean": bool, "null": type(None)}


@cache
def load(name: str) -> dict:
    return json.loads((SCHEMAS / name).read_text(encoding="utf-8"))


def _same(a, b) -> bool:
    """Equality with the same type: true is not 1, and "2" is not 2."""
    return type(a) is type(b) and a == b


def _is(value, kind: str) -> bool:
    if kind in ("integer", "number") and isinstance(value, bool):
        return False
    return isinstance(value, TYPES[kind])


def _resolve(ref: str, doc: str) -> tuple[dict, str]:
    name, _, pointer = ref.partition("#")
    name = name or doc
    node = load(name)
    for part in filter(None, pointer.split("/")):
        node = node[part]
    return node, name


def validate(data, schema: dict | str, doc: str | None = None, path: str = "$") -> list[str]:
    """Errors of data against a schema (a name in schemas/ or a node of the document doc)."""
    if isinstance(schema, str):
        doc, schema = schema, load(schema)
    unknown = set(schema) - KEYWORDS
    if unknown:
        raise ValueError(f"{doc}: palabras fuera del subconjunto del validador: {', '.join(sorted(unknown))}")
    if "$ref" in schema:
        node, ref_doc = _resolve(schema["$ref"], doc)
        return validate(data, node, ref_doc, path)
    if "const" in schema and not _same(data, schema["const"]):
        return [f"{path}: debe ser {json.dumps(schema['const'], ensure_ascii=False)}"]
    if "enum" in schema and not any(_same(data, v) for v in schema["enum"]):
        return [f"{path}: {json.dumps(data, ensure_ascii=False)} no está en "
                f"{json.dumps(schema['enum'], ensure_ascii=False)}"]
    kinds = schema.get("type")
    if kinds and not any(_is(data, k) for k in ([kinds] if isinstance(kinds, str) else kinds)):
        return [f"{path}: debe ser de tipo {kinds}"]
    errors = []
    if isinstance(data, str):
        if len(data.strip()) < schema.get("minLength", 0):
            errors.append(f"{path}: vacío")
        if "pattern" in schema and not re.search(schema["pattern"], data):
            errors.append(f"{path}: «{data}» no sigue {schema['pattern']}")
    if _is(data, "number") and "minimum" in schema and data < schema["minimum"]:
        errors.append(f"{path}: menor que {schema['minimum']}")
    if isinstance(data, list):
        if len(data) < schema.get("minItems", 0):
            errors.append(f"{path}: menos de {schema['minItems']} elementos")
        if "maxItems" in schema and len(data) > schema["maxItems"]:
            errors.append(f"{path}: más de {schema['maxItems']} elementos")
        if "items" in schema:
            for i, item in enumerate(data):
                errors += validate(item, schema["items"], doc, f"{path}[{i}]")
    if isinstance(data, dict):
        props = schema.get("properties", {})
        errors += [f"{path}: falta {key}" for key in schema.get("required", []) if key not in data]
        if schema.get("additionalProperties") is False:
            errors += [f"{path}: campo no previsto {key}" for key in data if key not in props]
        for key, sub in props.items():
            if key in data:
                errors += validate(data[key], sub, doc, f"{path}.{key}")
    return errors


def property_names(node) -> set[str]:
    """Every property name declared anywhere in a schema (for the invariants test)."""
    if isinstance(node, dict):
        names = set(node.get("properties", {})) if isinstance(node.get("properties"), dict) else set()
        return names.union(*(property_names(v) for v in node.values()))
    if isinstance(node, list):
        return set().union(*(property_names(v) for v in node))
    return set()
