"""The store of frozen pages from the command line.

  pages fetch ID URL [--profile NAME]
                        freeze a product page as var/pages/ID.html with the capture engine,
                        under a new ID (on the host it runs in the container); the capture
                        profile is `reader` unless another is named (capture.profiles)
  pages audit AUDIT [URL ...] [--from FILE] [--sitemap-files N] [--sitemap-mb N]
                        capture the pages of an audit (D-167) in var/audits/AUDIT/ under audit-es:
                        the product pages given, the home page, the policies, the immediate
                        category of each product page, robots.txt and the sitemaps (capture.audit)
"""
import argparse
import subprocess
import sys

from pathlib import Path

from . import ROOT, audit, pages, profiles
from .audit import AuditError
from .pages import PageError


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
    audit.check_new(args.audit)
    if not urls:
        raise AuditError("sin fichas del encargo: da sus URL o --from FICHERO")
    if not pages.engine_available():
        # On the host the list is read here and the URLs go to the container
        code = subprocess.call([str(ROOT.parent / "bin/run"), "dev", "exec", "python", "-m", "capture.cli",
                                "audit", args.audit, *urls, "--sitemap-files", str(args.sitemap_files),
                                "--sitemap-mb", str(args.sitemap_mb)])
        if code:
            print("pages: audit se ejecuta en el contenedor; si no está levantado: bin/run dev up", file=sys.stderr)
        sys.exit(code)
    record = audit.run(args.audit, urls, sitemap_files=args.sitemap_files, sitemap_mb=args.sitemap_mb)
    captured = sum(p["outcome"] == "captured" for p in record["pages"])
    missing = [k for k, v in (record.get("policies") or {}).items() if v["status"] != "located"]
    print(f"{args.audit}: {captured}/{len(record['pages'])} páginas capturadas"
          + (f"; políticas no localizadas: {', '.join(missing)}" if missing else "")
          + (f"; {record['stopped']}" if record["stopped"] else "")
          + f"; manifiesto en var/audits/{args.audit}/audit.json")


def main() -> None:
    parser = argparse.ArgumentParser(prog="pages", description="Almacén de fichas congeladas.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("fetch"); p.add_argument("id"); p.add_argument("url")
    p.add_argument("--profile", choices=list(profiles.PROFILES), default=profiles.DEFAULT,
                   help="perfil de captura (por defecto, %(default)s)")
    p.set_defaults(func=cmd_fetch)
    p = sub.add_parser("audit", help="páginas de una auditoría (D-167), con audit-es")
    p.add_argument("audit"); p.add_argument("urls", nargs="*", help="fichas del encargo")
    p.add_argument("--from", dest="from_file", help="fichero con una URL de ficha por línea")
    p.add_argument("--sitemap-files", type=int, default=audit.SITEMAP_FILES,
                   help="tope de ficheros de sitemap (por defecto, %(default)s)")
    p.add_argument("--sitemap-mb", type=int, default=audit.SITEMAP_MB,
                   help="tope de MB de sitemaps (por defecto, %(default)s)")
    p.set_defaults(func=cmd_audit)
    args = parser.parse_args()
    try:
        args.func(args)
    except (PageError, AuditError) as e:
        sys.exit(f"pages: {e}")


if __name__ == "__main__":
    main()
