---
id: demand-model
title: Modelo de demanda y requisitos informativos
layer: model
status: vigente
version: 1.1
updated: 2026-10-24
sources: [BASE §4, FUND §3, FUND §11.1]
---

# Modelo de demanda y requisitos informativos

## Definición

### Modelo de demanda

> El **modelo de demanda** es la representación estructurada de las **cuestiones informativas relevantes** que necesitan poder resolverse sobre una **clase de producto u oferta** para apoyar su comprensión, comparación y evaluación durante la decisión de compra. Se materializa en un catálogo de requisitos informativos. — BASE §4

> La **relevancia** expresa que poder responder una cuestión desempeña un papel justificable en la evaluación general de esa clase de oferta. — BASE §4

### Requisito informativo (RI)

> Un **requisito informativo** es una necesidad de conocimiento formulada como **cuestión evaluable** que especifica qué debe poder determinarse y fundamentarse sobre una oferta comercial. Puede referirse a una característica, una relación entre entidades o una condición de comercialización, y su respuesta puede construirse a partir de varios datos o afirmaciones relacionados. — BASE §4.1

**Ejemplo:** «¿Qué tallas están disponibles para cada variante?». Para responderla hay que identificar las variantes, conocer sus tallas y atribuir correctamente la disponibilidad. La pregunta expresa la necesidad informativa; los valores publicados son su posible respuesta.

Cada RI se caracteriza por:

- **Dimensión:** ámbito temático al que pertenece (precio, materiales, dimensiones físicas, disponibilidad, devoluciones…).
- **Objeto, alcance y aplicabilidad:** entidad o condición sobre la que se pregunta (producto, variante, oferta, vendedor o circunstancia comercial) y situaciones en las que procede evaluarlo.
- **Importancia relativa:** papel de su resolución en la evaluación general de la clase.

Para documentarlo operativamente, el catálogo puede registrar además: identificador, clase de oferta, formulación exacta, fundamento, tipos de información potencialmente resolutiva e **interfaces pertinentes**.

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

## Distinciones

| Elemento | Ejemplo | Por qué no equivale a un RI |
|---|---|---|
| Dimensión o atributo | Impermeabilidad. | Identifica un tema, no la cuestión que debe poder resolverse. |
| Dato comercial | «Membrana impermeable». | Es una afirmación que puede contribuir a la respuesta. |
| Condición de compra | «Apto para caminar con lluvia intensa». | Expresa una exigencia de un uso o comprador concreto. |
| Escenario de compra | «Botas talla 42, impermeables, por menos de 120 €». | Combina varias necesidades y valores de un caso particular. |
| Requisito técnico de interfaz | «El feed debe contener `availability`», si su especificación lo exige. | Es una condición técnica, no una cuestión de conocimiento de la demanda. |

## Sistema de construcción vigente

> El catálogo se construye mediante **inferencia a partir de fuentes de referencia** que reflejan cómo se caracterizan, diferencian y comercializan las ofertas de la clase estudiada. — BASE §4.2

Las fuentes se organizan en **dos vías de referencia complementarias** (BASE §4.2, enmendada por [D-009](../30-governance/decisions.md#d-009)):

1. **Taxonomía de clases de producto.** Delimita la clase y permite reconocer atributos, facetas y dimensiones del dominio. Su estructura principal es la **Shopify Product Taxonomy**. Amazon (especialización) y Google (contraste) son fuentes de apoyo de la taxonomía, **no fuentes directas de RI**. Denominación canónica según [D-012](../30-governance/decisions.md#d-012).
2. **MPIR: información comercial publicada por ecommerce referentes.** Permite reconocer criterios de elección, preguntas anticipadas, contextos, relaciones y condiciones que la taxonomía no anticipa.

**Recorrido:**

1. Observar los atributos y la información comercial publicada.
2. Inferir cuestiones relevantes para la compra.
3. Formular y normalizar los requisitos.
4. Justificar su inclusión e importancia relativa.

Las fuentes permiten una selección razonada, pero **no prueban por sí solas la frecuencia real en la demanda** ni convierten los atributos de una taxonomía en obligaciones universales. Contrastar después con consultas reales o con investigación de usuarios puede mejorar el catálogo.

Métodos operativos (propuesta): [product-taxonomy](../20-methods/product-taxonomy/README.md) y [mpir](../20-methods/mpir/README.md).

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

- contraste empírico del catálogo;
- calibración de la importancia relativa;
- forma definitiva del perfil de RI;
- función de los escenarios de compra.

## Relacionado

- [evaluation-scopes](evaluation-scopes.md)
- [effective-availability](effective-availability.md)
- [scoring-systems](scoring-systems.md)
