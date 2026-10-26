"""Selection of the training catalog (T-024, OQ-48): product pages of a store, a few of each
product type and as many types as possible.

  discover (container, capture engine): legitimacy of the site and every product URL of its
            sitemaps, read from the site's own window; kept in var/training/<store>/.
  select   (host, deterministic): one page per product (variants share its id), grouped by
            department and product type, drawn with a fixed seed; written to training/selection/.

The product type is the first word of the product name in the URL, skipping the words of a
spec's stoplist ("juego de 2 vasos" → vaso), in the singular; in the departments whose names are titles (books,
films) the type is the department. It is a proxy known before capturing: the class of each page
is the one the classifier gives it.
"""
from __future__ import annotations

import datetime
import gzip
import json
import random
import re
from collections import defaultdict
from pathlib import Path

from .. import ROOT
from ..capture.robots import Robots

SELECTIONS = ROOT / "training" / "selection"
DISCOVERIES = ROOT / "var" / "training"


class SelectionError(Exception):
    pass


def read_spec(path: Path) -> dict:
    spec = json.loads(Path(path).read_text(encoding="utf-8"))
    for key in ("store", "base_url", "sitemap", "product", "follow_products", "seed", "categories",
                "per_category"):
        if key not in spec:
            raise SelectionError(f"{path}: falta «{key}»")
    return spec


# ---------------------------------------------------------------- discover (container)

def discover(spec: dict, browser=None) -> Path:
    """check_site and the product and category URLs of the sitemaps → var/training/<store>/discovery-<stamp>/."""
    from ..capture import profile, sitemaps
    from ..capture.browser import Browser
    from ..capture.files import now, stamp, write_json
    from ..capture.legitimacy import check_site

    folder = DISCOVERIES / spec["store"] / f"discovery-{stamp()}"
    folder.mkdir(parents=True)
    own = browser is None
    if own:
        browser = Browser(profile())
        browser.start()
    page = browser.new_window()
    rng = random.Random()
    try:
        check = check_site(page, spec["base_url"], folder, 20, rng)
        write_json(folder / "check.json", check)
        if check["verdict"] != "ok":
            raise SelectionError(f"{spec['base_url']}: veredicto {check['verdict']} ({'; '.join(check['flags'])}); "
                                 f"evidencia en {folder}")
        found = {}
        for kind in ("products", "categories"):
            follow = spec.get(f"follow_{kind}")
            if not follow:
                continue
            page.idle(rng.uniform(3, 8))
            found[kind] = sitemaps.discover(page, spec["base_url"], [spec["sitemap"]], None, follow,
                                            spec.get("limit", 2_000_000), rng, budget=spec.get("budget", 120))
    finally:
        browser.close_window(page)
        if own:
            browser.stop()
    for kind, result in found.items():
        (folder / f"{kind}.json.gz").write_bytes(gzip.compress(json.dumps(
            sorted({u["loc"] for u in result["urls"]})).encode("utf-8")))
    write_json(folder / "discovery.json", {
        "store": spec["store"], "at": now(), "sitemap": spec["sitemap"], "verdict": check["verdict"],
        "flags": check["flags"], **{kind: {"urls": len(r["urls"]), "sitemaps": r["sitemaps"],
                                           "pending_sitemaps": r["pending_sitemaps"]} for kind, r in found.items()}})
    return folder


def shown(path: Path) -> str:
    """A path relative to demand-engine/ when it is inside it."""
    try:
        return str(Path(path).resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def latest_discovery(store: str) -> Path:
    found = sorted((DISCOVERIES / store).glob("discovery-*/discovery.json"))
    if not found:
        raise SelectionError(f"no hay descubrimiento de {store}: train discover SPEC")
    return found[-1].parent


# ---------------------------------------------------------------- select (host)

def singular(word: str) -> str:
    """Spanish plural → singular, enough to group types: anillos → anillo, calcetines → calcetin."""
    if word.endswith("es") and len(word) > 4 and word[-3] in "lnrdzj":
        return word[:-2]
    if word.endswith("s") and len(word) > 3 and not word.endswith("ss"):
        return word[:-1]
    return word


def product_type(slug: str, stop: set) -> str | None:
    for word in slug.split("-"):
        if len(word) > 1 and not word.isdigit() and word not in stop:
            return singular(word)
    return None


def products(urls: list, spec: dict) -> tuple[dict, dict]:
    """One page per product of the departments in scope: {product id: {...}} and the counts.
    robots.txt is checked when drawing, on the pages drawn only."""
    pattern = re.compile(spec["product"])
    excluded, titles = set(spec.get("exclude_departments", [])), set(spec.get("title_departments", []))
    stop, excluded_types = set(spec.get("stopwords", [])), set(spec.get("exclude_types", []))
    counts = defaultdict(int)
    chosen = {}
    for url in sorted(urls):
        m = pattern.match(url)
        if not m:
            counts["not_product"] += 1
            continue
        dept = m["dept"]
        if dept in excluded:
            counts["excluded_department"] += 1
            continue
        if m["id"] in chosen:
            counts["variant"] += 1
            continue
        kind = dept if dept in titles else product_type(m["slug"], stop)
        if not kind or kind in excluded_types:
            counts["no_type" if not kind else "excluded_type"] += 1
            continue
        chosen[m["id"]] = {"product": m["id"], "url": url, "department": dept, "type": kind}
    counts["products"] = len(chosen)
    return chosen, dict(counts)


def store_category(dept: str, kind: str, categories: list) -> str | None:
    """The store's category that names the type (the shortest path), if any: for reading only."""
    stem = kind[:max(4, len(kind) - 2)]
    hits = [c for c in categories
            if f"/{dept}/" in c and any(w.startswith(stem) for w in c.rstrip("/").rsplit("/", 1)[-1].split("-"))]
    return min(hits, key=lambda c: (c.count("/"), c)) if hits else None


def page_id(spec: dict, item: dict) -> str:
    return f"{spec['store']}-{item['type']}-{item['product'].lower().replace('_', '')}"[:40].rstrip("-")


def select(spec: dict, discovery: Path) -> dict:
    robots = Robots((discovery / "robots.txt").read_text(encoding="utf-8"), 200)
    urls = json.loads(gzip.decompress((discovery / "products.json.gz").read_bytes()))
    cats_file = discovery / "categories.json.gz"
    store_cats = json.loads(gzip.decompress(cats_file.read_bytes())) if cats_file.exists() else []
    chosen, counts = products(urls, spec)
    counts["disallowed"] = 0

    groups = defaultdict(list)
    for item in chosen.values():
        groups[(item["department"], item["type"])].append(item)
    need = spec["per_category"] + spec.get("reserves", 0)
    floor = max(need, spec.get("min_products", 0))
    named = {}
    eligible = defaultdict(list)
    for (dept, kind), items in groups.items():
        if len(items) < floor:
            continue
        named[(dept, kind)] = store_category(dept, kind, store_cats)
        if named[(dept, kind)] or not spec.get("require_store_category"):
            eligible[dept].append(kind)

    rng = random.Random(spec["seed"])
    depts = sorted(eligible)
    rng.shuffle(depts)
    for dept in depts:
        eligible[dept].sort()
        rng.shuffle(eligible[dept])
    order = []  # round robin over the departments: as many departments as possible
    for r in range(max((len(v) for v in eligible.values()), default=0)):
        order += [(d, eligible[d][r]) for d in depts if r < len(eligible[d])]

    categories, taken = [], set()
    for dept, kind in order:
        if len(categories) == spec["categories"]:
            break
        if kind in taken:  # the same type in another department
            continue
        items = sorted(groups[(dept, kind)], key=lambda i: i["product"])
        rng.shuffle(items)
        picked = []
        for item in items:
            if len(picked) == need:
                break
            if robots.allowed(item["url"]):
                picked.append({"id": page_id(spec, item), **item})
            else:
                counts["disallowed"] += 1
        if len(picked) < need:  # robots.txt leaves too few
            continue
        taken.add(kind)
        categories.append({
            "category": f"{dept}/{kind}", "department": dept, "type": kind,
            "store_category": named[(dept, kind)],
            "products_in_store": len(items), "pilot": len(categories) < spec.get("pilot", 0),
            "pages": picked[:spec["per_category"]], "reserves": picked[spec["per_category"]:]})

    meta = json.loads((discovery / "discovery.json").read_text(encoding="utf-8"))
    return {
        "store": spec["store"], "created": datetime.date.today().isoformat(), "seed": spec["seed"],
        "discovery": {"folder": shown(discovery), "at": meta["at"], "flags": meta["flags"]},
        "counts": {"urls": len(urls), **counts, "types": len(groups),
                   "eligible_types": sum(len(v) for v in eligible.values()), "departments": len(depts),
                   "selected_types": len(categories),
                   "selected_departments": len({c["department"] for c in categories}),
                   "pages": sum(len(c["pages"]) for c in categories),
                   "pilot_pages": sum(len(c["pages"]) for c in categories if c["pilot"])},
        "categories": categories,
    }


def pages_of(selection: dict, pilot_only: bool = False) -> list:
    """The pages to capture, in the order of the selection."""
    return [p for c in selection["categories"] if c["pilot"] or not pilot_only for p in c["pages"]]


def write_selection(spec_path: Path, selection: dict) -> Path:
    out = SELECTIONS / f"{selection['store']}-{selection['created']}.json"
    selection = {"spec": shown(spec_path), **selection}
    out.write_text(json.dumps(selection, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return out
