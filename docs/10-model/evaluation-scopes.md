---
id: evaluation-scopes
title: Interfaces, ámbitos de evaluación y requisitos técnicos
layer: model
status: vigente
version: 1.1
updated: 2026-10-27
sources: [BASE §3, BASE §3.1, CTX §5, FUND §4, FUND §7.3, FUND §10.4, INTAKE 2026-10-27-ac-applicability-and-reliability]
---

# Interfaces, ámbitos de evaluación y requisitos técnicos

## Definición

### Interfaces de exposición

> Las **interfaces de exposición** son los medios técnicos mediante los que el ecommerce publica, estructura y distribuye información comercial para su consulta y utilización por otros sistemas. — BASE §3

### Ámbitos de evaluación

El sistema establece tres **ámbitos de evaluación**. Cada ámbito determina qué información se examina y qué requisitos informativos son pertinentes.

| Ámbito | Información comercial examinada | Áreas de comprobación técnica |
|---|---|---|
| **Catálogos distribuidos** | Información publicada y distribuida mediante feeds y catálogos destinados a plataformas como Google Merchant Center y Meta Commerce. | Generación, transformación, formato, validación, actualización, entrega, sincronización y distribución. |
| **Web** | Información del recurso web en su conjunto, incluidos el contenido HTML y el marcado Schema.org. | Publicación, recuperación, lectura efectiva y presencia del marcado Schema.org. |
| **Web Schema.org** | Información expresada mediante el marcado Schema.org, considerada aisladamente del resto del contenido HTML. | Sintaxis, estructura, vocabularios y conformidad con las especificaciones del marcado. |

### Requisitos técnicos generales

> Los **requisitos técnicos generales** expresan las condiciones de implementación, publicación, acceso, consumo y distribución aplicables a cada ámbito, según sus especificaciones. — BASE §3.1

- **Web:** se comprueban las condiciones técnicas de recuperación y lectura del recurso, incluida la **implementación de marcado Schema.org como requisito técnico**.
- **Web Schema.org:** se examinan los requisitos técnicos específicos del marcado (sintaxis, estructura, conformidad).
- **Catálogos distribuidos:** se examinan generación, formato, validación, actualización, entrega y distribución **por perfil**.

## Reglas e invariantes

1. **Web y Web Schema.org no son independientes** en la información que contienen: Web incluye el marcado Schema.org. Sus resultados se mantienen **diferenciados** y **no se suman ni se promedian automáticamente**.
2. **Web** examina la capacidad de resolución conjunta del recurso, se exprese la información en HTML o en Schema.org. Las afirmaciones de ambas representaciones pueden combinarse si las relaciones están justificadas.
3. **Web Schema.org** examina solo la representación estructurada. **No usa el resto del HTML para completar respuestas.**
4. Cada ámbito tiene su propio conjunto de requisitos informativos pertinentes, derivados del catálogo del [modelo de demanda](demand-model.md). **Un ámbito no es defectuoso por omitir una cuestión que no le corresponde exponer** según su función y alcance.
5. La evaluación técnica usa un **sistema cuantitativo propio**, independiente de la evaluación de calidad informativa. Las [propiedades de calidad](quality-properties.md) pertenecen **exclusivamente** al modelo informativo y no son unidades de evaluación técnica.
6. La revisión de requisitos técnicos **no depende** de haber seleccionado antes una pregunta del catálogo de demanda.
7. Para cada requisito técnico se documentan:
   - el ámbito;
   - la especificación aplicable;
   - su naturaleza **obligatoria o recomendada**;
   - el método de comprobación;
   - la evidencia;
   - los estados de satisfacción, aplicabilidad y evaluación.

## Perfil de consumo no interactivo

En Web, el perfil de consumo no interactivo debe precisar **qué información puede recuperarse y leerse sin operar la página**. Cuando sea relevante, se documenta si la exposición de los datos depende de ejecutar JavaScript. Esa circunstancia **no se convierte en una prohibición técnica universal** desligada de las vías de consumo definidas.

Puede revisarse de forma auxiliar la política de acceso para sistemas automatizados y la existencia de bloqueos efectivos, cuando afecten a las vías examinadas. Eso **no** constituye una auditoría integral del rastreo, la infraestructura o la seguridad.

## Punto de contacto entre la evaluación técnica y la informativa

La comprobación informativa **no reproduce** los controles técnicos. Atiende a la exposición técnica solo por sus **consecuencias para el RI examinado**: si la información pertinente puede obtenerse y leerse efectivamente con el perfil de consumo definido. Ver [effective-availability](effective-availability.md).

- La conformidad técnica general **no sustituye** a esta comprobación contextual.
- Una incidencia técnica **no determina automáticamente** una insuficiencia informativa.
- Si un factor técnico (formato, marcado, transformación, validación, distribución, mecanismo de acceso) impide consumir la información pertinente, su **consecuencia informativa** se refleja en la disponibilidad efectiva. La **causa** y el incumplimiento se documentan en el expediente técnico.

**Ejemplo:** una incidencia de marcado Schema.org puede ser relevante para la conformidad técnica. Si en **Web** la información que exige el RI también se obtiene y se lee en HTML admisible, esa incidencia no demuestra por sí misma falta de disponibilidad ni deficiencia de los criterios informativos de Web. En **Web Schema.org** hay que comprobar por separado qué información pertinente del marcado puede utilizarse.

## Complementariedad y coherencia entre representaciones

- La información de distintas representaciones puede ser complementaria. Para interpretarla hay que preservar la **identidad de producto, variante, oferta o vendedor**, el alcance comercial, las condiciones y el momento de cada afirmación.
- Una discrepancia solo es una **contradicción material** cuando las afirmaciones se refieren a **la misma realidad comercial bajo condiciones y momentos comparables**.
- **La coincidencia entre representaciones no demuestra por sí sola la exactitud** de lo afirmado.
- Web y Web Schema.org comparten parte de la información examinada, pero tienen **finalidades evaluativas diferentes**. La evaluación de Web Schema.org identifica las capacidades y limitaciones de la representación estructurada **sin sustituir la evaluación conjunta del recurso web** (FUND §4.1, §4.3).
- Una limitación observada en Web Schema.org **no implica necesariamente** una limitación equivalente en Web, porque el HTML puede aportar información complementaria. Los resultados se documentan por separado, conservando la procedencia de cada afirmación y las discrepancias entre representaciones.

### Consistencia transversal

> La consistencia se puede evaluar para cada ámbito y, a nivel transversal, «adquiere una nueva dimensión de análisis». **Unidad:** RI × par de ámbitos. **Forma:** hallazgos sin escala; por RI y par de ámbitos, hecho, valores, momento, materialidad, y si la diferencia es legítima (p. ej., un precio propio de un canal, declarado). Una diferencia legítima y declarada no es incoherencia. **No modifica el GSC de ningún ámbito ni se agrega.** — INTAKE 2026-10-27-ac-applicability-and-reliability

- **Lo que aporta:** lo que el juicio por ámbito no puede expresar. Ejemplo (hipotético): un marcado coherente consigo mismo a 89 € en una página que dice 79 €; quien solo lee el marcado no puede saberlo. Lo mismo, un feed desfasado.
- **Por qué no toca el GSC:** no se puede saber cuál de los dos lados está mal, y mezclarlos rompería la separación de Web y Web Schema.org. La consistencia **dentro** de cada ámbito sí cuenta en su Fiabilidad ([acceptance-criteria](acceptance-criteria.md#fiabilidad-lectura-refutadora-y-comprobaciones)).
- **Pares:**
  - Catálogos distribuidos ↔ Web;
  - Catálogos distribuidos ↔ Web Schema.org;
  - HTML ↔ Web Schema.org: el mismo hallazgo que ya ve Web, reutilizado;
  - entre perfiles de Catálogos distribuidos (Google, Meta).
- **Condiciones de operación:** captura de los ámbitos en un momento comparable; identidad de la entidad entre ámbitos (GTIN, SKU o `item_group_id` frente a URL y variante); acceso al feed.
- Es una dimensión de análisis, no un indicador ni una escala ([D-124](../30-governance/decisions.md#d-124)). Un estado cualitativo por RI queda pendiente ([OQ-67](../30-governance/open-questions.md)).

## Distinciones

- **Interfaz** y **ámbito de evaluación**. En la unidad de evaluación (RI × interfaz / RI × ámbito) y en los sistemas de valoración son **sinónimos** ([D-010](../30-governance/decisions.md#d-010)). Fuera de ese contexto, «interfaz de exposición» designa además el medio técnico mediante el que se publica la información. En texto nuevo se prefiere «ámbito» para la unidad evaluada.
- **Legibilidad técnica u operativa** frente a **P09 · Claridad** y **P10 · Estructuración semántica**. Ver [quality-properties](quality-properties.md#lectura-efectiva-frente-a-propiedades-semánticas).

## Pendiente

- Completar los perfiles de implementación, obligaciones, recomendaciones, métodos y cobertura de los controles técnicos de cada ámbito. Ver [open-questions](../30-governance/open-questions.md).

## Relacionado

- [effective-availability](effective-availability.md)
- [evaluation-architecture](evaluation-architecture.md)
- [scoring-systems](scoring-systems.md#tasa-de-cumplimiento-técnico)
