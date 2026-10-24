# Conceptos base del sistema de estudio

El sistema estudia la **calidad de la información comercial y de sus condiciones de representación y exposición** a partir de las cuestiones informativas relevantes para la demanda de una clase de producto u oferta. Relaciona las necesidades de conocimiento con la información que publica un ecommerce, las interfaces mediante las que la hace disponible y el grado en que permite determinar y fundamentar respuestas suficientes.

## 1. Información comercial

La **información comercial** es el conjunto de contenidos, datos, afirmaciones y relaciones mediante los que un ecommerce describe sus productos, variantes, ofertas, vendedores y condiciones de comercialización. Comprende los hechos expresados, su significado, las relaciones entre entidades, su atribución y las circunstancias en las que resultan válidos.

La **representación** es la forma concreta en que esa información se expresa y organiza en una interfaz; la **exposición** comprende las condiciones bajo las que se publica, distribuye, recupera y consume. Una misma realidad comercial puede disponer de distintas representaciones, con niveles de detalle y funciones diferentes.

La calidad se determina por la **capacidad de la información comercial y de sus condiciones de representación y exposición para resolver cuestiones informativas relevantes**, proporcionando respuestas suficientes, interpretables, atribuibles y fundamentadas para la entidad y las condiciones consideradas.

## 2. Funciones informativas de la IA

Las **funciones informativas de la IA** describen las operaciones de conocimiento que la información comercial y sus condiciones de exposición deben favorecer durante el descubrimiento y la decisión de compra:

| Función         | Capacidad que debe facilitar la información comercial                                                |
| --------------- | ---------------------------------------------------------------------------------------------------- |
| **Descubrir**   | Localizar productos, ofertas y recursos informativos pertinentes.                                    |
| **Acceder**     | Obtener y consultar la información comercial expuesta.                                               |
| **Identificar** | Distinguir productos, variantes, ofertas y vendedores, y reconocer sus relaciones.                   |
| **Comprender**  | Interpretar atributos, valores, afirmaciones y condiciones comerciales.                              |
| **Comparar**    | Contrastar alternativas sobre dimensiones equivalentes o equivalencias justificadas.                 |
| **Evaluar**     | Determinar la adecuación de una oferta a necesidades, preferencias y restricciones de compra.        |
| **Justificar**  | Sostener y reconstruir las conclusiones mediante información y relaciones de soporte identificables. |

Estas funciones orientan el estudio de la calidad de la información comercial expuesta. Una respuesta que fundamenta la incompatibilidad de una oferta con una necesidad puede resolver adecuadamente la cuestión planteada.

## 3. Interfaces y ámbitos de evaluación

Las **interfaces de exposición** son los medios técnicos mediante los que el ecommerce publica, estructura y distribuye información comercial para su consulta y utilización por otros sistemas.

El sistema establece tres **ámbitos de evaluación**, que determinan qué información se examina y qué requisitos informativos son pertinentes:

|Ámbito|Información comercial examinada|
|---|---|
|**Catálogos distribuidos**|Información comercial publicada y distribuida mediante feeds y catálogos destinados a plataformas como Google Merchant Center y Meta Commerce.|
|**Web**|Información comercial del recurso web en su conjunto, incluyendo contenido HTML y marcado estructurado Schema.org.|
|**Web Schema.org**|Información comercial expresada mediante el marcado Schema.org del recurso web, considerada aisladamente del resto del contenido HTML.|

Los ámbitos **Web y Web Schema.org no son independientes en cuanto a la información que contienen**: Web incluye el marcado Schema.org, mientras que Web Schema.org permite examinar específicamente su capacidad informativa.

Cada ámbito dispone de un conjunto de requisitos informativos pertinentes, derivados del catálogo del modelo de demanda. La evaluación determina en qué grado la información efectivamente utilizable dentro de cada ámbito permite resolverlos.

Los resultados de Web y Web Schema.org se mantienen diferenciados y no se agregan automáticamente como si correspondieran a conjuntos independientes de información.

### 3.1. Requisitos técnicos

Los **requisitos técnicos generales** expresan las condiciones de implementación, publicación, acceso, consumo y distribución aplicables a cada ámbito, según sus especificaciones.

En **Web**, se comprueban las condiciones técnicas de recuperación y lectura del recurso, incluyendo la implementación de marcado Schema.org como requisito técnico.

En **Web Schema.org**, se examinan los requisitos técnicos específicos del marcado estructurado, incluyendo las condiciones sintácticas, estructurales y de conformidad aplicables.

En **Catálogos distribuidos**, se examinan los requisitos de generación, formato, validación, actualización, entrega y distribución correspondientes a cada perfil.

La evaluación técnica utiliza un **sistema cuantitativo propio**, independiente de la evaluación de calidad informativa.

Las propiedades de calidad pertenecen exclusivamente al modelo de evaluación informativa.
## 4. Modelo de demanda

El **modelo de demanda** es la representación estructurada de las **cuestiones informativas relevantes** que necesitan poder resolverse sobre una **clase de producto u oferta** para apoyar su comprensión, comparación y evaluación durante la decisión de compra. Se materializa en un catálogo de requisitos informativos.

La **relevancia** expresa que poder responder una cuestión desempeña un papel justificable en la evaluación general de esa clase de oferta. El modelo organiza necesidades de conocimiento de la clase estudiada, mientras que las condiciones de un comprador concreto determinan cómo se utilizan las respuestas en una decisión particular.

### 4.1. Requisitos informativos

Un **requisito informativo** es una necesidad de conocimiento formulada como **cuestión evaluable** que especifica qué debe poder determinarse y fundamentarse sobre una oferta comercial. Puede referirse a una característica, una relación entre entidades o una condición de comercialización, y su respuesta puede construirse a partir de varios datos o afirmaciones relacionados.

Por ejemplo, «¿Qué tallas están disponibles para cada variante?» exige identificar las variantes, conocer sus tallas y atribuir correctamente la disponibilidad. La pregunta expresa la necesidad informativa; los valores publicados constituyen su posible respuesta.

Cada requisito se caracteriza por:

- **Dimensión:** ámbito temático al que pertenece, como precio, materiales, dimensiones físicas, disponibilidad o devoluciones.
- **Objeto, alcance y aplicabilidad:** entidad o condición sobre la que se pregunta —producto, variante, oferta, vendedor o circunstancia comercial— y situaciones en las que procede evaluarlo.
- **Importancia relativa:** papel de su resolución en la evaluación general de la clase, clasificado como **crítico**, **principal** o **complementario**.

Un requisito **crítico** aporta conocimiento indispensable para considerar suficientemente evaluable una oferta de la clase estudiada; uno **principal** aporta conocimiento central; y uno **complementario** amplía de forma relevante el conocimiento disponible. Estas clases expresan una **importancia relativa cualitativa**: valoran la trascendencia de poder responder cada cuestión para la demanda de la clase, con independencia de la calidad observada en un comercio concreto.

Los requisitos del catálogo se relacionan con las **interfaces pertinentes** para determinar dónde se examina su satisfacción y qué entidad, condiciones y contenido comprende cada comprobación.

### 4.2. Sistema de construcción vigente

El catálogo se construye mediante **inferencia a partir de fuentes de referencia** que reflejan cómo se caracterizan, diferencian y comercializan las ofertas de la clase estudiada. Las fuentes principales son:

- **Shopify Product Taxonomy:** categorías y atributos normalizados que permiten reconocer dimensiones relevantes del dominio comercial.
- **Información comercial publicada por ecommerce referentes:** contenidos y estructuras utilizados para presentar características, variantes, ofertas y condiciones de compra.

La construcción sigue el recorrido **observación de atributos e información comercial publicada → inferencia de cuestiones relevantes para la compra → formulación y normalización de requisitos → justificación de su inclusión e importancia relativa**. Las fuentes fundamentan una selección razonada de necesidades informativas para la clase de producto.

## 5. Modelo de evaluación de calidad informativa

El **modelo de evaluación de calidad informativa** determina en qué grado la información comercial expuesta **en cada interfaz** permite resolver los requisitos informativos pertinentes. La resolución significa poder **determinar y fundamentar una respuesta suficiente** para la entidad, el alcance y las condiciones examinadas.

La evaluación relaciona **requisitos informativos, criterios de aceptación, propiedades de calidad y evidencias**. Para cada requisito e interfaz se comprueba qué información está disponible, cómo debe interpretarse y qué fundamento ofrece para responder. Los resultados distinguen las limitaciones observadas y su efecto sobre la resolución de la cuestión.


### 5.1. Requerimiento previo de evaluación: Disponibilidad efectiva

La **disponibilidad efectiva** es el requerimiento previo que determina si existe información comercial pertinente para un requisito informativo que pueda obtenerse y leerse efectivamente bajo las condiciones de consumo establecidas para la interfaz evaluada.

Se comprueba para cada **requisito informativo × interfaz pertinente**, mediante una valoración binaria:

|Valor|Condición|
|---|---|
|**0 — Sin disponibilidad efectiva**|No existe información pertinente utilizable, porque no está presente o porque no puede obtenerse y leerse bajo las condiciones previstas.|
|**1 — Con disponibilidad efectiva**|Existe al menos un dato, afirmación o relación pertinente que puede obtenerse y leerse efectivamente bajo las condiciones previstas.|

La disponibilidad efectiva constituye una **condición necesaria, pero no suficiente, para la resolución del requisito informativo**. No evalúa la suficiencia, el detalle, el significado, la atribución ni la fiabilidad de la información disponible, aspectos que corresponden a los criterios de aceptación.

Su resultado condiciona el proceso de evaluación:

- **Disponibilidad efectiva = 0:** el indicador de resolución del requisito informativo (IR) es directamente 0. No se procede a valorar los criterios de aceptación.
    
- **Disponibilidad efectiva = 1:** se procede a valorar los criterios de aceptación sobre la información pertinente efectivamente utilizable. La existencia de información utilizable no garantiza que sea suficiente para resolver el requisito.
    

La comprobación de disponibilidad efectiva se realiza desde la perspectiva de la necesidad informativa y no constituye una evaluación del cumplimiento de los requisitos técnicos de la interfaz, que dispone de su propio sistema de evaluación.

### 5.2. Criterios de aceptación

Los **criterios de aceptación** son las condiciones evaluativas con las que se juzgan aspectos diferenciados de la capacidad de la información comercial expuesta en una interfaz para resolver un requisito informativo. Cada criterio expresa una condición específica:

| Criterio           | Condición evaluada                                                                                                                                                      |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Concreción**     | La información cubre los componentes de la cuestión con la extensión y el detalle necesarios, directamente o mediante derivaciones justificadas.                        |
| **Precisión**      | El significado de afirmaciones, términos, valores y relaciones puede interpretarse inequívocamente.                                                                     |
| **Aplicabilidad**  | La información puede atribuirse con claridad a la entidad, el alcance y las condiciones concretas que plantea el requisito.                                             |
| **Comparabilidad** | La información permite efectuar o evaluar el contraste requerido sobre bases equivalentes o equivalencias justificadas.                                                 |
| **Fiabilidad**     | La corrección, actualidad y consistencia de la información están suficientemente sustentadas mediante comprobaciones y evidencias pertinentes.                          |
| **Justificación**  | La información expuesta aporta una base identificable y suficiente para sostener y reconstruir la respuesta mediante afirmaciones y relaciones de soporte justificadas. |

Los criterios proporcionan **juicios diferenciados y complementarios**. La disponibilidad se refiere al acceso al contenido; la concreción, a la cobertura de la cuestión; la precisión, al significado; y la aplicabilidad, a su correcta atribución. La fiabilidad atiende a la confianza en lo afirmado y la justificación al fundamento que permite sostener la respuesta. La comparabilidad interviene cuando la cuestión requiere contraste.

La **pertinencia y el impacto relativo** de cada criterio dependen del requisito. Algunos aspectos pueden resultar indispensables para su resolución, de modo que su insuficiencia condiciona el resultado conjunto, incluso cuando los demás criterios están satisfechos.

### 5.3. Propiedades de calidad

Las **propiedades de calidad** son características observables de la información comercial y de sus condiciones de representación y exposición. Sirven para interpretar hallazgos y fundamentar las valoraciones de los criterios de aceptación y los requisitos técnicos generales.

| Ámbito                          | Propiedad                          | Definición                                                                                                         |
| ------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| **Informativa y semántica**     | **P06 · Completitud**              | Presencia de los componentes informativos necesarios para resolver la cuestión examinada.                          |
|                                 | **P07 · Granularidad**             | Nivel de detalle y diferenciación con el que se describen entidades, atributos y condiciones.                      |
|                                 | **P08 · Explicitud**               | Expresión directa de los hechos comerciales, sin requerir inferencias injustificadas.                              |
|                                 | **P09 · Claridad**                 | Precisión expresiva y ausencia de ambigüedad en afirmaciones, términos y valores.                                  |
|                                 | **P10 · Estructuración semántica** | Organización, delimitación y relación significativa de los componentes informativos.                               |
|                                 | **P11 · Identificabilidad**        | Posibilidad de distinguir inequívocamente productos, variantes, ofertas y otras entidades.                         |
|                                 | **P12 · Contextualización**        | Presencia de circunstancias, referencias y condiciones necesarias para interpretar y aplicar la información.       |
|                                 | **P13 · Normalización**            | Uso de conceptos, valores, unidades y referencias que facilitan establecer equivalencias.                          |
| **Fiabilidad y fundamentación** | **P14 · Exactitud**                | Correspondencia de lo representado con los hechos comerciales comprobables.                                        |
|                                 | **P15 · Actualidad**               | Correspondencia de la información con el estado comercial vigente en el momento pertinente.                        |
|                                 | **P16 · Coherencia**               | Consistencia entre afirmaciones referidas a una misma realidad comercial, bajo condiciones y momentos comparables. |
|                                 | **P17 · Trazabilidad**             | Posibilidad de identificar y seguir la procedencia y trayectoria de la información.                                |
|                                 | **P18 · Verificabilidad**          | Posibilidad de contrastar las afirmaciones con evidencias o referencias pertinentes.                               |

Las propiedades se relacionan con los criterios según el **requisito, la interfaz y el hallazgo**. Una misma propiedad puede fundamentar varios criterios, y un criterio puede depender de varias propiedades. Por ejemplo, la granularidad puede afectar tanto a la concreción de una respuesta como a su aplicabilidad a una variante concreta.

## 6. Sistemas de valoración

Los **sistemas de valoración** expresan los resultados de la auditoría desde la satisfacción de cada criterio hasta la resolución de los requisitos y la lectura conjunta de la información comercial y de las interfaces examinadas.

### 6.1. Calidad informativa

#### Grado de satisfacción de criterio (GSC)

Valora **cada criterio de aceptación para un requisito informativo y una interfaz**, a partir de la evidencia observada. Utiliza una escala ordinal de tres niveles: **0 — No**, cuando el aspecto requerido no queda satisfecho; **1 — Parcialmente**, cuando se satisface con limitaciones relevantes; y **2 — Sí, es suficiente**, cuando se satisface adecuadamente para la cuestión y las condiciones evaluadas.

La valoración considera la pertinencia del criterio, la suficiencia de la evidencia y la distinción entre una deficiencia comprobada, un criterio **no aplicable** y una situación **no evaluable**.

#### Indicador de resolución de requisito informativo (IR)

Sintetiza el **grado de resolución de cada requisito informativo por interfaz**. Depende de la satisfacción de sus criterios de aceptación y del **impacto relativo** que cada uno tiene sobre la posibilidad de determinar y fundamentar la respuesta. También considera la existencia de criterios indispensables, la aplicabilidad y la cobertura efectiva de la evaluación.

#### Indicador de calidad informativa (ICI)

Sintetiza la **calidad informativa de la información comercial expuesta en una interfaz** a partir de los resultados de resolución de sus requisitos pertinentes y de la **importancia relativa** de estos dentro del modelo de demanda. Su interpretación considera las dimensiones informativas, la aplicabilidad de los requisitos y la cobertura de la evaluación. La importancia de un requisito y el impacto de un criterio actúan en niveles distintos.

#### Tasa de resolución informativa (TRI)

Expresa la **proporción de requisitos informativos suficientemente resueltos** respecto del conjunto pertinente para el ámbito evaluado. Permite apreciar la extensión de la resolución y analizarla **por interfaz, dimensión e importancia relativa**. Su lectura considera las unidades evaluadas, la aplicabilidad, los resultados parciales y la disponibilidad de evidencia suficiente para establecer la resolución.

### 6.2. Requisitos técnicos

#### Tasa de cumplimiento técnico

Expresa la **proporción de requisitos técnicos generales satisfechos por interfaz** respecto de los que resultan pertinentes para su perfil de implementación. Su interpretación considera la cobertura de las comprobaciones, la naturaleza obligatoria o recomendada de cada condición y los estados de aplicabilidad y evaluación. Caracteriza la capacidad técnica de las interfaces para exponer y hacer consumible la información comercial.
