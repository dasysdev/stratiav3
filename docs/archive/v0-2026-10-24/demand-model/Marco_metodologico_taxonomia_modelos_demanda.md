# Marco metodológico para construir la taxonomía de clases de producto

*Referencias, estrategia de integración y reglas para los modelos de demanda*

**Proyecto:** Calidad de información v1  
**Fecha de referencia:** 24 de octubre de 2026  
**Naturaleza:** documento metodológico de referencia y propuesta de diseño. No incluye los catálogos taxonómicos de las plataformas ni sustituye los documentos rectores del estudio.

## Resumen ejecutivo

El proyecto necesita una **taxonomía propia de clases de producto u oferta** que permita seleccionar la unidad adecuada para construir modelos de demanda. Su finalidad no es replicar la navegación de una tienda ni validar datos de un marketplace: es disponer de clases suficientemente bien delimitadas para formular y justificar las cuestiones informativas que deben poder resolverse durante el descubrimiento y la decisión de compra.

La conclusión de la investigación es que **Shopify, Amazon y Google son fuentes complementarias, pero sus estructuras no son directamente fusionables en un único árbol sin interpretación semántica**. Shopify constituye una buena estructura principal de referencia por sus categorías y atributos normalizados; Amazon puede aportar especializaciones de navegación y esquemas de atributos; Google sirve para contrastar categorías, vocabulario comercial y reglas de datos. La información publicada por ecommerce referentes sigue siendo una fuente principal para inferir requisitos informativos [M2, M3].

La estrategia es **conservar las fuentes externas sin modificarlas, construir correspondencias auditables y derivar una capa interna de clases y facetas**. Un siguiente nivel de especialización es deseable allí donde cambien sustancialmente las necesidades informativas, pero no debe imponerse a todas las ramas ni justificarse por la mera existencia de una subcategoría en Amazon.

| Decisión metodológica | Orientación propuesta |
|---|---|
| Estructura principal | Shopify Standard Product Taxonomy, fijada por versión como referencia inicial. |
| Ampliación de granularidad | Amazon Browse Tree, y en su caso atributos de Amazon Product Type Definitions. |
| Contraste complementario | Google Product Taxonomy, Merchant Center y Manufacturer Center. |
| Unidad canónica | Clase interna definida por alcance funcional e informativo; identificador propio. |
| Mecanismo de integración | Correspondencias semánticas versionadas, no unión automática de árboles. |
| Vínculo con demanda | La clase delimita el dominio; los requisitos informativos se infieren y validan por separado. |

## 1. Propósito, alcance y precedencia

### 1.1. Para qué necesitamos esta taxonomía

El **modelo de demanda**, según los documentos rectores, representa las cuestiones informativas relevantes que han de poder resolverse respecto de una clase de producto u oferta para facilitar la comprensión, comparación y evaluación durante la decisión de compra. Se materializa en requisitos informativos formulados como preguntas evaluables [M2].

La taxonomía de clases es una **estructura de referencia anterior al modelo de demanda**. Sirve para: delimitar qué productos pertenecen a una clase; identificar familias y especializaciones comparables; organizar el trabajo de construcción de requisitos; reutilizar cuestiones compartidas sin perder aplicabilidad; y mantener trazabilidad hacia las fuentes que justifican la segmentación.

La taxonomía no pretende resolver por sí misma los requisitos de demanda, establecer la calidad de la información publicada, decidir si un producto es adecuado para un comprador particular ni reproducir todas las categorías de comercio digital disponibles.

### 1.2. Alcance del proyecto que debe respetarse

El estudio se centra en el **descubrimiento y la decisión de compra**, para el contexto relevante en España desde octubre de 2026, con horizonte al menos hasta el primer trimestre de 2027. Considera productos, variantes, ofertas, vendedores y condiciones comerciales, y evalúa las representaciones por los ámbitos Catálogos distribuidos, Web y Web Schema.org, bajo los perfiles de consumo definidos [M1, M2].

La taxonomía es transversal a esos ámbitos: **no se diseña una clase distinta porque una interfaz tenga o no tenga cierto campo**. El vínculo con interfaces se determina posteriormente al definir qué requisitos resultan pertinentes para cada ámbito [M2].

### 1.3. Conceptos que no deben confundirse

| Concepto | Significado operativo para el proyecto |
|---|---|
| Categoría externa | Nodo de una clasificación Shopify, Google o Amazon; responde a fines de la plataforma. |
| Tipo de producto externo | Noción propia del sistema proveedor; en Amazon, un tipo PTD no equivale necesariamente a un nodo de navegación. |
| Atributo y valor | Característica y posible valor descriptivo; pueden revelar una especialización, pero no son clases por defecto. |
| Clase interna | Conjunto de productos u ofertas delimitado por reglas claras y necesidades informativas suficientemente homogéneas. |
| Subclase interna | Clase más específica cuya delimitación y diferenciación informativa están justificadas. |
| Faceta | Dimensión transversal (uso, protección, estilo, material...) que ayuda a segmentar sin exigir una rama exclusiva. |
| Modelo de demanda | Catálogo de requisitos informativos pertinentes para la clase, con objeto, alcance, aplicabilidad e importancia relativa. |
| Variante u oferta | Entidades comerciales sobre las que recaen preguntas; no son automáticamente categorías taxonómicas. |

**Precedencia documental.** En definiciones de calidad informativa, requisitos, ámbitos e indicadores prevalecen *Contexto y marco del estudio* y *Conceptos base del sistema de estudio* [M1, M2]. Este documento propone la arquitectura de clasificación y no modifica aquellas definiciones. El documento de fundamentos consolidados es apoyo interpretativo [M3].

## 2. Inventario razonado de fuentes externas

### 2.1. Shopify: base estructural y vocabulario de atributos

La **Shopify Standard Product Taxonomy** dispone de categorías jerárquicas, atributos, valores, localizaciones y archivos de correspondencias con otras clasificaciones. Su repositorio es abierto y proporciona distribuciones versionadas [R1, R2]. La última versión estable verificada para esta referencia es **v2026-08**, publicada el 24 de agosto de 2026 [R3].

Su utilidad principal es ofrecer un **esqueleto compartido de familias y clases candidatas** con IDs, rutas y relaciones de categorías, junto con atributos que pueden sugerir dimensiones de demanda. No debe interpretarse que cada hoja es una clase obligatoria del proyecto ni que cada atributo se transforma automáticamente en un requisito.

Shopify también publica mapeos hacia Google, pero la integración documentada con Google está referida a la taxonomía **2021-09-21**; no debe suponerse que representa la última semántica de Google o que constituye un mapeo exhaustivo a Amazon [R4].

**Tratamiento:** mantener una instantánea fija del sistema externo, conservar ID, nombre, ruta, jerarquía, versión y procedencia de sus atributos. Las denominaciones traducidas son etiquetas de presentación, no claves de identidad.

### 2.2. Amazon: especialización comercial, con dos sistemas distintos

Amazon dispone de una estructura de **nodos de navegación (browse nodes / Browse Tree Guides)** destinada a clasificar y hacer descubribles productos. Los nodos pueden formar parte de múltiples rutas; por ello su organización no debe convertirse sin análisis en un árbol único [R5, R6].

Además, las **Product Type Definitions (PTD)** proporcionan esquemas JSON de atributos y reglas de datos para los tipos de producto del catálogo Amazon. Un *product type* de Amazon no es el mismo objeto que un *browse node*, aunque ambos puedan relacionarse durante la publicación y clasificación de ofertas [R7, R8].

El informe `GET_XML_BROWSE_TREE_DATA` expone la jerarquía y los refinamientos de la navegación por marketplace, pero requiere acceso autorizado como vendedor mediante la SP-API [R5]. Por ello **no se afirma aquí la existencia o vigencia en Amazon.es de un nodo concreto de botas de montaña** hasta contrastarlo con una extracción actual del marketplace español.

**Tratamiento:** usar el árbol Amazon como descubridor de especializaciones candidatas y los PTD como fuente adicional de atributos y condiciones descriptivas. Documentar marketplace, fecha, identificador de nodo o tipo, ruta y nivel de comprobación.

### 2.3. Google: contraste, datos comerciales y vocabulario de exposición

Google mantiene una **Product Taxonomy** para clasificar productos en Merchant Center y permite a los comerciantes declarar su propio `product_type`; este último no es una rama oficial añadida por Google [R9, R10].

La **Product Data Specification** de Merchant Center define atributos, formatos, valores y reglas según producto, mercado o destino [R11]. El atributo `product_detail` permite publicar especificaciones adicionales mediante nombres y valores elegidos por el comerciante, pero no constituye una ontología universal y cerrada por categoría [R12]. **Manufacturer Center** aporta especificaciones adicionales desde la perspectiva de fabricante [R13].

Las guías de **Google Search sobre `Product`, `Offer` y `ProductGroup`** documentan expresiones de información estructurada y relaciones entre variantes, pero **no son una taxonomía de subclases de producto** [R14, R15]. Son especialmente útiles para relacionar el futuro modelo de demanda con su evaluación por interfaces, sin determinar por sí mismas la segmentación de clases.

**Tratamiento:** emplear Google para contrastar el alcance de clases, identificar dimensiones de información comercial y verificar vocabulario de los canales. Las obligaciones de un feed se estudian separadamente como requisitos técnicos o de plataforma: **no equivalen a requisitos informativos críticos por definición** [M2].

### 2.4. Evidencia comercial y otras referencias

La publicación real de **ecommerce referentes** sigue siendo fuente principal para inferir las cuestiones de demanda, conforme a los documentos rectores [M2, M3]. En esta fase también sirve para comprobar si una especialización es reconocible de forma estable en el mercado y si sus características se diferencian de las de otras clases.

Como vocabulario metodológico de correspondencias puede utilizarse **SKOS**, estándar del W3C que distingue `exactMatch`, `closeMatch`, `broadMatch`, `narrowMatch` y `relatedMatch` [R16]. Su aplicación es una **opción de diseño** y exige definir las reglas de uso locales. No cubre por sí solo todos los casos de solapamiento parcial y pertenencia condicional que pueden darse entre clasificaciones comerciales.

## 3. Estrategia de integración propuesta

### 3.1. No fusionar literalmente las fuentes: integrar sus significados

La vía recomendada es una **integración semántica con identificadores internos estables**, no la unión de nombres o nodos. Las fuentes siguen existiendo como sistemas autónomos. Cada clase propia explicita a qué nodos o atributos externos se vincula, qué relación mantiene con ellos y con qué fundamento.

Una coincidencia de etiqueta no acredita identidad conceptual; dos conceptos pueden compartir nombre y tener inclusiones distintas. Inversamente, dos categorías con nombres diferentes pueden cubrir prácticamente el mismo dominio. La semántica se verifica por **definición, reglas de inclusión, uso comercial y ejemplos positivos/negativos**, no solo por la ruta nominal.

### 3.2. Arquitectura de cinco capas

| Capa | Contenido | Resultado esperado |
|---|---|---|
| 0. Fuentes congeladas | Versiones de Shopify, Amazon por marketplace, Google y fuentes documentales. | Procedencia reproducible. |
| 1. Alineación semántica | Conceptos externos, atributos, definiciones y correspondencias con revisión. | Mapa de relaciones, sin perder discrepancias. |
| 2. Taxonomía propia | Clases, subclases, posibles facetas, inclusiones y exclusiones. | Estructura canónica para delimitar el estudio. |
| 3. Modelos de demanda | Requisitos compartidos y diferenciales, con aplicabilidad e importancia relativa. | Catálogo de preguntas evaluables por clase. |
| 4. Auditoría por ámbito | Evaluación posterior de la resolución de cada requisito en cada interfaz pertinente. | Diagnóstico de calidad informativa; fuera del objeto de esta taxonomía. |

Esta separación evita que el cambio de un nodo Amazon o un atributo de Google obligue a cambiar de inmediato el significado de una clase interna o a reescribir todos los requisitos del estudio.

### 3.3. Jerarquía y facetas, no profundidad uniforme

La clasificación principal puede mantener una relación **general-específico** y permitir, cuando sea necesario, múltiples pertenencias o facetas. Por ejemplo, el uso previsto y el nivel de protección pueden cruzarse: ciertas botas son simultáneamente calzado de montaña y equipo de protección. No conviene forzar una elección arbitraria entre esas ramas si altera qué requisitos resultan aplicables.

Si la herramienta operativa solo admite un padre, conservar un **padre primario** para navegación y representar las demás relaciones mediante facetas y vínculos tipados. Este es un compromiso de implementación, no una afirmación ontológica de exclusividad.

**No establecer un nivel de profundidad fijo.** El objetivo práctico de obtener al menos una especialización adicional se aplica donde exista una diferencia significativa de demanda y evidencias; no como mandato de subdividir todas las clases Shopify.

## 4. Reglas para alinear conceptos de las tres plataformas

### 4.1. Relaciones que debe poder registrar un mapeo

| Relación | Uso recomendado |
|---|---|
| Equivalente confirmada | Extensiones y definiciones suficientemente alineadas para uso intercambiable en el alcance estudiado. |
| Aproximadamente equivalente | Alta similitud, pero diferencias de frontera o uso que deben conservarse. |
| Más amplia / más específica | Una categoría incluye conceptualmente a la otra dentro del alcance declarado. |
| Relacionada | Relación asociativa sin implicación de inclusión. |
| Solapamiento parcial | Parte de los productos pertenece a ambos conceptos, pero ninguno contiene al otro por completo. |
| Sin correspondencia comprobada | No se identifica un equivalente defendible o la referencia necesaria no está disponible. |

Los tipos anteriores son una propuesta interna inspirada en SKOS [R16]. **No deben confundirse `equivalente` con `identidad absoluta`**, ni representarse todos los solapamientos como equivalencias exactas.

### 4.2. Procedimiento de correspondencia

1. **Identificar los dos extremos:** sistema, versión, marketplace cuando corresponda, ID, nombre y ruta completa.
2. **Examinar el alcance:** definición, finalidad funcional, productos incluidos y excluidos, atributos distintivos y posibles relaciones con otras ramas.
3. **Proponer la relación:** equivalencia, inclusión jerárquica, aproximación, relación o solapamiento; evitar decisiones binarias precipitadas.
4. **Contrastar con casos:** productos representativos y contraejemplos, información de ecommerce referentes y documentación de las fuentes.
5. **Registrar evidencia y estado:** fuente concreta, justificación, revisión y si el mapeo es provisional o está validado.
6. **Comprobar consecuencias:** qué clases internas, facetas y requisitos informativos se verían afectados por utilizar esa correspondencia.

Se admiten relaciones **uno-a-varios y varios-a-varios**. La ausencia de mapeo no obliga a descartar una clase candidata; obliga a identificar correctamente su origen y el grado de incertidumbre.

### 4.3. Semáforo de validación de las relaciones (no puntuación de calidad)

- **Validado:** fuentes verificadas y definiciones comparadas; los casos fronterizos se han resuelto o explicitado.
- **Provisional:** correspondencia plausible con algún límite relevante pendiente de contraste.
- **No verificado:** se cuenta con un nombre, ejemplo o referencia parcial, pero faltan evidencias para establecer una relación semántica.
- **Rechazado o sustituido:** la correspondencia se descartó o cambió tras la revisión, conservando historial.

Estos estados son controles de **gobierno de la taxonomía**, no grados de satisfacción de criterios ni indicadores de calidad informativa del sistema de auditoría.

## 5. Cuándo crear una subclase de producto

### 5.1. La subclase debe expresar diferencia informativa, no solo una etiqueta

Una subclase justifica su existencia cuando identifica un conjunto estable de productos con **función, uso o características que generan cuestiones informativas centrales distintas**, cambios materiales de aplicabilidad o una importancia relativa justificablemente diferente respecto de la clase base.

El mero hecho de que Amazon disponga de un nodo adicional o Shopify ofrezca un valor de estilo **no obliga** a crear una nueva clase. También puede ser innecesaria una subclase si las preguntas son esencialmente las mismas y solo cambian los valores esperados, como negro frente a marrón.

### 5.2. Prueba de especialización

| Pregunta de control | Criterio de decisión |
|---|---|
| ¿Hay una definición positiva clara? | Se puede explicar la pertenencia sin definir la clase como simple resto de otra. |
| ¿Existe una diferencia funcional estable? | El uso o función no depende solo de una etiqueta promocional. |
| ¿Cambian preguntas relevantes? | Aparecen cuestiones nuevas o diferencias sustantivas en alcance, aplicabilidad o importancia relativa. |
| ¿Hay respaldo observable? | La distinción tiene apoyo en fuentes taxonómicas y/o ecommerce referentes. |
| ¿Se resuelve con una condición? | Si basta con una regla de aplicabilidad en el mismo modelo, evitar duplicar clases. |
| ¿Se solapa transversalmente? | Si cruza múltiples ramas, considerar faceta o pertenencia múltiple en lugar de un único hijo. |

### 5.3. Cuatro salidas posibles del análisis

- **Conservar clase única:** no existe diferencia informativa suficientemente fundamentada.
- **Conservar la clase y condicionar requisitos:** algunas cuestiones aplican solo bajo determinadas características, sin construir un modelo independiente.
- **Crear una faceta transversal:** una dimensión (uso, estilo, protección) segmenta productos de diversas clases.
- **Crear una subclase con modelo propio:** cambia de forma estable un conjunto importante de cuestiones, con una definición clara y evidencias suficientes.

Cuando hay herencia de requisitos, la clase hija puede **reutilizar preguntas compartidas**, pero la aplicabilidad y la importancia relativa se revisan expresamente. No se hereda automáticamente la criticidad ni se asignan pesos numéricos universales [M2].

## 6. Ejemplo metodológico: botas urbanas y botas de montaña

### 6.1. De la fuente al concepto interno

El ejemplo expresa la estrategia, **no certifica una jerarquía vigente de Amazon.es**. Se parte de una categoría amplia Shopify de botas. En sus valores descriptivos pueden existir estilos o usos orientados al senderismo; Amazon puede proponer rutas especializadas de calzado deportivo o de exterior, pero el nodo español específico deberá verificarse antes de incorporar su ID. Google puede ofrecer una categoría de calzado más general y datos descriptivos, sin aportar necesariamente la subclase buscada [R1, R5, R9].

| Elemento observado | Uso en el piloto | Precaución |
|---|---|---|
| Shopify: botas | Clase base candidata. | No supone que todas las botas compartan un modelo homogéneo. |
| Shopify: atributo o valor asociado a senderismo | Evidencia de una posible faceta de uso. | Un valor de atributo no es automáticamente un nuevo nodo. |
| Amazon: posible nodo de actividad o calzado de exterior | Especialización candidata por contrastar en Amazon.es. | No declarar equivalencia exacta sin revisar inclusiones y rutas. |
| Google: calzado y atributos comerciales | Contraste de categoría y dimensiones. | `product_type` del comerciante no es taxonomía de Google. |
| Ecommerce referentes | Evidencia de diferenciación informativa real. | Una estructura de menú aislada no demuestra demanda general. |

### 6.2. Definiciones iniciales como hipótesis, no clases aprobadas

**Botas de uso urbano o casual:** calzado tipo bota cuyo contexto predominante es el uso cotidiano y/o de moda. Debe definirse con criterios positivos; no basta decir "todas las botas que no son de montaña". **Botas de senderismo:** botas diseñadas o comercializadas para rutas a pie en terrenos naturales, con necesidades posibles sobre agarre, terreno, protección, impermeabilidad y estabilidad. **Botas de seguridad:** producto cuyo uso protector puede implicar requisitos de certificaciones y protecciones específicas. Los tres conceptos pueden tener fronteras no excluyentes y deben validarse.

### 6.3. Diferencias de cuestiones candidatas

| Cuestiones compartidas | ¿En qué puede diferir la demanda? |
|---|---|
| Talla y sistema de medidas; composición y materiales; variantes; precio, disponibilidad y condiciones de comercialización. | Urbano/casual: estilo, diseño, altura de caña, tipo de cierre o ajuste. Senderismo: terreno previsto, agarre, impermeabilidad, soporte, protección y características de suela. Seguridad: protección declarada, certificaciones, condiciones de uso y limitaciones. |

Estos son **candidatos a requisitos**, no un catálogo ya validado. Su formulación definitiva deberá ser una cuestión evaluable: por ejemplo, "¿Para qué tipos de terreno y condiciones de uso está diseñada la bota?". Una vez formulada, se justifica su relevancia, aplicabilidad y clase de importancia, sin inferirla de una etiqueta de Shopify o Amazon [M2, M3].

### 6.4. Decisión del piloto

La pregunta no es "¿dónde está en el árbol de Amazon?", sino **"¿la distinción entre ambos usos cambia suficientemente lo que debemos poder conocer para evaluar la oferta?"**. Si la respuesta está fundamentada, se crea la subclase o faceta correspondiente; si no, se conserva la clase y se condicionan los requisitos relevantes. El acceso a la estructura Amazon mejoraría el fundamento, pero no reemplaza el análisis informativo.

## 7. De la clase al modelo de demanda

El documento *Conceptos base del sistema de estudio* ya fija el método general: **observar atributos e información comercial publicada; inferir cuestiones relevantes; formular y normalizar requisitos; justificar su inclusión e importancia relativa** [M2]. La taxonomía propuesta organiza la **selección de la clase y la detección de diferencias**, no modifica ese procedimiento.

Para cada clase aprobada se recomienda mantener una **matriz de continuidad**: requisitos comunes de la familia, requisitos específicos, requisitos condicionados y cuestiones excluidas por no aplicables. Cada requisito conservará su pregunta, dimensión, entidad, alcance, aplicabilidad, importancia relativa, fundamento y fuentes. Un mismo requisito podrá asociarse a varias clases sin duplicar su definición.

Hay tres separaciones necesarias:

1. **Clasificación frente a demanda:** la taxonomía describe el dominio; el requisito formula una necesidad de conocimiento.
2. **Requisito informativo frente a atributo del feed:** el atributo puede contribuir a una respuesta, pero ni define automáticamente el requisito ni su importancia.
3. **Clases frente a interfaces:** la pregunta pertenece al modelo de demanda; su pertinencia y capacidad de resolución se evalúan posteriormente en Catálogos distribuidos, Web y Web Schema.org, según sus funciones y condiciones [M2].

La **disponibilidad efectiva**, los seis criterios de aceptación, las propiedades P06-P18 y la valoración por requisito e interfaz pertenecen al sistema de auditoría posterior [M2, M3]. No deben introducirse como criterios técnicos de fusiones taxonómicas ni utilizarse para decidir qué es una clase.

## 8. Modelo de datos de referencia (sin importar árboles completos)

La implementación mínima necesita separar fuentes, conceptos externos, clases internas, correspondencias, evidencia comercial y requisitos. Los campos siguientes son **orientativos**, no un esquema informático cerrado.

| Entidad lógica | Campos esenciales |
|---|---|
| `source_snapshot` | sistema, versión, marketplace/idioma, fecha, URL, condiciones de acceso, huella y estado de revisión. |
| `external_concept` | ID origen, nombre, ruta, clase de objeto (nodo, atributo, valor, PTD), referencia a instantánea. |
| `product_class` | ID interno, nombre, definición, inclusiones, exclusiones, clase(s) padre, estado, versión. |
| `class_facet` | faceta, valores, criterio de uso, relación con clases pertinentes. |
| `concept_mapping` | concepto externo, clase interna, tipo de relación, evidencia, justificación, estado, fecha de revisión. |
| `commercial_evidence` | ecommerce/recurso, observación, fecha, característica, clase candidata y fundamento de uso. |
| `information_requirement` | ID, pregunta, dimensión, objeto/alcance, aplicabilidad, importancia, justificación, fuente. |
| `class_requirement` | clase, RI, condición, estado de reutilización, diferencias de importancia o alcance. |
| `change_log` | versión de clase, cambio, motivo, fuentes afectadas, impacto y aprobación. |

**Regla de trazabilidad:** una clase interna puede mapearse a varios conceptos externos y una misma categoría externa puede servir de referencia a varias clases. Una pregunta informativa puede derivarse de múltiples evidencias; una evidencia de atributo puede sugerir más de una pregunta. Ninguna relación debe forzarse a ser uno-a-uno.

## 9. Procedimiento de construcción y revisión

| Etapa | Actividad | Entregable / control |
|---|---|---|
| 0. Delimitación | Definir familias piloto, mercado, versión y objetivos de especialización. | Alcance aprobado. |
| 1. Fijar fuentes | Congelar Shopify; inventariar Google; obtener Amazon autorizado si está disponible. | Registro de fuentes, versiones y accesos. |
| 2. Recoger candidatos | Identificar categorías, atributos, valores y rutas que sugieran especializaciones. | Inventario de conceptos candidatos. |
| 3. Alinear | Crear correspondencias semánticas y registrar solapamientos, ausencias y dudas. | Tabla de mapeos con evidencia y estado. |
| 4. Delimitar clases | Formular definiciones, inclusiones, exclusiones, padres y facetas. | Fichas de clase propuestas. |
| 5. Contrastar | Revisar ecommerce referentes y casos fronterizos; decidir entre subclase, faceta o aplicabilidad. | Clases validadas o pendientes, con motivos. |
| 6. Construir demanda | Inferir, normalizar y justificar las preguntas por clase, reutilizando núcleos comunes. | Primeros modelos de demanda. |
| 7. Calibrar | Detectar duplicaciones, clases artificiales, vacíos, reglas ambiguas e importancia inconsistente. | Registro de cambios y aprobación de piloto. |
| 8. Mantener | Revisar versiones externas, nuevos usos y evidencias comerciales, controlando impacto. | Versionado y gobierno del catálogo. |

**Condiciones para cerrar una clase:** definición positiva; al menos una regla clara de pertenencia; frontera de exclusión documentada; correspondencias con origen y estado; evidencia suficiente de diferenciación; y decisión explícita sobre si necesita modelo propio o condiciones de aplicabilidad. No se establece una cuota numérica universal de categorías por rama.

### 9.1. Prueba piloto aconsejada

La familia **calzado > botas** es idónea para probar las decisiones porque incluye estilos comerciales y usos técnicos potencialmente diferentes. Un piloto acotado debería: seleccionar la categoría Shopify base, identificar posibles facetas y especializaciones, comprobar Amazon.es si se dispone de acceso, contrastar un conjunto razonado de ecommerce referentes, formular modelos de demanda provisionales y decidir qué distinciones soportan clases independientes.

El éxito no se mide por el número de nodos creados, sino por la **claridad de fronteras, coherencia de la asignación de productos y explicabilidad de las diferencias de requisitos**.

## 10. Gobierno, versiones y riesgos

### 10.1. Política de cambio

- Cada fuente externa conserva su versión y ámbito geográfico o de marketplace; no se mezcla información de diferentes fechas como si fuese una única instantánea.
- Los identificadores propios de clase permanecen estables mientras la definición conceptual sea equivalente; una división, fusión o redefinición significativa genera un cambio controlado.
- Los mapeos deben revisarse al cambiar un origen externo o aparecer evidencia que altere fronteras conceptuales.
- Cambios de etiqueta o traducción no deben modificar por sí mismos la identidad de clase.
- Los cambios de clase deben acompañarse de un **análisis de impacto** sobre requisitos informativos, aplicabilidad e importancia relativa; no se reescriben automáticamente.
- La consulta y reutilización de datos Amazon queda supeditada a permisos y condiciones de uso aplicables; la taxonomía propia no debe prometer una descarga pública completa de Amazon.

### 10.2. Riesgos y medidas preventivas

| Riesgo | Prevención |
|---|---|
| Unir árboles por nombres | Mapear semántica con IDs, inclusiones, contraejemplos y evidencia. |
| Crear un modelo por hoja externa | Exigir justificación de homogeneidad y diferencia informativa. |
| Convertir atributo o variante en clase | Distinguir dimensión, valor, faceta, subclase y entidad comercial. |
| Ignorar solapamiento funcional | Admitir varias relaciones, pertenencia múltiple o facetas. |
| Usar PTD Amazon como nodo BTG | Registrar por separado tipo de producto y nodo de navegación. |
| Tomar `product_type` de Google como oficial | Tratarlo como clasificación declarada por comerciante. |
| Presentar mapeos Shopify-Google como actuales sin fecha | Registrar que Shopify documenta versión Google 2021-09-21. |
| Confundir requisitos de plataforma con demanda | Justificar preguntas e importancia por relevancia informativa, no por validación técnica. |
| Suponer un nodo Amazon.es sin extracción vigente | Marcar no verificado y no asignar ID definitivo. |
| Reutilizar criticidad sin revisar clase | Confirmar importancia y aplicabilidad en cada clase [M2]. |

### 10.3. Indicadores útiles de salud de la taxonomía

Porcentaje de clases con definición completa y evidencias; porcentaje de correspondencias validadas frente a provisionales; conceptos sin mapeo; fronteras con solapamiento documentado; tasa de asignaciones de producto ambiguas en muestras; número de clases nuevas que no aportan diferencias relevantes de requisitos; proporción de requisitos compartidos frente a específicos; y cambios pendientes de propagación a modelos de demanda.

Son **medidas de gobierno y cobertura**, no los indicadores IR, ICI, GSC o los indicadores técnicos de la auditoría [M2].

## 11. Conclusiones y decisiones pendientes

### 11.1. Conclusiones respaldadas por fuentes

1. Shopify ofrece una clasificación estructurada con categorías y atributos versionados, adecuada como punto de partida abierto [R1-R4].
2. Amazon aporta nodos de navegación y esquemas PTD diferentes, que pueden suministrar especializaciones y atributos; su consulta completa mediante informes requiere acceso de vendedor [R5-R8].
3. Google dispone de categorías propias, especificaciones de atributos, `product_type` comerciante y `product_detail`, pero no equivale a un árbol universal de subclases funcionales con atributos cerrados [R9-R15].
4. Las correspondencias entre sistemas pueden ser jerárquicas, aproximadas o asociativas; la normalización semántica requiere decisiones explícitas y evidencia [R16].
5. El modelo de demanda del proyecto exige requisitos inferidos y justificados; no se obtiene automáticamente de campos taxonómicos [M1-M3].

### 11.2. Orientaciones de diseño recomendadas (no decisiones rectoras ya aprobadas)

- Adoptar **Shopify v2026-08 como instantánea inicial** y estructura principal de familias.
- Incorporar **Amazon** como fuente de especializaciones y atributos, cuando el acceso y las evidencias lo permitan.
- Incorporar **Google** como referencia de clasificación, atributos y reglas comerciales, separando semántica de obligación de interfaz.
- Mantener **clases internas con IDs propios**, definiciones, facetas y mapeos versionados.
- Crear subclases solo cuando existan **fronteras positivas y diferencias sustantivas de necesidades de información**.
- Reutilizar requisitos comunes con reglas explícitas de aplicabilidad; validar la importancia relativa en cada clase.

### 11.3. Decisiones que el proyecto todavía debe validar

- Si las clases internas admiten varios padres o si habrá un padre principal más facetas y relaciones adicionales.
- Los criterios operativos y la evidencia mínima para aprobar equivalencias y nuevas subclases.
- La disponibilidad de acceso SP-API para obtener el árbol vigente de Amazon.es y las restricciones de reutilización de esos datos.
- La selección de ecommerce referentes y casos frontera para el piloto de botas.
- El grado de especialización que realmente reduce ambigüedad sin fragmentar innecesariamente los modelos de demanda.
- El mecanismo de gobierno, revisión y calendario de actualización de fuentes externas.

## 12. Fuentes y materiales de referencia

### Documentos del proyecto (precedencia interna)

- **[M1]** *Contexto y marco del estudio* (`Contexto_marco_de_estudio.md`). Objeto, alcance geográfico y funcional; información comercial; ámbitos examinados.
- **[M2]** *Conceptos base del sistema de estudio* (`Conceptos_base_sistema_de_estudio.md`). Definición de modelo de demanda, requisito informativo, construcción vigente, aplicabilidad, importancia e interfaces.
- **[M3]** *Fundamentos consolidados del sistema de estudio y auditoría de la calidad de la información comercial* (`Fundamentos_consolidados_calidad_de_la_informacion_comercial.md`, 24/10/2026). Consolidación interpretativa compatible, sin desplazar [M1] y [M2].

### Fuentes oficiales externas (consulta: 24 de octubre de 2026)

- **[R1] Shopify.** [Standard Product Taxonomy: repositorio, modelo y distribución](https://github.com/Shopify/product-taxonomy). Fuente principal de estructura, atributos y política de versiones.
- **[R2] Shopify.** [Taxonomy Explorer](https://shopify.github.io/product-taxonomy/). Exploración de categorías y atributos.
- **[R3] Shopify.** [Release v2026-08](https://github.com/Shopify/product-taxonomy/releases/tag/v2026-08). Versión estable fijada para la referencia inicial.
- **[R4] Shopify.** [Integrations / mapping documentation](https://github.com/Shopify/product-taxonomy/blob/main/data/integrations/README.md). Mapeos disponibles y versiones de Google usadas.
- **[R5] Amazon SP-API.** [Browse Tree Reports](https://developer-docs.amazon/sp-api/docs/report-type-values-browse-tree). Informe `GET_XML_BROWSE_TREE_DATA`, contenido y permisos de acceso.
- **[R6] Amazon Seller Central.** [Browse for products (Amazon.es)](https://sellercentral.amazon.es/help/hub/reference/external/G202078740) y [Change a product’s category or browse path](https://sellercentral.amazon.com/help/hub/reference/external/G201950630). Jerarquía de navegación, asignación por nodo y posibilidad de múltiples rutas (la segunda guía corresponde al marketplace estadounidense; la propiedad se usa como precaución estructural).
- **[R7] Amazon SP-API.** [Product Type Definitions API](https://developer-docs.amazon/sp-api/docs/product-type-definitions-api). Esquemas de requisitos de datos por tipo de producto.
- **[R8] Amazon SP-API.** [Catalog Items API v2022-04-01](https://developer-docs.amazon/sp-api/lang-es_es/docs/catalog-items-api-v2022-04-01-reference). Datasets diferenciados `attributes`, `classifications` y `productTypes`.
- **[R9] Google Merchant Center.** [Categoría de producto de Google](https://support.google.com/merchants/answer/6324436?hl=es). Jerarquía propia y asignación de categoría.
- **[R10] Google Merchant Center.** [Tipo de producto del comerciante](https://support.google.com/merchants/answer/6324406?hl=es-es). Diferencia entre `product_type` y categoría Google.
- **[R11] Google Merchant Center.** [Especificación de datos de producto](https://support.google.com/merchants/answer/7052112?hl=es). Atributos y reglas por categoría / mercado / destino.
- **[R12] Google Merchant Center.** [Detalles del producto (`product_detail`)](https://support.google.com/merchants/answer/9218260?hl=es). Vocabulario abierto para detalles adicionales.
- **[R13] Google Manufacturer Center.** [Product data specification](https://support.google.com/manufacturers/answer/6124116?hl=en). Datos ampliados de fabricante.
- **[R14] Google Search Central.** [Introduction to Product structured data](https://developers.google.com/search/docs/appearance/structured-data/product). Distinción de tipos de marcado y fuentes de datos.
- **[R15] Google Search Central.** [Product variant structured data (`ProductGroup`)](https://developers.google.com/search/docs/appearance/structured-data/product-variants). Modelo de relaciones entre producto y variantes.
- **[R16] W3C.** [SKOS Simple Knowledge Organization System Reference](https://www.w3.org/TR/skos-reference/). Vocabulario metodológico de relaciones de correspondencia.

**Nota sobre evidencia:** este documento registra conclusiones de documentación externa y decisiones metodológicas propuestas. No constituye una extracción del árbol completo de Amazon.es ni certifica mapeos específicos entre hojas de las tres plataformas. La aprobación de clases requiere la comprobación indicada en el método.

## Anexo A. Ficha de clase propuesta

**Identidad:** ID interno; nombre canónico ES; otras denominaciones; estado; versión.  
**Definición:** función principal y alcance; reglas positivas de inclusión; exclusiones; ejemplos positivos y negativos.  
**Estructura:** padre(s); facetas relevantes; especializaciones; relaciones no jerárquicas.  
**Correspondencias:** Shopify/Amazon/Google (sistema, versión, marketplace, ID, ruta, relación, grado de verificación).  
**Diferenciación de demanda:** preguntas compartidas, preguntas específicas, condiciones de aplicabilidad y justificación de modelo propio.  
**Evidencia y revisión:** fuentes, ecommerce observados, casos frontera, responsable, fecha y cambios.

## Anexo B. Ficha de correspondencia propuesta

**Origen:** sistema, versión, marketplace, ID, etiqueta y ruta.  
**Destino:** clase interna (ID y versión).  
**Relación:** equivalente / cercana / más amplia / más específica / relacionada / solapamiento / sin correspondencia.  
**Fundamento:** definición comparada, inclusiones, exclusiones y ejemplos.  
**Estado:** validado / provisional / no verificado / rechazado; fecha; responsable; vínculos a evidencia.  
**Consecuencia:** efecto sobre pertenencia de productos, facetas y requisitos de demanda si cambia el mapeo.

