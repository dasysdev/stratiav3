# Marco metodológico para construir el Modelo de Prácticas Informativas de Referencia (MPIR)

*Estrategia de observación, extracción, estructuración y análisis de información comercial publicada por ecommerce referentes para apoyar la construcción sistemática de modelos de demanda*

**Proyecto:** Calidad de información v1  
**Fecha de referencia:** 24 de octubre de 2026  
**Versión:** 1.0 — metodología inicial consolidada para aplicación y calibración  
**Naturaleza:** documento metodológico de la segunda vía de construcción del modelo de demanda. No es un catálogo de requisitos informativos, una auditoría de ecommerce ni una especificación cerrada de software.

## Resumen ejecutivo

El **Modelo de Prácticas Informativas de Referencia (MPIR)** es una base de conocimiento estructurada que documenta **cómo los ecommerce referentes presentan, explican, relacionan y utilizan información comercial para facilitar el descubrimiento, la comprensión, la comparación y la evaluación de sus ofertas**. Su utilidad es ofrecer **evidencia indirecta sobre posibles necesidades informativas de la demanda** de una clase de producto u oferta.

El MPIR complementa el **Modelo de Taxonomía de Productos**, basado en la integración semántica de Shopify, Amazon y Google. La taxonomía delimita las clases y facilita reconocer atributos, facetas y dimensiones del dominio. El MPIR permite observar **qué preguntas se anticipan, qué criterios de elección se emplean, qué contextos y relaciones se explican y cómo se ayuda a tomar decisiones**. Las dos fuentes se utilizan posteriormente para inferir, formular y justificar requisitos informativos del **modelo de demanda**.

La estrategia de adquisición será **híbrida, estructural y semántica**, pero con responsabilidades separadas: **capturar y preservar las fuentes originales → construir un corpus estructurado de unidades informativas → identificar señales y prácticas candidatas → consolidar patrones entre referentes → transferir evidencia contrastada al proceso de construcción de requisitos informativos**. Las etapas pueden ejecutarse en ciclos incrementales; la interpretación no sustituye ni altera la evidencia conservada.

La hipótesis del método es que ecommerce reconocidos o especializados **pueden** reflejar, a través de sus decisiones informativas, conocimiento acumulado sobre las necesidades de sus compradores. **No se presupone** que sus prácticas sean correctas, universales o representativas de la frecuencia real de la demanda. El MPIR es una fuente **inferencial y cualitativa**, no una medición directa del mercado.

### Decisiones metodológicas adoptadas

| Cuestión | Decisión |
|---|---|
| Función del MPIR | Recoger y normalizar evidencias de prácticas informativas utilizadas como indicios indirectos de necesidades de demanda. |
| Relación con taxonomías | Complementaria: no duplicar mecánicamente atributos ni limitar la exploración a dimensiones taxonómicas conocidas. |
| Material de observación | Recursos informativos de ecommerce referentes relevantes para el descubrimiento y la decisión de compra. |
| Estrategia de extracción | Scraping orientado por recursos y bloques del DOM, con renderizado dinámico selectivo y análisis semántico posterior. |
| Persistencia | Conservar tanto el recurso original como las unidades estructuradas y las interpretaciones versionadas. |
| Unidad básica de evidencia | Unidad de contenido contextualizada, que puede contener texto, datos, opciones, entidades o relaciones y remite al recurso original. |
| Identificación de prácticas | Posterior y lógicamente independiente de la captura, con anotaciones preliminares permitidas durante el procesamiento. |
| Operación | Ciclos de extracción, análisis, revisión y ampliación; no esperar a completar todo el universo antes de analizar. |
| Inferencia | Separar lo publicado, la práctica interpretada y la necesidad informativa candidata. |
| Valoración | Sin puntuaciones de calidad ni conversión automática de frecuencia, prominencia o presencia en importancia del requisito. |

---

## 1. Propósito, alcance y encaje en el sistema de estudio

### 1.1. Finalidad

La finalidad es **identificar y documentar de forma sistemática indicios de qué cuestiones informativas se consideran útiles para comprender, comparar y evaluar ofertas de una clase**, observando cómo las tratan ecommerce referentes. Este conocimiento alimenta la inferencia del modelo de demanda sin sustituir su proceso de justificación.

El problema que aborda esta vía no es «¿qué atributos publica una tienda?» ni «¿qué ecommerce informa mejor?», sino:

> **¿Qué necesidades de conocimiento de la demanda podemos reconocer a partir de las decisiones informativas de ecommerce referentes que no se desprenden, o no quedan suficientemente desarrolladas, de las taxonomías de producto?**

El análisis puede producir confirmaciones, nuevas cuestiones, mayor profundidad de preguntas conocidas o diferencias de aplicabilidad entre clases y subclases.

### 1.2. Alcance funcional

Se mantiene el perímetro de los documentos rectores: **descubrimiento y decisión de compra**, en el contexto relevante para **España desde octubre de 2026**, con horizonte hasta al menos el primer trimestre de 2027. Se atiende a productos, variantes, ofertas, vendedores y condiciones comerciales **cuando su conocimiento interviene antes de decidir la compra**.

La exploración de referentes puede incluir páginas y herramientas interactivas como **fuentes para conocer prácticas informativas**. Ello no modifica el alcance **no interactivo** de la auditoría posterior de información comercial: son actividades y finalidades distintas.

No se investigan la preparación operativa de la compra, la ejecución de pagos, los procesos postcompra ni la infraestructura general de los ecommerce. Sí pueden observarse políticas de devolución o garantía en la medida en que **su conocimiento previo** sea relevante para valorar una oferta, sin auditar los procesos operativos correspondientes.

### 1.3. Relación con las dos vías de referencia

| Vía | Objeto observado | Contribución principal | Límite |
|---|---|---|---|
| **Modelo de Taxonomía de Productos** | Categorías, especializaciones, facetas, atributos, valores y correspondencias de Shopify, Amazon y Google. | Delimitar la clase e identificar dimensiones y distinciones candidatas. | No equivale al conjunto de preguntas necesarias para evaluar una oferta. |
| **MPIR** | Contenidos, estructuras y mecanismos informativos utilizados por ecommerce referentes. | Reconocer criterios de elección, preguntas anticipadas, contextos, relaciones, limitaciones y patrones de explicación/comparación. | No acredita por sí mismo frecuencia de demanda, corrección de las prácticas o importancia de los requisitos. |
| **Modelo de demanda** | Cuestiones informativas relevantes, inferidas y justificadas. | Definir los requisitos informativos de la clase con dimensión, alcance, aplicabilidad e importancia relativa. | No se obtiene copiando literalmente campos o contenidos de ninguna de las dos fuentes. |

La taxonomía propia es la **referencia para delimitar la muestra por clase**, pero el análisis comercial mantiene una **vía exploratoria abierta** para encontrar información que dicha taxonomía no haya anticipado.

### 1.4. Precedencia documental

Las definiciones de **modelo de demanda**, **requisito informativo**, **relevancia**, **importancia relativa**, **interfaces** y **evaluación** provienen de los documentos rectores [M1, M2]. El documento consolidado [M3] aporta desarrollo interpretativo; la metodología taxonómica [M4] fija la relación entre clases internas y fuentes externas. El presente documento operacionaliza **solo la vía de ecommerce referentes** y no modifica esos conceptos.

---

## 2. Hipótesis de observación y límites de inferencia

La hipótesis de trabajo es que algunos ecommerce especializados o con experiencia comercial significativa han invertido recursos en conocer a sus compradores y en organizar contenidos que anticipan necesidades de información. La observación de dichas decisiones permite aprovechar **indirectamente** ese conocimiento.

Se aplican las siguientes cautelas:

1. **Práctica observada ≠ necesidad demostrada.** Una FAQ, filtro o comparador ofrece un indicio razonable, no una prueba de demanda real.
2. **Autoridad comercial ≠ validación metodológica.** La escala o notoriedad de un ecommerce no asegura que todas sus decisiones informativas sean correctas.
3. **Frecuencia observada ≠ prevalencia en el mercado.** Cinco comercios que incluyen una cuestión no prueban cuántos compradores la necesitan.
4. **Prominencia editorial ≠ importancia relativa.** Posición visual, extensión del contenido y repetición pueden responder a SEO, publicidad, diferenciación, limitaciones de plataforma o estrategia de marca.
5. **Ausencia editorial ≠ irrelevancia.** Que una cuestión no aparezca en los referentes observados no implica que no deba incluirse en el modelo de demanda.
6. **Información del referente ≠ respuesta de una oferta auditada.** La evidencia usada para construir el modelo no puede incorporarse después como si fuera información publicada por el ecommerce objeto de auditoría.

Por tanto, el MPIR debe registrar **observaciones, interpretaciones, incertidumbres y fundamentos**. Si procede, el modelo de demanda podrá contrastarse después con consultas reales o investigación de usuarios, sin exigir que esa contrastación forme parte de esta fase inicial.

---

## 3. Objetos y niveles del sistema

### 3.1. Definiciones operativas

| Concepto | Definición dentro del MPIR |
|---|---|
| **Ecommerce referente** | Comercio seleccionado por su pertinencia, experiencia o especialización respecto de una clase, mediante criterios documentados. |
| **Recurso comercial** | Página o recurso del ecommerce examinado: ficha, categoría, guía, comparador, FAQ, selector, etc. |
| **Instantánea original** | Versión preservada del recurso obtenido, con contexto técnico y temporal suficiente para su revisión. |
| **Unidad de contenido estructurada** | Fragmento delimitado del recurso con sus valores, etiquetas, contexto, entidades y relaciones relevantes conservados. |
| **Señal informativa** | Observación contextualizada que sugiere una cuestión, criterio de elección, relación o condición informativa potencialmente relevante. |
| **Práctica informativa observada** | Forma identificable en que el ecommerce utiliza información para describir, orientar, explicar, relacionar, comparar o delimitar una decisión de compra. |
| **Patrón de referencia** | Formulación normalizada de una práctica o necesidad sugerida por una o varias evidencias, preservando variantes y excepciones. |
| **Cuestión candidata de demanda** | Pregunta potencialmente evaluable inferida a partir de un patrón o evidencia, todavía pendiente de normalización y justificación como requisito informativo. |
| **Requisito informativo (RI)** | Cuestión evaluable del modelo de demanda que especifica qué debe poder determinarse y fundamentarse sobre una oferta. Su validación pertenece a dicho modelo. |

**Diferencia esencial:** el corpus guarda **lo publicado**; las anotaciones semánticas registran **lo interpretado**; el MPIR consolida **prácticas y patrones**; el modelo de demanda define **lo que importa poder conocer**.

### 3.2. Arquitectura de información

```text
Clase interna y facetas (Modelo de Taxonomía de Productos)
                       |
                       v
      Panel de ecommerce y recursos seleccionados
                       |
                       v
        [A] Corpus de recursos originales
            HTML / DOM / datos admitidos
            procedencia, captura y versiones
                       |
                       v
        [B] Corpus estructurado de evidencias
            bloques, tablas, filtros, FAQ,
            entidades, contexto y relaciones
                       |
                       v
        [C] Capa de señales e interpretaciones
            funciones, prácticas candidatas,
            preguntas sugeridas, incertidumbres
                       |
                       v
        [D] Modelo de Prácticas Informativas
            patrones normalizados entre fuentes
                       |
             contraste con taxonomías
                       v
        [E] Construcción del modelo de demanda
            requisitos informativos justificados
```

Las capas **A, B, C y D** se mantienen diferenciadas y vinculadas por identificadores. La **E** pertenece al proceso posterior de construcción de demanda; el MPIR le suministra evidencias y propuestas, sin aprobar automáticamente requisitos.

---

## 4. Diseño de la muestra: qué ecommerce y qué recursos observar

### 4.1. Delimitación por clase

Antes del rastreo se registra: identificador y versión de la clase interna, definición, inclusiones/exclusiones, subclases o facetas relevantes, mercado, idioma, periodo y temas taxonómicos ya reconocidos. Se prepara una **matriz inicial de cobertura** que permita detectar diferencias entre segmentos y tipologías de producto.

La lista de atributos conocida sirve de **guía de contraste**, no de filtro excluyente de la extracción.

### 4.2. Panel de ecommerce referentes

Se propone un **muestreo intencional y diversificado**, no una lista basada solo en tráfico o notoriedad. En la selección se considera:

- **Especialización y pertinencia:** conocimiento o surtido significativo de la clase estudiada.
- **Diversidad de modelos comerciales:** especialistas, distribuidores multimarca, fabricantes con venta directa y, si aporta contraste, generalistas.
- **Diversidad de segmentos:** usos, niveles de especialización, gamas, públicos y subclases pertinentes.
- **Riqueza de recursos informativos:** existencia de guías, comparadores, FAQ, filtros u otras formas de ayudar a elegir; sin descartar por sistema fuentes con formatos distintos.
- **Independencia editorial:** evitar contar como múltiples observaciones independientes el mismo contenido del fabricante replicado por varios vendedores.
- **Relevancia territorial y temporal:** preferir información aplicable al mercado estudiado y marcar expresamente diferencias de país, idioma o vigencia.
- **Viabilidad y legitimidad de acceso:** restricciones, condiciones de uso y cobertura realmente obtenible.

Cada comercio tendrá ficha de selección, tipo, motivos de inclusión, sesgos posibles y grado de independencia respecto de los demás. **No se establece un número universal de ecommerce:** la cantidad y mezcla se calibrarán en el piloto según diversidad y rendimiento informativo.

### 4.3. Perfiles de recursos

| Perfil | Qué permite observar | Precaución |
|---|---|---|
| **Ficha de producto / variante / oferta** | Atributos, prestaciones, diferenciadores, descripciones, relaciones, advertencias y condiciones comerciales. | No reducir el contenido a campos técnicos ni tratar todo argumento promocional como demanda. |
| **Página de categoría y filtros** | Facetas de búsqueda, criterios de selección, segmentación por usos o características. | Un filtro puede obedecer a restricciones de plataforma o merchandising. |
| **Comparador y tabla de alternativas** | Dimensiones de contraste, equivalencias, diferencias y compromisos. | Conservar asociaciones entre filas, columnas y entidades. |
| **Guías de compra y artículos técnicos** | Problemas, preguntas, contextos, recomendaciones, relaciones causa-uso y límites de adecuación. | Separar recomendaciones generales de hechos atribuidos a productos concretos. |
| **FAQ y contenidos de ayuda precompra** | Dudas anticipadas y condiciones que el comercio considera necesario explicar. | Distinguir contenido editorial de preguntas auténticas de usuarios cuando sea posible. |
| **Selectores y asistentes de elección** | Variables utilizadas para orientar una recomendación y secuencia de decisiones. | La exploración interactiva es investigación de referencia, no prueba del perfil de auditoría. |
| **Páginas informativas de condiciones comerciales** | Cuestiones previas a decidir sobre disponibilidad, envío, garantías o devoluciones. | No extender el análisis a la ejecución de procesos postcompra. |

Las reseñas, preguntas de usuarios y otros contenidos generados por terceros, cuando se incluyan, se marcarán como **evidencia de procedencia distinta**: no deben atribuirse a una decisión editorial del ecommerce sin justificación.

### 4.4. Selección de productos y casos

En cada perfil se seleccionan recursos representativos de los segmentos definidos: productos comunes, especializaciones relevantes, variantes o configuraciones diferenciadas, casos fronterizos y ofertas con condiciones distintas cuando ello pueda cambiar la cuestión informativa.

El muestreo debe permitir reconocer **preguntas compartidas, específicas y condicionadas**. No se presupone que cada subcategoría, variante o valor de un atributo exija un modelo de demanda independiente.

---

## 5. Estrategia técnica de captura y scraping

### 5.1. Principio rector

**Capturar con amplitud razonable dentro de un perímetro comercial definido, conservar la estructura y posponer las conclusiones semánticas.** No se pretende almacenar indiscriminadamente todo el dominio ni extraer únicamente los atributos previstos por la taxonomía.

### 5.2. Descubrimiento y clasificación de recursos

1. Identificar dominios autorizados, categorías y rutas vinculadas a la clase; utilizar sitemaps y enlaces internos cuando sean accesibles.
2. Detectar tipos de recursos por estructura, contenido y función, no exclusivamente por patrones de URL.
3. Registrar recursos candidatos, duplicados, redirecciones, variantes de idioma y paginación.
4. Seleccionar una muestra por clase, ecommerce, perfil de recurso y segmento según la matriz de cobertura.
5. Mantener un inventario también de recursos previstos pero no recuperados, con su causa y alcance.

### 5.3. Captura estructural como procedimiento principal

El procedimiento principal será la obtención del **HTML/DOM y sus bloques** con selectores CSS/XPath y reglas por plantilla, conservando, cuando sea pertinente:

- Encabezados, subtítulos, párrafos, listas, títulos y contenidos asociados.
- Preguntas y respuestas de FAQ, sin separar cada respuesta de su pregunta.
- Tablas con filas, columnas, cabeceras, unidades y entidad comparada.
- Filtros con etiquetas, valores y contexto de la categoría.
- Datos de producto, variantes y condiciones comerciales con identidades y correspondencias.
- Enlaces entre recursos que establecen continuidad explicativa, comparativa o de compatibilidad.
- Datos estructurados disponibles, como JSON-LD, **como representaciones complementarias**, no como verdad de referencia.
- Anotaciones o advertencias de alcance, uso, compatibilidad y limitaciones.

No se utilizará una única conversión a texto plano si destruye relaciones. Para contenido editorial puede emplearse una extracción de texto principal adicional, **sin reemplazar** el DOM o el contexto de tablas, navegación y filtros.

### 5.4. Contenido dinámico e interacción selectiva

Si un bloque comercial de interés no figura en la respuesta inicial, podrá utilizarse un navegador automatizado (por ejemplo, Playwright) para obtener el DOM renderizado y, cuando resulte pertinente, abrir desplegables, selectores o comparadores. Se registra qué acciones se realizaron y qué estado del recurso quedó observado.

El renderizado se empleará **selectivamente** para evitar coste y complejidad innecesarios. La presencia de JavaScript, por sí misma, no debe confundirse con una limitación metodológica ni con un incumplimiento técnico del ecommerce.

No se eludirán autenticaciones, controles de acceso, bloqueos ni medidas anti-bot. El rastreo respetará las políticas aplicables, las condiciones de uso y límites conservadores de solicitudes; si una fuente no puede inspeccionarse legítimamente, se documentará la limitación y se ajustará la muestra.

### 5.5. Qué se conserva en la capa original

Para cada recurso obtenido se preservan: URL solicitada y final; fecha/hora; ecommerce; clase y perfil; idioma/mercado; método de obtención; código/estado relevante; contenido original o referencia a la instantánea; DOM renderizado cuando exista; acciones de interacción; versión o huella del recurso; restricciones de lectura y errores; y enlaces con otras capturas.

Se distinguen **fuente no recuperada**, **fuente recuperada sin determinado contenido**, **contenido no inspeccionado** y **contenido inspeccionado donde no se halló una señal**. Ninguna de estas situaciones equivale automáticamente a que la necesidad informativa sea irrelevante.

### 5.6. Exploración abierta y dirigida

Se aplican dos recorridos complementarios:

- **Exploración abierta:** localizar señales y relaciones sin exigir coincidencia con los atributos taxonómicos existentes. Es esencial para descubrir cuestiones imprevistas.
- **Exploración dirigida:** utilizar dimensiones, clases, facetas y dudas ya identificadas para comprobar cobertura, matices, equivalencias y ausencias aparentes.

Si aparecen recursos o estructuras no previstos, se registra la incidencia, se amplía el perfil de extracción y se reexploran muestras comparables para evitar sesgos por cambios de procedimiento.

---

## 6. Corpus estructurado: unidad mínima y reglas de segmentación

La unidad mínima recomendada es la **unidad de contenido estructurada y contextualizada**, identificada mediante un ID propio y un localizador reproducible en el recurso original.

No se fija un tamaño textual universal: debe conservarse la **menor unidad que mantenga íntegra la relación informativa que se pretende analizar**. Puede ser una pregunta con su respuesta, una fila con su cabecera de tabla, un filtro con sus opciones o un párrafo junto a sus condiciones de uso.

### 6.1. Reglas

1. Preservar **literalidad** o la representación estructural del contenido original, sin convertir interpretaciones en citas.
2. Mantener el **contexto inmediato** necesario: sección, categoría, productos, variantes, unidades, mercado y condiciones.
3. Conservar las **relaciones entre elementos**; una tabla de compatibilidades no se descompone en valores desvinculados.
4. Admitir unidades compuestas y vínculos entre unidades cuando una relación necesite más de un bloque.
5. Evitar duplicar como evidencias independientes copias idénticas del mismo contenido o plantilla.
6. Registrar el **origen editorial o de terceros** cuando pueda distinguirse.
7. No descartar información por no coincidir con atributos conocidos o códigos semánticos previstos.

### 6.2. Campos mínimos de una unidad de evidencia

| Grupo | Campos operativos |
|---|---|
| Identificación | `content_unit_id`, `snapshot_id`, `reference_site_id`, `product_class_id`, versión. |
| Localización | URL, tipo de recurso, sección, selector o localizador, orden relativo dentro del recurso. |
| Contenido | Texto literal o estructura preservada (tabla, filtros, pregunta-respuesta, relación), idioma. |
| Contexto | Entidades y vínculos identificables, unidades, alcance de producto/variante/oferta, mercado y momento cuando consten. |
| Captura | Método de recuperación, estado de renderizado, interacción realizada, momento, incidencias. |
| Procedencia | Autoría editorial/tercero si es reconocible, dependencia o duplicación respecto de otra fuente. |
| Control | Estado de extracción, comprobación de integridad, referencia a original y limitaciones. |

Los campos de interpretación (cuestión sugerida, práctica, pertinencia o grado de confianza) se almacenan **en otra capa**, referidos a la unidad original por su ID.

---

## 7. Clasificación inicial de señales informativas

La siguiente tipología dirige la **observación**, no clasifica automáticamente los futuros requisitos ni define criterios de calidad. Es una taxonomía **abierta y versionable** de señales: un mismo bloque puede recibir varias etiquetas.

| Código orientativo | Tipo de señal | Pregunta de extracción |
|---|---|---|
| `SI-01` | **Cuestión explícita** | ¿Qué pregunta de compra o duda se formula o responde? |
| `SI-02` | **Criterio de selección** | ¿Qué dimensión se utiliza para filtrar, segmentar o elegir? |
| `SI-03` | **Criterio de comparación** | ¿Qué se contrasta entre alternativas, con qué base y para qué decisión? |
| `SI-04` | **Necesidad o contexto de uso** | ¿Qué actividad, problema, condición o situación da significado a la información? |
| `SI-05` | **Relación o compromiso funcional** | ¿Qué vínculo entre características, prestaciones o limitaciones se explica? |
| `SI-06` | **Adecuación o compatibilidad** | ¿Qué correspondencia entre producto, uso, sistema o condición de aplicación se informa? |
| `SI-07` | **Restricción o advertencia** | ¿Qué incompatibilidad, límite o condición excluyente se expresa? |
| `SI-08` | **Cuestión comercial precompra** | ¿Qué aspecto de variantes, precio, disponibilidad, entrega, garantía o devolución se explica para decidir? |

Los **atributos, afirmaciones, valores y relaciones** de producto se capturan aunque no constituyan por sí solos una señal diferencial. Pueden dar soporte a varias señales y a posibles requisitos; el objetivo del MPIR no es duplicar indiscriminadamente el diccionario taxonómico.

---

## 8. Identificación de prácticas: análisis semántico separado

### 8.1. Preguntas obligatorias de interpretación

Para cada unidad o conjunto relacionado de unidades se revisa:

1. **Qué se observa:** ¿qué contenido, estructura o mecanismo ha publicado el ecommerce, sin añadir hechos?
2. **Qué función cumple:** ¿describe, identifica, explica, relaciona, contextualiza, compara, recomienda, advierte o sustenta algo?
3. **Qué cuestión podría revelar:** ¿qué conocimiento del producto u oferta parece querer facilitar al comprador?
4. **Sobre qué objeto y condiciones:** ¿producto, variante, oferta, vendedor, uso, mercado, situación o momento?
5. **Cuál es el fundamento:** ¿qué fragmentos y relaciones justifican la interpretación?
6. **Qué no puede afirmarse:** ¿qué parte permanece ambigua, es puramente promocional o requeriría supuestos externos?

La **proximidad temática no basta** para inferir una necesidad. Una frase genérica sobre «aventura» no prueba una cuestión técnica concreta si no establece una relación informativa identificable.

### 8.2. Uso de IA

Se recomienda utilizar un LLM para **proponer anotaciones estructuradas**, no para declarar unilateralmente prácticas definitivas. El analizador recibe bloques con contexto e IDs y devuelve:

- señal o señales candidatas y su función informativa;
- práctica observada formulada neutralmente;
- cuestión o cuestiones candidatas de demanda;
- entidades, alcance, aplicabilidad o condiciones sugeridos;
- citas/localizadores de soporte;
- incertidumbres, relaciones pendientes y motivos de exclusión;
- estado de revisión.

Cada salida debe ser trazable a unidades del corpus. **No se aceptan citas inventadas, atribuciones no publicadas, identidades supuestas ni preguntas inferidas solo por conocimiento externo del modelo.** Las inferencias pueden apoyarse en varias unidades enlazadas; deben explicitar las relaciones utilizadas.

### 8.3. Estados de las anotaciones

- **Candidata:** interpretación plausible pendiente de contraste o revisión.
- **Sustentada:** la función informativa está apoyada por evidencia identificable y el alcance está suficientemente delimitado.
- **Pendiente por contexto:** faltan recursos, identidades o relaciones para aceptar o descartar la interpretación.
- **Descartada:** la inferencia no queda justificada, es ajena al alcance o era duplicado mal atribuido.

Estos estados controlan **la investigación del MPIR**. No son GSC, IR, ICI, indicadores técnicos ni clases de importancia de un RI.

### 8.4. Revisión humana y consistencia

La revisión debe concentrarse en casos nuevos, fronterizos, conflictivos, potencialmente críticos para la clase y en una muestra de anotaciones rutinarias. En el piloto se comparan las anotaciones automáticas con una lectura humana de recursos seleccionados y se registran **omisiones, sobreinferencias, pérdidas de contexto y desacuerdos de clasificación**. Las reglas o instrucciones del analizador se versionan; su actualización permite reprocesar el mismo corpus.

---

## 9. Consolidación interfuente: de señales a patrones

La consolidación agrupa señales por su **significado funcional**, no por igualdad literal de términos o formatos. Por ejemplo, un filtro por terreno, una guía sobre superficies húmedas y una comparación de suelas pueden apuntar a una misma necesidad de evaluar el agarre según condiciones de uso, aunque tengan formas distintas.

### 9.1. Procedimiento

1. Agrupar señales candidatas por clase, dimensión, objeto y función, conservando agrupaciones cruzadas cuando proceda.
2. Proponer una descripción canónica de la práctica o patrón, sin eliminar matices que alteren la cuestión.
3. Comparar **alcance, condiciones, entidades, segmentación y fundamento**; separar patrones solo cuando la diferencia sea informativamente sustantiva.
4. Asociar todas las evidencias y fuentes de apoyo; registrar replicaciones editoriales para no inflar el contraste entre comercios.
5. Conservar variantes, excepciones y conflictos, sin fabricar consenso donde las referencias discrepan.
6. Marcar los patrones que proponen **nuevas facetas o subclases** para revisión en el Modelo de Taxonomía de Productos.

Un patrón puede estar sustentado en **una única fuente especializada** si su función resulta justificable. La recurrencia refuerza la observación de uso comercial, pero **no constituye una regla de aceptación, relevancia o criticidad**.

### 9.2. Campos de un patrón MPIR

- ID y versión de patrón.
- Denominación y formulación neutral de la práctica informativa.
- Clase(s), faceta(s), segmentos, entidades y condiciones a las que se refiere.
- Función para la comprensión, comparación o evaluación comercial.
- Relación con otros patrones: equivalente, más general, más específico, complementario, condicionado o en conflicto.
- Lista de señales y unidades de evidencia que lo sustentan.
- Ecommerce y recursos representados; procedencia editorial y posibles dependencias.
- Variantes y contraejemplos; incertidumbres y límites interpretativos.
- Cuestiones informativas candidatas que podría fundamentar.
- Estado de revisión y trazabilidad de cambios.

---

## 10. Contraste con taxonomías y transferencia al modelo de demanda

El MPIR no aprueba directamente requisitos. Ofrece **patrones, observaciones y cuestiones candidatas** que se contrastan con el inventario taxonómico y con los requisitos que se estén desarrollando para la clase.

### 10.1. Tipos de aportación

| Resultado del contraste | Interpretación | Tratamiento |
|---|---|---|
| **Confirmación** | La práctica observada aporta evidencia sobre una cuestión ya inferida mediante la taxonomía. | Vincular la evidencia sin crear un RI duplicado. |
| **Ampliación** | Aparece una cuestión relevante no reconocida suficientemente en las fuentes taxonómicas. | Formular nueva cuestión candidata y justificar su pertinencia. |
| **Profundización** | Se descubre contexto, relación, desagregación o condición necesaria para formular mejor una cuestión conocida. | Revisar formulación, núcleo de conocimiento o alcance del RI candidato. |
| **Diferenciación** | La necesidad cambia para una subclase, faceta, uso o circunstancia. | Valorar requisito específico, condicionado o revisión de clase; no crear subclase automáticamente. |
| **Tensión o discrepancia** | Distintas prácticas muestran enfoques incompatibles o fronteras dudosas. | Conservar perspectivas, investigar condiciones y evitar síntesis artificial. |

### 10.2. Filtro de transferencia

Antes de trasladar una cuestión al catálogo de demanda, comprobar:

1. **Necesidad de conocimiento:** ¿se formula qué debe poder determinarse sobre una oferta, no simplemente qué campo aparece o qué consejo recibe una persona?
2. **Relevancia para la clase:** ¿poder responderla desempeña un papel justificable en la comprensión, comparación o evaluación general de esa clase?
3. **Objeto y alcance:** ¿se identifica la entidad, relación, desagregación y condiciones de aplicación?
4. **Generalización prudente:** ¿la pregunta trasciende la redacción o estrategia de un comercio, sin perder diferencias relevantes?
5. **Solapamiento y fragmentación:** ¿ya existe otra pregunta equivalente o conviene separar/componer requisitos?
6. **Fundamento:** ¿qué observaciones del MPIR y/o de la taxonomía sustentan la inclusión y qué incertidumbres quedan?

La clasificación final como **crítico, principal o complementario** se realiza **en el modelo de demanda**, por el papel de poder resolver la cuestión para la clase, **no** por el número de ecommerce que la mencionan. Las interfaces pertinentes (Catálogos distribuidos, Web y Web Schema.org) se relacionan con los RI en la fase correspondiente, de acuerdo con la función de cada ámbito.

---

## 11. Cobertura, calidad del proceso y condición de cierre

La sistematicidad del MPIR depende de poder explicar **qué se observó, qué quedó fuera y por qué se considera suficiente el trabajo efectuado para su finalidad exploratoria**.

### 11.1. Tres controles de cobertura

- **Cobertura de referentes y recursos:** proporción y diversidad efectiva de comercios, segmentos, productos y tipos de recurso inspeccionados respecto de la muestra planificada.
- **Cobertura temática:** dimensiones conocidas de la taxonomía examinadas, relaciones nuevas observadas, temas sin evidencia y exploración abierta no restringida al vocabulario inicial.
- **Cobertura del procesamiento:** recursos recuperados, bloques extraídos, fallos de parseo, contenido dinámico pendiente, señales sin revisar y relaciones no resueltas.

Un resultado negativo exige precisar **el perímetro inspeccionado**: «no identificado en la muestra y perfiles examinados» no equivale a «no lo demanda el mercado».

### 11.2. Saturación cualitativa

En ciclos sucesivos se observa si nuevos ecommerce y recursos aportan **patrones sustantivamente diferentes**, nuevas condiciones o casos fronterizos, o si principalmente replican lo ya identificado. La saturación se examina **por clase y segmento** y se documenta junto con la diversidad de fuentes y las limitaciones.

No se adopta por ahora un porcentaje universal, número fijo de páginas ni umbral de saturación: deberán calibrarse con el piloto para evitar falsa precisión.

### 11.3. Condición de cierre de una iteración

Puede cerrarse una iteración cuando:

- la muestra y sus desviaciones están documentadas;
- las capturas y unidades estructuradas pertinentes son recuperables y revisables;
- las señales de mayor interés, novedosas o fronterizas han recibido revisión adecuada;
- se han consolidado patrones sin duplicidades significativas no justificadas;
- las cuestiones candidatas y las relaciones con taxonomía quedan trazadas;
- están explicitados los vacíos, recursos inaccesibles y límites de generalización.

El cierre significa **suficiencia operativa de la iteración**, no demostración de cobertura exhaustiva de la demanda.

---

## 12. Ciclo operativo de ejecución

La ejecución es **incremental**, pero conserva una separación lógica y persistente entre captura y análisis:

| Etapa | Operación | Producto / control |
|---|---|---|
| **0. Preparación** | Fijar clase, alcance, taxonomía de referencia, segmentos, panel y matriz de cobertura. | Plan de observación versionado. |
| **1. Descubrimiento** | Inventariar recursos relevantes por ecommerce y perfil. | Lista de recursos candidatos, motivos y cobertura. |
| **2. Captura** | Recuperar y preservar recursos, con renderizado selectivo si procede. | Corpus original versionado. |
| **3. Estructuración** | Segmentar bloques y conservar entidades, tablas, filtros, relaciones y contexto. | Corpus estructurado de unidades informativas. |
| **4. Anotación** | Detectar señales y proponer prácticas/cuestionamientos mediante reglas y análisis semántico. | Anotaciones candidatas ligadas a evidencias. |
| **5. Revisión** | Comprobar interpretaciones y corregir omisiones, sobreinferencias o atribuciones. | Anotaciones sustentadas o descartadas. |
| **6. Consolidación** | Normalizar prácticas y patrones entre referentes. | Versión del MPIR para la clase. |
| **7. Contraste** | Comparar con taxonomías y trasladar cuestiones candidatas justificadas. | Matriz de aportaciones al modelo de demanda. |
| **8. Iteración** | Ampliar muestra, corregir extractores y reprocesar corpus cuando sea necesario. | Nueva versión trazable y análisis de cobertura. |

**Regla de operación:** el análisis puede comenzar tras un primer lote razonable, antes de completar todo el panel. Si revela contenidos omitidos, se ajusta la extracción; las versiones previas de las fuentes permanecen conservadas. **No se generan «prácticas definitivas» en el mismo acto de descargar una página.**

---

## 13. Modelo lógico de datos y trazabilidad

El diseño lógico mínimo separa entidades para que una fuente sustente varios patrones, un patrón reúna múltiples evidencias y una evidencia pueda apoyar distintas cuestiones sin copiarse artificialmente.

| Entidad lógica | Campos clave o relaciones |
|---|---|
| `reference_site` | ID, dominio, tipo de ecommerce, mercado, especialización, justificación de selección, grupo editorial. |
| `observation_plan` | Clase interna/versionada, segmentos, perfiles, periodo, panel, criterios de muestra. |
| `resource_snapshot` | ID, ecommerce, URL, tipo, captura, versión/huella, método, estado, instantánea preservada. |
| `content_unit` | ID, instantánea, localizador, estructura original, contexto, entidades, relaciones, procedencia. |
| `informative_signal` | ID, unidad(es), código(s) SI, interpretación, función, soporte y estado. |
| `reference_practice` | ID, descripción neutral, señales, función y alcance, estado de revisión. |
| `practice_pattern` | ID canónico, prácticas/evidencias, clases, variantes, relaciones, conflictos y versión. |
| `demand_question_candidate` | ID, pregunta candidata, patrón(es), objeto y condiciones, justificación, estado de transferencia. |
| `taxonomy_alignment` | Cuestión/patrón, clase/faceta/atributo taxonómico, tipo de aportación, fundamento. |
| `review_log` | Revisor o procedimiento, fecha, decisión, cambios, incertidumbres y soporte. |

**Integración recomendada:** reutilizar los IDs de clases de producto y las correspondencias del modelo taxonómico [M4]; no crear una segunda clasificación de productos desconectada. Los IDs de prácticas y patrones serán internos y estables, con versiones explícitas cuando cambie su significado.

---

## 14. Ejemplo ilustrativo completo

**Clase:** botas de senderismo. **Caso hipotético**, no evidencia real de ecommerce concreto.

### Observaciones en el corpus

| Fuente hipotética | Unidad de contenido conservada | Tipo de recurso |
|---|---|---|
| Ecommerce A | Filtro «Tipo de terreno» con opciones diferenciadas. | Categoría / filtros. |
| Ecommerce B | Guía que relaciona el diseño de la suela con roca húmeda y barro. | Guía de compra. |
| Ecommerce C | Tabla que compara agarre en distintas superficies para varios modelos. | Comparador. |

Cada observación conserva URL, localizador, fecha, texto o estructura exacta y correspondencias entre producto y dato.

### Interpretación y consolidación

- **Señales:** criterio de selección (`SI-02`), contexto de uso (`SI-04`), relación funcional (`SI-05`) y comparación (`SI-03`).
- **Prácticas observadas:** segmentar por terreno; explicar adecuación del agarre a superficies; comparar alternativas bajo condiciones de uso.
- **Patrón normalizado:** utilización del **tipo y estado del terreno** para orientar la evaluación del agarre de las botas.
- **Cuestión informativa candidata:** «¿Para qué tipos de superficie y condiciones de terreno está diseñado el agarre del calzado?».
- **Aportación frente a taxonomía:** posible **profundización** de características de suela o agarre, al incorporar un alcance funcional y condiciones de aplicación que pueden no estar expresados en los atributos.

La pregunta se traslada al proceso de construcción de demanda para decidir **pertinencia, objeto, alcance, aplicabilidad, posible solapamiento e importancia relativa**. Ni la repetición de tres señales ni su presencia en comparadores prueba que la cuestión sea crítica. Tampoco se concluye que un modelo determinado sea adecuado para roca húmeda: eso exigiría información sobre esa oferta concreta.

---

## 15. Validación piloto y parámetros que deben calibrarse

Se recomienda comenzar con **una clase acotada**, alineada con el piloto taxonómico de **calzado > botas**, seleccionando subsegmentos informativamente diferenciados. La prueba debe incluir recursos de tipos distintos y ecommerce con perspectivas editoriales diversas.

### 15.1. Preguntas de validación del piloto

1. ¿El sistema captura correctamente las estructuras informativas relevantes (FAQ, filtros, tablas y relaciones), no solo texto editorial?
2. ¿Aparecen cuestiones que no podíamos inferir suficientemente a partir de las taxonomías?
3. ¿Podemos distinguir observaciones, interpretación y pregunta inferida sin perder trazabilidad?
4. ¿Las anotaciones automáticas reproducen razonablemente la revisión humana o producen omisiones y asociaciones temáticas injustificadas?
5. ¿Qué parte del corpus permite identificar patrones nuevos, profundizaciones o diferencias de aplicabilidad?
6. ¿Cómo cambia el rendimiento de descubrimiento al incorporar nuevos ecommerce y perfiles de recursos?
7. ¿Qué cambios de clase, faceta o requisito candidato surgen de la evidencia y cuáles eran meras diferencias editoriales?

### 15.2. Parámetros abiertos, sin alterar el método adoptado

- Tamaño y combinación concreta del panel de ecommerce por tipo de clase.
- Número de páginas y productos por perfil y segmento.
- Umbrales o reglas prácticas de suficiencia de cobertura y saturación.
- Campos finales obligatorios/opcionales y almacenamiento físico de recursos.
- Herramientas y selectores por plataforma, navegador y configuración de captura.
- Taxonomía fina de funciones o señales tras resolver casos fronterizos.
- Proporción y procedimiento de revisión humana, medición de errores y tratamiento de discrepancias.
- Política de actualización periódica y antigüedad tolerada de las evidencias.

Estos aspectos requieren **calibración operativa**; no se presentan como acuerdos cerrados en la documentación de partida.

---

## 16. Riesgos metodológicos y medidas de control

| Riesgo | Medida preventiva |
|---|---|
| Confundir lo que publica un referente con lo que demanda el mercado. | Formular resultados como evidencia indirecta, con límites de generalización. |
| Seleccionar solo ecommerce con contenidos abundantes o plantillas semejantes. | Diversificar perfiles, segmentos e independencia editorial; documentar sesgos. |
| Extraer solo atributos conocidos. | Combinar exploración abierta y dirigida; preservar bloques no previstos. |
| Transformar páginas directamente en requisitos o prácticas definitivas. | Separar corpus, anotaciones, patrones y transferencia al modelo de demanda. |
| Perder contexto al limpiar HTML o convertir tablas en texto. | Preservar DOM, cabeceras, relaciones, entidades y localizadores. |
| Sobreinferir con IA o asumir conocimiento externo. | Exigir evidencia enlazada, revisión de casos inciertos y reglas versionadas. |
| Duplicar señales reproducidas de un mismo fabricante. | Registrar procedencia editorial y dependencias; consolidar sin inflar apoyo. |
| Confundir ausencia de captura con ausencia de práctica. | Registrar cobertura, errores, recursos no inspeccionados y límites de acceso. |
| Asignar criticidad por frecuencia o prominencia. | Evaluar importancia únicamente en el modelo de demanda y por su relevancia para la clase. |
| Tratar contenido de referencia como evidencia de oferta auditada. | Mantener separación entre fuentes de construcción de demanda e interfaces de evaluación. |
| Automatización sin permisos o con rastreo intrusivo. | Respetar condiciones aplicables, no eludir controles y limitar la tasa de acceso. |

---

## 17. Entregables y criterio de aceptación del MPIR

**Entregables de una iteración por clase:**

1. **Plan de observación:** definición de clase y muestra, panel de ecommerce, perfiles y cobertura prevista.
2. **Corpus de Evidencias Comerciales de Referencia:** instantáneas originales, metadatos, bloqueos y limitaciones.
3. **Corpus estructurado:** unidades contextualizadas, relaciones y trazabilidad a originales.
4. **Registro semántico:** señales, prácticas candidatas, fundamentos, incertidumbres y estados de revisión.
5. **MPIR consolidado:** catálogo versionado de patrones informativos por clase, con evidencias y variantes.
6. **Matriz de contraste taxonomía–MPIR:** confirmaciones, ampliaciones, profundizaciones, diferenciaciones y tensiones.
7. **Propuesta de transferencia:** cuestiones informativas candidatas con su justificación, para evaluación en el modelo de demanda.
8. **Informe de cobertura y limitaciones:** qué se examinó, qué no pudo examinarse y qué decisiones quedan abiertas.

La iteración es metodológicamente aceptable cuando sus observaciones importantes son **reexaminables**, sus interpretaciones son **rastreables a evidencia**, las prácticas están **normalizadas sin borrar diferencias sustantivas** y la transferencia al modelo de demanda distingue **hipótesis de cuestiones** de **requisitos aprobados**.

## 18. Conclusión metodológica

El MPIR constituye la **segunda base de referencia** para la construcción sistemática del modelo de demanda, paralela y complementaria al Modelo de Taxonomía de Productos. Su contribución diferencial es revelar **cómo los ecommerce especializados y referentes transforman características, relaciones, contextos y condiciones comerciales en información destinada a apoyar decisiones de compra**.

Se adopta una secuencia **captura original → corpus estructurado → interpretación semántica → consolidación de prácticas → contraste con taxonomía → inferencia justificada de requisitos**, ejecutable por lotes y con retroalimentación controlada. **No** se generan prácticas definitivas mientras se realiza el scraping ni se prescinde del original una vez interpretado.

El éxito del método no se mide por el volumen de HTML acumulado ni por la cantidad de requisitos sugeridos, sino por **la capacidad de descubrir aportaciones informativas diferenciales, justificar su significado y alcance, y reconstruir cada inferencia desde fuentes comerciales concretas**.

---

## Referencias documentales internas

- **[M1]** *Contexto y marco del estudio* (`Contexto_marco_de_estudio.md`). Objeto, alcance, funciones de información comercial y separación entre calidad técnica e informativa.
- **[M2]** *Conceptos base del sistema de estudio* (`Conceptos_base_sistema_de_estudio.md`). Definición del modelo de demanda y requisitos informativos; fuentes de inferencia; importancia relativa; ámbitos de evaluación.
- **[M3]** *Fundamentos consolidados del sistema de estudio y auditoría de la calidad de la información comercial* (`Fundamentos_consolidados_calidad_de_la_informacion_comercial.md`, 24 de octubre de 2026). Desarrollo interpretativo, pertinencia, trazabilidad y límites metodológicos.
- **[M4]** *Marco metodológico para construir la taxonomía de clases de producto* (`Marco_metodologico_taxonomia_modelos_demanda(1).md`, 24 de octubre de 2026). Integración de Shopify, Amazon y Google, definición de clases internas y relación con el modelo de demanda.

**Nota de procedencia:** los conceptos rectores y la relación entre taxonomías, ecommerce referentes y modelo de demanda se fundamentan en [M1–M4]. El nombre **MPIR**, la separación en corpus y capas, la tipología `SI-01`–`SI-08`, los registros propuestos y el procedimiento de scraping/consolidación son **decisiones de diseño metodológico desarrolladas en esta sesión** y deberán verificarse operativamente en el piloto. No se ha realizado una extracción real ni se atribuyen a ecommerce concretos los ejemplos ilustrativos.
