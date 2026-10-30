"""The filter Alfa (alfa/1, docs/20-methods/audit-gsc/filter-alfa.md): what goes in and what does
not (the canary page of T-101), the structure of the text, each annotation, the parser, the
encoding and the page of capture."""
import gzip
import hashlib
import json
import re

import pytest

from info_audit import alfa
from info_audit.encoding import decode, sniff

CANARIES = alfa.REPO / "research_notes/text-reading-canaries"
URL = "https://tienda.test/p/edredon-1"

# The codes of the canary page by rule of the specification (Entra / No entra)
IN = {
    "1 <title>": ["QX01-PIZARRA"],
    "2 nodos de texto del <body>": [
        "QX05-GALERNA", "QX06-SABINA", "QX07-GRANITO", "QX08-ARCILLA", "QX09-ISTMO", "QX10-BADANA",
        "QX11-ESCARCHA", "QX17-DOLMEN", "QX18-CIERZO", "QX19-HELECHO", "QX20-MIMBRE", "QX21-CERCETA",
        "QX22-HORNACINA", "QX23-JABEGA", "QX24-FRAGUA", "QX25-DORNILLO", "QX26-RAMBLA", "QX27-SALOBRE",
        "QX28-NACAR", "QX35-ACEBO", "QX47-TAHONA", "QX51-VAGUADA", "QX53-FANAL", "QX54-SALINA",
        "QX55-HUSILLO", "QX56-PALOMAR", "QX57-PEDERNAL", "QX58-RIBERA"],
    "3 <noscript>": ["QX29-ZARZO"],
    "4 formularios": ["QX38-VENCEJO", "QX40-ALMENA", "QX45-MARJAL", "QX46-RETAMA"],
    "5 <svg>": ["QX50-TOMILLO"],
    "6 alt de <img>": ["QX33-NORIA"],
}
OUT = {
    "1 resto de <head>": ["QX02-ULMO", "QX03-TOJAL", "QX04-BERILO"],
    "2 <script> y <style>": ["QX14-VILANO", "QX15-LABRADOR", "QX16-ENEBRO"],
    "3 <template>": ["QX30-CARRASCA"],
    "4 comentarios": ["QX31-ERIAL"],
    "5 atributos": ["QX12-GAZAPO", "QX13-QUEJIGO", "QX32-GAVIOTA", "QX34-LENTISCO", "QX36-URDIMBRE",
                    "QX37-CANTIL", "QX39-NEBLINA", "QX41-ALCOR", "QX42-ZAFRA", "QX43-CORNISA", "QX44-FALUCHO",
                    "QX48-FOGARIL"],
    "6 <iframe>, <object>, <embed>": ["QX49-BOTIJO"],
    "7 contenido generado por CSS": ["QX52-JUNCO"],
}
CODE = re.compile(r"Q[XTC]\d\d-[A-ZÁÉÍÓÚÑ]+")


def run(html, url=URL, content_type="text/html; charset=utf-8"):
    raw = html.encode("utf-8") if isinstance(html, str) else html
    return alfa.run(raw, ficha="t-1", url=url, content_type=content_type)


def text(html, **kw):
    return run(html, **kw)["text"]


def frag(rep, start):
    """The one fragment whose text starts with `start`."""
    found = [f for f in rep["fragments"] if f["text"].startswith(start)]
    assert len(found) == 1, (start, found)
    return found[0]


def spans_ok(rep):
    t, last = rep["text"], 0
    for f in rep["fragments"]:
        assert t[f["start"]:f["end"]] == f["text"]
        assert last <= f["start"] < f["end"]
        last = f["end"]


# --- Entra / No entra: the canary page -------------------------------------------------------------

@pytest.fixture(scope="module")
def canaries():
    return alfa.run((CANARIES / "site/index.html").read_bytes(), ficha="canaries", url="https://canarios.test/")


def test_canaries_are_all_classified():
    codes = {c["token"] for c in json.loads((CANARIES / "canaries.json").read_text(encoding="utf-8"))["constructs"]}
    ins = [c for v in IN.values() for c in v]
    outs = [c for v in OUT.values() for c in v]
    assert len(ins) + len(outs) == len(set(ins) | set(outs)) == len(codes)
    assert set(ins) | set(outs) == codes


def test_canaries_exactly_the_codes_of_entra(canaries):
    content = canaries["title"] + "\n" + canaries["text"]
    assert set(CODE.findall(content)) == {c for v in IN.values() for c in v}
    for rule, codes in OUT.items():
        assert not [c for c in codes if c in content], rule
    assert not [c for f in canaries["fragments"] for c in CODE.findall(f["text"]) if c not in content]


def test_canaries_title_and_format(canaries):
    assert canaries["filter"] == "alfa" and canaries["version"] == 1 and canaries["ficha"] == "canaries"
    assert canaries["title"] == "Edredón de prueba Canario · QX01-PIZARRA"
    assert "QX01-PIZARRA" not in canaries["text"]
    assert canaries["source"]["encoding"] == "UTF-8" and canaries["source"]["encoding_from"] == "meta"
    spans_ok(canaries)
    # The URL of a link is the annotation enlace, not content
    assert frag(canaries, "Ver referencia")["enlace"] == "https://canarios.test/ref/QX48-FOGARIL"


# --- Structure -------------------------------------------------------------------------------------

def test_blocks_start_a_line_and_inline_runs_on():
    assert text("<div>uno</div>dos<span>tres</span><span>cuatro</span><p>cinco</p>") == "uno\ndostrescuatro\ncinco"


def test_headings_carry_their_level():
    assert text("<h1>Edredón</h1><h3>Composición</h3><h6>Nota</h6>") == "# Edredón\n### Composición\n###### Nota"


def test_list_items_one_line_each():
    assert text("<ul><li>Reversible</li><li>Lavable <b>a 30º</b></li></ul>Fin") == "- Reversible\n- Lavable a 30º\nFin"


def test_table_rows_one_line_cells_joined():
    html = ("<table><tr><th>Composición</th><td>100% poliéster</td></tr>"
            "<tr><td><p>Medida</p></td><td><p>150 cm</p></td></tr><tr><td>A</td><td></td><td>C</td></tr></table>")
    assert text(html) == "Composición | 100% poliéster\nMedida | 150 cm\nA | | C"


def test_pre_keeps_spaces_and_the_rest_collapses():
    assert text("<p>  muchos \n\t espacios  </p><pre>\n a  b\n  c</pre>") == "muchos espacios\n a  b\n  c"


def test_br_starts_a_line():
    assert text("<p>Envío<br>gratis<br><br>desde 49 €</p>") == "Envío\ngratis\ndesde 49 €"


def test_spaces_between_inline_elements():
    rep = run("<p>Precio: <b>64,49 €</b> <i>IVA incl.</i></p>")
    assert rep["text"] == "Precio: 64,49 € IVA incl."
    assert frag(rep, "64,49")["start"] == len("Precio: ")
    spans_ok(rep)


# --- Annotations -----------------------------------------------------------------------------------

def test_posicion_is_the_span_in_text():
    rep = run("<h1>Edredón</h1><p>Uno <a href='/x'>dos</a> tres</p><ul><li>cuatro</li></ul>"
              "<table><tr><td>a</td><td>b</td></tr></table><img alt='foto'>")
    spans_ok(rep)
    assert [f["text"] for f in rep["fragments"]] == ["Edredón", "Uno", "dos", "tres", "cuatro", "a", "b", "foto"]


def test_ruta_is_the_path_of_the_element():
    rep = run("<div><p>a</p><p>b <b>c</b></p></div><p>d</p><svg><text>e</text></svg>")
    assert frag(rep, "a")["ruta"] == "/html/body/div/p[1]"
    assert frag(rep, "b")["ruta"] == "/html/body/div/p[2]"
    assert frag(rep, "c")["ruta"] == "/html/body/div/p[2]/b"
    assert frag(rep, "d")["ruta"] == "/html/body/p"
    assert frag(rep, "e")["ruta"] == "/html/body/svg/text"


@pytest.mark.parametrize("html,reasons", [
    ("<div hidden><p>x</p></div>", ["hidden"]),
    ("<div hidden='until-found'>x</div>", ["hidden"]),
    ("<div aria-hidden='true'>x</div>", ["aria-hidden"]),
    ("<div aria-hidden=' TRUE '>x</div>", ["aria-hidden"]),
    ("<aside role='dialog' aria-hidden='true' inert><p>x</p></aside>", ["aria-hidden", "inert"]),
    ("<div style='color:red; display: none !important'>x</div>", ["display:none"]),
    ("<div style='visibility:hidden'><span>x</span></div>", ["visibility:hidden"]),
    ("<dialog><p>x</p></dialog>", ["dialog"]),
    ("<details><summary>Cuidados</summary><p>x</p></details>", ["details"]),
    ("<details><summary>Cuidados</summary>x suelto</details>", ["details"]),
    ("<div hidden><dialog>x</dialog></div>", ["hidden", "dialog"]),
])
def test_oculto(html, reasons):
    assert frag(run(html), "x")["oculto"] == reasons


@pytest.mark.parametrize("html", [
    "<style>.oculto{display:none}</style><div class='oculto'>x</div>",   # CSS of a sheet is not read
    "<div aria-hidden='false'>x</div>",
    "<div style='display:block'>x</div>",
    "<dialog open>x</dialog>",
    "<details open><summary>s</summary>x</details>",
    "<details><summary>x</summary><p>y</p></details>",                    # the summary of a closed details
])
def test_not_oculto(html):
    assert "oculto" not in frag(run(html), "x")


def test_a_text_node_that_says_end():
    assert text("<p>end</p><p>fin</p>") == "end\nfin"


def test_oculto_does_not_remove_text():
    assert text("<div hidden>Devoluciones: 14 días</div>") == "Devoluciones: 14 días"


@pytest.mark.parametrize("html,region", [
    ("<header><p>x</p></header>", ["header"]),
    ("<nav><ul><li>x</li></ul></nav>", ["nav"]),
    ("<footer><nav>x</nav></footer>", ["footer", "nav"]),
    ("<aside>x</aside>", ["aside"]),
    ("<div role='banner'>x</div>", ["role=banner"]),
    ("<div role='navigation'>x</div>", ["role=navigation"]),
    ("<div role='contentinfo'>x</div>", ["role=contentinfo"]),
    ("<div role='complementary'>x</div>", ["role=complementary"]),
])
def test_region(html, region):
    assert frag(run(html), "x")["region"] == region


@pytest.mark.parametrize("html", ["<main><section>x</section></main>", "<div role='main'>x</div>", "<article>x</article>"])
def test_not_region(html):
    assert "region" not in frag(run(html), "x")


@pytest.mark.parametrize("html,control", [
    ("<form><p>x</p></form>", ["form"]),
    ("<select><option>x</option></select>", ["select"]),
    ("<button>x</button>", ["button"]),
    ("<textarea>x</textarea>", ["textarea"]),
    ("<label>x</label>", ["label"]),
    ("<form><label for=m>x</label></form>", ["form", "label"]),
])
def test_control(html, control):
    assert frag(run(html), "x")["control"] == control


def test_not_control():
    assert "control" not in frag(run("<fieldset><legend>x</legend></fieldset>"), "x")


def test_alt_in_the_place_of_the_image():
    rep = run("<p>Antes<img src=a.jpg alt='Foto  del   edredón' title='Título'>después</p><img alt=''><img src=b>")
    assert rep["text"] == "Antes Foto del edredón después"
    f = frag(rep, "Foto")
    assert f["alt"] is True and f["ruta"] == "/html/body/p/img"
    assert "alt" not in frag(rep, "Antes")
    assert len(rep["fragments"]) == 3


def test_enlace_absolute_url():
    rep = run("<a href='/envios'>Envíos</a> <a href=' politica?x=1&amp;y=2 '>Política</a>"
              "<a href='https://otra.test/a'><img alt='Logo'></a> fuera")
    assert frag(rep, "Envíos")["enlace"] == "https://tienda.test/envios"
    assert frag(rep, "Política")["enlace"] == "https://tienda.test/p/politica?x=1&y=2"
    assert frag(rep, "Logo")["enlace"] == "https://otra.test/a"
    assert "enlace" not in frag(rep, "fuera")


def test_enlace_with_base_href():
    rep = run("<head><base href='https://cdn.test/es/'></head><a href='envios'>Envíos</a>")
    assert frag(rep, "Envíos")["enlace"] == "https://cdn.test/es/envios"


def test_enlace_keeps_query_references_that_are_not_ended():
    rep = run("<a href='/p?a=1&currency=EUR&copy=2'>x</a>")
    assert frag(rep, "x")["enlace"] == "https://tienda.test/p?a=1&currency=EUR&copy=2"


# --- Parser (HTML Living Standard, scripting disabled) ---------------------------------------------

def test_out_of_the_text():
    html = ("<head><meta name=description content='meta'><script>var head = 1</script></head>"
            "<body><script type='application/ld+json'>{\"sku\": \"ld\"}</script><style>p{}</style>"
            "<template><p>plantilla</p></template><!-- comentario --><iframe>marco</iframe>"
            "<object><p>objeto</p></object><embed src=x><svg><style>.a{}</style><text>svg</text></svg><p>Fin</p></body>")
    assert text(html) == "svg\nFin"


def test_noscript_is_content():
    rep = run("<head><noscript><img src=pixel alt='Píxel'></noscript></head><body><noscript><p>Sin JS</p></noscript></body>")
    assert rep["text"] == "Píxel\nSin JS"


def test_title_of_the_document():
    rep = run("<head><title>\n  Edredón   nude &amp; <b>rayas</b> </title></head><svg><title>icono</title></svg>")
    assert rep["title"] == "Edredón nude & <b>rayas</b>"
    assert rep["text"] == "icono"


def test_text_in_head_goes_to_the_body():
    assert run("<html><head><title>T</title>Hola<p>mundo</p></head></html>")["text"] == "Hola\nmundo"


def test_implied_end_tags():
    assert text("<p>uno<div>dos</div><ul><li>tres<li>cuatro</ul><dl><dt>a<dd>b</dl>") == \
        "uno\ndos\n- tres\n- cuatro\na\nb"


def test_foster_parenting_moves_text_before_the_table():
    assert text("<table><tr><td>celda</td></tr>suelto<tr><td>otra</td></tr></table>") == "suelto\ncelda\notra"


def test_implied_tbody_and_rows():
    rep = run("<table><td>a<td>b<tr><th>c</table>")
    assert rep["text"] == "a | b\nc"
    assert frag(rep, "a")["ruta"] == "/html/body/table/tbody/tr[1]/td[1]"


def test_svg_title_is_markup_and_self_closing_counts_in_svg():
    rep = run("<div><svg><title/><desc/><g/></svg><p>después</p></div><svg><title>Icono <b>X</b></title></svg>")
    assert rep["text"] == "después\nIcono X"
    assert frag(rep, "después")["ruta"] == "/html/body/div/p"


def test_self_closing_does_not_close_an_html_element():
    rep = run("<div/>dentro</div><span/>también")
    assert frag(rep, "dentro")["ruta"] == "/html/body/div"
    assert frag(rep, "también")["ruta"] == "/html/body/span"


def test_cdata_is_text_only_in_svg():
    assert text("<svg><text><![CDATA[a<b]]></text></svg><p><![CDATA[x]]>y</p>") == "a<b\ny"


def test_self_closing_script_swallows_until_its_end_tag():
    assert text("<script src=a.js /><p>dentro</p></script><p>fuera</p>") == "fuera"


def test_newline_after_pre_and_textarea_is_dropped():
    assert text("<textarea>\nTexto</textarea>") == "Texto"


# --- Encoding --------------------------------------------------------------------------------------

def test_encoding_bom_first():
    assert sniff(b"\xef\xbb\xbf<p>x", "text/html; charset=iso-8859-1") == ("UTF-8", "bom", 3)


def test_encoding_http_before_meta():
    raw = "<meta charset=utf-8><p>Edredón".encode("cp1252")
    assert decode(raw, "text/html; charset=ISO-8859-1")[1:] == ("windows-1252", "http")
    assert decode(raw, "text/html; charset=ISO-8859-1")[0].endswith("Edredón")


def test_encoding_meta_charset_and_pragma():
    raw = "<meta http-equiv='Content-Type' content='text/html; charset=latin1'><p>Envío 5".encode("cp1252") + b"\x80\x81"
    out, name, where = decode(raw, "text/html")
    assert (name, where) == ("windows-1252", "meta") and out.endswith("Envío 5€\x81")


def test_encoding_without_declaration():
    assert decode("<p>Edredón".encode("utf-8"))[1:] == ("UTF-8", "detectada")
    assert decode("<p>Edredón".encode("cp1252"))[1:] == ("windows-1252", "detectada")


def test_unknown_label_is_ignored():
    assert sniff(b"<meta charset=utf-8>", "text/html; charset=klingon")[:2] == ("UTF-8", "meta")


# --- Page of capture, output and CLI ---------------------------------------------------------------

@pytest.fixture
def store(tmp_path, monkeypatch):
    """A store of capture with one audit-es page and one reader page."""
    import capture
    from capture import pages

    monkeypatch.setattr(capture, "ROOT", tmp_path)
    monkeypatch.setattr(pages, "PAGES", tmp_path / "var/pages")
    raw = "<html><head><title>Ficha</title></head><body><p>Composición: 100% algodón</p></body></html>".encode("cp1252")
    for pid, profile in (("audit-x", "audit-es"), ("reader-x", "reader")):
        snap = tmp_path / f"var/pages/{pid}/20261030T000000"
        snap.mkdir(parents=True)
        (snap / "response.html.gz").write_bytes(gzip.compress(raw))
        meta = {"profile": profile, "response_body": "original" if profile == "audit-es" else "decoded",
                "http": {"headers": {"content-type": "text/html; charset=windows-1252"}},
                "files": {"response.html": {"sha256": hashlib.sha256(raw).hexdigest()}}}
        (snap / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
        (tmp_path / f"var/pages/{pid}.html").write_bytes(raw)
        info = {"id": pid, "url": "https://tienda.test/x", "url_final": "https://tienda.test/x",
                "fetched_at": "2026-10-30T00:00:00+01:00", "profile": profile,
                "snapshot": f"var/pages/{pid}/20261030T000000"}
        (tmp_path / f"var/pages/{pid}.json").write_text(json.dumps(info), encoding="utf-8")
    monkeypatch.setattr(alfa, "REPRESENTATIONS", tmp_path / "representations")
    return tmp_path


def test_from_page_reads_the_original_bytes(store):
    rep = alfa.from_page("audit-x")
    assert rep["ficha"] == "audit-x" and rep["title"] == "Ficha"
    assert rep["text"] == "Composición: 100% algodón"
    assert rep["source"]["encoding"] == "windows-1252" and rep["source"]["encoding_from"] == "http"
    assert rep["source"]["profile"] == "audit-es" and rep["source"]["captured_at"].startswith("2026-10-30")


def test_from_page_refuses_what_is_not_audit_es(store):
    with pytest.raises(alfa.AlfaError, match="audit-es"):
        alfa.from_page("reader-x")
    with pytest.raises(alfa.AlfaError, match="no hay página congelada"):
        alfa.from_page("no-existe")


def test_write_keeps_an_output_and_refuses_another(store):
    rep = alfa.from_page("audit-x")
    path, written = alfa.write(rep)
    assert written and path.name == "audit-x.alfa-1.json"
    assert json.loads(path.read_text(encoding="utf-8")) == rep
    assert alfa.write(rep) == (path, False)
    with pytest.raises(alfa.AlfaError, match="ya existe"):
        alfa.write(rep | {"text": rep["text"] + "!"})


def test_output_is_read_by_the_validator(store):
    """records.Representation reads filter, version, ficha, title and text."""
    from info_audit.records import Representation

    rep = alfa.from_page("audit-x")
    r = Representation(json.loads(alfa.dumps(rep)), "alfa/1")
    f = rep["fragments"][0]
    ev = {"evidencia_id": "E-001", "tipo": "presencia", "contenido_original": "100% algodón",
          "localizador": {"posicion": [f["start"], f["end"]], "ruta": f["ruta"]}}
    assert r.page == "audit-x" and r.check(ev) == []


# --- The quilt of BB (T-101): its panels are aria-hidden and inert ---------------------------------

def test_bb_quilt_panels_are_oculto():
    from capture import pages

    if not (pages.PAGES / "audit-bb-edredon-6172.html").exists():
        pytest.skip("sin la ficha audit-bb-edredon-6172 en capture/var/pages/")
    rep = alfa.from_page("audit-bb-edredon-6172")
    spans_ok(rep)
    for start in ("100% Poliéster", "3 a 4 días laborables.", "Dispones de 14 días naturales"):
        f = frag(rep, start)
        assert {"aria-hidden", "inert"} <= set(f["oculto"]), f
