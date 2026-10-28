"""A document tree from the HTML of a response, with the standard library only.

html.parser tokenizes; the tree is built with the few rules of the HTML parsing algorithm that
the methods of the reference depend on: void elements; the head closes at the first element that
cannot be in it (or at non-blank text), so a link or meta after it is in the body; a start tag of
p, li, option, dt or dd closes the open one; and an end tag closes up to its open element, or is
ignored if there is none. script and style keep their text as it is (html.parser does not decode
references in them). Each element keeps its line and column in the document.

Visible text (method common to Web Schema.org, point 7): the text outside script, style and
template and outside elements with hidden, aria-hidden="true" or an inline display:none. With
JavaScript disabled (audit-es) noscript is rendered, so its text counts.
"""
from __future__ import annotations

import re
from html.parser import HTMLParser

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track",
        "wbr", "param", "keygen", "basefont", "bgsound", "frame"}
HEAD_ONLY = {"base", "basefont", "bgsound", "link", "meta", "title", "style", "script", "noscript",
             "template"}
AUTOCLOSE = {"p": {"p"}, "li": {"li"}, "option": {"option"}, "dt": {"dt", "dd"}, "dd": {"dt", "dd"},
             "tr": {"tr"}, "td": {"td", "th"}, "th": {"td", "th"}}
BLOCK_CLOSES_P = {"address", "article", "aside", "blockquote", "div", "dl", "fieldset", "footer", "form",
                  "h1", "h2", "h3", "h4", "h5", "h6", "header", "hr", "main", "nav", "ol", "p", "pre",
                  "section", "table", "ul", "figure", "details", "menu"}
INVISIBLE = {"script", "style", "template"}
# Elements whose text does not run into the text around them
BLOCKS = {"address", "article", "aside", "blockquote", "br", "button", "dd", "details", "div", "dl", "dt", "figcaption",
          "figure", "footer", "form", "h1", "h2", "h3", "h4", "h5", "h6", "header", "hr", "label", "li", "main", "nav",
          "noscript", "ol", "option", "p", "pre", "section", "summary", "table", "td", "th", "tr", "ul"}
DISPLAY_NONE = re.compile(r"display\s*:\s*none", re.I)
SPACE = re.compile(r"\s+")


class Element:
    __slots__ = ("tag", "attrs", "children", "parent", "line", "col", "raw")

    def __init__(self, tag: str, attrs: list, parent: "Element | None", line: int = 0, col: int = 0,
                 raw: str = "") -> None:
        self.tag = tag
        self.attrs: dict[str, str] = {}
        for name, value in attrs:
            self.attrs.setdefault(name, "" if value is None else value)  # the first one wins
        self.children: list = []  # Element or str
        self.parent = parent
        self.line, self.col, self.raw = line, col, raw

    def get(self, name: str, default=None):
        return self.attrs.get(name, default)

    def has(self, name: str) -> bool:
        return name in self.attrs

    def iter(self):
        """This element and its descendants, in tree order."""
        stack = [self]
        while stack:
            node = stack.pop()
            yield node
            stack.extend(c for c in reversed(node.children) if isinstance(c, Element))

    def ancestors(self):
        node = self.parent
        while node is not None:
            yield node
            node = node.parent

    def in_(self, tag: str) -> bool:
        return any(a.tag == tag for a in self.ancestors())

    def text(self) -> str:
        """textContent: every descendant text, in order."""
        out = []
        stack = [self]
        while stack:
            node = stack.pop()
            if isinstance(node, str):
                out.append(node)
            else:
                stack.extend(reversed(node.children))
        return "".join(out)

    def where(self) -> str:
        return f"<{self.tag}> línea {self.line}"


class Document:
    def __init__(self, root: Element, source: str) -> None:
        self.root = root
        self.source = source
        self.ids: dict[str, Element] = {}
        for el in root.iter():
            if "id" in el.attrs and el.attrs["id"] not in self.ids:
                self.ids[el.attrs["id"]] = el

    def all(self, tag: str | None = None):
        return [e for e in self.root.iter() if e is not self.root and (tag is None or e.tag == tag)]

    def head(self) -> Element | None:
        return next((e for e in self.root.iter() if e.tag == "head"), None)

    def body(self) -> Element | None:
        return next((e for e in self.root.iter() if e.tag == "body"), None)

    def in_head(self, el: Element) -> bool:
        return el.in_("head")

    def visible_text(self, within: Element | None = None) -> str:
        out = []

        def walk(node):
            if isinstance(node, str):
                out.append(node)
                return
            if node.tag in INVISIBLE or node.has("hidden") or node.get("aria-hidden", "").strip().lower() == "true":
                return
            if DISPLAY_NONE.search(node.get("style", "")):
                return
            block = node.tag in BLOCKS
            if block:
                out.append(" ")
            for child in node.children:
                walk(child)
            if block:
                out.append(" ")

        walk(within or self.root)
        return SPACE.sub(" ", "".join(out)).strip()


class _Builder(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = Element("#document", [], None)
        self.stack = [self.root]
        self.head_closed = False

    @property
    def current(self) -> Element:
        return self.stack[-1]

    def _close_head_if_needed(self, tag: str | None) -> None:
        if self.head_closed:
            return
        tags = [e.tag for e in self.stack]
        if "head" not in tags:
            return
        if tag is not None and tag in HEAD_ONLY:
            return
        # inside noscript, script, style… of the head the rule is the same: pop to the head's parent
        while self.stack and self.stack[-1].tag != "head":
            self.stack.pop()
        self.stack.pop()
        self.head_closed = True

    def _ensure_body(self) -> None:
        if any(e.tag == "body" for e in self.stack):
            return
        html = next((e for e in self.stack if e.tag == "html"), None)
        parent = html or self.root
        while self.stack[-1] is not parent:
            self.stack.pop()
        body = Element("body", [], parent, *self.getpos())
        parent.children.append(body)
        self.stack.append(body)

    def handle_starttag(self, tag, attrs):
        line, col = self.getpos()
        raw = self.get_starttag_text() or ""
        if tag == "head":
            if any(e.tag == "head" for e in self.root.iter()):
                return
        elif tag == "body":
            self._close_head_if_needed(None)
            if any(e.tag == "body" for e in self.stack):
                return
        elif tag not in ("html",):
            if not self.head_closed and any(e.tag == "head" for e in self.stack):
                self._close_head_if_needed(tag)
            if self.head_closed and tag not in HEAD_ONLY:
                self._ensure_body()
        closes = AUTOCLOSE.get(tag, set()) | ({"p"} if tag in BLOCK_CLOSES_P else set())
        if closes:
            for i in range(len(self.stack) - 1, 0, -1):
                if self.stack[i].tag in closes:
                    del self.stack[i:]
                    break
                if self.stack[i].tag in ("div", "ul", "ol", "table", "body", "section", "article", "form"):
                    break
        el = Element(tag, attrs, self.current, line, col, raw)
        self.current.children.append(el)
        if tag not in VOID:
            self.stack.append(el)

    def handle_startendtag(self, tag, attrs):
        line, col = self.getpos()
        el = Element(tag, attrs, self.current, line, col, self.get_starttag_text() or "")
        if tag not in ("svg", "math") and not self.head_closed and any(e.tag == "head" for e in self.stack):
            self._close_head_if_needed(tag)
            if self.head_closed and tag not in HEAD_ONLY:
                self._ensure_body()
                el.parent = self.current
        self.current.children.append(el)

    def handle_endtag(self, tag):
        for i in range(len(self.stack) - 1, 0, -1):
            if self.stack[i].tag == tag:
                if tag == "head":
                    self.head_closed = True
                del self.stack[i:]
                return

    def handle_data(self, data):
        if not self.head_closed and data.strip() and self.current.tag == "head":
            self._close_head_if_needed(None)
            self._ensure_body()
        self.current.children.append(data)


def parse(text: str) -> Document:
    builder = _Builder()
    builder.feed(text)
    builder.close()
    return Document(builder.root, text)
