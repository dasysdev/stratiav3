"""A law, by its official consolidated text: the BOE (Spanish legislation, `boe`: its BOE-A-…
id) or EUR-Lex through Cellar, the repository of the EU Publications Office (`celex`: the
CELEX of the original act; eur-lex.europa.eu answers with a challenge). `cite` is the code
that names the law in a citation (ley:TRLGDCU-97.1.e@2026-02-28).

A version is the date the official source names the text by: in the BOE, the publication date
of the last amendment it includes («última actualización publicada el…»); in EUR-Lex, the
date of a consolidated version (02011R1007-20180215) or, for the original act, its publication
in the Official Journal. By default the latest one in force (not after today); --version
fetches another. Each version keeps the files as published (they count by their text) and its
text.md: a heading per article (## Artículo 16), and per division, provision, annex or final
formula, which closes the article before it, and one line per paragraph, with the mark of an
apartado or a letter ("1.", "e)") opening it. The reader cites by article and apartado.
"""
import json
import re
import urllib.parse
import xml.etree.ElementTree as ET
from html.parser import HTMLParser

from .. import net
from ..store import RefsError, Version, entry, latest_manifest, today, versions

BOE_API = "https://www.boe.es/datosabiertos/api/legislacion-consolidada/id/{}/"
CELLAR = "http://publications.europa.eu/resource/celex/{}"
SPARQL = "https://publications.europa.eu/webapi/rdf/sparql"
XHTML = {"accept": "application/xhtml+xml", "accept-language": "spa"}
XML = {"accept": "application/xml"}

ARTICLE = {"articulo", "oj-ti-art", "title-article-norm"}     # classes of an article (or BOE provision) heading
DIVISION = {"libro_num", "titulo_num", "capitulo_num", "seccion", "subseccion", "anexo_num", "anexo", "firma_rey",
            "oj-doc-ti", "oj-ti-section-1", "oj-final", "title-division-1", "title-annex-1"}   # BOE, OJ, consolidated
TITLE = {"oj-doc-ti", "title-doc-first"}                      # of the title of an EU act
SKIP = {"modref", "arrow"}                                     # marks of the amending acts (▼M1)
BLOCKS = {"p", "div", "tr", "table", "li", "h1", "h2", "h3", "h4", "h5", "h6", "body"}
VOID = {"area", "base", "br", "col", "hr", "img", "input", "link", "meta", "wbr"}
MARK_ONLY = re.compile(r"^(?:\(?\d+[.)º]?|[a-zñ]{1,4}\)|[–—•-])$")   # «1.» or «a)» waiting for its text
AMENDMENT = re.compile(r"[►▼]\s?[A-Z]\d*|◄")


class LawText(HTMLParser):
    """Lines of the text of a law in (X)HTML: one per paragraph or table row. A mark alone in
    its element (the «1.» of a span, the «a)» of a cell or of a list column) opens the line of
    the text that follows it. The title of an article, a division, a provision, an annex or the
    final formula becomes a heading (## Artículo 16), with all the text of its element."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.lines, self.inline, self.skipping, self.classes = [], [], 0, []
        self.heading = None     # depth of the open element whose text is a heading

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            if tag == "br" and not self.skipping:
                self.flush()
            return
        classes = set((dict(attrs).get("class") or "").split())
        if self.skipping or tag in ("head", "script", "style") or classes & SKIP:
            self.skipping += 1
            return
        if self.heading is None:
            if tag in BLOCKS:
                self.flush()
            if classes & (ARTICLE | DIVISION):
                self.heading = len(self.classes)
        elif tag in BLOCKS:
            self.inline.append(" ")         # the paragraphs of a heading, one after another
        self.classes.append(classes)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.skipping:
            self.skipping -= 1
            return
        if self.classes:
            self.classes.pop()
        if self.heading == len(self.classes):
            self.heading = None
            self.flush("## ")
        elif tag in BLOCKS and self.heading is None:
            self.flush()

    def handle_data(self, data):
        if not self.skipping:
            self.inline.append(data)

    def flush(self, head: str = "") -> None:
        text = " ".join(AMENDMENT.sub(" ", "".join(self.inline)).split())
        if not text or MARK_ONLY.match(text) and not head:
            self.inline = [text + " "] if text else []
            return
        self.inline = []
        self.lines.append(head + text)


def text_lines(markup: str) -> list:
    parser = LawText()
    parser.feed(markup)
    parser.close()
    parser.flush()
    return parser.lines


def text_md(title: str, lines: list) -> bytes:
    return ("\n".join([f"# {title}", ""] + lines) + "\n").encode("utf-8")


def iso(compact: str) -> str:
    """20260228 → 2026-02-28."""
    return f"{compact[:4]}-{compact[4:6]}-{compact[6:8]}"


def chosen(sid: str, found: list, tag: str) -> str:
    """The version to fetch: `tag`, which must be one of `found`, or the latest not after today."""
    if tag:
        if tag not in found:
            raise RefsError(f"{sid}: no hay versión {tag} (hay: {', '.join(found)})")
        return tag
    current = [v for v in found if v <= today()]
    return (current or found)[-1]


# --- BOE ----------------------------------------------------------------------

def boe_versions(root) -> list:
    return sorted({iso(v.get("fecha_publicacion")) for v in root.iter("version")})


def boe_text(root, title: str, version: str) -> bytes:
    """The consolidated text at `version`: each block in the version published on or before it."""
    lines = []
    for block in root.iter("bloque"):
        found = [v for v in block.findall("version") if iso(v.get("fecha_publicacion")) <= version]
        if found:
            lines += text_lines(ET.tostring(found[-1], encoding="unicode"))
    return text_md(title, lines)


def boe_fetch(sid: str, source: dict, tag: str) -> None:
    base = BOE_API.format(source["boe"])
    meta, _, _ = net.download(base + "metadatos", XML)
    data, _, final = net.download(base + "texto", XML)
    root = ET.fromstring(data)
    version = chosen(sid, boe_versions(root), tag)
    title = ET.fromstring(meta).findtext(".//titulo") or source["title"]
    snap = Version(sid, version, {"url": base + "texto", "final_url": final, "boe": source["boe"]})
    snap.put("metadatos.xml", meta, entry("metadatos.xml", meta, base + "metadatos", counted_by="text.md"))
    snap.put("texto.xml", data, entry("texto.xml", data, final, counted_by="text.md"))
    text = boe_text(root, title, version)
    snap.put("text.md", text, entry("text.md", text, "texto.xml"))
    snap.commit()


def boe_latest(source: dict) -> str:
    data, _, _ = net.download(BOE_API.format(source["boe"]) + "texto", XML)
    return chosen("", boe_versions(ET.fromstring(data)), None)


# --- EUR-Lex (Cellar) ---------------------------------------------------------

def consolidated(celex: str) -> dict:
    """Date → CELEX of each consolidated version of an act (02011R1007-20180215)."""
    query = ("PREFIX cdm: <http://publications.europa.eu/ontology/cdm#> SELECT DISTINCT ?celex WHERE { "
             "?w cdm:resource_legal_id_celex ?celex . "
             f'FILTER(STRSTARTS(STR(?celex), "0{celex[1:]}-")) }}')
    url = SPARQL + "?" + urllib.parse.urlencode({"query": query})
    data, _, _ = net.download(url, {"accept": "application/sparql-results+json"})
    found = [b["celex"]["value"] for b in json.loads(data)["results"]["bindings"]]
    return {iso(c.rsplit("-", 1)[1]): c for c in found}


def oj_date(markup: str) -> str:
    """Publication date of an original act in the Official Journal (18.10.2011 → 2011-10-18)."""
    m = re.search(r'class="oj-hd-date"[^>]*>\s*(\d{1,2})\.(\d{1,2})\.(\d{4})', markup)
    if not m:
        raise RefsError("no se encuentra la fecha del Diario Oficial en el texto original")
    return f"{m[3]}-{int(m[2]):02d}-{int(m[1]):02d}"


def eu_title(markup: str, lines: list) -> str:
    """Title of an act: its number, date and subject (the first three elements of a title
    class), else the first line of its text."""
    parser = TitleText()
    parser.feed(markup)
    return " ".join(parser.parts[:3]) or lines[0]


class TitleText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts, self.depth, self.inline = [], 0, []

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            return
        if self.depth:
            self.depth += 1
        elif set((dict(attrs).get("class") or "").split()) & TITLE:
            self.depth, self.inline = 1, []

    def handle_endtag(self, tag):
        if tag in VOID or not self.depth:
            return
        self.depth -= 1
        if not self.depth and (text := " ".join("".join(self.inline).split())):
            self.parts.append(text)

    def handle_data(self, data):
        if self.depth:
            self.inline.append(data)


def eu_fetch(sid: str, source: dict, tag: str) -> None:
    """A consolidated version (by default the latest in force) or, by its date in the Official
    Journal, the original act; an act never amended has only the original."""
    celex = source["celex"]
    found = consolidated(celex)
    if found and (tag is None or tag in found):
        version = chosen(sid, sorted(found), tag)
        target = found[version]
    else:
        target = celex
    data, _, final = net.download(CELLAR.format(target), XHTML)
    markup = data.decode("utf-8")
    if target == celex:
        version = oj_date(markup)
        if tag not in (None, version):
            raise RefsError(f"{sid}: no hay versión {tag} (consolidadas: {', '.join(sorted(found)) or 'ninguna'}; "
                            f"original: {version})")
    lines = text_lines(markup)
    snap = Version(sid, version, {"url": CELLAR.format(target), "final_url": final, "celex": target})
    snap.put("page.html", data, entry("page.html", data, final, counted_by="text.md"))
    text = text_md(eu_title(markup, lines), lines)
    snap.put("text.md", text, entry("text.md", text, "page.html"))
    snap.commit()


def eu_latest(source: dict) -> str:
    found = consolidated(source["celex"])
    if found:
        return chosen("", sorted(found), None)
    data, _, _ = net.download(CELLAR.format(source["celex"]), XHTML)
    return oj_date(data.decode("utf-8"))


# --- Kind ---------------------------------------------------------------------

def check(sid: str, source: dict) -> str:
    latest = latest_manifest(sid)
    upstream = boe_latest(source) if "boe" in source else eu_latest(source)
    if not latest:
        return f"sin descargar (en origen: {upstream})"
    if upstream in versions(sid):
        return f"al día ({upstream})"
    return f"hay una versión {upstream} (la última descargada es {latest['version']}): refs fetch {sid}"


def fetch(sid: str, source: dict, tag: str) -> None:
    (boe_fetch if "boe" in source else eu_fetch)(sid, source, tag)
