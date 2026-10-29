# Estrategia del ámbito Texto: un criterio estable para lectores que divergen

> **Nombres adoptados el 30-10-2026:** el ámbito que aquí se llama «Texto» se llama **Contenido** (`content`), y el filtro `full-text/1` se llama **Alfa** (`alfa/1`). Los filtros se nombran con el alfabeto radiofónico, empezando por la A.

Continúa [Lectura de texto de los asistentes](Lectura%20de%20texto%20de%20los%20asistentes.md) (T-101). La prueba midió cuatro lectores en vivo: ChatGPT, Claude.ai, Claude Code y Gemini Flash. Coinciden en lo esencial y difieren en 18 construcciones. Este informe propone el criterio que fija qué es el ámbito Texto, para que sea estable, tenga fundamento y siga apoyado en las pruebas.

## 1. El problema

- **Los lectores divergen y cambian sin aviso.** Claude.ai y Claude Code, del mismo proveedor, difieren en tres construcciones. Un proveedor puede cambiar su extractor mañana.
- **El canon no deja tomar un agente como patrón.**
  - [ai-functions](../docs/10-model/ai-functions.md#fundamento-interpretación-y-utilización-por-sistemas-de-ia): «la auditoría **no toma como patrón** la ejecución de un modelo o agente específico».
  - [scope](../docs/00-context/scope.md#límite-de-interpretación): el estudio «no mide el comportamiento […] de un agente de IA particular».
- **La disponibilidad es binaria y no admite umbrales inventados** (invariantes 3 y 7).

Con eso, las dos opciones que planteé antes fallan:

| Opción | Qué haría | Por qué no vale |
|---|---|---|
| **Unión** de los lectores (la recomendé antes) | Cuenta lo que recibe alguno | Define el ámbito por cuatro productos concretos. Mete en Texto la meta descripción porque la recibe Claude.ai, y el `noscript` porque lo recibe ChatGPT. Cambia cada vez que un lector añade algo. |
| **Intersección** | Cuenta lo que reciben todos | También toma los productos como patrón, y lo hace con el más restrictivo de cada construcción. Una pestaña con `hidden` daría 0 aunque tres de los cuatro la reciban. Cambia cada vez que un lector quita algo. |
| **Mayoría** (p. ej. 3 de 4) | Cuenta lo que reciben casi todos | Es un umbral inventado. |

En las tres, la nota del comercio dependería del comportamiento de agentes concretos. Retiro la recomendación de la unión.

## 2. Qué hacen otros con consumidores que divergen

- **Herramientas de auditoría SEO y GEO.** Usan una sola representación genérica: el HTML de la respuesta sin ejecutar JavaScript, reducido a texto. Comprueban aparte el acceso por bot (robots.txt, bloqueos). No modelan el extractor de cada IA ([encited](https://encited.com/free-tools/seo-audit), [seomator](https://seomator.com/geo-audit-tool), [justidea](https://justidea.agency/en/blog/top-5-seo-crawlers-for-technical-audits/)).
- **WCAG (accesibilidad).** Sus criterios son normativos e independientes de cualquier lector de pantalla. Aparte está el concepto de **«accessibility supported»**: una técnica solo vale para cumplir si consta que la soportan las tecnologías de apoyo, y ese soporte se documenta con pruebas. WCAG no fija qué grado de soporte basta ([W3C, Documenting Accessibility Support](https://www.w3.org/WAI/WCAG21/Understanding/documenting-accessibility-support)).
- **Baseline (plataforma web).** Hay un **conjunto fijo y publicado** de navegadores (Chrome, Edge, Firefox y Safari, de escritorio y móviles). Una función es «Baseline» cuando todos la soportan; si no, tiene «disponibilidad limitada». El estado está fechado y se revisa ([web.dev/baseline](https://web.dev/baseline), [definición](https://web.dev/blog/baseline-definition-update)).
- **Google.** El contenido oculto en pestañas y acordeones por diseño «should have full weight» en la indexación móvil. Lo que se penaliza es el texto oculto para engañar ([SEJ, Mueller](https://www.searchenginejournal.com/googles-mueller-on-myth-of-hidden-tab-content/358724/)).

**El patrón común es separar dos cosas:**
- **la norma:** qué cuenta, definido de forma estable y sin depender de un consumidor;
- **el soporte:** qué consumidores lo reciben, medido con un conjunto fijo, documentado y fechado.

El soporte informa, pero no redefine la norma.

## 3. Propuesta: definición normativa + alcance de lectura medido

### Capa 1. Definición del ámbito Texto (condición adoptada, como D-156)

> **Texto** es el título del documento y el contenido textual de su cuerpo, tal como resultan de analizar la respuesta HTTP con los scripts desactivados, sin el contenido de `<script>` ni `<style>`. Incluye el texto alternativo de las imágenes. No incluye los demás atributos, los metadatos del `<head>` ni lo que solo existe al ejecutar JavaScript.

Base normativa:
- **DOM Standard §4.4:** el contenido textual de un elemento es su *descendant text content*, la concatenación de sus nodos de texto. No depende de CSS ni de que el elemento se muestre.
- **HTML Living Standard:** con los scripts desactivados, el contenido de `<noscript>` es contenido normal. El de `<template>` no forma parte del árbol del documento.
- **HTML §4.8.4.4:** el `alt` es «a replacement for the image», con la intención de que sustituir cada imagen por su `alt` «does not change the meaning of the page».

Reglas, con su base y la evidencia de la prueba:

| Regla | Base normativa | Lectores que coinciden (de 4) |
|---|---|---|
| Entra el texto del `<body>`, también el oculto por CSS, `hidden`, `aria-hidden` o `inert` | DOM §4.4: el texto no depende de mostrarse | 4 (`hidden`: 3) |
| Entran la cabecera, el menú, los `aside` y el pie | Son contenido del cuerpo | 4 |
| Entra el texto de formularios: `<label>`, `<button>`, `<textarea>`, `<option>` | Nodos de texto del cuerpo | etiquetas y botones: 3; `<option>`: 2 |
| Entra `<noscript>` | Perfil sin scripts: contenido normal | 1 |
| Entra el texto de `<svg>` | Nodos de texto del cuerpo | 2 |
| Entra el `<title>` | Título del documento | 3 |
| Entra el `alt` de `<img>` | HTML §4.8.4.4: sustituye a la imagen | 3 |
| No entran `<script>` (JSON-LD incluido) ni `<style>` | No son texto del documento | 4 |
| No entra `<template>` | Fuera del árbol del documento | 4 |
| No entran los atributos `title`, `aria-label`, `placeholder`, `value`, `data-*` ni `content` | Son atributos, no contenido. El `alt` es la excepción normativa. | `title`: 3; `placeholder`: 3; los demás: 4 |
| No entran la meta descripción ni Open Graph | Metadatos del `<head>` en atributos | 3 |
| No entra lo que solo aparece al ejecutar JavaScript | D-156 | 4 |
| Sin truncado | La norma no corta; el corte es de cada lector | — |

El filtro **`full-text/1`** implementa esta definición. Solo cambia de versión si cambia la definición o su lectura de la norma, no porque un lector cambie.

### Capa 2. Alcance de lectura: hallazgos sin escala

Es una dimensión de análisis aparte, con el mismo patrón que la consistencia transversal ([D-124](../docs/30-governance/decisions.md#d-124)). Son hallazgos sin escala que no modifican la disponibilidad ni el GSC.

- **Por cada RI × Texto con disponibilidad 1:** qué lectores del panel reciben los fragmentos que la sostienen y, si alguno no los recibe, por qué. Ejemplo: «La política de devoluciones solo está en una pestaña con `hidden`. No la recibe Claude.ai (panel 2026-10).»
- **Causas registradas por construcción,** según la matriz del panel: `hidden`, formulario, `<option>`, `noscript`, `svg`, `alt`, `<title>`, migas, relacionados, y la posición respecto al corte medido de cada lector (Gemini, unos 12.800 caracteres).
- **Panel de lectores versionado:** `panel/2026-10` = ChatGPT sin sesión, Claude.ai, Claude Code y Gemini Flash, más Perplexity cuando se mida. La batería de canarios ([research_notes/text-reading-canaries/](../research_notes/text-reading-canaries/)) se repite y cada pasada da una matriz fechada. Es el equivalente del conjunto de navegadores de Baseline y de la documentación de soporte de WCAG.
- **El informe** puede decir «la información está publicada como texto, pero solo la reciben 2 de los 4 lectores del panel». Es una recomendación accionable y no cambia la escala.

## 4. Por qué es estable y tiene fundamento

- **Estable:** la definición se apoya en DOM y HTML, que cambian despacio y con versiones. Un cambio de un lector solo cambia el alcance, nunca la disponibilidad ni el GSC.
- **Fundada:** cada regla tiene una base normativa y la confirma la mayoría de los lectores medidos. Las excepciones son reglas que la norma explica, no votaciones: `noscript` y `option` entran por la norma aunque los reciban pocos lectores, y `title` sale por la norma aunque lo reciban tres.
- **Fiel a cómo leen:** es la familia A, la de los cuatro lectores, expresada como norma. Lo que cada uno hace distinto queda medido y a la vista.
- **Coherente con el canon:**
  - no toma ningún agente como patrón (ai-functions, scope);
  - es una condición adoptada, como el perfil sin JavaScript (D-156);
  - la disponibilidad sigue siendo binaria y no hay umbrales (invariantes 3 y 7);
  - el alcance sigue el patrón de la consistencia transversal (D-124);
  - responde a la premisa de FUND §2.3, que la información sirva a «una diversidad de sistemas»: el alcance mide justo eso.

**Límites que se aceptan:**
- Un hecho cuenta como disponible aunque algún lector del panel no lo reciba. El alcance lo deja dicho.
- El texto oculto entra, también el que podría ocultarse para engañar. La anotación `oculto` lo deja visible, y la Fiabilidad sigue leyendo lo publicado con su regla refutadora.

## 5. Efectos en BB

- La composición, las medidas, el lavado, el envío y las devoluciones están en paneles `aside` con `aria-hidden` e `inert`. **Texto: disponibilidad 1.** Alcance: los reciben los cuatro lectores.
- Hallazgo de posición: la composición empieza en el carácter 10.035 y el envío en el 10.625, cerca del corte medido de Gemini (unos 12.800). Un menú más largo los dejaría fuera.

## 6. Decisiones del usuario

1. **Criterio:** definición normativa + alcance de lectura (esta propuesta), frente a la unión o la intersección de lectores.
2. **`alt`:** dentro, por HTML §4.8.4.4. Enmienda D-195, que ya lo contaba.
3. **Recalibración del panel:** a petición, al empezar cada tanda de auditorías o con fecha fija.
4. **Perplexity:** se mide para el panel 2026-10 o queda para el siguiente.

## 7. Especificación del filtro Alfa (`alfa/1`), ámbito Contenido

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

**Formato:** JSON con `filter` (`alfa`), `version` (`1`), la ficha de origen, `title`, `text` y `fragments` (`start`, `end`, `text`, `ruta` y sus anotaciones). Cada expediente registra la representación que usó como `audit-es` + `alfa/1`.
