# Primera pasada del inventario de Schema.org (T-047)

Fecha: 2026-10-27. Con la skill `/web-reference`: siete agentes por fuente y nivel, más las fichas que no son especificación aplicable, que se escribieron aparte. Función y estado de cada fuente: [inventory.md](../inventory.md).

## Resultado

`web-audit/bin/reqs check`:

```
correcto · 29 fichas (23 de especificaciones aplicables), 502 citas, 440 requisitos (208 obligatorias, 232 recomendadas)
sin ficha (2): gs1-web-vocabulary, gs1-web-vocabulary-standard
```

| Nivel | Especificación | Obligatorias | Recomendadas |
|---|---|---|---|
| Serialización (44) | `w3c-json-ld11` | 17 | 1 |
| | `whatwg-html-microdata` | 18 | 0 |
| | `w3c-rdfa-core` | 1 | 2 |
| | `w3c-html-rdfa` | 3 | 2 |
| Vocabulario (12) | `schemaorg` | 0 | 8 |
| | `schemaorg-data-model` | 0 | 2 |
| | `schemaorg-getting-started`, `schemaorg-faq` | 0 | 1 + 1 |
| Consumidor (384) | `google-search-merchant-listing` | 66 | 83 |
| | `google-search-product-snippet` | 11 | 16 |
| | `google-search-review-snippet` | 26 | 10 |
| | `google-search-product-variants` | 9 | 12 |
| | `google-search-return-policy` | 13 | 24 |
| | `google-search-shipping-policy` | 32 | 30 |
| | `google-search-organization` | 4 | 38 |
| | `google-search-sd-policies` | 8 | 2 |

**Fuentes añadidas (7), todas especificaciones aplicables:**
- serialización: `w3c-json-ld11-api`, `whatwg-html-microdata`, `w3c-rdfa-core` y `w3c-html-rdfa`;
- consumidor: `google-search-product-snippet`, `google-search-javascript` y `google-search-review-snippet`. Esta última se añadió por los tipos de las fichas reales: AggregateRating está en 10 fichas y Review en 5.

## Criterios de la pasada

1. **Remisión.** Si una especificación del perfil exige seguir otra del mismo consumidor, la otra entra como especificación aplicable:
   - `google-search-sd-policies`: «you must follow these guidelines», en las fichas de comerciante y en los fragmentos de producto;
   - `google-search-review-snippet`: «Follow the Review snippet guidelines…», en las filas `review` y `aggregateRating`.

   Cada ficha recoge la remisión en su `note`.
2. **Especificaciones sin requisitos propios.** `w3c-json-ld11-api` (sus MUST son del procesador) y `google-search-javascript` (Google procesa el marcado del DOM renderizado) sirven para el método y como citas adicionales. Las páginas de tipo de Schema.org son vistas de la release: los requisitos citan la release.
3. **Naturaleza.**
   - La cabecera de la tabla («Required properties», «Recommended properties») fija la naturaleza de la presencia de cada fila.
   - Las reglas de valor de una fila (formato, códigos, como mucho un valor) toman la naturaleza de la cabecera y lo explican en `rationale`, salvo que la fila diga must o should.
   - Una obligación condicional («Required if…», «if applicable») es de su naturaleza, con la condición en `applicability`.
4. **Aplicabilidad.** Es la existencia de lo que examina el requisito: la entidad, la sintaxis o el dato visible. Si no existe, el requisito es NA.
5. **Contenido visible.** Las condiciones que contrastan el marcado con la página se comprueban como presencia, nunca como verdad.
6. **Fuera:**
   - la conformidad de procesadores y agentes de usuario;
   - Search Console y Merchant Center;
   - lo que exige juzgar veracidad, licitud o relevancia (D-129): productos prohibidos, contenido engañoso, reseñas propias o incentivadas, «el tipo más específico»;
   - las filas sin término normativo («may», «can», «up to N»).

## Lo que no encaja en el canon

- **[I-47](../../../docs/30-governance/issues.md#i-47):** el GS1 Web Vocabulary no encaja en ninguna clase de fuente. Se propone la clase «vocabulario complementario»; sus dos fuentes siguen sin ficha.
- **[I-41](../../../docs/30-governance/issues.md#i-41), anotada:**
  - El dígito de control del GTIN lo recomienda Schema.org 30.1 (`ws-vocabulary/006`).
  - Las fichas de comerciante solo piden la forma numérica (`ws-consumer/026`).
  - La pregunta de I-41 sigue abierta, pero el requisito técnico es del vocabulario.

## Pendiente

### Fuentes por registrar (próxima pasada de `/web-reference`)

| Fuente | Por qué | Prioridad |
|---|---|---|
| HTML Living Standard, sección 4 (`meta`, `link`, `time` y `script` como bloque de datos) | La versión congelada de Microdata solo trae la sección 5. Lo que HTML exige al elemento que lleva el valor (meta con content, link con href, time con datetime) y al `script` de JSON-LD no tiene cita. Las 5 fichas con Microdata usan `<meta itemprop>`. | Alta |
| ISO 4217 e ISO 3166-1/2 | Comprobar los códigos de moneda, país y región queda en NE. | Media |
| Formatos de Google Images | El formato del logo (`ws-consumer/336`) queda en NE. | Baja |
| Namespaces in XML 1.1 y contextos iniciales de RDFa | `ws-serialization/037` y `041` dependen de ellos. Ninguna ficha real usa RDFa. | Baja |

### Decisiones de método comunes a los niveles (T-049)

- **HTML servido o DOM renderizado.**
  - Serialización examina el HTML servido. El consumidor contempla el DOM renderizado (`google-search-javascript`) y recomienda el marcado en el HTML inicial (`ws-consumer/201` y la directriz de fichas de comerciante).
  - Con JSON-LD inyectado por JavaScript, la serialización quedaría NA y el consumidor sí aplicaría.
  - Hace falta una regla común para los tres niveles (relación con el perfil de consumo no interactivo del canon).
- **Bloque JSON-LD roto.** `ws-serialization/001` queda no satisfecho y el resto de requisitos de ese bloque, NE. Hay que ver si encaja con el diseño del auditor.
- **Términos no definidos en 30.1.** Microdata exige que itemtype e itemprop estén definidos en el vocabulario (`ws-serialization/023` y las de itemprop); JSON-LD y Schema.org no lo exigen. Así, `productGroupId` solo incumple un requisito cuando va en Microdata.
- **Alcance en RDFa.** Las condiciones son del documento entero. Si una página tiene RDFa con Schema.org, también se comprueban sus etiquetas Open Graph (`ws-serialization/040`).

### Lecturas discutibles, para el contraste (T-048) o para revisión

- **Reglas de valor con la naturaleza de la cabecera** (criterio 3): unas 50 en el consumidor. Con una lectura estricta (sin must ni should no hay requisito) caerían.
- **Obligatorias solo por la cláusula general «you must follow these guidelines»:**
  - `ws-consumer/145`: la página permite comprar;
  - `182`: Product como tipo principal;
  - `197`: Product además de ProductGroup;
  - `208`: devoluciones bajo Organization;
  - `245`: ShippingService bajo Organization.
- **Cercanas a la consistencia transversal (D-124), comprobadas como presencia:**
  - `ws-vocabulary/003–004`;
  - `ws-consumer/141–142`, `181` y `183`;
  - `ws-consumer/377–380` y `382–383`.
- **Contradicciones dentro de una fuente:**
  - Fichas de comerciante: la fila priceType solo admite StrikethroughPrice, pero `#pricing-examples` admite ListPrice en transición. Se siguió la fila (`ws-consumer/079`).
  - Envío: las tablas de `orderValue` y `shippingRate` exigen dos propiedades y la introducción, una de las dos. Se siguió la introducción (`ws-consumer/296` y `299`).
- **Otras:**
  - `ws-serialization/002`: un array raíz con `@graph`, patrón frecuente en tiendas, incumple con la lectura estricta;
  - `018`: un SHOULD de una pauta de autoría;
  - `039`: «unnecessary whitespace»;
  - `ws-consumer/216`: lee «only when» como «se exige cuando»;
  - `352` y `365`: «omit itemReviewed» como obligatoria.
- **Recomendadas universales del consumidor** (color, material, size, gtin…): saldrán «no satisfecho» también en productos donde no son pertinentes. La pertinencia es del modelo de demanda, no de la evaluación técnica.
- **España:** `ws-consumer/119–121` (addressRegion y postalCode) serán casi siempre NA, porque Google solo los admite en otros países.

### Para T-048

- `demand-engine/var/pages/` tiene 45 fichas de solo 6 tiendas. T-048 pide 10 tiendas distintas: hay que capturar más, e incluir fichas con Microdata.
- Contrastar con Schema Markup Validator y Rich Results Test. Casos a mirar:
  - el array raíz con `@graph`;
  - `productGroupId` en Grupo Todoplano;
  - las reseñas de la tienda dadas como AggregateRating de la Organization (Burrito Blanco);
  - las reseñas con el texto en `description` en lugar de `reviewBody`.
