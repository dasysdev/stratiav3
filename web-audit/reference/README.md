# Referencia técnica

Fichas de fuente con citas literales y requisitos técnicos de la evaluación técnica ([D-133](../../docs/30-governance/decisions.md#d-133)). Son datos gobernados por el canon: [evaluation-scopes](../../docs/10-model/evaluation-scopes.md#requisitos-técnicos-generales) (perfil de implementación, estados del requisito técnico y fuentes) prevalece sobre todo lo de aquí. Los requisitos los deciden los agentes, siempre con cita; el usuario los revisa si lo pide. Se crean y se mantienen con la skill `/web-reference` y se validan con `web-audit/bin/reqs check`.

```
reference/
├── inventory.md              inventario: función y estado de cada fuente, las que quedan fuera del
│                             registro y la cobertura de los tipos de las fichas reales
├── cards/<fuente>.json       ficha de cada fuente registrada
├── requirements/<nivel>.json requisitos técnicos de un nivel del perfil de un ámbito:
│                             Marcado: serialization.json · vocabulary.json · consumer.json
│                             Contenido: web-protocol.json · web-document.json · web-consumer.json
├── retired.json              requisitos retirados, con su motivo
└── reports/                  informe de cada pasada de la skill (fecha-tema.md)
```

## Ficha de fuente

Una por fuente registrada, con su id como nombre de fichero. Dice qué función tiene la fuente en el canon y guarda las citas literales que fundamentan los requisitos.

| Campo | Contenido |
|---|---|
| `source` | Id de la fuente en [references/sources.json](../../references/sources.json), con web-audit en su `uses`. |
| `version` | La versión que cita la ficha. Ha de ser la **fijada** (`references/var/pins.json`). |
| `class` | Su clase según el canon ([D-132](../../docs/30-governance/decisions.md#d-132)): `especificación aplicable`, `instrumento del sistema`, `principios generales`, `método de comprobación`, `práctica de terceros`, `antecedente histórico` o `datos comerciales distribuidos`. |
| `level` | Solo en una especificación aplicable: su nivel del perfil. En Marcado ([D-130](../../docs/30-governance/decisions.md#d-130)), `serialización`, `vocabulario` o `consumidor`; en Contenido ([D-159](../../docs/30-governance/decisions.md#d-159)), `protocolo`, `documento` o `consumidor`. |
| `scopes` | Solo en una especificación aplicable: los ámbitos de cuyo perfil es, `Marcado`, `Contenido` o los dos, con el mismo nivel (las directrices generales de datos estructurados de Google son del consumidor en los dos). |
| `summary` | Qué fija la fuente o para qué sirve, en una o dos frases. |
| `quotes` | Citas: `id` (`q01`, `q02`…; no se reutiliza), `section` y `text` (literal). Opcional, `note`. |
| `note` | Opcional. |

**Secciones.** Una cita es un fragmento continuo de una sección de la versión fijada:

- **Página HTML** (`text.md`): el ancla del encabezado, `#product-properties` para `## Product {#product-properties}`. Si el encabezado no tiene ancla, su texto. La sección llega hasta el siguiente encabezado del mismo nivel o superior, con sus subsecciones. `#` es el **preámbulo**: el texto antes del primer encabezado, o todo si no hay ninguno. Ahí queda la introducción de las páginas cuyo título está fuera de la raíz del contenido, como las de los bots de OpenAI, Anthropic y Perplexity.
- **Vocabulario en JSON-LD** (la release de Schema.org, `gs1Voc.jsonld`): el término, `schema:gtin`. La cita es parte de su definición (`rdfs:comment`).
- **PDF:** no tiene texto citable.

`web-audit/bin/reqs section FUENTE` lista las secciones y `reqs section FUENTE SECCIÓN` muestra el texto tal como lo lee la validación: las citas se copian de ahí. Al comparar solo cuentan las palabras, no los saltos de línea ni los espacios. No se parafrasea, no se traduce y no se unen fragmentos.

## Requisito técnico

Cada fichero de `requirements/` es un nivel del perfil de implementación de un ámbito: `{"level": "consumidor", "requirements": [...]}`.

| Ámbito | Fichero (nivel) | Ids |
|---|---|---|
| Marcado | `serialization.json` (serialización) · `vocabulary.json` (vocabulario) · `consumer.json` (consumidor) | `ws-serialization/001` · `ws-vocabulary/001` · `ws-consumer/001` |
| Contenido | `web-protocol.json` (protocolo) · `web-document.json` (documento) · `web-consumer.json` (consumidor) | `w-protocol/001` · `w-document/001` · `w-consumer/001` |

Los ficheros y los prefijos de los ids conservan los nombres anteriores de los ámbitos, Web y Web Schema.org ([D-220](../../docs/30-governance/decisions.md#d-220)): un id no cambia.

Un requisito tiene los campos que pide el canon ([regla 7](../../docs/10-model/evaluation-scopes.md#reglas-e-invariantes)), su perfil y su cita, y ningún otro:

| Campo | Contenido | En el canon |
|---|---|---|
| `id` | El prefijo del fichero y un número (`ws-consumer/001`, `w-protocol/001`). No se reutiliza. | — |
| `scope` | El ámbito del fichero, `Marcado` o `Contenido`. Catálogos distribuidos no tiene perfil ([OQ-30](../../docs/30-governance/open-questions.md#f-evaluación-técnica)). | ámbito |
| `spec` | Fuente con ficha de especificación aplicable, del nivel del fichero y con el ámbito en sus `scopes`. Falta si lo funda una condición del proyecto. | especificación aplicable |
| `decision` | Solo si lo funda una **condición del proyecto** en lugar de una especificación: la decisión del canon que la adopta y fija su naturaleza (`D-162`). Lleva `decision` o `spec`, nunca los dos. Sus `quotes` pueden estar vacías o citar fuentes de apoyo del método. | condición del proyecto ([D-162](../../docs/30-governance/decisions.md#d-162)) |
| `view` | `general` (una vez por sitio: robots.txt, sitemaps, la organización y sus políticas) o `particular` (en cada página auditada). | vista ([D-161](../../docs/30-governance/decisions.md#d-161)) |
| `page_types` | Solo en la vista particular: los tipos de página a los que se aplica, sin repetir: `ficha de producto`, `categoría o listado`, `políticas y contenido`, `portada`. | tipo de página |
| `condition` | Una sola condición comprobable, en una frase. Si se cumple, el requisito está satisfecho. | estado de satisfacción |
| `nature` | `obligatoria` o `recomendada`, la que fija la especificación, nunca el auditor. | naturaleza |
| `quotes` | Citas de las fichas (`fuente#q01`), al menos una de `spec`. Entre las de `spec`, el texto que fija la naturaleza. | cita ([D-132](../../docs/30-governance/decisions.md#d-132)) |
| `method` | Cómo se comprueba la condición. | método de comprobación |
| `evidence` | Qué se registra como evidencia. | evidencia |
| `applicability` | `universal` o el hecho del recurso del que depende. Si no se da, es NA. | estado de aplicabilidad |
| `not_evaluable` | Causas propias por las que la comprobación puede no hacerse (NE); `[]` si solo tiene las comunes, como no obtener el recurso o su marcado. | estado de evaluación |
| `rationale` | Opcional: por qué la condición sale de la cita. | — |

El perfil del requisito es su ámbito, el nivel de su fichero y su especificación. Su versión es la de la ficha de `spec`. Los estados son los del canon ([D-131](../../docs/30-governance/decisions.md#d-131)): estos campos dicen cuándo se da cada uno, sin añadir valores, pesos, puntuaciones ni umbrales.

**Qué se escribe** ([D-145](../../docs/30-governance/decisions.md#d-145), [D-147](../../docs/30-governance/decisions.md#d-147), [D-148](../../docs/30-governance/decisions.md#d-148)). De una especificación del consumidor, solo lo técnico:

- la presencia de lo que **exige**, también lo condicional (con la condición en `applicability`);
- la **forma** de lo que se publica, aunque la propiedad sea recomendada (un solo `sku`, `priceValidUntil` en ISO 8601);
- la **formación estructural** de una estructura publicada: las partes que exige, las partes sin las que un valor publicado no se puede interpretar (unidad, escala `bestRating`/`worstRating`, sistema y grupo de tallas, moneda, `priceType`, `inCodeSet`, `valueReference`, la URL del logo) y la coherencia entre partes («Ningún… tiene…», una sola moneda);
- la presencia de lo recomendado que es **dato del mínimo de representación**: `ws-consumer/032`, `034`, `042`, `066`, `153`, `192`, `202`, `205` y `339`.

La presencia de lo que solo se recomienda y solo añade otro hecho (`description`, `gtin`, `brand`, `handlingTime`, `refundType`…) no es requisito técnico: la juzga la evaluación informativa: es apoyo de demanda «referencias», sin ámbito, y localizador en la ficha de Marcado del motor de demanda ([D-155](../../docs/30-governance/decisions.md#d-155)).

**En Contenido** ([D-160](../../docs/30-governance/decisions.md#d-160)) se escribe el acceso y la recuperación del recurso, la forma de la respuesta y del documento y la presencia de lo que el consumidor exige para la página (no bloqueado, 200, contenido indexable, marcado). Las recomendaciones de acceso (permitir un bot) también, porque no añaden un hecho comercial. Solo se audita lo que, si falla, puede impedir obtener o leer la información de la página o el acceso de los sistemas que la consumen: no la conformidad formal sin efecto en la lectura (DOCTYPE, etiqueta y posición de la declaración de codificación), ni el rastreo del sitio (enlaces a otras páginas), ni lo redundante ([triaje de Contenido](reports/2026-10-28-triaje-web.md)). Si la información comercial está en el documento es de la evaluación informativa. El marcado se examina solo por su presencia: su sintaxis y su estructura son de Marcado. Las condiciones de la petición, la ejecución de JavaScript y la operación de la página son el perfil de consumo, no requisitos ([D-159](../../docs/30-governance/decisions.md#d-159)). Del mínimo de representación de Contenido ([D-168](../../docs/30-governance/decisions.md#d-168)) se escriben el título (`w-document/008`, `009`), la URL canónica (`w-consumer/015`–`017`) y, si la página usa Open Graph, sus cuatro propiedades exigidas y la coincidencia de `og:url` con la canónica (`w-document/010`–`014`).

**Una especificación por requisito.** Si dos especificaciones fijan la misma condición (`name` en las fichas de comerciante y en los fragmentos de producto), cada una tiene su requisito, con su naturaleza. En la tasa de cumplimiento técnico cada requisito cuenta uno, sin pesos ([D-166](../../docs/30-governance/decisions.md#d-166)).

Ejemplo (ilustrativo, con citas reales de `google-search-merchant-listing` 2026-10-27):

```jsonc
// cards/google-search-merchant-listing.json
{"source": "google-search-merchant-listing", "version": "2026-10-27",
 "class": "especificación aplicable", "level": "consumidor",
 "summary": "Propiedades exigidas y recomendadas por Google Search para las fichas de comerciante (Product, Offer).",
 "quotes": [
  {"id": "q01", "section": "#structured-data-type-definitions",
   "text": "You must include the required properties for your content to be eligible for display as a rich result."},
  {"id": "q02", "section": "#product-properties", "text": "Required properties"},
  {"id": "q03", "section": "#product-properties", "text": "offers | Offer A nested Offer to sell the product."}]}

// requirements/consumer.json
{"level": "consumidor", "requirements": [
 {"id": "ws-consumer/001", "scope": "Marcado", "spec": "google-search-merchant-listing",
  "condition": "Cada entidad Product del marcado tiene la propiedad offers.", "nature": "obligatoria",
  "quotes": ["google-search-merchant-listing#q01", "google-search-merchant-listing#q02", "google-search-merchant-listing#q03"],
  "method": "Extraer las entidades Product del marcado (JSON-LD, Microdata y RDFa) y comprobar que cada una tiene al menos un valor de offers.",
  "evidence": "Por cada Product: su localización en el marcado y los valores de offers, o su ausencia.",
  "applicability": "universal", "not_evaluable": []}]}
```

## Método común

Todos los métodos de Marcado lo presuponen. Un método puede apartarse de él si lo dice expresamente. Sale del contraste con fichas reales ([informe](reports/2026-10-28-contraste.md), T-048).

1. **Documento.** Se examina el HTML servido. Si no se dispone de él, se examina el DOM renderizado, y se registra cuál de los dos se usó. La aplicabilidad se decide sobre el mismo documento. Esto no se aplica a los requisitos que comparan los dos documentos (`ws-consumer/149`) ni a los que exigen el HTML servido: si falta, son NE.
2. **Entidades.** Se examinan **todas** las entidades del marcado, también las de productos relacionados o recomendados: el marcado ha de ser correcto aunque describa otros productos.
   - **JSON-LD:** los nodos con el mismo `@id` son una sola entidad, aunque estén en bloques distintos o en un `@graph`.
   - **Microdata:** son entidades los elementos con `itemscope`. Un item con `itemprop` sin item antecesor se examina como entidad suelta de su `itemtype`, sin perjuicio de `ws-serialization/036`.
3. **Cada tipo, con sus reglas.** Las reglas de un tipo se aplican a sus subtipos, salvo que el subtipo tenga reglas propias en el perfil:
   - Lo que se dice de «Product» no se aplica a ProductGroup, que tiene las suyas (`google-search-product-variants`). Sus variantes son Product.
   - Lo que se dice de «Offer» no se aplica a AggregateOffer, que tiene las suyas (`ws-consumer/167`–`170`). Que un Product use AggregateOffer lo comprueban `011` y `154`.
   - Un requisito que nombra los dos tipos («Product o ProductGroup») se aplica a los dos.
   - **Entidad valorada** (requisitos de `google-search-review-snippet`): una entidad de uno de los tipos válidos que da la guía para el objeto de la reseña (Book, Course, CreativeWorkSeason, CreativeWorkSeries, Episode, Event, Game, HowTo, LocalBusiness, MediaObject, Movie, MusicPlaylist, MusicRecording, Organization, Product, Recipe, SoftwareApplication) o de un subtipo suyo. Con ProductGroup y OnlineStore incluidos.
4. **Enlaces.** Cada enlace entre entidades se sigue por anidamiento o por `@id` en JSON-LD, y por anidamiento o `itemref` en Microdata. Puede ser de la organización a su política o de una estructura a sus partes. Si una referencia `@id` no se resuelve en el marcado de la página, porque la entidad se publica en otra página, lo que dependa de ella es NE.
5. **Contexto de Schema.org.** Los contextos remotos `http://schema.org` y `https://schema.org`, con o sin barra final, se resuelven con el contexto congelado de la release fijada (`schemaorgcontext.jsonld` de la fuente `schemaorg`). Solo un contexto remoto distinto que no se pueda obtener da NE.
6. **Valores.**
   - **Miembro de una enumeración:** se reconoce como IRI `https://schema.org/…` o `http://schema.org/…`, o por su nombre. En JSON-LD vale como cadena o como `@id`; en Microdata, en `content` o en `href`.
   - **Booleano:** vale el booleano JSON, el texto `true`/`false` (sin distinguir mayúsculas) o `schema:True`/`schema:False`.
   - **Grafía de las propiedades:** cuenta solo la exacta. JSON-LD y Microdata distinguen mayúsculas, y la normalización de un validador no es prueba.
7. **Contenido visible.** Es el texto del documento examinado que queda fuera de `script`, `style`, `template` y de los atributos, y fuera de los elementos ocultos con `hidden`, `aria-hidden="true"` o `display:none` en línea. El texto solo para lectores de pantalla cuenta como visible.

## Método común de Contenido

Todos los métodos de Contenido lo presuponen, y pueden apartarse de él si lo dicen expresamente.

1. **Respuesta.** Se examina la respuesta HTTP del recurso tal como la registra la ficha congelada de [capture](../../capture/README.md#qué-se-conserva): en `meta.json`, la URL pedida y la final, las redirecciones, el estado y las cabeceras; en `response.html`, el cuerpo del documento. Es el perfil de consumo, sin ejecutar JavaScript ([D-156](../../docs/30-governance/decisions.md#d-156)): el DOM tras la carga (`dom.html`) no se usa. Si la ficha no tiene respuesta del recurso (un desafío, un error de red), lo que dependa de ella es NE.
2. **Bytes del cuerpo.** Con `audit-es`, capture guarda además los bytes originales del cuerpo, sin `Content-Encoding` y con su BOM (`response.html.gz`; `response_body` vale `original` en `meta.json`). Lo que depende de ellos (la codificación real, el BOM) se examina en esos bytes; `response.html` es el cuerpo ya decodificado y pasado a UTF-8. En una ficha sin los bytes originales (capturada con otro perfil), lo que dependa de ellos es NE. Las cabeceras son las que envió el servidor.
3. **robots.txt** (RFC 9309, `ietf-rfc9309`; para Googlebot, la lectura de Google, `google-crawling-robots-txt`, donde difiera):
   - **Fichero:** el `/robots.txt` del origen de la URL pedida. Si la cadena de redirecciones cambia de origen, el del destino no se examina.
   - **Estado del fichero:**
     - con 2xx, se leen sus reglas;
     - con 4xx («unavailable»), todo está permitido, y el cuerpo de la respuesta (una página de error) no se lee como reglas;
     - con 5xx o sin respuesta («unreachable»), todo está prohibido.
     - capture trata el 429 como «unreachable», como Google, y el RFC lo da como 4xx: se registra cuál se aplicó.
   - **Evidencia:** en una auditoría ([D-167](../../docs/30-governance/decisions.md#d-167)), el fichero de cada origen está en `sites/HOST/robots.txt` y su estado en `legitimacy.robots.status` del `meta.json` de cada página (el del sitio, también en `audit.json`); el registro por bot de capture, en `robots_bots`. Si faltan, es NE.
   - **Grupo:** el que nombra el token del bot, sin distinguir mayúsculas (si son varios, sus reglas se combinan). Si no hay ninguno, el de `*`, y si tampoco existe ese, no se aplica ninguna regla.
   - **Regla:**
     - se compara la ruta con su query, normalizadas como fija el RFC y con los comodines `*` y `$`;
     - gana la coincidencia más larga (más octetos);
     - entre un `allow` y un `disallow` equivalentes se aplica `allow`, que el RFC fija con «SHOULD»;
     - sin coincidencia, está permitido, y `/robots.txt` lo está siempre.
4. **Contenido textual.** Es el contenido visible del documento de la respuesta, con la definición del [método común](#método-común) de Marcado (punto 7).
5. **Sitemaps** (`sitemaps-org-protocol`):
   - **Cuáles:** los que declaran las líneas `sitemap:` del robots.txt del origen de la página. Si no declara ninguno, `/sitemap.xml` en la raíz, que es donde lo recomiendan el protocolo y Google. Un índice de sitemaps se sigue hasta sus sitemaps, y los comprimidos con gzip se leen descomprimidos.
   - **Formatos:** XML (`urlset` o `sitemapindex`), RSS o Atom y texto. Los requisitos de forma de sitemaps.org son del XML.
   - **URL que valen** (para saber si una página está en los sitemaps, w-consumer/014): la lectura de Google (`google-search-sitemaps-build#q05`, decisión del usuario del 2026-10-29). Un sitemap enviado vale para todo su host, no solo para su directorio. Los del conjunto están enviados: los declara el robots.txt del sitio, directamente o por un índice, o son `/sitemap.xml` en la raíz. Valen, pues, las URL con el mismo protocolo y host que su sitemap, en cualquier directorio, y las de otro host cuyo robots.txt declare el sitemap (cross submit). Un envío por Search Console no se puede observar y no se presupone.
   - **Ubicación estricta del protocolo:** sitemaps.org solo admite las URL bajo el directorio del sitemap. Esa forma la comprueba w-protocol/009, como requisito del protocolo, y no cambia qué páginas están en los sitemaps.
   - **Decisión:** un requisito de forma no se satisface si algún sitemap examinado incumple. Se satisface si se obtuvieron todos y ninguno incumple. Es NE si alguno no se pudo obtener y ninguno de los obtenidos incumple.
   - **Evidencia:** capture congela los sitemaps de una auditoría ([D-167](../../docs/30-governance/decisions.md#d-167)) tal como llegan, en `sitemaps/`, con su URL y su estado en `audit.json` (`sitemaps.read`) y los que el tope dejó sin leer en `pending`. Un 4xx distinto de 429 es que el sitemap no existe; un error, un 5xx, un 429 o uno pendiente es un sitemap no obtenido.
6. **Vistas** ([D-161](../../docs/30-governance/decisions.md#d-161)):
   - un requisito `general` se evalúa una vez por sitio, sobre sus recursos de sitio o sus entidades de sitio;
   - uno `particular` se evalúa en cada página auditada cuyo tipo esté en `page_types`; en las demás no se aplica.
   - En Marcado, la organización y sus políticas (vista general) se examinan en el marcado de las páginas auditadas del sitio, como una sola entidad por `@id`. Su sintaxis y su vocabulario los comprueban los requisitos particulares de la página donde se publican.
7. **Propiedades Open Graph** (`ogp-protocol`): los elementos `meta` del documento de la respuesta cuyo atributo `property` es `og:…` (sin distinguir mayúsculas ASCII en el nombre), con su `content`. El protocolo los pone en `head` y se basa en RDFa: los que usan `name` en lugar de `property` no cuentan como Open Graph, pero se registran. Si una propiedad se repite, se examina cada valor.

## Requisitos retirados

`retired.json` guarda los requisitos que salen de `requirements/`: `{"retired": [...]}`. Un retirado conserva los campos que dicen qué pedía la especificación (`id`, `scope`, `spec`, `condition`, `nature`, `quotes`, `applicability`), sin `method`, `evidence` ni `not_evaluable`, que eran del control técnico, y añade:

| Campo | Contenido |
|---|---|
| `reason` | `no se audita` (los triajes del 2026-10-28, de Marcado y de Contenido) o `modelo de demanda` (presencia de lo que el consumidor solo recomienda, [D-145](../../docs/30-governance/decisions.md#d-145)). |
| `decision` | Dónde se decidió: `triaje 2026-10-28` ([informe](reports/2026-10-28-triaje.md)), `triaje de Contenido 2026-10-28` ([informe](reports/2026-10-28-triaje-web.md)) o la decisión del canon. |
| `note` | Opcional: el bloque del triaje y su porqué. |

- **Los ids no se reutilizan.** Un requisito nuevo toma el siguiente número libre contando los retirados.
- **Las citas siguen vivas:** las fichas conservan las que usan los retirados y la validación comprueba que existen.
- **Contrato con el motor de demanda.** Los de `modelo de demanda` son la entrada de demand-engine (T-056, [D-155](../../docs/30-governance/decisions.md#d-155)): su `catalog/google-search.json` lista cada id con la propiedad que nombra, y `demand-engine/bin/model check --catalog` comprueba que los dos registros tienen los mismos ids y que cada propiedad apoya un requisito o una aportación o es un candidato. Si cambia esta lista o el motivo de un retirado, esa comprobación falla hasta que demand-engine lo recoge.

## Huecos

Datos del canon que la referencia no puede comprobar porque ninguna especificación del perfil los fija con must o should:

- **Identificador de la entidad (`@id`).** Es dato de sostén del mínimo de representación en Marcado ([D-147](../../docs/30-governance/decisions.md#d-147)), sin requisito técnico de presencia. Su forma, si se publica, sí la comprueba la serialización (en JSON-LD, una referencia IRI), y los métodos de la referencia lo siguen para enlazar entidades; pero ninguna fuente del consumidor pide que exista. Sin requisito, no entra en la tasa de cumplimiento técnico ([D-166](../../docs/30-governance/decisions.md#d-166)): se registra como hueco.
- **Imagen en Contenido.** Es dato de sostén del mínimo de representación de Contenido ([D-168](../../docs/30-governance/decisions.md#d-168)). Solo la declara de forma comprobable Open Graph (`og:image`, `w-document/012`), que es condicional: en una página sin Open Graph ninguna especificación del perfil de Contenido exige una imagen, y se registra como hueco.
- **Fragmento en la URL canónica.** Google lo desaconseja («Don't specify a URL fragment as canonical»), pero sin must, should ni recommend: no da requisito.

## Validación

`web-audit/bin/reqs check` se ejecuta en el host y sale con error si encuentra algún problema:

- **Formato:** campos obligatorios presentes, ningún campo fuera del formato, valores del canon (clase, nivel, ámbito y naturaleza), ids únicos y con su forma.
- **Retirados:** su formato, que su id no siga en `requirements/`, que solo lo recomendado vaya al modelo de demanda y que sus citas existan.
- **Citas:** la ficha cita la versión fijada y cada cita está, literal, en su sección de esa versión. Tras `references/bin/refs pin`, la comprobación falla hasta que se revisan las fichas de la fuente.
- **Fichas:** una especificación aplicable lleva `level` y `scopes`, y el perfil de cada ámbito de `scopes` tiene ese nivel.
- **Vista:** cada requisito tiene `view`, y los particulares, `page_types` del canon.
- **Condición del proyecto:** un requisito lleva `spec` o `decision`, y la `decision` es una de `docs/30-governance/decisions.md`. Su naturaleza la fija la decisión, sin término en las citas.
- **Requisitos:** su ámbito es el del fichero, y su especificación es aplicable, del nivel del fichero y del perfil del ámbito. Cada cita existe y es de una especificación aplicable. Al menos una es de `spec`, y alguna de las de `spec` contiene el término de su naturaleza (must, required, requirement(s) o shall para obligatoria; should o recommend para recomendada). «requirements» es como Search Essentials fija lo que Google Search exige («minimum technical requirements», [D-159](../../docs/30-governance/decisions.md#d-159)). La condición es una sola frase, sin «;».
- **Resumen:** fichas, citas, requisitos por naturaleza, por ámbito y por vista, retirados por motivo y las fuentes registradas sin ficha.

No puede comprobar el sentido. Que la condición sea **una** sola, que la clase y el nivel sean los de la tabla del canon y que la cita fundamente de verdad la condición quedan a cargo de quien la escribe, con las reglas de la skill.
