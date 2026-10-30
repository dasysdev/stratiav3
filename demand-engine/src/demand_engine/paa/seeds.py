"""Seeds of the PAA phase of an execution (D-224): paa seeds MODEL.json [--set SET] [--trait ATTR] [--values V ...]
[--seed KEY=TEXT ...].

The class of the set is the key of the assembled model: one set per distinct key (D-116). A set of the same key is
used as it is; nothing is written. The seeds follow the rule of the README (seed strategy) and come from the key and
from the references that taxo reads (Shopify, the pinned version in references/):
  core     one seed per category of the composition (the nearest block of each class in the key; the sector blocks
           are not) and per specialization of the key, with the name of its Shopify category; a set, «juego de …»
  values   one seed per chosen value of the trait, a Shopify attribute that the classes carry: «<first core seed> de
           <value>»
The rule is calibrated with textiles (README): in a model that the textile regulation reaches (a requirement cites
ley:UE-1007/2011, D-043.6), the trait is the fabric (Shopify «fabric», else «material»). In any other class the code
does not choose it: who chooses it, and how, is open (OQ-93); --trait gives it.
The values with use in Spain and the name of each seed in the Spanish market are a judgment, as in the sets of paa/:
--values chooses them among the values of taxo (ATTR=VALUE, a value of another attribute of the classes), and
--seed KEY=TEXT renames a seed (KEY: the block of a core seed, or a value). Without --values nothing is written: the
command shows what taxo gives.
Standard library only: it runs on the host.
"""
from __future__ import annotations

import datetime
import json
from pathlib import Path

from capture.files import read_json
from references.read import shopify_attributes, shopify_categories

from .. import ROOT
from ..demand.catalog import TEXTILE_LAW, category_name, chain
from .store import DEFAULTS, SeedSet, StoreError, find_capture, sets_dir, slug
from .text import norm

CORE = "núcleo"
CALIBRATED = ("fabric", "material")  # README, rule 2: in textiles, the material (Shopify fabric/material)
RULE = ("Regla vigente (README del motor PAA, estrategia de semillas; D-224), con «paa seeds»: núcleo (la categoría de "
        "cada clase en la clave, sin las de sector, y cada especialización de la clave) + valores del rasgo que más "
        "condiciona las prestaciones, de las referencias de taxo.")
MAX_ID = 60


def key_of(model: dict) -> list[str]:
    """The blocks of the key of a model, without their versions: the class of a PAA set (D-116, D-224)."""
    return [k.split("@")[0] for k in model["key"]["model"]]


def requirements(model: dict) -> list[dict]:
    return [r for b in model.get("general", []) + model.get("blocks", []) for r in b["requirements"]] + \
        model.get("inferred", [])


def textile(model: dict) -> str | None:
    """The requirement of the model that cites the textile regulation (D-043.6), or None."""
    return next((r["id"] for r in requirements(model) if any(s.startswith(TEXTILE_LAW) for s in r.get("sources", []))),
                None)


def carried(classes: list[str]) -> dict:
    """The Shopify attributes of the classes, own and inherited (the base that «taxo category» shows): handle → class."""
    cats, out = shopify_categories(), {}
    for c in classes:
        for owner in reversed(chain(c)):
            for a in cats.get(owner, {}).get("attributes", []):
                out.setdefault(a["handle"], c)
    return out


def lower(name: str) -> str:
    return name[:1].lower() + name[1:]


def core(model: dict) -> list[dict]:
    """The core seeds from taxo: the nearest block of each class (its own, else the closest ancestor with one) and
    each specialization of the key. [{key, q}, …; a specialization also with its name and order]"""
    by_node = {b["shopify"]: b for b in model["blocks"] if b.get("shopify")}
    out, seen = [], set()
    for c in model["composition"]["classes"]:
        node = next((n for n in reversed(chain(c)) if n in by_node), None)
        if node and by_node[node]["id"] not in seen:
            seen.add(by_node[node]["id"])
            out.append({"key": by_node[node]["id"], "q": lower(category_name(node))})
    main = out[0]["q"] if out else lower(model["name"].split(" › ")[-1])
    for b in model["blocks"]:
        if b["type"] == "especialización":
            spec = {"key": b["id"], "name": b.get("name") or b["id"].removeprefix("esp."), "order": b.get("order")}
            out.append({**spec, "q": specialized(spec, main)})
    return out


def specialized(spec: dict, main: str) -> str:
    """The seed of a specialization from the first core seed: «juego de …» for a set, else «… <name>»."""
    return f"juego de {main}" if spec.get("order") == "juego" else f"{main} {spec['name']}"


def values_of(handle: str) -> list[str]:
    """The values of a Shopify attribute, once each."""
    out, seen = [], set()
    for v in shopify_attributes().get(handle, {}).get("values", []):
        if norm(v["name"]) not in seen:
            seen.add(norm(v["name"]))
            out.append(v["name"])
    return out


def trait_for(model: dict, attrs: dict, chosen: str | None) -> tuple:
    """(handle, why) of the trait of the values: the one given, or the calibrated one in a textile class; (None, why)
    if the code may not choose it (OQ-93)."""
    if chosen:
        if chosen not in attrs:
            raise StoreError(f"el atributo «{chosen}» no es de las clases del modelo ({', '.join(sorted(attrs))})")
        return chosen, "--trait"
    law = textile(model)
    handle = next((h for h in CALIBRATED if h in attrs), None)
    if law and handle:
        return handle, f"regla calibrada, clase textil: {law} cita {TEXTILE_LAW} (README, regla 2)"
    return None, ("clase sin calibrar: el código no elige el rasgo de los valores (OQ-93); elige uno con --trait "
                  "entre los atributos de las clases")


def renames(pairs: list[str]) -> dict:
    out = {}
    for p in pairs or []:
        key, sep, text = p.partition("=")
        if not sep or not key.strip() or not text.strip():
            raise StoreError(f"--seed «{p}»: CLAVE=TEXTO")
        out[key.strip()] = text.strip()
    return out


def model_ref(path: Path) -> str:
    """The model as the sets name it: its .model.md, from the root of the repository."""
    md = path.resolve().with_name(path.name.replace(".model.json", ".model.md"))
    try:
        return str(md.relative_to(ROOT.parent))
    except ValueError:
        return str(md)


def set_key(set_id: str) -> list[str] | None:
    """The key of an existing set: its «key», else the key of its model (if the model is still there)."""
    spec = SeedSet(set_id).definition()
    if spec.get("key"):
        return spec["key"]
    if not spec.get("model"):
        return None
    path = ROOT.parent / spec["model"]
    model = read_json(path.with_name(path.name.replace(".model.md", ".model.json")))
    return key_of(model) if model else None


def plan(model_path: Path, set_id: str | None = None, trait: str | None = None, values: list | None = None,
         seeds: list | None = None) -> dict:
    """What «paa seeds» does with a model: the set (an existing one of the same key, or a new one) and, for a new one,
    its seeds from taxo, with the choices given. Writes nothing."""
    model = read_json(model_path)
    if not model or "key" not in model:
        raise StoreError(f"{model_path}: no es un modelo ensamblado")
    key = key_of(model)
    label = model["name"].split(" › ")[-1]
    keys = {s: set_key(s) for s in SeedSet.ids()}
    same = next((s for s, k in keys.items() if k and set(k) == set(key)), None)
    if same and set_id not in (None, same):
        raise StoreError(f"la clave ya tiene el conjunto {same} (D-116): no se crea otro")
    out = {"model": model, "key": key, "class": label, "existing": same, "set": same}
    if same:
        return out
    if set_id and set_id in keys:
        raise StoreError(f"ya existe el conjunto {set_id}, de otra clave")
    base = set_id or slug(label)[:MAX_ID].strip("-")
    out["set"] = base if base not in keys else next(f"{base}-{i}" for i in range(2, 100) if f"{base}-{i}" not in keys)
    names = renames(seeds)
    nucleus = core(model)
    attrs = carried(model["composition"]["classes"])
    handle, why = trait_for(model, attrs, trait)
    out.update(core=nucleus, attributes=attrs, trait=handle, why=why, values=[], seeds=[],
               related={s: [x["q"] for x in SeedSet(s).seeds()] for s, k in keys.items()
                        if k and {c["key"] for c in nucleus} & set(k)})
    if handle:
        out["taxo_values"] = values_of(handle)
        for v in values or []:
            attr, _, name = v.partition("=") if "=" in v else (handle, "", v)
            known = {norm(x): x for x in values_of(attr)} if attr in attrs else {}
            if norm(name) not in known:
                raise StoreError(f"«{v}» no es un valor de «{attr}» en taxo" + ("" if attr in attrs else
                                 " (el atributo no es de las clases del modelo)"))
            out["values"].append((attr, known[norm(name)]))
    by_key = {norm(k): t for k, t in names.items()}
    unknown = set(by_key) - {norm(c["key"]) for c in nucleus} - {norm(v) for _, v in out["values"]}
    if unknown:
        raise StoreError(f"--seed con claves que no son un bloque del núcleo ni un valor elegido: {', '.join(sorted(unknown))}")
    first = next((c for c in nucleus if "order" not in c), None)
    main = by_key.get(norm(first["key"]), first["q"]) if first else lower(label)
    group = lower(shopify_attributes().get(handle, {}).get("name", handle or ""))
    for c in nucleus:
        default = specialized(c, main) if "order" in c else c["q"]
        out["seeds"].append({"q": by_key.get(norm(c["key"]), default), "group": CORE, "from": c["key"]})
    for attr, v in out["values"]:
        out["seeds"].append({"q": by_key.get(norm(v), f"{main} de {v.lower()}"), "group": group,
                             "from": f"shopify-attr:{attr}={v}"})
    repeated = {norm(s["q"]) for s in out["seeds"] if [norm(x["q"]) for x in out["seeds"]].count(norm(s["q"])) > 1}
    if repeated:
        raise StoreError(f"semillas repetidas: {', '.join(sorted(repeated))}")
    market = DEFAULTS["market"]
    for s in out["seeds"]:
        found = find_capture(s["q"], market)
        s["_reuse"] = found[0] if found else None
    return out


def dump(data: dict) -> str:
    """The set as the sets of paa/ are written: one seed per line."""
    head = json.dumps({k: v for k, v in data.items() if k != "seeds"}, ensure_ascii=False, indent=2)
    seeds = ",\n".join("    " + json.dumps(s, ensure_ascii=False) for s in data["seeds"])
    return head[:-2] + ',\n  "seeds": [\n' + seeds + "\n  ]\n}\n"


def write(p: dict, model_path: Path) -> Path:
    """paa/<set>.json from a plan with its values chosen."""
    attr = shopify_attributes().get(p["trait"], {})
    data = {"class": p["class"], "model": model_ref(model_path), "key": p["key"],
            "rule": f"{RULE} Valores: {lower(attr.get('name', p['trait']))} (Shopify {p['trait']}; {p['why']}).",
            "trait": {"attribute": p["trait"], "name": attr.get("name"), "chosen": p["why"]},
            "generated": datetime.date.today().isoformat(), "clicks": DEFAULTS["clicks"],
            "seeds": [{k: v for k, v in s.items() if not k.startswith("_")} for s in p["seeds"]]}
    path = sets_dir() / f"{p['set']}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dump(data), encoding="utf-8")
    SeedSet(p["set"]).definition()  # what the engine reads
    return path
