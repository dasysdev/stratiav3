"""JSON-LD blocks of a document: strict parsing, the syntax checks of the serialization level
(ws-serialization/001–018) and the entities of the graph.

The active context is what the expansion algorithm needs to recognise keyword aliases and to tell
which keys and types expand to an IRI: a local context (a map) is read; the Schema.org context,
referenced by its URL, is the frozen one of the release (schemaorgcontext.jsonld, with `id` and
`type` as aliases); any other remote context cannot be obtained, and what depends on it is NE
(`remote` in the report). Local contexts are processed in order; a null context resets.
"""
from __future__ import annotations

import functools
import json
import re
from dataclasses import dataclass, field
from urllib.parse import urljoin

from . import vocab
from .graph import Entity, Lit, Ref

KEYWORDS = {"@base", "@container", "@context", "@direction", "@graph", "@id", "@import", "@included", "@index",
            "@json", "@language", "@list", "@nest", "@none", "@prefix", "@propagate", "@protected", "@reverse",
            "@set", "@type", "@value", "@version", "@vocab"}
SCHEMA_CONTEXT = re.compile(r"^https?://schema\.org/?(docs/jsonldcontext\.json(ld)?)?$", re.I)
SCHEME = re.compile(r"^[A-Za-z][A-Za-z0-9+.\-]*:")
IRI_FORBIDDEN = re.compile(r"[\x00-\x20<>\"{}|\\^`\x7f]")
_ALNUM = "[A-Za-z0-9]"
BCP47 = re.compile(
    r"^(?:(?:[A-Za-z]{2,3}(?:-[A-Za-z]{3}){0,3}|[A-Za-z]{4}|[A-Za-z]{5,8})"  # language (extlang)
    r"(?:-[A-Za-z]{4})?"                                                    # script
    r"(?:-(?:[A-Za-z]{2}|[0-9]{3}))?"                                       # region
    rf"(?:-(?:{_ALNUM}{{5,8}}|[0-9]{_ALNUM}{{3}}))*"                         # variants
    rf"(?:-[0-9A-WY-Za-wy-z](?:-{_ALNUM}{{2,8}})+)*"                          # extensions
    rf"(?:-[xX](?:-{_ALNUM}{{1,8}})+)?"                                      # private use
    rf"|[xX](?:-{_ALNUM}{{1,8}})+"                                           # private use only
    r"|en-GB-oed|i-ami|i-bnn|i-default|i-enochian|i-hak|i-klingon|i-lux|i-mingo|i-navajo|i-pwn|i-tao"
    r"|i-tay|i-tsu|sgn-BE-FR|sgn-BE-NL|sgn-CH-DE|art-lojban|cel-gaulish|no-bok|no-nyn|zh-guoyu"
    r"|zh-hakka|zh-min|zh-min-nan|zh-xiang)$", re.I)


def is_iri_ref(value) -> bool:
    """Syntax of an IRI reference (RFC 3987): a string without spaces or characters it forbids."""
    return isinstance(value, str) and not IRI_FORBIDDEN.search(value)


def is_language(value) -> bool:
    return value is None or (isinstance(value, str) and bool(BCP47.match(value)))


# --- Strict JSON ----------------------------------------------------------------

class Duplicate:
    """A key repeated in the same object (json keeps only the last one)."""

    def __init__(self, pairs):
        self.pairs = pairs


def _pairs(pairs):
    keys = [k for k, _ in pairs]
    out = dict(pairs)
    repeated = sorted({k for k in keys if keys.count(k) > 1})
    if repeated:
        out["\x00duplicates"] = repeated
    return out


def _reject(name):
    raise ValueError(f"constante no admitida: {name}")


def parse(text: str):
    """(data, error): RFC 8259 strict, no comments, trailing commas, NaN or empty content.
    Repeated keys are kept under the key "\\x00duplicates" of their object."""
    if not text.strip():
        return None, "contenido vacío"
    try:
        return json.loads(text, object_pairs_hook=_pairs, parse_constant=_reject, strict=True), None
    except (ValueError, RecursionError) as e:
        return None, str(e)


def _clean(data):
    """The data without the duplicates markers."""
    if isinstance(data, dict):
        return {k: _clean(v) for k, v in data.items() if k != "\x00duplicates"}
    if isinstance(data, list):
        return [_clean(v) for v in data]
    return data


# --- Active context ---------------------------------------------------------------

@dataclass
class Context:
    vocab: str | None = None
    base: bool = False
    terms: dict = field(default_factory=dict)      # term → IRI or keyword
    coerce: dict = field(default_factory=dict)     # term → its @type (@id, @vocab…)
    remote: bool = False                           # a remote context we could not read

    def copy(self) -> "Context":
        return Context(self.vocab, self.base, dict(self.terms), dict(self.coerce), self.remote)

    def expand(self, key: str, vocab_relative: bool = True) -> str | None:
        """A key or a type: keyword, absolute IRI, or None when it does not expand."""
        if not isinstance(key, str):
            return None
        if key in KEYWORDS:
            return key
        if key in self.terms:
            return self.terms[key]
        if key.startswith("@"):
            return None  # looks like a keyword: ignored by the expansion
        if ":" in key:
            prefix, suffix = key.split(":", 1)
            if prefix == "_":
                return key
            if prefix in self.terms and not suffix.startswith("//"):
                target = self.terms[prefix]
                return target + suffix if isinstance(target, str) and not target.startswith("@") else None
            if SCHEME.match(key):
                return key
        if vocab_relative and self.vocab is not None:
            return self.vocab + key
        return None

    def keyword(self, key: str) -> str | None:
        expanded = self.expand(key)
        return expanded if expanded in KEYWORDS else None


@functools.cache
def _schema_context() -> Context:
    ctx = Context()
    raw = vocab.load().context
    ctx.vocab = raw.get("@vocab")
    for term, value in raw.items():
        if term.startswith("@"):
            continue
        if isinstance(value, str):
            ctx.terms[term] = value
        elif isinstance(value, dict) and isinstance(value.get("@id"), str):
            if value.get("@type"):
                ctx.coerce[term] = value["@type"]
    for term, value in list(ctx.terms.items()):
        if isinstance(value, str) and ":" in value and not value.startswith("@"):
            prefix, suffix = value.split(":", 1)
            if prefix in ctx.terms and not suffix.startswith("//"):
                ctx.terms[term] = ctx.terms[prefix] + suffix
    return ctx


def apply(ctx: Context, local) -> Context:
    """The active context after a local context (null, IRI, map or array of them)."""
    for item in (local if isinstance(local, list) else [local]):
        if item is None:
            ctx = Context()
        elif isinstance(item, str):
            if SCHEMA_CONTEXT.match(item.strip()):
                schema = _schema_context()
                merged = ctx.copy()
                merged.vocab = schema.vocab
                merged.terms.update(schema.terms)
                merged.coerce.update(schema.coerce)
                ctx = merged
            else:
                ctx = ctx.copy()
                ctx.remote = True
        elif isinstance(item, dict):
            ctx = ctx.copy()
            if "@vocab" in item:
                v = item["@vocab"]
                ctx.vocab = (ctx.expand(v, vocab_relative=False) or v) if isinstance(v, str) else None
            if "@base" in item:
                ctx.base = True
            for term, value in item.items():
                if term.startswith("@") or term == "\x00duplicates":
                    continue
                if isinstance(value, str):
                    ctx.terms[term] = ctx.expand(value, vocab_relative=False) or value
                elif isinstance(value, dict):
                    target = value.get("@id", term)
                    if isinstance(target, str):
                        ctx.terms[term] = ctx.expand(target) or target
                    if isinstance(value.get("@type"), str):
                        ctx.coerce[term] = value["@type"]
                elif value is None:
                    ctx.terms.pop(term, None)
    return ctx


# --- Syntax checks ------------------------------------------------------------------

@dataclass
class Block:
    index: int
    line: int
    text: str
    data: object = None
    error: str | None = None

    @property
    def ok(self) -> bool:
        return self.error is None

    def where(self, path: str = "") -> str:
        return f"bloque {self.index} (línea {self.line}){' ' + path if path else ''}"


@dataclass
class Report:
    """Findings of the syntax checks: for each check, the occurrences examined (`seen`, what its
    applicability counts) and the problems found, with their location."""
    blocks: list
    remote: list = field(default_factory=list)          # locations of unreadable remote contexts
    seen: dict = field(default_factory=dict)
    problems: dict = field(default_factory=dict)

    def note(self, check: str, problem: str | None = None) -> None:
        self.seen[check] = self.seen.get(check, 0) + 1
        if problem:
            self.problems.setdefault(check, []).append(problem)

    @property
    def invalid(self) -> list:
        return [b for b in self.blocks if not b.ok]

    @property
    def valid(self) -> list:
        return [b for b in self.blocks if b.ok]


def _is_graph_object(obj: dict, ctx: Context) -> bool:
    kws = {ctx.keyword(k) for k in obj if k != "\x00duplicates"}
    return "@graph" in kws and kws <= {"@graph", "@context", "@id", "@index"}


def _kind(obj: dict, ctx: Context) -> str:
    kws = {ctx.keyword(k) for k in obj if k != "\x00duplicates"}
    for kw, kind in (("@value", "value"), ("@list", "list"), ("@set", "set")):
        if kw in kws:
            return kind
    return "node"


def _check_context(value, report: Report, where: str) -> None:
    items = value if isinstance(value, list) else [value]
    report.note("context")
    bad = [i for i in items if not (i is None or isinstance(i, dict) or (isinstance(i, str) and is_iri_ref(i)))]
    if isinstance(value, list) and any(isinstance(i, list) for i in value):
        bad = bad or [value]
    if bad:
        report.problems.setdefault("context", []).append(f"{where}: @context {json.dumps(_clean(value))[:120]}")
    for item in items:
        if isinstance(item, dict):
            for term, definition in item.items():
                if isinstance(definition, dict) and "@context" in definition:
                    _check_context(definition["@context"], report, f"{where} > {term}")
            if "@language" in item:
                lang = item["@language"]
                report.note("context-language", None if is_language(lang) else f"{where}: @language {lang!r}")
        if isinstance(item, str) and not SCHEMA_CONTEXT.match(item.strip()):
            report.remote.append(f"{where}: {item}")


def _walk(value, ctx: Context, report: Report, where: str, block: Block, top: bool = False) -> None:
    if isinstance(value, list):
        for i, item in enumerate(value):
            _walk(item, ctx, report, f"{where}[{i}]", block, top)
        return
    if not isinstance(value, dict):
        return
    if value.get("\x00duplicates"):
        report.problems.setdefault("duplicates", []).append(f"{block.where(where)}: {', '.join(value['\x00duplicates'])}")
    if "@context" in value:
        _check_context(value["@context"], report, block.where(where))
        ctx = apply(ctx, _clean(value["@context"]))
    keys = {k: ctx.expand(k) for k in value if k not in ("\x00duplicates", "@context")}
    by_kw = {exp: k for k, exp in keys.items() if exp in KEYWORDS}
    kind = _kind(value, ctx)
    loc = block.where(where)
    if kind == "value":
        report.note("value")
        if "@type" in by_kw and ("@language" in by_kw or "@direction" in by_kw):
            report.problems.setdefault("value-type-language", []).append(loc)
        extra = [k for k, exp in keys.items() if exp is not None
                 and exp not in ("@value", "@type", "@language", "@direction", "@index", "@context")]
        if extra:
            report.problems.setdefault("value-keys", []).append(f"{loc}: {', '.join(extra)}")
        v = value[by_kw["@value"]]
        vtype = value.get(by_kw.get("@type", "\x01"))
        is_json = isinstance(vtype, str) and ctx.expand(vtype) == "@json"
        if isinstance(v, (list, dict)) and not is_json:
            report.problems.setdefault("value-value", []).append(loc)
        if "@type" in by_kw:
            t = value[by_kw["@type"]]
            ok = t is None or (isinstance(t, str) and (t == "@json" or ctx.expand(t) is not None))
            report.note("value-type", None if ok else f"{loc}: @type {json.dumps(_clean(t))[:80]}")
        if "@language" in by_kw:
            lang = value[by_kw["@language"]]
            report.note("value-language", None if is_language(lang) else f"{loc}: @language {lang!r}")
        return
    if kind in ("list", "set"):
        report.note(kind)
        allowed = {"@list", "@index"} if kind == "list" else {"@set", "@index"}
        extra = [k for k, exp in keys.items() if exp is not None and exp not in allowed and exp != "@context"]
        if extra:
            report.problems.setdefault(f"{kind}-keys", []).append(f"{loc}: {', '.join(extra)}")
        _walk(value[by_kw["@" + kind]], ctx, report, f"{where}.@{kind}", block)
        return
    # node object
    if top:
        meaningful = [k for k, exp in keys.items() if exp is not None]
        if not [k for k in meaningful if keys[k] != "@id"]:
            report.problems.setdefault("empty-top", []).append(loc)
        report.note("top")
    if "@id" in by_kw:
        v = value[by_kw["@id"]]
        report.note("id", None if is_iri_ref(v) else f"{loc}: @id {json.dumps(_clean(v))[:80]}")
        if isinstance(v, str) and not (SCHEME.match(v) or v.startswith("_:")):
            report.note("base", f"{loc}: @id {v!r}")
        else:
            report.note("base")
    if "@type" in by_kw:
        t = value[by_kw["@type"]]
        items = t if isinstance(t, list) else [t]
        ok = all(isinstance(i, str) and (i in ctx.terms or is_iri_ref(i)) for i in items)
        report.note("type", None if ok else f"{loc}: @type {json.dumps(_clean(t))[:80]}")
    if "@graph" in by_kw:
        g = value[by_kw["@graph"]]
        items = g if isinstance(g, list) else [g]
        ok = all(isinstance(i, dict) and _kind(i, ctx) == "node" and not _is_graph_object(i, ctx) for i in items) \
            and not (isinstance(g, list) and any(isinstance(i, list) for i in g))
        report.note("graph", None if ok else f"{loc}: @graph")
        _walk(g, ctx, report, f"{where}.@graph", block, top=top and where == "")
    for key, exp in keys.items():
        if exp is None or exp in KEYWORDS:
            continue
        v = value[key]
        if isinstance(v, list) and any(isinstance(i, list) for i in v):
            report.problems.setdefault("nested-array", []).append(f"{loc}: {key}")
        if ctx.coerce.get(key) == "@id":
            for i in (v if isinstance(v, list) else [v]):
                if isinstance(i, str):
                    ok = SCHEME.match(i) or i.startswith("_:")
                    report.note("base", None if ok else f"{loc}: {key} {i!r}")
        _walk(v, ctx, report, f"{where}.{key}" if where else key, block)


def analyze(blocks: list[Block]) -> Report:
    report = Report(blocks)
    for block in blocks:
        if not block.ok:
            continue
        data = block.data
        ctx = Context()
        has_base = '"@base"' in block.text  # a local context of the block fixes @base
        # the root
        if isinstance(data, dict):
            root_ctx = apply(ctx, _clean(data["@context"])) if "@context" in data else ctx
            kws = {root_ctx.keyword(k) for k in data if k != "\x00duplicates"}
            only_graph = kws <= {"@context", "@graph"} and kws & {"@context", "@graph"}
            ok = bool(only_graph) or _kind(data, root_ctx) == "node"
        elif isinstance(data, list):
            ok = all(isinstance(i, dict) and _kind(i, ctx) == "node" and not _is_graph_object(i, ctx) for i in data)
        else:
            ok = False
        report.note("root", None if ok else f"{block.where()}: raíz {type(data).__name__}")
        before = len(report.problems.get("base", []))
        _walk(data, ctx, report, "", block, top=True)
        if has_base and len(report.problems.get("base", [])) > before:
            del report.problems["base"][before:]
    return report


# --- Entities --------------------------------------------------------------------------

def entities(blocks: list[Block], page_url: str, page_id: str | None = None) -> list:
    """Every node of the valid blocks, nested ones included, as entities of the graph."""
    out: list = []

    def node(obj: dict, ctx: Context, where: str, top: bool):
        if "@context" in obj:
            ctx = apply(ctx, _clean(obj["@context"]))
        keys = {k: ctx.expand(k) for k in obj if k not in ("\x00duplicates", "@context")}
        by_kw = {exp: k for k, exp in keys.items() if exp in KEYWORDS}
        kind = _kind(obj, ctx)
        if kind == "value":
            v = obj[by_kw["@value"]]
            t = obj.get(by_kw.get("@type", "\x01"))
            return [Lit(v, "value-object", where, ctx.expand(t) if isinstance(t, str) else None)]
        if kind in ("list", "set"):
            items = obj[by_kw["@" + kind]]
            return [x for i, item in enumerate(items if isinstance(items, list) else [items])
                    for x in value(item, ctx, f"{where}[{i}]", None)]
        if _is_graph_object(obj, ctx) and not top:
            g = obj[by_kw["@graph"]]
            return [x for i, item in enumerate(g if isinstance(g, list) else [g])
                    for x in value(item, ctx, f"{where}.@graph[{i}]", None)]
        raw_id = obj.get(by_kw.get("@id", "\x01"))
        ident = None
        if isinstance(raw_id, str):
            ident = raw_id if raw_id.startswith("_:") else urljoin(page_url, raw_id.strip())
        raw_types = obj.get(by_kw.get("@type", "\x01"))
        types = []
        for t in (raw_types if isinstance(raw_types, list) else [raw_types] if raw_types is not None else []):
            if isinstance(t, str):
                exp = ctx.expand(t)
                types.append(vocab.short(exp) or exp or f"<{t}>" if exp else f"<{t}>")
        props = [(k, exp) for k, exp in keys.items() if exp is not None and exp not in KEYWORDS]
        if ident is not None and not types and not props and "@graph" not in by_kw:
            return [Ref(ident, where)]
        entity = Entity(types, "json-ld", where, ident, top, page=page_id)
        out.append(entity)
        for key, exp in props:
            prop = vocab.short(exp) or exp
            items = obj[key]
            for i, item in enumerate(items if isinstance(items, list) else [items]):
                for v in value(item, ctx, f"{where}.{key}" + (f"[{i}]" if isinstance(items, list) else ""), key):
                    entity.add(prop, v)
        if "@graph" in by_kw:
            g = obj[by_kw["@graph"]]
            for i, item in enumerate(g if isinstance(g, list) else [g]):
                for v in value(item, ctx, f"{where}.@graph[{i}]", None, top=True):
                    pass
        return [entity]

    def value(item, ctx: Context, where: str, key: str | None, top: bool = False):
        if isinstance(item, dict):
            return node(item, ctx, where, top)
        if isinstance(item, list):
            return [x for i, sub in enumerate(item) for x in value(sub, ctx, f"{where}[{i}]", key, top)]
        if item is None:
            return []
        if isinstance(item, bool):
            return [Lit(item, "json-boolean", where)]
        if isinstance(item, (int, float)):
            return [Lit(item, "json-number", where)]
        if key is not None and ctx.coerce.get(key) == "@id":
            return [Ref(item if item.startswith("_:") else urljoin(page_url, item), where)]
        return [Lit(item, "json-string", where)]

    for block in blocks:
        if not block.ok:
            continue
        data = _clean(block.data)
        ctx = Context()
        here = f"JSON-LD bloque {block.index} (línea {block.line})"
        if isinstance(data, dict) and not any(k for k in data if k not in ("@context", "@graph")) and "@graph" in data:
            ctx = apply(ctx, data.get("@context")) if "@context" in data else ctx
            g = data["@graph"]
            for i, item in enumerate(g if isinstance(g, list) else [g]):
                value(item, ctx, f"{here} @graph[{i}]", None, top=True)
        elif isinstance(data, list):
            for i, item in enumerate(data):
                value(item, ctx, f"{here} [{i}]", None, top=True)
        else:
            value(data, ctx, here, None, top=True)
    return out
