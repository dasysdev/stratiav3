"""Genera las páginas de canarios de lectura de texto y su clave.

Cada canario es un código único (QX##-PALABRA) colocado en una construcción HTML.
Las preguntas: qué construcciones llegan al modelo en la lectura en vivo de cada
asistente y qué hacen los extractores de referencia (Turndown, Readability…).

Uso: python3 generate.py SEMILLA  → site/index.html, site/largo.html, canaries.json
"""
import json
import random
import sys
from pathlib import Path

WORDS = """ACEBO ALCOR BADANA BERILO CANTIL CIERZO DORNAJO ESPARTO FANAL GALERNA HINOJO
ISTMO JABEGA LABRADOR MADROÑO NACAR OCRE PIZARRA QUEJIGO RETAMA SALOBRE TOMILLO ULMO
VENCEJO ZARZO ALJIBE BRUÑIDO CAÑIZO DEHESA ERIAL FRAGUA GAVIOTA HORNACINA ÍNSULA JARAL
LENTISCO MIMBRE NORIA OLMEDA PALOMAR QUINQUÉ RAMBLA SABINA TAHONA URDIMBRE VILANO
ZÓCALO ALMENA BÁLAGO CERCETA DOLMEN ENEBRO FARALLÓN GUIJARRO HELECHO JUNCO LAUREL
MARJAL NEBLINA OTERO PEDERNAL RIBERA SALINA TOJAL VAGUADA ZAFRA ARCILLA BRAÑA CORNISA
ESCARCHA FALUCHO GRANITO ACANTO BOTIJO CARRASCA DORNILLO ESTRAGON FOGARIL GAZAPO
HUSILLO""".split()
# Códigos de corte.html: lista aparte, para no cambiar el barajado de WORDS (códigos ya publicados).
WORDS_FINE = "ALBUFERA BREZO CANTUESO DUNA ESPLIEGO GAMONAL JARAMAGO".split()

# (id, construcción, cómo se coloca)
CONSTRUCTS = [
    ("title", "<title>", "head"),
    ("meta-description", "<meta name=description>", "head"),
    ("og", "<meta property=og:description>", "head"),
    ("jsonld-head", "JSON-LD en <head>", "head"),
    ("h1", "<h1>", "body"),
    ("p-visible", "<p> visible en el contenido principal", "body"),
    ("ul-li", "<li> visible", "body"),
    ("table-value", "celda <td> de una tabla etiqueta | valor", "body"),
    ("dl-dd", "<dd> de una lista de definición", "body"),
    ("pre", "<pre>", "body"),
    ("microdata-text", "microdato con valor en texto visible (itemprop en <span>)", "body"),
    ("microdata-meta", "microdato en <meta itemprop content>", "body"),
    ("rdfa-meta", "RDFa en <meta property content>", "body"),
    ("jsonld-body", "JSON-LD en <body>", "body"),
    ("json-state", "<script type=application/json> (estado de la aplicación)", "body"),
    ("js-injected", "texto que inserta un script en línea", "body"),
    ("inline-display-none", "<div style=display:none>", "body"),
    ("class-display-none", "clase con display:none en una hoja <style>", "body"),
    ("hidden-attr", "atributo hidden", "body"),
    ("aria-hidden", "<div aria-hidden=true>", "body"),
    ("visibility-hidden", "<div style=visibility:hidden>", "body"),
    ("font-size-zero", "<span style=font-size:0>", "body"),
    ("sr-only", "clase sr-only (fuera de pantalla)", "body"),
    ("dialog-aside", "<aside role=dialog aria-hidden=true inert> (panel lateral, patrón de BB)", "body"),
    ("dialog-native", "<dialog> sin open", "body"),
    ("details-closed", "contenido de <details> cerrado", "body"),
    ("tabpanel-hidden", "pestaña <div role=tabpanel hidden>", "body"),
    ("escaped-html", "HTML escapado como texto en un <span style=display:none>", "body"),
    ("noscript", "<noscript>", "body"),
    ("template", "<template>", "body"),
    ("comment", "comentario HTML", "body"),
    ("data-attr", "atributo data-*", "body"),
    ("img-alt", "atributo alt de <img>", "body"),
    ("img-title", "atributo title de <img>", "body"),
    ("figcaption", "<figcaption>", "body"),
    ("aria-label", "atributo aria-label de un botón", "body"),
    ("title-attr", "atributo title de un <span> (tooltip)", "body"),
    ("select-option", "texto de un <option>", "body"),
    ("option-value", "atributo value de un <option>", "body"),
    ("radio-label", "<label> de un botón de radio", "body"),
    ("input-value", "value de un <input type=text>", "body"),
    ("input-hidden", "value de un <input type=hidden>", "body"),
    ("input-submit", "value de un <input type=submit>", "body"),
    ("placeholder", "atributo placeholder", "body"),
    ("textarea", "contenido de <textarea>", "body"),
    ("button", "texto de un <button>", "body"),
    ("link-text", "texto de un enlace", "body"),
    ("link-href", "código en la URL de un enlace", "body"),
    ("iframe-srcdoc", "<iframe srcdoc>", "body"),
    ("svg-text", "<text> dentro de <svg>", "body"),
    ("canvas-fallback", "texto alternativo dentro de <canvas>", "body"),
    ("css-before", "content de ::before", "body"),
    ("header", "texto de <header>", "body"),
    ("nav", "texto de <nav>", "body"),
    ("breadcrumbs", "migas (<nav class=breadcrumbs>)", "body"),
    ("aside", "<aside> lateral (no diálogo)", "body"),
    ("related", "sección de productos relacionados (class=related)", "body"),
    ("footer", "texto de <footer>", "body"),
]

# Sondas de truncado: código tras N caracteres de texto de relleno.
OFFSETS = [2_000, 10_000, 25_000, 50_000, 100_000, 200_000, 400_000]
# Segunda página: afina el corte de ChatGPT y Gemini (entre 10.000 y 25.000).
OFFSETS_FINE = [12_000, 14_000, 16_000, 18_000, 20_000, 22_000, 24_000]

FILLER = [
    "El tejido se ha probado en lavados sucesivos a treinta grados sin perder color.",
    "La costura perimetral está rematada con doble pespunte para evitar deshilachados.",
    "Recomendamos airear el relleno al sacarlo del embalaje durante unas horas.",
    "El acabado del borde es recto y la etiqueta interior indica la composición.",
    "Las medidas se toman con la pieza extendida sobre una superficie plana.",
    "El embalaje es de cartón reciclado y no contiene plásticos de un solo uso.",
    "Cada pieza se revisa a mano antes de salir del almacén de Valencia.",
    "La tonalidad puede variar ligeramente según la luz de la pantalla.",
]


def main(seed: str) -> None:
    rnd = random.Random(seed)
    words = [w for w in WORDS if w.isascii()]  # sin tildes: la codificación no interfiere
    rnd.shuffle(words)
    n = len(CONSTRUCTS) + len(OFFSETS)
    assert n <= len(words), (n, len(words))
    tok = {}
    for i, (cid, _, _) in enumerate(CONSTRUCTS):
        tok[cid] = f"QX{i + 1:02d}-{words[i]}"
    probes = {}
    for j, off in enumerate(OFFSETS):
        probes[off] = f"QT{j + 1:02d}-{words[len(CONSTRUCTS) + j]}"
    fine = {}
    for j, off in enumerate(OFFSETS_FINE):
        fine[off] = f"QC{j + 1:02d}-{WORDS_FINE[j]}"

    site = Path(__file__).parent / "site"
    site.mkdir(exist_ok=True)
    (site / "index.html").write_text(index_html(tok), encoding="utf-8")
    (site / "largo.html").write_text(long_html(probes, rnd), encoding="utf-8")
    (site / "corte.html").write_text(long_html(fine, random.Random(seed + "-corte"), 26_000), encoding="utf-8")
    (site / "robots.txt").write_text("User-agent: *\nAllow: /\n", encoding="utf-8")
    key = {
        "seed": seed,
        "constructs": [
            {"id": cid, "token": tok[cid], "construct": desc, "where": where}
            for cid, desc, where in CONSTRUCTS
        ],
        "truncation": [{"offset_chars": off, "token": probes[off]} for off in OFFSETS],
        "truncation_fine": [{"offset_chars": off, "token": fine[off]} for off in OFFSETS_FINE],
    }
    (Path(__file__).parent / "canaries.json").write_text(
        json.dumps(key, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def index_html(t: dict) -> str:
    jsonld_head = json.dumps({
        "@context": "https://schema.org", "@type": "Product",
        "name": "Edredón de prueba Canario",
        "description": f"Referencia interna {t['jsonld-head']}",
    }, ensure_ascii=False)
    jsonld_body = json.dumps({
        "@context": "https://schema.org", "@type": "Offer",
        "sku": t["jsonld-body"], "price": "64.49", "priceCurrency": "EUR",
    }, ensure_ascii=False)
    state = json.dumps({"product": {"id": 1, "ref": t["json-state"]}}, ensure_ascii=False)
    return f"""<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Edredón de prueba Canario · {t['title']}</title>
<meta name="description" content="Página de prueba de lectura. Código {t['meta-description']}.">
<meta property="og:title" content="Edredón de prueba Canario">
<meta property="og:description" content="Código {t['og']}.">
<script type="application/ld+json">{jsonld_head}</script>
<style>
.oculto {{ display: none; }}
.sr-only {{ position: absolute; left: -9999px; width: 1px; height: 1px; overflow: hidden; }}
.antes::before {{ content: "{t['css-before']}"; }}
</style>
</head>
<body>
<header class="site-header"><p>Tienda de prueba. Aviso de cabecera {t['header']}.</p></header>
<nav class="menu"><ul><li><a href="#">Edredones</a></li><li><a href="#">Menú {t['nav']}</a></li></ul></nav>
<nav class="breadcrumbs" aria-label="breadcrumb"><a href="#">Inicio</a> › <a href="#">Edredones</a> › Migas {t['breadcrumbs']}</nav>
<main>
<article class="product">
<h1>Edredón de prueba Canario {t['h1']}</h1>
<p>Edredón reversible para pruebas de lectura. Párrafo visible {t['p-visible']}.</p>
<ul><li>Reversible</li><li>Característica en lista {t['ul-li']}</li></ul>
<table class="specs">
<tr><th>Composición</th><td>100% poliéster</td></tr>
<tr><th>Gramaje</th><td>Valor de tabla {t['table-value']}</td></tr>
</table>
<dl><dt>Lavado</dt><dd>A 30 grados. Definición {t['dl-dd']}</dd></dl>
<pre>Ficha técnica en bloque preformateado {t['pre']}</pre>
<div itemscope itemtype="https://schema.org/Product">
<span itemprop="name">Edredón Canario</span>, marca <span itemprop="brand">Microdato visible {t['microdata-text']}</span>
<meta itemprop="sku" content="{t['microdata-meta']}">
</div>
<div vocab="https://schema.org/" typeof="Product"><meta property="mpn" content="{t['rdfa-meta']}"><span property="name">Edredón Canario RDFa</span></div>
<script type="application/ld+json">{jsonld_body}</script>
<script type="application/json" id="state">{state}</script>
<div id="inyectado"></div>
<script>document.getElementById("inyectado").textContent = "Texto insertado por script {t['js-injected']}";</script>
<div style="display:none">Bloque con display none en línea {t['inline-display-none']}</div>
<div class="oculto">Bloque oculto por clase {t['class-display-none']}</div>
<div hidden>Bloque con atributo hidden {t['hidden-attr']}</div>
<div aria-hidden="true">Bloque con aria-hidden {t['aria-hidden']}</div>
<div style="visibility:hidden">Bloque con visibility hidden {t['visibility-hidden']}</div>
<span style="font-size:0">Texto de tamaño cero {t['font-size-zero']}</span>
<span class="sr-only">Texto solo para lectores de pantalla {t['sr-only']}</span>
<button type="button" class="abrir-panel">Qué incluye y medidas</button>
<aside class="info-sheet" role="dialog" aria-modal="true" aria-hidden="true" inert>
<h3>Qué incluye y medidas</h3><p>Medidas del panel lateral {t['dialog-aside']}</p>
</aside>
<dialog id="envio"><p>Diálogo nativo cerrado {t['dialog-native']}</p></dialog>
<details><summary>Cuidados</summary><p>Contenido de details cerrado {t['details-closed']}</p></details>
<div role="tablist"><button role="tab" aria-selected="true">Descripción</button><button role="tab" aria-selected="false">Envíos</button></div>
<div role="tabpanel"><p>Pestaña visible de descripción.</p></div>
<div role="tabpanel" hidden><p>Pestaña de envíos oculta {t['tabpanel-hidden']}</p></div>
<span class="visitado" style="display:none">&lt;p&gt;Descripción escapada {t['escaped-html']}&lt;/p&gt;</span>
<noscript><p>Texto de noscript {t['noscript']}</p></noscript>
<template><p>Texto de template {t['template']}</p></template>
<!-- Comentario {t['comment']} -->
<div data-ref="{t['data-attr']}">Elemento con atributo data.</div>
<figure>
<img src="data:image/gif;base64,R0lGODlhAQABAAAAACw=" alt="Foto del edredón {t['img-alt']}" title="Título de imagen {t['img-title']}" width="1" height="1">
<figcaption>Pie de foto {t['figcaption']}</figcaption>
</figure>
<button type="button" aria-label="Añadir a favoritos {t['aria-label']}">♥</button>
<span title="Ayuda emergente {t['title-attr']}">¿Qué medida elijo?</span>
<form>
<label for="medida">Medida</label>
<select id="medida" name="medida">
<option value="90">Cama 90 cm</option>
<option value="135">Cama 135 cm opción {t['select-option']}</option>
<option value="{t['option-value']}">Cama 150 cm</option>
</select>
<fieldset><legend>Color</legend>
<input type="radio" id="c1" name="color" value="nude"><label for="c1">Nude etiqueta {t['radio-label']}</label>
</fieldset>
<input type="text" name="nota" value="Valor de campo {t['input-value']}">
<input type="hidden" name="ref" value="{t['input-hidden']}">
<input type="text" name="cp" placeholder="Código postal {t['placeholder']}">
<textarea name="comentario">Texto de textarea {t['textarea']}</textarea>
<input type="submit" value="Enviar {t['input-submit']}">
<button type="submit">Añadir al carrito {t['button']}</button>
</form>
<p><a href="/politicas/envios">Política de envíos {t['link-text']}</a> · <a href="/ref/{t['link-href']}">Ver referencia</a></p>
<iframe srcdoc="&lt;p&gt;Contenido de iframe {t['iframe-srcdoc']}&lt;/p&gt;" title="marco"></iframe>
<svg width="200" height="20" role="img"><text x="0" y="15">Texto SVG {t['svg-text']}</text></svg>
<canvas width="1" height="1">Alternativa de canvas {t['canvas-fallback']}</canvas>
<p class="antes">: texto con pseudoelemento.</p>
</article>
<aside class="sidebar"><p>Lateral con ofertas {t['aside']}</p></aside>
<section class="related"><h2>También te puede gustar</h2><p>Producto relacionado {t['related']}</p></section>
</main>
<footer class="site-footer"><p>Pie de página. Envío gratis desde 49 €. Código {t['footer']}.</p></footer>
</body>
</html>
"""


def long_html(probes: dict, rnd: random.Random, tail: int = 0) -> str:
    parts, size, i = [], 0, 0
    for off in sorted(probes):
        while size < off:
            s = FILLER[i % len(FILLER)] + f" Lote {rnd.randint(1000, 9999)}."
            parts.append(f"<p>{s}</p>")
            size += len(s) + 1
            i += 1
        s = f"Marca de posición {off} caracteres: {probes[off]}."
        parts.append(f"<p>{s}</p>")
        size += len(s) + 1
    while size < tail:  # relleno tras la última sonda: la página no acaba en ella
        s = FILLER[i % len(FILLER)] + f" Lote {rnd.randint(1000, 9999)}."
        parts.append(f"<p>{s}</p>")
        size += len(s) + 1
        i += 1
    body = "\n".join(parts)
    return f"""<!doctype html>
<html lang="es">
<head><meta charset="utf-8"><title>Prueba de longitud de lectura</title></head>
<body><main><h1>Prueba de longitud de lectura</h1>
{body}
</main></body></html>
"""


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "stratia-cic")
