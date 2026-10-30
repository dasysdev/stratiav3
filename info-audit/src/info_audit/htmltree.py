"""The document tree of an HTML response, with the standard library only (filter-alfa.md).

html.parser tokenizes as the HTML Living Standard does with scripting disabled: <noscript> is
markup, <script>, <style>, <iframe>, <xmp>, <noembed> and <noframes> are raw text, and <title>
and <textarea> are escapable raw text. On that token stream the builder applies the rules of the
tree construction stage that decide where each node goes:

- the implied html, head and body, and what goes in the head (with scripting disabled, an
  element of <noscript> that cannot be in the head closes it and goes to the body);
- void elements, and the self-closing flag, which only counts in SVG and MathML;
- the implied end tags (p, li, dd, dt, option, optgroup, rb, rp, rt, rtc), the closing of p by
  the blocks, and the scopes that limit an end tag;
- tables: the implied tbody and tr, the closing of cells and rows, and foster parenting of
  text and elements that are directly in a table;
- foreign content (SVG and MathML), its integration points and the HTML elements that break
  out of it; there <title>, <style> and the rest are markup, not raw text, and CDATA sections
  are text;
- newlines: CR LF and CR are LF, and the newline right after <pre>, <listing> and <textarea>
  is dropped.

Simplified, without effect on the text or its order: the adoption agency algorithm and the
reconstruction of the active formatting elements (an end tag of a formatting element closes it
and what is open inside it; a new <a> or <nobr> closes the open one), the frameset mode and
the quirks mode. Comments, the doctype and processing instructions are not in the tree.
"""
from __future__ import annotations

from html import unescape
from html.parser import HTMLParser

HTML, SVG, MATH = "html", "svg", "math"
WS = " \t\n\f\r"

VOID = {"area", "base", "basefont", "bgsound", "br", "col", "embed", "frame", "hr", "img", "input", "keygen",
        "link", "meta", "param", "source", "track", "wbr"}
HEAD_ELEMENTS = {"base", "basefont", "bgsound", "link", "meta", "noframes", "script", "style", "template", "title"}
HEAD_NOSCRIPT = {"basefont", "bgsound", "link", "meta", "noframes", "style"}
CLOSE_P = {"address", "article", "aside", "blockquote", "center", "details", "dialog", "dir", "div", "dl",
           "fieldset", "figcaption", "figure", "footer", "header", "hgroup", "main", "menu", "nav", "ol", "p",
           "search", "section", "summary", "ul"}
HEADINGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
BLOCK_END = CLOSE_P - {"p"} | {"button", "listing", "pre", "select"}
FORMATTING = {"a", "b", "big", "code", "em", "font", "i", "nobr", "s", "small", "strike", "strong", "tt", "u"}
IMPLIED_END = {"dd", "dt", "li", "optgroup", "option", "p", "rb", "rp", "rt", "rtc"}
SPECIAL = {"address", "applet", "area", "article", "aside", "base", "basefont", "bgsound", "blockquote", "body",
           "br", "button", "caption", "center", "col", "colgroup", "dd", "details", "dir", "div", "dl", "dt",
           "embed", "fieldset", "figcaption", "figure", "footer", "form", "frame", "frameset", "h1", "h2", "h3",
           "h4", "h5", "h6", "head", "header", "hgroup", "hr", "html", "iframe", "img", "input", "keygen", "li",
           "link", "listing", "main", "marquee", "menu", "meta", "nav", "noembed", "noframes", "noscript",
           "object", "ol", "p", "param", "plaintext", "pre", "script", "search", "section", "select", "source",
           "style", "summary", "table", "tbody", "td", "template", "textarea", "tfoot", "th", "thead", "title",
           "tr", "track", "ul", "wbr", "xmp"}
SPECIAL_FOREIGN = {(MATH, t) for t in ("mi", "mo", "mn", "ms", "mtext", "annotation-xml")} | \
                  {(SVG, t) for t in ("foreignobject", "desc", "title")}
SCOPE = {"applet", "caption", "html", "table", "td", "th", "marquee", "object", "template"}
TABLE_SCOPE = {"html", "table", "template"}
TABLE_PARTS = {"caption", "col", "colgroup", "tbody", "td", "tfoot", "th", "thead", "tr"}
SECTIONS = {"tbody", "thead", "tfoot"}
FOSTER_TARGETS = {"table", "tbody", "tfoot", "thead", "tr"}
BREAKOUT = {"b", "big", "blockquote", "body", "br", "center", "code", "dd", "div", "dl", "dt", "em", "embed",
            "h1", "h2", "h3", "h4", "h5", "h6", "head", "hr", "i", "img", "li", "listing", "menu", "meta",
            "nobr", "ol", "p", "pre", "ruby", "s", "small", "span", "strong", "strike", "sub", "sup", "table",
            "tt", "u", "ul", "var"}
MATH_TEXT_POINTS = {"mi", "mo", "mn", "ms", "mtext"}
RAW_TEXT = {"iframe", "noembed", "noframes", "plaintext", "script", "style", "textarea", "title", "xmp"}
MARKERS = {"applet", "caption", "marquee", "object", "td", "template", "th"}


class Node:
    """An element: its tag (lower case), namespace, attributes (the first of each name wins),
    children (Node or str, adjacent text merged as in the DOM) and parent."""
    __slots__ = ("tag", "ns", "attrs", "children", "parent")

    def __init__(self, tag: str, attrs: dict[str, str] | None = None, ns: str = HTML) -> None:
        self.tag, self.ns = tag, ns
        self.attrs = attrs or {}
        self.children: list = []
        self.parent: Node | None = None

    def is_(self, *tags: str, ns: str = HTML) -> bool:
        return self.ns == ns and self.tag in tags

    def append(self, child) -> None:
        self.insert(child, len(self.children))

    def insert(self, child, index: int) -> None:
        if isinstance(child, str):
            if index > 0 and isinstance(self.children[index - 1], str):
                self.children[index - 1] += child
                return
            self.children.insert(index, child)
            return
        child.parent = self
        self.children.insert(index, child)

    def iter(self):
        """This element and its descendant elements, in tree order."""
        stack = [self]
        while stack:
            node = stack.pop()
            yield node
            stack.extend(c for c in reversed(node.children) if isinstance(c, Node))

    def text(self) -> str:
        """The descendant text content (DOM §4.4)."""
        out, stack = [], [self]
        while stack:
            node = stack.pop()
            if isinstance(node, str):
                out.append(node)
            else:
                stack.extend(reversed(node.children))
        return "".join(out)

    def __repr__(self) -> str:
        return f"<{self.tag}>" if self.ns == HTML else f"<{self.ns}:{self.tag}>"


def _attrs(raw: list) -> dict[str, str]:
    out: dict[str, str] = {}
    for name, value in raw:
        out.setdefault(name, "" if value is None else value)
    return out


class Builder(HTMLParser):
    """The tree construction stage over the tokens of html.parser (see the module)."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.document = Node("#document")
        self.html: Node | None = None
        self.head: Node | None = None
        self.body: Node | None = None
        self.form: Node | None = None
        self.stack: list[Node] = []
        self.mode = "before html"
        self.skip_newline = False
        self.last: Node | None = None   # the element inserted for the last start tag

    # --- The stack of open elements -------------------------------------------------------------

    @property
    def current(self) -> Node:
        return self.stack[-1] if self.stack else self.document

    def _in_scope(self, tags, extra=frozenset(), table=False) -> Node | None:
        tags = {tags} if isinstance(tags, str) else tags
        for node in reversed(self.stack):
            if node.ns == HTML and node.tag in tags:
                return node
            if table:
                if node.ns == HTML and node.tag in TABLE_SCOPE:
                    return None
            elif (node.ns == HTML and (node.tag in SCOPE or node.tag in extra)) or (node.ns, node.tag) in SPECIAL_FOREIGN:
                return None
        return None

    def _pop_until(self, tags) -> None:
        tags = {tags} if isinstance(tags, str) else tags
        while self.stack:
            node = self.stack.pop()
            if node.ns == HTML and node.tag in tags:
                return

    def _implied_end(self, keep: str | None = None) -> None:
        while self.stack and self.current.ns == HTML and self.current.tag in IMPLIED_END and self.current.tag != keep:
            self.stack.pop()

    def _close_p(self) -> None:
        if self._in_scope("p", {"button"}):
            self._implied_end("p")
            self._pop_until("p")

    def _clear_to(self, tags) -> None:
        while self.stack and not (self.current.ns == HTML and self.current.tag in tags):
            self.stack.pop()

    def _special(self, node: Node) -> bool:
        return (node.ns == HTML and node.tag in SPECIAL) or (node.ns, node.tag) in SPECIAL_FOREIGN

    def _in_template(self) -> bool:
        return any(n.ns == HTML and n.tag == "template" for n in self.stack)

    def _formatting(self, tag: str) -> Node | None:
        """The open formatting element with this tag after the last marker (td, th, caption…)."""
        for node in reversed(self.stack):
            if node.is_(tag):
                return node
            if node.ns == HTML and node.tag in MARKERS:
                return None
        return None

    # --- Insertion ------------------------------------------------------------------------------

    def _foster(self) -> bool:
        return self.current.ns == HTML and self.current.tag in FOSTER_TARGETS and self._table_mode()

    def _table_mode(self) -> bool:
        """The insertion mode is one of the table ones (in table, in table body, in row)."""
        for node in reversed(self.stack):
            if node.ns != HTML:
                return False
            if node.tag in ("td", "th", "caption", "template", "html", "body"):
                return False
            if node.tag in FOSTER_TARGETS:
                return True
        return False

    def _place(self, foster: bool) -> tuple[Node, int]:
        """The appropriate place for inserting a node: the current node or, with foster parenting,
        just before the last table."""
        if foster:
            table = next((n for n in reversed(self.stack) if n.is_("table")), None)
            template = next((n for n in reversed(self.stack) if n.is_("template")), None)
            if template and (table is None or self.stack.index(template) > self.stack.index(table)):
                return template, len(template.children)
            if table is None:
                return self.html, len(self.html.children)
            if table.parent is not None:
                return table.parent, table.parent.children.index(table)
            above = self.stack[self.stack.index(table) - 1]
            return above, len(above.children)
        return self.current, len(self.current.children)

    def _insert(self, tag: str, attrs: dict, ns: str = HTML, void: bool = False, foster: bool = False) -> Node:
        node = Node(tag, attrs, ns)
        parent, index = self._place(foster)
        parent.insert(node, index)
        if not void:
            self.stack.append(node)
        self.last = node
        return node

    def _text(self, data: str) -> None:
        if not data:
            return
        foster = self._foster() and data.strip(WS) != ""
        parent, index = self._place(foster)
        parent.insert(data, index)

    # --- Before the body ------------------------------------------------------------------------

    def _ensure_html(self) -> None:
        if self.html is None:
            self.html = Node("html")
            self.document.append(self.html)
            self.stack.append(self.html)
            self.mode = "before head"

    def _ensure_head(self) -> None:
        self._ensure_html()
        if self.head is None:
            self.head = self._insert("head", {})
            self.mode = "in head"

    def _leave_head(self) -> None:
        if self.mode == "in head noscript":
            self._pop_until("noscript")
            self.mode = "in head"
        if self.mode == "in head":
            if self.head in self.stack:
                del self.stack[self.stack.index(self.head):]
            self.mode = "after head"

    def _ensure_body(self) -> None:
        self._ensure_head()
        self._leave_head()
        if self.body is None:
            del self.stack[1:]
            self.body = self._insert("body", {})
        self.mode = "in body"

    # --- Tokens ---------------------------------------------------------------------------------

    def _html_rules(self) -> bool:
        """The token goes by the HTML rules, not those of foreign content."""
        node = self.current
        if not self.stack or node.ns == HTML:
            return True
        if node.ns == MATH and node.tag in MATH_TEXT_POINTS:
            return True
        if node.ns == SVG and node.tag in ("foreignobject", "desc", "title"):
            return True
        if node.ns == MATH and node.tag == "annotation-xml":
            return node.attrs.get("encoding", "").lower() in ("text/html", "application/xhtml+xml")
        return False

    def _set_cdata_support(self) -> None:
        """CDATA sections only when the current node is not in the HTML namespace."""
        if hasattr(self, "_set_support_cdata"):
            self._set_support_cdata(bool(self.stack) and self.current.ns != HTML)

    def handle_starttag(self, tag, attrs):
        self.last = None
        self._start(tag, _attrs(attrs), self_closing=False)
        # html.parser makes <title>, <style>, <textarea>… raw text by their name; in SVG and
        # MathML they are not, and their content is markup
        if self.last is not None and self.last.ns != HTML and self.last.tag == tag:
            self.CDATA_CONTENT_ELEMENTS = self.RCDATA_CONTENT_ELEMENTS = ()
        else:
            self.__dict__.pop("CDATA_CONTENT_ELEMENTS", None)
            self.__dict__.pop("RCDATA_CONTENT_ELEMENTS", None)
        self._set_cdata_support()

    def handle_startendtag(self, tag, attrs):
        self._start(tag, _attrs(attrs), self_closing=True)
        # In HTML the flag does not count: a raw text element still swallows what follows
        if self.current.is_(tag) and tag in HTMLParser.CDATA_CONTENT_ELEMENTS:
            self.set_cdata_mode(tag)
        elif self.current.is_(tag) and tag in getattr(HTMLParser, "RCDATA_CONTENT_ELEMENTS", ()):
            self.set_cdata_mode(tag, escapable=True)
        self._set_cdata_support()

    def handle_endtag(self, tag):
        self._end(tag)
        self._set_cdata_support()

    def handle_data(self, data):
        data = data.replace("\x00", "")
        if self.skip_newline:
            self.skip_newline = False
            if data.startswith("\n"):
                data = data[1:]
        if not data:
            return
        if self.mode == "in body" or self._in_template() or (self.current.ns == HTML and self.current.tag in RAW_TEXT):
            self._text(data)
            return
        lead = len(data) - len(data.lstrip(WS))
        if lead == len(data):
            if self.mode in ("in head", "in head noscript", "after head"):
                self._text(data)
            return
        if self.mode in ("in head", "in head noscript"):
            self._text(data[:lead])
        self._ensure_body()
        self._text(data[lead:])

    def handle_charref(self, name):
        self.handle_data(unescape(f"&#{name};"))

    def handle_entityref(self, name):
        self.handle_data(unescape(f"&{name};"))

    def unknown_decl(self, data):
        if data.startswith("CDATA[") and self.stack and self.current.ns != HTML:
            self._text(data[6:])

    # --- Start tags -----------------------------------------------------------------------------

    def _start(self, tag: str, attrs: dict, self_closing: bool) -> None:
        if tag == "image":
            tag = "img"
        if not self._html_rules():
            node = self.current
            if node.ns == MATH and node.tag == "annotation-xml" and tag == "svg":
                pass   # by the HTML rules: an svg element
            elif tag in BREAKOUT or (tag == "font" and {"color", "face", "size"} & attrs.keys()):
                while self.stack and not self._html_rules():
                    self.stack.pop()
            else:
                self._insert(tag, attrs, node.ns, void=self_closing)
                return
        self.skip_newline = False
        if self.mode != "in body" and not self._in_template():
            if self._start_before_body(tag, attrs):
                return
        self._start_in_body(tag, attrs, self_closing)

    def _start_before_body(self, tag: str, attrs: dict) -> bool:
        """The modes before the body; True if the token is done."""
        if tag == "html":
            self._ensure_html()
            for k, v in attrs.items():
                self.html.attrs.setdefault(k, v)
            return True
        if self.mode in ("before html", "before head"):
            self._ensure_html()
            if tag == "head":
                self.head = self._insert("head", attrs)
                self.mode = "in head"
                return True
            self._ensure_head()
        if self.mode == "in head noscript":
            if tag in HEAD_NOSCRIPT:
                self._insert(tag, attrs, void=tag in VOID)
                return True
            if tag in ("head", "noscript"):
                return True
            self._pop_until("noscript")
            self.mode = "in head"
        if self.mode == "in head":
            if tag == "head":
                return True
            if tag == "noscript":
                self._insert(tag, attrs)
                self.mode = "in head noscript"
                return True
            if tag in HEAD_ELEMENTS:
                self._insert(tag, attrs, void=tag in VOID)
                return True
            self._leave_head()
        if self.mode == "after head":
            if tag == "head":
                return True
            if tag in HEAD_ELEMENTS:   # back into the head, which leaves the stack again
                self.stack.append(self.head)
                self._insert(tag, attrs, void=tag in VOID)
                self.stack.remove(self.head)
                return True
            if tag == "body":
                del self.stack[1:]
                self.body = self._insert("body", attrs)
                self.mode = "in body"
                return True
            self._ensure_body()
        return False

    def _start_in_body(self, tag: str, attrs: dict, self_closing: bool) -> None:
        if tag in TABLE_PARTS or tag == "table" or self._table_mode():
            if self._start_in_table(tag, attrs):
                return
        foster = self._foster()
        if tag == "html":
            if self.html is not None:
                for k, v in attrs.items():
                    self.html.attrs.setdefault(k, v)
        elif tag == "body":
            if self.body is not None:
                for k, v in attrs.items():
                    self.body.attrs.setdefault(k, v)
        elif tag in ("head", "frameset", "frame") or tag in TABLE_PARTS:
            pass
        elif tag in HEAD_ELEMENTS:
            self._insert(tag, attrs, void=tag in VOID, foster=foster and tag not in ("script", "style", "template"))
        elif tag in CLOSE_P:
            self._close_p()
            self._insert(tag, attrs, foster=foster)
        elif tag in HEADINGS:
            self._close_p()
            if self.current.ns == HTML and self.current.tag in HEADINGS:
                self.stack.pop()
            self._insert(tag, attrs, foster=foster)
        elif tag in ("pre", "listing"):
            self._close_p()
            self._insert(tag, attrs, foster=foster)
            self.skip_newline = True
        elif tag == "form":
            if self.form is not None and not any(n.is_("template") for n in self.stack):
                return
            self._close_p()
            node = self._insert(tag, attrs, foster=foster)
            if not any(n.is_("template") for n in self.stack):
                self.form = node
        elif tag in ("li", "dd", "dt"):
            closes = {"li"} if tag == "li" else {"dd", "dt"}
            for node in reversed(self.stack):
                if node.ns == HTML and node.tag in closes:
                    self._implied_end(node.tag)
                    self._pop_until(node.tag)
                    break
                if self._special(node) and not node.is_("address", "div", "p"):
                    break
            self._close_p()
            self._insert(tag, attrs, foster=foster)
        elif tag == "plaintext":
            self._close_p()
            self._insert(tag, attrs, foster=foster)
        elif tag == "button":
            if self._in_scope("button"):
                self._implied_end()
                self._pop_until("button")
            self._insert(tag, attrs, foster=foster)
        elif tag in ("a", "nobr"):
            node = self._formatting(tag)
            if node is not None:
                del self.stack[self.stack.index(node):]
            self._insert(tag, attrs, foster=foster)
        elif tag == "hr":
            self._close_p()
            self._insert(tag, attrs, void=True, foster=foster)
        elif tag == "xmp":
            self._close_p()
            self._insert(tag, attrs, foster=foster)
        elif tag == "textarea":
            self._insert(tag, attrs, foster=foster)
            self.skip_newline = True
        elif tag == "select":
            if self._in_scope("select"):
                self._pop_until("select")
                return
            self._insert(tag, attrs, foster=foster)
        elif tag == "option":
            if self.current.is_("option"):
                self.stack.pop()
            self._insert(tag, attrs, foster=foster)
        elif tag == "optgroup":
            if self.current.is_("option"):
                self.stack.pop()
            if self.current.is_("optgroup"):
                self.stack.pop()
            self._insert(tag, attrs, foster=foster)
        elif tag in ("svg", "math"):
            self._insert(tag, attrs, SVG if tag == "svg" else MATH, void=self_closing, foster=foster)
        elif tag == "input" and foster and attrs.get("type", "").lower() == "hidden":
            self._insert(tag, attrs, void=True)
        else:
            self._insert(tag, attrs, void=tag in VOID, foster=foster)

    def _start_in_table(self, tag: str, attrs: dict) -> bool:
        """The table modes for a start tag; True if the token is done."""
        mode = self._table_context()
        if mode in (None, "cell", "caption"):
            if tag == "table":
                self._close_p()
                self._insert(tag, attrs)
                return True
            if tag not in TABLE_PARTS:
                return False
            if mode == "cell" and self._in_scope({"td", "th"}, table=True):
                self._close_cell()
            elif mode == "caption":
                self._pop_until("caption")
            else:
                return True   # a table part outside a table, or a cell outside its scope, is ignored
            self._start_in_body(tag, attrs, False)
            return True
        if mode == "row":
            if tag in ("td", "th"):
                self._clear_to({"tr", "template", "html"})
                self._insert(tag, attrs)
                return True
            if tag in TABLE_PARTS or tag == "table":
                if self._in_scope("tr", table=True):
                    self._clear_to({"tr", "template", "html"})
                    self.stack.pop()
                    return self._start_in_table(tag, attrs)
                return True
        if mode == "section":
            if tag == "tr":
                self._clear_to(SECTIONS | {"template", "html"})
                self._insert(tag, attrs)
                return True
            if tag in ("td", "th"):
                self._clear_to(SECTIONS | {"template", "html"})
                self._insert("tr", {})
                return self._start_in_table(tag, attrs)
            if tag in TABLE_PARTS or tag == "table":
                if self._in_scope(SECTIONS, table=True):
                    self._clear_to(SECTIONS | {"template", "html"})
                    self.stack.pop()
                    return self._start_in_table(tag, attrs)
                return True
        # in table
        if tag == "caption":
            self._clear_to({"table", "template", "html"})
            self._insert(tag, attrs)
            return True
        if tag == "colgroup":
            self._clear_to({"table", "template", "html"})
            self._insert(tag, attrs)
            self.stack.pop()   # its content (col) is void and has no text
            return True
        if tag == "col":
            self._clear_to({"table", "template", "html"})
            colgroup = self._insert("colgroup", {})
            colgroup.append(Node("col", attrs))
            self.stack.pop()
            return True
        if tag in SECTIONS:
            self._clear_to({"table", "template", "html"})
            self._insert(tag, attrs)
            return True
        if tag in ("td", "th", "tr"):
            self._clear_to({"table", "template", "html"})
            self._insert("tbody", {})
            return self._start_in_table(tag, attrs)
        if tag == "table":
            if self._in_scope("table", table=True):
                self._pop_until("table")
                self._start_in_body(tag, attrs, False)
            return True
        if tag == "form":
            if self.form is None and not any(n.is_("template") for n in self.stack):
                self.form = self._insert(tag, attrs)
                self.stack.pop()
            return True
        return False

    def _table_context(self) -> str | None:
        """The table mode by the stack: cell, caption, row, section, table, or None outside tables."""
        for node in reversed(self.stack):
            if node.ns != HTML:
                continue
            if node.tag in ("td", "th"):
                return "cell"
            if node.tag == "caption":
                return "caption"
            if node.tag == "tr":
                return "row"
            if node.tag in SECTIONS:
                return "section"
            if node.tag == "table":
                return "table"
            if node.tag in ("template", "html", "body"):
                return None
        return None

    def _close_cell(self) -> None:
        self._implied_end()
        self._pop_until({"td", "th"})

    # --- End tags -------------------------------------------------------------------------------

    def _end(self, tag: str) -> None:
        # An end tag goes by the rules of foreign content also at an integration point
        if self.stack and self.current.ns != HTML:
            if tag in ("br", "p"):
                while self.stack and not self._html_rules():
                    self.stack.pop()
            else:
                for i in range(len(self.stack) - 1, 0, -1):
                    node = self.stack[i]
                    if node.ns == HTML:
                        break
                    if node.tag == tag:
                        del self.stack[i:]
                        return
        self.skip_newline = False
        if self.current.ns == HTML and self.current.tag in RAW_TEXT and self.current.tag == tag:
            self.stack.pop()
            return
        if self.mode != "in body" and not self._in_template():
            if self.mode == "in head noscript" and tag == "noscript":
                self._pop_until("noscript")
                self.mode = "in head"
                return
            if self.mode == "in head" and tag == "head":
                self._leave_head()
                return
            if tag != "br":
                return   # ignored before the body (</body> and </html> change nothing there)
            self._ensure_body()
        mode = self._table_context()
        if mode is not None and tag in TABLE_PARTS | {"table"}:
            self._end_in_table(tag, mode)
            return
        if tag in ("body", "html"):
            return
        if tag in BLOCK_END:
            if self._in_scope(tag):
                self._implied_end()
                self._pop_until(tag)
        elif tag == "form":
            node, self.form = self.form, None
            if node is not None and self._in_scope("form") is node:
                self._implied_end()
                self.stack.remove(node)
        elif tag == "p":
            if not self._in_scope("p", {"button"}):
                self._insert("p", {})
            self._implied_end("p")
            self._pop_until("p")
        elif tag == "li":
            if self._in_scope("li", {"ol", "ul"}):
                self._implied_end("li")
                self._pop_until("li")
        elif tag in ("dd", "dt"):
            if self._in_scope(tag):
                self._implied_end(tag)
                self._pop_until(tag)
        elif tag in HEADINGS:
            if self._in_scope(HEADINGS):
                self._implied_end()
                self._pop_until(HEADINGS)
        elif tag in FORMATTING or tag in ("applet", "marquee", "object"):
            node = self._formatting(tag) if tag in FORMATTING else self._in_scope(tag)
            if node is not None and self._in_scope(tag) is node:
                del self.stack[self.stack.index(node):]
        elif tag == "br":
            self._insert("br", {}, void=True, foster=self._foster())
        elif tag == "template":
            if any(n.is_("template") for n in self.stack):
                self._implied_end()
                self._pop_until("template")
        else:
            for i in range(len(self.stack) - 1, -1, -1):
                node = self.stack[i]
                if node.ns == HTML and node.tag == tag:
                    self._implied_end(tag)
                    del self.stack[i:]
                    return
                if self._special(node):
                    return

    def _end_in_table(self, tag: str, mode: str) -> None:
        if mode == "cell":
            if tag in ("td", "th"):
                if self._in_scope(tag, table=True):
                    self._implied_end()
                    self._pop_until(tag)
            elif tag in ("table", "tbody", "tfoot", "thead", "tr"):
                if self._in_scope(tag, table=True):
                    self._close_cell()
                    self._end(tag)
            return
        if mode == "caption":
            if tag == "caption" or tag == "table":
                if self._in_scope("caption", table=True):
                    self._pop_until("caption")
                    if tag == "table":
                        self._end(tag)
            return
        if tag == "tr":
            if self._in_scope("tr", table=True):
                self._clear_to({"tr", "template", "html"})
                self.stack.pop()
        elif tag in SECTIONS:
            if self._in_scope(tag, table=True):
                self._clear_to(SECTIONS | {"template", "html"})
                self.stack.pop()
        elif tag == "table":
            if self._in_scope("table", table=True):
                self._pop_until("table")


def parse(text: str) -> Builder:
    """The tree of a decoded document. The result has document, html, head and body."""
    builder = Builder()
    builder.feed(text.replace("\r\n", "\n").replace("\r", "\n"))
    builder.close()
    if builder.body is None:
        builder._ensure_body()
    return builder
