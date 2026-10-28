"""The store of frozen pages from the command line.

  pages fetch ID URL    freeze a product page as var/pages/ID.html with the capture engine,
                        under a new ID (on the host it runs in the container)
"""
import argparse
import subprocess
import sys

from . import ROOT, pages
from .pages import PageError


def cmd_fetch(args) -> None:
    pages.check_new(args.id)
    if not pages.engine_available():
        # On the host: the capture engine (Chrome, websockets) runs in the container
        code = subprocess.call([str(ROOT.parent / "bin/run"), "dev", "exec", "python", "-m", "capture.cli",
                                "fetch", args.id, args.url])
        if code:
            print("pages: fetch se ejecuta en el contenedor; si no está levantado: bin/run dev up", file=sys.stderr)
        sys.exit(code)
    info = pages.fetch(args.id, args.url)
    print(f"{args.id}: {info['size']} bytes (DOM renderizado, HTTP {info['http_status']}); instantánea en {info['snapshot']}")


def main() -> None:
    parser = argparse.ArgumentParser(prog="pages", description="Almacén de fichas congeladas.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("fetch"); p.add_argument("id"); p.add_argument("url"); p.set_defaults(func=cmd_fetch)
    args = parser.parse_args()
    try:
        args.func(args)
    except PageError as e:
        sys.exit(f"pages: {e}")


if __name__ == "__main__":
    main()
