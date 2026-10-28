"""refs: the frozen external sources of every system (D-149). Custody in store.py, kinds of
source in kinds/, readers in read.py.

Usage:
  refs [status]                      versions per source, the pinned one and who uses it
  refs check [SOURCE...]             has the source changed upstream? (stores nothing)
  refs fetch [SOURCE...] [--version V]
                                     download a new version (--version: the release of a
                                     Shopify, Schema.org or EU Vocabularies source, or the
                                     dated version of a law)
  refs diff SOURCE [OLD [NEW]] [--all]
                                     changes between two versions: nodes of a taxonomy, terms
                                     of the vocabulary, text of a document (default: pinned → latest)
  refs pin SOURCE VERSION            set the version every system works with; lists the systems
                                     that use the source and how each one reviews the change
  refs props SOURCE [TYPE] [--version V]
                                     the property tables of a document (Google Search): type,
                                     property, table (required or recommended), heading, expected type
  refs props SOURCE:Type.property@VERSION
                                     resolve a citation of a property (error if that version lacks it)
  refs law ley:CODE[-ARTICLE.APARTADO…][@VERSION]
                                     the passage of a law a citation names (error if it does not exist)
  refs law SOURCE [OLD NEW]          the parts of a law (articles, the rest by heading) that changed
                                     between two versions (default: pinned → latest)

SP-API credentials (Amazon sources) come from references/.env or the environment:
SPAPI_LWA_ID, SPAPI_LWA_SECRET, SPAPI_REFRESH_TOKEN.
REFS_DIR overrides the directory of the versions and SOURCES_FILE the registry (tests).
"""
import argparse
import sys
import time
import urllib.error

from .kinds import KINDS
from .kinds.document import INTERVAL
from .read import law_changes, law_citation, properties, property_citation
from .store import RefsError, manifest, pins, registry, save_pins, sources, sources_file, versions

DIFF_LIMIT = 40     # lines per section unless --all


def fail(msg: str) -> None:
    print(f"refs: {msg}", file=sys.stderr)
    sys.exit(1)


def selected(found: dict, names: list) -> list:
    unknown = [n for n in names if n not in found]
    if unknown:
        fail(f"fuente desconocida: {', '.join(unknown)} (ver {sources_file().name} o refs status)")
    return names or list(found)


def cmd_status(args) -> None:
    current = pins()
    found_sources = sources()
    width = max(map(len, found_sources))
    for sid, source in found_sources.items():
        uses = ", ".join(source["uses"])
        found = versions(sid)
        if not found:
            print(f"{sid:<{width}}  sin descargar · {uses}")
            continue
        pin = current.get(sid, "—")
        latest = manifest(sid, found[-1])
        newer = " · hay una versión posterior a la fijada" if found[-1] != pin else ""
        print(f"{sid:<{width}}  fijada {pin} · última {found[-1]} ({latest['fetched_at'][:10]}) · "
              f"{len(found)} versión(es){newer} · {uses}")


def cmd_check(args) -> None:
    found = sources()
    names = selected(found, args.sources)
    width = max(map(len, names))
    for sid in names:
        source = found[sid]
        try:
            print(f"{sid:<{width}}  {KINDS[source['kind']].check(sid, source)}", flush=True)
        except (urllib.error.URLError, RefsError) as e:
            print(f"{sid:<{width}}  no se pudo comprobar: {e}")
        if source["kind"] == "document":
            time.sleep(INTERVAL)


def cmd_fetch(args) -> None:
    found = sources()
    names = selected(found, args.sources)
    if args.version and (not args.sources or any(not KINDS[found[n]["kind"]].release for n in names)):
        fail("--version solo se aplica a las fuentes versionadas por release (Shopify, Schema.org, EU Vocabularies) "
             "y a las normas: refs fetch SOURCE --version V")
    failed = []
    for sid in names:
        source = found[sid]
        try:
            KINDS[source["kind"]].fetch(sid, source, args.version)
        except (urllib.error.URLError, RefsError) as e:
            print(f"{sid}: no se pudo descargar: {e}", file=sys.stderr)
            failed.append(sid)
        if source["kind"] == "document" and sid != names[-1]:
            time.sleep(INTERVAL)
    if failed:
        fail(f"sin descargar: {', '.join(failed)}")


def cmd_diff(args) -> None:
    found_sources = sources()
    selected(found_sources, [args.source])
    found = versions(args.source)
    old = args.old or pins().get(args.source)
    new = args.new or (found[-1] if found else None)
    for version in (old, new):
        if version not in found:
            fail(f"{args.source}: no existe la versión {version} (hay: {', '.join(found) or 'ninguna'})")
    if old == new:
        print(f"{args.source}: {old} es a la vez la fijada y la última; nada que comparar")
        return
    print(f"{args.source}: {old} → {new}")
    KINDS[found_sources[args.source]["kind"]].diff(args.source, old, new, sys.maxsize if args.all else DIFF_LIMIT)


def cmd_pin(args) -> None:
    reg = registry()
    selected(reg["sources"], [args.source])
    if args.version not in versions(args.source):
        fail(f"{args.source}: no existe la versión {args.version}")
    current = pins()
    previous = current.get(args.source)
    current[args.source] = args.version
    save_pins(current)
    print(f"{args.source}: fijada {args.version}" + (f" (antes {previous})" if previous else ""))
    if previous and previous != args.version:
        print(f"Cambios: references/bin/refs diff {args.source} {previous} {args.version}")
        print(f"Revisa en cada sistema que la usa lo construido sobre {previous}:")
        for system in reg["sources"][args.source]["uses"]:
            print(f"  {system}: {reg['systems'][system]['review']}")


def cmd_props(args) -> None:
    if args.type is None and "@" in args.what:
        rows = property_citation(args.what)
    else:
        selected(sources(), [args.what])
        rows = [r for r in properties(args.what, args.version) if args.type in (None, r["type"])]
        if not rows:
            fail(f"{args.what}: sin tablas de propiedades" + (f" de {args.type}" if args.type else ""))
        print(f"{args.what} {rows[0]['version']}: {len(rows)} filas")
    for r in rows:
        table = r["table"] + (f" · {r['group']}" if r["group"] else "")
        print(f"  {r['type']}.{' | '.join(r['names']) or '«' + r['label'] + '»'}  [{table}]  {r['heading']}  "
              f"{r['expects'] or '—'}")


def cmd_law(args) -> None:
    if args.what.startswith("ley:"):
        found = law_citation(args.what)
        print(f"{found['source']} {found['version']}\n{found['text']}")
        return
    selected(sources(), [args.what])
    old, new = args.old or pins().get(args.what), args.new or (versions(args.what) or [None])[-1]
    changed = law_changes(args.what, old, new)
    print(f"{args.what} {old} → {new}: {len(changed)} partes cambiadas (artículos y, por su encabezado, el resto)")
    for key in changed:
        print(f"  {key[:100]}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="refs", description="Fuentes externas congeladas de todos los sistemas (references/var/).")
    sub = parser.add_subparsers(dest="cmd")
    sub.add_parser("status", help="versiones por fuente, la fijada y quién la usa").set_defaults(func=cmd_status)
    p = sub.add_parser("check", help="¿ha cambiado la fuente en origen? (no guarda nada)")
    p.add_argument("sources", nargs="*", metavar="SOURCE")
    p.set_defaults(func=cmd_check)
    p = sub.add_parser("fetch", help="descargar una versión nueva")
    p.add_argument("sources", nargs="*", metavar="SOURCE")
    p.add_argument("--version", help="release de una fuente de Shopify, Schema.org o EU Vocabularies, o versión de una "
                                     "norma (por defecto, la última vigente)")
    p.set_defaults(func=cmd_fetch)
    p = sub.add_parser("diff", help="cambios entre dos versiones")
    p.add_argument("source")
    p.add_argument("old", nargs="?")
    p.add_argument("new", nargs="?")
    p.add_argument("--all", action="store_true", help="sin límite de líneas")
    p.set_defaults(func=cmd_diff)
    p = sub.add_parser("pin", help="fijar la versión con la que trabajan todos los sistemas")
    p.add_argument("source")
    p.add_argument("version")
    p.set_defaults(func=cmd_pin)
    p = sub.add_parser("props", help="tablas de propiedades de un documento, o resolver una cita fuente:Tipo.propiedad@versión")
    p.add_argument("what", metavar="SOURCE|CITATION")
    p.add_argument("type", nargs="?", help="solo las propiedades de este tipo")
    p.add_argument("--version", help="una versión distinta de la fijada")
    p.set_defaults(func=cmd_props)
    p = sub.add_parser("law", help="pasaje de una norma que nombra una cita ley:…, o artículos cambiados entre dos versiones")
    p.add_argument("what", metavar="CITATION|SOURCE")
    p.add_argument("old", nargs="?")
    p.add_argument("new", nargs="?")
    p.set_defaults(func=cmd_law)
    args = parser.parse_args()
    try:
        (getattr(args, "func", None) or cmd_status)(args)
    except RefsError as e:
        fail(str(e))


if __name__ == "__main__":
    main()
