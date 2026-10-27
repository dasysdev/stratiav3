---
id: demand-model
title: Modelo de demanda y requisitos informativos
layer: model
status: vigente
version: 3.1
updated: 2026-10-27
sources: [BASE §4, FUND §3, FUND §11.1, INTAKE 2026-10-24-define-class, INTAKE 2026-10-24-specialization-criterion, INTAKE 2026-10-25-class-composition, INTAKE 2026-10-25-own-questions-offer, INTAKE 2026-10-25-objective-classification, INTAKE 2026-10-25-requirements-purpose, INTAKE 2026-10-25-requirement-blocks, INTAKE 2026-10-25-block-catalog, INTAKE 2026-10-25-amazon-source-blocks, INTAKE 2026-10-25-training-runtime, INTAKE 2026-10-25-induced-rules, INTAKE 2026-10-25-training-operation, INTAKE 2026-10-25-offer-application, INTAKE 2026-10-25-relevance-origin, INTAKE 2026-10-26-question-formulation, INTAKE 2026-10-26-answer-form, INTAKE 2026-10-26-resolving-information, INTAKE 2026-10-26-resolving-information-rules, INTAKE 2026-10-26-resolving-contribution-name, INTAKE 2026-10-26-general-layer-issues, INTAKE 2026-10-26-open-issues-resolution, INTAKE 2026-10-26-model-name-full-composition, INTAKE 2026-10-26-choice-criteria-and-descriptions, INTAKE 2026-10-27-paa-construction-route, INTAKE 2026-10-27-assessment-hints]
---

# Modelo de demanda y requisitos informativos

## Definición

### Modelo de demanda

> El **modelo de demanda** es la representación estructurada de las **cuestiones informativas relevantes** que necesitan poder resolverse sobre una **clase de producto u oferta** para apoyar su comprensión, comparación y evaluación durante la decisión de compra. Se materializa en un catálogo de requisitos informativos. — BASE §4

> La **relevancia** expresa que poder responder una cuestión desempeña un papel justificable en la evaluación general de esa clase de oferta. — BASE §4

La clase sobre la que se construye el modelo es la [clase de estudio](study-class.md) ([D-020](../30-governance/decisions.md#d-020)); el modelo es una [composición de bloques de requisitos](#composición-e-identidad-del-modelo) ([D-033](../30-governance/decisions.md#d-033)).

### Requisito informativo (RI)

> Un **requisito informativo** es una necesidad de conocimiento formulada como **cuestión evaluable** que especifica qué debe poder determinarse y fundamentarse sobre una oferta comercial. Puede referirse a una característica, una relación entre entidades o una condición de comercialización, y su respuesta puede construirse a partir de varios datos o afirmaciones relacionados. — BASE §4.1

**Ejemplo:** «¿Qué tallas están disponibles para cada variante?». Para responderla hay que identificar las variantes, conocer sus tallas y atribuir correctamente la disponibilidad. La pregunta expresa la necesidad informativa; los valores publicados son su posible respuesta.

Cada RI se caracteriza por:

- **Dimensión:** ámbito temático al que pertenece (precio, materiales, dimensiones físicas, disponibilidad, devoluciones…).
- **Objeto, alcance y aplicabilidad:** entidad o condición sobre la que se pregunta (producto, variante, oferta, vendedor o circunstancia comercial) y situaciones en las que procede evaluarlo.
- **Importancia relativa:** papel de su resolución en la evaluación general de la clase.

Para documentarlo operativamente, el catálogo puede registrar además: identificador, clase de oferta, formulación exacta, fundamento e **interfaces pertinentes**. Cada requisito lleva además sus [pistas de valoración](assessment-hints.md) y su marca de dimensión de comparación ([D-125](../30-governance/decisions.md#d-125), [D-126](../30-governance/decisions.md#d-126)). Los tipos de información potencialmente resolutiva, en cambio, los registra siempre: son la **[información resolutiva](resolving-information.md)** del requisito, una lista de aportaciones resolutivas ([D-064](../30-governance/decisions.md#d-064)) que sirve para localizar información pertinente y recomendar ([D-062](../30-governance/decisions.md#d-062), [D-063](../30-governance/decisions.md#d-063); aún no se registra en el catálogo). Registra siempre, además, su **[descripción](requirement-description.md)**, que concreta la pregunta ([D-092](../30-governance/decisions.md#d-092); aún no implantada en el catálogo). ⚠ Ver [I-40](../30-governance/issues.md#i-40)

### Importancia relativa

> Un requisito **crítico** aporta conocimiento indispensable para considerar suficientemente evaluable una oferta de la clase estudiada; uno **principal** aporta conocimiento central; y uno **complementario** amplía de forma relevante el conocimiento disponible. Estas clases expresan una **importancia relativa cualitativa**: valoran la trascendencia de poder responder cada cuestión para la demanda de la clase, con independencia de la calidad observada en un comercio concreto. — BASE §4.1

Desarrollo de FUND §3.3:

| Clase | Significado |
|---|---|
| **Crítico** | Aporta conocimiento indispensable para considerar suficientemente evaluable una oferta de la clase estudiada. |
| **Principal** | Aporta conocimiento central para comprender, comparar o evaluar una oferta. |
| **Complementario** | Amplía de forma relevante el conocimiento disponible sin ser central ni indispensable. |

## Reglas e invariantes

1. **La importancia es cualitativa y ordinal.** No implica pesos numéricos, distancias equivalentes ni cuotas predefinidas. «Complementario» no significa irrelevante.
2. **Un RI se considera «Crítico» por su indispensabilidad para la clase**, no por la dificultad de obtener la información en un comercio ni por su atractivo para un comprador concreto.
3. **Hay tres juicios distintos:**
   - la **pertinencia** de incluir la cuestión en el catálogo;
   - su **importancia relativa**;
   - el **grado de resolución observado** en un ámbito.

   La importancia pertenece al modelo de demanda. No se obtiene de la puntuación observada ni equivale al impacto de un criterio sobre un RI concreto.
4. **El modelo describe necesidades de la clase**, no las preferencias de un comprador concreto ni el resultado que debería tener una oferta.
5. **Principios de formulación de un RI:**
   - **Neutralidad respecto de la respuesta.** Una respuesta positiva y una negativa pueden resolver igualmente la cuestión. Carecer de una característica no es lo mismo que carecer de información sobre ella.
   - **Independencia de un campo o formato.** No se prescribe una estructura técnica única, pero la satisfacción se examina en las interfaces pertinentes.
   - **Composición de la respuesta.** La respuesta puede resultar de afirmaciones y relaciones complementarias, siempre que la derivación esté fundamentada.
   - **Alcance y aplicabilidad.** Se evalúa sobre la entidad y las condiciones a las que corresponda. Incluir un RI en el catálogo no obliga a aplicarlo a todas las ofertas.

> **Confianza e importancia:** la confianza en un requisito es independiente de su importancia: un requisito dudoso no se baja de nivel por dudoso. — INTAKE 2026-10-25-requirement-blocks

Pruebas operativas de importancia (propuesta): [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#pruebas-de-importancia) ([D-035](../30-governance/decisions.md#d-035)). Reglas de formulación de las cuestiones del catálogo (propuesta): [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formulación-de-las-cuestiones) ([D-060](../30-governance/decisions.md#d-060)).

## Distinciones

| Elemento | Ejemplo | Por qué no equivale a un RI |
|---|---|---|
| Dimensión o atributo | Impermeabilidad. | Identifica un tema, no la cuestión que debe poder resolverse. |
| Dato comercial | «Membrana impermeable». | Es una afirmación que puede contribuir a la respuesta. |
| Condición de compra | «Apto para caminar con lluvia intensa». | Expresa una exigencia de un uso o comprador concreto. |
| Escenario de compra | «Botas talla 42, impermeables, por menos de 120 €». | Combina varias necesidades y valores de un caso particular. |
| Requisito técnico de interfaz | «El feed debe contener `availability`», si su especificación lo exige. | Es una condición técnica, no una cuestión de conocimiento de la demanda. |

## Clase de estudio

La clase sobre la que se construye el modelo es la **clase de estudio**: clase general más las especializaciones pertinentes ([D-020](../30-governance/decisions.md#d-020)). Su eje de base, su composición y el criterio de especialización están en [study-class](study-class.md). La clase es el medio para descubrir los requisitos; la identidad del modelo la da la composición de requisitos que resulta.

## Composición e identidad del modelo

> Mi intención es que el modelo de demanda de un producto se «denomine» por su composición de requisitos. Es decir, composición de clase <> composición de requisitos. El modelo de demanda representa una composición concreta de requisitos. Entonces la denominación del modelo viene de cómo identificamos esa composición. — INTAKE 2026-10-25-requirement-blocks (palabras del usuario)

> La unidad de composición son **bloques de requisitos**, no preguntas sueltas ni la clase. Tipos de bloque:
>
> - bloque general universal;
> - bloques generales condicionados (variantes, descuento, unidad no nueva…);
> - bloques de sector (atributos heredados de Shopify);
> - bloques de categoría;
> - bloques de especialización (juego, polar, piel…).
>
> Un bloque agrupa las cuestiones que trae un mismo hecho. La importancia por defecto va en el bloque, y el modelo puede revisarla con justificación. — INTAKE 2026-10-25-requirement-blocks; la revisión por clase la hacen las reglas específicas inducidas en el entrenamiento, no la ejecución ([D-044](../30-governance/decisions.md#d-044))

> - […]
> - El modelo de requisitos es el conjunto de bloques, incluidos los condicionados con su disparador. Es lo que se reutiliza.
> - […]
>
> — INTAKE 2026-10-25-requirement-blocks; la identidad ya no incluye la aplicación, que es de la oferta (enmendada por [D-047](../30-governance/decisions.md#d-047))

> Consideremos sacar la aplicación de la denominación. Ya que parecen ser cuestiones de estado temporal. Entonces las vinculamos a la oferta y no al producto. Modelo de demanda se vincula al producto, aplicación a la oferta. — INTAKE 2026-10-25-offer-application (palabras del usuario)

> - En gris solo quedan los detalles; la pregunta universal nunca es NA. Lo que los pone en gris es el hecho declarado, como hoy (D-037) […]. El detalle está siempre en el modelo; en la oferta que no lo tiene aparece en gris […] y la auditoría lo registra como NA justificado.
> - Una oferta sin condiciones activas no es una ausencia sino un resultado (el clasificador ha comprobado que no se declara ninguna […]). […] Recomendado: **estándar**.
> - La oferta nunca aporta requisitos; solo activa requisitos condicionados que ya viven en el modelo del producto.
>
> — INTAKE 2026-10-25-offer-application (propuestas de Claude aprobadas)

Todo modelo incluye la capa general completa, universal y condicionada con su disparador. Lo que distingue un modelo son sus bloques de categoría y de especialización y los condicionados del producto (elementos digitales). La **aplicación** es la lista de condiciones de la oferta que se dan: variantes ofrecidas, unidad no nueva, descuento, cantidad limitada, garantía comercial, asistencia posventa, opiniones publicadas, precio personalizado o suscripción ([D-066](../30-governance/decisions.md#d-066)). Los cambios no son una condición de la oferta: son condiciones de devolución y cambio ([D-085](../30-governance/decisions.md#d-085)). Lo que se audita es la oferta: el modelo de su producto más su aplicación. El modelo solo incluye cuestiones relevantes para la clase: lo que no lo es sale por el [filtro de relevancia](model-training.md#relevancia) ([D-050](../30-governance/decisions.md#d-050)). Cuándo vale como «no» lo que la ficha no declara lo fija la auditoría ([OQ-50](../30-governance/open-questions.md)). Una cuestión que solo trae una condición de la oferta es un requisito condicionado de la clase, como la salud de la batería de un smartphone reacondicionado (ejemplo hipotético) ([D-047](../30-governance/decisions.md#d-047), [D-048](../30-governance/decisions.md#d-048)). Las categorías por clasificación objetiva que no aportan requisitos son [alias](study-class.md#composición-de-la-clase). Pila de bloques: capa general → sector → clase → especializaciones ([D-033](../30-governance/decisions.md#d-033)). Sector y categoría son un mismo tipo de bloque, con los atributos propios de una categoría de Shopify que no lista ninguna de sus madres ([D-040](../30-governance/decisions.md#d-040)), y se distinguen por su posición: los de las madres forman el sector; así la base heredada ([D-029](../30-governance/decisions.md#d-029)) no se cuenta dos veces ([D-038](../30-governance/decisions.md#d-038)). Un atributo repetido en varios niveles va siempre al bloque de la categoría más general que lo lista, y los bloques de categoría salen de un catálogo generado con la herramienta y compilado en el entrenamiento; si falta la categoría, en ejecución se genera con las reglas vigentes y se usa en estado «no compilado» (si su rama no tiene regla, la importancia es el voto del agente, provisional) ([D-040](../30-governance/decisions.md#d-040), [D-041](../30-governance/decisions.md#d-041), [D-044](../30-governance/decisions.md#d-044), [D-045](../30-governance/decisions.md#d-045)).

> Hay dos niveles:
>
> - **Clave, para la máquina (identidad):** la lista ordenada de bloques del modelo […]. Dos ofertas comparten modelo si comparten la primera lista.
> - **Nombre, para personas:** «Categorías (alias) · especializaciones […]».
>   - Los bloques universales […] no se nombran.
>   - Las categorías se unen con «+», en el orden de las piezas.
>   - Las especializaciones van en orden fijo: juego, uso, material, función.
>   - […]
>
> — INTAKE 2026-10-25-block-catalog; la clave lleva la versión de cada bloque (`<bloque>@<versión>`), enmendada por [D-045](../30-governance/decisions.md#d-045); la clave y el nombre ya no llevan la aplicación, que es de la oferta, enmendada por [D-047](../30-governance/decisions.md#d-047); los bloques de sector sí se nombran, enmendada por [D-077](../30-governance/decisions.md#d-077). La clave empieza por la versión de la capa general (`gen@<versión>`), común a todos los modelos, y los bloques generales del producto se nombran tras las especializaciones («Electrónica › Video › Televisores · con elementos digitales», ejemplo hipotético)

> Me interesa que figure la composición completa. — INTAKE 2026-10-26-model-name-full-composition (palabras del usuario)

El nombre es «Sectores › Categorías (alias) · especializaciones». Los sectores van delante, de lo general a lo particular y en el orden de la clave, separados por «›»; los del mismo nivel de Shopify se unen con «+», y un último «›» los separa de las categorías. Se nombran los sectores que tienen bloque: un nivel de Shopify sin bloque no forma parte de la composición. Las categorías de la clase y los alias se nombran aunque no tengan bloque. Sectores y categorías llevan su nombre de Shopify en la versión fijada, no el nombre del bloque. La capa general, que está en todos los modelos, no se nombra, salvo sus bloques del producto. Ejemplo, del [juego de toallas](../20-methods/product-taxonomy/cases.md#juego-de-toallas): «Casa y jardín › Ropa de casa › Toallas › Toallas de baño + Toallas de mano · juego» ([D-077](../30-governance/decisions.md#d-077)).

Los identificadores de bloque son propios y no dependen de las referencias, que se registran aparte para la trazabilidad ([D-038](../30-governance/decisions.md#d-038)); su formato está en [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo).

## Capa general

> Hay requisitos que se aplican a cualquier producto, críticos, principales o complementarios; por ejemplo, saber qué precio tiene.
>
> - La capa general tiene **cuestiones universales**, que se aplican siempre, y **cuestiones condicionadas**, con un disparador declarado: si hay variantes, si hay descuento, si la unidad no es nueva, si la cantidad es limitada…
> - El disparador es el hecho declarado, no la etiqueta: una liquidación puede ser de producto nuevo.
> - Las importancias son valores por defecto, revisables por clase con justificación (recomendación aceptada).
>
> — INTAKE 2026-10-25-requirement-blocks; enmendada por [D-045](../30-governance/decisions.md#d-045): las importancias de la capa general quedan fijas como parte del marco y ninguna regla las revisa por clase

Catálogo inicial (propuesta, se irá afinando): [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) ([D-034](../30-governance/decisions.md#d-034)), contrastado con la información precontractual obligatoria de la venta a distancia en España ([D-038](../30-governance/decisions.md#d-038)) y con el art. 19 del Reglamento (UE) 2023/988; el origen de cada cuestión sigue su fuente ([D-052](../30-governance/decisions.md#d-052)).

## Sistema de construcción vigente

El catálogo se construye por inferencia a partir de fuentes de referencia, organizadas en vías complementarias: la taxonomía de clases de producto, el MPIR (aparcado) y People Also Ask (PAA), a las que se suman las cuestiones inferidas. Cada requisito lleva su origen: «referencias», «normativa», «inferida» o «paa». Ver [construction-routes](construction-routes.md) ([D-098](../30-governance/decisions.md#d-098)).

### Entrenamiento y ejecución

El modelo de cada producto se construye en una **ejecución** automática con las reglas y el catálogo que produce un **entrenamiento** periódico; la persona responsable solo define el marco (propósito, objetivos, características del resultado, criterios de éxito e invariantes). Ver [model-training](model-training.md) ([D-041](../30-governance/decisions.md#d-041), [D-044](../30-governance/decisions.md#d-044)).

## Relación con los ámbitos de evaluación

El catálogo relaciona cada RI con sus [ámbitos pertinentes](evaluation-scopes.md) (Catálogos distribuidos, Web, Web Schema.org). Esa relación determina **dónde** se examina su satisfacción y **qué entidades, condiciones y contenidos** incluye la comprobación.

## Núcleo de conocimiento y perfil de resolución y pertinencia

Para localizar la información que puede responder un RI, el catálogo debe caracterizar su **núcleo de conocimiento**:

- qué entidad o conjunto de entidades se examina;
- qué hecho o relación se solicita;
- qué desagregación exige la pregunta;
- bajo qué condiciones y alcance corresponde formularla.

La necesidad informativa se define en el modelo de demanda; **su expresión concreta en los recursos publicados se reconoce durante la auditoría** (FUND §3.6).

Como instrumento auxiliar, cada RI puede tener un **perfil de resolución y pertinencia**, cuya forma definitiva se concretará en el diseño metodológico. Orienta la exploración y limita las selecciones arbitrarias, **sin** establecer un conjunto obligatorio de campos comerciales, un formato de publicación único ni una nueva unidad de valoración.

| Elemento orientativo | Función |
|---|---|
| Pregunta, objeto y hecho solicitado | Fijar la necesidad y la entidad a la que debe responderse. |
| Desagregación, alcance y aplicabilidad | Determinar si la cuestión corresponde a producto, variante, oferta, vendedor, mercado, momento u otras condiciones. |
| Relaciones y formas de resolución | Reconocer afirmaciones directas, relaciones y derivaciones justificadas. |
| Funciones informativas de los elementos | Identificar si cada dato describe, identifica, relaciona, contextualiza, sustenta o contrasta. |
| Expresiones ilustrativas y casos fronterizos | Facilitar la detección sin limitarla a coincidencias literales. |
| Ámbitos pertinentes y fundamento | Precisar dónde procede la evaluación y por qué. |

**Pertinencia informativa:** la **contribución identificable y justificable** de un elemento a una necesidad constitutiva del RI. La proximidad temática no basta. Un contenido puede ser pertinente aunque sea general, incompleto o insuficiente; esas limitaciones se valoran después con los [criterios de aceptación](acceptance-criteria.md).

**La caracterización del RI y la localización concreta se mantienen diferenciadas.** El agente auditor **puede** reconocer expresiones imprevistas y relaciones legítimas si acredita su función informativa (FUND §3.6). Pero **no debe**:

- ampliar silenciosamente la cuestión;
- alterar su importancia relativa;
- aceptar asociaciones basadas en hechos comerciales supuestos.

Operativización (propuesta V1): [ri-profile](../20-methods/audit-gsc/ri-profile.md).

## Escenarios de compra (posible extensión, no unidad de valoración)

> **Estado: pendiente**

Un **escenario de compra** concreta las necesidades, preferencias, restricciones, valores y contexto de un comprador. Por ejemplo: «Botas impermeables para lluvia intensa, talla 42, precio total máximo de 120 € y entrega en Madrid antes de una fecha concreta».

- Puede usarse como **extensión metodológica** que conecta varias cuestiones del modelo con condiciones reales o sintéticas.
- La *compilación* de escenarios desde RI y su *decompilación* para recuperar cuestiones se mantienen como **línea de desarrollo posible**.
- **Resolver informativamente una cuestión no implica que la oferta satisfaga una restricción de compra.** Concluir con fundamento que la oferta no cumple una fecha de entrega es una respuesta válida.
- **No hay un método vigente de agregación por escenario.** Un eventual motor de escenarios necesitará reglas propias y no puede diluir condiciones excluyentes en promedios.

## Pendiente

Ver [open-questions](../30-governance/open-questions.md):

- contraste empírico del catálogo (PAA lo avanza con preguntas de compradores filtradas por Google);
- representación de la clase de estudio en la taxonomía (en parte resuelta: se registran los modelos como composiciones de bloques);
- calibración de la importancia relativa (pruebas operativas en propuesta);
- pendientes del catálogo de la capa general: importancia de la condicionada de suscripción y depósitos, trasposición de la directiva Omnibus sobre opiniones, letra l del art. 97.1 y equivalentes del GPSR en alimentos y piensos ([OQ-45](../30-governance/open-questions.md));
- forma definitiva del perfil de RI;
- función de los escenarios de compra.

## Relacionado

- [evaluation-scopes](evaluation-scopes.md)
- [effective-availability](effective-availability.md)
- [scoring-systems](scoring-systems.md)
- [study-class](study-class.md) — clase de estudio
- [model-training](model-training.md) — entrenamiento y ejecución
- [resolving-information](resolving-information.md) — información resolutiva de cada requisito
- [requirement-description](requirement-description.md) — descripción de cada requisito
- [choice-criteria](choice-criteria.md) — criterios de elección y requisitos que generan
- [product-taxonomy](../20-methods/product-taxonomy/README.md) (método, propuesta); [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) (capa general e importancia, propuesta)
