# Fundamentos consolidados del sistema de estudio y auditoría de la calidad de la información comercial

**Versión · 24 de octubre de 2026**

**Naturaleza y precedencia documental.** Documento de fundamento conceptual y orientación metodológica del sistema de estudio y auditoría. En caso de diferencias conceptuales, prevalecen las definiciones de **«Contexto y marco del estudio»** y **«Conceptos base del sistema de estudio»**. Las pautas de aplicación y los instrumentos de trabajo se distinguen de las reglas de valoración que todavía requieren especificación y validación.

## 1. Contexto, problema y objeto del estudio

### 1.1. La información comercial en el comercio digital

La **información comercial** es el conjunto de contenidos, datos, afirmaciones y relaciones mediante los que un ecommerce describe sus **productos, variantes, ofertas, vendedores y condiciones de comercialización**. Comprende los hechos expresados, su significado, las relaciones entre entidades, su atribución y las circunstancias en las que resultan válidos.

Buscadores, plataformas publicitarias, sistemas de recomendación y agentes de inteligencia artificial utilizan esa información para descubrir, interpretar, seleccionar, comparar y evaluar productos y ofertas. Su publicación no garantiza, por sí sola, un uso adecuado: debe resultar accesible, comprensible, suficientemente detallada, correctamente atribuida, coherente y capaz de fundamentar conclusiones.

El problema que motiva el estudio es **en qué medida la información comercial y sus condiciones de representación y exposición permiten resolver las cuestiones informativas relevantes para evaluar una oferta**, más allá de la cantidad de datos publicados o del cumplimiento formal de un formato.

### 1.2. Objeto y definición de calidad

El objeto del estudio es **la calidad de la información comercial y de sus condiciones de representación y exposición**: el grado en que la información publicada por un ecommerce y las interfaces que la presentan permiten **determinar y fundamentar respuestas suficientes a las cuestiones informativas relevantes para la demanda de una clase de producto u oferta**.

Se distinguen tres conceptos que no deben utilizarse como sinónimos:

| Concepto | Significado en el sistema |
|---|---|
| **Información comercial** | Contenidos, datos, afirmaciones y relaciones que describen la realidad comercial, sus entidades y condiciones. |
| **Representación** | Forma concreta en que esa información se expresa y organiza en una interfaz. |
| **Exposición** | Condiciones bajo las que la información se publica, distribuye, recupera y consume. |

Una misma realidad comercial puede tener varias representaciones con funciones, alcances y niveles de detalle distintos. La representación es una dimensión del objeto de estudio; **no sustituye a la información comercial como objeto principal**.

La evaluación abarca dos dimensiones complementarias:

- **Técnica:** publicación, acceso, localización, recuperación, legibilidad, estructura, conformidad y distribución de la información mediante las interfaces pertinentes.
- **Informativa y semántica:** suficiencia, detalle, significado, relaciones, atribución, vigencia, coherencia, exactitud y fundamento de la información necesaria para resolver las cuestiones evaluadas.

Estas dimensiones no son equivalentes. Una interfaz técnicamente conforme puede aportar una respuesta insuficiente; y la respuesta obtenida por una interfaz no hace desaparecer las limitaciones técnicas o informativas de otra. Su separación se establece por el **objeto de la pregunta evaluativa**: la dimensión técnica examina cómo se implementa y expone la interfaz conforme a sus especificaciones; la dimensión informativa examina, para una cuestión de demanda concreta, qué información pertinente puede obtenerse y leerse y qué permite determinar y fundamentar.

La calidad evaluada concierne a la **información comercial expuesta y a su utilidad informativa**, no a la calidad intrínseca del producto ni a su conveniencia para un comprador particular. Una respuesta suficientemente fundamentada puede acreditar tanto la adecuación como la incompatibilidad de una oferta con una necesidad.

### 1.3. Finalidad de la auditoría

El modelo sustenta un **sistema de auditoría basado en requisitos, criterios explícitos y evidencias** para examinar las condiciones que un ecommerce ofrece al descubrimiento, la comprensión, la comparación y la evaluación de sus ofertas.

La auditoría debe identificar las limitaciones de acceso, cobertura, significado, atribución, contraste, fiabilidad y fundamentación; separar sus causas técnicas e informativas; explicar su impacto sobre las cuestiones pertinentes; y orientar **mejoras verificables**.

La referencia evaluativa es **poder determinar y justificar suficientemente la respuesta que corresponda** a cada cuestión, atendiendo a la entidad, el alcance y las condiciones examinadas. La auditoría valora las **condiciones que ofrece la información expuesta**, no el éxito efectivo de un consumidor particular de esa información. No consiste en premiar la acumulación de atributos, medir la precisión o la dificultad de razonamiento de un agente de IA concreto ni atribuir directamente resultados comerciales de visibilidad o conversión a la puntuación de la auditoría.

## 2. Marco funcional: Agentic Commerce

### 2.1. Contexto y delimitación funcional

El estudio se sitúa en el **Agentic Commerce**, un modelo de comercio en el que agentes de inteligencia artificial pueden intervenir en distintas fases del proceso de compra, desde la búsqueda y valoración de alternativas hasta determinadas operaciones comerciales cuando estén habilitadas.

La **Agentic Commerce Readiness** designa, en sentido amplio, el grado de preparación de un ecommerce para atender las capacidades que requieren esos agentes. **Este estudio no evalúa toda esa preparación**: se concentra en las condiciones informativas y técnicas que favorecen el descubrimiento y la decisión de compra.

| Fase del ciclo de compra | Finalidad | Alcance del estudio |
|---|---|---|
| **Descubrimiento y decisión de compra** | Encontrar ofertas, comprender características y condiciones, contrastar alternativas y valorar su adecuación. | **Incluida.** |
| Preparación de la compra | Seleccionar o configurar productos y preparar la operación. | Excluida. |
| Transacción | Autorizar y formalizar pedido y pago. | Excluida. |
| Postcompra | Gestionar pedidos, entregas, cancelaciones, devoluciones y reembolsos. | Excluida. |

El perímetro temporal y geográfico es el **contexto relevante para España desde octubre de 2026, con horizonte hasta, al menos, el primer trimestre de 2027**. La modalidad examinada es el comercio agéntico **sin navegación interactiva**: se consideran las vías de acceso y consumo que no exigen operar interactivamente las páginas o procesos de compra. No se auditan las operaciones transaccionales ni la infraestructura completa del ecommerce.

### 2.2. Funciones informativas de la IA

Las **funciones informativas de la IA** describen operaciones de conocimiento que la información comercial y sus condiciones de exposición deben favorecer. **No son los criterios de aceptación ni unidades de puntuación**.

| Función | Capacidad que debe facilitar la información comercial |
|---|---|
| **Descubrir** | Localizar productos, ofertas y recursos informativos pertinentes. |
| **Acceder** | Obtener y consultar la información comercial expuesta. |
| **Identificar** | Distinguir productos, variantes, ofertas y vendedores, y reconocer sus relaciones. |
| **Comprender** | Interpretar atributos, valores, afirmaciones y condiciones comerciales. |
| **Comparar** | Contrastar alternativas sobre dimensiones equivalentes o equivalencias justificadas. |
| **Evaluar** | Determinar la adecuación de una oferta a necesidades, preferencias y restricciones de compra. |
| **Justificar** | Sostener y reconstruir las conclusiones mediante información y relaciones de soporte identificables. |

La función **Justificar** se refiere a sostener y reconstruir respuestas. Debe distinguirse de la propiedad **P18 · Verificabilidad**, que caracteriza la posibilidad de contrastar afirmaciones con evidencias o referencias pertinentes; ambas nociones se relacionan, pero no son equivalentes.

Las interfaces son los medios técnicos de exposición; las funciones indican **qué actividades de conocimiento** deberían resultar posibles; los requisitos informativos determinan **qué cuestiones concretas** importa resolver; los criterios de aceptación permiten juzgar **si la información expuesta puede resolverlas**.

### 2.3. Fundamento de interpretación y utilización por sistemas de IA

Los sistemas basados en IA que intervienen en el descubrimiento y la decisión de compra son heterogéneos: difieren en sus modelos, herramientas, conocimientos complementarios y capacidades de interpretación. Por esa razón, la auditoría no toma como patrón la ejecución de un modelo o agente específico, ni la capacidad máxima de inferencia que podría exhibir un sistema especialmente avanzado.

El modelo utiliza criterios y propiedades vinculados con condiciones generales del significado y el uso de información: disponer de componentes relevantes, distinguir entidades, comprender afirmaciones, interpretar contextos, relacionar datos, establecer equivalencias, contrastar hechos y reconstruir el fundamento de una respuesta. Estas condiciones proporcionan una base de aplicación amplia sin constituir una garantía de compatibilidad o éxito con cualquier IA.

La premisa metodológica es que **cuanto más facilite la información comercial una interpretación y utilización fundamentadas, más favorables serán las condiciones para que una diversidad de sistemas pueda resolver las cuestiones informativas de compra**. Facilitar ese tratamiento no equivale a imponer un formato único, repetir todos los datos, exigir literalidad ni optimizar el contenido para un proveedor concreto. Supone evitar que la resolución dependa de suplir carencias relevantes con suposiciones o conocimientos no sustentados en el ámbito evaluado.

Una IA puede resolver correctamente una cuestión pese a una representación deficiente, o fallar ante información suficiente. Ninguna de esas situaciones cambia por sí misma la calidad observada de la información. La evaluación no mide latencia, número de inferencias, consumo de recursos ni probabilidad de recomendación: juzga el soporte informativo ofrecido para la cuestión.

## 3. Modelo de demanda y requisitos informativos

### 3.1. Modelo de demanda

El **modelo de demanda** es la representación estructurada de las **cuestiones informativas relevantes** que deben poder resolverse sobre una **clase de producto u oferta** para apoyar la comprensión, comparación y evaluación durante la decisión de compra. Se materializa en un **catálogo de requisitos informativos**.

La **relevancia** significa que poder responder una cuestión cumple un papel justificable en la evaluación general de la clase. El modelo describe necesidades de conocimiento de esa clase, no las preferencias individuales de un comprador ni el resultado que debería tener una oferta concreta.

### 3.2. Requisito informativo

Un **requisito informativo** es una necesidad de conocimiento formulada como **cuestión evaluable** que especifica **qué debe poder determinarse y fundamentarse** acerca de una oferta comercial. Puede preguntar por una característica, por relaciones entre entidades o por condiciones de comercialización. Su respuesta puede depender de varios datos, afirmaciones, relaciones o derivaciones justificadas; no tiene por qué corresponder a un solo atributo o campo.

Ejemplo: **«¿Qué tallas están disponibles para cada variante?»** exige identificar las variantes, conocer las tallas y atribuir correctamente la disponibilidad. La pregunta define la necesidad; los valores publicados son posibles componentes de su respuesta.

Los requisitos se formulan atendiendo a estos principios:

- **Neutralidad respecto de la respuesta.** Tanto una respuesta positiva como una negativa pueden resolver la cuestión. Carecer de una característica no es lo mismo que carecer de información sobre ella.
- **Independencia de un campo o formato particular.** No se prescribe una estructura técnica única para responder; sin embargo, **la satisfacción se examina en las interfaces pertinentes**, de acuerdo con el modelo vigente.
- **Composición de la respuesta.** La información necesaria puede resultar de afirmaciones y relaciones complementarias, siempre que su derivación esté fundamentada; la pregunta no se reduce a una lista de palabras o atributos.
- **Alcance y aplicabilidad.** La cuestión se evalúa sobre la entidad y las condiciones a las que realmente corresponda; su inclusión en el catálogo no obliga a aplicarla indiscriminadamente a todas las ofertas.

| Elemento | Ejemplo | Por qué no equivale al requisito |
|---|---|---|
| Dimensión o atributo | Impermeabilidad. | Identifica un tema, no la cuestión que debe poder resolverse. |
| Dato comercial | «Membrana impermeable». | Constituye una afirmación que puede contribuir a la respuesta. |
| Condición de compra | «Apto para caminar con lluvia intensa». | Expresa una exigencia de un uso o comprador concreto. |
| Escenario de compra | «Botas talla 42, impermeables, por menos de 120 €». | Combina varias necesidades y valores de un caso particular. |
| Requisito técnico de interfaz | «El feed debe contener el atributo `availability`», cuando su especificación así lo exija. | Define una condición técnica de una interfaz, no una cuestión de conocimiento de la demanda. |

### 3.3. Caracterización e importancia relativa

Cada requisito se caracteriza conceptualmente por su **dimensión**, **objeto, alcance y aplicabilidad**, e **importancia relativa**. Para documentarlo operativamente, el catálogo puede registrar además un identificador, la clase de oferta, la formulación exacta de la pregunta, su fundamento, los tipos de información potencialmente resolutiva y las **interfaces pertinentes**.

La **importancia relativa** clasifica cualitativamente el papel de **poder responder esa cuestión** dentro de la evaluación general de la clase de oferta:

| Clase | Significado |
|---|---|
| **Crítico** | Aporta conocimiento indispensable para considerar suficientemente evaluable una oferta de la clase estudiada. |
| **Principal** | Aporta conocimiento central para comprender, comparar o evaluar una oferta. |
| **Complementario** | Amplía de forma relevante el conocimiento disponible sin ser central ni indispensable. |

Estas categorías son **cualitativas y ordinales**. No implican pesos numéricos, distancias equivalentes ni cuotas predefinidas. «Complementario» no significa irrelevante. La consideración de un requisito como «Crítico» debe justificarse por la indispensabilidad de la información para la **clase estudiada**, no por la dificultad de obtenerla en un comercio ni por su atractivo para un comprador individual.

Deben distinguirse tres juicios: **pertinencia de incluir la cuestión** en el catálogo, **importancia relativa** de su resolución y **grado de resolución observado** en una interfaz. La importancia pertenece al modelo de demanda; no se obtiene de la puntuación observada ni equivale al impacto de un criterio de aceptación sobre un requisito concreto.

### 3.4. Sistema de construcción vigente

El catálogo se construye por **inferencia desde fuentes de referencia** que muestran cómo se caracterizan, diferencian y comercializan las ofertas de la clase estudiada:

1. **Shopify Product Taxonomy**, que ofrece categorías y atributos normalizados útiles para reconocer dimensiones del dominio comercial.
2. **Información comercial publicada por ecommerce referentes**, incluidos contenidos y estructuras empleados para presentar productos, variantes, ofertas y condiciones de compra.

El recorrido es: **observar atributos e información comercial publicada → inferir cuestiones relevantes para la compra → formular y normalizar requisitos → justificar su inclusión e importancia relativa**.

Las fuentes permiten elaborar una selección razonada de cuestiones; **no prueban, por sí solas, su frecuencia real en la demanda** ni convierten los atributos de una taxonomía en obligaciones universales. La contrastación posterior con consultas reales, investigación de usuarios u otras fuentes empíricas puede mejorar el catálogo.

### 3.5. Relación con los ámbitos de evaluación

El catálogo relaciona cada requisito informativo con los **ámbitos de evaluación pertinentes: Catálogos distribuidos, Web y Web Schema.org**.

Esta relación determina dónde se examina su satisfacción y qué entidades, condiciones y contenidos incluye la comprobación.

Los ámbitos Web y Web Schema.org pueden compartir requisitos informativos, pero su evaluación considera bases de información distintas: Web comprende la información comercial del recurso completo, mientras que Web Schema.org considera exclusivamente la expresada mediante el marcado estructurado.

Un ámbito no debe considerarse defectuoso por omitir una cuestión que no le corresponde exponer según su función y alcance.

### 3.6. Estructura informativa y límites de pertinencia de cada requisito

Para poder localizar la información que puede responder un RI, el catálogo de demanda debe ofrecer una caracterización suficiente de su **núcleo de conocimiento**: qué entidad o conjunto de entidades se examina, qué hecho o relación se solicita, qué desagregación exige la pregunta y bajo qué condiciones y alcance corresponde formularla. La necesidad informativa se define en el modelo de demanda; su expresión concreta en los recursos publicados se reconoce durante la auditoría.

Como instrumento auxiliar, cada RI puede contar con un **perfil de resolución y pertinencia**, cuya forma definitiva deberá concretarse en el diseño metodológico. Este perfil orienta la exploración y limita las selecciones arbitrarias sin establecer un conjunto obligatorio de campos comerciales, un formato de publicación único ni una nueva unidad de valoración.

| Elemento orientativo del perfil | Función |
|---|---|
| **Pregunta, objeto y hecho solicitado** | Fijar la necesidad informativa y la entidad a la que debe responderse. |
| **Desagregación, alcance y aplicabilidad** | Determinar si la cuestión corresponde a producto, variante, oferta, vendedor, mercado, momento u otras condiciones. |
| **Relaciones y formas de resolución** | Reconocer afirmaciones directas, relaciones y derivaciones justificadas capaces de contribuir a la respuesta. |
| **Funciones informativas de los elementos** | Identificar si cada dato describe, identifica, relaciona, contextualiza, sustenta o contrasta algún componente del RI. |
| **Expresiones ilustrativas y casos fronterizos** | Facilitar la detección sin limitarla a nombres de atributos, coincidencias literales o ejemplos preseleccionados. |
| **Ámbitos pertinentes y fundamento** | Precisar dónde procede la evaluación y por qué los componentes caracterizados pertenecen a la cuestión. |

La **pertinencia informativa** se determina por la contribución **identificable y justificable** de un elemento a una necesidad constitutiva del RI. La proximidad temática no basta. Un contenido puede ser pertinente aunque resulte general, incompleto, ambiguo o insuficiente para resolver la cuestión: esas limitaciones se valoran después, mediante los criterios de aceptación.

La caracterización del RI y la localización concreta deben mantenerse diferenciadas. El agente auditor puede reconocer expresiones imprevistas y relaciones legítimas si acredita su función informativa, pero no debe ampliar silenciosamente la cuestión, alterar su importancia relativa ni aceptar asociaciones basadas en hechos comerciales supuestos.

## 4. Interfaces de exposición y requisitos técnicos generales

### 4.1. Interfaces y ámbitos incluidos

Las **interfaces de exposición** son los medios técnicos mediante los que un ecommerce publica, estructura y distribuye información comercial para su consulta y utilización por otros sistemas.

Se establecen tres ámbitos de evaluación:

|Ámbito|Información examinada|Áreas de comprobación técnica|
|---|---|---|
|**Catálogos distribuidos**|Información comercial de feeds y catálogos destinados a plataformas y canales de distribución.|Generación, transformación, formato, validación, actualización, entrega, sincronización y distribución.|
|**Web**|Información comercial del recurso web completo, incluyendo contenido HTML y marcado Schema.org.|Publicación, recuperación, lectura efectiva y presencia del marcado Schema.org.|
|**Web Schema.org**|Información comercial representada específicamente mediante marcado Schema.org.|Sintaxis, estructura, vocabularios y conformidad con las especificaciones aplicables al marcado.|

El ámbito **Web** examina la capacidad de resolución conjunta de la información comercial del recurso, independientemente de que se exprese en el contenido HTML o mediante marcado Schema.org.

El ámbito **Web Schema.org** examina aisladamente la capacidad informativa de la representación estructurada, sin utilizar el resto del contenido HTML para completar las respuestas.

Ambos ámbitos comparten parte de la información examinada, pero tienen finalidades evaluativas diferentes.

En Web, el perfil de consumo no interactivo debe precisar qué información puede recuperarse y leerse sin operar la página. Cuando sea relevante, se documentará si la exposición de los datos depende de ejecutar JavaScript, sin convertir esta circunstancia en una prohibición técnica universal desligada de las vías de consumo definidas.

### 4.2. Requisitos técnicos generales

Los **requisitos técnicos generales** son condiciones de implementación, publicación, acceso, lectura, consumo y distribución aplicables a cada ámbito según sus especificaciones. Su revisión no depende de que previamente se haya seleccionado una pregunta concreta del catálogo de demanda.

Para cada requisito técnico se documentan el ámbito, la especificación o referencia aplicable, su naturaleza **obligatoria o recomendada**, el método de comprobación, la evidencia y los estados de satisfacción, aplicabilidad y evaluación.

La implementación de marcado Schema.org se contempla como requisito técnico de **Web**. Los requisitos técnicos específicos del marcado se examinan en **Web Schema.org**.

La evaluación técnica utiliza un sistema cuantitativo propio, independiente del modelo de calidad informativa. Examina el **modo de implementación** de la interfaz respecto de sus requisitos y especificaciones: por ejemplo, si un recurso se entrega bajo las condiciones estipuladas, si el marcado cumple la sintaxis aplicable o si el feed se valida y distribuye correctamente.

La comprobación informativa no reproduce esos controles. Su atención a la exposición técnica se limita a sus **consecuencias para el RI examinado**: si la información pertinente puede obtenerse y leerse efectivamente con el perfil de consumo definido. La conformidad técnica general no sustituye esta comprobación contextual, ni una incidencia técnica determina automáticamente una insuficiencia informativa.

Las propiedades de calidad pertenecen exclusivamente al modelo informativo y no constituyen unidades de evaluación del cumplimiento técnico.

Puede revisarse de forma auxiliar la política de acceso para sistemas automatizados y la existencia de bloqueos efectivos, cuando afecten a las vías examinadas. Esto no constituye una auditoría integral del rastreo, de la infraestructura o de la seguridad.

### 4.3. Complementariedad y coherencia entre representaciones

La información de distintas representaciones puede ser complementaria. Para interpretar su relación deben preservarse la **identidad de producto, variante, oferta o vendedor**, el alcance comercial, las condiciones y el momento de cada afirmación.

En el ámbito **Web**, la información comercial del contenido HTML y del marcado Schema.org puede combinarse para resolver requisitos informativos, siempre que las relaciones utilizadas estén justificadas.

Una discrepancia solo constituye una contradicción material cuando las afirmaciones se refieren a **la misma realidad comercial bajo condiciones y momentos comparables**. La coincidencia entre representaciones no demuestra por sí sola la exactitud de lo afirmado.

La evaluación de **Web Schema.org** permite identificar específicamente las capacidades y limitaciones de la representación estructurada, sin sustituir la evaluación conjunta del recurso web.

Los resultados de ambos ámbitos conservan su identidad y no se agregan automáticamente, dado que sus conjuntos de información se solapan.
## 5. Arquitectura del sistema de evaluación

### 5.1. Dos naturalezas de requisitos, evaluadas por ámbito

El sistema diferencia los requisitos técnicos generales de los requisitos informativos:

|Naturaleza|Qué se evalúa|Unidad básica|
|---|---|---|
|**Técnica**|Cumplimiento de las condiciones de exposición, implementación y consumo especificadas para cada ámbito, mediante un sistema cuantitativo propio.|**Requisito técnico × ámbito**.|
|**Informativa**|Capacidad de la información comercial efectivamente utilizable para determinar y fundamentar una cuestión pertinente, mediante la disponibilidad efectiva y los criterios de aceptación.|**Requisito informativo × ámbito**.|

La evaluación informativa se realiza en los ámbitos **Catálogos distribuidos, Web y Web Schema.org**, cada uno con sus requisitos informativos pertinentes.

En **Web**, se considera conjuntamente la información comercial del contenido HTML y del marcado Schema.org. En **Web Schema.org**, se considera exclusivamente la información expresada mediante dicho marcado.

Ambos ámbitos generan resultados informativos diferenciados. Dado que Web incluye la información de Web Schema.org, sus indicadores no se agregan automáticamente como resultados independientes.

La evaluación técnica y la informativa mantienen sus propias unidades, procedimientos y sistemas de valoración. Una incidencia técnica puede afectar a la disponibilidad efectiva de información pertinente, pero el incumplimiento de un requisito técnico no determina por sí mismo una valoración negativa de calidad informativa. El **punto de contacto** es la información utilizable para la finalidad del RI, no el grado general de conformidad de su implementación.

### 5.2. Componentes y relación entre ellos

|Componente|Función|
|---|---|
|**Modelo de demanda**|Identificar y justificar las cuestiones relevantes para la clase de oferta.|
|**Requisito informativo**|Fijar la pregunta, dimensión, entidad, alcance, aplicabilidad e importancia relativa.|
|**Interfaz pertinente**|Determinar la representación de información comercial que se examina.|
|**Disponibilidad efectiva**|Comprobar, mediante una valoración binaria, si existe información pertinente efectivamente utilizable para iniciar la valoración informativa del requisito.|
|**Criterios de aceptación**|Formular juicios diferenciados sobre la capacidad de la información utilizable para resolver la cuestión.|
|**Propiedades de calidad**|Describir características observables de la información comercial y de sus condiciones de representación y exposición que explican fortalezas y limitaciones de calidad informativa.|
|**Comprobaciones y evidencias**|Sustentar la disponibilidad efectiva, las valoraciones de los criterios y las conclusiones obtenidas.|
|**Sistemas de valoración**|Expresar la satisfacción de los criterios, la resolución de requisitos informativos y el cumplimiento de requisitos técnicos mediante sus respectivos sistemas.|

La cadena de análisis informativo comprende **RI y ámbito pertinentes → estructura informativa del RI → exploración y localización de candidatos → determinación de pertinencia funcional → información pertinente contextualizada → disponibilidad efectiva → análisis de propiedades → juicio de los criterios (GSC) → resolución del RI (IR)**. Las comprobaciones y evidencias acompañan transversalmente el proceso y pueden exigir ampliar la exploración cuando aparezcan relaciones o contextos relevantes.

Cuando no existe información pertinente utilizable, la comprobación de disponibilidad efectiva determina directamente la ausencia de resolución del requisito en ese ámbito. Cuando existe información utilizable, la evaluación de los criterios se fundamenta en las propiedades y evidencias pertinentes. La justificación de las conclusiones sigue la relación **información observada → evidencia → interpretación y hallazgo → propiedad o relación afectada → consecuencia para el criterio → GSC justificado**. La síntesis de IR se realiza conforme a las reglas que correspondan, sin confundir este nivel con el juicio sobre un criterio.

Las propiedades y los criterios de aceptación se relacionan de **muchos a muchos**. Una propiedad puede afectar varios criterios y un criterio puede depender de diversas propiedades. **Las propiedades no reciben subpuntuaciones que se sumen automáticamente**.

Las propiedades pertenecen exclusivamente al modelo de evaluación informativa. El sistema de valoración técnica se fundamenta en los requisitos técnicos generales de cada interfaz.

### 5.3. Requerimiento previo de evaluación: Disponibilidad efectiva

La **disponibilidad efectiva** es el requerimiento previo que determina si existe información comercial pertinente para un requisito informativo que pueda obtenerse y leerse efectivamente bajo las condiciones de consumo establecidas para la interfaz evaluada.

Su pregunta de comprobación es: **¿puedo obtener y leer en esta interfaz, bajo las condiciones de consumo definidas, al menos un dato, afirmación o relación que contribuya a la necesidad informativa de este RI?** No se comprueba si la interfaz es técnicamente correcta en todos sus aspectos, sino si permite consumir información pertinente para esa finalidad concreta.

Se comprueba para cada **requisito informativo × interfaz pertinente**, mediante una valoración binaria:

|Valor|Condición|
|---|---|
|**0 — Sin disponibilidad efectiva**|No existe información pertinente utilizable, porque no está presente o porque no puede obtenerse y leerse bajo las condiciones previstas.|
|**1 — Con disponibilidad efectiva**|Existe al menos un dato, afirmación o relación pertinente que puede obtenerse y leerse efectivamente bajo las condiciones previstas.|

La disponibilidad efectiva constituye una **condición necesaria, pero no suficiente, para la resolución del requisito informativo**. No exige que la información encontrada permita resolver el RI ni evalúa su suficiencia, detalle, significado, atribución o fiabilidad: tales aspectos corresponden a los criterios de aceptación. Una afirmación general sobre el modelo puede ser pertinente y legible para una cuestión sobre cada variante y, por tanto, justificar **disponibilidad efectiva = 1**, aunque no satisfaga la desagregación o atribución necesarias.

La declaración de **ausencia** exige una inspección de alcance y cobertura adecuados; no se acredita por una búsqueda literal sin resultados. Si no se ha conseguido examinar suficientemente el ámbito, la ausencia de evidencia no debe convertirse sin fundamento en un valor 0. El tratamiento formal de una comprobación de disponibilidad inconclusa requiere especificación sin introducir por ello un tercer valor en su escala binaria.

Su resultado condiciona el proceso de evaluación:

- **Disponibilidad efectiva = 0:** el indicador de resolución del requisito informativo (IR) es directamente 0. No se procede a valorar los criterios de aceptación.

- **Disponibilidad efectiva = 1:** se procede a valorar los criterios de aceptación sobre la información pertinente efectivamente utilizable. La existencia de información utilizable no garantiza que sea suficiente para resolver el requisito.

La comprobación de disponibilidad efectiva se realiza desde la **perspectiva del propósito informativo del RI**. Que una limitación de implementación impida obtener o leer información pertinente puede explicar el resultado observado, pero su análisis de conformidad pertenece a los requisitos técnicos generales. En consecuencia, se registran separadamente **el efecto sobre la disponibilidad del RI** y **la incidencia técnica que lo provoca**, cuando esta se ha acreditado.

## 6. Criterios de aceptación de calidad informativa

### 6.1. Concepto y catálogo vigente

Los **criterios de aceptación** son condiciones evaluativas con las que se juzgan aspectos diferenciados de la **capacidad de la información comercial efectivamente utilizable en una interfaz para resolver un requisito informativo**.

Su valoración se realiza después de comprobar la disponibilidad efectiva de información pertinente para el requisito y la interfaz examinados.

El catálogo comprende seis criterios:

|Criterio de aceptación|Condición evaluada|
|---|---|
|**Concreción**|La información cubre los componentes de la cuestión con la extensión y el detalle necesarios, directamente o mediante derivaciones justificadas.|
|**Precisión**|El significado de afirmaciones, términos, valores y relaciones puede interpretarse inequívocamente.|
|**Aplicabilidad**|La información puede atribuirse con claridad a la entidad, el alcance y las condiciones concretas que plantea el requisito.|
|**Comparabilidad**|La información permite efectuar o evaluar el contraste requerido sobre bases equivalentes o equivalencias justificadas.|
|**Fiabilidad**|La corrección, actualidad y consistencia de la información están suficientemente sustentadas mediante comprobaciones y evidencias pertinentes.|
|**Justificación**|La información expuesta aporta una base identificable y suficiente para sostener y reconstruir la respuesta mediante afirmaciones y relaciones de soporte justificadas.|

Estos seis elementos **no son indicadores de resolución**: constituyen el nivel de valoración de condiciones específicas que precede a la síntesis por requisito.

Su formulación se refiere siempre a la información pertinente efectivamente utilizable **en una interfaz** y a la cuestión y el alcance examinados.

La disponibilidad efectiva no forma parte de este catálogo, dado que constituye un requerimiento previo que condiciona la evaluación y determina directamente un IR de 0 cuando no existe información pertinente utilizable.

### 6.2. Separación de juicios y límites interpretativos

- **Disponibilidad efectiva frente a concreción.** La disponibilidad efectiva determina si existe información pertinente utilizable. La concreción determina si esa información cubre, con la extensión y el detalle necesarios, los componentes de la cuestión. La existencia de datos utilizables no implica que sean suficientes para responder.

- **Concreción frente a precisión.** La primera comprueba si la cuestión queda cubierta; la segunda, si es inequívoco el significado de lo expresado.

- **Precisión frente a aplicabilidad.** Comprender «disponible» no determina necesariamente **qué variante** está disponible.

- **Aplicabilidad frente a fiabilidad.** La atribución correcta de una afirmación no garantiza su exactitud o vigencia.

- **Fiabilidad frente a justificación.** La fiabilidad depende del sustento de corrección, actualidad y coherencia; la justificación exige un soporte identificable para reconstruir la respuesta. Ni citar una fuente demuestra su verdad ni la ausencia de contradicciones demuestra exactitud.

- **Comparabilidad contextual.** Se evalúa cuando la cuestión requiere contraste. Puede apoyarse en conversiones o equivalencias justificadas, sin imponer formatos idénticos.

- **Evidencia compartida.** Un hallazgo puede afectar varios criterios, pero debe explicarse la consecuencia específica para cada uno, sin tratarlo como varios defectos independientes.


La valoración de los criterios se realiza exclusivamente sobre la **información pertinente efectivamente utilizable**. Los contenidos que no pueden obtenerse o leerse bajo las condiciones previstas no pueden contribuir a satisfacer los criterios de aceptación.

Una respuesta puede estar **expresada directamente** o ser **derivable mediante relaciones y operaciones justificadas** por la evidencia publicada. Ninguna derivación válida se penaliza por el mero hecho de requerir varios pasos, ni la cantidad de pasos constituye una escala auxiliar del GSC. En cambio, no se presentan como datos publicados los estados, identidades, condiciones o relaciones que el agente complete mediante conjeturas o conocimiento externo no acreditado. La interpretación semántica legítima y el razonamiento sustentado se distinguen de la invención de hechos faltantes.

La valoración de cada criterio expresa la **satisfacción de su condición específica**, no la capacidad compensatoria ni el esfuerzo computacional de un modelo. Una valoración baja no demuestra que toda IA sea incapaz de resolver la cuestión por otros medios; una valoración alta tampoco garantiza el éxito de todo sistema.

La **pertinencia y el impacto relativo de cada criterio dependen del requisito y de la interfaz**. Algunas condiciones pueden ser indispensables para la resolución de la cuestión, sin que ello autorice a trasladar al modelo vigente los antiguos pesos y topes numéricos.

## 7. Propiedades de calidad

Las **propiedades de calidad** son características observables de la información comercial y de sus condiciones de representación y exposición **consideradas desde el propósito informativo de un RI**. Permiten interpretar hallazgos y fundamentar el juicio sobre los **criterios de aceptación**; no son subpuntuaciones ni sustituyen los controles generales de implementación de la interfaz.

En la evaluación informativa se examinan las propiedades necesarias para comprender qué aporta o limita la información pertinente efectivamente utilizable. Los requisitos técnicos generales se valoran por separado según sus especificaciones, incluso cuando ambos análisis observan un mismo recurso o utilizan evidencias comunes.

### 7.1. Información y semántica

| ID | Propiedad | Definición |
|---|---|---|
| **P06** | **Completitud** | Presencia de los componentes informativos necesarios para resolver la cuestión examinada. |
| **P07** | **Granularidad** | Nivel de detalle y diferenciación con el que se describen entidades, atributos y condiciones. |
| **P08** | **Explicitud** | Expresión directa de los hechos comerciales, sin requerir inferencias injustificadas. |
| **P09** | **Claridad** | Precisión expresiva y ausencia de ambigüedad en afirmaciones, términos y valores. |
| **P10** | **Estructuración semántica** | Organización, delimitación y relación significativa de los componentes informativos. |
| **P11** | **Identificabilidad** | Posibilidad de distinguir inequívocamente productos, variantes, ofertas y otras entidades. |
| **P12** | **Contextualización** | Presencia de circunstancias, referencias y condiciones necesarias para interpretar y aplicar la información. |
| **P13** | **Normalización** | Uso de conceptos, valores, unidades y referencias que facilitan establecer equivalencias. |

### 7.2. Fiabilidad y fundamentación

| ID | Propiedad | Definición |
|---|---|---|
| **P14** | **Exactitud** | Correspondencia de lo representado con los hechos comerciales comprobables. |
| **P15** | **Actualidad** | Correspondencia de la información con el estado comercial vigente en el momento pertinente. |
| **P16** | **Coherencia** | Consistencia entre afirmaciones referidas a una misma realidad comercial, bajo condiciones y momentos comparables. |
| **P17** | **Trazabilidad** | Posibilidad de identificar y seguir la procedencia y trayectoria de la información. |
| **P18** | **Verificabilidad** | Posibilidad de contrastar las afirmaciones con evidencias o referencias pertinentes. |

### 7.3. Lectura efectiva y relación con las condiciones técnicas

La **obtención y legibilidad efectiva** de la información pertinente es la única condición de exposición técnica que la evaluación informativa necesita comprobar directamente como puerta de entrada al análisis del RI. Se examina en la disponibilidad efectiva y, cuando corresponde, se documenta como condición de uso de las evidencias. Su pregunta no es si la interfaz satisface todos sus estándares técnicos, sino **si la información necesaria para la cuestión puede consumirse bajo las condiciones previstas**.

Esta legibilidad es **técnica u operativa**: que un dato o una afirmación puedan recuperarse y leerse. No debe confundirse con la **P09 · Claridad**, que examina si el significado de lo leído es inequívoco, ni con la **P10 · Estructuración semántica**, que examina la organización y las relaciones significativas de sus componentes. Una información puede ser obtenible y legible, pero semánticamente ambigua; o puede estar muy bien redactada en una parte del recurso que el perfil de consumo no permite leer.

La conformidad del formato, el marcado, las transformaciones, la generación de recursos, la validación, la distribución, el funcionamiento de mecanismos de acceso o cualquier otra propiedad técnica general se aborda **mediante la evaluación de requisitos técnicos**, no como un requisito informativo adicional ni como un descuento automático del GSC. Si alguno de esos factores impide consumir la información pertinente, su **consecuencia informativa concreta** se refleja en la disponibilidad efectiva; la causa y su incumplimiento se documentan en el expediente técnico.

Por ejemplo, una incidencia de marcado Schema.org puede ser relevante para la conformidad técnica del ámbito correspondiente. Si en **Web** la información exigida por el RI también se obtiene y se lee mediante HTML admisible, esa incidencia no demuestra por sí misma una falta de disponibilidad o una deficiencia de los criterios informativos de Web. En **Web Schema.org**, donde se considera solo el marcado, habrá que comprobar separadamente qué información pertinente del marcado puede utilizarse.

### 7.4. Asociaciones orientativas con los criterios

| Criterio           | Propiedades que pueden sustentar su análisis                     |
| ------------------ | ---------------------------------------------------------------- |
| **Concreción**     | P06, P07, P08 y P12.                                             |
| **Precisión**      | P08, P09, P10 y P13.                                             |
| **Aplicabilidad**  | P10, P11 y P12.                                                  |
| **Comparabilidad** | P07, P10, P12 y P13.                                             |
| **Fiabilidad**     | P14, P15, P16 y, cuando procede, P18.                            |
| **Justificación**  | P08, P17 y P18, además de las relaciones de soporte pertinentes. |

Estas asociaciones son **ilustrativas, no cerradas ni automáticas**. La propiedad relevante se selecciona a partir de la evidencia, del RI y del problema observado. Por ejemplo, la granularidad (P07) puede contribuir tanto a la concreción de una respuesta como a su aplicabilidad a una variante determinada. Las propiedades **no se valoran y suman mecánicamente** para producir el GSC: la consecuencia observada debe explicarse para cada criterio afectado.

## 8. Sistemas de valoración vigentes

### 8.1. Grado de satisfacción de cada criterio

La valoración básica se refiere a **un criterio de aceptación, un requisito informativo y una interfaz**. Se emplea la escala **ordinal de tres niveles 0–2**:

| Valor | Denominación | Interpretación |
|---|---|---|
| **0** | **No** | El aspecto requerido no queda satisfecho, según evidencia suficiente. |
| **1** | **Parcialmente** | Se satisface con limitaciones relevantes para la cuestión y condiciones examinadas. |
| **2** | **Sí, es suficiente** | Se satisface adecuadamente para esa cuestión y ámbito. |

**2** expresa suficiencia del criterio, no necesariamente resolución del requisito completo ni garantía de que cualquier sistema de IA pueda dar una respuesta correcta. Un **0** expresa insatisfacción acreditada de la condición del criterio, no imposibilidad universal de resolver la cuestión. Las cifras son etiquetas ordinales; sus distancias no constituyen porcentajes o magnitudes de calidad.

Deben distinguirse de las puntuaciones los estados:

| Estado | Cuándo procede | Tratamiento conceptual |
|---|---|---|
| **No aplicable (NA)** | El criterio o requisito no corresponde al ámbito o la cuestión definida. | Se justifica y separa de las unidades pertinentes. |
| **No evaluable (NE)** | Es pertinente, pero las evidencias disponibles no permiten formular un juicio suficientemente fundado. | No se equipara a 0; se documenta la limitación de cobertura y su efecto sobre la interpretación. |

La **insatisfacción acreditada de una condición de calidad** tras una comprobación apropiada puede justificar una valoración negativa de un criterio que resulte evaluable. La **imposibilidad de obtener evidencia suficiente** requiere un tratamiento diferenciado. En particular, no se declara falsa o incorrecta una afirmación solo porque no se haya podido verificar externamente. El agente debe fundamentar el juicio en lo observado, sin decidir primero la puntuación y buscar después ejemplos que la respalden.

### 8.2. Indicador de resolución de requisito

El **indicador de resolución de requisito** sintetiza el **grado en que cada requisito informativo puede resolverse en una interfaz pertinente**, a partir de la satisfacción de sus criterios de aceptación.

La síntesis debe considerar el **impacto relativo de cada criterio para la cuestión concreta**, la existencia de aspectos indispensables, los estados de aplicabilidad y la **cobertura efectiva de la evaluación**. Por tanto, **no se obtiene de una suma o media automática de los seis GSC ni de tratar la disponibilidad efectiva como un séptimo criterio puntuable**.

La documentación de referencia define la función de este indicador, pero **no fija una escala final ni una fórmula de agregación**. Una insuficiencia en un criterio indispensable puede condicionar la resolución, incluso si los demás criterios se satisfacen; su traducción a reglas cuantitativas queda pendiente de especificación.

### 8.3. Indicador de calidad informativa

El **indicador de calidad informativa** sintetiza la **calidad informativa de la información comercial expuesta en una interfaz**, utilizando los resultados de resolución de sus requisitos pertinentes y la **importancia relativa** de estos dentro del modelo de demanda.

Su lectura debe considerar **dimensiones informativas, aplicabilidad y cobertura de evaluación**. Es esencial distinguir dos niveles: el **impacto de un criterio** sobre la resolución de un requisito y la **importancia de un requisito** dentro del catálogo de la clase de oferta. Las clases Crítico, Principal y Complementario no disponen aquí de coeficientes numéricos preaprobados.

### 8.4. Indicador general de resolución de requisitos informativos

El **indicador general de resolución informativa** expresa la **proporción de requisitos informativos suficientemente resueltos respecto del conjunto pertinente al ámbito evaluado**. Permite observar la extensión de la resolución **por interfaz, dimensión e importancia relativa**.

La lectura del resultado debe distinguir requisitos resueltos, parcialmente resueltos, no aplicables y no evaluables, además de indicar qué unidades se examinaron. Es un indicador de **alcance de la resolución**, distinto del indicador de calidad informativa, que también considera la importancia relativa de las necesidades evaluadas.

### 8.5. Indicador general de resolución de requisitos técnicos

Para cada interfaz, el **indicador general de resolución técnica** expresa la **proporción de requisitos técnicos generales satisfechos entre los pertinentes para su perfil de implementación**.

Su interpretación requiere documentar qué comprobaciones se efectuaron, su cobertura, la distinción entre obligaciones y recomendaciones y los estados de aplicabilidad y evaluación. Caracteriza la capacidad técnica de la interfaz para exponer y permitir consumir la información comercial. **No sustituye al diagnóstico informativo ni demuestra por sí mismo la resolución de requisitos de demanda.**

### 8.6. Lectura integrada, sin confundir unidades

|Nivel|Pregunta de interpretación|Salida conceptual|
|---|---|---|
|**Disponibilidad efectiva × requisito × ámbito**|¿Existe información pertinente efectivamente utilizable?|Valor binario **0 o 1**. Si es 0, **IR = 0**.|
|**Criterio × requisito × ámbito**|¿Se satisface este aspecto de calidad sobre la información utilizable?|Grado **0, 1 o 2** y estados pertinentes.|
|**Requisito × ámbito**|¿Puede determinarse y fundamentarse suficientemente la respuesta?|**Indicador de resolución de requisito (IR).**|
|**Conjunto de requisitos de un ámbito**|¿Qué calidad informativa ofrece el ámbito respecto de las necesidades relevantes?|**Indicador de calidad informativa (ICI).**|
|**Cobertura resolutiva informativa**|¿Qué proporción de cuestiones pertinentes se resuelve suficientemente?|**Indicador general de resolución informativa.**|
|**Controles técnicos por ámbito**|¿Qué proporción de requisitos técnicos pertinentes se cumple?|**Indicador general de resolución técnica.**|

La valoración informativa mantiene como unidad **requisito informativo × ámbito de evaluación**.

Los ámbitos **Web y Web Schema.org** ofrecen perspectivas complementarias, pero sus resultados no son independientes porque Web incluye la información estructurada examinada en Web Schema.org.

Sus indicadores se interpretan por separado y no se suman ni promedian automáticamente para obtener una puntuación conjunta.

El sistema mantiene la regla **disponibilidad efectiva = 0 → IR = 0** y no presupone una fórmula completa de síntesis de criterios, pesos universales ni límites numéricos por criticidad.

La evaluación técnica conserva su sistema cuantitativo independiente.
## 9. Método de comprobación, evidencias y diagnóstico

### 9.1. Delimitación y exploración de la información pertinente

La unidad de observación informativa es **RI × ámbito de evaluación pertinente**. Cada comprobación identifica la clase de oferta, el ecommerce, el recurso, la entidad, la cuestión, su alcance, las condiciones comerciales, el perfil de consumo y el momento de referencia. Se utiliza la estructura informativa del RI para guiar la localización sin imponer etiquetas o formatos obligatorios.

La exploración combina tres modalidades complementarias:

- **Exploración general:** obtener las representaciones admisibles e identificar la organización del recurso, sus entidades, valores, bloques, relaciones y contextos.
- **Exploración dirigida por el RI:** localizar datos, afirmaciones y relaciones que puedan desempeñar una función informativa para alguno de los componentes de la cuestión, sin depender solo de coincidencias literales.
- **Ampliación guiada por los hallazgos:** volver a partes o representaciones admisibles para aclarar identidades, atribuciones, relaciones, ausencias aparentes o dudas evidenciales surgidas durante la evaluación.

No es preciso analizar exhaustivamente cada fragmento antes de iniciar la localización dirigida, pero la cobertura debe ser **suficiente para el juicio que se pretende emitir**, especialmente al sostener que no existe información pertinente utilizable. Que todo un recurso sea accesible tampoco significa que todos sus contenidos deban seleccionarse como pertinentes.

### 9.2. Selección de candidatos y pertinencia funcional

La detección de candidatos debe ser semánticamente amplia; la selección de información pertinente, rigurosa. Para cada elemento se comprueba:

1. **Contribución:** ¿a qué necesidad de conocimiento constitutiva del RI contribuye?
2. **Función:** ¿aporta el hecho solicitado, identifica una entidad, establece una relación, contextualiza, delimita, sustenta o contrasta algún componente?
3. **Fundamento:** ¿qué afirmación, relación, contexto o regla de interpretación justifica esa contribución sin añadir hechos comerciales supuestos?

La **relación temática** con la pregunta no basta. Un elemento que tiene una función identificable y justificada es pertinente aunque la información sea incompleta o insuficiente. Una conexión plausible pero todavía no acreditada debe tratarse como **candidato pendiente de comprobación**; si solo subsiste una asociación temática o una cadena de suposiciones, no se incorpora al conjunto pertinente.

No se fija un número máximo de relaciones admisibles. El límite de la derivación está en la **justificación de cada conexión significativa y su contribución a la cuestión**, no en contar los pasos. Por ejemplo, `talla 42 → SKU-420 → InStock` puede sustentar un estado por talla si cada correspondencia pertenece a la misma oferta, condiciones y momento. La popularidad del modelo o la capacidad productiva de un proveedor no permiten, por sí solas, inferir stock de esa talla.

La selección conserva un **conjunto contextualizado de datos, afirmaciones, entidades y relaciones**, potencialmente distribuidos en varias partes de la representación permitida. No se reduce a una lista de bloques de texto ni a una paráfrasis libre del auditor; se conservan los soportes que permiten reconstruir la atribución y las derivaciones.

| Nivel | Pregunta que resuelve | Consecuencia |
|---|---|---|
| **Candidato** | ¿Podría desempeñar una función para el RI? | Se examina su conexión y contexto. |
| **Pertinencia** | ¿Qué contribución identificable y justificable ofrece? | Se incorpora a la información pertinente. |
| **Disponibilidad efectiva** | ¿Hay al menos una información pertinente que se pueda obtener y leer? | Habilita los AC o conduce a **IR = 0**, según el binario 0/1. |
| **Satisfacción del criterio** | ¿En qué grado se cumple la condición específica del AC? | Se justifica el **GSC**. |
| **Resolución de la cuestión** | ¿Puede determinarse y fundamentarse suficientemente la respuesta? | Se expresa en el **IR** según las reglas de síntesis que correspondan. |

### 9.3. Secuencia operativa de la auditoría informativa

La ejecución sigue esta secuencia, manteniendo la obtención de evidencias en todas las fases:

1. **Delimitar** el RI, el ámbito, las entidades y condiciones, el perfil de consumo y su estructura de resolución/pertinencia.
2. **Obtener y preservar** los recursos admisibles y registrar las limitaciones de recuperación o lectura.
3. **Explorar y localizar** candidatos, datos, afirmaciones, entidades, relaciones y contexto con una cobertura apropiada.
4. **Fundamentar la pertinencia** de los candidatos y formar el conjunto pertinente contextualizado.
5. **Comprobar la disponibilidad efectiva**. Si es 0 con evidencia adecuada, establecer **IR = 0** y no valorar AC; si es 1, continuar.
6. **Examinar las propiedades y sus efectos** sobre cada AC pertinente, recurriendo a comprobaciones y evidencias específicas.
7. **Asignar y motivar el GSC** de cada AC aplicable, o justificar NA o NE cuando proceda.
8. **Sintetizar el IR**, cuando se disponga de las reglas correspondientes, y elaborar el informe con referencias al registro de evaluación.

La evaluación técnica se ejecuta conforme a sus requisitos y su sistema cuantitativo. Una misma observación puede alimentar ambos expedientes, pero en el informativo se describe el **efecto sobre la cuestión** y en el técnico se valora **la implementación conforme a su especificación**.

### 9.4. Principio y registro de evidencias

Toda valoración ha de resultar de **comprobaciones identificables y evidencias suficientes, contextualizadas y reexaminables** para reconstruir el camino desde el recurso publicado hasta el juicio. El orden lógico es **contenido o resultado observado → evidencia → interpretación → hallazgo → propiedad afectada → efecto sobre el AC → GSC**; el resultado no puede ser una afirmación libre sin soporte.

El registro común de evaluación debe conservar, según la naturaleza de la comprobación:

| Dimensión | Contenido a preservar |
|---|---|
| **Identificación y origen** | Caso, RI, ámbito, ecommerce, recurso, URL/feed, representación y localizador del contenido. |
| **Contenido original** | Dato, fragmento literal, afirmación, valor, relación o resultado de prueba tal como se obtuvo. |
| **Contexto, identidad y alcance** | Entidades, vínculos, unidades, condiciones, canal, mercado, momento de referencia y relaciones necesarias para interpretar la evidencia. |
| **Método y condiciones de obtención** | Perfil de consumo, vía de recuperación, momento de inspección y operaciones de comprobación. |
| **Cobertura y limitaciones** | Partes y representaciones examinadas, recursos no consumibles, candidatos pendientes y límites de las búsquedas, especialmente ante ausencias. |
| **Contribución al RI** | Necesidad o componente del RI, función informativa del elemento y fundamento de su pertinencia. |
| **Resultado y juicio** | Hallazgos, propiedades afectadas, AC correspondientes, consecuencia y justificación del GSC o estado NA/NE. |
| **Soporte reexaminable** | Referencia al recurso conservado, extracto, artefacto o comprobación que permita revisar la observación. |

Estos campos constituyen una **estructura orientativa**; el protocolo definitivo concretará cuáles son mínimos u opcionales por tipo de evidencia. La riqueza buscada es la necesaria para justificar y revisar las decisiones, no acumular capturas indiscriminadamente.

Las evidencias pueden acreditar **presencia y contenido; identidad y atribución; relaciones y derivaciones; condiciones y contexto; coherencia y contraste; procedencia, vigencia o verificabilidad; ausencia y cobertura; y limitaciones de obtención o evaluación**. Una pieza puede servir a varios hallazgos sin duplicarse artificialmente.

**La ausencia requiere una prueba de cobertura.** Una búsqueda infructuosa no demuestra que no haya información pertinente. Para fundamentar un resultado negativo es necesario documentar qué recursos y representaciones se obtuvieron, qué se inspeccionó, qué candidatos aparecieron, por qué no aportan información pertinente utilizable y qué limitaciones permanecen. La ausencia acreditada no se confunde con la insuficiencia de evidencia.

La base sustantiva de la respuesta a un RI es la **información comercial utilizable en el ámbito evaluado**. Las referencias externas podrán servir para comprobar exactitud, vigencia o fiabilidad cuando lo permita el método; no se incorporan como si fueran contenido publicado por el ecommerce para suplir carencias de la representación. Una comprobación externa inconclusa no demuestra falsedad.

El **registro estructurado** conserva observaciones, decisiones y soportes. El **informe de auditoría** expresa los resultados, las limitaciones, los GSC y las recomendaciones verificables con vínculos al registro; no reemplaza las evidencias originales por una descripción resumida del agente.

### 9.5. Diagnóstico y recomendaciones

El diagnóstico debe distinguir **qué información se ha encontrado y podido leer, qué cuestión permite responder, qué limitación subsiste y cuál es su causa observada**. Cuando una incidencia de implementación afecta a un RI, se explica el efecto informativo y se remite el examen de conformidad al control técnico correspondiente.

Las recomendaciones deben:

- Referirse a una deficiencia acreditada, sin atribuir causas no demostradas.
- Diferenciar si se necesita **publicar, concretar, aclarar, atribuir, normalizar, corregir, actualizar, relacionar o fundamentar** información, o mejorar su exposición técnica.
- Identificar la entidad, el ámbito, las condiciones y, cuando proceda, la relación informativa afectada.
- Guardar proporción con la importancia de la cuestión y el impacto de los criterios afectados, evitando prioridades numéricas no aprobadas.
- Distinguir acciones correctivas verificables de comprobaciones adicionales cuando falte evidencia.

Un mismo hallazgo puede afectar a diversos AC o RI, pero cada consecuencia se justifica de manera diferenciada. **No se multiplica el defecto por el número de criterios relacionados**, ni se degrada un criterio solo porque exista una incidencia técnica cuya repercusión informativa no está acreditada.

## 10. Ejemplo de aplicación: disponibilidad por variante

**Requisito informativo:** «¿Cuál es la disponibilidad comercial de cada variante del modelo?».

### 10.1. Caso con disponibilidad efectiva de información pertinente

**Interfaz evaluada:** ficha HTML de un modelo de calzado con tallas 41, 42 y 43.

La ficha es recuperable y muestra «Disponible para compra online» referido al modelo, pero no ofrece un estado por talla ni una regla que permita atribuirlo a la talla **42**. No se aporta contraste suficiente con inventario o referencias de vigencia. El requisito, en este ejemplo, no demanda una comparación entre ofertas.

**Comprobación previa de disponibilidad efectiva: 1 — Con disponibilidad efectiva.**

La afirmación sobre la disponibilidad comercial del modelo constituye información pertinente que puede obtenerse y leerse efectivamente bajo las condiciones de consumo previstas para la interfaz.

La existencia de esta información permite iniciar la valoración de los criterios de aceptación, aunque no garantiza que resulte suficiente para resolver el requisito por variante.

|Criterio de aceptación|Valor ilustrativo|Justificación|
|---|---|---|
|**Concreción**|**1**|Existe información sobre el modelo, pero falta el desglose o regla necesarios para la cuestión por variante.|
|**Precisión**|**2**|La expresión comercial tiene significado interpretable; la dificultad principal está en su atribución.|
|**Aplicabilidad**|**1**|El estado se atribuye al modelo, pero no inequívocamente a la talla 42.|
|**Comparabilidad**|**NA**|No se requiere contrastar alternativas en este requisito y ámbito.|
|**Fiabilidad**|**NE**|No hay evidencia suficiente para establecer la corrección o vigencia del estado publicado.|
|**Justificación**|**1**|La afirmación general aporta soporte parcial, pero no fundamenta una conclusión específica para la talla 42.|

Las limitaciones se relacionan, entre otras, con **P06 · Completitud, P07 · Granularidad, P11 · Identificabilidad y P12 · Contextualización**; las dificultades para contrastar el estado se investigan mediante las propiedades de fiabilidad y fundamentación pertinentes.

**Diagnóstico:** existe información comercial pertinente efectivamente utilizable, por lo que la disponibilidad efectiva es 1. Sin embargo, la ficha **no permite determinar y fundamentar suficientemente la disponibilidad comercial de la talla 42**.

La limitación de atribución no constituye una insuficiencia de disponibilidad efectiva ni demuestra que el inventario sea falso. Tampoco refleja una carencia de acceso o lectura técnica: la afirmación se obtiene y lee, pero su alcance no permite responder adecuadamente por variante.

La puntuación sintética del **indicador de resolución de requisito** no se calcula en este caso porque las reglas de síntesis de los criterios de aceptación todavía no están definidas completamente.

Los valores son ilustrativos, no una auditoría real.

### 10.2. Caso sin disponibilidad efectiva de información pertinente

**Requisito informativo:** «¿Cuál es la disponibilidad comercial de cada variante del modelo?».

**Interfaz evaluada:** ficha HTML de producto cuyo contenido sobre variantes y disponibilidad comercial se incorpora exclusivamente mediante ejecución de JavaScript.

Bajo las condiciones de consumo establecidas para la evaluación, la interfaz se recupera sin ejecutar JavaScript. El HTML obtenido contiene únicamente un contenedor vacío destinado a incorporar posteriormente la información de variantes y disponibilidad.

No se obtiene ningún dato, afirmación o relación pertinente que permita conocer la disponibilidad comercial de las variantes.

**Comprobación previa de disponibilidad efectiva: 0 — Sin disponibilidad efectiva.**

Aunque el recurso HTML puede recuperarse, la información pertinente no está disponible para su utilización bajo las condiciones de lectura establecidas.

**Resultado: IR = 0.**

No se procede a valorar los criterios de aceptación, puesto que no existe información pertinente efectivamente utilizable sobre la que realizar las comprobaciones.

El diagnóstico informativo identifica la ausencia de disponibilidad efectiva para este requisito y esta interfaz. El problema no es la mera presencia de JavaScript, sino que, **bajo el perfil concreto de obtención y lectura**, no se accede a ningún contenido pertinente. La implementación y conformidad técnica del mecanismo se analizan separadamente mediante los requisitos técnicos aplicables al HTML y sus condiciones de consumo.

### 10.3. Caso con relaciones suficientes para derivar la respuesta

**Requisito informativo:** «¿Cuál es la disponibilidad comercial de cada variante del modelo?». **Ámbito:** Web.

Supóngase que la información admisible identifica las tallas **41, 42 y 43**, contiene la correspondencia **talla 42 ↔ SKU-420** y publica **SKU-420: `InStock`**. Si las relaciones se refieren al mismo modelo y oferta, y su alcance y momento son comparables, la conclusión **«la talla 42 está en stock»** puede estar fundamentada sin aparecer literalmente en una sola frase.

Los elementos de identificación, correspondencia y estado son pertinentes por sus diferentes funciones; la ruta **talla 42 → SKU-420 → estado comercial** sirve para reconstruir la evidencia, **no para penalizar el número de pasos de razonamiento**. Esto no acredita por sí mismo el estado de las tallas 41 o 43: los criterios deberán examinar la cobertura real respecto del RI completo.

Por contraste, expresiones como «producto muy vendido», «fabricación de 10.000 unidades mensuales» o «envío gratuito» no bastan por sí solas para establecer la disponibilidad de una talla; una promesa de reposición sin entidad y periodo suficientemente identificados puede requerir comprobación adicional antes de decidir su función pertinente.

De modo análogo, ante el RI «¿Cuál es el precio final tras el descuento anunciado?», la publicación de precio base, porcentaje de descuento y condiciones inequívocas puede permitir una derivación aritmética válida sin exigir que el total figure literalmente. Si faltan las condiciones de aplicación, esa carencia se analizará por los AC pertinentes.

### 10.4. Interpretación entre ámbitos de evaluación

En el ámbito **Web**, la disponibilidad efectiva y la capacidad de resolución se comprueban considerando conjuntamente la información pertinente utilizable del contenido HTML y del marcado Schema.org.

El ámbito **Web Schema.org** evalúa por separado la capacidad resolutiva de la información estructurada para los requisitos que le corresponden.

Una limitación observada en Web Schema.org no implica necesariamente una limitación equivalente en Web, puesto que el contenido HTML puede aportar información complementaria.

Los resultados se documentan separadamente, conservando la procedencia de las afirmaciones y las posibles discrepancias entre representaciones.

## 11. Relación con escenarios de compra y con el modelo de trabajo

### 11.1. Escenarios de compra: posible extensión, no unidad básica de valoración

Un **escenario de compra** concreta necesidades, preferencias, restricciones, valores y contexto de un comprador; por ejemplo: «Botas impermeables para lluvia intensa, talla 42, precio total máximo de 120 € y entrega en Madrid antes de una fecha concreta».

Puede utilizarse como **aplicación o extensión metodológica** que conecta varias cuestiones del modelo de demanda con condiciones reales o sintéticas. El modelo anterior contemplaba la *compilación* de escenarios desde requisitos y la *decompilación* de escenarios para recuperar las cuestiones necesarias. Estas operaciones se mantienen aquí **como línea de desarrollo posible**, no como componente de puntuación confirmado por los dos documentos conceptuales vigentes.

**Resolver informativamente una cuestión no implica que la oferta satisfaga una restricción de compra.** Concluir fundamentadamente que no cumple una fecha de entrega es una respuesta informativamente válida. Un eventual motor de escenarios necesitará reglas propias y no puede diluir condiciones excluyentes en promedios de otras necesidades. No hay un método vigente de agregación por escenario.

### 11.2. Encaje de la auditoría en una iniciativa más amplia

La auditoría forma parte de un modelo de **consultoría, enriquecimiento y optimización de información comercial** para mejorar las condiciones de descubrimiento y evaluación de productos y ofertas en canales orgánicos, de pago y mediados por IA.

El trabajo puede articularse en **auditoría y diagnóstico; consultoría y planificación; implementación y transformación; y medición y optimización continua**. Comprende campos de aplicación como **SEO, AI SEO y GEO, publicidad digital, recomendación y personalización, AI Commerce, PIM/PXM y gestión de feeds, ecommerce y CRO, y tecnología y operaciones**.

La hipótesis aplicada del estudio es que una **mayor calidad informativa** puede ofrecer **condiciones más favorables de interpretación y utilización por sistemas de IA**, aumentar el **potencial de resolución de cuestiones de compra** y, por esa vía, contribuir eventualmente a la visibilidad, la consideración y el rendimiento de la oferta. Es una relación plausible por contrastar, **no una causalidad demostrada**.

Las mejoras en información y exposición pueden favorecer la presencia comercial, pero **el diagnóstico de calidad informativa no equivale a una medición de visibilidad, recomendación, conversión o rendimiento económico**. La comprobación de estos posibles efectos requiere indicadores y métodos diferentes a los empleados para asignar GSC e IR.

## 12. Estado de definición y límites metodológicos

Los documentos rectores fijan el **objeto de estudio, el modelo de demanda, las funciones informativas, los tres ámbitos, los requisitos técnicos generales, el requerimiento previo de disponibilidad efectiva, los seis criterios de aceptación, las propiedades de calidad informativa explicitadas (P06–P18) y la arquitectura conceptual de los sistemas de valoración**.

La disponibilidad efectiva es un requerimiento previo de evaluación informativa, con valoración **binaria 0–1** y la regla **disponibilidad efectiva = 0 → IR = 0**, sin valoración posterior de AC. La escala básica de satisfacción de los seis criterios de aceptación es **ordinal de tres niveles, 0–2**, con los estados diferenciados NA y NE. Las propiedades informativas ayudan a justificar el GSC sin convertirse en unidades cuantitativas independientes. La evaluación técnica conserva su propio sistema basado en requisitos generales de la interfaz.

El desarrollo operativo debe establecer instrumentos suficientemente precisos y reproducibles para que el agente auditor **reconozca información pertinente, compruebe su disponibilidad, examine las propiedades y justifique los criterios** sobre evidencias reexaminables. Los perfiles de RI, las pruebas de pertinencia y las rutas de resolución son apoyos al método; **no introducen nuevos RI, AC, propiedades, indicadores o escalas de puntuación**.

| Elemento | Especificación o validación que requiere |
|---|---|
| **Modelo de demanda** | Contrastar requisitos inferidos con fuentes empíricas y revisar pertinencia, cobertura, solapamientos y fragmentación. |
| **Importancia relativa** | Calibrar decisiones de Crítico, Principal y Complementario con fundamentos y casos comparables. |
| **Perfil de resolución y pertinencia del RI** | Fijar campos necesarios, estructura, límites, ejemplos y procedimiento de elaboración y validación en el catálogo. |
| **Exploración y selección** | Establecer pautas de reconocimiento semántico, pertinencia funcional, tratamiento de candidatos fronterizos y cobertura suficiente. |
| **Disponibilidad y ausencias** | Especificar pruebas de obtención/legibilidad, registros de cobertura y tratamiento de comprobaciones inconclusas sin modificar el binario vigente. |
| **Requisitos técnicos por ámbito** | Completar perfiles de implementación, obligaciones, recomendaciones, métodos y cobertura de controles técnicos independientes. |
| **Propiedades P06–P18** | Concretar qué observar y cómo comprobar propiedades relevantes según RI, ámbito, evidencia y consecuencia informativa. |
| **Guías de los seis AC** | Definir pruebas, evidencias, reglas interpretativas y anclajes GSC 0/1/2 y NA/NE con calibración suficiente. |
| **Registro de evidencias** | Determinar mínimos de localización, contenido original, contexto, identidades, condiciones, método, cobertura y reexamen. |
| **Resolución del RI (IR)** | Definir síntesis de criterios considerando impacto relativo, aspectos indispensables, aplicabilidad y cobertura, sin fórmulas asumidas. |
| **Calidad por ámbito (ICI) e indicadores generales** | Precisar universo pertinente, importancia relativa, umbrales, estados y cobertura, sin convertir automáticamente categorías cualitativas en pesos numéricos. |
| **Calibración y consistencia** | Contrastar casos suficientes, parciales, negativos, fronterizos y NE/NA para reducir omisiones, sobreinclusión y variación entre auditores. |
| **Escenarios de compra** | Decidir su eventual función como extensión operativa y especificar reglas propias de decisión si procede. |

La metodología se organiza en **un marco común de evaluación**, la **caracterización de los RI**, un **protocolo de localización y pertinencia**, un **protocolo transversal de evidencias**, **guías de propiedades y de cada AC**, y una **fase de calibración**. La especificación de la búsqueda y de la evidencia antecede al cierre de los anclajes de GSC, porque determina sobre qué base pueden aplicarse consistentemente. Una posterior **Skill de auditoría** implementará las guías consolidadas, sin sustituirlas por decisiones libres del modelo.

El procedimiento debe vigilar especialmente las **falsas ausencias**, la inclusión por simple asociación temática, el uso de conocimiento externo como si fuera información expuesta, las atribuciones entre entidades o momentos no comparables y la confusión entre hecho observado e interpretación. La independencia frente a modelos concretos de IA es metodológica y razonablemente reproducible; no equivale a invariancia absoluta del comportamiento de todos los agentes.

**Límite de interpretación:** el estudio valora la información comercial expuesta y sus condiciones técnicas e informativas de utilización; **no mide el comportamiento ni la dificultad computacional de un agente de IA particular**, no garantiza éxito universal de resolución y no acredita por sí mismo efectos de visibilidad o conversión.

El modelo utiliza referencias conceptuales orientativas como el **W3C Data Quality Vocabulary (DQV)** y la **ISO/IEC/IEEE 15939:2017** en materia de calidad de datos y medición, mencionadas en el consolidado anterior. **No debe atribuirse a esas referencias la definición o validación de los criterios, indicadores o reglas de síntesis aquí descritos**.

---

**Documentos rectores:** «Contexto y marco del estudio» y «Conceptos base del sistema de estudio». **Documentos metodológicos de apoyo:** «Fundamento metodológico: calidad informativa orientada a su interpretación y utilización por sistemas de IA» y «Estrategia metodológica de evaluación informativa: estructura del RI, localización de información pertinente, evidencias y valoración del GSC». **Referencia de antecedentes compatible:** «Calidad de representación de oferta comercial». En caso de discrepancia conceptual, prevalecen los dos documentos rectores.