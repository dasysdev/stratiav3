"""The informative audit of Contenido and Marcado: effective availability and GSC by AC (D-153).

Phase 1 (an agent per page × scope) writes an availability record; phase 2 (agents per lot of RI
with availability 1) writes assessment records. Both are JSON validated and versioned (D-199):
schemas in info-audit/schemas/, rules in records.py. `validate` is the check between the phases
(QA-15) and before the dossier.

  info-audit/var/audits/<audit>/   the records of each audit (outside git)
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

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


def main() -> None:
    parser = argparse.ArgumentParser(prog="audit", description="Auditoría informativa de Contenido y Marcado.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("validate", help="validar registros de disponibilidad (fase 1) o de valoración (fase 2)")
    p.add_argument("records", nargs="+", metavar="RECORD.json")
    p.set_defaults(func=cmd_validate)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
