"""Resolving information of the requirements (D-062 to D-064): the contributions that can resolve each one.

Four origins (D-063): the framework (general layer, from the law), the references (titles and
descriptions of the sources, which whoever drafts a block turns into contributions), the real
pages (a contribution the classifier proposes is accepted when two different stores publish it
and it contributes to a component of the question) and the inferred ones (provisional until two
different stores publish them too, D-193). No
contribution is withdrawn for not being observed: the stores where each one was seen are
evidence, not a weight.
"""
from urllib.parse import urlparse

from references.read import ptd, shopify_attributes
from references.store import RefsError

from .text import stems

SKIP = {"marketplace_id", "language_tag"}
MIN_STORES = 2  # D-063: two different stores, not two pages
ORIGINS = ("marco", "referencias", "fichas", "inferida")


def store(url: str) -> str:
    """The store of a page: its host without «www.»."""
    return urlparse(url or "").netloc.lower().removeprefix("www.")


def _values(node, out=None) -> list:
    """The enum values of a schema node, without the units of its measures."""
    out = [] if out is None else out
    if isinstance(node, dict):
        if isinstance(node.get("enum"), list):
            out.extend(node.get("enumNames") or node["enum"])
        for k, v in node.items():
            if k != "unit":
                _values(v, out)
    elif isinstance(node, list):
        for v in node:
            _values(v, out)
    return out


def _properties(node) -> dict:
    node = node.get("items", node) if isinstance(node, dict) else {}
    return node.get("properties", {}) if isinstance(node, dict) else {}


def reference_info(source: str):
    """Title, description, parts and values of a reference source, for drafting its contributions, or None."""
    kind, _, rest = source.partition(":")
    try:
        if kind == "shopify-attr":
            handle, _, value = rest.partition("=")
            attr = shopify_attributes().get(handle)
            if attr is None:
                return None
            return {"source": source, "title": attr.get("name"), "description": attr.get("description"), "parts": [],
                    "values": [value] if value else [v["name"] for v in attr.get("values", [])]}
        if kind == "amazon-ptd-prop":
            path, _, value = rest.partition("=")
            product_type, *names = path.split(".")
            node = ptd(product_type)[0].get(names[0]) if names else None
            for name in names[1:]:
                node = _properties(node).get(name) if node else None
            if node is None:
                return None
            parts = [{"name": k, "title": v.get("title"), "description": v.get("description")}
                     for k, v in _properties(node).items() if k not in SKIP and k != "value"]
            return {"source": source, "title": node.get("title"), "description": node.get("description"), "parts": parts,
                    "values": [value] if value else _values(node)}
    except RefsError:
        return None
    return None


def contribution(fact: dict):
    """The contribution a declared fact instantiates, normalised: {contribution, component, new} or None.

    The classifier writes the name of a contribution of the requirement's list, or proposes one:
    {"new": name, "component": the part of the question it contributes to}."""
    c = fact.get("contribution")
    if isinstance(c, str) and c.strip():
        return {"contribution": c.strip(), "component": None, "new": False}
    if isinstance(c, dict) and (c.get("new") or "").strip():
        return {"contribution": c["new"].strip(), "component": (c.get("component") or "").strip() or None, "new": True}
    return None


def same(a: str, b: str) -> bool:
    """Two names of one contribution: they share at least half of their significant words (a shared «plazo» does not
    make «plazo de cambio» the «plazo para desistir o devolver»)."""
    sa, sb = stems(a), stems(b)
    if not sa or not sb:
        return (a or "").strip().lower() == (b or "").strip().lower()
    return len(sa & sb) / len(sa | sb) >= 0.5


def observations(models: dict) -> dict:
    """By requirement, the contributions the pages declared, grouped by name: names, components, stores, cases."""
    out = {}
    for cases in models.values():
        for case, model in cases.items():
            shop = store(model.get("url"))
            for c in model.get("coverage", {}).get("contributions", []):
                groups = out.setdefault(c["answers"], [])
                group = next((g for g in groups if same(c["contribution"], g["name"])), None)
                if group is None:
                    group = {"name": c["contribution"], "components": {}, "stores": set(), "cases": set(), "new": False}
                    groups.append(group)
                group["stores"].add(shop)
                group["cases"].add(case)
                group["new"] |= c["new"]
                if c.get("component"):
                    group["components"][c["component"]] = group["components"].get(c["component"], 0) + 1
    return out


def induce(questions: dict, models: dict) -> dict:
    """Per requirement with a list or with observations: the stores where each listed contribution was seen, the
    ones never observed, and the proposed ones: accepted (two stores, a component of the question), pending (one
    store) or rejected (no component of the question). `questions` maps requirement id to requirement."""
    seen = observations(models)
    result = {}
    for req, r in questions.items():
        listed = [c["contribution"] for c in r.get("resolving_info", [])]
        groups = seen.get(req, [])
        if not listed and not groups:
            continue
        entry = {"observed": {}, "accepted": [], "proposed": [], "rejected": []}
        for g in groups:
            stores = sorted(g["stores"])
            match = next((name for name in listed if same(g["name"], name)), None)
            if match:
                entry["observed"][match] = sorted(set(entry["observed"].get(match, [])) | set(stores))
                continue
            component = max(g["components"], key=g["components"].get) if g["components"] else None
            item = {"contribution": g["name"], "component": component, "stores": stores, "cases": sorted(g["cases"])}
            if not component or not stems(component) & stems(r.get("question", "")):
                entry["rejected"].append({**item, "reason": "no aporta a un componente de la pregunta"})
            elif len(stores) >= MIN_STORES:
                entry["accepted"].append(item)
            else:
                entry["proposed"].append(item)
        entry["never_observed"] = [name for name in listed if name not in entry["observed"]]
        # D-193: an inferred contribution observed in two different stores is no longer provisional
        entry["inferred_accepted"] = [c["contribution"] for c in r.get("resolving_info", [])
                                      if c.get("origin") == "inferida"
                                      and len(entry["observed"].get(c["contribution"], [])) >= MIN_STORES]
        result[req] = entry
    return result


def for_model(r: dict, compiled: dict) -> list:
    """The resolving information of a requirement in a model: its list plus the contributions accepted from the
    pages, each with the stores where it was observed."""
    entry = compiled.get("requirements", {}).get(r["id"], {})
    observed = entry.get("observed", {})
    confirmed = set(entry.get("inferred_accepted", []))
    out = [{**c, "stores": observed.get(c["contribution"], []),
            **({"status": "aceptada"} if c["contribution"] in confirmed else
               {"status": "provisional"} if c.get("origin") == "inferida" else {})}
           for c in r.get("resolving_info", [])]
    out += [{"contribution": a["contribution"], "component": a["component"], "origin": "fichas", "support": a["cases"],
             "stores": a["stores"]} for a in entry.get("accepted", [])]
    return out
