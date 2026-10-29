---
id: T-101
title: Prueba de canarios: qué texto reciben los asistentes de IA al leer una página
status: en-curso
depends:
milestone:
created: 2026-10-29
---

## Objetivo

Medir qué construcciones HTML llegan al modelo en la lectura en vivo de los asistentes públicos (ChatGPT, Claude, Gemini, Perplexity, Copilot) y de los extractores de referencia, para fijar el filtro full-text/1 del ámbito Texto.

## Criterios de aceptación

- [ ] La ficha de prueba (58 canarios) y la página larga (7 sondas de truncado) quedan publicadas en una URL pública con registro de peticiones
- [x] Hay una matriz canario × lector en research_notes/text-reading-canaries/results/ para los extractores de referencia y para cada asistente probado
- [ ] El registro de peticiones dice, por asistente, el user agent y qué recursos pidió (HTML, CSS, JS, imágenes, robots.txt)
- [x] Un informe en reports/ propone el filtro full-text/1 con cada regla respaldada por la matriz

## Siguiente paso

Medir Gemini, Perplexity, Claude.ai y Copilot con sesión (prompts/dump.txt); pedir al usuario el access_log de /test-read-canaries/ en dasys.es; decidir intersección o unión; cerrar el informe

## Notas

- 2026-10-29 Extractores de referencia (11) en results/local/index.md. Sonda de chats sin sesión con el Chrome del motor (tools/chats.py probe): ChatGPT, Gemini y Perplexity ofrecen campo de texto; Claude pide login; Copilot (copilot.com/es-es) y Meta AI, sin campo detectado. Alojamiento bloqueado por el entorno: descarga de cloudflared y túnel SSH (localhost.run) denegados; servidor local con registro listo (tools/serve.py, 127.0.0.1:8765). Falta la URL pública.
- 2026-10-29 ChatGPT sin sesión: 2 pasadas iguales y copia literal de 66 líneas (results/chat/chatgpt-20261029T232342.txt). Claude Code WebFetch: Turndown sin script/style ni noscript; trunca a 100.000 caracteres. ChatGPT: primer tramo < 25.000 caracteres. Gemini sin sesión no abre URL; Perplexity pide registro. Informe: reports/Lectura de texto de los asistentes.md (borrador del filtro full-text/1; pendiente decidir intersección o unión).
- 2026-10-29 Gemini Flash con sesión (manual del usuario): recibe HTML depurado (etiquetas + alt, title, href, hidden, aria-*, role, itemprop), sin <title>, head, scripts, class, style, data-*, <form> ni noscript; truncado entre 10.000 y 25.000 como ChatGPT. En BB los hechos están fuera de <form>. Nueva página site/corte.html (sondas QC cada 2.000 de 12.000 a 24.000); clave de index y largo sin cambios (verificado contra lo publicado).
- 2026-10-29 Corte (corte.html): Gemini Flash corta hacia 12.845 caracteres de texto (~14,1 KB de HTML depurado); ChatGPT lee por tramos y en corte.html leyó la página entera (559 líneas); Claude Code, 100.000. Informe actualizado.
