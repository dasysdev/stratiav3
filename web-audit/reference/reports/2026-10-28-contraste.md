# Contraste de los requisitos técnicos con fichas reales (T-048)

Fecha: 2026-10-28. Se aplican los 322 requisitos técnicos a cinco fichas congeladas, una por tienda, y se contrastan con Schema Markup Validator. El objetivo es encontrar los requisitos que no se pueden comprobar o que son ambiguos. Cinco agentes, uno por grupo de requisitos, aplicaron cada requisito a las cinco fichas tal como estaba escrito. El estado de cada requisito en cada ficha, con su evidencia, está en [2026-10-28-contraste/](2026-10-28-contraste/), y refleja los requisitos **antes** de las correcciones.

## Muestra

La tarea pedía 10 fichas; el usuario la redujo a 5. Todas salen de las ya capturadas (`capture/var/pages/`, DOM renderizado, sin HTML servido). Se deja fuera 5V Valverde, que no publica Product.

| Ficha | Tienda | Marcado |
|---|---|---|
| `eci-lijadora-a200805914` | El Corte Inglés | Product en JSON-LD; itemprop sueltos sin itemscope |
| `cojin-018` | Burrito Blanco | Cinco bloques JSON-LD enlazados por `@id`; AggregateRating de la Organization |
| `colchoneta-refrescante-freedog` | Guaw | Solo Microdata: el producto y 30 relacionados como Product completos |
| `cuerda-tootoy` | Kiwoko | ProductGroup en JSON-LD (`lowprice`/`highprice` en minúsculas) y una Offer suelta en Microdata |
| `sofa-cama-luna` | Grupo Todoplano | Product en JSON-LD con `productGroupId` (no definido en 30.1) |

## Estados por ficha

| Ficha | Satisfecho | No satisfecho | NA | NE |
|---|---|---|---|---|
| El Corte Inglés | 56 | 2 | 249 | 15 |
| Burrito Blanco | 55 | 2 | 246 | 19 |
| Guaw | 45 | 8 | 256 | 13 |
| Kiwoko | 60 | 12 | 235 | 15 |
| Grupo Todoplano | 78 | 3 | 227 | 14 |

- **NA dominan:** ninguna ficha publica políticas de devolución o envío bajo Organization (los 72 requisitos de esas políticas dan NA en las cinco), ni tallas, ni certificaciones, ni RDFa.
- **NE comunes:** sin HTML servido, cabeceras HTTP, imágenes, robots.txt de su host ni otras páginas del sitio. Destaca `ws-serialization/001` (JSON-LD bien formado), NE en las cuatro fichas con JSON-LD.

## Schema Markup Validator

Endpoint `POST https://validator.schema.org/validate` con el HTML de la ficha congelada.

| Ficha | Errores | Avisos |
|---|---|---|
| El Corte Inglés | 0 | 0 |
| Burrito Blanco | 0 | 0 |
| Guaw | 0 | 0 |
| Kiwoko | 0 | 0 |
| Grupo Todoplano | 0 | 1: `productGroupId` desconocido en Product |

Lo que el validador no ve y los requisitos sí:
- normaliza `lowprice` a `lowPrice`;
- extrae como item la Offer de Microdata sin item padre (Kiwoko);
- no se queja de los itemprop sin itemscope;
- no se queja de `<meta itemprop="url">` (Guaw);
- no se queja de los precios con símbolo (`3.49€`).

Es un validador de sintaxis y vocabulario indulgente: no sirve de contraste para los requisitos del consumidor.

## Rich Results Test

El usuario lanzó la prueba sobre la URL en vivo de cada ficha, rastreada el 28 de octubre, no sobre la versión congelada. Los resultados se leyeron con el Chrome del motor de captura: la página se genera con JavaScript y no tiene API. Detalle en [rich-results-test.json](2026-10-28-contraste/rich-results-test.json), con el enlace a cada resultado. Ninguna ficha tiene errores críticos. Todas las advertencias son campos opcionales que faltan.

| Ficha | Elementos válidos | Advertencias (no críticas) |
|---|---|---|
| El Corte Inglés | 3: fragmento de producto, ficha de comerciante, ruta de exploración | Fragmento: faltan `review` y `aggregateRating`. Ficha: falta `shippingDetails`. |
| Burrito Blanco | 5: los tres anteriores, más organización y fragmento de reseña («Burrito Blanco») | Fragmento: faltan `review` y `aggregateRating`. Ficha: faltan `hasMerchantReturnPolicy` y `shippingDetails` (dice 3 problemas; se leyeron 2). |
| Guaw | 72: 32 fragmentos y 32 fichas (el producto y los relacionados), 7 fragmentos de reseña y 1 ruta | Fragmentos: faltan `review`, `aggregateRating` y `availability`. Fichas: faltan `availability`, `validFrom`, `hasMerchantReturnPolicy` y `shippingDetails`. Se leyeron 3 elementos de cada tipo. |
| Kiwoko | 3: fragmento, ficha (ProductGroup con su variante) y ruta | Fragmento: faltan `review` y `aggregateRating`. Ficha: faltan `description` (de la variante), `hasMerchantReturnPolicy` y `shippingDetails`. |
| Grupo Todoplano | 5: fragmento, ficha, ruta y 2 fragmentos de reseña | Ficha: faltan `validFrom`, `hasMerchantReturnPolicy` y `shippingDetails`. |

**Contraste con los requisitos:**

- **Todas las entidades se examinan.** Google valida como fichas de comerciante los 32 Product de Guaw, también los relacionados. Coincide con el método común (punto 2).
- **El grupo, con sus variantes.** En Kiwoko la ficha de comerciante es el ProductGroup con su variante, y lo que se exige se mira en la variante (falta su `description`). Coincide con el punto 3.
- **Lo que Google no señala:** `lowprice` en minúsculas, el precio `3.49€` y la Offer suelta de Microdata (Kiwoko), `<meta itemprop="url">` (Guaw), `productGroupId` (Todoplano) y los itemprop sin item. Nuestros requisitos sí los señalan, porque el Rich Results Test solo informa de lo que impide o mejora el resultado enriquecido. No contrasta la serialización ni la forma de los valores: que los dos coincidan no prueba nada.
- **AggregateRating de la Organization** (Burrito Blanco): Google la detecta como fragmento de reseña válido, pero su propia guía declara no apta la página de una organización que publica las reseñas sobre sí misma (`#technical-guidelines`, «you must follow»). El Rich Results Test no aplica esa directriz. Resuelto con el usuario (ver abajo).
- **Las advertencias del Rich Results Test son presencia de recomendados** (`review`, `aggregateRating`, `shippingDetails`, `hasMerchantReturnPolicy`, `description`, `validFrom`, `availability`). Desde D-145 casi todas son del modelo de demanda, no requisitos técnicos. `validFrom` (precio de rebaja, `072`) sí es técnico; y `availability`, que es del modelo de demanda, Google la avisa en los relacionados de Guaw.

## Correcciones locales (70 requisitos)

Con `/web-reference`. `reqs check`: correcto, 322 requisitos (199 obligatorios y 123 recomendados).

| Problema | Requisitos | Corrección |
|---|---|---|
| El método no nombra la propiedad | `211`, `239`; los de enumeración `212`, `215`, `220`, `222`, `224`, `228`, `230`, `232`, `234`, `237`, `241`, `251` | Nombran la propiedad. |
| El filtro por miembro de enumeración no dice cómo se reconoce | `213`, `216`, `217`, `218`, `225`, `226`, `242` | IRI http/https o nombre. `217` deja la lista de admitidos copiada y `218` dice qué pasa sin value ni maxValue. |
| El booleano `doesNotShip` | `274`, `276` | true, «true» o `schema:True`. |
| La condición choca con `254` | `253` | Basta un ShippingService de miembros, no todos. |
| Asimetría con `208` | `245` | Se descartan los ShippingService de un OfferShippingDetails. |
| Formación estructural supeditada a la página | `257`, `282` | Sin condición de página. |
| ISO 3166-2 sin fuente | `279` | Solo la forma; se dice que la asignación no se comprueba. |
| El método pide más que la condición | `087`, `088`, `105`, `107`, `108`, `139` | Solo presencia, como la condición. |
| Grafía y URL | `159` (http y https), `167`, `169` (grafía exacta; la normalización de un validador no prueba) | |
| Condición y método no coinciden | `178` (todas las entidades en JSON-LD), `177` (basta un documento), `184` (URL final sin fragmento) | |
| «URL de imagen» sin definir | `185`, `186` | image, logo, thumbnailUrl e ImageObject; no las URL dentro de un texto. |
| Aplicabilidad más ancha que la cita | `072` (solo precios de rebaja), `078`, `081` (precio por unidad de medida del producto, no por pieza) | |
| Causas NE que faltaban | `090`, `091`, `149`, `180`, `340`, `341` | |
| Selector con un solo valor | `032`, `034`, `192`, `205` | Hacen falta dos o más opciones. `034` registra la relación inversa hasVariant. |
| «Nivel superior» solo para @graph | `307`, `314`, `319`, `333`–`337`, `339`–`341`, `346` | Cuenta también un bloque JSON-LD propio referenciado por `@id`. |
| Otros | `119`, `147` (todas las Offer, también AggregateOffer y relacionadas), `ws-serialization/033` (URL es subtipo de Text en 30.1), `036` (itemprop sueltos), `ws-vocabulary/001` (referencias `@id` entre bloques, enumeraciones como texto, términos no definidos en la evidencia) | |

## Método común (decidido con el usuario)

Las ambigüedades que afectaban a muchos métodos a la vez se resuelven en la sección [Método común](../README.md#método-común) del README, que todos los métodos presuponen. En el caso de ProductGroup, dos agentes habían llegado a propuestas contrarias.

1. **Documento:** HTML servido o, si no se dispone de él, DOM renderizado. `ws-serialization/001` deja de ser NE: el texto de un script no cambia al analizar el HTML.
2. **Todas las entidades,** también las de productos relacionados, porque el marcado ha de ser correcto aunque describa otros productos (decisión del usuario). En Guaw, los 30 relacionados con una sola imagen no satisfacen `006`. `ws-consumer/173` (página centrada en un producto) los cuenta: un Product de otro producto hace que no se satisfaga.
3. **Cada tipo, con sus reglas:** ProductGroup se evalúa con las reglas de variantes, no con las de «Product»; AggregateOffer, con las suyas, no con las de «Offer». En Kiwoko, el grupo deja de incumplir `001` y `003`.
4. **Enlaces** por `@id` e `itemref`. Una referencia `@id` sin resolver en la página da NE: por ejemplo, una política publicada en otra página.
5. **Contexto de Schema.org:** se resuelve con el contexto congelado de 30.1.
6. **Valores:** cómo se reconocen las enumeraciones y los booleanos, y que solo cuenta la grafía exacta.
7. **Contenido visible:** su definición sobre el documento examinado.

También se corrige `ws-consumer/053`: un precio tiene forma numérica, sin símbolo de moneda, coma decimal ni separador de miles. Así, «3.49€» de Kiwoko no lo satisface.

## Reseñas de cualquier entidad valorada (decidido con el usuario)

- **Ampliación.** Los 28 requisitos de `google-search-review-snippet` se aplican a las reseñas y valoraciones de cualquier **entidad valorada**, no solo de Product y ProductGroup. Entidad valorada es una de los tipos válidos de la guía (Organization, LocalBusiness, Product, Book…) o de un subtipo. Su definición está en el método común (punto 3), y la cita es `q36`. Es el mismo criterio que con los productos relacionados: el marcado ha de ser correcto aunque describa otra cosa.
- **`ws-consumer/385`, nuevo y obligatorio** (`q28`, `q37` y `q38`): ninguna Organization del marcado con aggregateRating o review es la organización del propio sitio. La organización es la del sitio si su url o su `@id` comparten host con la página, o si es el seller de una Offer o el publisher del sitio. Es un hecho del marcado: no se juzga la veracidad de las reseñas (D-129). Burrito Blanco no lo satisface.
- La nota de la ficha `google-search-review-snippet` lo recoge. Las reseñas sueltas con itemReviewed siguen fuera.
- **Pendiente del triaje:** este bloque seguía marcado «se revisa como requisitos informativos». La ampliación lo mantiene en la evaluación técnica.

## Pendiente

- **`ws-consumer/029`** (contenido para adultos): siempre NE. Hay que registrar la política de contenido para adultos de Google como fuente.
- **`ws-consumer/032`:** Kiwoko da el ID del grupo en `productGroupID` de la ProductGroup, no en `inProductGroupWithID` de la variante. La guía de variantes admite las dos formas, pero la fila de fichas de comerciante solo nombra la segunda: se sigue la fila.
- **Propiedades no definidas en 30.1 en JSON-LD** (`productGroupId`, `lowprice`): ningún requisito las recoge, a diferencia de Microdata (`ws-serialization/032`).
- **Datos sin requisito técnico:** el sku `PADRE00000000` en 15 relacionados de Guaw y los `@id` de 5V Valverde con una ruta interna del servidor. No entran en ningún requisito técnico.
