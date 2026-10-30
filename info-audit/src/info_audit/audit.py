"""The informative audit of Contenido and Marcado: effective availability and GSC by AC (D-153).

Phase 1 (an agent per page × scope) writes an availability record; phase 2 (agents per lot of RI
with availability 1) writes assessment records. Both are JSON validated and versioned (D-199):
schemas in info-audit/schemas/, rules in records.py. `validate` is the check between the phases
(QA-15) and before the dossier. `alfa` writes the representation that Contenido reads: the output
of the filter Alfa (alfa.py) over a frozen audit-es page of capture.

  info-audit/var/audits/<audit>/                          the records of each audit (outside git)
  info-audit/var/representations/<page-ID>.alfa-1.json   the output of alfa/1 of each page (outside git)
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from . import ROOT
from .records import check


def cmd_validate(args) -> None:
    failed = 0
    for name in args.records:
        try:
            record = json.loads(Path(name).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            errors = [f"no se puede leer: {e}"]
        else:
            errors = check(record)
        print(f"{name}: {'válido' if not errors else f'{len(errors)} errores'}")
        for line in errors:
            print(f"  ERROR {line}")
        failed += bool(errors)
    if failed:
        sys.exit(1)


def cmd_alfa(args) -> None:
    if sys.version_info < (3, 13):
        # The tokenizer of html.parser changes between versions of Python: alfa/1 runs in the
        # container (Python 3.13, as pyproject.toml requires), so that every output is the same
        code = subprocess.call([str(ROOT.parent / "bin/run"), "dev", "exec", "python", "-m", "info_audit.audit",
                                "alfa", *args.pages])
        if code not in (0, 1):   # 1: a page failed, and the output says why
            print("audit: alfa se ejecuta en el contenedor; si no está levantado: bin/run dev up", file=sys.stderr)
        sys.exit(code)
    from . import alfa

    failed = 0
    for page in args.pages:
        try:
            rep = alfa.from_page(page)
            path, written = alfa.write(rep)
        except alfa.AlfaError as e:
            print(f"{page}: ERROR {e}")
            failed += 1
            continue
        hidden = sum(1 for f in rep["fragments"] if "oculto" in f)
        state = "escrita" if written else "sin cambios"
        print(f"{page}: {len(rep['text'])} caracteres, {len(rep['fragments'])} fragmentos ({hidden} con oculto);"
              f" {state} en {alfa.shown(path)}")
    if failed:
        sys.exit(1)


def main() -> None:
    parser = argparse.ArgumentParser(prog="audit", description="Auditoría informativa de Contenido y Marcado.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("validate", help="validar registros de disponibilidad (fase 1) o de valoración (fase 2)")
    p.add_argument("records", nargs="+", metavar="RECORD.json")
    p.set_defaults(func=cmd_validate)
    p = sub.add_parser("alfa", help="aplicar el filtro Alfa (alfa/1) a fichas audit-es congeladas por capture",
                       description="Aplica alfa/1 a la respuesta HTTP de cada ficha (page-ID de capture/var/pages/) "
                                   "y escribe su salida en info-audit/var/representations/PAGE-ID.alfa-1.json.")
    p.add_argument("pages", nargs="+", metavar="PAGE-ID")
    p.set_defaults(func=cmd_alfa)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
