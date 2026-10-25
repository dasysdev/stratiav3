"""Write the review document of the category blocks of the catalog.

Usage: catalog-review [OUT]   (default: catalog/REVIEW.md)

Lists every block of catalog/cat/ as a tree (parents first), with its references
and its requirements (question, importance, entity, origin, sources), the excluded
candidates and the empty categories of the skeleton. It is the document the user
reviews in training (D-041); approving a block changes its status to «validado».
"""
import json
import sys
from pathlib import Path

from . import ROOT

CAT = ROOT / "catalog/cat"
IMP = {"crítico": "**crítico**", "principal": "principal", "complementario": "complementario"}


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "catalog/REVIEW.md"
    blocks = {b["id"]: b for b in (json.loads(p.read_text(encoding="utf-8")) for p in sorted(CAT.glob("*.json")))}
    skeleton = json.loads((ROOT / "catalog/skeleton.json").read_text(encoding="utf-8"))
    drafted = {b.get("shopify") for b in blocks.values()}
    empty = [f"{b['shopify']} {b['name']}" for b in skeleton["blocks"] if b["shopify"] not in drafted]
    children = {}
    for b in blocks.values():
        children.setdefault(b.get("parent"), []).append(b["id"])
    roots = sorted(i for i, b in blocks.items() if not b.get("parent") or b["parent"] not in blocks)
    n_req = sum(len(b.get("requirements", [])) for b in blocks.values())
    crit = [(b["id"], r) for b in blocks.values() for r in b.get("requirements", []) if r.get("importance") == "crítico"]
    lines = [
        "# Revisión del catálogo de bloques de categoría",
        "",
        f"Borrador generado con `bin/blocks` y redactado automáticamente: {len(blocks)} bloques, {n_req} requisitos, "
        f"{len(crit)} críticos. Estado de todos: propuesta. Al aprobar un bloque pasa a «validado» (D-041).",
        "",
        "## Críticos",
        "",
    ]
    lines += [f"- `{r['id']}` — {r['question']}" for _, r in crit] or ["- (ninguno)"]
    lines += ["", "## Categorías sin requisitos propios (sin bloque; quedan como alias si un producto entra en ellas)", ""]
    lines += [f"- {e}" for e in empty] or ["- (ninguna)"]
    lines += ["", "## Bloques", ""]

    def walk(bid: str, depth: int) -> None:
        b = blocks[bid]
        lines.append(f"{'#' * min(3 + depth, 6)} `{bid}` · {b.get('name')} ({b.get('shopify')})")
        lines.append("")
        lines.append(f"Referencias: {', '.join(b.get('refs', []))}")
        lines.append("")
        reqs = b.get("requirements", [])
        if reqs:
            lines.append("| Requisito | Cuestión | Importancia | Entidad | Fuentes |")
            lines.append("|---|---|---|---|---|")
            for r in reqs:
                src = ", ".join(s.replace("amazon-ptd-prop:", "amz:").replace("shopify-attr:", "shp:") for s in r.get("sources", []))
                if len(src) > 120:
                    src = src[:117] + "…"
                lines.append(f"| `{r['id']}` | {r['question']} | {IMP.get(r.get('importance'), r.get('importance'))} | {r.get('entity')} | {src} |")
            lines.append("")
        exc = b.get("excluded", [])
        if exc:
            lines.append(f"<details><summary>Excluidos ({len(exc)})</summary>")
            lines.append("")
            for e in exc:
                lines.append(f"- `{e.get('source')}`: {e.get('reason')}")
            lines.append("")
            lines.append("</details>")
            lines.append("")
        for c in sorted(children.get(bid, [])):
            walk(c, depth + 1)

    for r in roots:
        walk(r, 0)
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{out}: {len(blocks)} bloques, {n_req} requisitos, {len(crit)} críticos, {len(empty)} categorías vacías")


if __name__ == "__main__":
    main()
