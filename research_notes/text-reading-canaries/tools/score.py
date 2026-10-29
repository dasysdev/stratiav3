"""Matriz canario × lector: qué códigos aparecen en cada texto de results/*/*/.

Uso: python3 score.py RESULTS_DIR → tabla Markdown por construcción y lector.
"""
import json
import sys
from pathlib import Path

here = Path(__file__).resolve().parent.parent
key = json.loads((here / "canaries.json").read_text(encoding="utf-8"))
root = Path(sys.argv[1])
texts = {p.stem: p.read_text(encoding="utf-8", errors="replace").replace("\\", "") for p in sorted(root.glob("*.txt"))}
readers = list(texts)
print("| construcción | código | " + " | ".join(readers) + " |")
print("|---|---|" + "---|" * len(readers))
for c in key["constructs"]:
    marks = ["✓" if c["token"] in texts[r] else "·" for r in readers]
    print(f"| {c['id']} | {c['token']} | " + " | ".join(marks) + " |")
