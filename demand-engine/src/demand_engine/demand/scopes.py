"""One demand model and one sheet per scope (D-155); the recommended properties of Google Search as support (D-145).

The model does not depend on the scope: questions, importance, resolving information and hints are the same in every
scope. Each scope has a versioned sheet (catalog/scopes/<scope>.json) with two parts:

- pertinence: every requirement of the model is pertinent in the scope, except the NA that rules grounded in the
  function of the scope give, by entity or component, never requirement by requirement. The lack of a property or a
  field in the vocabulary of the scope is not a reason. Contenido (content) has no exceptions.
- localization: the vocabulary of the scope related to the contributions of the resolving information, which reaches
  the auditor as illustrative expressions of the RI profile: it guides the search; it neither closes it nor decides
  pertinence. In Marcado (markup) it is derived from the Google Search support of the catalog (general layer and
  attributes) plus the sheet's own entries (the properties that are not support, such as the required ones).
  Contenido has none: it does not use the markup, and a sheet never includes the localization of another (D-220).

The audit composes model × sheet into RI × scope units and records the version of the sheet (compose). Each unit carries
the comparison mark of its requirement as the model has it (D-126; the scope does not decide it, and without a mark it
stays None, D-139) and the fields of the RI profile that come from the model (D-177): the components and their
contributions from the resolving information, the description for «objeto», «alcance» and «casos_frontera», the
resolved hints (D-135) and the localization as illustrative expressions (D-155). The auditor does not fill them in; what
the model lacks is pointed out in «pendientes_de_definicion». The requirements that the PAA phase adds to the model
(D-224, «no compilado») are units like the others.

The properties that the consumers of the Marcado profile recommend without requiring are demand support with
origin «referencias» and no scope, like the Amazon PTD (D-052): those of the general layer in the sources and support of
their requirement in gen.json; those of category attributes in catalog/google-search.json, by equivalence with the
Shopify attributes a requirement cites; the ones no requirement or contribution covers, as candidates there.
"""
import fnmatch
import sys
from pathlib import Path

from .catalog import CATALOG, read_json, write_json

SCOPES_DIR = CATALOG / "scopes"
GOOGLE = CATALOG / "google-search.json"
RETIRED = CATALOG.parent.parent / "web-audit" / "reference" / "retired.json"   # the contract with web-audit (T-055)
PREFIX = "google-search-"
STATUSES = ("propuesto", "descartado")


def load_google() -> dict:
    return read_json(GOOGLE)


def load_sheet(scope: str) -> dict:
    path = SCOPES_DIR / f"{scope}.json"
    if not path.exists():
        sys.exit(f"model: no hay ficha del ámbito «{scope}» ({', '.join(scope_names())})")
    return read_json(path)


def scope_names() -> list:
    return sorted(p.stem for p in SCOPES_DIR.glob("*.json"))


def handles(sources: list) -> set:
    """The Shopify attributes a requirement cites: shopify-attr:fabric, shopify-attr:color=Rojo@v… → fabric, color."""
    return {s.split(":", 1)[1].split("@")[0].split("=")[0] for s in sources if s.startswith("shopify-attr:")}


def attribute_support(sources: list, google: dict) -> list:
    """The Google Search properties that support a category requirement through the Shopify attributes it cites."""
    cited = handles(sources)
    return [a["source"] for a in google.get("attributes", [])
            if any(fnmatch.fnmatchcase(h, pattern) for h in cited for pattern in a["shopify"])]


def google_sources(sources: list) -> list:
    return [s for s in sources if s.startswith(PREFIX)]


# --- Localization and composition ---------------------------------------------------------------------------------

def localization(sheet: dict, gen: dict) -> dict:
    """requirement id → [{source, contribution}] of the general layer: the Google Search support of each contribution
    (when the sheet takes it from the catalog) and the sheet's own entries."""
    out = {}
    if "gen.json" in sheet.get("localization", {}).get("from", []):
        for b in gen["blocks"]:
            for r in b["requirements"]:
                for c in r.get("resolving_info", []):
                    for s in google_sources(c.get("support", [])):
                        out.setdefault(r["id"], []).append({"source": s, "contribution": c["contribution"]})
    for e in sheet.get("localization", {}).get("properties", []):
        out.setdefault(e["requirement"], []).append({"source": e["source"], "contribution": e["contribution"]})
    return out


def exception(entry: dict, rules: list):
    """The first NA rule of the sheet that matches a requirement of the model: by entity, or by component when every
    contribution of the requirement answers that component."""
    components = {c.get("component") for c in entry.get("resolving_info", [])}
    for rule in rules:
        if rule.get("entity") and entry.get("entity") == rule["entity"]:
            return rule
        if rule.get("component") and components == {rule["component"]}:
            return rule
    return None


def requirements_of(model: dict) -> list:
    """(entry, block) of every requirement that the model audits in this offer: the general layer that applies, the
    category and specialization blocks, the inferred questions and the candidates of the PAA phase (D-224)."""
    out = [(r, b["id"]) for b in model["general"] for r in b["requirements"] if r.get("applies", True)]
    out += [(r, b["id"]) for b in model["blocks"] for r in b["requirements"]]
    out += [(r, r.get("block") or "inf") for r in model.get("inferred", [])]
    out += [(r, r.get("block") or "paa") for r in (model.get("paa") or {}).get("requirements", [])]
    return out


NO_RESOLVING, NO_DESCRIPTION, NO_MARK = "sin información resolutiva", "sin descripción", "sin marca de comparación"
GAPS = (NO_RESOLVING, NO_DESCRIPTION, NO_MARK)


def components(resolving_info: list) -> list:
    """«componentes_respuesta»: the contributions of the resolving information grouped by the component they answer, in
    the order of the catalog (D-177)."""
    out = {}
    for c in resolving_info:
        entry = {"aportacion": c["contribution"], "origen": c.get("origin")}
        if c.get("status"):
            entry["estado"] = c["status"]
        out.setdefault(c.get("component"), []).append(entry)
    return [{"componente": k, "aportaciones": v} for k, v in out.items()]


def profile(r: dict, where: list) -> dict:
    """The fields of the RI profile that the demand engine composes from the model (D-177, D-135, D-155). «objeto»,
    «alcance» and «casos_frontera» take the whole description; what the model lacks is pointed out, never filled in
    (a comparison mark too: D-139)."""
    description = r.get("description")
    missing = [NO_RESOLVING] * (not r.get("resolving_info")) + [NO_DESCRIPTION] * (not description) \
        + [NO_MARK] * (not r.get("comparison"))
    return {"objeto": description, "alcance": description, "casos_frontera": description,
            "componentes_respuesta": components(r.get("resolving_info", [])),
            "pistas_valoracion": r.get("hints", []), "expresiones_ejemplo": where,
            "pendientes_de_definicion": missing}


def compose(model: dict, sheet: dict, gen: dict, google: dict) -> dict:
    """The RI × scope units of a model in the scope of the sheet, with the version of the sheet (D-155)."""
    found = localization(sheet, gen)
    by_attribute = "google-search.json" in sheet.get("localization", {}).get("from", [])
    rules = sheet.get("pertinence", {}).get("exceptions", [])
    units = []
    for r, block in requirements_of(model):
        rule = exception(r, rules)
        where = list(found.get(r["id"], []))
        if by_attribute:
            where += [{"source": s, "contribution": None} for s in attribute_support(r.get("sources", []), google)]
        units.append({"id": r["id"], "block": block, "question": r.get("question"), "importance": r.get("importance"),
                      "pertinent": rule is None, "na_reason": rule.get("reason") if rule else None,
                      "comparison": r.get("comparison"),  # D-126: the mark of the model, never decided here
                      "profile": profile(r, [] if rule else where)})
    return {"case": model.get("case"), "model_key": model["key"]["model"], "scope": sheet["scope"],
            "sheet": f"{sheet['id']}@{sheet['version']}", "units": units}


def render_units(composed: dict) -> str:
    units = composed["units"]
    na = [u for u in units if not u["pertinent"]]
    located = [u for u in units if u["profile"]["expresiones_ejemplo"]]
    lacking = {gap: [u for u in units if gap in u["profile"]["pendientes_de_definicion"]] for gap in GAPS}
    marks = [(u.get("comparison") or {}).get("mark") for u in units]
    lines = [f"# {composed['case']} × {composed['scope']}", "",
             f"- Ficha: `{composed['sheet']}` · clave del modelo: `{' '.join(composed['model_key'])}`",
             f"- Unidades RI × ámbito: {len(units)} · pertinentes: {len(units) - len(na)} · NA: {len(na)}",
             f"- Con localización: {len(located)}",
             f"- Perfil del RI: {sum(bool(u['profile']['pistas_valoracion']) for u in units)} con pistas de valoración · "
             + " · ".join(f"{len(v)} {gap}" for gap, v in lacking.items()),
             f"- Marca de comparación (del modelo, D-126): {marks.count('sí')} se compara · {marks.count('no')} no se "
             f"compara · {marks.count(None)} sin marca (pendiente, D-139)", ""]
    if na:
        lines += ["## No pertinentes", ""] + [f"- {u['id']} {u['question']} — {u['na_reason']}" for u in na] + [""]
    if lacking[NO_RESOLVING]:
        lines += [f"## Perfil del RI {NO_RESOLVING} (no se completa)", ""] \
            + [f"- {u['id']} {u['question']}" for u in lacking[NO_RESOLVING]] + [""]
    lines += ["## Localización (orienta; no cierra la búsqueda)", ""]
    for u in located:
        lines.append(f"- {u['id']} {u['question']}")
        lines += [f"  - `{s['source']}`" + (f" → {s['contribution']}" if s.get("contribution") else "")
                  for s in u["profile"]["expresiones_ejemplo"]]
    return "\n".join(lines) + "\n"


def cmd_scope(model_path: Path, scopes: list) -> None:
    from .catalog import load_gen
    model, gen, google = read_json(model_path), load_gen(), load_google()
    stem = model_path.name.removesuffix(".model.json")
    for scope in scopes or scope_names():
        composed = compose(model, load_sheet(scope), gen, google)
        out = model_path.with_name(f"{stem}.{scope}.json")
        write_json(out, composed)
        out.with_suffix(".md").write_text(render_units(composed), encoding="utf-8")
        units = composed["units"]
        print(f"{composed['scope']} ({composed['sheet']}): {len(units)} unidades, "
              f"{sum(not u['pertinent'] for u in units)} NA, {sum(bool(u['profile']['expresiones_ejemplo']) for u in units)} "
              f"con localización; perfil del RI: "
              + ", ".join(f"{sum(gap in u['profile']['pendientes_de_definicion'] for u in units)} {gap}"
                          for gap in GAPS))
        print(f"  → {out} y {out.with_suffix('.md')}")


# --- Checks -------------------------------------------------------------------------------------------------------

def contributions(gen: dict) -> dict:
    return {r["id"]: {c["contribution"] for c in r.get("resolving_info", [])} for b in gen["blocks"] for r in b["requirements"]}


def gen_google(gen: dict) -> set:
    return {s for b in gen["blocks"] for r in b["requirements"] for c in r.get("resolving_info", [])
            for s in google_sources(c.get("support", []))}


def google_problems(google: dict, gen: dict, shopify: dict, retired=None) -> list:
    """What is wrong in google-search.json: every retired property is covered (support of the general layer, an
    attribute equivalence or a candidate), the Shopify attributes exist, the candidates are well formed; and, if the
    registry of web-audit is at hand, the contract lists the same requirements."""
    problems = []
    covered = gen_google(gen) | {a["source"] for a in google.get("attributes", [])} \
        | {s for c in google.get("candidates", []) for s in c.get("sources", [])}
    for e in google.get("retired", {}).get("requirements", []):
        if e["source"] not in covered:
            problems.append(f"{e['id']} ({e['source']}): ni apoyo de la capa general, ni atributo, ni candidato")
    for a in google.get("attributes", []):
        if not a.get("shopify"):
            problems.append(f"{a['source']}: sin atributos de Shopify")
        problems += [f"{a['source']}: el atributo de Shopify «{h}» no existe" for h in a.get("shopify", [])
                     if "*" not in h and h not in shopify]
    for c in google.get("candidates", []):
        if c.get("status") not in STATUSES:
            problems.append(f"candidato {c.get('sources')}: estado «{c.get('status')}» no válido ({', '.join(STATUSES)})")
        elif not c.get("sources") or not c.get("rationale"):
            problems.append(f"candidato {c.get('question')}: sin fuentes o sin fundamento")
        elif c["status"] == "propuesto" and not (c.get("question") and c.get("entity")):
            problems.append(f"candidato {c.get('sources')}: un propuesto necesita pregunta y entidad")
    if retired is not None:
        theirs = {x["id"] for x in retired if x.get("reason") == "modelo de demanda"}
        ours = {e["id"] for e in google.get("retired", {}).get("requirements", [])}
        problems += [f"{i}: retirado al modelo de demanda en web-audit y fuera del contrato" for i in sorted(theirs - ours)]
        problems += [f"{i}: en el contrato y no retirado al modelo de demanda en web-audit" for i in sorted(ours - theirs)]
    return problems


def sheet_problems(sheet: dict, gen: dict) -> list:
    """What is wrong in a scope sheet: identity, NA rules with entity or component and reason, the sources of the
    localization, no included sheet (D-220) and the requirements and contributions its own entries name."""
    problems, name = [], sheet.get("id", "?")
    for key in ("id", "scope", "version"):
        if not sheet.get(key):
            problems.append(f"{name}: falta «{key}»")
    for rule in sheet.get("pertinence", {}).get("exceptions", []):
        if not (rule.get("entity") or rule.get("component")) or not rule.get("reason"):
            problems.append(f"{name}: excepción sin entidad ni componente, o sin fundamento: {rule}")
    loc = sheet.get("localization", {})
    problems += [f"{name}: localización desde «{f}» desconocida" for f in loc.get("from", []) if f not in ("gen.json", "google-search.json")]
    if "include" in loc:
        problems.append(f"{name}: la localización incluye otra ficha; un ámbito no usa la de otro (D-220)")
    known = contributions(gen)
    for e in loc.get("properties", []):
        if e.get("requirement") not in known:
            problems.append(f"{name}: {e.get('source')} → requisito «{e.get('requirement')}» fuera de la capa general")
        elif e.get("contribution") not in known[e["requirement"]]:
            problems.append(f"{name}: {e.get('source')} → aportación «{e.get('contribution')}» que {e['requirement']} no tiene")
    return problems


def catalog_problems(gen: dict) -> list:
    """The checks of google-search.json and of every scope sheet, for «model check --catalog»."""
    from references.read import shopify_attributes
    retired = read_json(RETIRED)["retired"] if RETIRED.exists() else None
    problems = google_problems(load_google(), gen, shopify_attributes(), retired)
    for scope in scope_names():
        problems += sheet_problems(load_sheet(scope), gen)
    return problems
