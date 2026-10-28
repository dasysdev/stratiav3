# Inventario de fuentes

Función y estado de cada fuente de la referencia técnica de Web Schema.org y de Web.

- **Origen:** el inventario de partida del estudio de Schema.org (códigos SCH, GSC, GMC, W3C, GS1, VAL y SKL; T-044), más los huecos detectados al planificar web-audit. Las de Web (columna **Inv.** `D-159`) salen del perfil de Web, construido sobre el documento base de 19 requisitos técnicos del HTML (T-072).
- **Dónde está cada dato:**
  - título, editor y URL: [references/sources.json](../../references/sources.json);
  - versión fijada: `references/var/pins.json`;
  - clase, nivel y citas: la ficha de cada fuente (`cards/`).
- **Clases y niveles:** los del canon. Clases de fuente, [D-132](../../docs/30-governance/decisions.md#d-132); niveles del perfil, [D-130](../../docs/30-governance/decisions.md#d-130) (Web Schema.org) y [D-159](../../docs/30-governance/decisions.md#d-159) (Web).
- **Estado:** a 2026-10-27, primera pasada (T-047), con el informe en [reports/2026-10-27-primera-pasada.md](reports/2026-10-27-primera-pasada.md). El 2026-10-28 se retiraron 118 requisitos (T-055, [reports/2026-10-28-retirada.md](reports/2026-10-28-retirada.md)); quedan en [retired.json](retired.json) y no cuentan en **Req.** El 2026-10-28, el perfil de Web (T-072): 19 fuentes nuevas y 22 requisitos, con el informe en [reports/2026-10-28-perfil-web.md](reports/2026-10-28-perfil-web.md); su triaje (T-073, [reports/2026-10-28-triaje-web.md](reports/2026-10-28-triaje-web.md)) deja 12. Con las vistas y los sitemaps (T-074, [reports/2026-10-28-vistas-sitemaps.md](reports/2026-10-28-vistas-sitemaps.md)), 23, y `w-consumer/014`, que funda una condición del proyecto (D-162) y no una fuente.

## Especificaciones aplicables

**Req.** = requisitos con esa especificación como `spec`: obligatorios / recomendados.

### Serialización

| Fuente | Inv. | Función | Citas | Req. |
|---|---|---|---|---|
| `w3c-json-ld11` | W3C-01 | Gramática de JSON-LD 1.1 e incrustación en HTML. | 32 | 17 / 1 |
| `w3c-json-ld11-api` | hueco | Procesado de JSON-LD (contexto, expansión, errores). Sus MUST son del procesador; sirve para el método y como cita adicional. | 19 | — |
| `whatwg-html-microdata` | hueco | Microdata (HTML Living Standard, sección 5): items, itemprop, itemtype, itemid e itemref. | 18 | 18 / 0 |
| `w3c-rdfa-core` | hueco | RDFa Core 1.1: CURIE, IRI y literales. | 10 | 1 / 2 |
| `w3c-html-rdfa` | hueco | RDFa en HTML: conformidad de documento. | 8 | 3 / 2 |

### Vocabulario (Schema.org 30.1)

| Fuente | Inv. | Función | Citas | Req. |
|---|---|---|---|---|
| `schemaorg` | hueco | La release 30.1 en formato máquina (congelada en T-045). Definiciones de tipos y propiedades. | 10 | 0 / 7 |
| `schemaorg-data-model` | SCH-02 | Modelo de datos: rangos, dominios y conformidad. | 7 | 0 / 2 |
| `schemaorg-getting-started` | SCH-01 | Guía de marcado: tipos esperados frente a texto y contenido visible. | 5 | — |
| `schemaorg-faq` | SCH-04 | Preguntas frecuentes: contenido oculto y espacios de nombres. | 3 | — |
| `schemaorg-full-hierarchy` | SCH-03 | Jerarquía de tipos; vista de la release. | 1 | — |
| `schemaorg-product`, `-productgroup`, `-offer`, `-organization` | SCH-05–08 | Páginas de tipo; vistas de la release, sin condiciones propias. | 2 c/u | — |

Schema.org es permisivo por diseño: todos los requisitos de este nivel son recomendados.

### Consumidor (Google Search)

| Fuente | Inv. | Función | Citas | Req. |
|---|---|---|---|---|
| `google-search-merchant-listing` | GSC-02 | Fichas de comerciante: Product, Offer y sus tipos anidados (precio, envío, devoluciones, certificación…). | 124 | 63 / 49 |
| `google-search-product-snippet` | hueco | Fragmentos de producto: Product, Review, AggregateRating y Offer. | 31 | 11 / 10 |
| `google-search-review-snippet` | tipos reales | Propiedades de Review y AggregateRating. Entra por remisión de las filas `review` y `aggregateRating` de las dos anteriores. | 35 | 23 / 5 |
| `google-search-product-variants` | GSC-03 | Variantes: ProductGroup, hasVariant, variesBy, productGroupID. | 27 | 9 / 8 |
| `google-search-return-policy` | GSC-04 | Política de devoluciones a nivel de organización. | 37 | 13 / 13 |
| `google-search-shipping-policy` | GSC-05 | Política de envío a nivel de organización (ShippingService). | 69 | 32 / 14 |
| `google-search-organization` | GSC-06 | Organization: identidad, contacto, logo y dirección. | 38 | 4 / 8 |
| `google-search-sd-policies` | GSC-01 | Directrices generales. Entran por remisión: las fichas de comerciante y los fragmentos de producto exigen seguirlas. | 9 | 5 / 2 |
| `google-search-javascript` | hueco | Marcado generado con JavaScript. Fija el método: Google procesa el marcado del DOM renderizado. | 3 | — |

## Especificaciones aplicables de Web

**Req.** = requisitos de Web con esa especificación como `spec`: obligatorios / recomendados.

### Protocolo

| Fuente | Inv. | Función | Citas | Req. |
|---|---|---|---|---|
| `ietf-rfc9110` | D-159 | HTTP Semantics: la respuesta (estado, cabeceras). Sus tres requisitos (`Location`, `Content-Type`, `Content-Encoding`) no se auditan (triaje Web). | 14 | — |
| `sitemaps-org-protocol` | D-162 | Protocolo de sitemaps: forma del sitemap XML y del índice, codificación, escape, límites y URL válidas según su ubicación (vista general). | 17 | 9 / 0 |
| `ietf-rfc9309` | D-159 | Robots Exclusion Protocol: cómo se leen las reglas de robots.txt (método común de Web, punto 3). Sus MUST son del rastreador. | 18 | — |

### Documento

| Fuente | Inv. | Función | Citas | Req. |
|---|---|---|---|---|
| `whatwg-html-semantics` | D-159, D-168 | Declaración de la codificación de caracteres (4.2.5.4): `meta charset` y `http-equiv`. La etiqueta y la posición no se auditan (triaje Web). El elemento `title` (4.2.1 y 4.2.2), dato del mínimo de representación. | 13 | 4 / 0 |
| `whatwg-html-syntax` | D-159 | Sintaxis del documento (13.1): partes, orden y DOCTYPE. El DOCTYPE no se audita (triaje Web). | 7 | — |
| `whatwg-html-links` | D-159 | `href` de `a` y `area`: una URL válida. No se audita: es rastreo del sitio (triaje Web). | 2 | — |
| `whatwg-html-parsing` | D-159 | Análisis (13.2): errores de análisis y el límite de 1024 bytes. Sus must son del analizador y del validador, no del documento. | 6 | — |
| `whatwg-encoding` | D-159 | UTF-8 y sus etiquetas. Apoya los requisitos de HTML. | 3 | — |
| `ogp-protocol` | D-168 | Open Graph, condicional: si la página lo usa, `og:title`, `og:type`, `og:image` y `og:url`, y `og:url` igual a la canónica. Sin tipo de producto. | 6 | 5 / 0 |

### Consumidor (Google Search y operadores de IA)

| Fuente | Inv. | Función | Citas | Req. |
|---|---|---|---|---|
| `google-search-technical-requirements` | D-159 | Search Essentials: Googlebot no bloqueado, HTTP 200 y contenido indexable. | 7 | 7 / 0 |
| `google-search-links-crawlable` | D-159 | Enlaces rastreables: `<a href>` con una dirección web. No se audita: es rastreo del sitio (triaje Web). | 10 | — |
| `google-search-sd-policies` | GSC-01 | Directrices generales de datos estructurados (también en Web Schema.org): presencia del marcado. | 9 | 1 / 0 |
| `google-crawling-robots-txt` | D-159 | Lectura de robots.txt por Google (método de `w-consumer/009`) y el campo `sitemap:`. | 19 | 1 / 0 |
| `google-search-sitemaps-build` | D-162 | Guía de sitemaps de Google: repite el protocolo (redundante). | 4 | — |
| `google-search-sitemaps-overview` | D-162 | Cuándo conviene un sitemap: no exige ni recomienda tenerlo. | 2 | — |
| `google-search-robots-meta` | D-159 | Meta robots y `X-Robots-Tag` (método de `w-consumer/010`). | 10 | — |
| `google-search-block-indexing` | D-159 | `noindex` (método de `w-consumer/010`). | 3 | — |
| `google-crawling-http-status` | D-159 | Cómo trata Google cada código de estado; soft 404 (método de `002` y `003`). | 4 | — |
| `google-search-indexable-file-types` | D-159 | Tipos de fichero indexables (método de `004`). | 5 | — |
| `google-search-canonical` | D-168 | URL canónica (`rel=canonical`): presencia, URL absoluta y un solo método (elemento o cabecera). Ningún método es obligatorio. | 8 | 0 / 3 |
| `google-search-redirects` | D-159 | Redirecciones. No fija nada comprobable sobre la cadena que sirve el recurso. | 3 | — |
| `google-search-javascript-seo` | D-159 | Cómo procesa Google el JavaScript. Fija el método; los RT-01, 12, 13 y 14 no dan requisito. | 9 | — |
| `openai-bots` | D-159 | Bots de OpenAI: recomienda permitir OAI-SearchBot en robots.txt. | 5 | 0 / 1 |
| `perplexity-crawlers` | D-159 | Bots de Perplexity: recomienda permitir PerplexityBot en robots.txt. | 4 | 0 / 1 |
| `anthropic-crawlers` | D-159 | Bots de Anthropic (ClaudeBot, Claude-User, Claude-SearchBot). Describe y no fija requisitos. | 4 | — |

## Otras clases: ficha sin requisitos

| Fuente | Inv. | Clase | Función |
|---|---|---|---|
| `google-merchant-center-structured-data` | GMC-01 | Datos comerciales distribuidos | Emparejamiento del marcado con los datos de producto de Merchant Center. Sirve para Catálogos distribuidos y la consistencia transversal. |
| `google-merchant-center-product-data-spec` | GMC-02 | Datos comerciales distribuidos | Atributos de producto de Merchant Center. |
| `w3c-dwbp` | W3C-02 | Principios generales | Orientan; no dan requisitos comprobables de una ficha. |
| `w3c-shacl` | W3C-03 | Instrumento del sistema | Para expresar los requisitos como restricciones en el auditor. |
| `w3c-prov-o` | W3C-04 | Instrumento del sistema | Para la procedencia de las evidencias del auditado. |
| `gs1-smartsearch` | GS1-02 | Antecedente histórico | Solo contexto. Es PDF y no tiene texto citable. |

## Sin clase en el canon

`gs1-web-vocabulary` (GS1-01) y `gs1-web-vocabulary-standard` (GS1-03) están registradas y congeladas, pero sin ficha. El GS1 Web Vocabulary es un vocabulario distinto de Schema.org y no encaja en ninguna clase de fuente: [I-47](../../docs/30-governance/issues.md#i-47), que propone la clase «vocabulario complementario». Ninguna ficha real usa términos `gs1:`.

## Fuera del registro

- **Método de comprobación ([D-132](../../docs/30-governance/decisions.md#d-132)):** VAL-01 (Schema Markup Validator) y VAL-02 (Rich Results Test). Son aplicaciones y no se congelan; se usan en el contraste con fichas reales (T-048).
- **Práctica de terceros:** SKL-01 a SKL-05 (skills de auditoría SEO). No tienen autoridad.
- **Documentos a los que remiten las especificaciones aplicables y que siguen sin registrar:**

| Documento | Lo citan | Situación |
|---|---|---|
| HTML Living Standard, sección 4 (`meta`, `link`, `time` y `script` como bloque de datos) | Microdata, JSON-LD | **Pendiente** para Web Schema.org; para Web está registrada la sección 4.2 (`whatwg-html-semantics`), con `meta`, sin `time` ni `script`. Es lo que HTML exige a los elementos que llevan el valor de una propiedad Microdata (las 5 fichas con Microdata usan `<meta itemprop>`) y al `script` de JSON-LD. |
| ISO 4217 e ISO 3166-1/2 (códigos de moneda, país y región) | Google (precio, envío, devoluciones) | **ISO 4217 e ISO 3166-1 alfa-2, registradas en [references](../../references/README.md)** (T-062): `iso-4217`, la lista uno de SIX, agencia de mantenimiento de ISO 4217, y `iso-3166-1`, la tabla «Country» de EU Vocabularies (Oficina de Publicaciones de la UE, CC BY 4.0). ISO no publica una lista reutilizable de ISO 3166; la tabla de la UE incluye además algunos códigos que ISO reserva excepcionalmente (EU, IC, CP, CQ). Lectores: `references.read.currency_codes` y `country_codes`. Ficha de cada una como instrumento del sistema, sin citas (XML y RDF no tienen texto citable): la condición la fija la especificación que pide el código, y la lista solo sirve para comprobarla. Los métodos de los 13 requisitos de moneda y país las nombran y ya no tienen como NE la falta de la lista (T-065); los de país excluyen EU, IC, CP y CQ, que la tabla de la UE incluye y ISO no asigna (253 códigos en 20260923-0 = 249 asignados + 4). **ISO 3166-2 (región), sin registrar:** no hay fuente oficial reutilizable, y hoy ningún requisito la comprueba. |
| Formatos de imagen de Google Images | Google (image, logo) | **Pendiente.** Hasta tenerlos, el formato del logo (`ws-consumer/336`) queda en NE. |
| Search Essentials | Fichas de comerciante (#guidelines) | Sus requisitos técnicos, registrados para Web (`google-search-technical-requirements`, D-159). Las políticas de spam siguen fuera: juzgan el contenido. |
| Free listings guidelines, Member program | Fichas de comerciante, Organization | Fuera: Merchant Center (Catálogos distribuidos). |
| Local business, Breadcrumb y otros tipos de Google | Organization; fichas reales | Fuera del perfil (D-130). |
| Namespaces in XML 1.1 y contextos iniciales de RDFa | RDFa | Sin prisa: ninguna ficha real usa RDFa. |
| GS1 Digital Link y reglas generales del GTIN | `schema:gtin`, `schema:hasGS1DigitalLink` | Con I-47. |

## Tipos de las fichas reales

Muestra: las 45 fichas congeladas en `capture/var/pages/` (el almacén común de [capture](../../capture/README.md#almacén-de-fichas)).

- **Tiendas (6):** El Corte Inglés 30, Burrito Blanco 9, Guaw 2, Grupo Todoplano 2, 5V Valverde 1, Kiwoko 1.
- **Sintaxis:** 40 solo JSON-LD, 2 solo Microdata y 3 con las dos; ninguna con RDFa.
- **Vocabulario:** todos los tipos y propiedades están definidos en Schema.org 30.1, salvo `productGroupId`, que aparece en las 2 fichas de Grupo Todoplano; el término definido es `productGroupID`. Ningún requisito lo exige, porque Schema.org no tiene cita normativa para eso: lo registran como evidencia `ws-vocabulary/001` y `ws-consumer/193` (variantes).

| Tipo | Fichas (JSON-LD / Microdata) | Requisitos del consumidor |
|---|---|---|
| Product, Offer, Brand | 42 / 2–3 | Fichas de comerciante, fragmentos de producto, variantes, directrices generales |
| BreadcrumbList, ListItem | 41 / 4–5 | Ninguno: el documento de migas de Google está fuera del perfil. Solo serialización y vocabulario (`ws-vocabulary/008`). |
| ImageObject | 37 / 0 | Como valor de `image` (fichas de comerciante) y de `logo` (Organization) |
| MerchantReturnPolicy | 30 / 0 | Fichas de comerciante (en Offer) y devoluciones (en Organization) |
| ImageGallery, WebPage, ItemList, PropertyValue | 27, 10, 5, 11 / 0 | Ninguno: solo serialización y vocabulario (WebPage: `ws-vocabulary/009`) |
| QuantitativeValue, UnitPriceSpecification | 13, 6 / 0 | Fichas de comerciante, fragmentos de producto, envío |
| Organization, PostalAddress, ContactPoint | 11, 9, 9 / 2 | Organization |
| AggregateRating, Review, Rating, Person | 10, 5, 5, 5 / 0 | Fragmentos de producto y de reseña |
| ProductGroup | 4 / 0 | Variantes, fichas de comerciante |
| AggregateOffer | 1 / 0 | Fragmentos de producto, fichas de comerciante |
| WebSite, SearchAction | 1 / 0 | Ninguno (`WebSite` solo aparece como contexto en Organization) |
| ItemAvailability, OfferItemCondition (como `itemtype`) | 0 / 1 | Ninguno: son enumeraciones usadas como tipo |
