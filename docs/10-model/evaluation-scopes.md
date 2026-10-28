---
id: evaluation-scopes
title: Interfaces, ámbitos de evaluación y requisitos técnicos
layer: model
status: vigente
version: 1.6
updated: 2026-10-28
sources: [BASE §3, BASE §3.1, CTX §5, FUND §4, FUND §7.3, FUND §10.4, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-27-web-schema-technical-framework, INTAKE 2026-10-28-minimum-representation-image, INTAKE 2026-10-28-technical-informative-frontier, INTAKE 2026-10-28-minimum-members-structural-formation, INTAKE 2026-10-28-references-system]
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

Los evalúa el sistema **web-audit** en Web y Web Schema.org, empezando por Web Schema.org. Es solo técnico: no hace la evaluación informativa, que es de la auditoría GSC ([D-129](../30-governance/decisions.md#d-129)).

### Perfil de implementación

> El **perfil de implementación** es el conjunto de especificaciones aplicables respecto del cual se determinan los requisitos técnicos pertinentes de un ámbito y su naturaleza obligatoria o recomendada. — INTAKE 2026-10-27-web-schema-technical-framework

- La naturaleza **obligatoria o recomendada** de un requisito técnico es **relativa al perfil** que la establece. La fija la especificación, nunca el auditor.
- En **Web Schema.org**, el perfil tiene tres niveles:

| Nivel | Especificaciones | Qué fijan |
|---|---|---|
| **Serialización** | JSON-LD 1.1 (con su procesado), Microdata y RDFa 1.1 | Sintaxis y estructura del marcado |
| **Vocabulario** | Schema.org, versión fijada **30.1** | Tipos, propiedades, dominios, rangos y enumeraciones |
| **Consumidor** | Google Search: fichas de comerciante (Merchant listing), variantes de producto, políticas de devolución y de envío, organización y fragmentos de producto (Product snippet) | Lo que exige ese consumidor y la forma de lo que se publica. La presencia de lo que solo recomienda es, en general, apoyo del modelo de demanda del ámbito ([frontera](#frontera-entre-la-evaluación-técnica-y-la-informativa)) |

- Schema.org es permisivo por diseño: los rangos son tipos esperados, admite texto donde espera una entidad y no tiene propiedades obligatorias. Por eso las condiciones de sintaxis salen de la serialización, y las propiedades exigidas y recomendadas, de los consumidores. De las recomendadas, su presencia no es un requisito técnico, salvo las partes de la [formación estructural](#frontera-entre-la-evaluación-técnica-y-la-informativa) y los datos del mínimo de representación ([D-145](../30-governance/decisions.md#d-145), [D-147](../30-governance/decisions.md#d-147), [D-148](../30-governance/decisions.md#d-148)).
- La versión del vocabulario se fija y queda registrada con cada resultado. Cambiarla obliga a revisar los requisitos que dependen de ella.
- **Google Merchant Center** pertenece a Catálogos distribuidos. En Web Schema.org solo sirve para la [consistencia transversal](#consistencia-transversal).
- No se añaden otros consumidores por ahora; podrían añadirse como perfil nuevo ([D-130](../30-governance/decisions.md#d-130), interpretación adoptada). Los perfiles de Web (sin marcado) y de Catálogos distribuidos están pendientes.

### Estados del requisito técnico

| Estado | Valores | Tratamiento |
|---|---|---|
| **Satisfacción** | **Satisfecho** · **no satisfecho** | Según la comprobación de su método. |
| **Aplicabilidad** | **No aplicable (NA)** | El requisito no corresponde al perfil o al recurso examinado. Se justifica y se separa de los pertinentes. |
| **Evaluación** | **No evaluable (NE)** | **Incidencia de la auditoría:** una comprobación que no se pudo hacer. No es una puntuación y **no equivale a «no satisfecho»**. |

NE recibe el mismo tratamiento que en la evaluación informativa ([scoring-systems](scoring-systems.md#grado-de-satisfacción-de-criterio-gsc)). El sistema cuantitativo (cómo entran las obligatorias y las recomendadas en la tasa, umbrales y cobertura) sigue abierto; **no se fijan pesos** ([D-131](../30-governance/decisions.md#d-131)).

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
   - su naturaleza **obligatoria o recomendada**, según su [perfil](#perfil-de-implementación);
   - el método de comprobación;
   - la evidencia;
   - los [estados](#estados-del-requisito-técnico) de satisfacción, aplicabilidad y evaluación.

## Fuentes de los requisitos técnicos

1. Solo una **especificación aplicable** (de serialización, de vocabulario o de un consumidor) fundamenta un requisito técnico. Las demás fuentes tienen otra función:

| Clase | Ejemplos | Función |
|---|---|---|
| Instrumento del sistema | SHACL, PROV-O | Sirven para construir el auditor (perfiles como restricciones, procedencia de las evidencias); no son condiciones que deba cumplir el ecommerce. |
| Principios generales | W3C Data on the Web Best Practices | Orientan; no dan requisitos comprobables de una ficha. |
| Método de comprobación | Schema Markup Validator, Rich Results Test | Sirven para comprobar y calibrar; no son fuente de criterios ni equivalen a calidad informativa. |
| Práctica de terceros | Skills de auditoría SEO | Listas de errores frecuentes, sin autoridad. |
| Antecedente histórico | GS1 SmartSearch (2015) | Solo contexto. |
| Datos comerciales distribuidos | Merchant Center | Catálogos distribuidos y consistencia transversal. |

2. Un requisito técnico expresa **una sola condición comprobable**.
3. Cada requisito técnico **cita literalmente** su especificación: fuente, sección y versión congelada ([D-132](../30-governance/decisions.md#d-132)).
4. **Referencia técnica:** vive en `web-audit/reference/`, como datos y fichas gobernados por el canon, igual que el catálogo de bloques del modelo de demanda. Reúne una ficha por fuente con citas literales y los requisitos técnicos, con los campos de la regla 7, su perfil y su cita. Las fuentes congeladas por versión (fuera de git) viven en `references/`, la custodia común de las fuentes externas de todos los sistemas; la referencia las cita a su versión fijada (enmendada por [D-149](../30-governance/decisions.md#d-149)).
5. Los requisitos técnicos los **deciden los agentes**, siempre con cita; el usuario los revisa si lo pide. Una skill los crea y los mantiene (añadir una fuente, actualizar ante una versión nueva, validar) y no crea conceptos, estados, pesos ni fórmulas: si le falta algo, va al intake ([D-133](../30-governance/decisions.md#d-133)).
6. La auditoría GSC puede consultar la referencia para **interpretar** el marcado. Eso no convierte los requisitos técnicos en criterios informativos ([D-129](../30-governance/decisions.md#d-129)).

## Perfil de consumo no interactivo

En Web, el perfil de consumo no interactivo debe precisar **qué información puede recuperarse y leerse sin operar la página**. Cuando sea relevante, se documenta si la exposición de los datos depende de ejecutar JavaScript. Esa circunstancia **no se convierte en una prohibición técnica universal** desligada de las vías de consumo definidas.

Puede revisarse de forma auxiliar la política de acceso para sistemas automatizados y la existencia de bloqueos efectivos, cuando afecten a las vías examinadas. Eso **no** constituye una auditoría integral del rastreo, la infraestructura o la seguridad.

## Punto de contacto entre la evaluación técnica y la informativa

La comprobación informativa **no reproduce** los controles técnicos. Atiende a la exposición técnica solo por sus **consecuencias para el RI examinado**: si la información pertinente puede obtenerse y leerse efectivamente con el perfil de consumo definido. Ver [effective-availability](effective-availability.md).

- La conformidad técnica general **no sustituye** a esta comprobación contextual.
- Una incidencia técnica **no determina automáticamente** una insuficiencia informativa.
- Si un factor técnico (formato, marcado, transformación, validación, distribución, mecanismo de acceso) impide consumir la información pertinente, su **consecuencia informativa** se refleja en la disponibilidad efectiva. La **causa** y el incumplimiento se documentan en el expediente técnico.
- Los datos del [mínimo de representación](commercial-information.md#mínimo-de-representación) se examinan en la técnica, que dice si existen y están bien formados (en Web Schema.org, los de la [lista del mínimo](commercial-information.md#mínimo-de-representación), [D-147](../30-governance/decisions.md#d-147)). Los que llevan un hecho comercial se examinan también en la informativa, por lo que transmiten; los de sostén, solo en la técnica ([D-143](../30-governance/decisions.md#d-143)).

**Ejemplo:** una incidencia de marcado Schema.org puede ser relevante para la conformidad técnica. Si en **Web** la información que exige el RI también se obtiene y se lee en HTML admisible, esa incidencia no demuestra por sí misma falta de disponibilidad ni deficiencia de los criterios informativos de Web. En **Web Schema.org** hay que comprobar por separado qué información pertinente del marcado puede utilizarse.

### Frontera entre la evaluación técnica y la informativa

Se formula para el perfil de Web Schema.org; los perfiles de Web y de Catálogos distribuidos siguen en [OQ-30](../30-governance/open-questions.md#f-evaluación-técnica).

> - **Evaluación técnica:** cómo está construido lo que se publica, más la presencia de lo que el consumidor **exige**.
> - **Evaluación informativa:** si se publica lo que el consumidor solo **recomienda**, como cualquier otra cuestión del modelo de demanda: disponibilidad efectiva y criterios de aceptación.
> - **El criterio es la naturaleza que fija la especificación** (obligatoria o recomendada), no un juicio del auditor. Vale igual en el primer nivel y en lo anidado.
>
> — INTAKE 2026-10-28-technical-informative-frontier

- **Lo técnico** ([D-145](../30-governance/decisions.md#d-145), [D-148](../30-governance/decisions.md#d-148)) son tres categorías y dos presencias:
  - sintaxis y vocabulario;
  - acceso y exposición;
  - **formación estructural**, que incluye la forma del valor (formatos, códigos, enumeraciones, cardinalidad), también la de lo recomendado;
  - presencia de los datos exigidos de primer nivel (name, image y offers del Product; precio y moneda de la Offer). Lo exigido incluye lo condicional, con la condición como aplicabilidad del requisito: en la referencia, 169 obligatorios del consumidor, 9 universales y 160 condicionales ([D-147](../30-governance/decisions.md#d-147));
  - presencia de los datos del mínimo de representación.

> **Formación estructural** (técnica): cuando se publica una estructura,
> 1. tiene las partes que el consumidor **exige** para ella;
> 2. tiene las partes sin las que un valor publicado **no se puede interpretar**: la unidad del peso, la escala de una valoración (`bestRating`/`worstRating`), el sistema de tallas, la moneda de un precio unitario;
> 3. sus partes son **coherentes entre sí**: con `doesNotShip` no hay tarifa; con devolución gratuita no hay importe de devolución.
>
> Las partes que solo **añaden otro hecho** (tipo de reembolso, tarifa de reposición, tiempo de preparación de un servicio de envío) son presencia de lo recomendado → informativa.
>
> — INTAKE 2026-10-28-minimum-members-structural-formation

- La estructura puede ser opcional y estar incluida: lo que cuenta es que, si se publica, no quede incompleta. Ejemplo con el envío en la oferta:
  - sin `shippingDetails` (recomendado): no es un defecto técnico; la informativa juzga si el ámbito responde al coste y al plazo del envío;
  - con `shippingDetails` y sin `deliveryTime`, que Google exige dentro de esa estructura (`ws-consumer/105`): técnico, estructura incompleta; la informativa ve además su efecto en el plazo de entrega (gen/08);
  - con todas las partes exigidas y sin `handlingTime` (recomendado, `122`): solo informativo, es un hecho más sobre el plazo.
- Lectura de [D-148](../30-governance/decisions.md#d-148): la coherencia entre partes recoge también las reglas de estructura del marcado de la página, como una sola moneda (`ws-consumer/147`, `174`) o URL distintas por variante (`200`).
- **Doble lectura, solo en lo exigido.** Si falta el precio, la técnica dice que el consumidor lo exige y falta; la informativa, que la cuestión no tiene respuesta en el ámbito. No es doble cómputo: la incidencia técnica y su efecto sobre la disponibilidad se registran por separado (punto de contacto, arriba).
- **Mínimo de representación:** mantiene en la técnica los datos del [mínimo](commercial-information.md#mínimo-de-representación) que el consumidor recomienda sin exigir; en Web Schema.org, nueve requisitos ([D-147](../30-governance/decisions.md#d-147)).
- **Lo recomendado** pasa a ser apoyo del modelo de demanda del ámbito Web Schema.org: ver [demand-model](demand-model.md#relación-con-los-ámbitos-de-evaluación).

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

- Los requisitos técnicos concretos (en web-audit), el método y la cobertura de cada uno, el sistema cuantitativo técnico y los perfiles de Web (sin marcado) y de Catálogos distribuidos. Ver [OQ-30](../30-governance/open-questions.md#f-evaluación-técnica).
- Frontera entre la sintaxis técnica y la estructura del dato cuando un perfil de consumidor exige un valor válido (GTIN). ⚠ Ver [I-41](../30-governance/issues.md#i-41).

## Relacionado

- [effective-availability](effective-availability.md)
- [evaluation-architecture](evaluation-architecture.md)
- [scoring-systems](scoring-systems.md#tasa-de-cumplimiento-técnico)
