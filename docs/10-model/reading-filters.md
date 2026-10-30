---
id: reading-filters
title: Filtros de lectura y alcance de lectura
layer: model
status: vigente
version: 1.1
updated: 2026-10-30
sources: [INTAKE 2026-10-30-content-and-markup-scopes, INTAKE 2026-10-30-pilot-base-sanitation]
---

# Filtros de lectura y alcance de lectura

## Definición

### Filtro de lectura

> - Un **filtro de lectura** obtiene de la respuesta HTTP la representación que lee un ámbito.
> - **Nombre y versión.** Los filtros se nombran con el alfabeto radiofónico, empezando por la A (Alfa, Bravo, Charlie…). La versión es un número: `alfa/1`.
> - Cada expediente registra su representación como perfil de consumo + filtro y versión: `audit-es` + `alfa/1`.
>
> — INTAKE 2026-10-30-content-and-markup-scopes

### Alfa, el filtro del ámbito Contenido

> **Contenido:** el título del documento y el contenido textual de su cuerpo, tal como resultan de analizar la respuesta HTTP con los scripts desactivados, sin el contenido de `<script>` ni `<style>`. Incluye el texto alternativo de las imágenes. No incluye los demás atributos, los metadatos del `<head>` ni lo que solo existe al ejecutar JavaScript. — INTAKE 2026-10-30-content-and-markup-scopes

Alfa (`alfa/1`) produce esa representación ([D-221](../30-governance/decisions.md#d-221)). Su especificación operativa está en [filter-alfa](../20-methods/audit-gsc/filter-alfa.md). El ámbito se define en [evaluation-scopes](evaluation-scopes.md#ámbitos-de-evaluación).

### Alcance de lectura

> - Es una **dimensión de análisis** aparte, con el mismo patrón que la consistencia transversal: **hallazgos sin escala**. No modifica la disponibilidad efectiva ni el GSC y no se agrega.
> - **Unidad:** RI × Contenido con disponibilidad 1. Registra qué lectores del panel reciben los fragmentos que sostienen la disponibilidad y, si alguno no los recibe, por qué (la construcción o la posición respecto al corte medido de ese lector).
> - **Panel de lectores:** un conjunto fijo, publicado y fechado de lectores en vivo. Panel 2026-10: ChatGPT sin sesión, Claude.ai, Claude Code y Gemini Flash. Cada pasada de la batería de canarios da una matriz fechada.
> - **Corte:** la posición de cada fragmento es un dato medido; el corte es del lector. El 0/1 no depende de ninguno de los dos.
>
> — INTAKE 2026-10-30-content-and-markup-scopes

## Reglas e invariantes

1. **Criterio normativo.** El filtro se define por la norma (DOM Standard y HTML Living Standard), no por la unión, la intersección ni la mayoría de los lectores medidos. La auditoría no toma como patrón un agente concreto ([ai-functions](ai-functions.md#fundamento-interpretación-y-utilización-por-sistemas-de-ia)).
2. **Estabilidad.** Un filtro solo cambia de versión si cambia su definición o su lectura de la norma. Si un lector cambia, cambia el alcance, no el filtro.
3. **La letra nombra el filtro y el número, su versión** (interpretación adoptada en D-221). Una corrección de Alfa es `alfa/2`. Otro planteamiento, como el contenido principal, es un filtro nuevo: Bravo.
4. **Sin corte.** El filtro entrega el texto entero. La posición de cada fragmento queda anotada.
5. **La disponibilidad se decide sobre la representación del filtro** ([effective-availability](effective-availability.md)). El alcance de lectura no la cambia, ni el GSC, ni se agrega ([D-222](../30-governance/decisions.md#d-222)).
6. **El alcance es de Contenido.** En Marcado, ningún lector del panel recibe el JSON-LD ni los `<meta itemprop content>`; de los microdatos del cuerpo, solo Gemini recibe los atributos. El alcance de Marcado no se mide con este panel (interpretación adoptada en D-222).

## Distinciones

- **Filtro de lectura frente a perfil de consumo.** El [perfil de consumo](evaluation-scopes.md#perfil-de-consumo-no-interactivo) dice cómo se obtiene la respuesta (sin JavaScript, estado limpio, `es-ES`). El filtro dice qué lee un ámbito de esa respuesta.
- **Contenido frente a texto visible.** El texto visible depende de CSS y de que el elemento se muestre (`innerText`). Contenido incluye lo oculto, como lo reciben casi siempre los lectores en vivo medidos (el atributo `hidden`, 3 de 4).
- **Contenido frente a contenido principal.** Un extractor de contenido principal (Readability) descarta la cabecera, el menú, el pie, los `aside`, los formularios y lo oculto. Contenido los incluye. Su posición y su región quedan anotadas.
- **Alcance de lectura frente a disponibilidad efectiva.** La disponibilidad dice si la información pertinente está en la representación del ámbito. El alcance dice qué lectores del panel la reciben.
- **Alcance de lectura frente a consistencia transversal.** Las dos son hallazgos sin escala. La consistencia compara lo que dicen dos ámbitos; el alcance compara lo que reciben los lectores de un ámbito.

## Interpretación

### Base normativa de Alfa

- **DOM Standard §4.4:** el contenido textual de un elemento es su *descendant text content*, la concatenación de sus nodos de texto. No depende de CSS ni de que el elemento se muestre.
- **HTML Living Standard:** con los scripts desactivados, el contenido de `<noscript>` se analiza como contenido normal. El de `<template>` no forma parte del árbol del documento.
- **HTML §4.8.4.4:** el `alt` es «a replacement for the image», y sustituir cada imagen por su `alt` «does not change the meaning of the page».

### Reglas de Alfa y evidencia del panel 2026-10

La evidencia es el número de lectores del panel que coinciden con la regla (de 4). Procede de la batería de canarios de T-101.

| Regla | Base | Lectores que coinciden |
|---|---|---|
| Entra el texto del `<body>`, también el oculto por CSS, `hidden`, `aria-hidden` o `inert` | DOM §4.4 | 4 (`hidden`: 3) |
| Entran la cabecera, el menú, los `aside` y el pie | Contenido del cuerpo | 4 |
| Entra el texto de formularios: `<label>`, `<button>`, `<textarea>`, `<option>` | Nodos de texto del cuerpo | etiquetas y botones: 3; `<option>`: 2 |
| Entra `<noscript>` | Análisis sin scripts | 1 |
| Entra el texto de `<svg>` | Nodos de texto del cuerpo | 2 |
| Entra el `<title>` | Título del documento | 3 |
| Entra el `alt` de `<img>` | HTML §4.8.4.4 | 3 |
| No entran `<script>` (JSON-LD incluido) ni `<style>` | No son texto del documento | 4 |
| No entra `<template>` | Fuera del árbol del documento | 4 |
| No entran los atributos `title`, `aria-label`, `placeholder`, `value`, `data-*` ni `content` | Atributos, no contenido; el `alt` es la excepción normativa | `title`: 3; `placeholder`: 3; los demás: 4 |
| No entran la meta descripción ni Open Graph | Metadatos del `<head>` | 3 |
| No entra lo que solo aparece al ejecutar JavaScript | [D-156](../30-governance/decisions.md#d-156) | 4 |

Donde la evidencia es baja (`<noscript>`, `<option>`, `<svg>`), la regla la decide la norma. La diferencia con cada lector es alcance de lectura.

## Ejemplo mínimo

Ficha del edredón de Burrito Blanco (T-101). La composición, las medidas, el envío y las devoluciones están en paneles `<aside role="dialog" aria-hidden="true" inert>`.
- **Contenido:** disponibilidad 1. Alfa los incluye, con la anotación `oculto`.
- **Alcance:** por la construcción, los reciben los 4 lectores del panel 2026-10. Por la posición, con la implementación alfa/1 sobre la ficha audit-es del piloto (`audit-bb-edredon-6172`; texto de 14.208 caracteres), la composición empieza en el carácter 9.638 (INTAKE 2026-10-30-pilot-base-sanitation): con la primera lectura del corte de Gemini Flash (unos 12.800 caracteres de texto) la recibe; con la segunda (el tamaño de su HTML depurado), no ([OQ-88](../30-governance/open-questions.md#d-auditoría-informativa-localización-evidencias-gsc)).

Caso hipotético: si la política de devoluciones solo estuviera en una pestaña con `hidden`, la disponibilidad seguiría siendo 1. El hallazgo de alcance diría que Claude.ai no la recibe.

## Pendiente

- Si el corte de Gemini cuenta caracteres de texto o el tamaño de su HTML depurado: [OQ-88](../30-governance/open-questions.md#d-auditoría-informativa-localización-evidencias-gsc).
- Perplexity en el panel: [OQ-89](../30-governance/open-questions.md#d-auditoría-informativa-localización-evidencias-gsc).
- Cuándo se repite la batería del panel: [OQ-90](../30-governance/open-questions.md#d-auditoría-informativa-localización-evidencias-gsc).

## Relacionado

- [evaluation-scopes](evaluation-scopes.md)
- [effective-availability](effective-availability.md)
- [ai-functions](ai-functions.md)
- [filter-alfa](../20-methods/audit-gsc/filter-alfa.md)
