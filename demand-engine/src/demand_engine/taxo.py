"""Look up the frozen references and product pages while composing a study class.

Reads the pinned version of each source (var/refs/pins.json). Read-only except
`page fetch`, which freezes a product page under var/pages/.

Usage:
  taxo shopify REGEX                 Shopify categories whose full name matches
  taxo category ID [--all-values] [--own]
                                     a Shopify category: ancestors, children, Google
                                     mapping and its base (own and inherited attributes);
                                     --own lists only its own attributes (one cat. block)
  taxo gen                           the general layer of the catalog (catalog/gen.json)
  taxo values REGEX                  Shopify attribute values that match, by attribute,
                                     with how many categories carry the attribute
  taxo google REGEX                  Google categories that match
  taxo amazon REGEX [--depth N]      Amazon.es browse nodes whose path matches, with PTD
  taxo ptd TYPE [REGEX] [--enum PROP ...] [--all-groups]
                                     PTD properties (group, name, title, values);
                                     --enum prints the full value list of PROP
  taxo page fetch ID URL             freeze a product page as var/pages/ID.html with the
                                     capture engine (on the host it runs in the container)
  taxo page facts ID [KEYWORD ...]   JSON-LD Product, breadcrumb and lines with keywords
  taxo page section ID HEADING [N]   the N text lines that follow a heading
  taxo page grep ID REGEX            text lines of the page that match

The base of a Shopify category is its own attributes plus those of all its
ancestors. Shopify labels repeat in Spanish (e.g. two «Cubrecolchones»): work by ID.
"""
import argparse
import gzip
import html
import json
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

from . import ROOT, pages
from .pages import PageError
from .refs import (RefsError, enum_values, google_mapping, google_names, pinned, ptd, shopify_attributes,
                   shopify_categories, short)

SKIP_GROUPS = {"images", "offer", "shipping", "variations", "safety_and_compliance", "compliance"}
VALUES_SHOWN = 25


def fail(msg: str) -> None:
    sys.exit(f"taxo: {msg}")


# --- Shopify ------------------------------------------------------------------

def cmd_shopify(args) -> None:
    rx = re.compile(args.regex, re.I)
    for k, c in shopify_categories().items():
        if rx.search(c["full_name"]):
            print(f"{k} | {c['full_name']} | hijos: {len(c['children'])}")


def cmd_category(args) -> None:
    cats, attrs = shopify_categories(), shopify_attributes()
    if args.id not in cats:
        fail(f"no existe la categoría {args.id}")
    c = cats[args.id]
    print(f"{args.id} | {c['full_name']}")
    mapping = google_mapping().get(args.id)
    if mapping:
        english, outputs = mapping
        names = google_names()
        print(f"  inglés: {english}")
        print("  Google (mapeo oficial): " + "; ".join(f"{g} {names.get(g, n)}" for g, n in outputs))
    if c["children"]:
        print("  hijas: " + "; ".join(f"{short(h['id'])} {h['name']}" for h in c["children"]))
    ancestors = [short(a["id"]) for a in c.get("ancestors", [])]
    print("  madres: " + (" > ".join(f"{a} {cats[a]['name']}" for a in reversed(ancestors)) or "—"))
    seen = {}
    for owner in [args.id] + ([] if args.own else ancestors):
        for a in cats[owner]["attributes"]:
            seen.setdefault(a["handle"], owner)
    print(f"  base: {len(seen)} atributos ({len(cats[args.id]['attributes'])} propios)")
    for handle, owner in seen.items():
        full = attrs.get(handle, {})
        values = [v["name"] for v in full.get("values", [])]
        shown = values if args.all_values else values[:VALUES_SHOWN]
        origin = "propio" if owner == args.id else f"heredado de {owner}"
        more = f" … +{len(values) - len(shown)}" if len(values) > len(shown) else ""
        print(f"  - {full.get('name', handle)} ({handle}) [{origin}]: {shown}{more}")
        if full.get("description"):
            print(f"      {full['description']}")


def cmd_gen(args) -> None:
    catalog = json.loads((ROOT / "catalog/gen.json").read_text(encoding="utf-8"))
    for b in catalog["blocks"]:
        print(f"{b['id']} | {b['name']}" + (f" | disparador: {b['trigger']}" if b["trigger"] else ""))
        for r in b["requirements"]:
            print(f"  {r['id']} [{r['importance'] or 'por fijar'}] ({r['entity']}) {r['question']}")


def cmd_values(args) -> None:
    rx = re.compile(args.regex, re.I)
    carriers = {}
    for k, c in shopify_categories().items():
        for a in c["attributes"]:
            carriers.setdefault(a["handle"], []).append(k)
    for handle, a in shopify_attributes().items():
        hits = [v["name"] for v in a.get("values", []) if rx.search(v["name"])]
        if hits:
            used = carriers.get(handle, [])
            print(f"{a['name']} ({handle}): {hits[:10]} | en {len(used)} categorías: {used[:6]}")


def cmd_google(args) -> None:
    rx = re.compile(args.regex, re.I)
    for gid, path in google_names().items():
        if rx.search(path):
            print(f"{gid} - {path}")


# --- Amazon -------------------------------------------------------------------

def cmd_amazon(args) -> None:
    rx = re.compile(args.regex, re.I)
    rows = set()
    with gzip.open(pinned("amazon-btg") / "browse_tree.es.xml.gz") as f:
        for _, el in ET.iterparse(f):
            if el.tag == "Node":
                path = el.findtext("browsePathByName") or ""
                if rx.search(path) and path.count(",") < args.depth:
                    rows.add((path, el.findtext("browseNodeId"), el.findtext("productTypeDefinitions") or "—",
                              el.findtext("hasChildren") == "true"))
                el.clear()
    for path, nid, ptd_name, children in sorted(rows):
        print(f"{nid} | {path.replace(',', ' > ')} | PTD {ptd_name}" + (" | tiene hijos" if children else ""))


def cmd_ptd(args) -> None:
    props, definition = ptd(args.type)
    if args.enum:
        for name in args.enum:
            p = props.get(name)
            print(f"{name} | {p.get('title', '') if p else '—'} | {enum_values(p) if p else 'no existe'}")
        return
    rx = re.compile(args.regex, re.I) if args.regex else None
    print(f"{args.type} {definition.get('displayName', '')} | {len(props)} propiedades")
    for group, g in definition["propertyGroups"].items():
        if group in SKIP_GROUPS and not args.all_groups:
            continue
        for name in g.get("propertyNames", []):
            p = props[name]
            title = p.get("title", "")
            if rx and not rx.search(f"{name} {title}"):
                continue
            values = enum_values(p)
            shown = f" | {values[:15]}" + (f" … +{len(values) - 15}" if len(values) > 15 else "") if values and len(values) < 400 else ""
            print(f"  [{group}] {name} | {title}{shown}")


# --- Pages --------------------------------------------------------------------

def cmd_page_fetch(args) -> None:
    if not pages.engine_available():
        # On the host: the capture engine (Chrome, websockets) runs in the container
        code = subprocess.call([str(ROOT.parent / "bin/run"), "dev", "exec", "python", "-m", "demand_engine.taxo",
                                "page", "fetch", args.id, args.url])
        if code:
            print("taxo: page fetch se ejecuta en el contenedor; si no está levantado: bin/run dev up", file=sys.stderr)
        sys.exit(code)
    info = pages.fetch(args.id, args.url)
    print(f"{args.id}: {info['size']} bytes (DOM renderizado, HTTP {info['http_status']}); instantánea en {info['snapshot']}")


def cmd_page_facts(args) -> None:
    raw = pages.read(args.id)
    print("TITLE:", (re.search(r"<title>(.*?)</title>", raw, re.S) or [None, ""])[1].strip())
    for data in pages.json_ld(raw):
        for node in pages.walk(data):
            kind = node.get("@type")
            kinds = kind if isinstance(kind, list) else [kind]
            if "Product" in kinds or "ProductGroup" in kinds:
                print("PRODUCT:", {k: node.get(k) for k in ("name", "category", "material", "color", "size", "brand") if node.get(k)})
                print("  description:", html.unescape(re.sub(r"<[^>]+>", " ", str(node.get("description", ""))))[:1500])
                for p in node.get("additionalProperty", []) or []:
                    print("  property:", p.get("name"), "=", p.get("value"))
            if "BreadcrumbList" in kinds:
                print("BREADCRUMB:", " > ".join(str(i.get("name") or (i.get("item") or {}).get("name", ""))
                                                for i in node.get("itemListElement", [])))
    lines = pages.text_lines(raw)
    for kw in args.keywords:
        for i in [i for i, l in enumerate(lines) if kw.lower() in l.lower()][:2]:
            print(f"[{kw}]", " | ".join(lines[i:i + 8])[:600])


def cmd_page_section(args) -> None:
    lines = pages.text_lines(pages.read(args.id))
    found = False
    for i, l in enumerate(lines):
        if l.lower() == args.heading.lower():
            print(" | ".join(lines[i:i + args.n]))
            found = True
    if not found:
        print(f"no hay ninguna línea igual a «{args.heading}»; prueba: taxo page grep {args.id} REGEX")


def cmd_page_grep(args) -> None:
    rx = re.compile(args.regex, re.I)
    for l in pages.text_lines(pages.read(args.id)):
        if rx.search(l):
            print(l[:600])


def main() -> None:
    parser = argparse.ArgumentParser(prog="taxo", description="Consulta de referencias y páginas para componer clases.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("shopify"); p.add_argument("regex"); p.set_defaults(func=cmd_shopify)
    p = sub.add_parser("category"); p.add_argument("id"); p.add_argument("--all-values", action="store_true")
    p.add_argument("--own", action="store_true"); p.set_defaults(func=cmd_category)
    p = sub.add_parser("gen"); p.set_defaults(func=cmd_gen)
    p = sub.add_parser("values"); p.add_argument("regex"); p.set_defaults(func=cmd_values)
    p = sub.add_parser("google"); p.add_argument("regex"); p.set_defaults(func=cmd_google)
    p = sub.add_parser("amazon"); p.add_argument("regex"); p.add_argument("--depth", type=int, default=99)
    p.set_defaults(func=cmd_amazon)
    p = sub.add_parser("ptd"); p.add_argument("type"); p.add_argument("regex", nargs="?")
    p.add_argument("--enum", nargs="+", metavar="PROP"); p.add_argument("--all-groups", action="store_true")
    p.set_defaults(func=cmd_ptd)
    page = sub.add_parser("page").add_subparsers(dest="page_cmd", required=True)
    p = page.add_parser("fetch"); p.add_argument("id"); p.add_argument("url"); p.set_defaults(func=cmd_page_fetch)
    p = page.add_parser("facts"); p.add_argument("id"); p.add_argument("keywords", nargs="*")
    p.set_defaults(func=cmd_page_facts)
    p = page.add_parser("section"); p.add_argument("id"); p.add_argument("heading"); p.add_argument("n", nargs="?", type=int, default=30)
    p.set_defaults(func=cmd_page_section)
    p = page.add_parser("grep"); p.add_argument("id"); p.add_argument("regex"); p.set_defaults(func=cmd_page_grep)
    args = parser.parse_args()
    try:
        args.func(args)
    except (RefsError, PageError) as exc:
        fail(str(exc))


if __name__ == "__main__":
    main()
