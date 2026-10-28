---
id: construction-routes
title: Vías de construcción del modelo de demanda
layer: model
status: vigente
version: 1.7
updated: 2026-10-28
sources: [INTAKE 2026-10-28-paa-control-review-rules, INTAKE 2026-10-28-paa-parent-and-material, BASE §4.2, INTAKE 2026-10-25-requirement-blocks, INTAKE 2026-10-25-amazon-source-blocks, INTAKE 2026-10-25-training-runtime, INTAKE 2026-10-25-induced-rules, INTAKE 2026-10-26-choice-criteria-and-descriptions, INTAKE 2026-10-27-paa-construction-route, INTAKE 2026-10-27-paa-new-requirements, INTAKE 2026-10-27-paa-classification-criteria, INTAKE 2026-10-27-paa-training, INTAKE 2026-10-27-assessment-hints, INTAKE 2026-10-27-hint-fields]
---

# Vías de construcción del modelo de demanda

Cómo se construye el catálogo del [modelo de demanda](demand-model.md): sus fuentes, organizadas en vías, y el origen que lleva cada requisito. Separado de demand-model por tamaño ([D-098](../30-governance/decisions.md#d-098)); el contenido no cambia.

## Definición

> El catálogo se construye mediante **inferencia a partir de fuentes de referencia** que reflejan cómo se caracterizan, diferencian y comercializan las ofertas de la clase estudiada. — BASE §4.2

## Reglas e invariantes

Las fuentes se organizan en **vías de referencia complementarias** (BASE §4.2, enmendada por [D-009](../30-governance/decisions.md#d-009) y por [D-094](../30-governance/decisions.md#d-094)):

1. **Taxonomía de clases de producto.** Delimita la clase y permite reconocer atributos, facetas y dimensiones del dominio. Su estructura principal es la **Shopify Product Taxonomy**. Amazon (especialización) y Google (contraste) son fuentes de apoyo de la taxonomía. Google y el árbol de navegación de Amazon son solo de apoyo, no fuentes directas de RI; los PTD de Amazon pueden además ser fuente de requisitos de la categoría (enmendada por [D-039](../30-governance/decisions.md#d-039)). Denominación canónica según [D-012](../30-governance/decisions.md#d-012).
2. **MPIR: información comercial publicada por ecommerce referentes.** Permite reconocer [criterios de elección](choice-criteria.md), preguntas anticipadas, contextos, relaciones y condiciones que la taxonomía no anticipa. Un criterio de elección genera un requisito cuando cumple las condiciones C1–C4 ([D-091](../30-governance/decisions.md#d-091)). **Aparcado** ([D-095](../30-governance/decisions.md#d-095)): su método sigue en el canon como propuesta, pero no se ejecuta ni se desarrolla por ahora; su papel en la construcción lo cumple PAA, y retomarlo es una decisión nueva.
3. **People Also Ask (PAA)** ([D-094](../30-governance/decisions.md#d-094)):

   > Las preguntas de «Más preguntas» (People Also Ask) de google.es, recogidas para un conjunto de semillas de una clase, son una **vía de construcción** del modelo de demanda. Son preguntas de los compradores, filtradas por Google. Sirven para:
   >
   > - **reconocer criterios de elección** de la clase (las preguntas valorativas), a los que se aplica la regla C1–C4 (D-091);
   > - **confirmar requisitos** del catálogo;
   > - **confirmar o revisar cuestiones inferidas**: lo que D-036 encargaba al MPIR «cuando exista» lo hace PAA.
   >
   > Solo se conservan las **preguntas**. Las respuestas son texto de la IA de Google («Vista creada con IA»), no evidencia de ninguna página: ni se leen ni se cargan. PAA no aporta información resolutiva.
   >
   > Como cualquier fuente, PAA no prueba por sí sola la importancia relativa, que sigue saliendo de las reglas. Que una pregunta aparezca, o en qué posición, no se puntúa.
   >
   > — INTAKE 2026-10-27-paa-construction-route

   Enmendada por [D-099](../30-governance/decisions.md#d-099), que añade un cuarto uso:

   > Además de reconocer criterios de elección, confirmar requisitos y confirmar o revisar cuestiones inferidas, PAA **propone requisitos nuevos**, por un solo camino:
   >
   > 1. La pregunta está dentro del perímetro y trata de la clase, no de una marca ni de una tienda.
   > 2. Ningún requisito del catálogo la responde sin derivar.
   > 3. Cumple C1–C4 (D-091). C2 a C4 sirven igual para una pregunta factual: es un hecho declarable, se aplica a toda la clase y se puede formular de forma neutral.
   > 4. Entra como requisito candidato, con origen «paa» y la pregunta como fuente.
   >
   > Las preguntas valorativas siguen pasando por su criterio de elección, como hasta ahora.
   >
   > — INTAKE 2026-10-27-paa-new-requirements

   **Lectura de las preguntas** (`INTAKE 2026-10-27-paa-classification-criteria`):

   - **Perímetro:** la confección casera (coser, hacer o arreglar la pieza) queda fuera, porque no hay compra ([D-100](../30-governance/decisions.md#d-100)). Las preguntas sobre otro producto (un hermano, o lo que solo tiene sentido para otro producto) quedan fuera siempre; las de la categoría madre van dentro cuando preguntan por algo que la clase hereda de su bloque, y las del material, cuando la clase tiene o hereda ese material. El perímetro va antes de la [lectura sobre la oferta](choice-criteria.md#lectura-de-las-preguntas-de-paa), que no lo decide ([D-141](../30-governance/decisions.md#d-141), `INTAKE 2026-10-28-paa-control-review-rules`; [D-146](../30-governance/decisions.md#d-146), `INTAKE 2026-10-28-paa-parent-and-material`).
   - **Confirmaciones y aportaciones de precisión** ([D-101](../30-governance/decisions.md#d-101)):

     - Una pregunta por el significado de un término («¿La microfibra es plástico?», «¿Qué significa 144 hilos?») confirma el requisito del atributo y propone aportaciones de precisión para él (la denominación de la fibra según el Reglamento (UE) 1007/2011, la unidad del recuento de hilos, la equivalencia en cm de una denominación de talla). No genera requisitos nuevos.
     - Una pregunta de tienda o marca que nombra un atributo («¿Dónde comprar sábanas 100 % algodón?») confirma el requisito de ese atributo: quien compra busca y filtra por él (función Descubrir). Sigue sin proponer requisitos.
     - El precio sin tienda («¿Cuánto cuesta una sábana de lino?») es una pregunta de clase y confirma `gen/04`.
     - La verificación («¿Cómo saber si es 100 % algodón?») confirma la composición y propone la aportación «certificación del contenido o del origen de la fibra».

   - **Criterios de elección** y candidatos: reglas de lectura en [choice-criteria](choice-criteria.md#lectura-de-las-preguntas-de-paa) ([D-100](../30-governance/decisions.md#d-100) a [D-106](../30-governance/decisions.md#d-106)).

   La estrategia de semillas es operativa y vive en el [README del motor PAA](../../demand-engine/src/demand_engine/paa/README.md#estrategia-de-semillas). PAA tiene un [entrenamiento propio](paa-training.md), que refina las semillas, el vocabulario de criterios y los parámetros de las reglas de lectura, y escribe en el catálogo lo que es de PAA ([D-114](../30-governance/decisions.md#d-114), [D-115](../30-governance/decisions.md#d-115)). **Legitimidad:** el motor PAA no aplica el robots.txt de Google, por una excepción a [D-042](../30-governance/decisions.md#d-042) para investigación y uso interno, con sus límites de ejecución ([D-096](../30-governance/decisions.md#d-096)).

> **Amazon como fuente:** […] que las propiedades de los PTD de Amazon, incluidos los valores de special_feature, puedan ser fuente de requisitos de la categoría cuando son relevantes para la clase, con origen «referencias». — INTAKE 2026-10-25-amazon-source-blocks

Así, una cuestión que solo recoge un PTD de Amazon y que cuenta como base para decidir una especialización ([D-030](../30-governance/decisions.md#d-030)) puede entrar en el modelo con origen «referencias», si es relevante para la clase ([D-039](../30-governance/decisions.md#d-039)). Si después una regla de relevancia la excluye en una clase, el efecto sobre esa base lo mide la validación automática del entrenamiento: no se acepta una relevancia que deje hechos declarados sin pregunta ([D-050](../30-governance/decisions.md#d-050), [D-072](../30-governance/decisions.md#d-072)).

A ellas se suman las cuestiones inferidas ([D-036](../30-governance/decisions.md#d-036)):

> Hay cuestiones de toda la clase que ninguna referencia recoge. […] El usuario eligió la opción b (el clasificador las propone) […]. Lectura de Claude que siguió a esa propuesta y que el usuario no objetó:
>
> - Entran en el modelo como provisionales, en el régimen de D-022: se usan en la auditoría, el usuario valida siempre las críticas y una muestra del resto, y el MPIR las confirma o revisa cuando exista.
> - Controles: solo cuestiones de toda la clase, neutrales, justificadas y que no dupliquen la base; origen marcado («referencias» o «inferida»); la auditoría puede informar con ellas y sin ellas; la estabilidad se mide con dos ejecuciones por caso.
>
> — INTAKE 2026-10-25-requirement-blocks; matizada por [D-041](../30-governance/decisions.md#d-041): la validación se hace en entrenamiento y no bloquea la ejecución; enmendada por [D-044](../30-governance/decisions.md#d-044): la validación la hace el entrenamiento contra el marco, no la persona responsable; enmendada por [D-094](../30-governance/decisions.md#d-094): las confirma o revisa PAA, no el MPIR

**Origen de un requisito:** «referencias», «normativa», «inferida» o «paa».

> Un requisito que entra en el catálogo **solo** por PAA […] lleva origen **«paa»**, con las preguntas que lo apoyan como fuentes. Se suma a «referencias», «normativa» e «inferida».
>
> - Si una referencia o una norma lo recoge, conserva su origen; las preguntas PAA se añaden como apoyo.
> - Una cuestión inferida que PAA confirma pasa a origen «paa», con sus preguntas como fuentes.
> - «paa» es un origen de requisitos, no de aportaciones resolutivas: PAA no aporta información resolutiva.
> - Como las inferidas, la auditoría puede informar con ellos y sin ellos.
>
> — INTAKE 2026-10-27-paa-construction-route ([D-097](../30-governance/decisions.md#d-097)); enmendada por [D-099](../30-governance/decisions.md#d-099): «paa» tanto si el requisito sale de un criterio de elección como de una pregunta factual (INTAKE 2026-10-27-paa-new-requirements)

**Recorrido:**

1. Observar los atributos y la información comercial publicada.
2. Inferir cuestiones relevantes para la compra.
3. Formular y normalizar los requisitos.
4. Justificar su inclusión e importancia relativa.

Las fuentes permiten una selección razonada, pero **no prueban por sí solas la frecuencia real en la demanda** ni convierten los atributos de una taxonomía en obligaciones universales. Contrastar después con consultas reales o con investigación de usuarios puede mejorar el catálogo.

Métodos operativos (propuesta): [product-taxonomy](../20-methods/product-taxonomy/README.md) y [mpir](../20-methods/mpir/README.md) (aparcado). Motor operativo de PAA: [README](../../demand-engine/src/demand_engine/paa/README.md).

## Pendiente

- Contraste empírico del catálogo: PAA lo avanza, pero no lo cierra ([OQ-01](../30-governance/open-questions.md)).
- Regla de semillas de PAA calibrada con una sola clase (sábanas): la revisa con datos de otras el [entrenamiento de PAA](paa-training.md), que empieza por un piloto de medición ([D-114](../30-governance/decisions.md#d-114)).
- Lo que escribe PAA en el catálogo, incluidas las [pistas de valoración](assessment-hints.md): paso de aceptación, estado, formatos y registro para taxo ([D-115](../30-governance/decisions.md#d-115); [OQ-62](../30-governance/open-questions.md), [OQ-63](../30-governance/open-questions.md)). La clasificación de las preguntas la hace un agente con su reglamento (`demand-engine/classifier/paa.md`).

## Relacionado

- [demand-model](demand-model.md) — modelo de demanda y requisitos informativos
- [choice-criteria](choice-criteria.md) — criterios de elección y regla C1–C4
- [model-training](model-training.md) — entrenamiento y ejecución
- [paa-training](paa-training.md) — entrenamiento de PAA
- [study-class](study-class.md) — clase de estudio
