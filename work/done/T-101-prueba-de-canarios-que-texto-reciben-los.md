---
id: T-101
title: Prueba de canarios: qué texto reciben los asistentes de IA al leer una página
status: hecha
depends:
milestone:
created: 2026-10-29
closed: 2026-10-30
---

## Objetivo

Medir qué construcciones HTML llegan al modelo en la lectura en vivo de los asistentes públicos (ChatGPT, Claude, Gemini, Perplexity, Copilot) y de los extractores de referencia, para fijar el filtro full-text/1 del ámbito Texto.

## Criterios de aceptación

- [x] La ficha de prueba (58 canarios) y la página larga (7 sondas de truncado) quedan publicadas en una URL pública con registro de peticiones
- [x] Hay una matriz canario × lector en research_notes/text-reading-canaries/results/ para los extractores de referencia y para cada asistente probado
- [x] El registro de peticiones dice, por asistente, el user agent y qué recursos pidió (HTML, CSS, JS, imágenes, robots.txt)
- [x] Un informe en reports/ propone el filtro full-text/1 con cada regla respaldada por la matriz

## Resultado

Canarios con 4 lectores en vivo; ámbitos Contenido y Marcado, filtro Alfa y alcance de lectura al canon (D-220 a D-223)

## Notas

- 2026-10-29 Extractores de referencia (11) en results/local/index.md. Sonda de chats sin sesión con el Chrome del motor (tools/chats.py probe): ChatGPT, Gemini y Perplexity ofrecen campo de texto; Claude pide login; Copilot (copilot.com/es-es) y Meta AI, sin campo detectado. Alojamiento bloqueado por el entorno: descarga de cloudflared y túnel SSH (localhost.run) denegados; servidor local con registro listo (tools/serve.py, 127.0.0.1:8765). Falta la URL pública.
- 2026-10-29 ChatGPT sin sesión: 2 pasadas iguales y copia literal de 66 líneas (results/chat/chatgpt-20261029T232342.txt). Claude Code WebFetch: Turndown sin script/style ni noscript; trunca a 100.000 caracteres. ChatGPT: primer tramo < 25.000 caracteres. Gemini sin sesión no abre URL; Perplexity pide registro. Informe: reports/Lectura de texto de los asistentes.md (borrador del filtro full-text/1; pendiente decidir intersección o unión).
- 2026-10-29 Gemini Flash con sesión (manual del usuario): recibe HTML depurado (etiquetas + alt, title, href, hidden, aria-*, role, itemprop), sin <title>, head, scripts, class, style, data-*, <form> ni noscript; truncado entre 10.000 y 25.000 como ChatGPT. En BB los hechos están fuera de <form>. Nueva página site/corte.html (sondas QC cada 2.000 de 12.000 a 24.000); clave de index y largo sin cambios (verificado contra lo publicado).
- 2026-10-29 Corte (corte.html): Gemini Flash corta hacia 12.845 caracteres de texto (~14,1 KB de HTML depurado); ChatGPT lee por tramos y en corte.html leyó la página entera (559 líneas); Claude Code, 100.000. Informe actualizado.
- 2026-10-29 Claude.ai (Sonnet 5.5, con sesión): bloque de metadatos (title, meta description, og) + Markdown; descarta el atributo hidden (QX19, QX27) y title de imagen; corte poco después de 100.000; corte.html entera. Informe con 4 lectores.
- 2026-10-29 access_log de dasys.es (results/access/): ChatGPT-User (158.158.5.x, sin robots.txt, pide la portada tras largo.html), Claude-User de claude.ai (160.79.106.x, pide robots.txt), Claude-User de Claude Code (IP del usuario), Gemini con UA «Google» (142.250.88.67) y antes Google-Lens. Nadie pidió CSS/JS/imágenes (la ficha no tiene subrecursos externos).
- 2026-10-29 Estrategia: reports/Estrategia del ámbito Texto.md. Propuesta: definición normativa (DOM §4.4 descendant text content + title + alt por HTML §4.8.4.4, con scripts desactivados, sin script/style/template ni atributos) + alcance de lectura como hallazgos sin escala con panel versionado (patrón D-124; análogos WCAG accessibility supported y Baseline). Retira la recomendación de unión.
- 2026-10-30 Corte en ficha real: estimación con depuración tipo Gemini en BB (edredón): HTML depurado ≈42 KB para 13.350 caracteres de texto (ratio 3,15); si Gemini corta a ~14,1 KB de su HTML, cortaría en el menú (~3.200 caracteres de texto), antes del nombre del producto. ChatGPT sin sesión sobre la misma ficha (results/chat/chatgpt-20261030T000321.txt): recibe la página entera (acaba en el modal de regalo) y ve composición, precio 135 y envío. Falta Gemini con sesión sobre BB (prompts/bb-corte.txt).
- 2026-10-30 Decisiones del usuario (30-10-2026): criterio = definición normativa + alcance de lectura (recomendación); ámbito Texto → «Contenido» (content); ámbito Web Schema.org → «Marcado» (markup); filtros con el alfabeto radiofónico: el primero es Alfa (alfa/1, antes full-text/1), especificación en reports/Estrategia del ámbito Texto.md §7. Pendiente: Gemini con sesión sobre BB (prompts/bb-corte.txt), Perplexity y cadencia del panel.
- 2026-10-30 Procesado con /docs-update: INTAKE 2026-10-30-content-and-markup-scopes → D-220 (Contenido y Marcado), D-221 (filtros de lectura, Alfa), D-222 (alcance de lectura), D-223 (fases sobre la representación de cada ámbito); OQ-88 a OQ-92. Código: T-102 (nombres) y T-103 (Alfa en info-audit, antes de T-098).
