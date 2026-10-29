"""Extractores de referencia en Python: trafilatura, html2text, markdownify, BeautifulSoup get_text."""
import sys
from pathlib import Path

import html2text
import trafilatura
from bs4 import BeautifulSoup
from markdownify import markdownify

src, outdir = Path(sys.argv[1]), Path(sys.argv[2])
html = src.read_text(encoding="utf-8")
out = {
    "trafilatura": trafilatura.extract(html, include_tables=True, include_comments=False) or "",
    "trafilatura-recall": trafilatura.extract(html, favor_recall=True, include_tables=True) or "",
    "html2text": html2text.html2text(html),
    "markdownify": markdownify(html),
}
soup = BeautifulSoup(html, "html.parser")
for t in soup(["script", "style"]):
    t.decompose()
out["bs4-get_text"] = soup.get_text("\n")
outdir.mkdir(parents=True, exist_ok=True)
for k, v in out.items():
    (outdir / f"{k}.txt").write_text(v, encoding="utf-8")
