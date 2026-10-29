---
id: audit-gsc-filter-alfa
title: Filtro Alfa y alcance de lectura (operativa)
layer: method
status: propuesta
version: 0.1
updated: 2026-10-30
sources: [INTAKE 2026-10-30-content-and-markup-scopes]
---

# Filtro Alfa y alcance de lectura (operativa)

> **Estado: propuesta V1** ([D-221](../../30-governance/decisions.md#d-221), [D-222](../../30-governance/decisions.md#d-222)). El canon está en [reading-filters](../../10-model/reading-filters.md). Este módulo da la especificación operativa de `alfa/1` y el procedimiento del alcance de lectura. No crea conceptos, escalas ni indicadores.

## Especificación de Alfa (`alfa/1`)

**Entrada:** `response.html` del perfil `audit-es`, con sus bytes originales.

**Análisis:** el analizador del HTML Living Standard, con los scripts desactivados. La codificación sale del Encoding Standard (BOM, cabecera HTTP o `<meta charset>`).

**Salida:** el contenido del documento: el título y el contenido textual del cuerpo, en el orden del documento.

### Entra

1. El texto de `<title>`.
2. Todo nodo de texto que desciende de `<body>`, se muestre o no.
3. El contenido de `<noscript>`.
4. El texto de los formularios: `<label>`, `<legend>`, `<button>`, `<option>` y `<textarea>`.
5. El texto de `<svg>`.
6. El `alt` de cada `<img>`, en la posición de la imagen.

### No entra

1. El resto de `<head>`.
2. El contenido de `<script>` (de cualquier tipo) y de `<style>`.
3. El contenido de `<template>`.
4. Los comentarios.
5. Los atributos, salvo el `alt` de `<img>`.
6. El contenido de `<iframe>`, `<object>` y `<embed>`.
7. El contenido que genera CSS (`::before`, `::after`).

### Estructura

1. Cada bloque empieza en una línea nueva: `p`, `div`, `li`, `h1`–`h6`, `tr`, `dt`, `dd`, `table`, `section`, `article`, `header`, `footer`, `nav`, `aside`, `main`, `figure`, `figcaption`, `form`, `fieldset`, `details`, `summary`, `dialog`, `blockquote`, `pre`, `option`, y `br`.
2. Los títulos `h1`–`h6` llevan su nivel (`#` a `######`).
3. Cada elemento de lista ocupa una línea, con `- `.
4. Cada fila de tabla ocupa una línea, con las celdas separadas por ` | `.
5. `<pre>` conserva sus espacios. En lo demás, los espacios se colapsan.
6. Un enlace queda como su texto.

### Anotaciones de cada fragmento

| Anotación | Valor |
|---|---|
| `posicion` | Carácter de inicio y de fin en el contenido |
| `ruta` | Ruta del elemento en el documento |
| `oculto` | Dentro de `hidden`, `aria-hidden="true"`, `inert`, `style` con `display:none` o `visibility:hidden`, `<dialog>` sin `open`, o `<details>` cerrado (fuera de su `<summary>`) |
| `region` | Dentro de `header`, `nav`, `footer` o `aside`, o de un elemento con `role` `banner`, `navigation`, `contentinfo` o `complementary` |
| `control` | Dentro de `form`, `select`, `button`, `textarea` o `label` |
| `alt` | Procede del atributo `alt` |
| `enlace` | URL absoluta del enlace |

**Corte:** ninguno.

**Formato:** JSON con `filter` (`alfa`), `version` (`1`), la ficha de origen, `title`, `text` y `fragments` (`start`, `end`, `text`, `ruta` y sus anotaciones). Cada expediente registra su representación como `audit-es` + `alfa/1` ([D-199](../../30-governance/decisions.md#d-199): JSON validado y versionado).

## Uso en la auditoría

- La [fase 1 y la fase 2](execution.md#ejecución-en-dos-fases) de Contenido leen la salida de Alfa, no el HTML ([D-223](../../30-governance/decisions.md#d-223)).
- Una evidencia de Contenido cita el texto literal de un fragmento ([evidence](evidence.md)). El código comprueba que el texto citado existe en la salida de Alfa ([QA-15](qa.md#validaciones-obligatorias-qa-01-a-qa-15)).
- Las anotaciones no cambian la disponibilidad. Un fragmento `oculto`, de `region` o de `control` da disponibilidad como cualquier otro.

## Alcance de lectura (operativa)

### Panel 2026-10

| Lector | Cómo se midió | Forma de lo que recibe | Corte medido |
|---|---|---|---|
| ChatGPT, sin sesión | Chrome del motor de PAA; dos pasadas y copia literal | Texto con líneas numeradas | Por tramos; el modelo decide si pide más |
| Claude.ai (Sonnet 5.5), con sesión | Prueba manual | Bloque de metadatos + Markdown | Poco después de 100.000 caracteres |
| Claude Code (WebFetch) | Desde el equipo local, con su IP y su red | Markdown | 100.000 caracteres |
| Gemini Flash, con sesión | Prueba manual | HTML depurado | Unos 12.800 caracteres de texto en una página casi sin etiquetas (⚠ [OQ-88](../../30-governance/open-questions.md#d-auditoría-informativa-localización-evidencias-gsc)) |

La matriz construcción × lector, las páginas de prueba y las respuestas están en `research_notes/text-reading-canaries/` (fuera de `docs/`). El informe es `reports/Lectura de texto de los asistentes.md`.

### Cómo se registra

1. Para cada RI × Contenido con disponibilidad 1, toma los fragmentos que la sostienen.
2. Para cada fragmento, busca en la matriz del panel la construcción de la que sale: `hidden`, `<form>`, `<option>`, `<noscript>`, `<svg>`, `alt`, `<title>`, migas o relacionados.
3. Compara su `posicion` con el corte medido de cada lector.
4. Registra qué lectores del panel reciben los fragmentos y, si alguno no los recibe, la causa (la construcción o la posición).
5. Registra la fecha de la matriz del panel con cada hallazgo.

Ejemplo (hipotético): «Devoluciones: la única respuesta está en una pestaña con `hidden`. No la recibe Claude.ai (panel 2026-10).»

### Recalibración

- La batería de canarios se repite con los mismos generador y clave (`generate.py`, `canaries.json`). Cada pasada da una matriz fechada.
- Cuándo se repite queda abierto: [OQ-90](../../30-governance/open-questions.md#d-auditoría-informativa-localización-evidencias-gsc).

## Relacionado

- [reading-filters](../../10-model/reading-filters.md)
- [execution](execution.md#ejecución-en-dos-fases)
- [availability-coverage](availability-coverage.md)
- [dossier](dossier.md)
