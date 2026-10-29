# Qué recibe un asistente de IA cuando lee una página

> **Nombres adoptados el 30-10-2026:** el ámbito que aquí se llama «Texto» se llama **Contenido** (`content`), y el filtro `full-text/1` se llama **Alfa** (`alfa/1`). Los filtros se nombran con el alfabeto radiofónico, empezando por la A.

Prueba de canarios del 29-10-2026 (T-101). Se usaron tres páginas publicadas en `https://dasys.es/test-read-canaries/`:
- una ficha con 58 construcciones HTML, cada una con un código único;
- una página larga con 7 sondas de posición;
- una página de corte con sondas cada 2.000 caracteres.

Lectores medidos:
- **ChatGPT**, sin sesión, con el Chrome real del motor de PAA: dos pasadas y una copia literal de lo recibido.
- **Claude.ai** (Sonnet 5.5) y **Gemini Flash**, con sesión: prueba manual del usuario.
- **WebFetch de Claude Code.**
- **11 extractores de referencia.**

Material: [research_notes/text-reading-canaries/](../research_notes/text-reading-canaries/). Contiene el generador, la clave `canaries.json`, los prompts, las respuestas (`results/chat/`) y la matriz completa (`results/matrix-index.md`).

## Resultado

- **Los cuatro lectores en vivo reciben el contenido del `<body>`, también casi todo el oculto.** No reciben los scripts (JSON-LD incluido) ni el estilo.
- **Del `<head>`:**
  - ChatGPT y Claude Code reciben solo el `<title>`;
  - Claude.ai recibe además la meta descripción y Open Graph, en un bloque de metadatos;
  - Gemini no recibe nada.
- **La forma de lo recibido cambia con el lector:**
  - ChatGPT: **texto** propio con líneas numeradas;
  - Claude.ai y Claude Code: **Markdown**;
  - Gemini: **HTML depurado** (etiquetas y algunos atributos).
- **Ninguno se parece a Readability** (contenido principal), que pierde la mitad de una ficha real de Burrito Blanco.

## Matriz de los lectores en vivo

✓ llega al modelo · · no llega. ChatGPT, igual en las dos pasadas y confirmado con la copia literal de sus 66 líneas.

| Construcción | ChatGPT | Claude.ai | Claude Code | Gemini Flash | Readability |
|---|---|---|---|---|---|
| Forma de lo recibido | texto con líneas `L0…`, enlaces `【n†texto】`, controles `[Select]`, `[Input: …]`, `[Button: …]` | bloque de metadatos + Markdown con URL absolutas | Markdown | HTML depurado (`<div hidden>`, `<aside aria-hidden=true inert role=dialog>`) | HTML del artículo |
| `h1`, `p`, `li`, `pre`, `dl`, tabla, `figcaption`, `canvas`, texto de enlace | ✓ | ✓ | ✓ | ✓ | ✓ |
| Oculto por CSS: `display:none` (en línea y por clase), `visibility:hidden`, tamaño 0, `sr-only` | ✓ | ✓ | ✓ | ✓ | parcial |
| `aria-hidden`; panel `<aside role=dialog aria-hidden inert>` (patrón de BB); `<dialog>` y `<details>` cerrados | ✓ | ✓ | ✓ | ✓ | · o parcial |
| Microdato con valor en texto | ✓ | ✓ | ✓ | ✓ (con `itemscope` e `itemprop`) | ✓ |
| HTML escapado en un `span` oculto | ✓ | ✓ | ✓ | ✓ | · |
| Cabecera, menú, `aside` lateral, pie | ✓ | ✓ | ✓ | ✓ | · |
| **Atributo `hidden`** (bloque y pestaña `role=tabpanel`) | ✓ | · | ✓ | ✓ | · |
| **`<title>`** | ✓ | ✓ | ✓ | · | · |
| **Meta descripción, Open Graph** | · | ✓ | · | · | · |
| **Migas, productos relacionados** | · | ✓ | ✓ | ✓ | · |
| **`alt` de `<img>`, URL del enlace** | · | ✓ | ✓ | ✓ | ✓ |
| **`title` de `<img>`** | · | · | ✓ | ✓ | ✓ |
| **Atributo `title` de un `span`** | · | · | · | ✓ | · |
| **`<label>`, `<textarea>`, `<button>`** (todo `<form>`) | ✓ | ✓ | ✓ | · | · |
| **Texto de `<option>`** | · (`[Select]`) | ✓ | ✓ | · | · |
| **`placeholder`, `noscript`** | ✓ | · | · | · | · |
| **`<text>` de un `<svg>`** | · | ✓ | ✓ | · | ✓ |
| JSON-LD (cabecera o cuerpo), `<script>` de estado, texto insertado por JavaScript, `<meta itemprop content>`, RDFa en `<meta>`, comentarios, `data-*`, `aria-label`, valores de `input`, `value` de `option`, `iframe srcdoc`, `::before`, `<template>` | · | · | · | · | · |

En negrita, las construcciones en que difieren los lectores.

## Truncado

Se usaron dos páginas: `largo.html` (436 KB, sondas de 2.000 a 400.000 caracteres) y `corte.html` (26.000 caracteres, sondas cada 2.000 de 12.000 a 24.000).

| Lector | Comportamiento medido |
|---|---|
| Gemini Flash | **Corte fijo** hacia el carácter 12.845 del texto: unos 14,1 KB de su HTML depurado. En `corte.html` llega a la sonda de 12.000 y no a la de 14.000. En `largo.html`, a la de 10.000. |
| ChatGPT | **Lectura por tramos.** Recibe la página en líneas y puede pedir más tramos. En `corte.html` los pidió y leyó la página entera (559 líneas, hasta el último párrafo). En `largo.html` (8.502 líneas) se paró antes de la sonda de 25.000. Llegar al final depende de lo que decida el modelo. |
| Claude.ai | **Corte fijo** poco después de los 100.000 caracteres: llega a la sonda de 100.000 y corta a mitad de frase. `corte.html`, entera. |
| Claude Code | **Corte fijo** a los 100.000 caracteres del Markdown, con `[Content truncated due to length...]`. La sonda de 100.000 queda fuera. |

En la ficha del edredón de BB, el texto completo mide unos 14.700 caracteres, y antes de la ficha van unos 3.800 de menú. La composición empieza en el carácter 10.035 y el envío en el 10.625: entran por poco en el corte de Gemini. Una tienda con más menú o más texto antes de la ficha los dejaría fuera. Lo que no llega a Gemini es lo que está más allá de unos 12.800 caracteres de texto, contados desde el principio del `<body>`, menú incluido.

## Peticiones al servidor

Registro de accesos de dasys.es (Plesk), filtrado y con la IP del usuario anonimizada: [results/access/](../research_notes/text-reading-canaries/results/access/access_ssl_log-canaries.txt). Horas en UTC.

| Lector | User agent | Origen | robots.txt | Qué pidió |
|---|---|---|---|---|
| ChatGPT (sin sesión) | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot` | 158.158.5.35–45 | No lo pidió | Solo el documento. Tras `largo.html` pidió también la portada del sitio (`/`). |
| Claude.ai | `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; +claude-user@anthropic.com)` | 160.79.106.x | **Sí, antes de la primera página** | Solo los documentos; siguió la redirección 301 de `/test-read-canaries` a `/test-read-canaries/`. |
| Claude Code (WebFetch) | `Claude-User (claude-code/2.1.312; +https://support.anthropic.com/)` | **La IP del usuario**: la petición sale del equipo local | No lo pidió | Solo los documentos. |
| Gemini Flash (con sesión) | `Google`; antes, seis peticiones simultáneas con `Google-Lens` | 142.250.88.67; Google-Lens desde 66.249.84.x y 66.102.7.x | No lo pidió | Solo los documentos. |

- **Nadie pidió CSS, JS ni imágenes.** La ficha de prueba no tiene subrecursos externos (la imagen es un `data:`), así que esto no prueba que no los pidan. Concuerda, eso sí, con las mediciones publicadas (Ripa, Vercel).
- **Solo Claude.ai consulta robots.txt.** Concuerda con lo documentado: Claude-User respeta robots.txt; ChatGPT-User y los fetchers a petición de Google, en general, no.
- **Ningún rastreador de índice** (Googlebot, Bingbot, OAI-SearchBot, PerplexityBot) pidió las páginas de prueba.
- **Claude Code lee desde la máquina del usuario,** con su IP y su red. En la auditoría eso importa: su lectura es la del perfil de red local, no la de un centro de datos.

## Lo que confirma y lo que cambia

- **Confirma la tesis del usuario.** El marcado no llega con el texto. Ningún lector recibe el JSON-LD. Gemini recibe los atributos de microdatos del cuerpo, pero no los `<meta itemprop content>`.
- **Confirma la familia A.** Lo oculto llega. En BB, la composición, las medidas, el lavado, el envío y las devoluciones están en paneles `aside` con `aria-hidden` e `inert`, y los cuatro lectores los reciben.
- **El atributo `hidden` es frágil.** Claude.ai descarta lo que lleva `hidden`, y las pestañas ocultas con ese atributo son habituales en las fichas. Si una tienda pone el envío en una pestaña con `hidden`, Claude.ai no lo recibe.
- **Cambia D-195.** El `alt` llega a Claude y a Gemini, pero no a ChatGPT.
- **Los controles dependen del lector.**
  - Gemini descarta el `<form>` entero.
  - ChatGPT conserva las etiquetas, pero no las opciones de un `<select>`.
  - En BB, los hechos de la ficha están fuera de los `<form>`: solo cae un precio. En una tienda con las variantes y el precio dentro del formulario de compra (p. ej. el tema por defecto de PrestaShop), Gemini no los recibiría.
- **La meta descripción llega a un lector.** Claude.ai la recibe en un bloque aparte. Afecta a D-203, la prominencia en `title`, metadescripción y `H1`.
- **No hay un extractor estándar.** Cada asistente tiene el suyo: Claude.ai y Claude Code, del mismo proveedor, difieren en el `hidden`, el `title` de imagen y los metadatos. Esto apoya un filtro con nombre y versión, recalibrado con esta prueba.

## Propuesta del filtro `full-text/1` (ámbito Texto)

Entrada: `response.html` del perfil `audit-es`. Salida: texto con fragmentos anotados.

1. **Base común (los cuatro lectores):** todo nodo de texto del `<body>`, también el oculto por CSS, `aria-hidden` o `inert`, el de `<dialog>` y `<details>`, la cabecera, el menú, los `aside` y el pie.
2. **No entra en ningún lector:** todo `<script>`, `<style>`, `<template>`, los comentarios, `iframe`, `::before` y `::after`, y los atributos `data-*`, `aria-label`, `value` y `content` del cuerpo.
3. **Discrepantes,** con la anotación de los lectores que los reciben (`chatgpt`, `claude-ai`, `claude-code`, `gemini`):
   - atributo `hidden`;
   - `<title>`, meta descripción, Open Graph;
   - migas, productos relacionados;
   - `alt` y `title` de imagen, atributo `title`, URL de enlace;
   - contenido de `<form>`, texto de `<option>`, `placeholder`;
   - `noscript`, `svg`.
4. **Estructura:** saltos de bloque, títulos, elementos de lista y filas de tabla en una línea con sus celdas separadas.
5. **Anotaciones sin efecto en la escala:**
   - `oculto`, `región` y `control`;
   - la posición en caracteres;
   - `más allá del corte de Gemini` (≈12.800 caracteres), un dato medido y versionado con el filtro.

**Decisión pendiente:** la base de la disponibilidad efectiva para lo discrepante.
- **Intersección:** cuenta lo que reciben todos los lectores medidos.
- **Unión:** cuenta lo que recibe alguno.

En los dos casos la diferencia queda como hallazgo y no hay un tercer valor (invariante 3).

## Pendiente

- Perplexity con sesión (prompt `prompts/dump.txt`).
- Una ficha con subrecursos externos (CSS, JS, imagen), para comprobar si algún lector los pide.
- Consumidores de índice (Google, Bing): necesitan tiempo de indexación. Quedan fuera de esta prueba.
