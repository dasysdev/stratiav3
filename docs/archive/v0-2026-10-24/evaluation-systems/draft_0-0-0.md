# Marco metodológico operativo general para la valoración GSC de los criterios de aceptación

**Proyecto:** Calidad de información v1  
**Versión del documento:** 0.1 — propuesta operativa integral para pilotaje  
**Fecha:** 24 de octubre de 2026  
**Finalidad:** especificar un procedimiento general y reutilizable para que un agente auditor examine información comercial, identifique información pertinente para un requisito informativo (RI), obtenga evidencias y emita el grado de satisfacción de cada criterio de aceptación (GSC).  
**Aplicación:** cualquier modelo de demanda construido conforme a los fundamentos del proyecto y los ámbitos **Catálogos distribuidos**, **Web** y **Web Schema.org**, con sus perfiles de consumo admitidos.

> **Estado documental.** Este documento es una **propuesta operativa completa para una primera ejecución controlada**. Consolida los principios acordados y desarrolla las reglas prácticas que todavía faltaban, pero **no presenta los nuevos anclajes, umbrales de suficiencia ni protocolos como empíricamente validados**. Antes de considerarlos definitivos deberán probarse y aprobarse mediante casos de calibración. No modifica el marco conceptual ni añade criterios, propiedades, escalas o indicadores de calidad.

> **Precedencia.** En caso de discrepancia prevalecen `Contexto_marco_de_estudio.md` y `Conceptos_base_sistema_de_estudio.md`. `Fundamentos_consolidados_calidad_de_la_informacion_comercial.md` recoge el desarrollo contextual y metodológico vigente. Son antecedentes complementarios `Fundamento_metodologico_IA_y_calidad_informativa.md` y `Estrategia_metodologica_RI_localizacion_pertinencia_evidencias_GSC.md`.

## Índice

1. Propósito, límites y principios
2. Arquitectura de ejecución y responsabilidades
3. Contratos de entrada y de salida
4. Estructuración operativa universal del RI
5. Exploración y localización del contenido
6. Determinación de pertinencia funcional
7. Delimitación y tratamiento del conjunto pertinente
8. Disponibilidad efectiva y cobertura
9. Protocolo transversal de evidencias
10. Comprobación operativa de propiedades P06–P18
11. Guías generales de los seis criterios de aceptación
12. Decisión de GSC, NA, NE y control de materialidad
13. Procedimiento integral de ejecución
14. Esquema de registros y salida para informe
15. Casos de aplicación y calibración
16. Controles de calidad y resolución de incidencias
17. Prueba de aceptación de la V1
18. Límites de generalización y decisiones pendientes
19. Matriz de cobertura de acuerdos y pendientes
20. Anexos: plantillas, reglas resumidas y glosario

---

## 1. Propósito, límites y principios

### 1.1. Pregunta operativa

Para una **unidad evaluada** —RI, ámbito y entidad/oferta concretos, con su alcance y condiciones—, el procedimiento debe permitir responder:

**¿Qué información comercial pertinente puede obtenerse y leerse; qué evidencia demuestra sus propiedades relevantes; y qué GSC corresponde a cada AC a partir de esas comprobaciones?**

La auditoría evalúa **las condiciones informativas ofrecidas por el ecommerce** para determinar y fundamentar cuestiones de compra. No mide la actuación, el esfuerzo computacional o el éxito de un modelo particular de IA. Una deficiencia no prueba que ningún agente pueda resolver la cuestión por otros medios, y una valoración suficiente tampoco garantiza éxito universal.

### 1.2. Invariantes del modelo — definiciones vigentes

- La unidad básica de evaluación informativa es **RI × ámbito pertinente**, aplicada a la entidad, oferta, recurso y condiciones concretas de la inspección.
- La **disponibilidad efectiva** es previa a la evaluación de AC: **0** si no existe información pertinente obtenible y legible según el perfil; **1** si existe al menos un elemento pertinente efectivamente utilizable. Si vale **0**, **IR = 0** y **no se valoran los AC**.
- Los AC son **Concreción, Precisión, Aplicabilidad, Comparabilidad, Fiabilidad y Justificación**.
- La escala de GSC es **0 — No**, **1 — Parcialmente**, **2 — Sí, es suficiente**. Los estados **NA** y **NE** no son puntuaciones.
- Las propiedades P06–P18 **fundamentan los juicios** y pueden relacionarse con varios AC; **no reciben subpuntuaciones que se sumen o promedien**.
- El análisis informativo no sustituye la evaluación de **requisitos técnicos generales**; la condición técnica directamente examinada aquí es la obtención y legibilidad efectiva de información pertinente para el RI.
- **Web** comprende la información comercial del recurso web, incluidos HTML y Schema.org; **Web Schema.org** considera únicamente el marcado; **Catálogos distribuidos** considera el catálogo o feed bajo el perfil evaluado. Web y Web Schema.org se informan por separado sin agregación automática.
- La modalidad de consumo es **sin navegación interactiva**, bajo un perfil documentado; esto no establece una prohibición universal de JavaScript desvinculada del perfil.
- Las derivaciones sustentadas son admisibles; no se puntúa su número o grado. La capacidad de inferencia del agente no completa como hechos publicados las carencias del ecommerce.

### 1.3. Principios transversales de ejecución — propuesta V1

**M01 · Fidelidad al RI.** No cambiar la cuestión, el conjunto de entidades, la desagregación ni sus condiciones durante la auditoría. Toda aclaración necesaria debe registrarse y, cuando modifique su significado, tramitarse como revisión del perfil de RI.

**M02 · Neutralidad de respuesta.** Poder responder fundamentadamente «no», «no cumple», «no disponible» o «incompatible» puede satisfacer una cuestión. No confundir la carencia de una característica con la carencia de información sobre ella.

**M03 · Pertinencia funcional.** Incluir contenido por su contribución identificable a la necesidad del RI, no por simple proximidad temática.

**M04 · Cobertura proporcionada.** Explorar lo suficiente para la conclusión que se quiere emitir; exigir más cobertura al afirmar ausencia que al acreditar presencia.

**M05 · Evidencia anterior al juicio.** No asignar el GSC y después buscar ejemplos favorables. Conservar lo observado, evaluar su relevancia y solo entonces decidir.

**M06 · Separación de planos.** Distinguir siempre recurso observado, afirmación comercial, relación sustentada, interpretación del auditor, hallazgo, propiedad afectada y consecuencia para el AC.

**M07 · Suficiencia relativa.** «Suficiente» se determina respecto del contenido y alcance del RI, no respecto de una perfección universal ni de la cantidad total de atributos publicados.

**M08 · Razonamiento justificado.** Admitir reconocimiento semántico, conversiones y derivaciones sustentadas; rechazar conjeturas que suplan estados, entidades, identidades o condiciones comerciales ausentes.

**M09 · No compensación encubierta.** No dar por satisfecho un AC mediante el buen resultado de otro ni sustituir la valoración específica de cada uno por una impresión global.

**M10 · Reexaminabilidad.** La evaluación debe permitir que otro auditor localice la base probatoria, reconstruya las relaciones relevantes y comprenda por qué se adoptó la decisión.

**M11 · Incertidumbre explícita.** No convertir una búsqueda incompleta o una comprobación inconclusa en una ausencia acreditada, una falsedad o un GSC negativo.

**M12 · Portabilidad.** Las reglas se aplican a cualquier modelo de demanda del proyecto. Solo la **necesidad concreta del RI**, el **perfil de interfaz**, los **hechos observados** y la **materialidad de los hallazgos** cambian entre casos.

### 1.4. Lo que no hace este marco

No construye automáticamente el catálogo de demanda, no determina prioridades o pesos de requisitos, no especifica el sistema de auditoría técnica, no calcula por defecto IR/ICI/TRI, no predice visibilidad, recomendación ni conversión y no impone a toda clase de oferta un inventario idéntico de campos. Estos desarrollos pertenecen a otros niveles del modelo.

## 2. Arquitectura de ejecución y responsabilidades

### 2.1. Capas que no deben confundirse

| Capa | Establece | No debe hacer |
|---|---|---|
| **Fundamentos** | Definiciones, alcance y arquitectura del estudio. | Resolver por sí sola la ejecución de cada inspección. |
| **Modelo de demanda** | RI, dimensión, objeto, alcance, aplicabilidad, importancia e interfaces pertinentes; perfil de resolución/pertinencia. | Definir valores comerciales particulares de un ecommerce. |
| **Perfil de evaluación** | Entidad/oferta, recurso, ámbito, momento, condiciones y vía de consumo admisible. | Cambiar el contenido informativo exigido por el RI. |
| **Marco operativo general** | Procedimientos, reglas y evidencias válidos para cualquier RI. | Imponer atributos específicos de una categoría. |
| **Agente auditor** | Obtención, localización, comprobación, interpretación, registros y GSC. | Completar hechos ausentes con conocimiento propio o redefinir el RI. |
| **Revisión/calibración** | Comprobar consistencia de reglas, coberturas y anclajes. | Sustituir sin trazabilidad la evidencia del caso original. |

### 2.2. Cadena de decisión

`RI y ámbito → perfil operativo del RI → recursos permitidos → exploración → candidatos → pertinencia funcional → conjunto pertinente contextualizado → disponibilidad efectiva → comprobación de propiedades → hallazgos por AC → GSC/NA/NE → validación → expediente e informe`.

**La evidencia atraviesa todas las fases.** La búsqueda puede reabrirse si el análisis de AC descubre una relación, contradicción, ausencia aparente o contexto relevante aún no examinado.

### 2.3. Una cuestión, varias representaciones

Se conserva siempre la procedencia de cada dato o afirmación. Las afirmaciones de HTML y Schema.org pueden complementar una respuesta en **Web** si identidad, condiciones y relaciones son justificables; **Web Schema.org** no puede usar afirmaciones externas al marcado como contenido resolutivo. En **Catálogos distribuidos** se respeta el perfil, alcance, variante/oferta y momento de distribución examinado.

Las referencias externas pueden servir **para contraste o verificación** cuando proceda, pero no para presentar como publicado por el ecommerce un dato que falta en su representación evaluada.

## 3. Contratos de entrada y de salida

### 3.1. Contrato de entrada mínimo

Antes de ejecutar, deben estar disponibles:

| Entrada | Exigencia mínima | Quién la aporta |
|---|---|---|
| **RI identificado** | ID, redacción exacta, dimensión y clase de oferta. | Modelo de demanda. |
| **Objeto y alcance** | Entidad/es interrogadas, desagregación, condiciones y aplicabilidad. | Modelo de demanda; aclaración de auditoría si procede. |
| **Ámbito pertinente** | Catálogos distribuidos, Web o Web Schema.org. | Modelo de demanda. |
| **Perfil informativo del RI** | Núcleo del hecho/relación solicitados y componentes de respuesta; puede elaborarse con el protocolo de §4 si no existe. | Modelo de demanda o fase preparatoria controlada. |
| **Caso evaluado** | Ecommerce, oferta/recurso, identificadores disponibles y momento/mercado relevantes. | Configuración de auditoría. |
| **Perfil de consumo** | Qué vías de obtención/lectura están permitidas y qué recursos se incluyen. | Configuración de ámbito. |
| **Soporte de inspección** | Acceso a recursos o instantáneas realmente obtenidos y posibilidad de guardar evidencias. | Entorno de ejecución. |

La **importancia relativa** del RI puede acompañar al expediente, pero **no altera individualmente un GSC**; pertenece a niveles superiores de análisis.

### 3.2. Regla de validación previa de entradas

- Si falta un dato **inferible sin alterar el significado** (por ejemplo, enumerar los componentes explícitos de un RI bien formulado), crear una **propuesta de descomposición** y señalar su procedencia.
- Si falta una decisión que determina el alcance (por ejemplo, «disponibilidad» sin especificar canal cuando el RI lo requiere), **no elegir silenciosamente** una interpretación. Registrar la ambigüedad; continuar únicamente con las partes inequívocas o solicitar definición del modelo de demanda.
- Si no puede delimitarse la entidad, el ámbito o el perfil de consumo, **no emitir un GSC como si la evaluación estuviera completa**. Registrar bloqueo de preparación o evaluación inconclusa, sin convertirlo en NA ni NE automáticamente.
- Si el RI no es aplicable a la oferta concreta, registrar **NA del RI** con fundamento. Esto es distinto de declarar NA a un AC aislado dentro de un RI aplicable.

### 3.3. Contrato de salida mínimo

Cada caso debe producir: identificación y configuración; perfil RI utilizado; recursos y cobertura; candidatos significativos y decisiones de pertinencia; conjunto pertinente; disponibilidad efectiva o estado procedimental inconcluso; evidencias originales; hallazgos con propiedades; valoración **por cada AC pertinente** (GSC o NA/NE); justificación de cada decisión; limitaciones y controles de validación. La plantilla detallada figura en §14 y anexos.

## 4. Estructuración operativa universal del RI

### 4.1. Objetivo y límite

Transformar un RI, ya definido en el modelo de demanda, en una **especificación informativa reutilizable** que oriente qué buscar y qué constituye una contribución. **No** convertir el RI en una lista cerrada de campos, formatos, expresiones comerciales o respuestas esperadas.

**El modelo de demanda determina la necesidad de conocimiento. El agente de auditoría la aplica a la información que realmente encuentra.**

### 4.2. Campos del perfil operativo

| Campo | Regla general | Exigencia en V1 |
|---|---|---|
| `ri_id`, `pregunta` | Conservar identificación y texto exacto. | Obligatorio. |
| `dimension`, `clase_oferta` | Preservar el marco temático; sin inventar nuevas dimensiones. | Obligatorio si figura en el catálogo. |
| `objeto` | Identificar entidad o conjunto sobre el que se pregunta. | Obligatorio. |
| `hecho_relacion_solicitado` | Expresar qué se debe determinar/fundamentar. | Obligatorio. |
| `componentes_respuesta` | Enumerar conocimientos constitutivos de una respuesta, no campos técnicos. | Obligatorio. |
| `desagregacion` | Definir si se responde por producto, variante, oferta, vendedor, condición o combinación. | Obligatorio cuando lo exige el RI. |
| `alcance` | Delimitar el conjunto y sus fronteras. | Obligatorio. |
| `condiciones` | Mercado, canal, ubicación, tiempo u otras restricciones que modifiquen la respuesta. | Cuando procedan; especificar «no determinada» si es necesario aclarar. |
| `aplicabilidad` | Precisar cuándo corresponde examinar este RI. | Obligatorio. |
| `relaciones_resolutivas` | Describir relaciones lógicas necesarias y posibles composiciones/derivaciones. | Recomendado; obligatorio si la respuesta es relacional. |
| `funciones_informativas` | Identificar cómo un elemento puede describir, identificar, relacionar, contextualizar, sustentar o contrastar. | Obligatorio como referencia de búsqueda, ampliable. |
| `expresiones_ejemplo` | Ejemplos de sinónimos, campos y representaciones. | Opcional, nunca excluyente. |
| `casos_frontera` | Ejemplos de pertinencia parcial, conexión dudosa o proximidad solo temática. | Recomendado para calibración. |
| `ambitos_pertinentes` | Interfaces en las que el RI debe evaluarse. | Obligatorio. |
| `fundamento_perfil` | Justificar inclusiones, límites y decisiones no explícitas en el RI. | Obligatorio cuando hay interpretación. |

### 4.3. Procedimiento de elaboración — reglas RI-01 a RI-09

**RI-01.** Leer literalmente la cuestión; fijar el **hecho o relación solicitados** antes de proponer datos candidatos.

**RI-02.** Identificar **objeto, entidades, granularidad requerida, conjunto, alcance y condiciones**. No equiparar «por variante» a «por modelo».

**RI-03.** Descomponer en el **mínimo conjunto suficiente de necesidades constitutivas**: aquellas sin las cuales no puede interpretarse o fundamentarse la respuesta solicitada. Evitar descomposición en multitud de atributos accesorios.

**RI-04.** Distinguir **componentes sustantivos** de respuesta (hecho o valor solicitado) y **componentes auxiliares** (identificación, vínculo, unidad, marco temporal, condiciones o soporte). Ambos pueden ser pertinentes; no desempeñan la misma función.

**RI-05.** Describir **relaciones necesarias** cuando la cuestión exige atribución, agregación, comparación, conversión o derivación. No imponer que la respuesta exista en una única frase.

**RI-06.** Admitir **representaciones alternativas** si aportan la misma contribución justificable; no condicionar pertinencia a coincidencias de etiquetas ni a un vocabulario único.

**RI-07.** Incorporar ejemplos positivos, parciales y negativos **solo como ayudas de interpretación**; nunca como enumeración exhaustiva.

**RI-08.** Separar los casos **no aplicables** de los casos **aplicables pero sin información**. La ausencia de característica no implica ausencia de necesidad de conocimiento si una respuesta negativa puede resolverla.

**RI-09.** Registrar toda hipótesis o ambigüedad que no esté resuelta por la formulación del RI. Si afecta materialmente a la pregunta, remitir a revisión del modelo de demanda antes de emitir valoraciones definitivas.

### 4.4. Prueba de calidad del perfil

Se acepta para exploración si permite a otro auditor: (i) decir qué se pregunta y a quién; (ii) reconocer una contribución parcial; (iii) distinguir información auxiliar de una respuesta; (iv) excluir conexiones meramente temáticas; (v) localizar expresiones alternativas sin alterar el RI. Si falla alguna comprobación, revisar el perfil antes de la búsqueda dirigida.

### 4.5. Ejemplo generalizable — disponibilidad por variante

**RI:** «¿Cuál es la disponibilidad comercial de cada variante del modelo?»

- **Objeto:** variantes comerciales del modelo.
- **Hecho solicitado:** estado de disponibilidad comercial.
- **Desagregación:** cada variante del conjunto pertinente.
- **Componentes sustantivos:** estado de disponibilidad, explícito o legítimamente derivable, para las variantes del alcance.
- **Componentes auxiliares:** identidad de variantes, correspondencias variante–SKU, relación SKU–estado, momento, oferta y canal cuando determinen el significado del estado.
- **Relación:** `variante → estado comercial`; puede expresarse mediante identificadores intermedios sustentados.
- **Ejemplos de contenido parcial:** «modelo disponible»; listado de variantes sin estados.
- **Ejemplos solo temáticos:** popularidad o capacidad de fabricación sin conexión acreditada con la disponibilidad de esas variantes.

La descomposición se reutiliza para distintas tiendas y representaciones; **los valores publicados no forman parte del perfil teórico del RI**.

## 5. Exploración y localización del contenido

### 5.1. Finalidad

Examinar el **contenido obtenible y legible** en el ámbito autorizado para reconocer afirmaciones, datos, entidades, relaciones y contextos que puedan contribuir al RI. La localización es **semántica y funcional**, no una búsqueda de palabras exclusivamente.

### 5.2. Tres modalidades complementarias

1. **Exploración general del recurso.** Obtener y conservar el contenido bajo el perfil admitido. Identificar su organización, entidades, grupos de valores, regiones comerciales, relaciones, formatos y referencias sin interpretar cada frase exhaustivamente.
2. **Exploración dirigida por el RI.** Utilizar el perfil para reconocer hechos, relaciones, unidades, identidades, condiciones y alternativas de expresión vinculados a la cuestión. Recoger elementos candidatos.
3. **Ampliación guiada por hallazgos.** Volver a secciones o representaciones permitidas para resolver referencias, dudas de atribución, aparentes ausencias, conflictos, unidades o condiciones detectadas durante la evaluación.

No se exige una lectura minuciosa de todo el recurso **antes** de iniciar la búsqueda dirigida, pero tampoco se autoriza una exclusión global de contenido no inspeccionado cuando pudiera contener material decisivo.

### 5.3. Reglas operativas L-01 a L-12

**L-01.** Delimitar recurso, ámbito, perfil, instante y condiciones antes de interpretar su contenido.

**L-02.** Guardar o referenciar de modo reexaminable la **representación efectivamente consumida**, no únicamente la página que un navegador interactivo podría mostrar en otras condiciones.

**L-03.** Reconocer entidades y agrupaciones antes de atribuirles afirmaciones. No atribuir automáticamente una propiedad de modelo a todas sus variantes.

**L-04.** Detectar candidatos mediante significado, sinónimos, equivalencias justificadas, unidades, identificadores, relaciones y referencias, no solo coincidencias literales.

**L-05.** Incluir candidatos directos, auxiliares y contextuales; no exigir respuesta completa para examinar un elemento.

**L-06.** Conservar la ubicación y contexto suficientes para separar etiquetas, valores, condiciones, entidades y afirmaciones.

**L-07.** Recorrer relaciones identificables que conduzcan a un componente del RI **siempre que cada conexión pueda justificarse**. No perseguir asociaciones genéricas ilimitadas.

**L-08.** Buscar datos relacionados en representaciones complementarias **solo dentro del ámbito admisible**; documentar cada procedencia.

**L-09.** Ampliar la inspección ante referencias explícitas o candidatos que puedan cambiar una decisión sustantiva y sean verificables con los recursos admitidos.

**L-10.** Documentar qué fuentes, secciones, entidades y componentes se inspeccionaron y qué no pudo examinarse; el registro debe ser proporcionado al juicio.

**L-11.** Una búsqueda textual sin resultados **no demuestra ausencia**. Antes de decidirla, aplicar el protocolo de cobertura del §8.

**L-12.** No mezclar varias capturas temporales como si representaran automáticamente el mismo estado comercial; conservar instante y versión.

### 5.4. Resultado de la exploración

El resultado inicial es un **inventario de candidatos** con localizador, contenido observado, posible función en el RI y relaciones/contextos que requieren comprobación. Debe distinguirse de la selección posterior de información pertinente y de la valoración de calidad.

## 6. Determinación de pertinencia funcional

### 6.1. Distinción rectora

**Relación temática** significa que un contenido guarda alguna asociación con el asunto del RI. **Pertinencia informativa** significa que puede desempeñar una **función identificable y justificable** respecto de una necesidad constitutiva de la cuestión. La primera no basta para acreditar la segunda.

La prueba de pertinencia **no es la valoración del AC**. Un contenido general, incompleto, ambiguo, no desagregado o todavía insuficiente para resolver el RI puede seguir siendo pertinente y servir como base para identificar posteriormente sus limitaciones de calidad.

### 6.2. Prueba obligatoria de pertinencia — PF-01 a PF-03

Para cada candidato, registrar:

1. **PF-01 · Contribución.** ¿Qué componente de respuesta o necesidad constitutiva del RI puede informar, delimitar o sustentar? Señalar el componente concreto del perfil.
2. **PF-02 · Función.** ¿Aporta el hecho; identifica entidad; establece relación; delimita o contextualiza; sirve de sustento o contraste; o cumple otra función razonada? Nombrar y explicar la función, no solo etiquetarla.
3. **PF-03 · Fundamento.** ¿Qué significado observable, afirmación, vínculo expreso, equivalencia admisible o regla interpretativa sostiene esa contribución? Identificar su evidencia y los supuestos que **no** pueden adoptarse.

La clasificación de funciones es **enunciativa, no limitativa**. Toda función adicional debe poder describirse por su contribución concreta y no puede ampliar arbitrariamente el RI.

### 6.3. Estados procedimentales de candidatos — no son puntuaciones

| Estado | Condición | Acción |
|---|---|---|
| **Candidato inicial** | Posible contribución aún no analizada. | Examinar función y fundamento. |
| **Pertinente** | Contribución y función justificables, aunque sean parciales. | Incorporar al conjunto pertinente, con evidencia y contexto. |
| **Pendiente de aclaración** | Hay una conexión posible, pero falta comprobar contexto, identidad o relación. | Ampliar dentro del ámbito; registrar incertidumbre si no puede resolverse. |
| **No pertinente** | No hay función justificable para el RI, o solo existe asociación temática/supuestos. | Excluir de la base del RI; documentar descartes relevantes para cobertura. |

Los elementos descartados **no se consideran deficiencias de calidad**. La selección pertinente tampoco acredita por sí misma suficiencia.

### 6.4. Reglas operativas PF-04 a PF-12

**PF-04.** La contribución puede ser **sustantiva, identificadora, relacional, contextual o probatoria**. No exigir que cada fragmento contenga el valor final de la respuesta.

**PF-05.** La afirmación «producto disponible» puede ser pertinente para una pregunta sobre variantes, aunque no permita atribuir correctamente el estado a cada una.

**PF-06.** El significado general de una expresión puede reconocerse por conocimiento lingüístico o del dominio (por ejemplo, `InStock`), pero las **identidades, relaciones y estados comerciales particulares** requieren sustento en las fuentes admitidas.

**PF-07.** No convertir popularidad, capacidad productiva, plazos logísticos u otros factores indirectos en disponibilidad actual sin relaciones comerciales expresas que justifiquen esa conclusión.

**PF-08.** No imponer límites por **número de relaciones o pasos**: comprobar la justificación de cada conexión y su pertinencia final para el RI. No utilizar una escala de grado de derivación.

**PF-09.** Un dato puede quedar como **candidato pendiente**, no pasar por fuerza a pertinente o excluido cuando existe incertidumbre resoluble o falta evidencia.

**PF-10.** Conservar los elementos que permiten reconstruir una relación pertinente: etiquetas, identificadores, sujeto, predicado, objeto, unidades, restricciones, fecha o versión, cuando correspondan.

**PF-11.** Si una información es pertinente para otro RI pero no para este, no importarla como si satisficiera la cuestión actual. Su eventual reutilización pertenece a otra unidad de evaluación.

**PF-12.** La aparición de un elemento nuevo que puede alterar un hallazgo obliga a revisar la selección previa y a actualizar los registros afectados, dejando constancia de la revisión.

### 6.5. Ejemplo de frontera

**RI:** disponibilidad comercial de cada talla.

| Contenido | Tratamiento inicial | Justificación |
|---|---|---|
| «Talla 42 → SKU-420» | Pertinente, auxiliar/relacional. | Permite reconocer y vincular una variante. |
| «SKU-420: `InStock`» | Pertinente, sustantivo; requiere comprobar identidad, oferta y momento. | Expresa un estado atribuible a un identificador. |
| «Disponible para compra online» (cabecera de modelo) | Pertinente, parcial. | Informa disponibilidad general, sin desagregación acreditada. |
| «Producto muy vendido» | No pertinente por sí solo. | La popularidad no informa el estado comercial actual. |
| «Producción de 10.000 unidades/mes» | No pertinente por sí solo. | Producción no acredita inventario de una variante. |
| «Reposición prevista el lunes» sin identificar talla/canal | Candidato por aclarar. | Puede delimitar un estado futuro, pero no fundamenta directamente uno actual. |
| «Envío gratuito a partir de 60 €» | No pertinente para este RI. | No contribuye al hecho solicitado. |

### 6.6. Cierre de selección y candidatos no resueltos

No es necesario resolver toda la información irrelevante del recurso. Sí deben resolverse o explicitarse los **candidatos plausiblemente decisivos** cuya inclusión pudiera cambiar la disponibilidad efectiva o un juicio material de AC.

Si un candidato decisivo no puede comprobarse, registrar su ubicación y causa. **No afirmar una ausencia global ni un GSC definitivo incompatible con esa incertidumbre.** Si ya existe otro elemento pertinente utilizable, la disponibilidad efectiva puede ser 1 aunque continúe una duda que afecte después a un AC.

## 7. Delimitación y tratamiento del conjunto pertinente

### 7.1. Objeto de trabajo

La base informativa de la evaluación es un **conjunto contextualizado de datos, afirmaciones, entidades, condiciones y relaciones**, no necesariamente una colección de párrafos. Puede estar distribuido en varias partes de una representación admitida.

Cada unidad incluida debe conservar: **contenido literal o valor original, procedencia, localizador, entidad/sujeto, significado que puede atribuírsele, condiciones, instante y vínculos pertinentes**. Los contextos preservados para entender una evidencia no se convierten automáticamente en contenidos que satisfagan otros componentes del RI.

### 7.2. Procedimiento de tratamiento — CT-01 a CT-10

**CT-01 · Normalizar para analizar, no para sustituir.** Pueden prepararse versiones interpretadas de valores, unidades y términos, pero siempre junto al contenido original y la regla usada. La representación transformada no debe reemplazar la evidencia primaria.

**CT-02 · Preservar identidad.** No fusionar producto, variante, oferta y vendedor por similitud de nombres. Utilizar identificadores o relaciones justificadas.

**CT-03 · Preservar alcance.** Asociar cada afirmación con el nivel a que realmente se refiere: modelo, variante, oferta, vendedor, mercado, canal, localidad o momento.

**CT-04 · Preservar condiciones.** Una afirmación sujeta a descuento, localización, fecha, canal o configuración no se generaliza fuera de esas condiciones.

**CT-05 · Relacionar representaciones de forma controlada.** En Web pueden combinarse HTML y Schema.org solo con conexión suficiente de entidad y contexto. Registrar de qué representación procede cada afirmación.

**CT-06 · Distinguir equivalencia y contradicción.** Dos valores aparentemente distintos pueden ser compatibles por unidades, periodo, entidad u otras condiciones. No declarar contradicción sin comprobar comparabilidad de alcance y momento.

**CT-07 · Rutas de respuesta.** Cuando la conclusión depende de varios elementos, registrar la sucesión de afirmaciones y conexiones que la fundamenta. No puntuar cantidad de pasos ni dar por publicada una conclusión inferida sin soporte.

**CT-08 · Evitar conocimiento externo sustitutivo.** Puede emplearse una regla aritmética o semántica general válida; no incorporar datos comerciales de otra fuente como si formaran parte de la interfaz examinada.

**CT-09 · No colapsar diferencias de contenido.** Conservar afirmaciones discordantes y variantes alternativas; el resumen informativo del agente no debe ocultar discrepancias.

**CT-10 · Revisión trazada.** Si aparece nueva evidencia, actualizar la interpretación, indicar qué decisión cambió y conservar la referencia a la evidencia que motivó el cambio.

### 7.3. Composición y derivación justificada

Una respuesta puede construirse a partir de hechos publicados y relaciones sustentadas: `talla 42 ↔ SKU-420`, `SKU-420 ↔ InStock`. Esta composición solo es válida si corresponde a la misma entidad comercial y a condiciones y momentos compatibles. Similarmente, precio base + descuento aplicable + condiciones explícitas pueden permitir un cálculo aritmético válido.

**Regla de cierre:** no se establece una longitud máxima de ruta. Se exige justificar **cada vínculo material para la conclusión** y no usar supuestos comerciales no acreditados. La ausencia de expresión literal no es, por sí sola, una deficiencia informativa.

### 7.4. Salida de la etapa

El conjunto pertinente debe permitir responder qué elementos contribuyen a qué componente del RI, con qué alcance y soporte; qué candidatos quedan pendientes; y qué partes esenciales todavía no tienen soporte observado. **Es una base para comprobar y valorar, no una respuesta comercial definitiva ni un GSC.**

## 8. Disponibilidad efectiva y cobertura

### 8.1. Comprobación previa vigente

La pregunta es: **¿existe al menos un dato, afirmación o relación pertinente que pueda obtenerse y leerse efectivamente bajo el perfil de consumo previsto para el ámbito?**

| Resultado | Regla y consecuencia |
|---|---|
| **Disponibilidad efectiva = 1** | Existe algún elemento pertinente utilizable, aunque sea incompleto o general. Continuar con los AC pertinentes. |
| **Disponibilidad efectiva = 0** | Se ha acreditado que no existe información pertinente utilizable, por ausencia o imposibilidad efectiva de obtenerla y leerla bajo el perfil. **IR = 0; no valorar los AC.** |
| **Comprobación inconclusa** | No se ha podido fundamentar el binario. Registrar estado del procedimiento y motivo **sin asignar un tercer valor a la escala 0/1**, sin fijar IR ni fabricar valoraciones de AC. |

**Advertencia:** un recurso recuperado correctamente puede carecer de información pertinente. A la inversa, una irregularidad técnica puede coexistir con información pertinente efectivamente utilizable en otra representación admisible del ámbito.

### 8.2. Regla general de suficiencia de exploración

La cobertura necesaria es **proporcional a la afirmación que debe sostenerse**:

- Para **afirmar presencia** basta probar al menos un elemento pertinente efectivamente utilizable. Esto **no implica** que la exploración esté completa para valorar después cada AC.
- Para **afirmar ausencia de información pertinente**, se necesita demostrar una revisión adecuada de las fuentes, representaciones y zonas plausibles del ámbito, incluyendo relaciones y expresiones alternativas razonables.
- Para **afirmar carencia de un componente o variante** en Concreción/Aplicabilidad, se necesita cobertura dirigida a ese componente y conjunto, no únicamente una búsqueda general.
- Para **afirmar coherencia o contradicción**, se necesita inspección adecuada de afirmaciones comparables relevantes; no se puede inferir exactitud a partir de la falta de conflictos encontrados.
- Para **afirmar fiabilidad**, la cobertura y el soporte dependen de la naturaleza y volatilidad del hecho, sin imponer a todos los casos una verificación externa idéntica.

### 8.3. Comprobación de cobertura — CO-01 a CO-09

**CO-01.** Registrar el **universo examinable** definido por ámbito, recurso, perfil y condiciones, sin prometer cobertura de fuentes fuera de ese universo.

**CO-02.** Registrar los recursos obtenidos, representaciones y secciones comerciales inspeccionadas, entidades reconocidas y limitaciones de lectura.

**CO-03.** Verificar que se buscaron las **funciones informativas del RI** y formas de representación pertinentes, no solo una cadena literal o un único atributo.

**CO-04.** Revisar los **componentes de respuesta** y conjuntos afectados: saber qué se buscó para cada componente y dónde podría aparecer.

**CO-05.** Comprobar referencias, vínculos e identificadores que razonablemente pudieran conducir a una pieza decisiva dentro del ámbito autorizado.

**CO-06.** Antes de un juicio negativo, resolver o justificar los candidatos plausiblemente decisivos que permanecen pendientes.

**CO-07.** Distinguir: *no publicado*, *no obtenible/legible bajo el perfil*, *no localizado pese a revisión suficiente* y *no comprobado por cobertura insuficiente*. Son diagnósticos diferentes y no autorizan idénticas conclusiones.

**CO-08.** Conservar prueba de cómo se examinó el contenido y de los límites de esa inspección, especialmente para una ausencia.

**CO-09.** Si una comprobación no alcanza cobertura adecuada para su conclusión, ampliar inspección o declarar la decisión inconclusa/NE según la fase y el juicio afectados.

### 8.4. Casos límite de obtención

- **Fallo puntual de una herramienta:** no se presume automáticamente ausencia de información; comprobar si se trata de una imposibilidad efectiva del perfil o de un fallo de auditoría no concluyente.
- **Contenido presente solo mediante interacción no admitida:** no es utilizable en ese ámbito/perfil; si no queda ningún otro elemento pertinente y se acredita la condición, disponibilidad efectiva = 0. La conformidad del mecanismo se juzga en el expediente técnico.
- **HTML utilizable y Schema.org defectuoso:** en Web puede existir disponibilidad efectiva 1 por HTML; en Web Schema.org hay que examinar aisladamente si su información pertinente es utilizable. No trasladar automáticamente uno de los resultados al otro.
- **Resultado positivo parcial:** basta para disponibilidad efectiva 1; no basta por sí mismo para otorgar GSC 2 a ningún AC.

### 8.5. Registros de cobertura

Cada comprobación susceptible de fundamentar una ausencia debe incluir: objetivo de la búsqueda, representaciones accesibles, regiones/entidades inspeccionadas, métodos semánticos y literales utilizados, alternativas verificadas, resultados, candidatos pendientes, limitaciones y conclusión razonada. **No se exige conservar una transcripción indiscriminada de cada operación irrelevante**, pero sí soporte adecuado para reexaminar la afirmación negativa.

## 9. Protocolo transversal de evidencias

### 9.1. Principio y tipos de registro

**Principio:** toda decisión relevante debe poder reconstruirse desde una observación o comprobación identificable. La evidencia no es una explicación inventada a posteriori.

Distinguir, como mínimo:

1. **Recurso/instantánea:** representación comercial efectivamente obtenida, con momento y condiciones de lectura.
2. **Evidencia elemental:** fragmento, valor, afirmación, relación o resultado de comprobación identificable y localizable.
3. **Cobertura de inspección:** registro de qué se examinó y con qué límites.
4. **Hallazgo:** interpretación fundada que expresa suficiencia, limitación, discrepancia o ausencia respecto de una propiedad o AC.
5. **Juicio GSC:** aplicación de las reglas del criterio a hallazgos y evidencias.

Estas entidades **se relacionan** y no deben reducirse a una sola nota narrativa.

### 9.2. Campos obligatorios generales del registro de evidencia — propuesta V1

| Campo | Obligación |
|---|---|
| `evidencia_id`, `caso_id` | Siempre: identificación y enlace al expediente. |
| `fuente`, `ambito`, `representacion` | Siempre: ecommerce/recurso y ámbito bajo examen. |
| `localizador` | Siempre que el formato lo permita: URL y sección/selector, ruta JSON/XML, fila/columna, identificador de entidad o fragmento. Si no existe localizador estable, aportar extracto/instantánea que lo supla. |
| `contenido_original` | Siempre: dato literal, valor, afirmación, relación o resultado de prueba; distinguirlo de la paráfrasis. |
| `captura_fecha_hora`, `perfil_consumo` | Siempre: cuándo y bajo qué condiciones se obtuvo. |
| `entidad_y_alcance` | Cuando afecten la interpretación: sujeto, producto/variante/oferta/vendedor, mercado, canal, periodo o condición. Si es desconocido, registrarlo, no inventarlo. |
| `contexto_necesario` | Cuando se necesite para comprender etiqueta, unidad, sujeto, condición o relación; puede remitir a evidencias vinculadas. |
| `metodo_comprobacion` | Siempre para resultados analíticos, negativos o derivados; indicar operación ejecutada y material inspeccionado. |
| `resultado_observado` | Siempre: qué acredita literalmente esta pieza, sin convertirlo en juicio GSC. |
| `soporte_reexaminable` | Siempre: referencia a recurso conservado, extracto verificable, evidencia conjunta o artefacto disponible. |
| `limitaciones` | Siempre que exista incertidumbre relevante, ausencia de identidad, contexto incompleto o restricción de cobertura. |

La vinculación funcional (`ri_id`, `componente`, `funcion`) y la vinculación evaluativa (`hallazgo_id`, `AC`, propiedades) pueden almacenarse en registros asociados para evitar duplicar la evidencia. **No son opcionales para un juicio que dependa de ella.**

### 9.3. Reglas generales EV-01 a EV-15

**EV-01.** Guardar el contenido observado **literalmente** y separar la versión interpretada o normalizada.

**EV-02.** Mantener procedencia, representación, localizador, fecha/hora y perfil de consumo; un enlace sin captura contextual no siempre basta si el dato puede cambiar.

**EV-03.** Conservar el contexto mínimo necesario para interpretar la afirmación sin desanclarla de sujeto, atributo, unidad o condición.

**EV-04.** Documentar la conexión entre cada evidencia y el componente o función del RI al que contribuye.

**EV-05.** Identificar expresamente qué relaciones están **publicadas**, cuáles son interpretaciones válidas y cuáles son hipótesis pendientes o excluidas.

**EV-06.** En pruebas de **ausencia**, conservar objetivo, alcance, métodos, cobertura, posibles localizaciones inspeccionadas y límites; una búsqueda sin resultados no es prueba suficiente por sí sola.

**EV-07.** En pruebas de **atribución**, incluir soporte que permita reconocer identidad de entidades y vínculo afirmación–entidad.

**EV-08.** En **derivaciones**, conservar operandos/datos, relaciones, reglas admitidas, condiciones y conclusión obtenida; distinguir resultado derivado de dato literal.

**EV-09.** En **contradicciones**, preservar las afirmaciones comparadas y justificar identidad, alcance, condiciones y momento comparables antes de declararlas materiales.

**EV-10.** Para **actualidad**, no presentar la hora de captura como prueba de que el contenido se actualizó o es vigente; buscar indicios pertinentes del estado comercial y su referencia temporal.

**EV-11.** Para **exactitud**, no presentar como comprobación de verdad la mera ausencia de contradicción entre representaciones del mismo origen; registrar qué sustento existe y qué no puede confirmarse.

**EV-12.** Diferenciar **trazabilidad/verificabilidad ofrecidas por la información** (P17/P18) de la capacidad del auditor para conservar un registro. Una captura auditora no confiere automáticamente esas propiedades al ecommerce.

**EV-13.** Reutilizar la misma evidencia para distintos hallazgos/AC cuando corresponda, explicando su consecuencia específica en cada uno; no duplicar ni multiplicar penalizaciones automáticamente.

**EV-14.** La evidencia externa, si se utiliza para contrastar exactitud o vigencia, debe etiquetarse como **fuente de comprobación**, nunca como contenido comercial publicado en la interfaz auditada.

**EV-15.** Mantener el vínculo entre registro estructurado e informe. El informe puede resumir, pero ha de conservar referencias que permitan acceder a las evidencias relevantes.

### 9.4. Reglas por tipo de evidencia

| Tipo | Contenido adicional que debe conservarse | Riesgo que controla |
|---|---|---|
| **Presencia/contenido** | Fragmento, etiqueta, unidad y sujeto pertinentes. | Citar un valor fuera de contexto. |
| **Identidad/atribución** | Identificadores, relaciones y alcance del sujeto. | Confundir variante, modelo u oferta. |
| **Relación/derivación** | Nodos, vínculos, condiciones y regla inferencial legítima. | Introducir una relación o dato supuesto. |
| **Normalización/comparación** | Valores originales, unidades, equivalencia/conversión y bases comparables. | Comparar magnitudes no equivalentes. |
| **Coherencia/conflicto** | Ambas afirmaciones, identidad, contexto y momentos. | Falsas contradicciones. |
| **Actualidad/exactitud** | Fuente de contraste, fecha del hecho y método de corroboración. | Confundir captura reciente o concordancia interna con verdad. |
| **Ausencia** | Universo examinable, rutas de inspección y cobertura negativa. | Ausencias falsas por mala búsqueda. |
| **Limitación de acceso/lectura** | Petición/perfil, respuesta y condición que impide consumir el contenido. | Confundir incidente técnico y efecto sobre RI. |

### 9.5. Suficiencia de evidencia para emitir un GSC

Antes de valorar, aplicar la siguiente prueba:

- **Correspondencia:** ¿las evidencias sostienen precisamente el hallazgo y el AC, para el mismo RI y entidad?
- **Contexto:** ¿se conocen el alcance y las condiciones necesarios, o la falta de ellos es precisamente el hallazgo acreditado?
- **Cobertura:** ¿se han examinado las unidades, componentes y representaciones necesarios para el juicio, especialmente si es negativo?
- **Resolución de conflictos:** ¿se han tratado las contradicciones/candidatos potencialmente decisivos, o se ha documentado el límite?
- **Reexamen:** ¿otro auditor puede recuperar o reconstruir las afirmaciones, pruebas y relaciones suficientes para revisar la valoración?

Si alguna respuesta es negativa y compromete **materialmente** el juicio, ampliar las comprobaciones. Si no es posible, usar el tratamiento de **NE** para el AC pertinente, o **comprobación de disponibilidad inconclusa** si el problema está en esa puerta previa; no asignar un 0 sin fundamento.

### 9.6. Salida para el informe

Cada hallazgo reportable ha de aportar, como mínimo: **qué se observó**, **qué faltó o qué quedó suficientemente resuelto**, **a qué componente del RI afecta**, **qué propiedad lo explica**, **qué consecuencia específica tiene para el AC**, **qué evidencia lo soporta** y **qué limitación impide conclusiones más amplias**. Las recomendaciones, si se generan, deben indicar una corrección verificable sin atribuir causas no probadas.

## 10. Comprobación operativa de propiedades P06–P18

### 10.1. Método común de comprobación — PR-01 a PR-09

Las propiedades **describen características observables de información pertinente**. Se comprueban según el RI, ámbito y hallazgo. **No se valoran individualmente con GSC, 0/1/2 ni con pesos**.

Para cada propiedad relevante, producir una ficha breve con: **pregunta de comprobación, elementos examinados, método aplicado, resultado observado, evidencia, limitación o condición favorable y efecto específico para el AC**.

**PR-01.** Seleccionar propiedades a partir de las necesidades del AC y de los hallazgos, no mediante una lista obligatoria e idéntica para todos los RI.

**PR-02.** Formular qué condición observable se espera comprobar antes de interpretar su satisfacción.

**PR-03.** Aplicar la comprobación a la información **pertinente y utilizable** del ámbito; no ampliar el universo para completar deficiencias.

**PR-04.** Contrastar las unidades necesarias del RI: objeto, desagregación, condiciones, relaciones y componentes de respuesta.

**PR-05.** Distinguir carencia **acreditada** de imposibilidad de obtener evidencia suficiente.

**PR-06.** Evitar considerar defectuosa una representación solo por no utilizar el campo, vocabulario, orden o forma literal preferida por el auditor.

**PR-07.** Identificar cuando una propiedad incide en varios AC; motivar por separado cada repercusión.

**PR-08.** Registrar limitaciones que se refieren al **contenido comercial** sin transformarlas en evaluaciones generales de sintaxis, publicación o conformidad técnica.

**PR-09.** Una observación favorable de una propiedad no garantiza por sí sola GSC 2: el juicio corresponde a la condición íntegra del AC.

### 10.2. Fichas operativas generales de propiedades

#### P06 · Completitud

- **Pregunta:** ¿están presentes los componentes de conocimiento necesarios para la cuestión y su alcance?
- **Prueba general:** comparar el inventario de componentes del RI con afirmaciones y relaciones pertinentes efectivamente disponibles; registrar qué piezas sustantivas/auxiliares aparecen y qué ausencias han sido comprobadas.
- **Evidencia requerida:** componentes del RI, elementos originales que los soportan y prueba de cobertura para los componentes ausentes.
- **Precaución:** no exigir atributos ajenos al RI ni confundir información de identidad con el estado solicitado. Puede existir información pertinente aunque falte la respuesta sustantiva.
- **Incidencia típica:** Concreción; también Justificación o Aplicabilidad cuando los componentes faltantes afectan su fundamento o atribución.

#### P07 · Granularidad

- **Pregunta:** ¿el nivel de diferenciación de la información coincide con la desagregación que exige el RI?
- **Prueba general:** comparar unidades del RI (modelo, variante, oferta, vendedor, periodo, condiciones) con las unidades a las que se refiere cada afirmación; examinar si existe vínculo suficiente para desagregar.
- **Evidencia:** enumeración del conjunto evaluado, unidades con datos, relación de estados por entidad y prueba de las unidades sin resolución.
- **Precaución:** una afirmación a nivel de modelo no equivale automáticamente a afirmaciones por variante; tampoco todo RI requiere detalle por variante.
- **Incidencia típica:** Concreción y, según la cuestión, Aplicabilidad o Comparabilidad.

#### P08 · Explicitud

- **Pregunta:** ¿los hechos comerciales pueden conocerse mediante expresiones directas o derivaciones suficientemente justificadas, sin introducir suposiciones que compensen información ausente?
- **Prueba general:** clasificar qué afirmaciones están publicadas, cuáles se obtienen de relaciones/operaciones sustentadas y qué conclusiones necesitarían asumir hechos no expresados.
- **Evidencia:** texto o valor original, vínculos/operaciones empleados y límites de la interpretación.
- **Precaución:** una derivación válida no se penaliza por longitud; literalidad o redundancia no son equivalentes a calidad.
- **Incidencia típica:** Concreción, Precisión o Justificación según el efecto.

#### P09 · Claridad

- **Pregunta:** ¿el significado de los términos, afirmaciones y valores pertinentes puede interpretarse sin ambigüedades materiales?
- **Prueba general:** identificar términos polisémicos, unidades o etiquetas no definidas, alcance ambiguo y lecturas alternativas razonables que cambien la respuesta.
- **Evidencia:** fragmento original, contexto semántico y alternativas de interpretación materialmente distintas.
- **Precaución:** no confundir dificultad técnica de lectura con ambigüedad semántica; tampoco confundir ambigüedad de significado con mera falta de atribución a una variante.
- **Incidencia típica:** Precisión.

#### P10 · Estructuración semántica

- **Pregunta:** ¿se distinguen los componentes y sus relaciones significativas para la cuestión?
- **Prueba general:** reconstruir sujetos, atributos, valores, agrupaciones, vínculos y condiciones; verificar si el contenido admite relaciones válidas o las presenta equívocas.
- **Evidencia:** elementos de estructura o texto donde figuran agrupaciones/vínculos, rutas de relación y posibles alternativas.
- **Precaución:** no premiar sintaxis Schema.org conforme por sí misma ni penalizar falta de marcado cuando otra representación admisible es semánticamente suficiente.
- **Incidencia típica:** Precisión, Aplicabilidad, Comparabilidad o Justificación según la consecuencia.

#### P11 · Identificabilidad

- **Pregunta:** ¿las entidades que intervienen pueden distinguirse suficientemente entre sí y vincularse con la información pertinente?
- **Prueba general:** confrontar productos, variantes, ofertas, vendedores e identificadores; localizar homónimos, identificadores ambiguos, referencias incompletas o uniones no acreditadas.
- **Evidencia:** denominaciones, SKU/IDs o relaciones que establecen identidad, con condiciones de alcance.
- **Precaución:** no equiparar «identificador existente» a identificación inequívoca; no exigir un tipo único de identificador si el contenido distingue adecuadamente las entidades.
- **Incidencia típica:** Aplicabilidad, Concreción o Justificación.

#### P12 · Contextualización

- **Pregunta:** ¿se conocen las circunstancias necesarias para entender y aplicar las afirmaciones al RI?
- **Prueba general:** examinar periodo, mercado, canal, unidad, configuración, oferta y condiciones comerciales relevantes; distinguir contextos exigidos del RI de detalles accesorios.
- **Evidencia:** condiciones publicadas, asociación con afirmaciones, alcance y momentos.
- **Precaución:** no exigir por defecto todas las circunstancias posibles; exigir las que cambian materialmente el significado, cobertura o aplicabilidad.
- **Incidencia típica:** Concreción, Aplicabilidad, Precisión, Comparabilidad.

#### P13 · Normalización

- **Pregunta:** ¿los conceptos, unidades, categorías y referencias permiten las equivalencias justificadas que necesita el RI?
- **Prueba general:** identificar bases de medida o convenciones y probar conversiones/equivalencias cuando sean necesarias para interpretar o contrastar valores.
- **Evidencia:** valores y unidades originales, convención de referencia, regla de equivalencia y resultado derivado.
- **Precaución:** no imponer formatos idénticos; una conversión fundamentada puede ser suficiente. La falta de normalización solo afecta el GSC si perjudica una condición relevante.
- **Incidencia típica:** Precisión y Comparabilidad.

#### P14 · Exactitud

- **Pregunta:** ¿qué comprobaciones sustentan la correspondencia de la afirmación con un hecho comercial comprobable?
- **Prueba general:** identificar la afirmación y su naturaleza; contrastar con referencias pertinentes y suficientemente independientes cuando existan; documentar discrepancias y alcance de la verificación.
- **Evidencia:** dato publicado, comprobación/ref. de contraste, momento, método y resultado, sin confundir corroboración con certeza absoluta.
- **Precaución:** falta de contraste no prueba falsedad; coincidencia de dos representaciones del mismo origen no demuestra exactitud.
- **Incidencia típica:** Fiabilidad.

#### P15 · Actualidad

- **Pregunta:** ¿qué soporte permite relacionar la información con el estado comercial vigente en el momento pertinente?
- **Prueba general:** identificar el momento exigido por el RI, fechas o señales de vigencia, posible volatilidad del dato y comprobaciones temporales disponibles.
- **Evidencia:** estado publicado, fecha de referencia, registro temporal o comprobación adecuada al hecho y contexto.
- **Precaución:** la hora de descarga del auditor no certifica que el hecho publicado sea actual; la ausencia de fecha visible no implica por sí sola desactualización.
- **Incidencia típica:** Fiabilidad.

#### P16 · Coherencia

- **Pregunta:** ¿son compatibles entre sí las afirmaciones sobre la misma realidad comercial bajo condiciones y momentos comparables?
- **Prueba general:** comparar afirmaciones internas y entre representaciones admitidas; verificar identidad, unidades, condiciones y tiempo antes de concluir contradicción.
- **Evidencia:** pares/conjuntos de afirmaciones originales, metadatos de sujeto/alcance/momento y explicación del conflicto o compatibilidad.
- **Precaución:** ausencia de contradicción no demuestra exactitud; diferencias legítimas de oferta, canal o instante no son incoherencias materiales.
- **Incidencia típica:** Fiabilidad y, según el caso, Precisión o Justificación.

#### P17 · Trazabilidad

- **Pregunta:** ¿puede identificarse y seguirse la procedencia y trayectoria relevante de la información que sustenta una respuesta?
- **Prueba general:** buscar autoría, fuente, versiones, referencias o cadenas de origen de las afirmaciones cuando sean pertinentes para la cuestión; distinguir la trazabilidad del ecommerce de la que crea el expediente auditor.
- **Evidencia:** referencias, registros y relaciones de procedencia efectivamente expuestos o identificables; límites de la cadena.
- **Precaución:** registrar una URL o un fragmento como auditor no convierte automáticamente la afirmación comercial en trazable.
- **Incidencia típica:** Justificación; puede contribuir a Fiabilidad cuando sustenta comprobaciones.

#### P18 · Verificabilidad

- **Pregunta:** ¿las afirmaciones pueden contrastarse mediante pruebas o referencias pertinentes y suficientemente identificables?
- **Prueba general:** determinar qué evidencia o referencia podría contrastar la afirmación, si es accesible bajo el método y qué alcance tiene el contraste; distinguir posibilidad de contrastar de comprobación ya concluida.
- **Evidencia:** referencias verificables, procedimiento de contraste, resultados obtenidos o límites documentados.
- **Precaución:** la posibilidad de contrastar un dato no prueba que sea verdadero; no crear verificabilidad artificial mediante afirmaciones libres del auditor.
- **Incidencia típica:** Justificación y, cuando procede, Fiabilidad.

### 10.3. Relaciones orientativas, no automáticas

| AC | Propiedades que pueden resultar especialmente relevantes |
|---|---|
| **Concreción** | P06, P07, P08, P12. |
| **Precisión** | P08, P09, P10, P13. |
| **Aplicabilidad** | P10, P11, P12; también P07 según el hallazgo. |
| **Comparabilidad** | P07, P10, P12, P13. |
| **Fiabilidad** | P14, P15, P16 y P18 cuando corresponda. |
| **Justificación** | P08, P17, P18, relaciones de soporte; otras propiedades si condicionan la reconstrucción. |

Las asociaciones son **orientativas**. La elección se explica por el RI, el AC y el hallazgo, no por una correspondencia fija muchos-a-uno.

## 11. Guías generales de los seis criterios de aceptación

### 11.1. Cómo utilizar los anclajes

Las tablas siguientes ofrecen **reglas universales provisionales para la V1**. Sus expresiones «fundamental», «parcial» y «material» deben interpretarse **respecto del RI**, nunca como porcentajes inventados ni como un umbral válido automáticamente para toda categoría de oferta.

En todos los AC, antes de asignar 0/1/2: verificar **aplicabilidad**, **evidencia suficiente** y **cobertura apropiada**. NA y NE se aplican según §12. No confundir una limitación de un AC con una insuficiencia universal de la respuesta.

### 11.2. Concreción

**Condición vigente:** la información cubre los componentes de la cuestión con la extensión y el detalle necesarios, directamente o mediante derivaciones justificadas.

**Pruebas operativas:** (a) desplegar componentes sustantivos y auxiliares del RI; (b) contrastar su presencia y suficiencia; (c) comprobar la desagregación por entidad; (d) identificar componentes ausentes o solo cubiertos parcialmente; (e) validar derivaciones pertinentes.

**Propiedades habituales:** P06, P07, P08, P12; otras si el hallazgo lo requiere.

| GSC | Regla provisional de anclaje |
|---|---|
| **0** | La cobertura sustantiva de la cuestión **no queda satisfecha**: los elementos presentes, aunque pertinentes o auxiliares, no proporcionan una contribución suficiente a los componentes centrales del RI; insuficiencia acreditada mediante cobertura apropiada. |
| **1** | Existe **cobertura sustantiva parcial**: se aporta información relevante sobre parte de lo solicitado, pero faltan componentes, unidades del conjunto, desagregación o condiciones materialmente necesarias. |
| **2** | Los componentes, alcance y desagregación requeridos están **suficientemente cubiertos**, por afirmaciones directas o derivaciones justificadas. |

**Evidencias mínimas específicas:** matriz componente del RI ↔ soporte; población/unidades del alcance cuando proceda; pruebas de ausencias; contexto y rutas de derivación.

**Fronteras:** disponibilidad efectiva 1 puede coexistir con GSC 0 en Concreción si solo se dispone, por ejemplo, de una identificación auxiliar sin el hecho solicitado. La diferencia 0/1 en cobertura parcial necesita calibración con RI que exijan múltiples componentes o variantes; no adoptar un porcentaje universal.

### 11.3. Precisión

**Condición vigente:** el significado de afirmaciones, términos, valores y relaciones puede interpretarse inequívocamente.

**Pruebas:** (a) identificar afirmaciones relevantes; (b) revisar significado, unidades, conceptos, etiquetas y relaciones; (c) buscar lecturas alternativas razonables; (d) determinar si estas cambian materialmente la respuesta o dejan parte interpretable.

**Propiedades habituales:** P08, P09, P10, P13.

| GSC | Regla provisional de anclaje |
|---|---|
| **0** | El significado de la información necesaria **no puede determinarse suficientemente** por ambigüedades materiales que impiden interpretar la condición examinada. |
| **1** | Existe significado interpretable en una parte relevante, pero permanecen ambigüedades que limitan materialmente el juicio sobre la cuestión. |
| **2** | El significado de los componentes relevantes es **suficientemente inequívoco** para el RI, incluso si requiere equivalencias o conversiones fundamentadas. |

**Evidencias:** fragmentos originales, contexto, unidades, definiciones y lecturas alternativas materiales con su fundamento.

**Fronteras:** «disponible» puede ser un término semánticamente claro (Precisión suficiente) aunque no esté correctamente atribuido a una variante (limitación de Aplicabilidad). No duplicar sin razón una carencia de atribución como ambigüedad del significado.

### 11.4. Aplicabilidad

**Condición vigente:** la información puede atribuirse con claridad a la entidad, el alcance y las condiciones concretas que plantea el requisito.

**Pruebas:** (a) enumerar entidades y condiciones del RI; (b) establecer sujeto/alcance de cada afirmación; (c) verificar identidad y vínculos; (d) comprobar cobertura de atribución para el conjunto requerido; (e) registrar atribuciones ambiguas o ausentes.

**Propiedades habituales:** P10, P11, P12 y, cuando aporta el hallazgo, P07.

| GSC | Regla provisional de anclaje |
|---|---|
| **0** | No es posible establecer con fundamento una atribución relevante **suficiente** a la entidad o condiciones centrales del RI. |
| **1** | La atribución está acreditada para parte del conjunto o del alcance, pero subsisten vínculos, identidades o condiciones materialmente insuficientes. |
| **2** | Las afirmaciones necesarias pueden atribuirse **claramente** a las entidades, alcance y condiciones requeridos por el RI. |

**Evidencias:** sujetos, IDs, relaciones, ubicación semántica de la afirmación, canal, momento y condiciones de aplicación.

**Fronteras:** una afirmación general de disponibilidad puede ser parcialmente aplicable al modelo y no permitir atribución por cada talla; no inferir que se aplica a todas las variantes. La existencia de valor no acredita atribución.

### 11.5. Comparabilidad

**Condición vigente:** la información permite efectuar o evaluar el contraste requerido sobre bases equivalentes o equivalencias justificadas.

**Pruebas:** (a) comprobar si el RI **requiere contraste**; (b) identificar objetos de comparación y dimensiones/condiciones; (c) determinar equivalencia de bases o conversión justificable; (d) identificar datos faltantes o asimetrías materiales; (e) evaluar si puede efectuarse el contraste solicitado.

**Propiedades habituales:** P07, P10, P12, P13.

| GSC | Regla provisional de anclaje |
|---|---|
| **0** | El contraste requerido no puede establecerse válidamente con los elementos disponibles, por falta acreditada de bases compatibles o componentes decisivos. |
| **1** | El contraste puede efectuarse **parcialmente**, pero existen asimetrías, contextos o equivalencias que limitan materialmente su alcance o fundamento. |
| **2** | El contraste requerido puede efectuarse o evaluarse **suficientemente** con bases equivalentes o conversiones/equivalencias justificadas. |

**Evidencias:** elementos comparados, dimensiones, valores originales, unidades, condiciones equivalentes, reglas de conversión y resultado contrastable.

**Aplicabilidad:** si la cuestión **no exige contraste**, declarar **NA** justificado; no asignar 0 porque no haya alternativas para una cuestión que no las requiere. Si sí requiere contraste, la falta de datos comparables es una posible deficiencia, no una razón automática para NA.

### 11.6. Fiabilidad

**Condición vigente:** la corrección, actualidad y consistencia de la información están suficientemente sustentadas mediante comprobaciones y evidencias pertinentes.

**Pruebas:** (a) identificar las afirmaciones esenciales; (b) examinar la posibilidad de comprobar su exactitud; (c) documentar su referencia temporal y necesidad de vigencia; (d) buscar contradicciones entre afirmaciones comparables; (e) evaluar el soporte reunido para sustentar —o refutar— su corrección, actualidad y consistencia.

**Propiedades habituales:** P14, P15, P16 y P18 según proceda.

| GSC | Regla provisional de anclaje |
|---|---|
| **0** | Las comprobaciones pertinentes **acreditan deficiencias materiales** de corrección, vigencia o consistencia que impiden considerar satisfecha la condición de fiabilidad. |
| **1** | Existe sustento de fiabilidad en parte relevante de lo examinado, pero permanecen **limitaciones acreditadas** que afectan materialmente a la confianza en la información. |
| **2** | Las afirmaciones pertinentes disponen de **sustento suficiente y proporcionado a su naturaleza, volatilidad y alcance** respecto de corrección, actualidad y consistencia. |

**Evidencias:** afirmaciones, métodos y fuentes de contraste, referencias temporales, pares comparables, discrepancias y límites explícitos de comprobación.

**Fronteras decisivas:**

- **Ausencia de corroboración no es falsedad.** Si falta evidencia para decidir, tras las comprobaciones razonables, corresponde estudiar **NE**, no 0 por defecto.
- **Sin contradicciones no significa exactitud.** Coherencia no sustituye P14.
- **Captura reciente no implica dato actual.** El instante de consulta no sustituye P15.
- La expectativa de prueba debe ajustarse a hechos estables y volátiles; no exigir idéntica fuente externa para todo dato comercial.
- La sola imposibilidad de verificar externamente una afirmación tampoco autoriza a valorar que es falsa; debe separarse limitación de verificabilidad de refutación material.

El límite entre **GSC 1 y NE** exige especial calibración: GSC 1 necesita una limitación material **que sí pueda caracterizarse y fundamentarse** respecto de la condición de fiabilidad, no únicamente desconocimiento general.

### 11.7. Justificación

**Condición vigente:** la información expuesta aporta una base identificable y suficiente para sostener y reconstruir la respuesta mediante afirmaciones y relaciones de soporte justificadas.

**Pruebas:** (a) identificar conclusión o posibles respuestas; (b) vincular cada afirmación necesaria con elementos de soporte publicados y relaciones admitidas; (c) reconstruir las rutas que conduzcan al hecho solicitado; (d) detectar saltos, supuestos o referencias que no sustentan la conclusión; (e) determinar si un tercero puede reconstruir el fundamento pertinente.

**Propiedades habituales:** P08, P17, P18 y relaciones de soporte; otras si condicionan la reconstrucción.

| GSC | Regla provisional de anclaje |
|---|---|
| **0** | No existe base identificable suficiente para **sostener y reconstruir** la conclusión requerida: los vínculos decisivos no están fundamentados. |
| **1** | Existe una base de soporte **parcial**, pero faltan afirmaciones, relaciones o referencias materialmente necesarias para reconstruir la respuesta con el alcance solicitado. |
| **2** | Las afirmaciones y relaciones expuestas proporcionan una base **identificable, suficiente y reconstruible** para sostener la respuesta pertinente. |

**Evidencias:** afirmaciones de origen, relaciones, referencias de procedencia/contraste pertinentes, conclusiones derivadas diferenciadas de los datos originales.

**Fronteras:** justificar una respuesta **no equivale** a demostrar verdad o actualidad de cada afirmación (Fiabilidad). Un auditor puede conservar una captura de un dato y aun así hallar insuficiencia de trazabilidad o de relaciones ofrecidas por la información comercial. Las derivaciones fundadas no se penalizan por su número.

### 11.8. Separación de juicios sobre una misma observación

**Ejemplo:** «Producto disponible» en la cabecera de un modelo con variantes.

- Puede ser **pertinente y obtenible** → disponibilidad efectiva 1.
- Puede proporcionar **cobertura parcial** del hecho por variante → consecuencia para **Concreción**.
- Puede significar inequívocamente «disponible para compra online» → **Precisión** potencialmente suficiente.
- Puede no identificar qué talla está disponible → consecuencia para **Aplicabilidad**.
- Puede no sostener una conclusión sobre la talla 42 → consecuencia para **Justificación**.
- Su corrección o vigencia pueden carecer de comprobación suficiente → posible **NE en Fiabilidad**, no falsedad automática.
- Si el RI no requiere contraste, **Comparabilidad = NA**.

Una observación puede afectar varios AC, pero **solo** si se razona la consecuencia **diferenciada** que tiene para cada condición. No se computan penalizaciones mecánicas ni se deduce el resultado de un AC a partir del valor de otro.

## 12. Decisión de GSC, NA, NE y control de materialidad

### 12.1. Procedimiento universal de decisión — GSC-01 a GSC-12

**GSC-01 · Puerta de disponibilidad.** Solo valorar AC si disponibilidad efectiva = 1. Si es 0, fijar IR = 0 y dejar los AC **sin valoración**; no registrar NA o 0 por defecto en todos ellos.

**GSC-02 · Aplicabilidad.** Para cada AC, determinar si su condición corresponde al RI y ámbito. Si no corresponde, **NA justificado**. No usar NA porque falta información para un criterio pertinente.

**GSC-03 · Base probatoria.** Verificar evidencias y cobertura suficientes para juzgar la condición específica. Si faltan y no pueden completarse, **NE**, no 0 automático.

**GSC-04 · Condición satisfecha.** Si el AC está satisfecho suficientemente para el RI, asignar **2**, indicando componentes y evidencias favorables.

**GSC-05 · Condición parcial.** Si existe satisfacción parcial con limitaciones materiales acreditadas, asignar **1**, explicando la parte satisfecha y la parte limitada.

**GSC-06 · Condición no satisfecha.** Si la insatisfacción de la condición está acreditada, asignar **0**, explicando qué no queda satisfecho y por qué la evidencia es suficiente para afirmarlo.

**GSC-07 · Sin falsa precisión.** No transformar la escala ordinal en porcentajes, distancias métricas ni subpromedios de propiedades. No asignar pesos universales no aprobados.

**GSC-08 · Materialidad relativa.** Una limitación repercute en el GSC si afecta a la condición que define el AC respecto de la cuestión, entidad y alcance concretos.

**GSC-09 · Múltiples elementos del RI.** Una satisfacción mixta debe examinarse por unidades y componentes. No fijar un porcentaje universal de variantes resueltas para decidir 0/1/2; explicar qué elementos quedan cubiertos y si la condición global se satisface.

**GSC-10 · Evidencia compartida.** Un hallazgo puede fundamentar varios GSC, pero se requieren juicios específicos de cada AC.

**GSC-11 · Revisión de nueva evidencia.** Si un hallazgo o candidato altera materialmente un juicio, reabrir la comprobación afectada y documentar el cambio.

**GSC-12 · Decisión completa.** Todo GSC debe quedar acompañado de: criterio y condición, valor, hechos comprobados, propiedades relacionadas, evidencias citadas, cobertura, motivo de la decisión y limitaciones.

### 12.2. Árbol de decisión operativo

```text
¿La unidad RI × ámbito es aplicable y está delimitada?
  NO  → Registrar NA del RI o bloqueo de preparación, según causa.
  SÍ  → ¿La disponibilidad efectiva puede determinarse con evidencia?
          NO  → Comprobación de disponibilidad inconclusa; no emitir AC.
          SÍ  → ¿Disponibilidad = 0?
                  SÍ → IR = 0; no emitir valoraciones de AC.
                  NO → Para cada AC:
                         ¿El criterio corresponde al RI?
                           NO → NA motivado.
                           SÍ → ¿Hay cobertura/evidencia suficiente para juzgarlo?
                                   NO → Ampliar prueba; si persiste → NE.
                                   SÍ → ¿Condición suficientemente satisfecha?
                                           SÍ → 2.
                                           NO → ¿Existe satisfacción parcial
                                                  materialmente acreditada?
                                                   SÍ → 1.
                                                   NO → 0, con prueba de
                                                          insatisfacción.
```

La última rama **no autoriza 0 por descarte lógico sin evidencia**: solo se llega a ella si previamente se verificó base probatoria suficiente para caracterizar una insatisfacción.

### 12.3. Prueba de materialidad — aplicable a todos los AC

Ante un hallazgo aparentemente negativo, documentar:

1. **Condición:** ¿qué aspecto definido del AC podría verse afectado?
2. **Objeto:** ¿a qué componente, entidad, desagregación, relación o condición del RI afecta?
3. **Consecuencia:** ¿qué respuesta o parte del juicio se vuelve imposible, parcial, ambigua, inaplicable, no sustentada o no reconstruible?
4. **Soporte:** ¿qué evidencia demuestra esa limitación —o solo la sugiere—?
5. **Alcance:** ¿la limitación es material para la cuestión completa o accesoria? ¿El resto de la información la resuelve legítimamente?

**Solo las limitaciones con consecuencia justificada para la condición examinada deben reducir el GSC.** Esto impide puntuar defectos cosméticos o exigir información ajena al RI.

### 12.4. Separación de estados de excepción

| Situación | Tratamiento correcto | Tratamiento incorrecto |
|---|---|---|
| RI no procede para la clase/oferta según aplicabilidad definida. | NA del RI, justificado. | Disponibilidad 0 sin analizar aplicabilidad. |
| RI aplicable, información pertinente ausente tras cobertura suficiente. | Disponibilidad 0, IR 0; no valorar AC. | Seis AC = 0 por defecto. |
| RI aplicable, comprobación previa inconclusa. | Estado procedimental «inconclusa»; disponibilidad sin valor emitido; no valorar AC. | Crear «disponibilidad 2» o fingir disponibilidad 0. |
| Disponibilidad 1, un AC no corresponde a la cuestión. | NA del AC. | Darle 0 porque no se puede comparar. |
| Disponibilidad 1, AC pertinente, evidencias insuficientes para juzgar. | NE del AC y motivo. | Dar 0 o 1 por incertidumbre general. |
| Disponibilidad 1, deficiencia suficientemente acreditada. | GSC 0 o 1 según su consecuencia. | NE solo porque el resultado es negativo. |
| Disponibilidad 1, respuesta negativa correctamente sustentada. | Evaluar favorablemente los AC que cumpla. | Penalizar porque la oferta no satisface una preferencia. |

### 12.5. Regla explícita sobre incertidumbre en Fiabilidad y Justificación

La **falta de pruebas para verificar un hecho** y la **ausencia de base expuesta para reconstruir una respuesta** no son lo mismo. Para Fiabilidad, cuando el auditor no puede establecer la corrección/vigencia con fundamento suficiente, estudiar NE. Para Justificación, la falta **comprobada** de afirmaciones o conexiones de soporte en la información expuesta puede justificar 0/1 con una cobertura de inspección suficiente. No obligar a ambos criterios a recibir el mismo resultado.

### 12.6. Salida separada por AC

Cada criterio mantiene su juicio propio. **No se calcula un GSC global ni una media de seis AC.** La síntesis del RI (IR) y del ámbito (ICI y otros indicadores) requiere las reglas de agregación correspondientes, que **no forman parte de esta V1** salvo el efecto ya vigente de disponibilidad 0 sobre IR.

## 13. Procedimiento integral de ejecución

### 13.1. Secuencia operativa completa — OP-01 a OP-12

| Paso | Acción del agente | Control de salida obligatorio |
|---|---|---|
| **OP-01** | Identificar RI, ámbito, entidad, recurso, condiciones y fecha de referencia. | Contrato de entrada revisado; aplicabilidad determinada. |
| **OP-02** | Cargar o construir controladamente el perfil operativo del RI. | Componentes sustantivos/auxiliares, desagregación y límites de pertinencia claros. |
| **OP-03** | Delimitar el perfil de consumo y obtener los recursos admitidos. | Recursos/instantáneas, fecha, vía y restricciones registrados. |
| **OP-04** | Ejecutar exploración general y dirigida. | Inventario de candidatos con localizadores y contexto inicial. |
| **OP-05** | Aplicar prueba de pertinencia a los candidatos. | Decisiones pertinentes/pendientes/excluidas relevantes, con función y soporte. |
| **OP-06** | Construir el conjunto pertinente contextualizado. | Sujetos, afirmaciones, relaciones y condiciones vinculados a las fuentes. |
| **OP-07** | Verificar cobertura y disponibilidad efectiva. | 0/1 sustentado o comprobación inconclusa; rama de ejecución correcta. |
| **OP-08** | Determinar AC aplicables y planificar pruebas de propiedades. | Plan de comprobación por criterio, con evidencias requeridas. |
| **OP-09** | Ejecutar comprobaciones y ampliar localización si hace falta. | Hallazgos con evidencia original y cobertura suficiente o limitación explícita. |
| **OP-10** | Aplicar prueba de materialidad y reglas de GSC. | Decisión por AC: 0/1/2, NA o NE, con explicación diferenciada. |
| **OP-11** | Ejecutar controles de integridad, contradicciones y atribución. | Expediente consistente y decisiones revisables; incidencias registradas. |
| **OP-12** | Publicar salida estructurada y generar informe desde el expediente. | GSC, evidencias, límites, acciones verificables; no inventar IR/ICI. |

### 13.2. Orden de procesamiento y eficiencia

Es admisible obtener primero una **representación comercial completa** y utilizarla para varios RI del mismo recurso, siempre que cada evaluación conserve su pertinencia, cobertura y GSC **por unidad RI × ámbito**. También es admisible reutilizar evidencias capturadas una sola vez y vinculadas a varios RI o AC si identidad, momento, contenido y condiciones siguen siendo aplicables.

No se requiere repetir descargas o análisis evidenciales idénticos sin necesidad. La eficiencia de proceso **no sustituye** la comprobación de cobertura y la distinción de ámbitos.

### 13.3. Reapertura controlada

Una duda posterior de AC puede revelar información contextual omitida. El agente debe: registrar la cuestión; volver a inspeccionar las representaciones permitidas; añadir evidencias; revisar la pertinencia y los hallazgos afectados; reevaluar el AC; y documentar el motivo del cambio. No modificar silenciosamente la puntuación final sin reflejar la nueva base.

### 13.4. Resumen del razonamiento permitido

| Permitido | No permitido |
|---|---|
| Reconocer sinónimos, términos de dominio y expresiones equivalentes justificadas. | Seleccionar por asociación temática ilimitada. |
| Relacionar datos de una misma entidad mediante vínculos acreditados. | Suponer identidades porque dos nombres se parecen. |
| Realizar conversiones o cálculos válidos con condiciones conocidas. | Introducir costes, descuentos o estados no publicados para completar un resultado. |
| Examinar corroboraciones externas para Fiabilidad bajo el protocolo. | Utilizar datos externos como contenido resolutivo de la interfaz auditada. |
| Reabrir la búsqueda cuando se detecta posible omisión. | Considerar ausencia una búsqueda literal fallida. |
| Declarar NE o fase inconclusa cuando la evidencia no basta. | Transformar incertidumbre en GSC bajo o alto por intuición. |

## 14. Esquema de registros y salida para informe

### 14.1. Objetos del expediente — propuesta de datos V1

| Objeto | Contenido | Cardinalidad conceptual |
|---|---|---|
| `perfil_ri` | Contrato informativo del RI. | Uno por RI/versión de perfil. |
| `caso_evaluado` | Recurso, oferta/entidad, ámbito, condiciones, momento y perfil. | Uno por unidad aplicada. |
| `recurso_obtenido` | Representación efectivamente consumida y soporte preservado. | Uno o varios por caso. |
| `candidato` | Elemento inicialmente reconocido y decisión de pertinencia. | Cero o varios por caso. |
| `evidencia` | Observación original individual o prueba identificable. | Cero o varias por recurso/comprobación. |
| `cobertura` | Alcance de inspección y limitaciones. | Al menos un registro de inspección por decisión que lo requiera. |
| `hallazgo` | Resultado interpretado con propiedades/RI/AC vinculados. | Cero o varios por caso. |
| `valoracion_ac` | AC, GSC/NA/NE, justificación y evidencias. | Un juicio por AC examinado con disponibilidad 1. |
| `revision` | Cambio justificado de evidencia, selección o juicio. | Si se produce revisión. |

Una evidencia puede sustentar varios hallazgos; un hallazgo puede apoyarse en varias evidencias; y un hallazgo puede tener **consecuencias diferentes para varios AC**. Estas relaciones se registran explícitamente.

### 14.2. Estructura de ficha del RI — ejemplo YAML de plantilla

```yaml
ri_id: "RI-XXX"
version_perfil: "borrador-V1"
clase_oferta: "<clase del modelo de demanda>"
dimension: "<dimension>"
pregunta: "<pregunta literal>"
objeto: "<entidad o conjunto>"
hecho_relacion_solicitado: "<necesidad de conocimiento>"
componentes_respuesta:
  sustantivos:
    - "<componente principal>"
  auxiliares:
    - "<identificacion, relacion o contexto necesario>"
desagregacion: "<unidad/entidad del RI>"
alcance: "<conjunto delimitado>"
condiciones: []
aplicabilidad: "<cuando procede el RI>"
relaciones_resolutivas: []
funciones_informativas:
  - "describir"
  - "identificar"
  - "relacionar"
  - "contextualizar"
  - "sustentar_o_contrastar"
expresiones_ejemplo: []
casos_frontera: []
ambitos_pertinentes:
  - "Web"
fundamento_perfil: "<justificacion de decisiones interpretativas>"
pendientes_de_definicion: []
```

El YAML es un **ejemplo de estructura de intercambio**, no un formato técnico obligatorio ni una lista cerrada de funciones. En una implementación posterior se precisarán validación, versionado y vocabularios de campos.

### 14.3. Registro de evidencia — ejemplo YAML de plantilla

```yaml
evidencia_id: "E-XXX"
caso_id: "AUD-XXX"
fuente:
  ecommerce: "<ecommerce>"
  recurso: "<URL, identificador de feed o artefacto>"
  ambito: "Web"
  representacion: "HTML"
  localizador: "<selector, ruta, fila o segmento>"
contenido_original: "<fragmento o valor observado literalmente>"
contexto_necesario: "<etiquetas y contexto relevante>"
entidad_y_alcance: "<sujeto y condiciones conocidas>"
captura_fecha_hora: "<fecha-hora y zona>"
perfil_consumo: "<version del perfil>"
metodo_comprobacion: "<recuperacion/lectura/contraste>"
resultado_observado: "<hecho observado, sin valoracion de calidad>"
soporte_reexaminable: "<referencia a instantanea o extracto>"
limitaciones: []
vinculos:
  componente_ri: "<componente>"
  funcion_informativa: "<funcion>"
  hallazgos: []
```

### 14.4. Registro de valoración por AC — ejemplo YAML de plantilla

```yaml
caso_id: "AUD-XXX"
ri_id: "RI-XXX"
ambito: "Web"
disponibilidad_efectiva: 1
valoraciones:
  - criterio: "Aplicabilidad"
    estado: "valorado"  # valorado | NA | NE
    gsc: 1               # null si NA o NE
    condicion_evaluada: "<condicion vigente del AC>"
    propiedades_consideradas: ["P10", "P11", "P12"]
    evidencias: ["E-001", "E-002"]
    hallazgos: ["H-001"]
    parte_satisfecha: "<que esta suficientemente acreditado>"
    limitacion_material: "<que impide satisfaccion completa>"
    justificacion: "<relacion entre evidencia, condicion y valor>"
    cobertura: "<comprobacion de alcance/cobertura>"
    limitaciones_de_evaluacion: []
```

**Importante:** si disponibilidad es **0**, el objeto `valoraciones` no debe contener seis ceros ni seis NA: los AC **no se valoran**. Si la disponibilidad no puede determinarse, mantener `disponibilidad_efectiva: null` junto al campo **procedimental** `estado_disponibilidad: inconclusa`; no crear un nuevo nivel de disponibilidad. Si no procede un AC, `estado: NA, gsc: null`; si no se puede juzgar, `estado: NE, gsc: null`.

### 14.5. Estructura del informe sustentado por evidencias

El informe debe tener dos niveles conectados:

**A. Ficha de resultado accesible:** unidad evaluada; disponibilidad; tabla de AC y GSC/NA/NE; síntesis de hallazgos que explican los resultados; limitaciones y recomendaciones condicionadas.

**B. Expediente reexaminable:** detalles de observación, recursos originales, contexto, método de obtención, cobertura, candidatos decisivos, rutas de relación, pruebas por propiedad, hallazgos, juicios y revisiones.

La redacción de un hallazgo del informe seguirá, por regla general, esta plantilla:

> **Hecho observado:** [...]. **Alcance y evidencia:** [...]. **Condición de calidad afectada:** [...]. **Consecuencia para el AC y RI:** [...]. **Valor GSC:** [...], porque [...]. **Límites y acción verificable:** [...].

La recomendación debe apuntar a una **corrección verificable** (publicar, detallar, aclarar, atribuir, normalizar, corregir, actualizar, relacionar o fundamentar información; o remitir una incidencia al análisis técnico). No se debe atribuir sin pruebas la causa organizativa o de implementación de la carencia.

## 15. Casos de aplicación y calibración

Los ejemplos siguientes son **hipotéticos y metodológicos**. Ilustran pruebas y límites de decisión; **no constituyen auditorías reales ni validan por sí mismos los anclajes**. Las evidencias en una ejecución deberán sustituirse por fragmentos y localizadores verdaderamente obtenidos.

### 15.1. Caso A — información general para una cuestión por variante

**RI:** «¿Cuál es la disponibilidad comercial de cada variante del modelo?»  
**Ámbito:** Web.  
**Recurso hipotético:** tallas 41, 42 y 43 identificadas, más la afirmación «Disponible para compra online» en la cabecera del modelo; inspección suficiente sin encontrar estados individualizados ni relaciones que atribuyan inequívocamente el estado a cada talla.

**Localización:** listado de tallas = pertinente auxiliar/identificador; afirmación general = pertinente sustantiva parcial.  
**Disponibilidad efectiva:** **1**.

**Hallazgo:** hay información general de disponibilidad, pero no se justifica su extensión a cada variante.

| AC | Orientación ilustrativa | Fundamento que debe comprobarse |
|---|---|---|
| Concreción | **1** | Cobertura sustantiva general pero sin la desagregación requerida. |
| Precisión | **2**, si el significado comercial es inequívoco | No confundir significado con atribución. |
| Aplicabilidad | **1**, si hay atribución válida al modelo y no a cada talla | La afirmación tiene alcance parcial respecto del RI. |
| Comparabilidad | **NA**, si no se requiere contraste | No imponer comparación artificial. |
| Fiabilidad | **NE**, si no es posible sustentar un juicio sobre corrección/vigencia | Ausencia de comprobación no prueba falsedad. |
| Justificación | **1**, si la afirmación general fundamenta solo parte del alcance | No permite reconstruir estado por talla. |

Los valores son **hipótesis de calibración**, condicionados por los matices indicados, no una regla de asignación automática para todas las fichas semejantes.

### 15.2. Caso B — relación legítima y respuesta derivada

**RI:** disponibilidad de cada variante; **ámbito:** Web.  
Contenido admisible: `Talla 42 ↔ SKU-420` y `SKU-420 ↔ InStock`, con oferta, canal y momento justificadamente compatibles.

La ruta `talla → SKU → estado` es **pertinente y puede fundamentar** la disponibilidad de la talla 42. No penalizar porque no exista una sola frase literal que una talla y stock. **Tampoco extrapolar** este resultado a tallas 41 y 43: la cobertura de Concreción del RI completo depende de qué se encuentre sobre esas unidades.

**Evidencias exigidas:** correspondencia talla–identificador, estado–identificador, identidad y contexto comercial comparables, recurso/representación y captura.

### 15.3. Caso C — ausencia de información pertinente bajo el perfil

**RI:** disponibilidad por variante.  
**Ámbito:** Web, perfil de consumo que no ejecuta interacción ni el mecanismo concreto necesario para incorporar el contenido.  
El HTML obtenido contiene únicamente un contenedor sin datos comerciales sobre variantes o disponibilidad; tras inspección adecuada no hay elementos pertinentes recuperables en las representaciones admitidas.

**Disponibilidad efectiva = 0 → IR = 0 → AC no valorados.**

**Evidencia negativa necesaria:** perfil, recurso recuperado, representación original, zona inspeccionada, posibles fuentes admitidas revisadas y condición que impide obtener/leer contenido pertinente. El mero hecho de usar JavaScript no constituye por sí solo falta universal de disponibilidad ni prueba incumplimiento técnico general.

### 15.4. Caso D — búsqueda insuficiente

**RI:** disponibilidad por variante.  
La herramienta recupera únicamente una porción del recurso; no se conoce si el resto contiene información pertinente y no puede completarse la inspección.

**Resultado:** disponibilidad **inconclusa**, no 0. Registrar qué se obtuvo, qué falló, qué revisión adicional sería necesaria y qué decisiones quedan suspendidas. Este estado describe el **procedimiento**, no un tercer grado de disponibilidad efectiva.

### 15.5. Caso E — diferencia entre Precisión y Aplicabilidad

**RI:** ¿qué variantes están disponibles?  
Afirmación: «Disponible» en una cabecera de producto; sin correspondencia por variante.

Es posible que el término tenga **significado comercial claro** y, a la vez, que falte **atribución** a la entidad requerida. En tal caso, la limitación principal corresponde a Aplicabilidad, y la cobertura por variante puede afectar Concreción; no degradar Precisión por duplicación automática.

### 15.6. Caso F — información directa y verificabilidad de la respuesta

**RI:** «¿Cuál es el material principal de la funda?»  
Afirmación comercial utilizable: «Composición principal: 100 % algodón», atribuida inequívocamente a la funda, sin condiciones omitidas.

Esta afirmación puede satisfacer **Concreción**, **Precisión**, **Aplicabilidad** y aportar una base **identificable** para **Justificación** sin exigir una cadena de inferencias o referencias externas innecesarias. **Fiabilidad** requiere su propio análisis de corrección, actualidad y coherencia; no se deduce automáticamente del resto de los AC.

### 15.7. Caso G — comparación que requiere equivalencia

**RI:** «¿Cuál de dos ofertas tiene menor precio por kilogramo?»  
Oferta A: 750 g por 6 €; oferta B: 1 kg por 7 €. Bajo condiciones de precio comparables y sin costes/condiciones relevantes omitidos, una conversión aritmética fundamentada permite el contraste.

La existencia de distintas unidades de masa **no es por sí sola** deficiencia de Comparabilidad si la equivalencia resulta justificable. Si un precio incluye condiciones distintas de compra no aclaradas, deben examinarse los límites de contexto y aplicabilidad.

### 15.8. Caso H — afirmaciones discordantes entre HTML y Schema.org

**RI:** precio de una oferta.  
En una instantánea comparable, HTML expresa «79 €» y Schema.org «89 €» para la misma oferta, moneda, condiciones y momento.

- **Web:** comparar ambas afirmaciones; si son realmente comparables, registrar discrepancia y analizar P16/Fiabilidad y otras consecuencias pertinentes, sin elegir arbitrariamente una como verdadera.
- **Web Schema.org:** evaluar informativamente el valor y soporte del marcado en su ámbito aislado; el contraste con HTML puede servir como **evidencia diagnóstica de coherencia de Web**, pero no completar el contenido resolutivo del ámbito Schema.org.
- **Prueba necesaria:** identidad, moneda, oferta, canal, fecha y condiciones. Si la divergencia se explica por momentos u ofertas distintos, no declarar incoherencia material.

### 15.9. Caso I — información de popularidad y pertinencia

**RI:** disponibilidad de talla 42.  
Contenido: «superventas» y «producción de 10.000 unidades mensuales».

Ambas informaciones tienen asociación comercial con demanda o fabricación, pero **no desempeñan una función informativa justificada** para conocer el estado comercial actual de la talla, salvo que se publiquen relaciones concretas adicionales. No seleccionarlas como sustento para disponibilidad ni inferir stock desde ellas.

### 15.10. Caso J — FIABILIDAD con verificación no concluyente

**RI:** disponibilidad comercial actual.  
Existe la afirmación inequívoca «En stock», pero no se consigue corroborar su vigencia ni establecer que sea falsa tras comprobaciones adecuadas.

**No asignar Fiabilidad 0 por falta de corroboración.** Distinguir qué aspecto puede juzgarse con evidencia, si hay soporte parcial materialmente suficiente para GSC 1 o si el juicio **debe quedar NE**. Documentar metodología y límites de contraste. La respuesta puede seguir siendo suficientemente clara, atribuible y reconstruible en otros AC.

### 15.11. Caso K — entidad con característica ausente

**RI:** «¿Incluye el producto una batería recargable?»  
Contenido: «No incluye batería recargable», claramente atribuido al producto.

La respuesta negativa **resuelve informativamente** la cuestión si está suficientemente determinada y fundamentada. No degradar Concreción o Justificación por el hecho de que la característica no esté presente.

### 15.12. Caso L — ausencia acreditada frente a ausencia no comprobada en una lista de variantes

**RI:** disponibilidad por cada variante. Una ficha enumera diez variantes; se encuentra estado en ocho.

La constatación de «dos sin estado» exige comprobar qué variantes integran el conjunto, si la información está relacionada por otros identificadores, si hay afirmaciones generales legítimamente aplicables y qué representaciones admisibles se examinaron. Una vez acreditadas las ausencias, documentar su efecto sobre Concreción y Aplicabilidad. **No calcular GSC a partir de 8/10 de manera automática**: la materialidad y naturaleza de la condición deben justificarse según el RI.

### 15.13. Matriz mínima de calibración

Antes de aprobar la V1, utilizar casos que cubran:

| Dimensión de prueba | Caso representativo | Error que se pretende detectar |
|---|---|---|
| Pertinencia directa | Afirmación que expresa el hecho solicitado. | Omitir información clara. |
| Pertinencia auxiliar | Identificador y relación de variante. | Excluir piezas que no son la respuesta literal. |
| Solo relación temática | Popularidad frente a stock. | Sobreinclusión del LLM auditor. |
| Derivación válida | SKU–estado, precio calculable. | Penalizar inferencias justificadas. |
| Contexto insuficiente | Estado sin canal/variante. | Completar condiciones con conjeturas. |
| Disponibilidad 0 | Ausencia comprobada con cobertura. | Valorar AC cuando no procede. |
| Disponibilidad inconclusa | Lectura/inspección insuficiente. | Falsa ausencia. |
| AC 0/1/2 | Casos negativos, parciales y suficientes por AC. | Fronteras ambiguas de los anclajes. |
| NA/NE | Comparabilidad no pertinente y fiabilidad no evaluable. | Uso incorrecto de estados. |
| Coherencia | Valores aparentemente distintos con o sin contexto comparable. | Confundir diferencia e incoherencia. |
| Ámbitos | Web vs Web Schema.org vs catálogo. | Completar un ámbito con contenido de otro. |
| Informe | Hallazgo reconstruible con evidencia. | Puntuación opaca o evidencia ornamental. |

Los resultados esperados deben ser **acordados por revisión metodológica** antes de utilizarlos como referencia de validación de la Skill. No se define todavía un porcentaje de acuerdo que garantice fiabilidad universal.

## 16. Controles de calidad y resolución de incidencias

### 16.1. Validaciones obligatorias — QA-01 a QA-14

**QA-01.** El RI está identificado, conserva su formulación y dispone de perfil operativo congruente.

**QA-02.** La aplicabilidad y el ámbito se han delimitado sin extrapolaciones no justificadas.

**QA-03.** Cada recurso/evidencia proviene de una representación admitida, con momento y perfil de lectura.

**QA-04.** La selección de información pertinente identifica una contribución concreta al RI y no solo una asociación temática.

**QA-05.** Las entidades, variantes, ofertas, vendedores y condiciones no se han fusionado por semejanza superficial.

**QA-06.** Las relaciones entre afirmaciones y las conclusiones derivadas cuentan con soporte reconstruible.

**QA-07.** No se han utilizado hechos comerciales externos como si fueran contenido de la interfaz auditada.

**QA-08.** El juicio sobre disponibilidad dispone de prueba adecuada; si es 0, no aparecen GSC de los AC.

**QA-09.** La cobertura permite sostener ausencias o limitaciones materiales invocadas para reducir un GSC.

**QA-10.** Se han diferenciado afirmaciones contradictorias de otras referidas a distintas entidades, condiciones o momentos.

**QA-11.** Los estados NA/NE se utilizan por sus razones vigentes y no encubren deficiencias o errores de búsqueda.

**QA-12.** Cada valoración AC cita hallazgos/evidencias y explica de manera propia el resultado frente a la condición del criterio.

**QA-13.** No se han introducido subpuntuaciones de propiedades, grados de derivación ni agregaciones IR/ICI no aprobadas.

**QA-14.** El informe remite a evidencias originales suficientes y distingue hallazgos de hipótesis, limitaciones y recomendaciones.

### 16.2. Incidencias del procedimiento

| Incidencia | Acción preferente | Consecuencia si no se resuelve |
|---|---|---|
| Perfil RI ambiguo | Revisar delimitación; registrar diferencia sin alterar pregunta. | Bloqueo o valoración solo de parte delimitable, con alcance explícito. |
| Contenido no recuperable | Verificar perfil, repetir comprobación razonable y registrar fallo. | Disponibilidad 0 si se acredita imposibilidad efectiva; de lo contrario, inconclusa. |
| Candidato decisivo sin contexto | Ampliar inspección de recursos admitidos. | No fundamentar conclusiones incompatibles con la incertidumbre. |
| Contradicción entre afirmaciones | Comprobar entidad, condiciones, unidades y momento. | Registrar discrepancia sin inventar versión «correcta». |
| Falta de fuente para Fiabilidad | Documentar método y qué se pudo contrastar. | NE cuando no pueda decidirse; no 0 automático. |
| Evidencia descontextualizada | Recuperar soporte original y contexto. | El hallazgo no puede aceptarse hasta subsanar o declarar limitación. |
| El informe afirma más que el expediente | Revisar texto y vínculos evidenciales. | No publicar la conclusión no sustentada. |

### 16.3. Auditoría de decisiones y desacuerdos

La revisión debe utilizar el mismo RI, perfil, ámbito, instantánea y reglas. Ante desacuerdo, clasificar la fuente: **interpretación del RI**, **cobertura y localización**, **pertinencia**, **atribución/contexto**, **lectura de propiedad**, **evidencia suficiente** o **anclaje GSC**. Resolverlo documentando qué regla cambió o qué evidencia era distinta, en lugar de promediar valoraciones discrepantes.

## 17. Prueba de aceptación de la V1

### 17.1. Condición de ejecutabilidad

Una primera versión se considera **operativamente ejecutable para pilotaje** si, dado un RI y una representación admisible, un agente puede completar **sin inventar decisiones estructurales**:

1. Interpretación y validación del perfil de RI.
2. Exploración, detección de candidatos y selección por pertinencia funcional.
3. Comprobación de disponibilidad efectiva con cobertura demostrable.
4. Captura de evidencias y conservación de contexto, procedencia y momento.
5. Comprobación de propiedades pertinentes y hallazgos diferenciados.
6. Aplicación de anclajes por AC para producir 0/1/2 o NA/NE según corresponda.
7. Revisión de consistencia y salida reexaminable.

Que el agente pueda **no emitir un juicio cuando la evidencia no lo permite** es una capacidad necesaria, no un fallo por sí mismo.

### 17.2. Condiciones mínimas de un piloto

- Utilizar **RI de naturalezas distintas** (atributo simple, atribución por variante, composición/derivación, contraste y condición comercial) y al menos un ámbito bien delimitado.
- Incluir casos **suficientes, parciales, negativos, NA, NE, disponibilidad 0 e inspección inconclusa**.
- Mantener representaciones/instantáneas comparables para que varios auditores puedan aplicar las mismas reglas.
- Revisar omisiones de localización, sobreinclusión temática, atribuciones indebidas, pruebas negativas, calidad de evidencia y diferencias GSC.
- Ajustar anclajes y ejemplos antes de adoptar el procedimiento como estándar estable del proyecto.

### 17.3. Criterio de revisión humana

Un segundo evaluador debe ser capaz de responder desde el expediente: **qué preguntaba el RI, qué información se obtuvo, por qué se consideró pertinente, qué se comprobó, qué propiedad explicó el hallazgo, qué condición del AC quedó satisfecha o limitada y qué justifica el GSC**. Si no puede reconstruirlo, el registro es insuficiente aunque la cifra pueda parecer razonable.

### 17.4. Alcance intencionalmente limitado de V1

La V1 ejecuta la **valoración de AC/GSC** y la regla previa **disponibilidad 0 → IR 0**. No exige cerrar antes los coeficientes por importancia relativa de RI, las reglas de impacto/indispensabilidad para sintetizar IR, fórmulas de ICI, métricas comerciales o toda la auditoría técnica.

## 18. Límites de generalización y decisiones pendientes

### 18.1. Qué queda definido de forma general

- Contratos y roles: demanda, configuración, ejecución, revisión e informe.
- Ficha operativa del RI y prueba de su congruencia.
- Exploración general, dirigida y ampliada; selección por pertinencia funcional.
- Separación entre pertinencia, disponibilidad, satisfacción de AC y resolución del RI.
- Reglas sobre relaciones sustentadas y rechazo de conjeturas comerciales.
- Disponibilidad binaria, cobertura de ausencias y tratamiento procedimental de casos inconclusos.
- Registro de evidencias originales, contexto y conexiones; hallazgos y juicios separados.
- Preguntas y pruebas generales por P06–P18, con anclajes provisionales para cada AC.
- Reglas transversales 0/1/2, NA/NE, materialidad, QA y salida para informe.

### 18.2. Qué debe aportar cada modelo de demanda o auditoría

- La **pregunta y necesidad** concreta del RI, dimensión, clase, objeto, aplicabilidad e importancia cualitativa.
- Los **componentes constitutivos**, desagregación, alcance, relaciones y condiciones específicos de esa pregunta.
- La **pertinencia de cada ámbito** y su perfil de consumo.
- La **entidad/oferta** concreta y los recursos comerciales accesibles.
- La información realmente encontrada, sus condiciones y la materialidad de las limitaciones respecto de esa cuestión.

**No** se pueden establecer universalmente los atributos obligatorios, todas las unidades comerciales, la cantidad de variantes suficiente, los tiempos máximos de actualización o el número de comprobaciones para toda clase de oferta.

### 18.3. Decisiones pendientes de calibración, no obstáculos conceptuales

| Decisión | Propuesta V1 | Qué debe contrastarse antes de aprobar definitivamente |
|---|---|---|
| Campos de perfil RI | Estructura de §4 y anexo. | Mínimos reales y claridad de los componentes en RI variados. |
| Estados de candidato | Inicial, pertinente, pendiente, no pertinente. | Si mejoran resultados sin introducir burocracia excesiva. |
| Cobertura suficiente | Prueba orientada al juicio, sin porcentaje universal. | Pruebas de falsas ausencias en diferentes recursos y ámbitos. |
| Evidencias mínimas | Esquema y pruebas de §9. | Reexaminabilidad real, tratamiento de cambios y soportes. |
| Anclajes GSC por AC | §11–12. | Fronteras 0/1, 1/2 y NE, especialmente en Fiabilidad/Justificación. |
| Materialidad | Prueba de cinco preguntas. | Juicios en RI multiatributo o con muchas unidades. |
| Contrastes de exactitud/vigencia | Proporcionados a tipo de hecho. | Casos sin fuentes independientes o con actualización volátil. |
| Formatos de intercambio | YAML ilustrativo de §14. | Campos normalizados, validación y versionado. |
| Calibración entre auditores | Casos de §15 y revisión de desacuerdos. | Nivel suficiente de concordancia y causas de variación. |

### 18.4. Decisiones explícitamente no adoptadas

- No una escala de «grado o número de derivaciones» para decidir pertinencia o GSC.
- No reglas que penalicen automáticamente respuestas obtenidas por relaciones justificadas.
- No una lista universal de campos obligatorios o una equivalencia entre pertinencia y coincidencia literal.
- No nuevas puntuaciones para propiedades P06–P18 ni promedios automáticos para GSC.
- No disponibilidad efectiva ternaria; un proceso inconcluso se registra fuera de la escala binaria.
- No inferir falsedad desde ausencia de corroboración ni verdad desde ausencia de contradicciones.
- No mezclar información de Web Schema.org con HTML ajeno al marcado como contenido resolutivo de aquel ámbito.
- No trasladar los requisitos técnicos directamente a descuentos del GSC.
- No calcular IR/ICI con fórmulas no establecidas.
- No interpretar un GSC como probabilidad de recomendación, conversión o éxito de una IA particular.

## 19. Matriz de cobertura de acuerdos y pendientes

Esta matriz comprueba que el documento desarrolla los asuntos tratados en el proyecto; **no significa que todos estén empíricamente validados**.

| Asunto tratado | Sección | Resultado documental |
|---|---|---|
| Abstracción respecto de LLM y otros sistemas de IA | §1–2 | Fundamento conservado; evaluación de condiciones informativas y no del modelo auditor. |
| Separación informativo/técnico | §1–2, §8, §16 | Reglas de perfil de consumo y efecto contextual sin evaluación técnica duplicada. |
| Construcción del RI y modelo de demanda | §3–4 | Contrato y procedimiento de estructuración reutilizable. |
| RI como cuestión y no campo | §4 | Componentes, desagregación y relaciones, sin catálogo rígido de atributos. |
| Selección de contenido pertinente | §5–7 | Exploración y prueba de contribución/función/fundamento. |
| Leer todo frente a búsqueda dirigida | §5 | Exploración general, dirigida y reabierta, con cobertura justificada. |
| Amplitud de candidatos y límite de inferencia | §6–7 | Reconocimiento abierto; pertinencia funcional; sin conjeturas ni escala de pasos. |
| Información parcial frente a resolución completa | §6, §8, §11 | Pertinencia y disponibilidad distintas del GSC. |
| Información distribuida y contexto | §7 | Conjunto de datos, entidades, afirmaciones y relaciones con procedencia. |
| Disponibilidad efectiva 0/1 | §8, §12–13 | Puerta previa, IR=0 si disponibilidad 0 y tratamiento inconcluso separado. |
| Ausencias y cobertura | §8–9 | Pruebas negativas y reexamen; evitar falsas ausencias. |
| Evidencias ricas para el informe | §9, §14 | Campos mínimos, pruebas especializadas y vínculos a hallazgos. |
| Propiedades de calidad P06–P18 | §10 | Pautas observables, pruebas y cautelas para cada propiedad. |
| Criterios Concreción a Justificación | §11 | Procedimientos y anclajes provisionales diferenciados por AC. |
| GSC 0/1/2, NA/NE y materialidad | §12 | Árbol decisorio y reglas de excepción. |
| Fiabilidad, trazabilidad, verificabilidad | §9–12, §15 | Distinción entre evidencia auditora, soporte comercial y verdad del hecho. |
| Rutas y derivaciones justificadas | §7, §10–11, §15 | Relaciones reconstruibles sin penalización por pasos. |
| Ejemplos reales/hipotéticos y calibración | §15–17 | Batería para validación de V1. |
| Salida GSC y expediente auditable | §9, §14–17 | Registros estructurados e informe vinculados a evidencia. |
| IR/ICI/indicadores y objetivo de negocio | §1, §12, §17–18 | Excluidos de la implementación GSC inicial, sin inventar fórmulas o causalidad. |

## 20. Anexos: plantillas, reglas resumidas y glosario

### Anexo A. Hoja rápida de ejecución por RI

```text
IDENTIFICACIÓN
[ ] RI, objeto, dimensión, ámbito y entidad concretos
[ ] Desagregación, alcance, condiciones y aplicabilidad
[ ] Perfil de consumo y recursos examinables

LOCALIZACIÓN
[ ] Recurso/instantánea original y contexto preservados
[ ] Exploración general y dirigida
[ ] Componentes del RI vinculados a candidatos
[ ] Prueba contribución–función–fundamento
[ ] Candidatos decisivos pendientes revisados

DISPONIBILIDAD
[ ] Al menos un elemento pertinente utilizable → 1
[ ] O ausencia/inaccesibilidad acreditada → 0, IR 0, sin AC
[ ] O procedimiento inconcluso documentado, sin 0/1 ni AC

VALORACIÓN
[ ] AC aplicables identificados
[ ] Propiedades pertinentes comprobadas, sin subpuntuación
[ ] Evidencias y cobertura adecuadas para cada hallazgo
[ ] Materialidad razonada frente a la condición del AC
[ ] 0/1/2 o NA/NE por AC, con justificación

CONTROL E INFORME
[ ] Confrontadas identidades, condiciones y momentos
[ ] No se añadieron hechos comerciales no publicados
[ ] Las evidencias originales son reexaminables
[ ] Informe enlazado al expediente
[ ] Limitaciones y revisiones registradas
```

### Anexo B. Preguntas de revisión por AC

| AC | Pregunta decisiva antes de emitir el GSC |
|---|---|
| **Concreción** | ¿Los componentes sustantivos y el detalle del RI están suficientemente cubiertos? |
| **Precisión** | ¿Puede interpretarse inequívocamente el significado pertinente, sin lecturas materialmente alternativas? |
| **Aplicabilidad** | ¿Cada afirmación necesaria se atribuye a la entidad y las condiciones concretas del RI? |
| **Comparabilidad** | ¿Puede realizarse el contraste requerido sobre bases equivalentes o equivalencias justificadas? |
| **Fiabilidad** | ¿Qué pruebas sustentan corrección, vigencia y coherencia; qué quedó realmente acreditado? |
| **Justificación** | ¿La respuesta se sostiene y reconstruye con afirmaciones y relaciones de soporte identificables? |

### Anexo C. Glosario operativo

- **AC:** criterio de aceptación que juzga una condición específica de la capacidad informativa del RI.
- **Ámbito:** conjunto de representaciones admisibles para una evaluación: Catálogos distribuidos, Web o Web Schema.org.
- **Candidato:** elemento localizado cuya contribución al RI está por comprobar.
- **Componente del RI:** necesidad de conocimiento sustantiva o auxiliar de la cuestión formulada.
- **Cobertura:** alcance de inspección y comprobación que sustenta una conclusión; depende de la naturaleza del juicio.
- **Disponibilidad efectiva:** existencia binaria de información pertinente efectivamente obtenible y legible en el ámbito/perfil.
- **Evidencia:** contenido o resultado obtenido mediante una comprobación identificable que sustenta una observación.
- **GSC:** grado ordinal 0/1/2 de satisfacción de un AC, con estados NA y NE diferenciados.
- **Hallazgo:** interpretación fundamentada de una condición favorable o limitación observada, vinculada a propiedad/AC/RI.
- **Información pertinente:** elemento con contribución funcional identificable y justificable a una necesidad constitutiva del RI; puede ser parcial.
- **NE:** AC aplicable para el que no se dispone de evidencia suficiente para un juicio fundado.
- **Perfil del RI:** caracterización operativa de la pregunta, sus componentes, entidades, desagregación, condiciones y posibles funciones resolutivas.
- **Perfil de consumo:** condiciones bajo las que el recurso se obtiene y lee en un ámbito.
- **Propiedad de calidad:** característica observable P06–P18 que permite fundamentar hallazgos, sin puntuación propia.
- **Ruta de respuesta:** conjunto de afirmaciones y relaciones sustentadas con las que puede reconstruirse una conclusión; no tiene escala de longitud o esfuerzo.

### Anexo D. Reglas de revisión documental y versionado

1. Mantener este documento como **procedimiento general**; dejar en el catálogo de demanda los perfiles concretos de RI y en el expediente los resultados de cada ecommerce.
2. Identificar los cambios de anclaje GSC, cobertura o exigencia de evidencia y sus efectos en evaluaciones anteriores.
3. Versionar perfiles RI cuando cambien objeto, componentes sustantivos, desagregación, condiciones o aplicabilidad.
4. Versionar el perfil de consumo cuando cambien las representaciones o vías admitidas; no comparar resultados de distintos perfiles sin advertirlo.
5. Anotar las reglas que cambien tras calibración y actualizar los casos de prueba afectados.
6. Convertir las reglas de este marco en instrucciones de Skill **solo después de probarlas** con expedientes reproducibles.

---

## Fuentes internas utilizadas y advertencia final

Este marco se ha preparado a partir de las definiciones y desarrollos del propio proyecto: `Contexto_marco_de_estudio.md`, `Conceptos_base_sistema_de_estudio.md`, `Fundamentos_consolidados_calidad_de_la_informacion_comercial.md`, `Fundamento_metodologico_IA_y_calidad_informativa.md` y `Estrategia_metodologica_RI_localizacion_pertinencia_evidencias_GSC.md`, junto con las decisiones expresamente debatidas.

**Advertencia de aprobación:** el documento está **completo como borrador operativo transversal para pilotaje**, no como norma metodológica ya validada. Las fichas, anclajes, requisitos de evidencia, criterios de cobertura y formatos de intercambio constituyen **propuestas V1** sujetas a calibración. Las definiciones rectoras y escalas vigentes mantienen su precedencia. El siguiente paso lógico es **probar el procedimiento completo** con RI variados y ajustar las fronteras de decisión, no rediseñar el modelo conceptual ni introducir nuevas puntuaciones.
