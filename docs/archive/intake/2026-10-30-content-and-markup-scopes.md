# Intake 2026-10-30 · Ámbitos Contenido y Marcado, filtro de lectura Alfa y alcance de lectura

Origen: sesión del 29 y 30-10-2026, tarea T-101 (prueba de canarios). Informes de apoyo, fuera de `docs/`:
- `reports/Lectura de texto de los asistentes.md`: qué reciben ChatGPT, Claude.ai, Claude Code y Gemini Flash al leer una página; matriz, truncado y peticiones al servidor.
- `reports/Estrategia del ámbito Texto.md`: el criterio (§1–§6) y la especificación del filtro Alfa (§7).
- `research_notes/text-reading-canaries/`: páginas de prueba, clave, prompts, respuestas y matriz.

## 1. Decisiones del usuario (citas literales)

1. Sobre los ámbitos, tras la investigación de cómo leen las páginas los sistemas de IA:
   > «y un ambito a cosniderar es el contneido textual (limpiaod el html). Por lo tanot tendriamos 2 ambitos bien definidos: web textual y marcado / en ningn caso tiene sentido evalaur ambos juntos como un html entero.»
2. Sobre la manera de limpiar el HTML (A: texto completo, B: contenido principal) y el `alt`:
   > «1,2. A. Intenta ser lo mas fiel a como lo hacen»
3. Sobre el filtro:
   > «sobre el filtro. Es psoible que lo vayamso cambiando. asique prevelo como un filtro con nombre y version»
4. Sobre la estrategia:
   > «Queiro algo mas omenos estable y con fundamenteo. basado en als pruebas peor que tenga unc rierio adecuado.»
   Claude propuso separar la norma (qué cuenta) del soporte (qué lectores lo reciben): una definición normativa del ámbito y un alcance de lectura medido, como hallazgos sin escala. Descartó la unión, la intersección y la mayoría de lectores. El usuario pidió la especificación del filtro «aplicando tu recomendación» y respondió «ok».
5. Nombres:
   > «Sobre el numple del sistema de filtro lo vamos a denominar por el alfabeto radiofonico. Empezando por la A.»
   > «El ambito que hemos renomabraod de "web" a "texto", lo vmaos a denominar "Contenido"»
   > «Por cierto schema.org pasa a llamrsa "marcado"»
6. Procesar este intake: «si».

## 2. Ámbitos

- **Contenido** sustituye a **Web**. **Marcado** sustituye a **Web Schema.org**. **Catálogos distribuidos** no cambia.
- **Contenido:** el título del documento y el contenido textual de su cuerpo, tal como resultan de analizar la respuesta HTTP con los scripts desactivados, sin el contenido de `<script>` ni `<style>`. Incluye el texto alternativo de las imágenes. No incluye los demás atributos, los metadatos del `<head>` ni lo que solo existe al ejecutar JavaScript.
- **Marcado:** el marcado Schema.org (JSON-LD, microdatos y RDFa) de la misma respuesta HTTP, considerado aisladamente del contenido.
- **Ningún ámbito evalúa el HTML entero.** Contenido no usa el marcado y Marcado no usa el contenido.
- El perfil de consumo sigue siendo uno (la respuesta HTTP sin ejecutar JavaScript). Cada ámbito lee de ella su representación con su filtro de lectura.

## 3. Filtros de lectura

- Un **filtro de lectura** obtiene de la respuesta HTTP la representación que lee un ámbito.
- **Nombre y versión.** Los filtros se nombran con el alfabeto radiofónico, empezando por la A (Alfa, Bravo, Charlie…). La versión es un número: `alfa/1`.
- Cada expediente registra su representación como perfil de consumo + filtro y versión: `audit-es` + `alfa/1`.
- **Criterio normativo.** El filtro se define por la norma (DOM Standard y HTML Living Standard), no por la unión, la intersección o la mayoría de los lectores medidos. Solo cambia de versión si cambia su definición o su lectura de la norma; un cambio de un lector no lo cambia.
- **Alfa** es el filtro del ámbito Contenido. Base normativa:
  - DOM Standard §4.4: el contenido textual de un elemento es su *descendant text content*. No depende de CSS ni de que el elemento se muestre.
  - HTML Living Standard: con los scripts desactivados, el contenido de `<noscript>` es contenido normal; el de `<template>` no forma parte del árbol del documento.
  - HTML §4.8.4.4: el `alt` es «a replacement for the image»; sustituir cada imagen por su `alt` «does not change the meaning of the page».

### Especificación de Alfa (`alfa/1`)

**Entrada:** `response.html` del perfil `audit-es`, con sus bytes originales.

**Análisis:** el analizador del HTML Living Standard, con los scripts desactivados. La codificación sale del Encoding Standard (BOM, cabecera HTTP o `<meta charset>`).

**Salida:** el contenido del documento: el título y el contenido textual del cuerpo, en el orden del documento.

**Entra:**
1. El texto de `<title>`.
2. Todo nodo de texto que desciende de `<body>`, se muestre o no.
3. El contenido de `<noscript>`.
4. El texto de los formularios: `<label>`, `<legend>`, `<button>`, `<option>` y `<textarea>`.
5. El texto de `<svg>`.
6. El `alt` de cada `<img>`, en la posición de la imagen.

**No entra:**
1. El resto de `<head>`.
2. El contenido de `<script>` (de cualquier tipo) y de `<style>`.
3. El contenido de `<template>`.
4. Los comentarios.
5. Los atributos, salvo el `alt` de `<img>`.
6. El contenido de `<iframe>`, `<object>` y `<embed>`.
7. El contenido que genera CSS (`::before`, `::after`).

**Estructura:**
1. Cada bloque empieza en una línea nueva: `p`, `div`, `li`, `h1`–`h6`, `tr`, `dt`, `dd`, `table`, `section`, `article`, `header`, `footer`, `nav`, `aside`, `main`, `figure`, `figcaption`, `form`, `fieldset`, `details`, `summary`, `dialog`, `blockquote`, `pre`, `option`, y `br`.
2. Los títulos `h1`–`h6` llevan su nivel (`#` a `######`).
3. Cada elemento de lista ocupa una línea, con `- `.
4. Cada fila de tabla ocupa una línea, con las celdas separadas por ` | `.
5. `<pre>` conserva sus espacios. En lo demás, los espacios se colapsan.
6. Un enlace queda como su texto.

**Anotaciones de cada fragmento:**

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

**Formato:** JSON con `filter` (`alfa`), `version` (`1`), la ficha de origen, `title`, `text` y `fragments` (`start`, `end`, `text`, `ruta` y sus anotaciones).

## 4. Alcance de lectura

- Es una **dimensión de análisis** aparte, con el mismo patrón que la consistencia transversal: **hallazgos sin escala**. No modifica la disponibilidad efectiva ni el GSC y no se agrega.
- **Unidad:** RI × Contenido con disponibilidad 1. Registra qué lectores del panel reciben los fragmentos que sostienen la disponibilidad y, si alguno no los recibe, por qué (la construcción o la posición respecto al corte medido de ese lector).
- **Panel de lectores:** un conjunto fijo, publicado y fechado de lectores en vivo. Panel 2026-10: ChatGPT sin sesión, Claude.ai, Claude Code y Gemini Flash. Cada pasada de la batería de canarios da una matriz fechada.
- **Corte:** la posición de cada fragmento es un dato medido; el corte es del lector. El 0/1 no depende de ninguno de los dos.

## 5. Enmiendas

- **D-153** (ejecución en dos fases): cada agente recibe la representación de su ámbito (en Contenido, la salida de Alfa; en Marcado, el marcado). El código comprueba las citas contra esa representación. Desaparece «en Web ve juntos el HTML y el Schema.org».
- **D-156 y D-157:** desaparece «de la que se usa todo el documento» y la frontera del documento «el texto del HTML (también el oculto), los atributos y el marcado». Cada ámbito lee su representación con su filtro.
- **D-195:** el `alt` cuenta en Contenido por HTML §4.8.4.4 (regla 6 de Alfa). El `title` de la imagen no cuenta.
- **D-155 y la ficha de ámbito `web.json`:** la ficha de Contenido ya no incluye la localización de Marcado.
- **D-203:** la metadescripción no forma parte del ámbito Contenido.
- **Invariantes 1 y 2** del `CLAUDE.md` raíz: los nombres y la definición de los ámbitos.

## 6. Pendientes

1. El corte de Gemini: si cuenta caracteres de texto o el tamaño de su HTML depurado. Con la segunda lectura, en la ficha del edredón de Burrito Blanco cortaría en el menú.
2. Perplexity en el panel.
3. Cuándo se repite la batería del panel: a petición, al empezar cada tanda de auditorías o con fecha fija.
