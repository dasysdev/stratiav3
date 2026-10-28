"""Assessment hints (D-125 to D-140) and the comparison mark (D-126, D-139): check the hints and find those of a
requirement, with code only (D-134).

The catalog of hints holds the hints that go to a type (trait, entity or both) or to the requirements that cite a
source (matched by the beginning of the tag, up to a separator: «ley:UE-1007/2011» matches
«ley:UE-1007/2011-16.1@2011-10-18»). The hints of one requirement live in the requirement itself, in «hints», without
«para» (D-140). The ids PV-n are unique across both places.
"""
import re

from .catalog import CATALOG, load_blocks, load_gen, load_traits, read_json

HINTS = CATALOG / "hints.json"
FIELDS = ("id", "pista", "propiedad", "ac", "para", "origen")
OWN_FIELDS = tuple(f for f in FIELDS if f != "para")  # a requirement's own hints (D-140)
OPTIONAL = ("retirada", "duda")  # D-136: a hint is retired, never deleted; a contradiction is marked as a doubt
PROPERTIES = {f"P{n:02d}" for n in range(6, 19)} - {"P15"}  # P15 retired (D-123)
ACS = ("Concreción", "Precisión", "Aplicabilidad", "Comparabilidad", "Fiabilidad", "Justificación")
ORIGINS = ("marco", "normativa", "referencias", "paa")
ENTITIES = ("producto", "variante", "oferta", "entrega", "condiciones", "vendedor")
KEYS = ({"rasgo"}, {"entidad"}, {"rasgo", "entidad"}, {"fuente"})
ORDER = {"tipo": 0, "fuente": 1, "requisito": 2}
ID = re.compile(r"PV-[1-9]\d*")
MAX_SENTENCES, MAX_CHARS = 2, 280  # «una o dos frases» (D-135)
MARKS, CASES = ("sí", "no"), ("a", "b", "c")


def load_hints() -> dict:
    return read_json(HINTS) if HINTS.exists() else {"hints": []}


def requirements() -> list:
    """Every requirement of the catalog (blocks, compiled or not, and the general layer)."""
    out = [r for b in load_blocks().values() for r in b["requirements"]]
    return out + [r for b in load_gen()["blocks"] for r in b["requirements"]]


def cites(source: str, tag: str) -> bool:
    """A law is cited with its article and date; an attribute or property, with a value. The hyphen and the dot only
    separate in a law: in a Shopify handle they are part of the name (fabric, fabric-weave)."""
    separators = "-.@" if source.startswith("ley:") else "=@"
    return tag == source or (tag.startswith(source) and tag[len(source)] in separators)


def reaches(hint: dict, req: dict) -> str:
    """The key by which a hint of the catalog reaches the requirement («tipo», «fuente») or ''."""
    to = hint["para"]
    if "fuente" in to:
        return "fuente" if any(cites(to["fuente"], s) for s in req.get("sources", [])) else ""
    if all(to[k] == req.get(f) for k, f in (("rasgo", "trait"), ("entidad", "entity")) if k in to):
        return "tipo"
    return ""


def find(req: dict, hints: list) -> list:
    """Hints of a requirement: those of the catalog that reach it and its own, without repeating any and leaving out
    the retired ones: [(key, hint)]."""
    found = [(key, h) for h in hints if (key := reaches(h, req))]
    found += [("requisito", h) for h in req.get("hints", [])]
    found = [(k, h) for k, h in found if "retirada" not in h]
    return sorted(found, key=lambda kh: (ORDER[kh[0]], int(kh[1]["id"][3:])))


def sentences(text: str) -> int:
    return len([s for s in re.split(r"(?<=[.!?])\s+(?=[«A-ZÁÉÍÓÚÑ])", text.strip()) if s])


def hint_errors(h: dict, fields: tuple) -> list:
    """What is wrong in one hint, wherever it lives: fields, id, length, properties, AC and origin (D-135, D-136)."""
    hid = h.get("id", "?")
    missing = [f for f in fields if f not in h]
    extra = [f for f in h if f not in fields + OPTIONAL]
    if missing or extra:
        return [f"{hid}: campos {'que faltan ' + ', '.join(missing) if missing else ''}"
                f"{' y ' if missing and extra else ''}{'que sobran ' + ', '.join(extra) if extra else ''}"]
    errors = []
    if not ID.fullmatch(hid):
        errors.append(f"{hid}: id no es PV-n sin ceros delante")
    text = h["pista"].strip()
    if not text or sentences(text) > MAX_SENTENCES or len(text) > MAX_CHARS:
        errors.append(f"{hid}: la pista ha de ser una o dos frases breves ({sentences(text)} frases, {len(text)} car.)")
    if not h["propiedad"] or set(h["propiedad"]) - PROPERTIES:
        errors.append(f"{hid}: propiedad fuera de P06–P18 (sin P15): {h['propiedad']}")
    if not h["ac"] or set(h["ac"]) - set(ACS):
        errors.append(f"{hid}: AC no válido: {h['ac']}")
    if not isinstance(h["origen"], dict) or h["origen"].get("tipo") not in ORIGINS:
        errors.append(f"{hid}: origen no admitido ({', '.join(ORIGINS)})")
    return errors


def same(group: list, where: str) -> list:
    """Hints with the same destination and the same property (D-136), unless the later one is marked as a doubt."""
    live = [h for h in group if "retirada" not in h]
    return [f"{a['id']} y {b['id']}: mismo destino{where} y misma propiedad "
            f"({', '.join(sorted(set(a['propiedad']) & set(b['propiedad'])))}): ¿dicen lo mismo?"
            for i, a in enumerate(live) for b in live[i + 1:]
            if set(a["propiedad"]) & set(b["propiedad"]) and "duda" not in b]


def check(catalog: dict, reqs: list, vocabulary: set) -> tuple:
    """(errors, warnings) of the hints, in the catalog and in each requirement, and of the comparison marks (D-139)."""
    errors, warnings, seen = [], [], set()
    valid = []
    for h in catalog.get("hints", []):
        errors += hint_errors(h, FIELDS)
        if not all(f in h for f in FIELDS):
            continue
        if h["id"] in seen:
            errors.append(f"{h['id']}: id repetido")
        seen.add(h["id"])
        to = h["para"]
        if not isinstance(to, dict) or set(to) not in KEYS:
            errors.append(f"{h['id']}: «para» ha de llevar rasgo y/o entidad, o fuente (las de un requisito viven "
                          f"en él, D-140): {to}")
            continue
        if to.get("rasgo") is not None and to["rasgo"] not in vocabulary:
            errors.append(f"{h['id']}: rasgo «{to['rasgo']}» fuera del vocabulario")
        if to.get("entidad") is not None and to["entidad"] not in ENTITIES:
            errors.append(f"{h['id']}: entidad «{to['entidad']}» no válida")
        if "retirada" not in h and not any(reaches(h, r) for r in reqs):
            errors.append(f"{h['id']}: su destino no existe (no llega a ningún requisito): {to}")
        valid.append(h)
    by_dest = {}
    for h in valid:
        by_dest.setdefault(repr(sorted(h["para"].items())), []).append(h)
    for group in by_dest.values():
        errors += same(group, "")
    for r in reqs:
        own = r.get("hints", [])
        for h in own:
            found = hint_errors(h, OWN_FIELDS)
            errors += [f"{r['id']}: {e}" for e in found]
            if h.get("id") in seen:
                errors.append(f"{r['id']}: {h['id']}: id repetido")
            seen.add(h.get("id"))
        if all(all(f in h for f in OWN_FIELDS) for h in own):
            errors += [f"{r['id']}: {e}" for e in same(own, " (el requisito)")]
    marked = 0
    for r in reqs:
        if any(not all(f in h for f in OWN_FIELDS) for h in r.get("hints", [])):
            continue
        found = find(r, valid)
        for i, (ka, a) in enumerate(found):  # the same check, on what reaches the requirement by different keys
            for kb, b in found[i + 1:]:
                shared = set(a["propiedad"]) & set(b["propiedad"])
                if a.get("para", ka) != b.get("para", kb) and shared and set(a["ac"]) & set(b["ac"]):
                    warnings.append(f"{r['id']}: {a['id']} y {b['id']} le llegan por llaves distintas con la misma "
                                    f"propiedad ({', '.join(sorted(shared))}) y el mismo AC: ¿dicen lo mismo?")
        mark = r.get("comparison")
        if mark is None:
            continue
        marked += 1
        if mark.get("mark") == "no":
            useless = [h["id"] for _, h in found if h["ac"] == ["Comparabilidad"]]
            if useless:
                warnings.append(f"{r['id']}: no se compara y le llegan pistas solo de Comparabilidad: {', '.join(useless)}")
        if mark.get("mark") not in MARKS or not (mark.get("reason") or "").strip():
            errors.append(f"{r['id']}: marca de comparación sin valor sí/no o sin motivo")
        elif mark["mark"] == "no" and mark.get("case") not in CASES:
            errors.append(f"{r['id']}: «no se compara» sin su caso a, b o c")
        elif mark["mark"] == "sí" and "case" in mark:
            errors.append(f"{r['id']}: «se compara» no lleva caso")
    warnings.append(f"{marked} de {len(reqs)} requisitos con marca de comparación")
    return errors, warnings


def cmd_check() -> None:
    catalog, reqs = load_hints(), requirements()
    errors, warnings = check(catalog, reqs, set(load_traits()["vocabulary"]))
    live = [h for h in catalog.get("hints", []) if "retirada" not in h]
    own = [h for r in reqs for h in r.get("hints", []) if "retirada" not in h]
    print(f"pistas {catalog.get('version', '?')}: {len(live)} vigentes en el catálogo y {len(own)} en los requisitos; "
          f"{len(errors)} errores")
    for line in errors:
        print(f"  ERROR {line}")
    for line in warnings:
        print(f"  {line}")
    if errors:
        raise SystemExit(1)


def cmd_find(ids: list) -> None:
    hints, by_id = load_hints().get("hints", []), {r["id"]: r for r in requirements()}
    for rid in ids:
        r = by_id.get(rid)
        if r is None:
            raise SystemExit(f"model: {rid} no está en el catálogo")
        found = find(r, hints)
        mark = r.get("comparison") or {}
        label = {"sí": "se compara", "no": f"no se compara ({mark.get('case')})"}.get(mark.get("mark"), "sin marca")
        print(f"{rid} [{r.get('trait') or '—'} × {r['entity']}] · {label} · {len(found)} pistas")
        for key, h in found:
            print(f"  {h['id']:<6} {key:<9} {'/'.join(h['propiedad']):<8} {', '.join(h['ac'])}")
