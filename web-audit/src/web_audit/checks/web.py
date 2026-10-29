"""Checks of Web (reference/requirements/web-*.json), with the method common to Web (reference/README.md).

The response is the one capture froze with audit-es (meta.json and the original bytes of the
body); the DOM after load is not used (D-156). robots.txt is that of the origin of the requested
URL; its status, the one capture recorded for the page. The sitemaps are those of the audit, in
any format, and a form requirement is satisfied only if every one was obtained and none fails.
"""
from __future__ import annotations

import codecs
import functools
import re
from urllib.parse import quote, unquote, urljoin, urlsplit, urlunsplit

from capture.robots import _normalize, matches, parse as parse_robots

from ..site import SITEMAP_NS
from . import NA, NE, PENDING, SAT, UNSAT, Case, Result, capped, check

GOOGLE_LIMIT = 500 * 1024
TEXT_TYPES = {"text/html", "application/xhtml+xml", "text/plain", "text/xml", "application/xml", "image/svg+xml",
              "text/csv", "application/vnd.google-earth.kml+xml", "application/vnd.google-earth.kmz",
              "application/gpx+xml", "application/x-tex", "text/x-tex", "text/vnd.wap.wml", "application/pdf",
              "application/postscript", "application/epub+zip", "application/x-hwp", "application/vnd.ms-excel",
              "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet", "application/vnd.ms-powerpoint",
              "application/vnd.openxmlformats-officedocument.presentationml.presentation", "application/msword",
              "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
              "application/vnd.oasis.opendocument.presentation", "application/vnd.oasis.opendocument.spreadsheet",
              "application/vnd.oasis.opendocument.text", "application/rtf", "text/rtf"}
NO_RESPONSE = "La ficha no tiene respuesta del recurso ({}): lo que depende de ella es NE (método común de Web, punto 1)."


# --- Common helpers -------------------------------------------------------------------------------

def no_response(case: Case) -> Result | None:
    page = case.page
    if page.meta is None or page.status is None:
        return Result(NE, {"outcome": page.outcome}, NO_RESPONSE.format(page.outcome))
    return None


def no_document(case: Case) -> Result | None:
    page = case.page
    if page.doc is None:
        return Result(NE, {"outcome": page.outcome, "estado": page.status},
                      f"No se dispone del documento de la respuesta (outcome {page.outcome}).")
    return None


def not_html(case: Case) -> Result | None:
    if not case.page.is_html:
        return Result(NA, {"Content-Type": case.page.headers.get("content-type")},
                      "El cuerpo de la respuesta no es un documento HTML.")
    return None


def not_200(case: Case) -> Result | None:
    if case.page.status != 200:
        return Result(NA, {"estado": case.page.status}, "La respuesta final no tiene el estado 200 (lo recoge w-consumer/002).")
    return None


def first(*guards):
    def run(case: Case) -> Result | None:
        for g in guards:
            r = g(case)
            if r is not None:
                return r
        return None
    return run


def normalize_url(url: str) -> str:
    """WHATWG-like normalization: scheme and host in lower case, default port removed, percent
    escapes normalized; the trailing slash and the query count."""
    parts = urlsplit(url.strip())
    host = (parts.hostname or "").lower()
    port = parts.port
    if port and not ((parts.scheme == "http" and port == 80) or (parts.scheme == "https" and port == 443)):
        host += f":{port}"
    path = quote(unquote(parts.path or "/"), safe="/:@!$&'()*+,;=-._~%")
    return urlunsplit((parts.scheme.lower(), host, path, parts.query, ""))


def same_url(a: str, b: str) -> bool:
    return normalize_url(a) == normalize_url(b)


# --- Sitemaps (w-protocol) ------------------------------------------------------------------------

def sitemap_form(test, describe: str):
    """A form requirement over each XML sitemap of the site (method common to Web, point 5)."""
    def run(case: Case) -> Result:
        site = case.site
        maps = [s for s in site.sitemaps if not s.missing]
        obtained = [s for s in maps if s.obtained]
        if not obtained and not [s for s in maps if not s.obtained] and not site.sitemaps_pending:
            return Result(NA, {"sitemaps": [s.url for s in site.sitemaps]}, "El sitio no publica ningún sitemap.")
        xml = [s for s in obtained if s.format == "xml"]
        bad, ok = [], []
        for s in xml:
            problems = test(s)
            (bad if problems else ok).append(f"{s.url}: {problems}" if problems else s.url)
        unobtained = [s.url for s in maps if not s.obtained] + site.sitemaps_pending
        ev = {"examinados": len(xml), "incumplen": capped(bad), "no obtenidos": capped(unobtained)}
        if bad:
            return Result(UNSAT, ev)
        if unobtained:
            return Result(NE, ev, "Algún sitemap del conjunto no se pudo obtener y ninguno de los obtenidos incumple "
                                  "(método común de Web, punto 5).")
        if not xml:
            return Result(NA, ev, "El sitio no publica ningún sitemap XML.")
        return Result(SAT, ev)
    return run


def _locs(s):
    return [(i, loc) for i, _, locs in s.summary["entries"] for loc in locs]


def _root(s):
    root, error = s.summary["root"], s.summary["parse_error"]
    if error:
        return f"no es XML bien formado ({error})"
    if root not in (f"{{{SITEMAP_NS}}}urlset", f"{{{SITEMAP_NS}}}sitemapindex"):
        return f"raíz {root}"
    return None


def _utf8(s):
    if s.summary["utf8_error"] is not None:
        return f"UTF-8 no válido en el byte {s.summary['utf8_error']}"
    declared = s.summary["declared_encoding"]
    try:
        if declared and codecs.lookup(declared).name != "utf-8":
            return f"declara {declared}"
    except LookupError:
        return f"declara {declared}"
    return None


def _locs_present(s):
    missing = [i for i, _, locs in s.summary["entries"] if not any(locs)]
    return f"{len(missing)} entradas sin loc (posiciones {missing[:5]})" if missing else None


def _absolute(s):
    bad = [loc for _, loc in _locs(s) if not re.match(r"^https?://[^/]+", loc)]
    return f"loc no absolutos: {bad[:3]}" if bad else None


def _short(s):
    bad = [len(loc) for _, loc in _locs(s) if len(loc) >= 2048]
    return f"loc de 2048 caracteres o más: {bad[:3]}" if bad else None


def _valid_location(case: Case):
    def test(s):
        if s.index:
            return None
        base = urlsplit(s.url)
        folder = base.path.rsplit("/", 1)[0] + "/"
        bad = []
        for _, loc in _locs(s):
            u = urlsplit(loc)
            if (u.scheme, u.netloc) == (base.scheme, base.netloc) and (u.path or "/").startswith(folder):
                continue
            if s.url not in case.site.declared_sitemaps(loc):
                bad.append(loc)
        return f"{len(bad)} URL fuera de su ubicación: {bad[:3]}" if bad else None
    return test


def _count(s):
    n = len(s.summary["entries"])
    return f"{n} entradas" if n > 50000 else None


def _size(s):
    n = s.summary["size"]
    return f"{n} bytes" if n > 52_428_800 else None


def _escaped(s):
    found = s.summary["unescaped"]
    return f"caracteres sin escapar (posiciones {found[:5]})" if found else None


check("w-protocol/004")(sitemap_form(_root, "raíz urlset o sitemapindex"))
check("w-protocol/005")(sitemap_form(_utf8, "UTF-8"))
check("w-protocol/006")(sitemap_form(_locs_present, "loc"))
check("w-protocol/007")(sitemap_form(_absolute, "URL absolutas"))
check("w-protocol/008")(sitemap_form(_short, "menos de 2048 caracteres"))


@check("w-protocol/009")
def _location(case: Case) -> Result:
    return sitemap_form(_valid_location(case), "URL de su ubicación")(case)


check("w-protocol/010")(sitemap_form(_count, "50.000 entradas como mucho"))
check("w-protocol/011")(sitemap_form(_size, "50 MB como mucho"))
check("w-protocol/012")(sitemap_form(_escaped, "sin & ni < sin escapar"))


# --- Document (w-document) --------------------------------------------------------------------------

@functools.cache
def encoding_labels() -> frozenset:
    from references.read import section_text
    text = section_text("whatwg-encoding", "document", "#names-and-labels")
    return frozenset(re.findall(r'"([^"\s]+)"', "\n".join(x for x in text.splitlines() if x.startswith("|"))))


def charset_param(content_type: str | None) -> str | None:
    if not content_type:
        return None
    m = re.search(r";\s*charset\s*=\s*(\"?)([^\";]*)\1", content_type, re.I)
    return m.group(2).strip() if m else None


def meta_declarations(doc) -> list:
    out = []
    for el in doc.all("meta"):
        if el.has("charset"):
            out.append(f"meta charset={el.get('charset')!r} ({el.where()})")
        elif el.get("http-equiv", "").strip().lower() == "content-type":
            out.append(f"meta http-equiv content={el.get('content')!r} ({el.where()})")
    return out


@check("w-document/001")
def _declares_encoding(case: Case) -> Result:
    r = first(no_response, no_document, not_html)(case)
    if r:
        return r
    page = case.page
    ctype = page.headers.get("content-type")
    param = charset_param(ctype)
    by_header = param is not None and param.lower() in encoding_labels()
    metas = meta_declarations(page.doc)
    ev = {"Content-Type": ctype, "meta": metas}
    if page.original_bytes and page.raw is not None:
        ev["primeros bytes"] = page.raw[:3].hex(" ")
        bom = page.raw.startswith((b"\xef\xbb\xbf", b"\xfe\xff", b"\xff\xfe"))
    else:
        bom = False
        if not (by_header or metas):
            return Result(NE, ev, "Falta comprobar el BOM: la ficha no conserva los bytes originales del cuerpo.")
    return Result(SAT if by_header or metas or bom else UNSAT, ev)


@check("w-document/004")
def _utf8_document(case: Case) -> Result:
    r = first(no_response, no_document, not_html)(case)
    if r:
        return r
    page = case.page
    if not page.original_bytes or page.raw is None:
        return Result(NE, None, "La ficha no conserva los bytes originales del cuerpo.")
    raw = page.raw
    bom = raw.startswith(b"\xef\xbb\xbf")
    try:
        raw[3 if bom else 0:].decode("utf-8", errors="strict")
        return Result(SAT, {"BOM": bom})
    except UnicodeDecodeError as e:
        return Result(UNSAT, {"BOM": bom, "posición": e.start, "bytes": raw[e.start:e.start + 4].hex(" ")})


def titles(doc) -> list:
    return [el for el in doc.all("title") if not el.in_("svg")]


@check("w-document/008")
def _title(case: Case) -> Result:
    r = first(no_response, no_document, not_html)(case)
    if r:
        return r
    found = titles(case.page.doc)
    ev = [f"{el.text()!r} ({'head' if el.in_('head') else 'fuera de head'}, línea {el.line})" for el in found] or "ninguno"
    return Result(SAT if any(el.text().strip(" \t\n\f\r") for el in found) else UNSAT, {"title": ev})


@check("w-document/009")
def _one_title(case: Case) -> Result:
    r = first(no_response, no_document, not_html)(case)
    if r:
        return r
    found = titles(case.page.doc)
    return Result(SAT if len(found) <= 1 else UNSAT, {"número": len(found), "title": [el.text() for el in found]})


def og(doc) -> tuple[list, list]:
    """(Open Graph properties, metas that use name instead of property): (name, content, element)."""
    props, by_name = [], []
    for el in doc.all("meta"):
        prop = el.get("property", "")
        if prop.lower().startswith("og:"):
            props.append((prop.lower(), el.get("content"), el))
        elif el.get("name", "").lower().startswith("og:"):
            by_name.append((el.get("name").lower(), el.get("content"), el))
    return props, by_name


def _og_guard(case: Case) -> Result | None:
    r = first(no_response, no_document, not_html)(case)
    if r:
        return r
    if not og(case.page.doc)[0]:
        return Result(NA, None, "El documento no tiene propiedades Open Graph (meta property=\"og:…\").")
    return None


def _og_has(name: str, test=lambda c: bool(c and c.strip())):
    def run(case: Case) -> Result:
        r = _og_guard(case)
        if r:
            return r
        props, by_name = og(case.page.doc)
        mine = [(c, el) for n, c, el in props if n == name]
        ev = {name: [f"{c!r} ({'head' if el.in_('head') else 'fuera de head'})" for c, el in mine] or "ausente"}
        named = [c for n, c, _ in by_name if n == name]
        if named:
            ev["con name en lugar de property"] = named
        return Result(SAT if any(test(c) for c, _ in mine) else UNSAT, ev)
    return run


def http_url(value) -> bool:
    if not value:
        return False
    parts = urlsplit(value.strip())
    return parts.scheme in ("http", "https") and bool(parts.netloc)


check("w-document/010")(_og_has("og:title"))
check("w-document/011")(_og_has("og:type"))
check("w-document/012")(_og_has("og:image", http_url))
check("w-document/013")(_og_has("og:url", http_url))


def link_header_canonicals(page) -> list[str]:
    value = page.headers.get("link") or ""
    out = []
    for part in re.split(r",\s*(?=<)", value):
        m = re.match(r"\s*<([^>]*)>(.*)", part)
        if m and re.search(r"rel\s*=\s*\"?[^\";]*\bcanonical\b", m.group(2), re.I):
            out.append(m.group(1))
    return out


def canonical_links(doc, in_head: bool = True) -> list:
    return [el for el in doc.all("link") if "canonical" in el.get("rel", "").lower().split()
            and el.get("href", "").strip() and el.in_("head") == in_head]


def canonicals(page) -> list[tuple[str, str]]:
    """(URL resolved against the final URL, origin) of each canonical the page declares in a
    link of head or in the Link header."""
    out = []
    if page.doc is not None:
        out += [(urljoin(page.url_final, el.get("href").strip()), "elemento") for el in canonical_links(page.doc)]
    out += [(urljoin(page.url_final, u), "cabecera") for u in link_header_canonicals(page)]
    return out


@check("w-document/014")
def _og_url_is_canonical(case: Case) -> Result:
    r = _og_guard(case)
    if r:
        return r
    page = case.page
    urls = [c.strip() for n, c, _ in og(page.doc)[0] if n == "og:url" and c and c.strip()]
    element = canonical_links(page.doc)
    canon = [(urljoin(page.url_final, el.get("href").strip()), "elemento") for el in element] or \
            [(urljoin(page.url_final, u), "cabecera") for u in link_header_canonicals(page)]
    if not urls or not canon:
        return Result(NA, {"og:url": urls, "canónica": canon}, "El documento no tiene og:url o la página no declara URL canónica.")
    og_norm = {normalize_url(urljoin(page.url_final, u)) for u in urls}
    can_norm = {normalize_url(u) for u, _ in canon}
    ev = {"og:url": urls, "canónica": canon, "normalizadas": sorted(og_norm | can_norm)}
    return Result(SAT if len(og_norm) == 1 and og_norm == can_norm else UNSAT, ev)


# --- Consumer (w-consumer) ----------------------------------------------------------------------------

@check("w-consumer/001")
def _no_login(case: Case) -> Result:
    page = case.page
    if page.status == 401:
        return Result(UNSAT, {"estado": 401, "URL final": page.url_final})
    if page.outcome == "blocked" or page.status in (403, 429):
        return Result(NE, {"outcome": page.outcome, "estado": page.status},
                      "Un desafío o un bloqueo a nuestro navegador no es exigir iniciar sesión (método común de Web, punto 1).")
    if page.status != 200:
        return Result(NE, {"estado": page.status}, "La respuesta final no es 200 ni 401: capture no guarda su documento.")
    r = no_document(case)
    if r:
        return r
    passwords = [el for el in page.doc.all("input") if el.get("type", "").lower() == "password"]
    hops = [h.get("to") for h in (page.meta or {}).get("redirects") or []]
    ev = {"estado": 200, "URL final": page.url_final, "redirecciones": hops,
          "title": [el.text().strip() for el in titles(page.doc)][:1],
          "campos de contraseña": [el.where() for el in passwords]}
    if not passwords:
        return Result(SAT, ev)
    return Result(PENDING, ev, "El documento tiene un campo de contraseña. ¿Es una página de inicio de sesión servida en "
                               "lugar de la página pedida (su contenido principal es el formulario y, fuera de él y de las "
                               "partes comunes del sitio, no tiene contenido propio de la página pedida)? Si lo es, no "
                               "satisfecho; si el formulario está en el menú, la cabecera o una ventana, satisfecho.")


@check("w-consumer/002")
def _status_200(case: Case) -> Result:
    page = case.page
    hops = (page.meta or {}).get("redirects") or []
    ev = {"estado": page.status, "outcome": page.outcome, "URL pedida": page.url, "URL final": page.url_final,
          "redirecciones": [f"{h.get('url')} → {h.get('status')} → {h.get('to')}" for h in hops]}
    if page.outcome == "blocked" or page.status in (403, 429):
        return Result(NE, ev, "La respuesta es un desafío, un 403 o un 429: puede ser un bloqueo a nuestro navegador, "
                              "que no es Googlebot (D-157).")
    if page.status is None:
        return Result(NE, ev, NO_RESPONSE.format(page.outcome))
    if len(hops) > 10:
        return Result(UNSAT, ev, None)
    return Result(SAT if page.status == 200 else UNSAT, ev)


# What an error page says in its title or main heading (Spanish, Catalan, English)
ERROR_SIGNAL = re.compile(r"\b(404|410|500|error|not found|no encontrad[ao]|no se (ha )?encontr|no existe|no disponible|"
                          r"page not found|pàgina no trobada|no trobada|ups|oops|vaya|lo sentimos|retirad[ao])\b", re.I)


@check("w-consumer/003")
def _not_error_page(case: Case) -> Result:
    r = first(no_response, not_200, no_document)(case)
    if r:
        return r
    doc = case.page.doc
    h1 = [el.text().strip() for el in doc.all("h1")][:2]
    title = [el.text().strip() for el in titles(doc)][:1]
    body = doc.body()
    sample = doc.visible_text(body)[:400] if body is not None else ""
    ev = {"URL final": case.page.url_final, "title": title, "h1": h1, "texto": sample}
    signals = [t for t in title + h1 if ERROR_SIGNAL.search(t)]
    if not signals:
        ev["indicio de error"] = "ninguno en el título ni en el encabezado principal"
        return Result(SAT, ev)
    ev["indicio de error"] = signals
    return Result(PENDING, ev,
                  "¿Es el documento un mensaje de error en lugar de la página pedida (soft 404: dice que la página o el "
                  "producto no existe, no se encuentra, se ha retirado o que hubo un error, y no tiene contenido propio "
                  "de la página pedida)? Si lo es, no satisfecho; si no, satisfecho. Agotado o descatalogado con su "
                  "contenido no es una página de error.")


@check("w-consumer/004")
def _indexable_type(case: Case) -> Result:
    r = first(no_response, not_200)(case)
    if r:
        return r
    ctype = case.page.headers.get("content-type")
    if not ctype:
        return Result(NE, {"Content-Type": None}, "La respuesta no tiene Content-Type.")
    mime = ctype.split(";")[0].strip().lower()
    if mime in TEXT_TYPES:
        return Result(SAT, {"Content-Type": ctype})
    if mime == "application/octet-stream" and case.page.doc is not None and case.page.doc.all("html"):
        return Result(NE, {"Content-Type": ctype}, "El tipo declarado no es el del contenido (un documento HTML).")
    return Result(UNSAT, {"Content-Type": ctype})


LOADING = re.compile(r"^(cargando|loading|please enable javascript|activa javascript|enable javascript|javascript is required|"
                     r"necesitas javascript|debes activar javascript)[\s.…!]*$", re.I)


@check("w-consumer/005")
def _has_text(case: Case) -> Result:
    r = first(no_response, not_200, no_document)(case)
    if r:
        return r
    body = case.page.doc.body()
    text = case.page.doc.visible_text(body) if body is not None else ""
    ev = {"caracteres": len(text), "fragmento": text[:200]}
    return Result(SAT if text and not LOADING.match(text) else UNSAT, ev)


@check("w-consumer/006")
def _has_markup(case: Case) -> Result:
    r = first(no_response, not_200, no_document)(case)
    if r:
        return r
    found = case.page.syntaxes
    return Result(SAT if found else UNSAT, found or {"marcado": "ninguno"})


# --- robots.txt ---------------------------------------------------------------------------------

def _groups(text: str, token: str, google: bool):
    groups, _ = parse_robots(text)
    token = token.lower()
    if google:
        own = [g for g in groups if any(a.rstrip("*") == token for a in g.agents)]
    else:
        own = [g for g in groups if token in g.agents]
    if own:
        return own, token
    star = [g for g in groups if "*" in g.agents]
    return star, ("*" if star else None)


def _decide(groups, url: str):
    parts = urlsplit(url)
    path = (parts.path or "/") + (f"?{parts.query}" if parts.query else "")
    if parts.path == "/robots.txt":
        return True, "/robots.txt siempre está permitido"
    best_len, best = -1, (True, "ninguna regla casa")
    for g in groups:
        for allow, pattern in g.rules:
            if matches(pattern, path):
                length = len(_normalize(pattern))
                if length > best_len or (length == best_len and allow):
                    best_len, best = length, (allow, f"{'allow' if allow else 'disallow'}: {pattern}")
    return best


def robots_case(case: Case, token: str, reader: str = "rfc") -> Result:
    """Whether robots.txt lets `token` crawl the page: the requested URL and, if the snapshot has
    the response, each URL of the redirect chain and the final one in the same origin.

    reader: google (w-consumer/009: Google's reading, 5xx/429 is NE), rfc (RFC 9309: 429 is
    unavailable, 5xx disallows everything) or consumer (ws-consumer/179: Googlebot or *, NE if the
    file cannot be obtained, other than a 404)."""
    page = case.page
    status, text, origin = case.site.robots(page.url)
    if page.meta and ((page.meta.get("legitimacy") or {}).get("robots") or {}).get("status") is not None:
        status = page.meta["legitimacy"]["robots"]["status"]
    urls = [page.url] + [h.get("to") for h in (page.meta or {}).get("redirects") or [] if h.get("to")]
    if page.meta and page.meta.get("url_final"):
        urls.append(page.meta["url_final"])
    same = list(dict.fromkeys(u for u in urls if urlsplit(u)._replace(path="", query="", fragment="").geturl().rstrip("/")
                              == origin.rstrip("/")))
    other = [u for u in dict.fromkeys(urls) if u not in same]
    ev = {"robots.txt": f"{origin}/robots.txt", "estado": status, "otro origen (no se examina)": other}
    if status is None and text is None:
        return Result(NE, ev, "La auditoría no conserva el robots.txt del origen ni su estado.")
    google = reader in ("google", "consumer")
    if status is None or status >= 500 or (status == 429 and google):
        if reader == "rfc":
            return Result(UNSAT, ev, None)
        return Result(NE, ev, "El robots.txt responde 5xx o 429, o no responde: Google aplica la última versión buena "
                              "del fichero, que no se conoce.")
    if 400 <= status < 500:
        ev["lectura"] = "sin restricciones (4xx)"
        return Result(SAT, ev)
    body = (text or "")
    if google:
        body = body.encode("utf-8")[:GOOGLE_LIMIT].decode("utf-8", errors="ignore")
    groups, chosen = _groups(body, token, google)
    ev["grupo"] = chosen or "ninguno"
    decisions = {u: _decide(groups, u) for u in same}
    ev["URL"] = {u: rule for u, (_, rule) in decisions.items()}
    return Result(UNSAT if any(not ok for ok, _ in decisions.values()) else SAT, ev)


@check("w-consumer/009")
def _robots_google(case: Case) -> Result:
    return robots_case(case, "googlebot", "google")


@check("w-consumer/011")
def _robots_openai(case: Case) -> Result:
    return robots_case(case, "OAI-SearchBot", "rfc")


@check("w-consumer/012")
def _robots_perplexity(case: Case) -> Result:
    return robots_case(case, "PerplexityBot", "rfc")


def noindex_rules(page, include_outside_head: bool = False) -> dict:
    """noindex or none rules for Googlebot: meta robots/googlebot of the head and X-Robots-Tag."""
    found, metas, outside = [], [], []
    if page.doc is not None:
        for el in page.doc.all("meta"):
            if el.get("name", "").strip().lower() in ("robots", "googlebot"):
                values = [v.strip().lower() for v in el.get("content", "").split(",")]
                entry = f"{el.get('name')}={el.get('content')!r} ({el.where()})"
                if el.in_("head") or include_outside_head:
                    metas.append(entry)
                    if {"noindex", "none"} & set(values):
                        found.append(entry)
                elif {"noindex", "none"} & set(values):
                    outside.append(entry)
    header = page.headers.get("x-robots-tag")
    tags = []
    for line in (header or "").split("\n"):
        agent = None
        m = re.match(r"\s*([A-Za-z][\w-]*)\s*:\s*(.*)", line)
        if m and m.group(1).lower() not in ("unavailable_after", "max-snippet", "max-image-preview", "max-video-preview",
                                             "noindex", "none", "nofollow"):
            agent, line = m.group(1).lower(), m.group(2)
        for rule in line.split(","):
            rule = rule.strip().lower()
            if rule:
                tags.append(f"{agent + ': ' if agent else ''}{rule}")
                if rule in ("noindex", "none") and agent in (None, "googlebot"):
                    found.append(f"X-Robots-Tag {agent + ': ' if agent else ''}{rule}")
    return {"meta": metas, "X-Robots-Tag": tags, "noindex": found, "fuera de head": outside}


@check("w-consumer/010")
def _no_noindex(case: Case) -> Result:
    r = first(no_response, not_200)(case)
    if r:
        return r
    rules = noindex_rules(case.page)
    if rules["noindex"]:
        return Result(UNSAT, rules)
    if rules["fuera de head"]:
        return Result(NE, rules, "Una meta robots o googlebot con noindex o none está fuera del head, y ninguna aplicable "
                                 "en el head ni en la cabecera: la fuente no dice si Google la aplica.")
    return Result(SAT, rules)


@check("w-consumer/013")
def _sitemap_lines(case: Case) -> Result:
    status, text, origin = case.site.robots(case.site.url)
    if status is None and text is None:
        return Result(NE, None, "La auditoría no conserva el robots.txt del sitio ni su estado.")
    if not (status and 200 <= status < 300):
        return Result(NA, {"estado": status}, "El robots.txt del sitio no responde 2xx.")
    lines = [line.split(":", 1)[1].strip() for line in (text or "").splitlines()
             if line.split("#", 1)[0].strip().lower().startswith("sitemap:")]
    if not lines:
        return Result(NA, {"estado": status}, "El robots.txt no tiene líneas sitemap.")
    bad = [u for u in lines if not re.match(r"^[A-Za-z][A-Za-z0-9+.-]*://[^/\s]+", u)]
    return Result(UNSAT if bad else SAT, {"sitemap": lines, "no absolutas": bad})


def sitemap_urls(site) -> dict[str, str]:
    """Normalized URL → the sitemap that lists it, of the valid URLs of the site's sitemaps."""
    if "sitemap_urls" in site.memo:
        return site.memo["sitemap_urls"]
    out = site.memo["sitemap_urls"] = {}
    for s in site.sitemaps:
        if not s.obtained or s.index:
            continue
        base = urlsplit(s.url)
        for loc in s.urls():
            u = urlsplit(loc)
            # Google's reading (method common to Web, point 5): a submitted sitemap is valid for its
            # whole host, in any directory; another host, if its robots.txt declares the sitemap.
            valid = (u.scheme, u.netloc) == (base.scheme, base.netloc) or s.url in site.declared_sitemaps(loc)
            if valid:
                out.setdefault(normalize_url(loc), s.url)
            else:
                site.memo.setdefault("sitemap_invalid", {}).setdefault(normalize_url(loc), s.url)
    return out


@check("w-consumer/014")
def _in_sitemap(case: Case) -> Result:
    page, site = case.page, case.site
    urls = sitemap_urls(site)
    final = page.url_final
    ev = {"sitemaps": [f"{s.url} ({s.status})" for s in site.sitemaps], "URL pedida": page.url, "URL final": final,
          "URL en los sitemaps": len(urls)}
    found = urls.get(normalize_url(final))
    if found:
        ev["sitemap"] = found
        return Result(SAT, ev)
    if urls.get(normalize_url(page.url)):
        ev["está la URL pedida"] = urls[normalize_url(page.url)]
    outside = site.memo.get("sitemap_invalid", {}).get(normalize_url(final))
    if outside:
        ev["aparece en un sitemap de otro host que no lo declara su robots.txt"] = outside
    if not site.sitemaps_complete:
        ev["no obtenidos"] = [s.url for s in site.sitemaps if not (s.obtained or s.missing)] + site.sitemaps_pending
        return Result(NE, ev, "Algún sitemap del conjunto no se pudo obtener y la URL no está en los obtenidos.")
    return Result(UNSAT, ev)


@check("w-consumer/015")
def _declares_canonical(case: Case) -> Result:
    r = first(no_response, no_document, not_html)(case)
    if r:
        return r
    page = case.page
    head = canonical_links(page.doc)
    body = canonical_links(page.doc, in_head=False)
    header = link_header_canonicals(page)
    ev = {"elemento": [el.get("href") for el in head], "fuera de head (no cuenta)": [el.get("href") for el in body],
          "cabecera Link": page.headers.get("link") if header else None}
    return Result(SAT if head or header else UNSAT, ev)


@check("w-consumer/016")
def _canonical_absolute(case: Case) -> Result:
    r = first(no_response, no_document)(case)
    if r:
        return r
    links = canonical_links(case.page.doc)
    if not links:
        return Result(NA, None, "El documento no tiene ningún link rel=canonical en head.")
    bad = [el.get("href") for el in links if not re.match(r"^https?://", el.get("href").strip(" \t\n\f\r"), re.I)]
    return Result(UNSAT if bad else SAT, {"href": [el.get("href") for el in links], "no absolutos": bad})


@check("w-consumer/017")
def _canonical_one_place(case: Case) -> Result:
    r = first(no_response, no_document)(case)
    if r:
        return r
    head = canonical_links(case.page.doc)
    header = link_header_canonicals(case.page)
    if not head and not header:
        return Result(NA, None, "La página no declara URL canónica (w-consumer/015 no satisfecho).")
    ev = {"elemento": [el.get("href") for el in head], "cabecera": header}
    return Result(UNSAT if head and header else SAT, ev)
