"""Text of an HTML page as light Markdown (text.md): what a citation quotes and what a page
counts by. Also the publisher's own version marker of a page, kept in the manifest."""
import codecs
import re
from html.parser import HTMLParser

PUBLISHED = (               # the publisher's own version marker, kept in the manifest
    (re.compile(r"Last updated (\d{4}-\d{2}-\d{2}) UTC"), "Last updated {0}"),        # Google developers
    (re.compile(r'id="versioninfo".{0,300}?V([\d.]+).{0,100}?(\d{4}-\d{2}-\d{2})', re.S), "Schema.org V{0} ({1})"),
    (re.compile(r"This version:.{0,300}?href=\"([^\"]+)\"", re.S), "This version: {0}"),  # W3C
)

SKIP_TAGS = {"script", "style", "noscript", "template", "svg", "nav", "header", "footer", "aside",
             "form", "button", "select", "iframe"}
BLOCK_TAGS = {"address", "article", "blockquote", "body", "caption", "dd", "details", "div", "dl",
              "dt", "figcaption", "figure", "hr", "main", "ol", "p", "section", "summary", "table",
              "tbody", "tfoot", "thead", "ul"}
HEADINGS = {f"h{n}": n for n in range(1, 7)}


class TextExtractor(HTMLParser):
    """The text of a page as light Markdown: headings with their anchor ({#id}), list items,
    one line per table row and code blocks. Only the content root counts (main, else article,
    else body); navigation, headers, footers, forms and scripts are left out."""

    def __init__(self, root: str, inside: bool):
        super().__init__(convert_charrefs=True)
        self.root, self.inside = root, int(inside)
        self.skipping = []      # open skipped elements
        self.lines, self.inline = [], []
        self.bullet = ""        # list mark waiting for the first line of its item
        self.lists = 0
        self.heading = None     # [level, anchor] of the open heading
        self.sections = []      # [id, its heading seen] of the open <section> elements
        self.row = None         # cells of the open table row
        self.cell = False       # a cell is open (its end tag may be omitted)
        self.pre = 0

    def flush(self, head: str = "", tail: str = "") -> None:
        text = re.sub(r"[ \t]+", " ", "".join(self.inline)).strip()
        self.inline = []
        if text:
            self.lines.append(self.bullet + head + text + tail)
            self.bullet = ""

    def end_cell(self) -> None:
        if self.cell:
            self.row.append(re.sub(r"\s+", " ", "".join(self.inline)).strip())
            self.inline, self.cell = [], False

    def end_row(self) -> None:
        self.end_cell()
        if any(self.row):
            self.lines.append("| " + " | ".join(self.row) + " |")
        self.row = None

    def handle_starttag(self, tag, attrs):
        if tag == self.root:
            self.inside += 1
        if self.skipping or tag in SKIP_TAGS:
            if tag in SKIP_TAGS:
                self.skipping.append(tag)
            return
        if not self.inside:
            return
        attrs = dict(attrs)
        if tag == "section":
            self.sections.append([attrs.get("id"), False])
        if self.heading and not self.heading[1] and tag == "a":
            self.heading[1] = attrs.get("id") or attrs.get("name")
        if self.row is not None:
            if tag in ("td", "th"):
                self.end_cell()
                self.cell = True
            elif tag == "tr":
                self.end_row()
                self.row = []
            elif tag in BLOCK_TAGS or tag in HEADINGS or tag in ("br", "li", "pre"):
                self.inline.append(" ")
            return
        if tag == "tr":
            self.flush()
            self.row = []
        elif tag in HEADINGS:
            # The anchor a citation names: that of the section the heading opens (W3C), else its
            # own id, else that of an <a id|name> inside it (Google Help)
            self.flush()
            section = self.sections[-1] if self.sections else [None, True]
            self.heading = [HEADINGS[tag], section[0] if not section[1] else attrs.get("id")]
            self.heading[1] = self.heading[1] or attrs.get("id")
            section[1] = True
        elif tag == "li":
            self.flush()
            self.bullet = "  " * max(self.lists - 1, 0) + "- "
        elif tag == "pre":
            self.flush()
            self.pre += 1
        elif tag == "br":
            self.inline.append("\n" if self.pre else " ")
            if not self.pre:
                self.flush()
        elif tag in BLOCK_TAGS:
            self.flush()
            if tag in ("ul", "ol"):
                self.lists += 1

    def handle_endtag(self, tag):
        if tag == self.root and self.inside:
            self.inside -= 1
        if self.skipping:
            if tag in self.skipping:
                while self.skipping.pop() != tag:
                    pass
            return
        if not self.inside and tag != self.root:
            return
        if tag == "section" and self.sections:
            self.sections.pop()
        if self.row is not None:
            if tag in ("td", "th"):
                self.end_cell()
            elif tag in ("tr", "table"):
                self.end_row()
            return
        if tag in HEADINGS and self.heading:
            level, anchor = self.heading
            self.lines.append("")
            self.flush("#" * level + " ", f" {{#{anchor}}}" if anchor else "")
            self.lines.append("")
            self.heading = None
        elif tag == "pre" and self.pre:
            self.pre -= 1
            code = "".join(self.inline).strip("\n")
            self.inline = []
            if code.strip():
                self.lines += ["", "```", code, "```", ""]
        elif tag in BLOCK_TAGS or tag == "li":
            self.flush()
            if tag in ("ul", "ol") and self.lists:
                self.lists -= 1
            if tag == "p":
                self.lines.append("")

    def handle_data(self, data):
        if self.skipping or not self.inside:
            return
        self.inline.append(data if self.pre else re.sub(r"\s+", " ", data))

    def text(self) -> str:
        self.flush()
        out = "\n".join(self.lines)
        return re.sub(r"\n{3,}", "\n\n", out).strip() + "\n"


def charset(html: bytes, content_type: str) -> str:
    match = re.search(r"charset=([\w-]+)", content_type or "") \
        or re.search(rb"<meta[^>]+charset=[\"']?([\w-]+)", html[:4096], re.I)
    name = match.group(1) if match else "utf-8"
    name = name.decode("ascii") if isinstance(name, bytes) else name
    try:
        return codecs.lookup(name).name
    except LookupError:
        return "utf-8"


def page_text(html: str) -> str:
    """Text of an HTML page (see TextExtractor)."""
    root = next((t for t in ("main", "article") if re.search(rf"<{t}[\s>]", html, re.I)), "body")
    parser = TextExtractor(root, inside=not re.search(rf"<{root}[\s>]", html, re.I))
    parser.feed(html)
    parser.close()
    return parser.text()


def published(html: str):
    for pattern, label in PUBLISHED:
        match = pattern.search(html)
        if match:
            return label.format(*match.groups())
    return None
