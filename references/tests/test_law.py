"""Laws (BOE and EUR-Lex through Cellar), the reader of their citations and the code lists (ISO 4217, ISO 3166-1)."""
import json
import urllib.parse

import pytest

from references import read, store
from references.kinds import euvoc, law

BOE = law.BOE_API.format("BOE-A-2007-20555")
BOE_META = b"<response><data><metadatos><titulo>Real Decreto Legislativo 1/2007</titulo></metadatos></data></response>"
BOE_TEXT = """<response><data><texto>
<bloque id="a96" tipo="precepto" titulo="Artículo 96">
 <version id_norma="BOE-A-2007-20555" fecha_publicacion="20071130" fecha_vigencia="20071201">
  <p class="articulo">Artículo 96. Antes.</p><p class="parrafo">Texto del 96.</p></version>
</bloque>
<bloque id="a97" tipo="precepto" titulo="Artículo 97">
 <version id_norma="BOE-A-2007-20555" fecha_publicacion="20071130" fecha_vigencia="20071201">
  <p class="articulo">Artículo 97. Información precontractual.</p>
  <p class="parrafo">1. Antes de contratar, el empresario facilitará:</p>
  <p class="parrafo_2">a) Las características principales.</p>
  <p class="parrafo">e) El precio total.</p>
 </version>
 <version id_norma="BOE-A-2026-1" fecha_publicacion="20260228" fecha_vigencia="20260301">
  <p class="articulo">Artículo 97. Información precontractual.</p>
  <p class="parrafo">1. Antes de contratar, el empresario facilitará:</p>
  <p class="parrafo_2">a) Las características principales.</p>
  <p class="parrafo">e) El precio total, con impuestos.</p>
  <p class="parrafo">f) El coste de la comunicación.</p>
  <p class="parrafo">2. Otro apartado.</p>
 </version>
</bloque>
<bloque id="df1" tipo="precepto" titulo="Disposición final primera">
 <version id_norma="BOE-A-2007-20555" fecha_publicacion="20071130" fecha_vigencia="20071201">
  <p class="articulo">Disposición final primera. Entrada en vigor.</p><p class="parrafo">Mañana.</p></version>
 <version id_norma="BOE-A-2026-1" fecha_publicacion="20260228" fecha_vigencia="20260301">
  <p class="articulo">Disposición final primera. Entrada en vigor.</p><p class="parrafo">Hoy.</p></version>
</bloque>
</texto></data></response>""".encode("utf-8")

ORIGINAL = """<html><head><title>L_2011272ES</title></head><body>
<p class="oj-hd-date">18.10.2011 </p>
<p class="oj-doc-ti">REGLAMENTO (UE) N<span class="oj-super">o</span> 1007/2011</p>
<p class="oj-doc-ti">de 27 de septiembre de 2011</p><p class="oj-doc-ti">relativo a las fibras textiles</p>
<div class="eli-subdivision" id="art_16"><p class="oj-ti-art">Artículo 16</p>
 <div class="eli-title"><p class="oj-sti-art">Uso de denominaciones</p></div>
 <div id="016.001"><p class="oj-normal">1.   La composición será visible antes de la adquisición:</p>
  <table><col width="4%"/><tbody><tr><td><p class="oj-normal">a)</p></td><td><p class="oj-normal">en la etiqueta;</p></td></tr></tbody></table>
  <table><tbody><tr><td><p class="oj-normal">b)</p></td><td><p class="oj-normal">en el catálogo.</p></td></tr></tbody></table></div>
 <div id="016.002"><p class="oj-normal">2.   La marca podrá situarse antes.</p><p class="oj-normal">Cualquier otra información, por separado.</p></div>
</div>
<div class="eli-subdivision" id="art_17"><p class="oj-ti-art">Artículo 17</p><p class="oj-normal">Excepciones.</p></div>
<div class="oj-final"><p class="oj-normal">Hecho en Estrasburgo,</p><p class="oj-signatory">Por el Parlamento</p></div>
<p class="oj-doc-ti" id="anx_I">ANEXO I</p><p class="oj-normal">Lista de fibras.</p>
</body></html>"""

CONSOLIDATED = """<html><body>
<table><tr><td><p class="arrow"><a href="x">►B</a></p></td><td>
<p class="title-doc-first">REGLAMENTO (UE) N<span class="superscript">o</span> 1007/2011</p>
<p class="title-doc-first">de 27 de septiembre de 2011</p><p class="title-doc-first">relativo a las fibras textiles</p></td></tr></table>
<p class="modref"><a href="y">▼M1</a></p>
<p class="title-article-norm">Artículo 16</p><p class="stitle-article-norm">Uso de denominaciones</p>
<div class="norm"><span class="no-parag">1.  </span><div class="norm inline-element">
 <p class="norm inline-element">La composición será visible antes de la adquisición:</p>
 <div class="grid-container grid-list"><div class="list grid-list-column-1"><span>a) </span></div>
  <div class="grid-list-column-2"><p class="norm">en la etiqueta;</p></div></div>
 <div class="grid-container grid-list"><div class="list grid-list-column-1"><span>b) </span></div>
  <div class="grid-list-column-2"><p class="norm">en el ►M1 catálogo electrónico ◄.</p></div></div></div></div>
<p class="norm">2.  La marca podrá situarse antes.</p><p class="norm">Cualquier otra información, por separado.</p>
<p class="title-article-norm">Artículo 17</p><p class="norm">Excepciones.</p>
</body></html>"""


def test_the_text_of_a_law_has_a_heading_per_article_and_a_line_per_paragraph():
    original = law.text_lines(ORIGINAL)
    assert original[original.index("## Artículo 16"):] == [
        "## Artículo 16", "Uso de denominaciones", "1. La composición será visible antes de la adquisición:",
        "a) en la etiqueta;", "b) en el catálogo.", "2. La marca podrá situarse antes.",
        "Cualquier otra información, por separado.", "## Artículo 17", "Excepciones.",
        "## Hecho en Estrasburgo, Por el Parlamento", "## ANEXO I", "Lista de fibras."]
    assert "## REGLAMENTO (UE) No 1007/2011" in original                     # the title, a heading of its own
    assert read.law_passage("\n".join(original), ["17"]) == "## Artículo 17\nExcepciones."
    consolidated = law.text_lines(CONSOLIDATED)
    assert "▼M1" not in "".join(consolidated) and "►B" not in "".join(consolidated)
    assert consolidated[consolidated.index("## Artículo 16"):][2:5] == [
        "1. La composición será visible antes de la adquisición:", "a) en la etiqueta;", "b) en el catálogo electrónico ."]
    assert law.eu_title(ORIGINAL, original) == "REGLAMENTO (UE) No 1007/2011 de 27 de septiembre de 2011 relativo a las fibras textiles"
    assert law.oj_date(ORIGINAL) == "2011-10-18"


def boe_pages(web):
    web[BOE + "metadatos"] = (BOE_META, {})
    web[BOE + "texto"] = (BOE_TEXT, {})


def test_a_boe_law_is_versioned_by_its_last_amendment_and_read_at_any_of_them(web, refs_dir):
    boe_pages(web)
    source = store.sources()["es-trlgdcu"]
    law.fetch("es-trlgdcu", source, None)
    assert store.versions("es-trlgdcu") == ["2026-02-28"] and store.pins()["es-trlgdcu"] == "2026-02-28"
    law.fetch("es-trlgdcu", source, "2007-11-30")                   # the text as it was then
    assert store.pins()["es-trlgdcu"] == "2026-02-28"               # the first version stays pinned
    old = (refs_dir / "es-trlgdcu/2007-11-30/text.md").read_text(encoding="utf-8")
    assert old.startswith("# Real Decreto Legislativo 1/2007\n") and "f) El coste" not in old
    files = {f["path"]: f for f in store.manifest("es-trlgdcu", "2026-02-28")["files"]}
    assert files["texto.xml"]["counted_by"] == "text.md" and "counted_by" not in files["text.md"]
    with pytest.raises(store.RefsError, match="no hay versión 2020-01-01"):
        law.fetch("es-trlgdcu", source, "2020-01-01")


def test_an_eu_law_is_its_latest_consolidated_version_or_the_original_by_its_journal_date(web, refs_dir, monkeypatch):
    monkeypatch.setattr(law, "consolidated", lambda celex: {"2018-02-15": "02011R1007-20180215", "2099-01-01": "02011R1007-20990101"})
    web[law.CELLAR.format("02011R1007-20180215")] = (CONSOLIDATED.encode("utf-8"), {})
    web[law.CELLAR.format("32011R1007")] = (ORIGINAL.encode("utf-8"), {})
    source = store.sources()["eu-reg-1007-2011"]
    law.fetch("eu-reg-1007-2011", source, None)                     # the latest not after today
    law.fetch("eu-reg-1007-2011", source, "2011-10-18")             # the original
    assert store.versions("eu-reg-1007-2011") == ["2011-10-18", "2018-02-15"]
    assert store.pins()["eu-reg-1007-2011"] == "2018-02-15"
    assert store.manifest("eu-reg-1007-2011", "2011-10-18")["origin"]["celex"] == "32011R1007"
    with pytest.raises(store.RefsError, match="original: 2011-10-18"):
        law.fetch("eu-reg-1007-2011", source, "2011-10-25")


def test_a_citation_names_a_law_by_its_code_and_a_passage_by_article_and_apartado(web, refs_dir, monkeypatch):
    boe_pages(web)
    law.fetch("es-trlgdcu", store.sources()["es-trlgdcu"], None)
    law.fetch("es-trlgdcu", store.sources()["es-trlgdcu"], "2007-11-30")
    codes = {"TRLGDCU": "es-trlgdcu", "UE-1007/2011": "eu-reg-1007-2011", "UE-1007/2011-X": "longer"}
    assert read.law_codes() == {"TRLGDCU": "es-trlgdcu", "UE-1007/2011": "eu-reg-1007-2011"}
    assert read.law_reference("ley:TRLGDCU-97.1.e@2026-02-28", codes) == ("es-trlgdcu", "TRLGDCU", ["97", "1", "e"], "2026-02-28")
    assert read.law_reference("ley:UE-1007/2011-X-16@2011", codes)[:3] == ("longer", "UE-1007/2011-X", ["16"])
    assert read.law_reference("ley:UE-1007/2011", codes) == ("eu-reg-1007-2011", "UE-1007/2011", [], None)
    assert read.law_reference("ley:LOCM-20.1@2022-03-30", codes) is None
    assert read.law_citation("ley:TRLGDCU-97.1.e@2026-02-28")["text"] == "e) El precio total, con impuestos."
    assert read.law_citation("ley:TRLGDCU-97.1.e@2007-11-30")["text"] == "e) El precio total."
    assert read.law_citation("ley:TRLGDCU-97.1")["text"].splitlines()[-1] == "f) El coste de la comunicación."
    assert read.law_citation("ley:TRLGDCU-97")["text"].splitlines()[-1] == "2. Otro apartado."   # a provision closes it
    with pytest.raises(store.RefsError, match="el artículo 97 no tiene 1.f"):
        read.law_citation("ley:TRLGDCU-97.1.f@2007-11-30")
    with pytest.raises(store.RefsError, match="no existe el artículo 98"):
        read.law_citation("ley:TRLGDCU-98")
    with pytest.raises(store.RefsError, match="no existe la versión 2026-01-01"):
        read.law_citation("ley:TRLGDCU-97@2026-01-01")
    assert read.law_changes("es-trlgdcu", "2007-11-30", "2026-02-28") == ["97", "Disposición final primera. Entrada en vigor."]


def test_marks_of_another_kind_stay_inside_the_passage():
    text = "## Artículo 3\n8) «producto»: todo artículo\ni) nuevo;\nii) usado;\n9) otra definición"
    assert read.law_passage(text, ["3", "8"]) == "8) «producto»: todo artículo\ni) nuevo;\nii) usado;"
    assert read.law_passage(text, ["3", "ii"]) == "ii) usado;\n9) otra definición"


def test_a_law_declares_its_code_and_a_single_official_identifier(refs_dir):
    path = store.sources_file()
    data = json.loads(path.read_text(encoding="utf-8"))
    data["sources"] += [{"id": "x", "kind": "law", "title": "X", "url": "u", "uses": ["demand-engine"], "boe": "a", "celex": "b"},
                        {"id": "y", "kind": "eu-authority", "title": "Y", "url": "u", "uses": ["web-audit"]}]
    path.write_text(json.dumps(data), encoding="utf-8")
    with pytest.raises(store.RefsError) as e:
        store.sources()
    assert "x: falta cite" in str(e.value) and "x: solo uno de boe, celex" in str(e.value)
    assert "y: falta authority" in str(e.value) and "y: falta file" in str(e.value)


SKOS = """<?xml version="1.0"?><rdf:RDF xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
 xmlns:skos="http://www.w3.org/2004/02/skos/core#" xmlns:owl="http://www.w3.org/2002/07/owl#"
 xmlns:atold="http://publications.europa.eu/ontology/authority/">
<skos:Concept rdf:about="http://publications.europa.eu/resource/authority/country/ESP">
 <skos:prefLabel xml:lang="en">Spain</skos:prefLabel><skos:prefLabel xml:lang="es">España</skos:prefLabel>
 <skos:notation rdf:datatype="http://publications.europa.eu/ontology/euvoc#ISO_3166_1_ALPHA_2">ES</skos:notation>
 <skos:notation rdf:datatype="http://publications.europa.eu/ontology/euvoc#ISO_3166_1_ALPHA_3">ESP</skos:notation>
</skos:Concept>
<skos:Concept rdf:about="http://publications.europa.eu/resource/authority/country/ANT">
 <atold:deprecated rdf:datatype="http://www.w3.org/2001/XMLSchema#boolean">true</atold:deprecated>
 <skos:notation rdf:datatype="http://publications.europa.eu/ontology/euvoc#ISO_3166_1_ALPHA_2">AN</skos:notation>
</skos:Concept></rdf:RDF>"""

LIST_ONE = """<?xml version="1.0" encoding="UTF-8"?><ISO_4217 Pblshd="2026-09-17"><CcyTbl>
<CcyNtry><CtryNm>SPAIN</CtryNm><CcyNm>Euro</CcyNm><Ccy>EUR</Ccy><CcyNbr>978</CcyNbr><CcyMnrUnts>2</CcyMnrUnts></CcyNtry>
<CcyNtry><CtryNm>FRANCE</CtryNm><CcyNm>Euro</CcyNm><Ccy>EUR</Ccy><CcyNbr>978</CcyNbr><CcyMnrUnts>2</CcyMnrUnts></CcyNtry>
<CcyNtry><CtryNm>ANTARCTICA</CtryNm><CcyNm>No universal currency</CcyNm></CcyNtry>
</CcyTbl></ISO_4217>"""


def test_an_eu_authority_table_is_versioned_by_its_release(web, refs_dir):
    web[euvoc.SCHEME.format("country")] = (b"<rdf:RDF><owl:versionInfo>20260923-0</owl:versionInfo></rdf:RDF>", {})
    cellar = euvoc.DISTRIBUTION.format("country", "20260923-0", "countries-skos.rdf")
    web[euvoc.DOWNLOAD + urllib.parse.urlencode({"cellarURI": cellar, "fileName": "countries-skos.rdf"})] = (SKOS.encode(), {})
    source = store.sources()["iso-3166-1"]
    assert euvoc.check("iso-3166-1", source) == "sin descargar (en origen: 20260923-0)"
    euvoc.fetch("iso-3166-1", source, None)
    assert store.pins()["iso-3166-1"] == "20260923-0" and euvoc.check("iso-3166-1", source) == "al día (20260923-0)"
    assert read.country_codes() == {"ES": "España"}


def test_the_currency_codes_of_list_one(refs_dir):
    snap = store.Version("iso-4217", "2026-10-28", {})
    snap.add("list-one.xml", LIST_ONE.encode(), "x")
    snap.commit()
    codes = read.currency_codes()
    assert list(codes) == ["EUR"]
    assert codes["EUR"] == {"name": "Euro", "number": "978", "minor_units": "2", "entities": ["SPAIN", "FRANCE"]}
