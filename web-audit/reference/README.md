# Referencia técnica

Fichas de fuente con citas literales y requisitos técnicos de la evaluación técnica ([D-133](../../docs/30-governance/decisions.md#d-133)). Son datos gobernados por el canon: [evaluation-scopes](../../docs/10-model/evaluation-scopes.md#requisitos-técnicos-generales) (perfil de implementación, estados del requisito técnico y fuentes) prevalece sobre todo lo de aquí. Los requisitos los deciden los agentes, siempre con cita; el usuario los revisa si lo pide. Se crean y se mantienen con la skill `/web-reference` y se validan con `web-audit/bin/reqs check`.

```
reference/
├── sources.json              registro de fuentes que congela refs (ver el README de web-audit)
├── inventory.md              inventario: función y estado de cada fuente, las que quedan fuera del
│                             registro y la cobertura de los tipos de las fichas reales
├── cards/<fuente>.json       ficha de cada fuente registrada
├── requirements/<nivel>.json requisitos técnicos de un nivel del perfil de Web Schema.org:
│                             serialization.json · vocabulary.json · consumer.json
└── reports/                  informe de cada pasada de la skill (fecha-tema.md)
```

## Ficha de fuente

Una por fuente registrada, con su id como nombre de fichero. Dice qué función tiene la fuente en el canon y guarda las citas literales que fundamentan los requisitos.

| Campo | Contenido |
|---|---|
| `source` | Id de la fuente en `sources.json`. |
| `version` | La versión que cita la ficha. Ha de ser la **fijada** (`var/refs/pins.json`). |
| `class` | Su clase según el canon ([D-132](../../docs/30-governance/decisions.md#d-132)): `especificación aplicable`, `instrumento del sistema`, `principios generales`, `método de comprobación`, `práctica de terceros`, `antecedente histórico` o `datos comerciales distribuidos`. |
| `level` | Solo en una especificación aplicable: su nivel del perfil ([D-130](../../docs/30-governance/decisions.md#d-130)), `serialización`, `vocabulario` o `consumidor`. |
| `summary` | Qué fija la fuente o para qué sirve, en una o dos frases. |
| `quotes` | Citas: `id` (`q01`, `q02`…; no se reutiliza), `section` y `text` (literal). Opcional, `note`. |
| `note` | Opcional. |

**Secciones.** Una cita es un fragmento continuo de una sección de la versión fijada:

- **Página HTML** (`text.md`): el ancla del encabezado, `#product-properties` para `## Product {#product-properties}`. Si el encabezado no tiene ancla, su texto. La sección llega hasta el siguiente encabezado del mismo nivel o superior, con sus subsecciones.
- **Vocabulario en JSON-LD** (la release de Schema.org, `gs1Voc.jsonld`): el término, `schema:gtin`. La cita es parte de su definición (`rdfs:comment`).
- **PDF:** no tiene texto citable.

`web-audit/bin/reqs section FUENTE` lista las secciones y `reqs section FUENTE SECCIÓN` muestra el texto tal como lo lee la validación: las citas se copian de ahí. Al comparar solo cuentan las palabras, no los saltos de línea ni los espacios. No se parafrasea, no se traduce y no se unen fragmentos.

## Requisito técnico

Cada fichero de `requirements/` es un nivel del perfil de implementación de Web Schema.org: `{"level": "consumidor", "requirements": [...]}`. Un requisito tiene los campos que pide el canon ([regla 7](../../docs/10-model/evaluation-scopes.md#reglas-e-invariantes)), su perfil y su cita, y ningún otro:

| Campo | Contenido | En el canon |
|---|---|---|
| `id` | `ws-<nivel>/NNN`, con el nivel del fichero (`ws-consumer/001`). No se reutiliza. | — |
| `scope` | `Web Schema.org`, el único ámbito con perfil; Web y Catálogos distribuidos, [OQ-30](../../docs/30-governance/open-questions.md#f-evaluación-técnica). | ámbito |
| `spec` | Fuente con ficha de especificación aplicable y del nivel del fichero. | especificación aplicable |
| `condition` | Una sola condición comprobable, en una frase. Si se cumple, el requisito está satisfecho. | estado de satisfacción |
| `nature` | `obligatoria` o `recomendada`, la que fija la especificación, nunca el auditor. | naturaleza |
| `quotes` | Citas de las fichas (`fuente#q01`), al menos una de `spec`. Entre las de `spec`, el texto que fija la naturaleza. | cita ([D-132](../../docs/30-governance/decisions.md#d-132)) |
| `method` | Cómo se comprueba la condición. | método de comprobación |
| `evidence` | Qué se registra como evidencia. | evidencia |
| `applicability` | `universal` o el hecho del recurso del que depende. Si no se da, es NA. | estado de aplicabilidad |
| `not_evaluable` | Causas propias por las que la comprobación puede no hacerse (NE); `[]` si solo tiene las comunes, como no obtener el recurso o su marcado. | estado de evaluación |
| `rationale` | Opcional: por qué la condición sale de la cita. | — |

El perfil del requisito es su ámbito, el nivel de su fichero y su especificación. Su versión es la de la ficha de `spec`. Los estados son los del canon ([D-131](../../docs/30-governance/decisions.md#d-131)): estos campos dicen cuándo se da cada uno, sin añadir valores, pesos, puntuaciones ni umbrales.

**Una especificación por requisito.** Si dos especificaciones fijan la misma condición (`name` en las fichas de comerciante y en los fragmentos de producto), cada una tiene su requisito, con su naturaleza. Cómo cuentan en la tasa de cumplimiento técnico es del sistema cuantitativo, que sigue abierto (OQ-30).

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
 {"id": "ws-consumer/001", "scope": "Web Schema.org", "spec": "google-search-merchant-listing",
  "condition": "Cada entidad Product del marcado tiene la propiedad offers.", "nature": "obligatoria",
  "quotes": ["google-search-merchant-listing#q01", "google-search-merchant-listing#q02", "google-search-merchant-listing#q03"],
  "method": "Extraer las entidades Product del marcado (JSON-LD, Microdata y RDFa) y comprobar que cada una tiene al menos un valor de offers.",
  "evidence": "Por cada Product: su localización en el marcado y los valores de offers, o su ausencia.",
  "applicability": "universal", "not_evaluable": []}]}
```

## Validación

`web-audit/bin/reqs check` se ejecuta en el host y sale con error si encuentra algún problema:

- **Formato:** campos obligatorios presentes, ningún campo fuera del formato, valores del canon (clase, nivel, ámbito y naturaleza), ids únicos y con su forma.
- **Citas:** la ficha cita la versión fijada y cada cita está, literal, en su sección de esa versión. Tras `refs pin`, la comprobación falla hasta que se revisan las fichas de la fuente.
- **Requisitos:** su especificación es aplicable y del nivel del fichero. Cada cita existe y es de una especificación aplicable. Al menos una es de `spec`, y alguna de las de `spec` contiene el término de su naturaleza (must, required o shall para obligatoria; should o recommend para recomendada). La condición es una sola frase, sin «;».
- **Resumen:** fichas, citas y requisitos por naturaleza, y las fuentes registradas sin ficha.

No puede comprobar el sentido. Que la condición sea **una** sola, que la clase y el nivel sean los de la tabla del canon y que la cita fundamente de verdad la condición quedan a cargo de quien la escribe, con las reglas de la skill.
