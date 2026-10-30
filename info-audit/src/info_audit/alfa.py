"""The reading filter Alfa, version 1 (alfa/1): the representation that the scope Contenido reads
(D-221; specification in docs/20-methods/audit-gsc/filter-alfa.md).

From the original bytes of the HTTP response of an audit-es page, decoded as the Encoding
Standard says (encoding.py) and parsed with scripts disabled (htmltree.py), Alfa gives the title
of the document and the text content of its body, in document order, without a cut:

- In: every text node under <body>, shown or not (noscript, forms, svg included), and the alt
  of each <img> where the image is.
- Out: the rest of <head>, <script> and <style>, <template>, comments, attributes (except the
  alt of <img>), the content of <iframe>, <object> and <embed>, and what CSS generates.

Each text node (and each alt) is a fragment: its span [start, end) in the text, the path of its
element and the annotations oculto, region, control, alt and enlace. Blocks start a new line;
headings carry "#" to "######", list items "- ", table rows their cells joined by " | "; <pre>
keeps its spaces and elsewhere spaces collapse. An image is replaced by its alt with a
collapsible space on each side.

  info-audit/var/representations/<page-ID>.alfa-1.json   the output of each page (outside git)
"""
from __future__ import annotations

import gzip
import hashlib
import json
import platform
import re
from pathlib import Path
from urllib.parse import urljoin

from . import ROOT
from .encoding import decode
from .htmltree import HTML, Node, parse

FILTER, VERSION = "alfa", 1
REPRESENTATIONS = ROOT / "var/representations"
REPO = ROOT.parent
WS = " \t\n\f\r"
COLLAPSE = re.compile(r"[ \t\n\f\r]+")

EXCLUDED = {"template", "iframe", "object", "embed"}      # their content is not text of the document
EXCLUDED_ANY_NS = {"script", "style"}                     # also inside <svg> and <math>
BLOCKS = {"p", "div", "li", "h1", "h2", "h3", "h4", "h5", "h6", "tr", "dt", "dd", "table", "section", "article",
          "header", "footer", "nav", "aside", "main", "figure", "figcaption", "form", "fieldset", "details",
          "summary", "dialog", "blockquote", "pre", "option"}
REGIONS = {"header", "nav", "footer", "aside"}
REGION_ROLES = {"banner", "navigation", "contentinfo", "complementary"}
CONTROLS = {"form", "select", "button", "textarea", "label"}


class AlfaError(Exception):
    pass


# --- Annotations -----------------------------------------------------------------------------------

def _style(value: str) -> dict[str, str]:
    """The declarations of a style attribute: property → value (the last one wins, unless an
    earlier one is !important)."""
    out: dict[str, tuple[str, bool]] = {}
    for decl in re.sub(r"/\*.*?\*/", "", value, flags=re.S).split(";"):
        prop, sep, val = decl.partition(":")
        if not sep:
            continue
        prop, val = prop.strip().lower(), val.strip().lower()
        important = val.endswith("!important")
        if important:
            val = val[:-len("!important")].strip()
        if prop in out and out[prop][1] and not important:
            continue
        out[prop] = (val, important)
    return {k: v for k, (v, _) in out.items()}


def _hidden_by(node: Node) -> list[str]:
    """What hides an element itself: hidden, aria-hidden="true", inert, display:none,
    visibility:hidden or a <dialog> without open (a closed <details> hides its children)."""
    a, out = node.attrs, []
    if "hidden" in a:
        out.append("hidden")
    if a.get("aria-hidden", "").strip(WS).lower() == "true":
        out.append("aria-hidden")
    if "inert" in a:
        out.append("inert")
    if "style" in a:
        style = _style(a["style"])
        if style.get("display") == "none":
            out.append("display:none")
        if style.get("visibility") == "hidden":
            out.append("visibility:hidden")
    if node.is_("dialog") and "open" not in a:
        out.append("dialog")
    return out


def _region(node: Node) -> list[str]:
    out = [node.tag] if node.ns == HTML and node.tag in REGIONS else []
    role = next((r for r in node.attrs.get("role", "").lower().split() if r in REGION_ROLES), None)
    return out + ([f"role={role}"] if role else [])


def _absolute(base: str, href: str) -> str:
    """The absolute URL of a link: the URL parser drops leading and trailing C0 controls and
    spaces, and tabs and newlines anywhere."""
    href = re.sub(r"[\t\n\r]", "", href.strip("".join(map(chr, range(0x21)))))
    try:
        return urljoin(base, href)
    except ValueError:
        return href


class Context:
    """The annotations that an element passes down to its descendants."""
    __slots__ = ("oculto", "region", "control", "enlace", "pre")

    def __init__(self, oculto=(), region=(), control=(), enlace=None, pre=False) -> None:
        self.oculto, self.region, self.control, self.enlace, self.pre = oculto, region, control, enlace, pre

    def enter(self, node: Node, base: str, extra_hidden: tuple = ()) -> "Context":
        def add(old, new):
            return old + tuple(x for x in new if x not in old)
        href = node.attrs.get("href", node.attrs.get("xlink:href")) if node.tag == "a" else None
        return Context(
            add(self.oculto, tuple(_hidden_by(node)) + extra_hidden),
            add(self.region, _region(node)),
            add(self.control, (node.tag,) if node.ns == HTML and node.tag in CONTROLS else ()),
            _absolute(base, href) if href is not None else self.enlace,
            self.pre or node.is_("pre"))

    def hide(self, reason: str) -> "Context":
        oculto = self.oculto if reason in self.oculto else self.oculto + (reason,)
        return Context(oculto, self.region, self.control, self.enlace, self.pre)

    def annotations(self) -> dict:
        out: dict = {}
        if self.oculto:
            out["oculto"] = list(self.oculto)
        if self.region:
            out["region"] = list(self.region)
        if self.control:
            out["control"] = list(self.control)
        if self.enlace is not None:
            out["enlace"] = self.enlace
        return out


# --- The text and its fragments --------------------------------------------------------------------

class Writer:
    """The text in document order: lines, markers, cell separators and collapsed spaces, and the
    span of every fragment in it."""

    def __init__(self) -> None:
        self.parts: list[str] = []
        self.pos = 0
        self.line_start = True
        self.newline = False       # a block boundary is pending
        self.space = False         # a collapsible space is pending
        self.prefix: list = []     # (element, marker) for the next line
        self.rows: list[list[int]] = []   # per open row: [cells seen, separators pending]
        self.fragments: list[dict] = []

    def _write(self, s: str) -> None:
        self.parts.append(s)
        self.pos += len(s)

    def block(self, node: Node, marker: str | None = None) -> None:
        self.newline = self.newline or not self.line_start
        self.space = False
        if marker:
            self.prefix.append((node, marker))

    def end_block(self, node: Node) -> None:
        self.newline = self.newline or not self.line_start
        self.space = False
        self.prefix = [p for p in self.prefix if p[0] is not node]

    def row(self, node: Node) -> None:
        self.block(node)
        self.rows.append([0, 0])

    def end_row(self, node: Node) -> None:
        if self.rows:
            self.rows.pop()
        self.end_block(node)

    def cell(self) -> None:
        if self.rows:
            row = self.rows[-1]
            if row[0]:
                row[1] += 1
            row[0] += 1
        self.space = False

    def soft_space(self) -> None:
        if not self.line_start:
            self.space = True

    def emit(self, text: str, path: str, annotations: dict, record: bool = True) -> None:
        row = self.rows[-1] if self.rows else None
        if row and row[1]:
            sep = " |" * row[1] + " "
            self._write(sep[1:] if self.line_start else sep)
            row[1] = 0
            self.line_start, self.space = False, False
        elif self.newline and not self.line_start:
            self._write("\n")
            self.line_start, self.space = True, False
        self.newline = False
        if self.prefix:
            self._write("".join(m for _, m in self.prefix))
            self.prefix = []
        elif self.space and not self.line_start:
            self._write(" ")
        self.space = False
        start = self.pos
        self._write(text)
        self.line_start = text.endswith("\n")
        if record:
            self.fragments.append({"start": start, "end": self.pos, "text": text, "ruta": path} | annotations)

    def text(self, data: str, ctx: Context, path: str) -> None:
        if ctx.pre:
            if data:
                self.emit(data, path, ctx.annotations(), record=data.strip(WS) != "")
            return
        if not data:
            return
        core = COLLAPSE.sub(" ", data).strip(" ")
        if data[0] in WS:
            self.soft_space()
        if core:
            self.emit(core, path, ctx.annotations())
            if data[-1] in WS:
                self.soft_space()

    def alt(self, alt: str, ctx: Context, path: str) -> None:
        core = COLLAPSE.sub(" ", alt).strip(" ")
        if core:
            self.soft_space()
            self.emit(core, path, ctx.annotations() | {"alt": True})
            self.soft_space()

    def result(self) -> str:
        return "".join(self.parts)


def _paths(node: Node, path: str) -> list[tuple[object, str]]:
    """The children of an element with their paths: tag, and [n] among siblings of the same tag."""
    counts: dict[str, int] = {}
    for c in node.children:
        if isinstance(c, Node):
            counts[c.tag] = counts.get(c.tag, 0) + 1
    seen: dict[str, int] = {}
    out = []
    for c in node.children:
        if isinstance(c, Node):
            seen[c.tag] = seen.get(c.tag, 0) + 1
            out.append((c, f"{path}/{c.tag}" + (f"[{seen[c.tag]}]" if counts[c.tag] > 1 else "")))
        else:
            out.append((c, path))
    return out


def _excluded(node: Node) -> bool:
    return node.tag in EXCLUDED_ANY_NS or (node.ns == HTML and node.tag in EXCLUDED)


def _body_path(body: Node) -> str:
    parts = []
    node = body
    while node.parent is not None:
        same = [c for c in node.parent.children if isinstance(c, Node) and c.tag == node.tag]
        parts.append(node.tag + (f"[{same.index(node) + 1}]" if len(same) > 1 else ""))
        node = node.parent
    return "/" + "/".join(reversed(parts))


END = object()   # marks the end of a block in the walk


def _body(body: Node, base: str) -> tuple[str, list[dict]]:
    out = Writer()
    stack: list = [(body, Context().enter(body, base), _body_path(body))]
    while stack:
        item = stack.pop()
        if item[0] is END:
            _, node = item
            if node.is_("tr"):
                out.end_row(node)
            else:
                out.end_block(node)
            continue
        node, ctx, path = item
        if isinstance(node, str):
            out.text(node, ctx, path)
            continue
        if node.is_("br"):
            out.block(node)
            continue
        if node.is_("img"):
            out.alt(node.attrs.get("alt", ""), ctx, path)
            continue
        if node.is_("tr"):
            out.row(node)
            stack.append((END, node))
        elif node.is_("td", "th"):
            out.cell()
        elif node.ns == HTML and node.tag in BLOCKS:
            level = int(node.tag[1]) if node.tag in ("h1", "h2", "h3", "h4", "h5", "h6") else 0
            out.block(node, "#" * level + " " if level else "- " if node.tag == "li" else None)
            stack.append((END, node))
        # A closed <details> hides all its children but its summary (the first <summary> child)
        closed = node.is_("details") and "open" not in node.attrs
        summary = next((c for c in node.children if isinstance(c, Node) and c.is_("summary")), None) if closed else None
        for child, child_path in reversed(_paths(node, path)):
            hidden = closed and child is not summary
            if isinstance(child, str):
                stack.append((child, ctx.hide("details") if hidden else ctx, child_path))
            elif not _excluded(child):
                stack.append((child, ctx.enter(child, base, ("details",) if hidden else ()), child_path))
    return out.result(), out.fragments


def _elements(doc: Node):
    """The elements of the document in tree order, without the contents of <template>."""
    stack = [doc]
    while stack:
        node = stack.pop()
        yield node
        if not node.is_("template"):
            stack.extend(c for c in reversed(node.children) if isinstance(c, Node))


def _title(doc: Node) -> str:
    """The title of the document: the first <title> in tree order (not that of an <svg>), its
    text with ASCII whitespace stripped and collapsed."""
    node = next((n for n in _elements(doc) if n.is_("title")), None)
    return COLLAPSE.sub(" ", node.text()).strip(" ") if node is not None else ""


def _base(doc: Node, url: str) -> str:
    """The base URL: the first <base href> in tree order, against the URL of the document."""
    node = next((n for n in _elements(doc) if n.is_("base") and "href" in n.attrs), None)
    return _absolute(url, node.attrs["href"]) if node is not None and url else url


# --- Entry points ----------------------------------------------------------------------------------

def run(raw: bytes, *, ficha: str, url: str = "", content_type: str | None = None) -> dict:
    """alfa/1 over the bytes of a response: filter, version, ficha, source, title, text and fragments."""
    decoded, encoding, where = decode(raw, content_type)
    tree = parse(decoded)
    base = _base(tree.document, url)
    text, fragments = _body(tree.body, base)
    source = {"url": url, "encoding": encoding, "encoding_from": where,
              "parser": f"html.parser (Python {platform.python_version()})"}
    return {"filter": FILTER, "version": VERSION, "ficha": ficha, "source": source,
            "title": _title(tree.document), "text": text, "fragments": fragments}


def load(page_id: str) -> dict:
    """The page as alfa/1 reads it from the store of capture: the original bytes of the response
    of an audit-es page, its Content-Type and its URL. AlfaError if it cannot."""
    import capture
    from capture import pages

    try:
        info = json.loads(pages.page_path(page_id).with_suffix(".json").read_text(encoding="utf-8"))
    except pages.PageError as e:
        raise AlfaError(str(e)) from e
    if info.get("profile") != "audit-es":
        raise AlfaError(f"{page_id}: es una ficha {info.get('profile') or 'reader'}; alfa/1 lee la respuesta HTTP "
                        "de una ficha audit-es")
    folder = capture.ROOT / info["snapshot"]
    try:
        meta = json.loads((folder / "meta.json").read_text(encoding="utf-8"))
        raw = gzip.decompress((folder / "response.html.gz").read_bytes())
    except (OSError, ValueError) as e:
        raise AlfaError(f"{page_id}: no se puede leer la instantánea {info['snapshot']}: {e}") from e
    if meta.get("response_body") != "original":
        raise AlfaError(f"{page_id}: la instantánea no conserva los bytes originales de la respuesta")
    sha = hashlib.sha256(raw).hexdigest()
    expected = ((meta.get("files") or {}).get("response.html") or {}).get("sha256")
    if expected and expected != sha:
        raise AlfaError(f"{page_id}: el sha256 de la respuesta no es el de su meta.json")
    headers = (meta.get("http") or {}).get("headers") or {}
    return {"raw": raw, "content_type": headers.get("content-type"),
            "url": info.get("url_final") or info.get("url") or "",
            "source": {"profile": "audit-es", "captured_at": info.get("fetched_at"),
                       "snapshot": f"capture/{info['snapshot']}", "sha256": sha}}


def from_page(page_id: str) -> dict:
    """alfa/1 over a frozen audit-es page of capture (its page-ID)."""
    page = load(page_id)
    rep = run(page["raw"], ficha=page_id, url=page["url"], content_type=page["content_type"])
    rep["source"] = page["source"] | rep["source"]
    return rep


def dumps(rep: dict) -> str:
    """JSON with one fragment per line."""
    head = {k: v for k, v in rep.items() if k != "fragments"}
    lines = [f" {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}," for k, v in head.items()]
    frags = [f"  {json.dumps(f, ensure_ascii=False)}" for f in rep["fragments"]]
    body = ",\n".join(frags)
    return "{\n" + "\n".join(lines) + '\n "fragments": [' + (f"\n{body}\n " if frags else "") + "]\n}\n"


def shown(path: Path) -> str:
    """A path from the root of the repository, if it is inside."""
    try:
        return str(path.relative_to(REPO))
    except ValueError:
        return str(path)


def output_path(page_id: str) -> Path:
    return REPRESENTATIONS / f"{page_id}.{FILTER}-{VERSION}.json"


def write(rep: dict) -> tuple[Path, bool]:
    """Write the output of a page; (path, written). An existing output with the same title, text
    and fragments stays; with others, AlfaError: records cite its positions."""
    path = output_path(rep["ficha"])
    if path.exists():
        try:
            old = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, ValueError):
            old = None
        same = old is not None and all(old.get(k) == rep[k] for k in ("filter", "version", "title", "text", "fragments"))
        if same:
            return path, False
        raise AlfaError(f"{shown(path)} ya existe con otra salida, y los registros citan sus posiciones. "
                        "Si quieres sustituirla, bórrala antes")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(dumps(rep), encoding="utf-8")
    return path, True
