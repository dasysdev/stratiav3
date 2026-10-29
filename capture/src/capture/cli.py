"""The store of frozen pages from the command line.

  pages fetch ID URL [--profile NAME]
                        freeze a product page as var/pages/ID.html with the capture engine,
                        under a new ID (on the host it runs in the container); the capture
                        profile is `reader` unless another is named (capture.profiles)
  pages crawl AUDIT URL [--max-urls N] [--sitemap-files N] [--sitemap-mb N]
  pages crawl AUDIT --resume [--max-urls N]
                        crawl the site of URL (its home page) and its sitemaps and capture each
                        page under audit-es in var/audits/AUDIT/ (D-170, capture.spider); --resume
                        goes on with an interrupted crawl; a TDM reservation ends it with exit
                        code 3 (D-171)
  pages audit AUDIT [URL ...] [--from FILE]
                        choose the pages of the audit (D-167) on the crawl AUDIT, in audit.json:
                        the product pages given (all those of the universe if none), the home
                        page, the policies and the categories (capture.audit); it asks for
                        nothing and runs on the host; a crawl stopped by a TDM reservation ends
                        it with exit code 3 (D-171)
  pages resources AUDIT [URL ...] [--from FILE]
                        ask with GET for each resource URL given (the images of the markup) and
                        record in var/audits/AUDIT/resources.json the status, the redirects and
                        the headers of its responses, without their bodies (capture.resources);
                        --from - reads the list from stdin; a URL already recorded is not asked
                        again; a TDM reservation ends it with exit code 3 (D-171)
"""
import argparse
import subprocess
import sys
from collections import Counter

from pathlib import Path

from . import ROOT, audit, pages, profiles, resources, spider
from .audit import AuditError
from .pages import PageError

RESERVED = 3  # exit code of an audit stopped by a TDM reservation (D-171)


def cmd_fetch(args) -> None:
    pages.check_new(args.id)
    if not pages.engine_available():
        # On the host: the capture engine (Chrome, websockets) runs in the container
        code = subprocess.call([str(ROOT.parent / "bin/run"), "dev", "exec", "python", "-m", "capture.cli",
                                "fetch", args.id, args.url, "--profile", args.profile])
        if code:
            print("pages: fetch se ejecuta en el contenedor; si no está levantado: bin/run dev up", file=sys.stderr)
        sys.exit(code)
    info = pages.fetch(args.id, args.url, profile=args.profile)
    print(f"{args.id}: {info['size']} bytes ({info['content']}, perfil {info['profile']}, HTTP {info['http_status']});"
          f" instantánea en {info['snapshot']}")


def cmd_audit(args) -> None:
    urls = list(args.urls) + (audit.load_list(Path(args.from_file)) if args.from_file else [])
    try:
        record = audit.run(args.audit, urls)
    except audit.Reserved as stop:
        reservation = stop.reservation
        print(f"pages: {args.audit}: el sitio reserva la minería de textos y datos (art. 67.3 TRLPI)."
              f" Dónde: {reservation['where']} ({reservation['source']}, {reservation['url']})."
              f" El rastreo está parado y no se audita. Evidencia: campo reservation de crawl.json.",
              file=sys.stderr)
        sys.exit(RESERVED)
    kinds = Counter(p["type"] for p in record["pages"])
    outside = [p["url"] for p in record["products"] if not p.get("page")]
    missing = [k for k, v in record["policies"].items() if v["status"] != "located"]
    print(f"{args.audit}: {len(record['pages'])} páginas ({', '.join(f'{n} {k}' for k, n in kinds.items())})"
          + (f"; fichas fuera del universo: {len(outside)}" if outside else "")
          + (f"; políticas no localizadas o no capturadas: {', '.join(missing)}" if missing else "")
          + f"; manifiesto en var/audits/{args.audit}/audit.json")


def cmd_crawl(args) -> None:
    if args.resume == bool(args.url):
        raise AuditError("da la URL de la portada para un rastreo nuevo, o --resume para seguir uno")
    if not args.resume:
        audit.check_new(args.audit)
    if not pages.engine_available():
        # On the host: the crawl runs in the container
        extra = ["--resume"] if args.resume else [args.url]
        extra += ["--max-urls", str(args.max_urls)] if args.max_urls else []
        extra += ["--sitemap-files", str(args.sitemap_files), "--sitemap-mb", str(args.sitemap_mb)]
        code = subprocess.call([str(ROOT.parent / "bin/run"), "dev", "exec", "python", "-m", "capture.cli",
                                "crawl", args.audit, *extra])
        if code and code != RESERVED:
            print("pages: crawl se ejecuta en el contenedor; si no está levantado: bin/run dev up", file=sys.stderr)
        sys.exit(code)
    record = spider.run(args.audit, args.url, resume=args.resume, limit=args.max_urls,
                        sitemap_files=args.sitemap_files, sitemap_mb=args.sitemap_mb)
    crawl = record["crawl"]
    coverage = crawl["coverage"]
    outcomes = ", ".join(f"{n} {outcome}" for outcome, n in sorted(crawl["outcomes"].items()))
    print(f"{args.audit}: {crawl['processed']} URL procesadas ({outcomes or 'ninguna'}); "
          f"{crawl['discovered']} descubiertas; "
          + ("cobertura completa" if coverage["complete"] else
             f"cobertura incompleta ({', '.join(r['reason'] for r in coverage['reasons']) or 'pendientes'}; "
             f"{coverage['pending']} pendientes)")
          + f"; manifiesto en var/audits/{args.audit}/crawl.json")
    reservation = record.get("reservation")
    if reservation:
        print(f"pages: {args.audit}: el sitio reserva la minería de textos y datos (art. 67.3 TRLPI)."
              f" Dónde: {reservation['where']} ({reservation['source']}, {reservation['url']})."
              f" El rastreo está parado e incompleto. Evidencia: campo reservation de audit.json.",
              file=sys.stderr)
        sys.exit(RESERVED)


def cmd_resources(args) -> None:
    urls = list(args.urls)
    if args.from_file == "-":
        urls += [l.strip() for l in sys.stdin.read().splitlines() if l.strip() and not l.lstrip().startswith("#")]
    elif args.from_file:
        urls += audit.load_list(Path(args.from_file))
    if not urls:
        raise AuditError("sin URL: da las URL de recurso o --from FICHERO")
    if not pages.engine_available():
        # On the host: the list is read here and goes to the container by stdin
        code = subprocess.run([str(ROOT.parent / "bin/run"), "dev", "exec", "python", "-m", "capture.cli",
                               "resources", args.audit, "--from", "-"], input="\n".join(urls), text=True).returncode
        if code and code != RESERVED:
            print("pages: resources se ejecuta en el contenedor; si no está levantado: bin/run dev up", file=sys.stderr)
        sys.exit(code)
    try:
        record = resources.run(args.audit, urls)
    except audit.Reserved as stop:
        record = {"reservation": stop.reservation}
    else:
        outcomes = ", ".join(f"{n} {k}" for k, n in record["outcomes"].items())
        print(f"{args.audit}: {len(record['resources'])} URL registradas ({outcomes or 'ninguna'})"
              + (f"; {record['stopped']}" if record["stopped"] else "")
              + f"; manifiesto en var/audits/{args.audit}/resources.json")
    reservation = record.get("reservation")
    if reservation:
        print(f"pages: {args.audit}: el sitio reserva la minería de textos y datos (art. 67.3 TRLPI)."
              f" Dónde: {reservation['where']} ({reservation['source']}, {reservation['url']})."
              f" La auditoría está parada y no se pide nada más.", file=sys.stderr)
        sys.exit(RESERVED)


def main() -> None:
    parser = argparse.ArgumentParser(prog="pages", description="Almacén de fichas congeladas.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("fetch"); p.add_argument("id"); p.add_argument("url")
    p.add_argument("--profile", choices=list(profiles.PROFILES), default=profiles.DEFAULT,
                   help="perfil de captura (por defecto, %(default)s)")
    p.set_defaults(func=cmd_fetch)
    p = sub.add_parser("crawl", help="rastreo y captura de un sitio y sus sitemaps (D-170), con audit-es")
    p.add_argument("audit"); p.add_argument("url", nargs="?", help="portada del sitio")
    p.add_argument("--resume", action="store_true", help="sigue un rastreo interrumpido")
    p.add_argument("--max-urls", type=int, help=f"tope de URL procesadas (por defecto, {spider.LIMIT})")
    p.add_argument("--sitemap-files", type=int, default=audit.SITEMAP_FILES,
                   help="tope de ficheros de sitemap (por defecto, %(default)s)")
    p.add_argument("--sitemap-mb", type=int, default=audit.SITEMAP_MB,
                   help="tope de MB de sitemaps (por defecto, %(default)s)")
    p.set_defaults(func=cmd_crawl)
    p = sub.add_parser("audit", help="páginas de una auditoría (D-167), elegidas sobre su rastreo")
    p.add_argument("audit"); p.add_argument("urls", nargs="*", help="fichas del encargo (sin ellas, todas las del universo)")
    p.add_argument("--from", dest="from_file", help="fichero con una URL de ficha por línea")
    p.set_defaults(func=cmd_audit)
    p = sub.add_parser("resources", help="acceso a los recursos de una auditoría (GET, sin el cuerpo), con audit-es")
    p.add_argument("audit"); p.add_argument("urls", nargs="*", help="URL de recurso")
    p.add_argument("--from", dest="from_file", help="fichero con una URL por línea (- para la entrada estándar)")
    p.set_defaults(func=cmd_resources)
    args = parser.parse_args()
    try:
        args.func(args)
    except (PageError, AuditError) as e:
        sys.exit(f"pages: {e}")


if __name__ == "__main__":
    main()
