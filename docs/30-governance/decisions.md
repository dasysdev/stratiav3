---
id: decisions
title: Registro de decisiones
layer: governance
status: vigente
version: 1.0
updated: 2026-10-28
sources: [GSC0 §18.4]
---

# Registro de decisiones

Registro **de solo adición**. Una decisión no se borra: se marca como `sustituida por D-NNN`.

**Estados:** `propuesta` · `aceptada` · `provisional` (aplicada a falta de confirmación) · `sustituida` · `rechazada`.

**Plantilla:**

```markdown
### D-NNN
**Título.** · Estado · Fecha
- **Contexto:** …
- **Decisión:** …
- **Consecuencias:** módulos afectados, efectos sobre evaluaciones previas.
- **Relacionado:** I-NN, OQ-NN.
```

| ID | Título | Estado | Fecha |
|---|---|---|---|
| [D-001](#d-001) | Documentación modular por capas | aceptada | 2026-10-24 |
| [D-002](#d-002) | Archivo v0 inmutable como línea base | aceptada | 2026-10-24 |
| [D-003](#d-003) | Denominaciones canónicas de indicadores | aceptada | 2026-10-24 |
| [D-004](#d-004) | «Ámbito de evaluación» como término de la unidad evaluada | sustituida por D-010 | 2026-10-24 |
| [D-005](#d-005) | Precedencia por capas | aceptada | 2026-10-24 |
| [D-006](#d-006) | Decisiones metodológicas explícitamente no adoptadas (V1) | aceptada | 2026-10-24 |
| [D-007](#d-007) | Las propiedades de calidad son exclusivamente informativas; P01–P05 retirados | aceptada | 2026-10-24 |
| [D-008](#d-008) | Antecedentes documentales no incorporados | aceptada | 2026-10-24 |
| [D-009](#d-009) | Dos vías de construcción del modelo de demanda: taxonomía y MPIR | aceptada (ampliada por D-036; enmendada por D-039; vía PAA y MPIR aparcado: D-094, D-095) | 2026-10-24 |
| [D-010](#d-010) | «Interfaz» y «ámbito» son sinónimos en la unidad de evaluación | aceptada | 2026-10-24 |
| [D-011](#d-011) | Nombre del proyecto: stratia.cic | aceptada | 2026-10-24 |
| [D-012](#d-012) | Denominación «Taxonomía de clases de producto» | aceptada | 2026-10-24 |
| [D-013](#d-013) | Tres ámbitos de evaluación también en CTX | aceptada | 2026-10-24 |
| [D-014](#d-014) | P07 en las asociaciones orientativas de Aplicabilidad | aceptada | 2026-10-24 |
| [D-015](#d-015) | Intake de updates y skill `docs-update` | aceptada (modificada por D-016) | 2026-10-24 |
| [D-016](#d-016) | El intake prevalece; aplicación sin aprobación previa | aceptada (estado «vigente» precisado por D-070) | 2026-10-24 |
| [D-017](#d-017) | Escala del IR: 0–10 | aceptada | 2026-10-24 |
| [D-018](#d-018) | Prominencia informativa, IP y calidad ajustada (propuesta) | aceptada | 2026-10-24 |
| [D-019](#d-019) | Estado binario de resolución = «suficientemente resuelto» de la TRI | aceptada | 2026-10-24 |
| [D-020](#d-020) | Clase de estudio: clase general más especializaciones relevantes | aceptada (precisada por D-033) | 2026-10-24 |
| [D-021](#d-021) | Shopify fija el eje de base de la clase general | aceptada (modificada por D-023) | 2026-10-24 |
| [D-022](#d-022) | Criterio de especialización: cinco condiciones y evidencia | aceptada (precisada por D-024 y D-026, ampliada por D-025; condición 1 enmendada por D-027; matizada por D-041; validación precisada por D-044; condición 1 restablecida por D-048) | 2026-10-24 |
| [D-023](#d-023) | Composición de la clase de estudio por categorías y piezas | aceptada (modificada por D-028, precisada por D-029; alcance de «juego» enmendado por D-086) | 2026-10-25 |
| [D-024](#d-024) | Condición 4 del criterio de especialización: lectura estricta | aceptada (precisada por D-029 y D-030) | 2026-10-25 |
| [D-025](#d-025) | Beneficios reclamados: no son especializaciones | aceptada (precisada por D-031) | 2026-10-25 |
| [D-026](#d-026) | Regla de las cuestiones propias para dimensiones que todo producto tiene | aceptada (precisada por D-029 y D-030; consecuencia del sofá cama revisada por D-032; ampliada por D-037) | 2026-10-25 |
| [D-027](#d-027) | La condición 1 incluye la oferta: especializaciones de oferta | sustituida por D-048 (ejemplo de outlet sustituido antes por D-037) | 2026-10-25 |
| [D-028](#d-028) | Clasificación objetiva: una categoría entra aunque no aporte requisitos | aceptada (precisada por D-032 y D-033: alias) | 2026-10-25 |
| [D-029](#d-029) | Base de una categoría de Shopify: atributos propios y de sus madres | aceptada | 2026-10-25 |
| [D-030](#d-030) | Características especiales de un PTD: dimensiones de la base y apoyo | aceptada | 2026-10-25 |
| [D-031](#d-031) | El material reciclado es especialización, no beneficio reclamado | aceptada | 2026-10-25 |
| [D-032](#d-032) | Propósito de la clase de estudio: los requisitos informativos | aceptada (precisada por D-033) | 2026-10-25 |
| [D-033](#d-033) | Identidad del modelo de demanda: composición de bloques de requisitos | aceptada (formato y denominación fijados por D-038; precisada por D-040 y D-057; la aplicación pasa a la oferta por D-047) | 2026-10-25 |
| [D-034](#d-034) | Capa general de requisitos: universales y condicionados | aceptada (borrador revisado por D-038; importancias fijas por D-045; elementos digitales al modelo por D-047; pregunta universal de promociones por D-049; fabricante, origen y seguridad por D-052; formulación dividida por D-065; bloques condicionados de garantía comercial, posventa y opiniones por D-066; pregunta del precio personalizado retirada por D-067; los cambios en `gen/11` y `gen/26` por D-085) | 2026-10-25 |
| [D-035](#d-035) | Pruebas operativas de importancia relativa | aceptada (la duda no baja la importancia ni excluye: D-050) | 2026-10-25 |
| [D-036](#d-036) | Cuestiones inferidas: tercera vía de construcción, provisional | aceptada (régimen: lectura de Claude no objetada; matizada por D-041; enmendada por D-044; con fuente, propuesta al bloque por D-088; confirmación por PAA: D-094) | 2026-10-25 |
| [D-037](#d-037) | Valores de oferta y activación de cuestiones condicionadas | aceptada (sin especializaciones de oferta por D-048; unidad de exposición precisada por D-057) | 2026-10-25 |
| [D-038](#d-038) | Catálogo de bloques: capa general contrastada, identificadores propios y denominación | aceptada (precisada por D-040; matizada por D-041; estados y clave enmendados por D-045; clave y nombre sin aplicación por D-047; sectores en el nombre por D-077) | 2026-10-25 |
| [D-039](#d-039) | Los PTD de Amazon, fuente de requisitos de la categoría | aceptada (precisada por D-044; ampliada por D-052: fuente también de la capa general) | 2026-10-25 |
| [D-040](#d-040) | Bloques de categoría deterministas y catálogo revisado | aceptada (matizada por D-041; precisada por D-044 y D-045) | 2026-10-25 |
| [D-041](#d-041) | Entrenamiento y ejecución: la revisión humana no bloquea la ejecución | aceptada (enmendada por D-044) | 2026-10-25 |
| [D-042](#d-042) | Capa original del MPIR: sin capturas de pantalla y políticas de acceso del motor | aceptada (motor compartido: D-046; renderizado siempre en el método: D-073; excepción del motor PAA: D-096) | 2026-10-25 |
| [D-043](#d-043) | Criterios de redacción del catálogo de bloques de categoría | aceptada (criterio 5 sustituido por D-044; criterio 1 precisado por D-051 y enmendado por D-055; reglas de formulación añadidas por D-060) | 2026-10-25 |
| [D-044](#d-044) | Marco humano y reglas inducidas: el usuario define el marco, no revisa reglas ni requisitos | aceptada (operación: D-045; «críticos pocos» retirado del marco por D-059) | 2026-10-25 |
| [D-045](#d-045) | Operación del entrenamiento, primera versión: rasgos, reglas de importancia por el árbol de Shopify y métricas | aceptada (relevancia inducida por D-050; vocabulario ampliado por D-051 y abierto por D-056; ejecución a escala enmendada por D-054; crítico por requisito y clase por D-055; excepciones por requisito y crítico de cualquier propiedad por D-058; información resolutiva inducida por D-063) | 2026-10-25 |
| [D-046](#d-046) | Motor de captura compartido por el MPIR y el entrenamiento del modelo de demanda | aceptada (primera selección: D-053; dónde vive el motor: D-150) | 2026-10-25 |
| [D-047](#d-047) | El modelo de demanda va con el producto; la aplicación, con la oferta | aceptada (tres disparadores nuevos por D-066; nombre con sectores por D-077) | 2026-10-25 |
| [D-048](#d-048) | La oferta no aporta requisitos: activa requisitos condicionados de la clase | aceptada | 2026-10-25 |
| [D-049](#d-049) | Pregunta universal de promociones y descuentos | aceptada | 2026-10-25 |
| [D-050](#d-050) | Filtro de relevancia aprendido: lo no relevante sale del modelo de la clase | aceptada | 2026-10-25 |
| [D-051](#d-051) | Peso, grosor y gramaje: rasgo «magnitud física», fuera de la regla de las medidas | aceptada (vocabulario abierto por D-056) | 2026-10-25 |
| [D-052](#d-052) | Fabricante, país de fabricación y seguridad en la capa general, según su origen | aceptada (ampliada a hechos de la oferta por D-065; ampliación sin efecto por D-066; fabricante con marca propia por D-080; la imagen, por D-144) | 2026-10-25 |
| [D-053](#d-053) | Catálogo de entrenamiento, primera selección: El Corte Inglés, amplitud de tipos y piloto | aceptada (primera vía de entrada del catálogo curado por D-158) | 2026-10-25 |
| [D-054](#d-054) | El entrenamiento a escala clasifica con agentes de Claude Code, no con la API | aceptada | 2026-10-25 |
| [D-055](#d-055) | Crítico por requisito y clase; la medida descriptiva puede ser crítica | aceptada (generalizada por D-058) | 2026-10-26 |
| [D-056](#d-056) | Vocabulario de rasgos abierto: rasgos propuestos y votados por los agentes | aceptada (criterio de crítico sustituido por D-058) | 2026-10-26 |
| [D-057](#d-057) | Composición y aplicación: hoja más específica, hermana como alias y unidad de exposición | aceptada (unidad de exposición precisada por D-079) | 2026-10-26 |
| [D-058](#d-058) | Excepciones de importancia por requisito y clase en cualquier propiedad, también para el crítico | aceptada | 2026-10-26 |
| [D-059](#d-059) | «Críticos pocos» no es un objetivo del marco | aceptada | 2026-10-26 |
| [D-060](#d-060) | Formulación de las cuestiones del catálogo: condiciones, una necesidad por requisito y componentes con fuente | aceptada (aplicada a la capa general por D-065; la regla 3 prevalece sobre la forma de sí o no por D-087) | 2026-10-26 |
| [D-061](#d-061) | Tipos de información potencialmente resolutiva: forma de la respuesta, con vocabulario cerrado | sustituida por D-062 | 2026-10-26 |
| [D-062](#d-062) | Información resolutiva: los tipos de información que pueden resolver cada requisito, para localizar y recomendar | aceptada (reglas del motor: D-063; entradas renombradas «aportación resolutiva» por D-064) | 2026-10-26 |
| [D-063](#d-063) | Información resolutiva: cuatro orígenes compilados por el entrenamiento y aceptación en dos tiendas distintas | aceptada (entradas renombradas «aportación resolutiva» por D-064; en la capa general, las que se redactan sin apoyo en la ley son inferidas por D-065; la norma de un requisito de categoría da referencias por D-068; listas de la capa general sin aprobación del usuario por D-084) | 2026-10-26 |
| [D-064](#d-064) | «Aportación resolutiva»: nombre de cada entrada de la información resolutiva | aceptada (siempre con su adjetivo por D-075; el plazo de cambio aporta a `gen/11` por D-085) | 2026-10-26 |
| [D-065](#d-065) | Formulación de la capa general: reglas de D-060, también para las partes de igual importancia, y aportaciones sin ley como inferidas | aceptada (condicionados de la oferta en bloques propios por D-066; `gen.precio-personalizado/01` retirada por D-067; listas de información resolutiva aprobadas por D-069) | 2026-10-26 |
| [D-066](#d-066) | Garantía comercial, asistencia posventa y opiniones publicadas: bloques condicionados de la capa general | aceptada (solo opiniones del producto u oferta por D-076; garantía sin contenido por D-081) | 2026-10-26 |
| [D-067](#d-067) | Se retira la pregunta del precio personalizado que repite su disparador | aceptada | 2026-10-26 |
| [D-068](#d-068) | La norma que es fuente de un requisito de categoría da aportaciones de origen «referencias» | aceptada | 2026-10-26 |
| [D-069](#d-069) | Información resolutiva de la capa general aprobada | sustituida por D-084 en la aprobación de las listas (`gen/17` ampliada por D-080) | 2026-10-26 |
| [D-070](#d-070) | El estado «vigente» incluye lo que un intake procesado formula como vigente | aceptada | 2026-10-26 |
| [D-071](#d-071) | Casos de taxonomía corregidos: polar, tapicería de piel y `warmth-level` | aceptada | 2026-10-26 |
| [D-072](#d-072) | El efecto de la relevancia sobre la base de D-030 lo mide la validación automática | aceptada | 2026-10-26 |
| [D-073](#d-073) | En el MPIR se renderiza siempre con un navegador real | aceptada | 2026-10-26 |
| [D-074](#d-074) | Mensajes comunes de la tienda: cuentan si fijan una condición comprobable para la oferta | aceptada (descuento condicionado precisado por D-078) | 2026-10-26 |
| [D-075](#d-075) | «Aportación» siempre con su complemento: resolutiva o al modelo de demanda | aceptada | 2026-10-26 |
| [D-076](#d-076) | Solo las opiniones del producto o de la oferta cuentan como opiniones publicadas | aceptada | 2026-10-26 |
| [D-077](#d-077) | El nombre del modelo de demanda muestra la composición completa, con los sectores | aceptada | 2026-10-26 |
| [D-078](#d-078) | Un descuento de toda la tienda activa `gen.descuento` aunque dependa de una acción del comprador | aceptada | 2026-10-26 |
| [D-079](#d-079) | La ficha identifica la unidad de exposición cuando sitúa en la exposición la unidad que se vende | aceptada | 2026-10-26 |
| [D-080](#d-080) | Quien comercializa el producto con su nombre o marca responde la pregunta del fabricante | aceptada | 2026-10-26 |
| [D-081](#d-081) | Una garantía nombrada sin contenido ni condiciones no activa `gen.garantia-comercial` | aceptada | 2026-10-26 |
| [D-082](#d-082) | Varias opciones visibles en un selector activan `gen.variantes`; una sola, no | aceptada | 2026-10-26 |
| [D-083](#d-083) | Política de cambios: bloque condicionado `gen.cambios` de la capa general | sustituida por D-085 | 2026-10-26 |
| [D-084](#d-084) | La información resolutiva de la capa general no requiere la aprobación del usuario | aceptada | 2026-10-26 |
| [D-085](#d-085) | Los cambios son condiciones de devolución y cambio: van en `gen/11` y `gen/26`, no en la aplicación | aceptada | 2026-10-26 |
| [D-086](#d-086) | La especialización «juego» aporta qué piezas incluye y cuántas de cada una; las medidas, los bloques de cada pieza | aceptada | 2026-10-26 |
| [D-087](#d-087) | La regla 3 prevalece sobre la forma de sí o no con detalle | aceptada | 2026-10-26 |
| [D-088](#d-088) | Una cuestión con fuente que el bloque ni pregunta ni excluye es una propuesta al bloque | aceptada | 2026-10-26 |
| [D-089](#d-089) | Precio anterior y precio por unidad de medida en la capa general, con su norma | aceptada | 2026-10-26 |
| [D-090](#d-090) | Derivar una prestación de un atributo no resuelve el requisito de la prestación | aceptada (enmendada por D-119) | 2026-10-27 |
| [D-091](#d-091) | Un criterio de elección genera un requisito cuando cumple las condiciones C1–C4 | aceptada | 2026-10-27 |
| [D-092](#d-092) | Los requisitos informativos llevan una descripción de tres partes | aceptada | 2026-10-27 |
| [D-093](#d-093) | La descripción es prosa y no repite la información resolutiva | aceptada | 2026-10-27 |
| [D-094](#d-094) | People Also Ask (PAA): vía de construcción del modelo de demanda | aceptada (propone requisitos nuevos: D-099) | 2026-10-27 |
| [D-095](#d-095) | El MPIR queda aparcado | aceptada | 2026-10-27 |
| [D-096](#d-096) | Excepción a D-042: el motor PAA no aplica el robots.txt de Google | aceptada | 2026-10-27 |
| [D-097](#d-097) | Origen «paa» para los requisitos que entran solo por PAA | aceptada (también desde preguntas factuales: D-099) | 2026-10-27 |
| [D-098](#d-098) | La construcción del modelo de demanda pasa a un módulo propio | aceptada | 2026-10-27 |
| [D-099](#d-099) | PAA propone requisitos nuevos, también desde preguntas factuales | aceptada | 2026-10-27 |
| [D-100](#d-100) | Lectura sobre la oferta de las preguntas PAA de clase | aceptada (enmendada por D-141: el perímetro va antes) | 2026-10-27 |
| [D-101](#d-101) | Confirmaciones y aportaciones de precisión que salen de PAA | aceptada | 2026-10-27 |
| [D-102](#d-102) | Basta una pregunta para apoyar un candidato de PAA | aceptada | 2026-10-27 |
| [D-103](#d-103) | Separación por dimensión en los atributos de lista | aceptada (precisada por D-109) | 2026-10-27 |
| [D-104](#d-104) | Criterios de elección intermedios; PAA y la pertinencia de los AC, en propuesta | aceptada (pertinencia de los AC adoptada por D-115) | 2026-10-27 |
| [D-105](#d-105) | Tacto por tipo y rasgo «sensorial» | aceptada (precisada por D-110) | 2026-10-27 |
| [D-106](#d-106) | Un requisito de certificación cubre la prestación cuya declaración recoge | aceptada (salvo dimensión: D-109) | 2026-10-27 |
| [D-107](#d-107) | Requisitos repetidos en bloques hermanos: misma pregunta y misma descripción | aceptada | 2026-10-27 |
| [D-108](#d-108) | Candidatos PAA de la clase de sábanas | aceptada (piel: D-113) | 2026-10-27 |
| [D-109](#d-109) | Precisiones de la separación por dimensión | aceptada (ejemplo de la piel retirado: D-113) | 2026-10-27 |
| [D-110](#d-110) | Preguntas de grado: C2 se juzga sobre el requisito | aceptada | 2026-10-27 |
| [D-111](#d-111) | Sujeción de la bajera, candidato PAA | sustituida por D-112 | 2026-10-27 |
| [D-112](#d-112) | Sujeción de la bajera: cubierta | aceptada | 2026-10-27 |
| [D-113](#d-113) | Piel en sábanas: cubierta | aceptada | 2026-10-27 |
| [D-114](#d-114) | Entrenamiento propio de PAA: qué refina, sus límites y el piloto de medición | aceptada (clases del piloto: D-116) | 2026-10-27 |
| [D-115](#d-115) | El entrenamiento de PAA escribe en el catálogo: cuatro papeles y un solo escritor por requisito | aceptada (papel 2 precisado por D-125) | 2026-10-27 |
| [D-116](#d-116) | Clases del piloto de PAA: las de los 14 casos de referencia | aceptada | 2026-10-27 |
| [D-117](#d-117) | Los criterios de aceptación se aplican siempre; NE es una incidencia | aceptada (NA de Comparabilidad: D-126) | 2026-10-27 |
| [D-118](#d-118) | Comparabilidad: el contraste se exige cuando la respuesta es una dimensión de comparación de la clase | aceptada | 2026-10-27 |
| [D-119](#d-119) | La prestación derivada de un atributo se decide en la pertinencia | aceptada | 2026-10-27 |
| [D-120](#d-120) | Prueba de derivación: conclusión necesaria con reglas generales, descriptivas y citadas | aceptada (el hecho particular tomado de fuera, enmendado por D-154) | 2026-10-27 |
| [D-121](#d-121) | Fiabilidad: nueva definición y lectura refutadora | aceptada | 2026-10-27 |
| [D-122](#d-122) | Comprobaciones de corrección: tres familias, límites del conocimiento del dominio e identificador ausente | aceptada (familias y fuente independiente, enmendadas por D-154) | 2026-10-27 |
| [D-123](#d-123) | Se retira la propiedad P15 · Actualidad | aceptada | 2026-10-27 |
| [D-124](#d-124) | Consistencia transversal: nueva dimensión de análisis por RI × par de ámbitos | aceptada | 2026-10-27 |
| [D-125](#d-125) | Pistas de valoración: nombre, tres niveles y alcance | aceptada | 2026-10-27 |
| [D-126](#d-126) | Marca de dimensión de comparación y NA de Comparabilidad | aceptada (cómo se fija: D-139) | 2026-10-27 |
| [D-127](#d-127) | Quién escribe las pistas de valoración | aceptada (dónde viven: D-134, D-140) | 2026-10-27 |
| [D-128](#d-128) | Las pistas de valoración son criterios breves apoyados en las propiedades, no listas | aceptada | 2026-10-27 |
| [D-129](#d-129) | web-audit: sistema de la evaluación técnica de Web y Web Schema.org | aceptada | 2026-10-27 |
| [D-130](#d-130) | Perfil de implementación: definición y tres niveles en Web Schema.org | aceptada (nivel del consumidor enmendado por D-145) | 2026-10-27 |
| [D-131](#d-131) | Estados del requisito técnico | aceptada | 2026-10-27 |
| [D-132](#d-132) | Solo una especificación aplicable fundamenta un requisito técnico | aceptada | 2026-10-27 |
| [D-133](#d-133) | Referencia técnica en web-audit: datos gobernados por el canon, decididos por los agentes | aceptada (las fuentes congeladas, en references: D-149) | 2026-10-27 |
| [D-134](#d-134) | Catálogo de pistas con destinatario; encontrarlas es código | aceptada (enmendada por D-140: las pistas de un requisito viven en él) | 2026-10-27 |
| [D-135](#d-135) | Campos de una pista de valoración, quién escribe las dirigidas a una fuente y cómo llegan al auditor | aceptada (precisada por D-140: `para`) | 2026-10-27 |
| [D-136](#d-136) | Gobierno de las pistas de valoración: aceptación, duplicadas, retiradas y orígenes | aceptada | 2026-10-27 |
| [D-137](#d-137) | Cuándo se definen las pistas de valoración | aceptada | 2026-10-27 |
| [D-138](#d-138) | Pistas de valoración: niveles no exclusivos, sin ámbito, trazabilidad y versión | aceptada | 2026-10-27 |
| [D-139](#d-139) | Cómo se fija la marca de dimensión de comparación | aceptada | 2026-10-27 |
| [D-140](#d-140) | Las pistas dirigidas a un requisito viven en el requisito | aceptada | 2026-10-27 |
| [D-141](#d-141) | Productos vecinos fuera del perímetro de PAA, antes de la lectura sobre la oferta | aceptada (madre y material: D-146) | 2026-10-28 |
| [D-142](#d-142) | Moda, popularidad, preferencia general y alternativa de producto en PAA | aceptada | 2026-10-28 |
| [D-143](#d-143) | Mínimo de representación de la oferta | aceptada (papel del mínimo precisado por D-145; datos en Web Schema.org, D-147) | 2026-10-28 |
| [D-144](#d-144) | La imagen: sostén del mínimo de representación; lo que muestra no es información | aceptada | 2026-10-28 |
| [D-145](#d-145) | Frontera entre la evaluación técnica y la informativa: decide la naturaleza que fija la especificación | aceptada (mínimo fijado por D-147; completitud y excepción precisadas por D-148; destino de lo recomendado precisado por D-155) | 2026-10-28 |
| [D-146](#d-146) | La categoría madre y el material en el perímetro de PAA | aceptada | 2026-10-28 |
| [D-147](#d-147) | Datos del mínimo de representación en Web Schema.org | aceptada | 2026-10-28 |
| [D-148](#d-148) | Formación estructural | aceptada | 2026-10-28 |
| [D-149](#d-149) | Sistema references: custodia común de las fuentes externas congeladas | aceptada | 2026-10-28 |
| [D-150](#d-150) | Sistema capture: motor de captura y almacén común de fichas congeladas | aceptada | 2026-10-28 |
| [D-151](#d-151) | Perfil de consumo base de Web: la respuesta HTTP sin ejecutar JavaScript | aceptada (segundo perfil retirado por D-156) | 2026-10-28 |
| [D-152](#d-152) | Ámbitos de la V1 de la auditoría informativa: Web y Web Schema.org | aceptada | 2026-10-28 |
| [D-153](#d-153) | Ejecución del auditor en dos fases: disponibilidad por ficha × ámbito, AC por lotes | propuesta | 2026-10-28 |
| [D-154](#d-154) | Fiabilidad sin fuentes externas y conocimiento del modelo como regla asimétrica | aceptada | 2026-10-28 |
| [D-155](#d-155) | Un modelo de demanda y una ficha por ámbito: pertinencia por excepción y localización | aceptada | 2026-10-28 |
| [D-156](#d-156) | Un solo perfil de consumo: sin JavaScript y con todo el documento | aceptada | 2026-10-28 |
| [D-157](#d-157) | Contexto de la petición del perfil de consumo y datos en scripts que no son marcado | aceptada (estado limpio precisado por D-163) | 2026-10-28 |
| [D-158](#d-158) | Catálogo de entrenamiento curado: candidatos, filtros, motivos de admisión, topes y casos manuales | aceptada | 2026-10-28 |
| [D-159](#d-159) | Perfil de implementación de Web: protocolo, documento y consumidor (Google Search y operadores de IA) | aceptada (enmendada por D-168: Open Graph en el nivel de documento) | 2026-10-28 |
| [D-160](#d-160) | Frontera entre la evaluación técnica y la informativa en Web | aceptada | 2026-10-28 |
| [D-161](#d-161) | Vistas general y particular de la evaluación técnica; tipos de página | aceptada | 2026-10-28 |
| [D-162](#d-162) | Descubribilidad: toda página auditada está en los sitemaps (condición del proyecto) | aceptada | 2026-10-28 |
| [D-163](#d-163) | Cómo cumple la captura el perfil de consumo: JavaScript desactivado y un contexto de navegador nuevo por ficha | aceptada | 2026-10-28 |
| [D-164](#d-164) | Las unidades de un conjunto no son partes de la cuestión: las valoran los AC | aceptada | 2026-10-28 |
| [D-165](#d-165) | Envío y plazos por zona de España en la capa general; impuestos y aduana de Canarias, Ceuta y Melilla | aceptada | 2026-10-28 |
| [D-166](#d-166) | Tasa de cumplimiento técnico: una sola tasa con desglose por naturaleza y cobertura; agregación por tipo de página | aceptada | 2026-10-28 |
| [D-167](#d-167) | Páginas de una auditoría: fichas del encargo, portada, políticas, categoría inmediata, robots.txt y sitemaps | aceptada | 2026-10-28 |
| [D-168](#d-168) | Mínimo de representación de Web: url, título y URL canónica; Open Graph condicional en el perfil de Web | aceptada | 2026-10-28 |

---

### D-001

**Documentación modular por capas.** · aceptada · 2026-10-24

- **Contexto:** el corpus v0 (~310 KB) repetía definiciones en 3–4 documentos y mezclaba normativa, fundamento, procedimiento y pendientes. Ya habían aparecido divergencias ([I-01](issues.md#i-01), [I-08](issues.md#i-08)).
- **Decisión:** reorganizar en capas (`00-context`, `10-model`, `20-methods`, `30-governance`) con módulos por tema de 80–250 líneas, una sola fuente de verdad por concepto y un glosario como capa de enrutamiento. Se descartaron los documentos íntegros con índice (no resuelven la deriva) y la atomización por concepto (fragmenta las relaciones; vocabulario aún en calibración).
- **Consecuencias:** las reglas de mantenimiento están en [docs/CLAUDE.md](../CLAUDE.md) y la validación en `tools/check_docs.py`.

### D-002

**Archivo v0 inmutable como línea base.** · aceptada · 2026-10-24

- **Contexto:** el proyecto no usa control de versiones por ahora.
- **Decisión:** copiar los originales a `docs/archive/v0-2026-10-24/` en modo solo lectura. `tmp/docs/` se conserva hasta que el propietario decida eliminarlo.
- **Actualización (2026-10-24):** el propietario eliminó `tmp/docs/`. `docs/archive/v0-2026-10-24/` es ahora la única copia de los originales.
- **Consecuencias:** cada módulo traza sus fuentes v0 en el frontmatter `sources`. Las líneas base futuras se archivan como carpetas nuevas.

### D-003

**Denominaciones canónicas de indicadores.** · aceptada · 2026-10-24

- **Contexto:** [I-01](issues.md#i-01).
- **Decisión:** usar las denominaciones de BASE (IR, ICI, **TRI**, **Tasa de cumplimiento técnico**) con los alias de FUND.
- **Consecuencias:** [scoring-systems](../10-model/scoring-systems.md).
- **Confirmación (2026-10-24):** el propietario la confirma como definitiva. Cierra I-01.

### D-004

**«Ámbito de evaluación» como término de la unidad evaluada.** · sustituida por [D-010](#d-010) · 2026-10-24

- **Contexto:** [I-03](issues.md#i-03).
- **Decisión:** en texto nuevo, la unidad informativa se expresa como **RI × ámbito**, alineado con GSC0 y con el uso mayoritario en FUND §5.1 y §8.6; ambos términos conviven dentro de BASE y FUND. «Interfaz» designa el medio técnico. Las citas literales de BASE y FUND se conservan tal cual y se marcan con ⚠ I-03.
- **Consecuencias:** módulos de `10-model/` y `20-methods/audit-gsc/`.

### D-005

**Precedencia por capas.** · aceptada · 2026-10-24

- **Contexto:** en v0, la precedencia se definía por documento (CTX y BASE rectores; FUND interpretativo; métodos subordinados).
- **Decisión:** `00-context` y `10-model` contienen el canon (citas literales de CTX/BASE más desarrollo de FUND) y prevalecen sobre `20-methods`. Los métodos no pueden introducir conceptos, criterios, propiedades, escalas, pesos ni indicadores. Dentro del canon, una cita literal de CTX/BASE prevalece sobre la interpretación de FUND.
- **Consecuencias:** [docs/CLAUDE.md](../CLAUDE.md#capas-y-precedencia).

### D-006

**Decisiones metodológicas explícitamente no adoptadas (V1).** · aceptada · 2026-10-24

- **Contexto:** línea base heredada de GSC0 §18.4.
- **Decisión.** **No se adopta:**
  - una escala de «grado o número de derivaciones» para decidir pertinencia o GSC;
  - reglas que penalicen automáticamente respuestas obtenidas mediante relaciones justificadas;
  - una lista universal de campos obligatorios ni una equivalencia entre pertinencia y coincidencia literal;
  - nuevas puntuaciones para las propiedades P06–P18 ni promedios automáticos para el GSC;
  - una disponibilidad efectiva ternaria (un proceso inconcluso se registra fuera de la escala binaria);
  - inferir falsedad de la ausencia de corroboración, ni verdad de la ausencia de contradicciones;
  - mezclar información de Web Schema.org con HTML ajeno al marcado como contenido resolutivo de ese ámbito;
  - trasladar los requisitos técnicos directamente a descuentos del GSC;
  - calcular IR/ICI con fórmulas no establecidas;
  - interpretar un GSC como probabilidad de recomendación, de conversión o de éxito de una IA concreta.
- **Consecuencias:** son invariantes de trabajo, recogidas en el `CLAUDE.md` raíz.

### D-007

**Las propiedades de calidad son exclusivamente informativas; P01–P05 retirados.** · aceptada · 2026-10-24

- **Contexto:** [I-08](issues.md#i-08) e [I-05](issues.md#i-05).
  - BASE §5.3 decía que las propiedades fundamentan también «los requisitos técnicos generales». Eso contradecía BASE §3.1 y FUND §4.2 y §5.2.
  - El origen es la arquitectura anterior. El antecedente «Calidad de representación de oferta comercial» (21/10/2026) y el registro de cambio «Perspectivas de evaluación v1.3» (20/10/2026) daban a las propiedades doble función: diagnóstico técnico por interfaz y fundamentación de indicadores.
  - Esa arquitectura incluía cinco propiedades técnicas: **P01 Localizabilidad, P02 Distribución efectiva, P03 Recuperabilidad, P04 Legibilidad técnica y P05 Conformidad técnica**.
  - Los documentos del 24/10 retiraron esa función, y la frase de BASE §5.3 quedó como residuo.
- **Decisión:**
  - Se enmienda la definición canónica de BASE §5.3, eliminando «y los requisitos técnicos generales».
  - Las propiedades pertenecen solo al modelo informativo. La evaluación técnica se basa en los requisitos técnicos generales y en su sistema cuantitativo propio.
  - Los IDs **P01–P05 quedan retirados** y no se reutilizan.
  - El contenido de P03 y P04 (obtención y legibilidad) pervive como condición dentro de la [disponibilidad efectiva](../10-model/effective-availability.md), no como propiedad.
- **Consecuencias:** [quality-properties](../10-model/quality-properties.md) pasa a la versión 1.1. El archivo v0 conserva el texto original de BASE §5.3. Cierra I-05 e I-08.
- **Alternativa descartada:** recuperar P01–P05 para el diagnóstico técnico por interfaz. Revertía la decisión más reciente, reiterada en BASE §3.1, FUND §4.2 y FUND §5.2.

### D-008

**Antecedentes documentales no incorporados.** · aceptada · 2026-10-24

- **Contexto:** [I-06](issues.md#i-06).
  - FUND y GSC0 citan tres documentos de apoyo.
  - Solo se localizó «Calidad de representación de oferta comercial», fuera del proyecto: `Downloads/Idea_general_calidad_representacion_oferta_comercial.md`.
  - Junto a él están otros antecedentes del mismo linaje que no se citan: `Sistema_de_evaluacion.md`, con el sistema anterior de 7 indicadores, escala 0–3, pesos y bandas, y los registros de cambio v1.3 (perspectivas) y v1.4 (importancia relativa).
  - «Fundamento metodológico… IA» y «Estrategia metodológica… RI/GSC» no existen en ningún lugar accesible.
- **Decisión:**
  - Los antecedentes **no se incorporan** al proyecto.
  - Los dos documentos no encontrados se registran como **no disponibles**; su contenido se considera absorbido por FUND y GSC0.
  - Las correspondencias entre los nombres de fichero citados y los reales son las de la tabla de claves v0 de [docs/CLAUDE.md](../CLAUDE.md#frontmatter-obligatorio-todo-md-salvo-archive-y-este-fichero).
- **Consecuencias:** las citas a esos documentos en el archivo v0 son solo históricas. Ningún módulo depende de ellos. Cierra I-06.

### D-009

**Dos vías de construcción del modelo de demanda: taxonomía y MPIR.** · aceptada · 2026-10-24

- **Contexto:** [I-02](issues.md#i-02).
  - BASE §4.2 citaba como fuentes la Shopify Product Taxonomy y la información de ecommerce referentes.
  - Los marcos TAX y MPIR desarrollan dos vías: una taxonomía propia, que integra Shopify, Amazon y Google, y el MPIR.
- **Decisión:** se enmienda BASE §4.2 en el canon. El catálogo se construye por inferencia a partir de **dos vías de referencia complementarias**:
  1. **Taxonomía de clases de producto.** La estructura principal es Shopify; Amazon (especialización) y Google (contraste) son fuentes **de apoyo de la taxonomía, no fuentes directas de RI**.
  2. **MPIR.** Información comercial publicada por ecommerce referentes.

  El recorrido de construcción (observar → inferir → formular y normalizar → justificar) no cambia.
- **Consecuencias:**
  - [demand-model](../10-model/demand-model.md) pasa a la versión 1.1.
  - Se retiran las marcas ⚠ I-02 de [product-taxonomy](../20-methods/product-taxonomy/README.md) y [mpir](../20-methods/mpir/README.md).
  - La denominación de la vía taxonómica sigue pendiente en [I-09](issues.md#i-09).

### D-010

**«Interfaz» y «ámbito» son sinónimos en la unidad de evaluación.** · aceptada · 2026-10-24

- **Contexto:** [I-03](issues.md#i-03). BASE y FUND alternan «RI × interfaz» y «RI × ámbito».
- **Decisión:**
  - En el contexto de la unidad de evaluación y de los sistemas de valoración, ambos términos son **sinónimos**: RI × interfaz ≡ RI × ámbito.
  - No hay incoherencia. Las citas literales se conservan sin marca.
  - En texto nuevo se prefiere «ámbito», por continuidad con GSC0 y el glosario.
  - Fuera de ese contexto, «interfaz de exposición» designa también el medio técnico de publicación.
- **Consecuencias:**
  - Sustituye a [D-004](#d-004).
  - Se retiran las marcas ⚠ I-03 de `10-model` y `20-methods`.
  - La propuesta de [I-04](issues.md#i-04) («2 interfaces y 3 ámbitos») deja de sostenerse y se reformula.

### D-011

**Nombre del proyecto: stratia.cic.** · aceptada · 2026-10-24

- **Contexto:** [I-07](issues.md#i-07). Los métodos TAX y MPIR usaban «Calidad de información v1» y el directorio se llama `stratiav3`.
- **Decisión:** el proyecto y su sistema de auditoría se denominan **stratia.cic** (stratia, calidad de información comercial). «Calidad de información v1» queda como denominación histórica del corpus v0. `stratiav3` es solo el nombre del directorio.
- **Consecuencias:** encabezado del `CLAUDE.md` raíz.

### D-012

**Denominación «Taxonomía de clases de producto».** · aceptada · 2026-10-24

- **Contexto:** [I-09](issues.md#i-09). TAX hablaba de «taxonomía de clases de producto» y MPIR de «Modelo de Taxonomía de Productos».
- **Decisión:** el nombre único es **Taxonomía de clases de producto**. Es el título del propio marco y encaja con «clase de producto u oferta» del canon.
- **Consecuencias:** se ajustan las menciones en [mpir](../20-methods/mpir/README.md), `concepts-architecture`, `interpretation-transfer` y `operation-validation`, y en [demand-model](../10-model/demand-model.md).

### D-013

**Tres ámbitos de evaluación también en CTX.** · aceptada · 2026-10-24

- **Contexto:** [I-04](issues.md#i-04). CTX §5 enumeraba dos ámbitos y BASE §3, tres. Con [D-010](#d-010) («interfaz» ≡ «ámbito» en la unidad de evaluación) dejaba de sostenerse la lectura «2 interfaces y 3 ámbitos».
- **Decisión:** se enmienda CTX §5 en el canon. Los ámbitos de evaluación son tres: **Catálogos distribuidos**, **Web** y **Web Schema.org**.
- **Consecuencias:** [scope](../00-context/scope.md) pasa a la versión 1.1 y se retira la marca ⚠ I-04 de [evaluation-scopes](../10-model/evaluation-scopes.md).

### D-014

**P07 en las asociaciones orientativas de Aplicabilidad.** · aceptada · 2026-10-24

- **Contexto:** [I-10](issues.md#i-10). La tabla de FUND §7.4 no incluía P07 en Aplicabilidad, aunque su texto lo admitía. GSC0 §10.3 sí lo incluía.
- **Decisión:** la tabla canónica asocia Aplicabilidad con P10, P11 y P12 y, **según el hallazgo**, también con P07. Las asociaciones siguen siendo orientativas, no cerradas ni automáticas.
- **Consecuencias:** [quality-properties](../10-model/quality-properties.md) pasa a la versión 1.2 y se retira la marca ⚠ I-10 de [property-checks](../20-methods/audit-gsc/property-checks.md).

### D-015

**Intake de updates y skill `docs-update`.** · aceptada · 2026-10-24

- **Contexto:** el propietario crea `docs/intake/` para depositar los artefactos que constituyen un update. Hace falta un procedimiento repetible para incorporarlos sin deriva ni cambios silenciosos.
- **Decisión:** los updates se procesan con la skill `/docs-update` (`.claude/skills/docs-update/SKILL.md`), que sigue estos pasos:
  1. Lectura del artefacto.
  2. Análisis de impacto (confirma, precisa, amplía, enmienda, contradice, nuevo concepto, cierra o abre pendiente, fuera de alcance).
  3. Plan y **aprobación del propietario**.
  4. Aplicación del flujo de cambio.
  5. Archivado del artefacto en `docs/archive/intake/AAAA-MM-DD-<slug>`, en solo lectura.
  6. Validación y, si hay cambios de canon, revisión independiente.

  Los artefactos archivados se citan como `INTAKE <stem>` en `sources`; el validador comprueba que existen. `docs/intake/` no es canon y queda fuera del validador.
- **Consecuencias:** se actualizan `docs/CLAUDE.md` (capa Intake, clave `INTAKE`, versionado), el `CLAUDE.md` raíz y `tools/check_docs.py`.
- **Precisión (2026-10-24):** a petición del propietario, **todo artefacto procesado se archiva** en `archive/intake/`, tanto si se aplica entero como en parte o se rechaza. El resultado consta en el changelog. Solo permanece en `intake/` lo pendiente o lo aplazado a petición expresa.

### D-016

**El intake prevalece; aplicación sin aprobación previa.** · aceptada · 2026-10-24

- **Contexto:** instrucción del propietario: «Todo intake prevalece sobre lo que hay. Sobreescribe. Por lo demás tú decides; no quiero gestionarlo».
- **Decisión:**
  - Lo que se deposita en `docs/intake/` **prevalece sobre todo el contenido existente**, incluidas las invariantes del `CLAUDE.md` raíz y las decisiones aceptadas, y lo sobrescribe.
  - La skill `/docs-update` decide y aplica **sin pedir aprobación**. Resuelve las ambigüedades con la interpretación más fiel al texto, las registra en la decisión correspondiente e informa al terminar.
  - Desaparece la vía de «rechazo»; se mantiene el aplazamiento a petición expresa.
- **Consecuencias:**
  - Modifica el paso de aprobación de [D-015](#d-015).
  - Se actualizan la skill, `docs/CLAUDE.md` (precedencia y flujo de cambio), `docs/intake/README.md` y el `CLAUDE.md` raíz.
  - Fuera del intake, las incoherencias se siguen registrando en `issues.md`.

### D-017

**Escala del IR: 0–10.** · aceptada · 2026-10-24

- **Contexto:** FUND §8.2 no fijaba escala ni fórmula del IR (invariante 7). El artefacto `INTAKE 2026-10-24-prominencia-informativa` afirma: «IR (0–10): mide la capacidad de resolución del RI mediante los criterios de aceptación. No se modifica».
- **Decisión:** el IR se expresa en **escala 0–10**. La fórmula de agregación de los GSC sigue sin fijar ([OQ-28](open-questions.md)). La regla «disponibilidad efectiva = 0 → IR = 0» es coherente con la escala.
- **Interpretación adoptada:** el artefacto presenta la escala como existente («no se modifica»), así que se incorpora como **vigente**, aunque el resto del artefacto sea provisional.
- **Consecuencias:** [scoring-systems](../10-model/scoring-systems.md) pasa a la versión 1.1. Se reformula la invariante 7 y se actualizan el glosario y OQ-28.
- **Sustituye:** la afirmación de FUND §8.2 de que no hay escala final del IR.

### D-018

**Prominencia informativa, IP y calidad ajustada (propuesta).** · aceptada · 2026-10-24

- **Contexto:** `INTAKE 2026-10-24-prominencia-informativa`, «propuesta metodológica provisional».
- **Decisión:** se incorporan con **estado propuesta**, en el nuevo módulo [informative-prominence](../10-model/informative-prominence.md):
  - la clasificación binaria de prominencia (HTML) por componente;
  - el IP (0–100 %, `100 × C/N`, NA si N = 0);
  - la calidad ajustada (modificador secundario, sin fórmula ni peso).
- **Interpretaciones adoptadas:**
  - Va a `10-model` porque introduce indicadores.
  - El IP y la calidad ajustada se calculan por **RI × ámbito**.
  - Solo están definidos para **Web**. En Web Schema.org y Catálogos distribuidos el IP es **NA** hasta que haya reglas específicas.
  - «IP» se mantiene sin expandir, como en la fuente.
  - Las tensiones con FUND §2.3, PR-06 y D-006 (respuestas derivadas no prominentes) **no bloquean**, porque el intake prevalece. Se registran como OQ-33 y OQ-35.
- **Consecuencias:** OQ-31 a OQ-36 en la sección G de [open-questions](open-questions.md). Cambian el glosario, el índice, `scoring-systems` y la invariante 7.

### D-019

**Estado binario de resolución = «suficientemente resuelto» de la TRI.** · aceptada · 2026-10-24

- **Contexto:** el artefacto introduce una «normalización binaria del IR (0/1)» que distingue resolución suficiente e insuficiente. La TRI (BASE §6.1) ya se basa en RI «suficientemente resueltos».
- **Decisión:** el estado binario de resolución es **la misma noción** que usa la TRI. Así hay un único concepto, con la regla de normalización pendiente (OQ-31). Su estado es propuesta.
- **Consecuencias:** sección «Estado binario de resolución» en [scoring-systems](../10-model/scoring-systems.md) y entrada en el glosario.

### D-020

**Clase de estudio: clase general más especializaciones relevantes.** · aceptada · 2026-10-24

- **Contexto:** `INTAKE 2026-10-24-define-class`. El canon define el modelo de demanda sobre una «clase de producto u oferta» (BASE §4), pero no decía cómo se determina esa clase. La taxonomía (propuesta) ofrece subclases, facetas y aplicabilidad condicionada, y dejaba abierto el grado de especialización ([OQ-09](open-questions.md)).
- **Decisión:**
  - La **clase objeto del modelo de demanda** se compone de una **clase general** y de **todas las especializaciones aplicables** (por uso, material, función u otras características) que introduzcan o modifiquen cuestiones informativas relevantes. No es necesario que formen una jerarquía estricta: pueden ser facetas que concurren.
  - El modelo de demanda integra los requisitos comunes y los específicos, sin duplicados y revisando su aplicabilidad e importancia relativa.
  - «La medida de cama (por ejemplo, 90 cm) caracteriza una variante, pero no obliga por sí sola a crear otra clase».
  - **Principio:** buscar la especificidad informativa necesaria, no el mayor número posible de subclases.
  - Cierra OQ-09.
- **Interpretaciones adoptadas:**
  - «Clase objeto del modelo de demanda» y «clase de estudio» son sinónimos en el artefacto. El término canónico es **clase de estudio**, y la «clase estudiada» de BASE §4.1 y §4.2 designa la misma clase.
  - Va a `10-model` porque introduce conceptos. Se incorpora como **vigente**, porque el artefacto la formula como regla y no la presenta como provisional.
  - El ejemplo de los juegos de sábanas se marca como **ilustrativo**: no es una clase aprobada (regla de ejemplos hipotéticos de `docs/CLAUDE.md`).
  - El artefacto no deroga la taxonomía: la prueba de especialización y sus cuatro salidas siguen como propuesta de método. Sus umbrales («cambien sustancialmente», «cuestiones informativas centrales distintas») se refieren a crear subclases o niveles. Para incorporar una especialización a la clase de estudio rige el criterio del artefacto, menos exigente, y la relación entre ambos umbrales pasa a OQ-38. Queda abierto cómo se representa en la taxonomía una clase de estudio compuesta ([OQ-37](open-questions.md)) y qué evidencia acredita que una especialización es pertinente ([OQ-38](open-questions.md)).
  - OQ-09 se cierra porque el artefacto fija el criterio de grado: tantas especializaciones como sean relevantes, con la especificidad informativa necesaria. Los criterios operativos y la evidencia mínima siguen en OQ-06 y OQ-38.
  - El paso 4 («construir el modelo de demanda») se realiza con el recorrido vigente del sistema de construcción (observar → inferir → formular y normalizar → justificar), que no cambia.
  - La frase de la medida de cama se recoge literal, como ejemplo, sin generalizarla a una regla sobre variantes.
  - OQ-05 sigue abierta: la regla trata de la composición de la clase de estudio, no de la estructura de padres de las clases internas.
- **Consecuencias:**
  - [demand-model](../10-model/demand-model.md) pasa a la versión 1.2, con la nueva sección «Clase de estudio».
  - Se enlaza desde [product-taxonomy](../20-methods/product-taxonomy/README.md), [subclasses](../20-methods/product-taxonomy/subclasses.md), [integration](../20-methods/product-taxonomy/integration.md) y [data-model-governance](../20-methods/product-taxonomy/data-model-governance.md), todos en la versión 1.1.
  - Nuevas entradas del glosario: clase de estudio, clase general y especialización. Nuevas OQ-37 y OQ-38.
- **Relacionado:** OQ-05, OQ-06, OQ-09, OQ-37, OQ-38.

### D-021

**Shopify fija el eje de base de la clase general.** · aceptada · 2026-10-24

- **Contexto:** `INTAKE 2026-10-24-specialization-criterion`, bloque A, procedente del caso de trabajo T-005 (juego de sábanas de coralina). [D-020](#d-020) pedía «identificar la clase general» sin decir con qué referencia. [D-009](#d-009) fijaba Shopify como estructura principal de la vía taxonómica.
- **Decisión:**
  - La clase general de una clase de estudio es una categoría de la Shopify Standard Product Taxonomy, en la versión fijada.
  - Lo que Shopify no distingue como categoría entra como especialización.
- **Interpretaciones adoptadas:**
  - Es un update descrito por el usuario en la conversación, sin artefacto en `intake/`. Se transcribe literal en `archive/intake/2026-10-24-specialization-criterion.md` para conservar la trazabilidad.
  - Va a `10-model`, como precisión del paso 1 de la regla de D-020, y se incorpora como **vigente** porque el usuario la formula como regla (misma situación que [I-11](issues.md#i-11)).
  - «Versión fijada» es la versión de Shopify adoptada como referencia: hoy, v2026-08 ([sources](../20-methods/product-taxonomy/sources.md#shopify-base-estructural-y-vocabulario-de-atributos)).
  - La regla determina **qué categoría** es la clase general, no cómo se representa como clase interna, que sigue en [OQ-37](open-questions.md). Tampoco convierte cada categoría de Shopify en una clase aprobada.
  - «Lo que Shopify no distingue como categoría entra como especialización» se lee como **candidata** a especialización: se examina con el criterio de [D-022](#d-022) y no se incorpora automáticamente. En el propio caso, el diseño, el color y la medida no son categorías y se descartan.
- **Consecuencias:** [demand-model](../10-model/study-class.md#clase-general-el-eje-de-base) 1.3; glosario (clase general); caso de trabajo en [subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina).
- **Relacionado:** D-009, D-020, OQ-37.

### D-022

**Criterio de especialización: cinco condiciones y evidencia.** · aceptada · 2026-10-24

- **Contexto:** `INTAKE 2026-10-24-specialization-criterion`, bloques B y C. [OQ-38](open-questions.md) pedía la evidencia y el criterio operativo para reconocer que una especialización «introduce o modifica cuestiones informativas relevantes» ([D-020](#d-020)). El criterio se probó a mano en el caso T-005.
- **Decisión:**
  - Una característica es especialización de la clase de estudio cuando cumple cinco condiciones: es del producto y estable; tiene un efecto comparativo sobre las cuestiones; las cuestiones afectadas son relevantes para la clase; tiene apoyo en las referencias; y se fija en el nivel más general cuyos miembros comparten las cuestiones que introduce.
  - No cuentan: un nodo o valor que solo existe en una referencia, un cambio de los valores esperados, una característica de variante, la proximidad temática ni un requisito de plataforma o de feed.
  - Evidencia: con las cinco condiciones razonadas en la ficha, la especialización queda provisional. La valida el responsable. El contraste con ecommerce referentes (MPIR) la confirma o la revisa después, cuando exista. No se fija ningún umbral numérico.
  - Cierra OQ-38.
- **Interpretaciones adoptadas:**
  - Va a `10-model` porque introduce un criterio, y se incorpora como **vigente** (misma situación que [I-11](issues.md#i-11)).
  - «La valida el usuario, como responsable» designa al responsable de la taxonomía, el propietario del proyecto. La cita del canon omite, marcándolo con […], el paréntesis «(opción B elegida por el usuario)», que solo indica cuál de las opciones discutidas se eligió.
  - «La ficha» es la ficha de clase del método ([Anexo A](../20-methods/product-taxonomy/data-model-governance.md#anexo-a-ficha-de-clase-propuesta)), que incluye el campo «responsable». Si una clase de estudio compuesta tiene ficha propia depende de [OQ-37](open-questions.md).
  - La lista de la condición 1 («un uso, material o función declarados») no se lee como cerrada. El artefacto no deroga el «u otras características» de D-020, que sigue citado literalmente. Lo decisivo de la condición es que la característica sea del producto, declarada y estable. En el caso, «juego» se clasifica como función o composición.
  - «Un nodo o valor que solo existe en una referencia» significa que su mera existencia en una referencia no basta (coherente con subclasses). No significa «que existe en una sola referencia»: el nodo de «juego» solo está en Amazon y sí cuenta como apoyo (condición 4).
  - Relación con la prueba de especialización de la taxonomía: el criterio rige la incorporación de una especialización a la clase de estudio. La prueba sigue rigiendo la creación de subclases o niveles jerárquicos de la taxonomía. Es más exigente en el umbral de efecto («cambien sustancialmente», «cuestiones informativas centrales distintas», frente a «al menos un efecto»), pero el criterio añade exigencias propias: el anclaje en Shopify, Amazon o Google (la prueba admite también ecommerce referentes) y la condición de nivel. Así se resuelve la parte de OQ-38 sobre la relación entre ambos umbrales.
  - OQ-06 sigue abierta para las equivalencias entre conceptos y la aprobación de subclases. El criterio solo resuelve el reconocimiento de especializaciones.
  - El caso del bloque C es **ilustrativo** y va al método ([subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina)). El ejemplo literal de D-020 se conserva; una nota indica que, con la condición 5, el tejido queda en «polar» y la coralina como valor.
  - Las «observaciones del caso» se recogen como observaciones del método, sin convertirlas en reglas.
- **Consecuencias:**
  - [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.3, con las secciones «Clase general: el eje de base» y «Criterio de especialización».
  - [subclasses](../20-methods/product-taxonomy/subclasses.md) 1.2, con el caso de trabajo y el enlace al criterio.
  - [integration](../20-methods/product-taxonomy/integration.md) 1.2: el umbral de la clase de estudio remite al criterio y deja de citar OQ-38 como pendiente.
  - OQ-38 cerrada; OQ-06, OQ-09 y OQ-37 anotadas; [I-11](issues.md#i-11) ampliada. Glosario: especialización (redefinida con el criterio) y nueva entrada «criterio de especialización».
- **Relacionado:** D-020, D-021, OQ-06, OQ-37, OQ-38.

### D-023

**Composición de la clase de estudio por categorías y piezas.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-class-composition`, bloques A y D, procedente de la evaluación del método con tres casos más (tarea T-006). [D-021](#d-021) decía que la clase general es «una» categoría de Shopify. El juego de toallas tiene piezas de dos categorías distintas de Toallas (Toallas de baño y Toallas de mano), y el sofá cama encaja también en la hermana Sofás de dos plazas.
- **Decisión:**
  - El modelo de clase es un sistema de composición de requisitos. Cada componente (categoría de Shopify o especialización) aporta sus requisitos, y el modelo de demanda de la clase de estudio los integra sin duplicados.
  - Si el producto abarca varias categorías de Shopify, la clase general es la composición de esas categorías, no su ancestro común.
  - Una categoría entra en la composición si aporta requisitos al producto o a alguna de sus piezas. En un juego, cada pieza es una entidad. Una categoría que no aporta requisitos propios no entra.
  - La especialización «juego» aporta los requisitos del conjunto: qué piezas incluye, cuántas y en qué medidas.
  - Modifica D-021: la clase general sigue fijada por el eje de Shopify, pero puede ser una composición de varias categorías.
- **Interpretaciones adoptadas:**
  - Es un update descrito por el usuario en la conversación; se transcribe en `archive/intake/2026-10-25-class-composition.md` (situación descrita en [I-11](issues.md#i-11)).
  - Va a `10-model` como enmienda de la regla de D-021 y se incorpora como **vigente**. La cita de D-021 se sustituye por su formulación enmendada. La cita del bloque A omite, marcándolo con […], las palabras del usuario que el artefacto recoge, porque no añaden regla.
  - El artefacto no dice cómo se comprueba «aportar requisitos». Aplicarle el efecto comparativo de la condición 2 sería circular, porque esa condición compara con la clase general que estas categorías forman. La prueba operativa queda abierta en [OQ-39](open-questions.md). En los casos se aplicó así: en el sofá, Sofás de dos plazas no aporta (mismos atributos en Shopify; en Amazon es un valor). En las toallas, Toallas de mano aporta porque sus requisitos recaen sobre otra pieza, aunque sean del mismo tipo que los de Toallas de baño.
  - La regla no decide si las composiciones se registran como clases internas o se componen en cada estudio: sigue en [OQ-37](open-questions.md), que se anota.
  - El caso de las sábanas se recompone por piezas en el método. La composición anterior («Sábanas + juego») deja de figurar en el canon.
- **Consecuencias:** [demand-model](../10-model/study-class.md#composición-de-la-clase) 1.4, con la nueva sección «Composición de la clase» y la cita de D-021 marcada como enmendada; [subclasses](../20-methods/product-taxonomy/subclasses.md) 1.3, con el caso de las sábanas recompuesto y los tres casos nuevos; glosario (clase general y nueva entrada «componente de la clase de estudio»); OQ-05 y OQ-37 anotadas; nueva OQ-39. La revisión independiente detectó que el caso de las sábanas apoya «juego» y «tejido polar» en Sábanas, que ya no es componente: [I-12](issues.md#i-12).
- **Relacionado:** D-020, D-021, D-022, OQ-05, OQ-37.

### D-024

**Condición 4 del criterio de especialización: lectura estricta.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-class-composition`, bloque B. En el sofá cama, el mecanismo de apertura solo tenía apoyo en una categoría afín (Futones). La condición 4 de [D-022](#d-022) no decía si ese apoyo bastaba.
- **Decisión:**
  - La dimensión debe existir en algún componente de la clase de estudio, en cualquiera de las tres referencias: atributos de la categoría de Shopify, nodo o PTD de Amazon, o categoría de Google.
  - El apoyo en una categoría afín se anota en la ficha como evidencia complementaria, pero no basta por sí solo.
  - Una distinción que no cumple la condición no se pierde: sus cuestiones quedan en la clase general como requisitos condicionados (salida «conservar la clase y condicionar requisitos»).
- **Interpretaciones adoptadas:** precisa la condición 4 sin cambiar su texto; el artefacto la denomina «lectura estricta».
- **Consecuencias:** [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.4; glosario (criterio de especialización).
- **Relacionado:** D-022, D-023.

### D-025

**Beneficios reclamados: no son especializaciones.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-class-composition`, bloque C. El hueso de cuerda declara que favorece la higiene dental. La condición 1 de [D-022](#d-022) excluía las etiquetas promocionales, pero no los beneficios funcionales.
- **Decisión:** un beneficio que el producto reclama no es especialización, salvo que las referencias tengan un tipo de producto definido por él. Su fundamento se evalúa en la auditoría, no en la clase.
- **Interpretaciones adoptadas:** amplía las exclusiones del criterio. «Se evalúa en la auditoría» remite a la [auditoría](../20-methods/audit-gsc/README.md) en general. Cómo llega a ella el fundamento de un beneficio que no entra en la clase (como RI, como requisito condicionado…) queda abierto en [OQ-40](open-questions.md).
- **Consecuencias:** [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.4; glosario (especialización); nueva OQ-40.
- **Relacionado:** D-022.

### D-026

**Regla de las cuestiones propias para dimensiones que todo producto tiene.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-own-questions-offer`, bloque A, procedente de la evaluación con cuatro casos más (tarea T-007). La condición 2 de [D-022](#d-022) compara con «la clase general sin esa característica», pero no existe sofá sin tapicería ni pienso sin forma. Los casos aplicaban la observación «el material habitual de la clase queda como valor», de `INTAKE 2026-10-25-class-composition` (sección E), y con ella la tela del sofá cama Luna figuraba como valor.
- **Decisión:**
  - Para una dimensión que todo producto de la clase tiene, un valor es especialización solo si trae cuestiones propias, que no salen de las dimensiones de la clase general.
  - Si solo cambia los valores, o solo hace que algunas cuestiones dejen de aplicarse, es un valor que condiciona (como en [D-024](#d-024)).
  - Consecuencias aceptadas, con las razones del artefacto: polar (sábanas) sigue siendo especialización («trae bolitas, electricidad estática y pérdida de pelo»); algodón (sábanas, toallas, funda nórdica) es valor («número de hilos, ligamento y gramaje ya están en la base»); polipropileno (cuerda) es valor; la tela del sofá cama Luna pasa a especialización («trae resistencia a la abrasión, desenfundable y antimanchas»); la piel del Stressless es especialización («tipo y acabado de la piel»); el pienso seco es especialización («tamaño de la croqueta»); adulto es valor («solo deja de aplicar lo de crecimiento»).
- **Interpretaciones adoptadas:**
  - Precisa la condición 2 sin cambiar su texto; va a `10-model` y se incorpora como **vigente**.
  - «Las dimensiones de la clase general» se comprueban en sus referencias, incluidos los PTD de Amazon y no solo los atributos de Shopify. Se lee así a partir de una observación del artefacto, que este marca como «no son reglas»: `leather_type` está en PTD `BOOT` pero no en `SOFA`, así que la piel es valor en botas y especialización en sofás.
  - El artefacto no trata dos efectos de la condición 2 para estas dimensiones: «cambia el alcance o la desagregación» y «cambia la importancia relativa». Queda abierto en [OQ-41](open-questions.md).
  - Corrige el caso del sofá cama Luna documentado con [D-023](#d-023): la tela pasa de valor a especialización («tapicería textil»). La regla de D-023 no cambia.
  - El bloque C (aplicación a los casos) lo elaboró Claude a partir de las reglas, como indica el artefacto, y va al método como ilustración.
- **Consecuencias:** [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.5; nueva OQ-41; [I-13](issues.md#i-13), sobre la revisión del caso de las sábanas y el apoyo de la piel del Stressless; dos observaciones de `INTAKE 2026-10-25-class-composition` quedan superadas; nuevo módulo de método [cases](../20-methods/product-taxonomy/cases.md), que recibe los casos de evaluación de subclasses (1.4) con el sofá cama corregido y cuatro casos nuevos; glosario (criterio de especialización).
- **Relacionado:** D-022, D-023, D-024.

### D-027

**La condición 1 incluye la oferta: especializaciones de oferta.** · sustituida por [D-048](#d-048) · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-own-questions-offer`, bloque B. El sofá Stressless es la última unidad de exposición, con garantía reducida «por ser producto outlet». La condición 1 de [D-022](#d-022) exigía que la característica fuera del producto. El canon habla de «clase de producto u oferta» (BASE §4), y [OQ-37](open-questions.md) preguntaba si la regla se aplica a las clases de oferta.
- **Decisión:**
  - La condición 1 pasa a decir: «es del producto o de la oferta, y estable».
  - Lo de outlet, exposición o reacondicionado pasa a ser una especialización de oferta. (Sustituida por [D-048](#d-048): la oferta no aporta requisitos ni especializaciones.)
  - Resuelve la parte de OQ-37 sobre las clases de oferta.
- **Interpretaciones adoptadas:**
  - Enmienda el texto de la condición 1: la cita del canon se sustituye por la versión enmendada. El resto de la condición («un uso, material o función declarados…») se conserva.
  - El artefacto no dice cómo se aplican las demás condiciones a una especialización de oferta; se aplican igual, como lectura sin fundamento expreso. En el caso, el apoyo de la condición 4 está en el grupo de oferta de PTD (`condition_type`, `condition_note`, garantía).
  - «Outlet» puede chocar con la exclusión de las etiquetas promocionales de la misma condición. Si outlet o exposición cuentan cuando declaran el estado de la unidad, como en el caso, queda abierto en [OQ-42](open-questions.md).
- **Consecuencias:** [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.5, con la condición 1 enmendada y la lectura del criterio ajustada («del producto o de la oferta»); glosario (especialización y nueva entrada «especialización de oferta»); OQ-37 anotada; nueva OQ-42.
- **Relacionado:** D-022, D-026, OQ-37.

### D-028

**Clasificación objetiva: una categoría entra aunque no aporte requisitos.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-objective-classification`, bloque A, procedente de la evaluación con cinco casos más (tarea T-008). El plaid de punto entra objetivamente en Mantas decorativas (`hg-15-1-4-2`), que no añade requisitos a los de su madre Mantas. [D-023](#d-023) decía que «una categoría que no aporta requisitos propios no entra».
- **Decisión:**
  - Palabras del usuario: «Por ordenamiento y coherencia, si hubiera una candidata que el producto entraría por clasificación objetiva, aunque no aporte nada, la añadimos. […]».
  - Una categoría candidata en la que el producto entra por clasificación objetiva forma parte de la composición aunque no aporte requisitos propios.
  - Sustituye «Una categoría que no aporta requisitos propios no entra»: aportar requisitos al producto o a alguna de sus piezas sigue siendo vía de entrada, pero no la única.
  - Lecturas aceptadas por el usuario: en el plaid entra Mantas decorativas y no Mantas para sillones y sofás (`hg-3-77`), que es una entrada duplicada en Decoración para el mismo tipo de producto; en la manta Nacarina, la clasificación objetiva es Mantas (`hg-15-1-4`) y no Mantas decorativas, porque el uso en sofá depende de la variante (medida).
  - Consecuencia aceptada: el sofá cama Luna, que es objetivamente un sofá de dos plazas, pasa a Sofás cama + Sofás de dos plazas (`fr-22-4`).
- **Interpretaciones adoptadas:**
  - Enmienda la regla de D-023: la cita del canon sustituye su tercer punto por la formulación enmendada. El resto de D-023 no cambia.
  - El artefacto no dice cómo se prueba que un producto entra «por clasificación objetiva», ni cómo se reconoce una entrada duplicada de Shopify. Queda abierto en [OQ-43](open-questions.md). Las dos lecturas aceptadas se documentan como casos.
  - El bloque E (aplicación a los casos) lo elaboró Claude, como indica el artefacto, y va al método como ilustración.
- **Consecuencias:** [demand-model](../10-model/study-class.md#composición-de-la-clase) 1.6; [cases](../20-methods/product-taxonomy/cases.md) 1.1, con el sofá cama Luna corregido y cinco casos nuevos; glosario (componente de la clase de estudio y nueva entrada «clasificación objetiva»); OQ-39 anotada; nueva OQ-43.
- **Relacionado:** D-021, D-023, OQ-39, OQ-43.

### D-029

**Base de una categoría de Shopify: atributos propios y de sus madres.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-objective-classification`, bloque B. En Shopify v2026-08, 1749 de 14580 categorías hijas tienen solo una parte de los atributos de su madre: Mantas decorativas tiene 3 y Mantas, 9; Sofás cama, 9 y Sofás, 17. Con la lectura literal, Mantas para sillones y sofás aportaría al plaid tejido, color, cuidados y patrón, y entraría como segunda categoría de un producto de una sola pieza.
- **Decisión:** la base de una categoría de Shopify son sus atributos propios más los de sus categorías madre (una categoría hija es un tipo de su madre).
- **Interpretaciones adoptadas:**
  - Precisa qué son los atributos de una categoría de Shopify en [D-023](#d-023) (aportar requisitos), [D-024](#d-024) (condición 4) y [D-026](#d-026) (dimensiones de la clase general), sin cambiar su texto. Se incorpora como **vigente** en `10-model`.
  - «Sus categorías madre» se lee como todas sus categorías ascendientes: el plural y la razón («una categoría hija es un tipo de su madre») se aplican de forma transitiva.
  - Resuelve [I-12](issues.md#i-12): en el caso de las sábanas, `bedding-pieces-included` y `fabric` están en Sábanas (`hg-15-1-2`), la madre de Sábanas planas y Sábanas ajustables, así que forman parte de la base de esos componentes. Los apoyos de «juego» y «tejido polar» quedan en componentes de la clase.
- **Consecuencias:** [demand-model](../10-model/study-class.md#composición-de-la-clase) 1.6; [subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina) 1.5, con los apoyos del caso de las sábanas en la base heredada; I-12 resuelta; observación del sofá cama en [cases](../20-methods/product-taxonomy/cases.md) actualizada.
- **Relacionado:** D-023, D-024, D-026, I-12.

### D-030

**Características especiales de un PTD: dimensiones de la base y apoyo.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-objective-classification`, bloque C. En la manta, la electricidad estática y la pelusa solo figuran en la base como valores de `special_feature` de PTD `BLANKET` («Antiestático», «Sin pelusa»). En las zapatillas, la absorción figura igual en `SLIPPER` («Absorbe la humedad»), y en el cojín, el material reciclado en `PILLOW` («Reciclada»).
- **Decisión:** los valores de la propiedad «Características especiales» (`special_feature`) de un PTD de Amazon cuentan como dimensiones de la base de la clase (regla de las cuestiones propias) y como apoyo (condición 4).
- **Interpretaciones adoptadas:**
  - Precisa [D-024](#d-024) y [D-026](#d-026) sin cambiar su texto. Se incorpora como **vigente** en `10-model`.
  - Presupone y confirma la lectura adoptada en D-026: las dimensiones de la clase general se comprueban en sus referencias, incluidos los PTD.
  - El artefacto reconoce un riesgo y no lo trata: el resultado depende de qué valores incluyó Amazon en cada lista (la de `BLANKET` no tiene «Resistente a la formación de bolitas»; la de `SLIPPER` sí). Se registra en la decisión. No se abre cuestión, porque las especializaciones ya quedan provisionales hasta su validación y el contraste MPIR ([D-022](#d-022)).
- **Consecuencias:** [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.6; glosario (criterio de especialización); [cases](../20-methods/product-taxonomy/cases.md) 1.1 (manta, zapatillas y cojín). La revisión independiente detectó que la regla cambia la base de casos ya documentados: [I-14](issues.md#i-14).
- **Relacionado:** D-022, D-024, D-026, I-14.

### D-031

**El material reciclado es especialización, no beneficio reclamado.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-objective-classification`, bloque D. El cojín declara 87 % algodón reciclado y 13 % poliéster reciclado, y se presenta como «producto sostenible». [D-025](#d-025) excluye los beneficios reclamados.
- **Decisión:** «material reciclado» es especialización, no beneficio reclamado: es composición verificable y trae cuestiones propias (qué proporción y en qué parte). «Sostenible» sí es beneficio reclamado (D-025).
- **Interpretaciones adoptadas:**
  - Precisa D-025 sin cambiar su texto. Se incorpora como **vigente** en `10-model`.
  - La especialización sigue sometida a las cinco condiciones; en el caso, el apoyo está en `PILLOW` (`special_feature` «Reciclada», [D-030](#d-030)).
  - La decisión se refiere al material reciclado. El artefacto no la extiende a otras características ambientales del material; se examinan con el criterio.
- **Consecuencias:** [demand-model](../10-model/study-class.md#criterio-de-especialización) 1.6; glosario (especialización); [cases](../20-methods/product-taxonomy/cases.md) 1.1 (cojín).
- **Relacionado:** D-022, D-025, D-030.

### D-032

**Propósito de la clase de estudio: los requisitos informativos.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-requirements-purpose`, procedente de la tarea T-008. La revisión independiente del update anterior abrió [I-14](issues.md#i-14): con [D-029](#d-029) y [D-030](#d-030), algunas cuestiones que los casos contaban como propias están en la base, y la tela del sofá cama Luna, especialización por una consecuencia aceptada de [D-026](#d-026), pasaría a valor. En el juego de funda nórdica bordada, la clasificación objetiva ([D-028](#d-028)) planteaba si entra Juegos de cama (`hg-15-1-11`).
- **Decisión:**
  - Palabras del usuario: «Recuerda que el propósito es establecer requisitos informativos. Esto es lo más importante (+ el matiz de denominación que hemos especificado cuando tiene sentido aunque no aporte)». El matiz es la clasificación objetiva (D-028).
  - Lectura aceptada: la pregunta que manda es qué requisitos informativos produce la clase; que algo sea especialización o valor es instrumental. Lo único que entra sin aportar requisitos es lo que nombra la clase por clasificación objetiva, cuando tiene sentido.
  - Sofá cama Luna: los requisitos no cambian. La resistencia a la abrasión, el desenfundable y el antimanchas siguen siendo requisitos, que ahora salen de la base de PTD `SOFA` (D-030). Que la tela pase a valor es un cambio de etiqueta, y el matiz de denominación no se aplica porque no es una categoría de clasificación objetiva. La clase queda en Sofás cama + Sofás de dos plazas. Sofás de dos plazas sí está bien añadido: no aporta requisitos, pero nombra lo que el producto es.
  - Resto de I-14: no cambia ningún requisito. El lavado de la cuerda y la resistencia a la mordida siguen siendo requisitos, igual que las bolitas, la electricidad estática y la pérdida de pelo del polar, y qué piezas incluye el juego, cuántas y en qué medidas. Se aplican las propuestas: la cuerda sigue siendo especialización por el deshilachado y la ingestión de fibras, y el lavado pasa a la base; el polar de las sábanas sigue siendo especialización, porque la pérdida de pelo no está en ninguna base; el efecto del juego se escribe con los requisitos del conjunto de [D-023](#d-023); se documenta el apoyo del polar en la manta. Leer la base pieza a pieza o para todo el juego no altera el resultado.
  - Juegos de cama no entra en el juego de funda nórdica: no aporta requisitos y traería uno que no aplica (el nivel de calidez «del edredón o la colcha», en un juego de fundas sin relleno). Añadirlo empeoraría los requisitos, así que tampoco tiene sentido por denominación. Además, Amazon separa los juegos de edredón o colcha (PTD `BEDDING_SET`, con `fill_material`) de los juegos de fundas (`BED_LINEN_SET`).
- **Interpretaciones adoptadas:**
  - Es un principio de lectura de la clase de estudio; va a `10-model` junto al principio de especificidad informativa necesaria y se incorpora como **vigente**. No cambia el texto de las reglas D-020 a D-031.
  - Revisa la consecuencia de D-026 sobre la tela del sofá cama Luna. Con ella, la observación de `INTAKE 2026-10-25-class-composition` «el método no fuerza especializaciones (sofá cama)» deja de estar superada.
  - Mordedor: la propuesta aceptada de I-14 era comprobar si «Uso rudo» cubre la resistencia a la mordida. PTD `PET_TOY` tiene en `special_feature` «Uso rudo» y «Tecnología Chew Guard». Se lee que «Uso rudo» la cubre; «Chew Guard» es el nombre de una tecnología y solo refuerza la lectura. Con el mismo criterio que la tela del sofá cama, el mordedor pasa a valor que condiciona, y la resistencia a la mordida sigue siendo requisito. Es una interpretación de Claude, provisional hasta que la valide el usuario.
  - En el juguete de cuerda, la base de Amazon se lee en `PET_TOY`, el PTD de los nodos hijos (Cuerdas, Juguetes para morder…), porque el nodo de la clase general (`13441958031`) tiene `PET_SUPPLIES`, que no tiene `special_feature`.
  - Juegos de cama precisa cómo se aplica «cuando tiene sentido»: una categoría que traería requisitos que no aplican no entra por denominación. Se anota en [OQ-43](open-questions.md).
  - El bloque C (casos) lo elaboró Claude y va al método como ilustración.
- **Consecuencias:** [demand-model](../10-model/study-class.md) 1.7, con el principio y la lectura citados, la precisión de la clasificación objetiva y sin la frase que repetía el paso 3 de la regla; [cases](../20-methods/product-taxonomy/cases.md) 1.2 (sofá cama, juguete de cuerda, manta, juego de funda nórdica, protector y nuevo caso del juego de funda nórdica bordada); `product-taxonomy` (README) 1.5; I-11 ampliada; I-13 anotada; [subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina) 1.6; I-14 resuelta; OQ-43 anotada; glosario (clase de estudio, componente de la clase de estudio y clasificación objetiva). La revisión independiente detectó que `warmth-level` no está solo en Juegos de cama, como dice el caso de las sábanas: [I-15](issues.md#i-15).
- **Relacionado:** D-020, D-026, D-028, D-029, D-030, I-14, OQ-43.

### D-033

**Identidad del modelo de demanda: composición de bloques de requisitos.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-requirement-blocks`, bloques A y G, procedente de la tarea T-010 tras el experimento base del clasificador (T-009). Hasta ahora la clase de estudio (categorías + especializaciones) identificaba el modelo, y la clasificación objetiva podía entrar en su denominación aunque no aportara requisitos ([D-028](#d-028), [D-032](#d-032)).
- **Decisión:**
  - Palabras del usuario: «el modelo de demanda de un producto se "denomine" por su composición de requisitos. Es decir, composición de clase <> composición de requisitos».
  - La unidad de composición son bloques de requisitos (general universal, generales condicionados, sector, categoría, especialización). Un bloque agrupa las cuestiones que trae un mismo hecho y lleva su importancia por defecto, revisable por el modelo con justificación.
  - (Enmendada por [D-047](#d-047): el modelo va con el producto y se identifica por sus bloques; la aplicación es de la oferta.) Identidad = modelo de requisitos (conjunto de bloques, incluidos los condicionados con su disparador) + aplicación concreta (qué bloques condicionados se activan o dejan de aplicarse en una oferta); ambos se identifican en la denominación.
  - Las categorías que entran por clasificación objetiva sin aportar requisitos son alias: «el objetivo de esto es puramente de etiquetado, denominación».
  - La composición de la clase es el medio de descubrimiento. La especialización es la característica que forma un bloque; una característica que revela una dimensión de toda la clase no forma bloque: su cuestión va al bloque de la clase y el valor declarado es la respuesta.
  - Estructura: la clase de estudio pasa a su propio módulo canónico, `study-class`.
- **Interpretaciones adoptadas:**
  - Va a `10-model` como vigente: es un concepto del modelo de demanda.
  - Precisa D-028 y D-032: la clasificación objetiva sigue rigiendo qué categorías se nombran, pero como alias, fuera de la identidad.
  - Resuelve la parte de [OQ-37](open-questions.md) sobre si las composiciones se registran: se registran los modelos como composiciones de bloques. El resto de OQ-37 sigue abierto.
  - El artefacto no fija el formato ni los identificadores de los bloques ni la sintaxis de la denominación más allá del ejemplo: [OQ-44](open-questions.md).
  - «Bloques de sector (atributos heredados de Shopify)» se lee como los atributos que una categoría hereda de sus madres, y los bloques de categoría como sus atributos propios, para no contar dos veces los de la base de D-029.
  - Precisa [D-020](#d-020): la clase de estudio deja de identificar el modelo y pasa a ser el medio para descubrir sus bloques.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.0 (reestructurado); nuevo módulo [study-class](../10-model/study-class.md) 1.0, con la sección que salió de demand-model y las reglas nuevas; nuevo módulo de método [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.0; enlaces actualizados; glosario.
- **Relacionado:** D-020, D-028, D-032, D-034, OQ-37.

### D-034

**Capa general de requisitos: universales y condicionados.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-requirement-blocks`, bloque B. Hay requisitos que aplican a cualquier producto, como el precio. El canon preveía «requisitos comunes» sin definirlos, y la taxonomía de producto no cubre la oferta.
- **Decisión:**
  - La capa general tiene cuestiones universales y cuestiones condicionadas con disparador declarado; el disparador es el hecho declarado, no la etiqueta.
  - Sus importancias son valores por defecto revisables por clase con justificación. (Enmendada por [D-045](#d-045): quedan fijas como parte del marco.)
  - Borrador inicial aceptado «para empezar, lo iremos perfeccionando» (catálogo en `requirement-blocks`).
- **Interpretaciones adoptadas:** el concepto va a `10-model` como vigente; el catálogo, a `20-methods` como propuesta. Las dudas del artefacto (envío ¿crítico?, medios de pago, opiniones, información precontractual por comprobar) quedan abiertas en [OQ-44](open-questions.md). En los casos, un descuento declarado activa la cuestión condicionada de descuento (aplicación «con descuento»).
- **Consecuencias:** [demand-model](../10-model/demand-model.md#capa-general) 2.0; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general).
- **Relacionado:** D-033, D-035, D-037.

### D-035

**Pruebas operativas de importancia relativa.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-requirement-blocks`, bloque C. El canon define crítico, principal y complementario, pero su calibración estaba abierta ([OQ-02](open-questions.md)).
- **Decisión:**
  - Pruebas aceptadas «para empezar, lo iremos perfeccionando»: crítico, si sin resolverla la oferta deja de ser evaluable; principal, si es criterio para comparar y elegir ofertas de la clase; complementario, si es relevante sin ser indispensable ni central.
  - La confianza en un requisito es independiente de su importancia.
- **Interpretaciones adoptadas:** son lectura operativa de las definiciones del canon, sin escala nueva; van al método como propuesta. La regla de la confianza va al canon como vigente. OQ-02 se anota, no se cierra: falta la calibración con casos comparables.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#importancia-relativa) 2.0; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#pruebas-de-importancia); OQ-02 anotada.
- **Relacionado:** D-034.

### D-036

**Cuestiones inferidas: tercera vía de construcción, provisional.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-requirement-blocks`, bloques D y F. Hay cuestiones de toda la clase que ninguna referencia recoge (el mecanismo de apertura de un sofá cama). El sistema de construcción solo tenía dos vías (taxonomía y MPIR).
- **Decisión:**
  - Palabras del usuario: «quizás no debemos esperar a validarlos por el MPIR sino darlos por válidos, confiar en el agente que los infiere».
  - Entran en el modelo como provisionales, en el régimen de [D-022](#d-022): las propone el clasificador; se usan en la auditoría, el usuario valida siempre las críticas y una muestra del resto, y el MPIR las confirma o revisa cuando exista; con los controles del artefacto (toda la clase, neutrales, justificadas, sin duplicar la base, origen marcado, informe con y sin ellas, dos ejecuciones por caso).
- **Interpretaciones adoptadas:**
  - El régimen provisional es una lectura de Claude que siguió a la propuesta del usuario y que este no objetó; así lo indica el artefacto, y así se cita.
  - Enmienda BASE §4.2 (dos vías, ya enmendada por [D-009](#d-009)): se añade una tercera vía, sin cambiar las otras dos.
  - Casos: el mecanismo de apertura del sofá cama Luna y la preparación y el acabado del algodón (funda bordada) entran como cuestiones inferidas del bloque de la clase.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#sistema-de-construcción-vigente) 2.0; READMEs de product-taxonomy y mpir (tercera vía); D-009 ampliada; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#cuestiones-inferidas); [cases](../20-methods/product-taxonomy/cases.md) 1.3; OQ-01 anotada.
- **Relacionado:** D-009, D-022, D-033.

### D-037

**Valores de oferta y activación de cuestiones condicionadas.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-requirement-blocks`, bloques E y F. Con la capa general, la condición de la unidad es un requisito general. [D-027](#d-027) ponía como ejemplo «lo de outlet, exposición o reacondicionado pasa a ser una especialización de oferta», y [OQ-42](open-questions.md) preguntaba si el outlet cuenta como estado o como etiqueta promocional.
- **Decisión:**
  - Outlet, liquidación, exposición o reacondicionado son valores de la oferta que condicionan cuestiones generales, no especializaciones, para cualquier producto.
  - Extensión de [D-026](#d-026): un valor que activa cuestiones condicionadas ya previstas en la base también es valor que condiciona; solo es especialización si trae cuestiones que la base no prevé.
- **Interpretaciones adoptadas:**
  - Sustituye el ejemplo de D-027; se mantiene que la condición 1 incluye la oferta. (Sustituida por [D-048](#d-048): la condición 1 solo admite características del producto.)
  - Cierra OQ-42: en ambos casos el valor condiciona cuestiones generales. (Precisada por [D-057](#d-057): la unidad de exposición que la ficha identifica como tal es estado declarado; «outlet» solo no basta.)
  - Revisión de casos (bloque F, aplicación de Claude aceptada): en el Stressless, el reclinable pasa a valor que condiciona, la piel sigue siendo especialización y el outlet pasa a valor (aplicación: unidad no nueva); polar, punto, seco y cuerda siguen siendo especialización.
- **Consecuencias:** [study-class](../10-model/study-class.md#criterio-de-especialización) 1.0, con la cita «Oferta» sustituida; [cases](../20-methods/product-taxonomy/cases.md) 1.3; OQ-42 cerrada.
- **Relacionado:** D-026, D-027, D-034, OQ-42.

### D-038

**Catálogo de bloques: capa general contrastada, identificadores propios y denominación.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-block-catalog`, tarea T-011. [OQ-44](open-questions.md) dejaba abiertos el formato y los identificadores de los bloques, la sintaxis de la denominación y las dudas del borrador de la capa general ([D-033](#d-033), [D-034](#d-034)). Claude comprobó el artículo 97.1 del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios (RDL 1/2007), versión consolidada del BOE a 28/02/2026.
- **Decisión:**
  - Capa general contrastada con el artículo 97.1 (aceptado: «1. ok. opiniones como complementaria»): precio y envío se unen en una cuestión crítica de precio total; lo que hace variar el envío es principal; los medios de pago entran como complementaria; el contacto del vendedor, complementaria; se reformulan desistimiento y devoluciones (97.1.j, k, m) y garantías y posventa (97.1.n, ñ); nuevas condicionadas: precio personalizado (97.1.f) y elementos digitales (97.1.s, t), principales, y duración, suscripción y depósitos (97.1.p, q, r); quedan fuera las letras g, i, o y u; las opiniones de clientes entran como complementaria.
  - Identificadores propios. Palabras del usuario: «el formato de id debe ser nuestro, no quiero acoplarme por si en el futuro cambian las referencias. Para mantener trazabilidad con referencia puedes especificar un formato como el propuesto pero no como el campo de id, sino más bien como de referencias o algo del estilo. Lo dejo a tu criterio».
  - Denominación en dos niveles, clave y nombre (aceptada: «3. si»).
  - Del resto del bloque B, aceptado por el usuario: los campos del bloque (identificador, tipo, nombre, disparador, versión, estado y requisitos) y del requisito (identificador, pregunta, dimensión, entidad, importancia por defecto, origen —referencias, inferida o normativa—, fundamento y aplicabilidad); las cuestiones inferidas dentro del bloque de su categoría, con el origen marcado en cada requisito; el catálogo como datos en `demand-engine/catalog/`.
  - Los medios de pago entran porque son información previa a la compra, aunque la transacción quede fuera del alcance.
- **Interpretaciones adoptadas:**
  - Formato de identificadores, por delegación del usuario: `gen`, `gen.<hecho>`, `cat.<nombre>` y `esp.<nombre>` para bloques, y `<bloque>/<nn>` para requisitos; `<nombre>` es un nombre propio, estable y único que no se deriva de las etiquetas de las referencias. Las referencias van en un campo aparte con formato `<fuente>:<identificador>@<versión>`. El tipo de bloque único para sector y categoría que propuso Claude (`shp:`) se mantiene como `cat.`, con los atributos propios de cada categoría.
  - Las opiniones entran como cuestión universal complementaria, con la parte de la propuesta de Claude sobre cómo se garantiza que proceden de compradores reales, si se publican. La trasposición de la directiva Omnibus queda por comprobar.
  - El artefacto no da importancia a la condicionada de duración, suscripción y depósitos: queda por fijar ([OQ-45](open-questions.md)). Las tres letras (p, q, r) se agrupan en un bloque `gen.suscripcion`, cuyo disparador es «si es una suscripción o hay depósito».
  - Precisiones de formato de Claude: valores del estado (propuesta o validado; enmendados por [D-045](#d-045): no compilado o compilado); campo «referencias» del bloque y campo «fuentes» del requisito, este a nivel de atributo cuando procede (`shopify-attr:…`, `amazon-ptd-prop:…`); las entidades del catálogo incluyen entrega y condiciones.
  - La cuestión universal de disponibilidad se separa de la cantidad, que pasa a la condicionada `gen.cantidad-limitada` (crítica, como la cuestión original), para que coincida con el disparador «si la cantidad es limitada» de la capa general.
  - La sintaxis de la denominación va al canon (cita literal); el formato del catálogo y la capa general, al método.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.1; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.1 (catálogo de la capa general, formato del catálogo y denominación); OQ-44 cerrada; nueva OQ-45; glosario (bloque de requisitos).
- **Relacionado:** D-033, D-034, OQ-44, OQ-45.

### D-039

**Los PTD de Amazon, fuente de requisitos de la categoría.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-amazon-source-blocks`, tarea T-016, tras el segundo experimento del clasificador (T-012). Se perdió un 35 % de las cuestiones clave por un hueco entre [D-009](#d-009), [D-030](#d-030) y [D-036](#d-036): una cuestión que solo recoge Amazon contaba como base para decidir la etiqueta, pero no era fuente de requisitos ni podía ser inferida.
- **Decisión (aceptada: «ok a 1 y 2»):** alternativa descartada: mantener D-009 y tratarlas como inferidas con Amazon de apoyo, lo que exigía redefinir «inferida». Se decide que las propiedades de los PTD de Amazon, incluidos los valores de special_feature, pueden ser fuente de requisitos de la categoría cuando son relevantes para la clase, con origen «referencias». Enmienda D-009.
- **Interpretaciones adoptadas:**
  - Se enmienda la frase del canon según la cual Amazon y Google son fuentes de apoyo, «no fuentes directas de RI»: Amazon puede serlo a través de sus PTD; Google sigue siendo solo de apoyo, porque el artefacto no lo menciona.
  - «Relevantes para la clase» se decide en la revisión del catálogo de bloques de categoría ([D-040](#d-040)). (Precisada por [D-044](#d-044): lo deciden las reglas inducidas en el entrenamiento.)
  - Las cuestiones inferidas siguen siendo las que no recoge ninguna referencia, ahora incluidos los PTD de Amazon; D-036 no cambia.
- **Capas:** la regla va al canon (`demand-model`, vigente); su operación, al método (`requirement-blocks`, `sources`, propuesta).
- **Consecuencias:** [demand-model](../10-model/demand-model.md#sistema-de-construcción-vigente) 2.2; [README de product-taxonomy](../20-methods/product-taxonomy/README.md) 1.7; [sources](../20-methods/product-taxonomy/sources.md) 1.1; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.3; [data-model-governance](../20-methods/product-taxonomy/data-model-governance.md); [cases](../20-methods/product-taxonomy/cases.md) 1.4 (el acabado del algodón deja de ser inferido); glosario (cuestión inferida). La revisión independiente detectó una posible tensión con D-030 en el filtro de relevancia: [I-17](issues.md#i-17).
- **Relacionado:** D-009, D-030, D-036, D-040.

### D-040

**Bloques de categoría deterministas y catálogo revisado.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-amazon-source-blocks`. En el segundo experimento, los bloques de sector coincidieron en 4 de 14 casos entre ejecuciones: Shopify repite atributos como propios en varios niveles y cada agente los asignaba a un nivel distinto. [D-038](#d-038) fijaba que un bloque de categoría lleva los atributos propios de su categoría.
- **Decisión (aceptada: «ok a 1 y 2»):** construir los bloques de categoría de forma determinista: un atributo repetido va siempre al bloque de la categoría más general que lo lista. Crear un catálogo de bloques cat. (preguntas e importancia por defecto), generado con la herramienta y revisado una vez por categoría; el clasificador elige bloques en lugar de redactarlos.
- **Interpretaciones adoptadas:**
  - Precisa D-033 y D-038: un bloque de categoría lleva los atributos propios de su categoría que no lista ninguna de sus madres.
  - La revisión la hace el usuario; hasta entonces el bloque está en estado propuesta. (Con [D-044](#d-044) y [D-045](#d-045): lo compila el entrenamiento; hasta entonces está «no compilado».) El clasificador sigue redactando las cuestiones inferidas y las especializaciones.
  - Las propiedades de Amazon (D-039) van al bloque de la categoría que la tabla de correspondencia `catalog/amazon-map.json` asocia a su PTD (una por categoría; si varias de la cadena comparten PTD, la más general); una propiedad que solo se aplica a una categoría hija va al bloque de la hija; si repite una dimensión que ya cubre un atributo de Shopify, no se duplica. El artefacto no lo dice; es la lectura necesaria para que el generador sea determinista.
  - **Capas:** la regla de asignación va al canon (`demand-model`); el catálogo y su generación, al método y al motor.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.2; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.3; glosario (bloque de requisitos); el catálogo de bloques se genera en `demand-engine/catalog/`. La revisión independiente detectó que las cuestiones inferidas dentro de un bloque de categoría hacen variar su contenido: [I-16](issues.md#i-16).
- **Relacionado:** D-033, D-038, D-039.

### D-041

**Entrenamiento y ejecución: la revisión humana no bloquea la ejecución.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-training-runtime`, tarea T-016. Palabras del usuario: «la revisión humana solo debe ser en tiempo de entrenamiento, en tiempo de ejecución debe ser automático». El canon podía leerse como bloqueante en dos puntos: una categoría que aún no está en el catálogo ([D-040](#d-040)) y la validación de las cuestiones inferidas críticas ([D-036](#d-036)). La incidencia [I-16](issues.md#i-16) señalaba además que las inferidas dentro de un bloque de categoría hacían variar su contenido.
- **Decisión (aceptada: «si»):**
  - Entrenamiento, con revisión humana: el usuario revisa los bloques nuevos del catálogo, las cuestiones inferidas, las especializaciones y las importancias, y calibra con el conjunto de casos; lo aprobado pasa a «validado».
  - Ejecución, totalmente automática: se usan los bloques del catálogo; si la categoría no está, el motor genera y redacta el bloque, lo usa marcado «no revisado» y lo encola. Las inferidas y las especializaciones nuevas se usan como provisionales y se encolan.
  - Trazabilidad: cada resultado indica qué partes del modelo usó sin revisar, para que la auditoría pueda informar con ellas y sin ellas.
  - Una cuestión inferida se usa en la ejecución como añadido provisional del modelo, marcado y fuera de la clave; al aceptarse, se incorpora al bloque del catálogo como nueva versión. Resuelve I-16.
- **Interpretaciones adoptadas:**
  - Matiza [D-022](#d-022), D-036, [D-038](#d-038) y D-040: sus validaciones se hacen en entrenamiento, y las cuestiones inferidas dejan de ir directamente al bloque de su categoría (D-038). El texto citado de D-036 («el usuario valida siempre las críticas…») se mantiene: «siempre» significa que ninguna crítica queda sin revisar, no que la ejecución espere.
  - La regla va al canon (`demand-model`, vigente); la operación del catálogo, al método (`requirement-blocks`, propuesta). La implantación de la redacción automática, la caché y la cola en el motor queda fuera de la documentación.
  - Alcance: las palabras del usuario son generales, pero el update se refiere a la construcción del modelo de demanda (catálogo, inferidas, especializaciones e importancias). Las revisiones humanas del MPIR y de la auditoría no se tocan; si el principio se extiende a ellas queda abierto en [OQ-46](open-questions.md).
  - La revisión independiente detectó tres lagunas de estados y versiones (qué cuenta como «no revisado», muestra frente a aceptación de las inferidas, versión del bloque en la clave): [I-19](issues.md#i-19).
- **Consecuencias:** [demand-model](../10-model/demand-model.md#entrenamiento-y-ejecución) 2.3; [study-class](../10-model/study-class.md#criterio-de-especialización) 1.1; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.4; [cases](../20-methods/product-taxonomy/cases.md) 1.5; I-16 resuelta; nuevas I-19 y OQ-46; glosario (entrenamiento, ejecución).
- **Relacionado:** D-022, D-036, D-038, D-040, I-16, I-19, OQ-46.

### D-042

**Capa original del MPIR: sin capturas de pantalla y políticas de acceso del motor.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-mpir-capture-engine`, tareas T-002 y T-013. El usuario pidió empezar el MPIR por la infraestructura y un motor de captura que evite bloqueos sin tardar «una eternidad». Claude propuso conservar también una captura de pantalla por recurso; el usuario respondió: «no hace falta captura de pantalla. Implementa el motor».
- **Decisión:**
  - La capa original del MPIR no conserva capturas de pantalla. El método no las exige y evitan la tentación de juzgar por la prominencia (cautela 4: «prominencia editorial ≠ importancia relativa»).
  - Entre las políticas aplicables que el método manda respetar, el motor aplica robots.txt (RFC 9309) y las reservas de minería de textos y datos expresadas por medios de lectura mecánica (art. 67.3 TRLPI: TDMRep, cabecera y meta `tdm-reservation`).
- **Interpretaciones adoptadas:**
  - Las políticas de acceso precisan «el rastreo respetará las políticas aplicables» y no crean conceptos. Aplicar una reserva significa no conservar el contenido del recurso; sí se conservan los metadatos de la visita.
  - La divergencia sobre el renderizado (el motor renderiza siempre) no se resuelve aquí: se registra en [I-18](issues.md#i-18).
  - OQ-14 y OQ-15 quedan anotadas con lo que fija el motor de forma provisional, sin cerrarse: la configuración definitiva la decide la sonda T-014.
- **Consecuencias:** [sampling-capture](../20-methods/mpir/sampling-capture.md#qué-se-conserva-en-la-capa-original) 1.1; I-18 abierta; OQ-14 y OQ-15 anotadas.
- **Relacionado:** I-18, OQ-14, OQ-15.

### D-043

**Criterios de redacción del catálogo de bloques de categoría.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-catalog-criteria`, tarea T-016. Tres agentes redactaron un borrador de 27 bloques de categoría ([D-040](#d-040)) con criterios distintos: importancia de las medidas, atributos con muchos valores, solapes con la capa general, propiedades repetidas de Amazon y cuestiones inferidas.
- **Decisión (aceptada: «si»):** cinco criterios (el 1, enmendado por [D-055](#d-055): la medida descriptiva puede ser crítica si lo dicen los votos de su clase): una medida es crítica cuando fija qué se vende y principal cuando solo describe; los atributos que mezclan temas se dividen por tema; un bloque de categoría solo repite una cuestión general si la concreta con algo propio de la clase, y las piezas incluidas pasan a esp.juego; una propiedad de Amazon repetida en categorías hermanas sube a la madre común solo si vale para todas sus hijas; las cuestiones inferidas propuestas se incluyen como provisionales y el usuario las aprueba una a una.
- **Interpretaciones adoptadas:**
  - Son criterios de método (`requirement-blocks`, propuesta) que aplican las pruebas de importancia de [D-035](#d-035) y la asignación de [D-040](#d-040); no cambian el canon.
  - El criterio 4 completa la lectura de D-040 sobre las propiedades de Amazon (que van a la categoría que la tabla de correspondencia asocia a su PTD).
  - Las tres tareas anunciadas por Claude se recogen en el método: la composición textil con origen «normativa» (Reglamento (UE) 1007/2011, art. 16.1, comprobado en el DOUE L 272 de 18.10.2011; importancia principal), la lectura de las propiedades descriptivas del grupo de cumplimiento de Amazon y la entidad «producto» para el color.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#criterios-de-redacción-del-catálogo) 1.5; el catálogo de `demand-engine/catalog/cat/` se corrige con estos criterios.
- **Relacionado:** D-035, D-038, D-040, D-041.

### D-044

**Marco humano y reglas inducidas: el usuario define el marco, no revisa reglas ni requisitos.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-induced-rules`, tarea T-016. [D-041](#d-041) preveía que en entrenamiento el usuario revisara bloques, inferidas, especializaciones e importancias, y [D-036](#d-036) que validara siempre las inferidas críticas. Ante el borrador del catálogo de bloques de categoría, el usuario rechazó la revisión manual de requisitos y también la de reglas sueltas.
- **Decisión:**
  - Palabras del usuario: «Lo que defino es el marco general, objetivos, características del resultado, etc. Las reglas concretas deben ser producto del entrenamiento también» y «La parametrización específica puede formar parte del sistema, pero como un resultado compilado, no como un diseño específico».
  - Marco del usuario, única intervención humana: propósito, objetivos y características del resultado, criterios de éxito e invariantes del canon. El usuario lee el informe agregado del entrenamiento y, si hace falta, ajusta el marco. (Precisada por [D-059](#d-059): «críticos pocos» sale del marco.)
  - Entrenamiento en ocho pasos (reunir casos, aplicar las reglas vigentes dos veces por caso, medir contra el marco, detectar patrones, inducir reglas generales y específicas, compilar el catálogo, validar automáticamente, publicar versión e informe) y ejecución automática con lo compilado, según el diagrama aprobado («documenta»).
- **Interpretaciones adoptadas:**
  - Enmienda D-041 (el entrenamiento ya no es una revisión humana) y [D-036](#d-036) (la validación de las inferidas la hace el entrenamiento contra el marco). Precisa [D-022](#d-022) (la «validación del usuario» de una especialización pasa a ser la del entrenamiento), [D-039](#d-039) (la relevancia de las propiedades de Amazon la deciden las reglas inducidas, paso 5 del entrenamiento) y [D-040](#d-040) (el catálogo se compila, no se revisa a mano). Sustituye el criterio 5 de [D-043](#d-043) (la aprobación una a una de las inferidas) por la validación automática.
  - Las decisiones ya aceptadas del canon, incluidos los criterios de [D-035](#d-035) y D-043, forman parte del marco: las reglas inducidas operan dentro de ellas. Si el entrenamiento las encuentra contraproducentes, lo dice en el informe agregado; no las cambia.
  - La capa general ([D-034](#d-034), [D-038](#d-038)) está dentro del rango «D-020 a D-043» del marco: el principio «ningún bloque ni importancia se diseña a mano» se aplica al catálogo que compila el entrenamiento, no a la capa general. Sus importancias siguen siendo valores por defecto.
  - La revisión de la importancia por defecto «por clase con justificación» ([D-033](#d-033), [D-034](#d-034)) la hacen las reglas específicas inducidas en el entrenamiento; la ejecución no revisa importancias. (Precisada por [D-045](#d-045): no se aplica a la capa general, que queda fija.)
  - «Cada requisito guarda la regla que lo decidió» se traduce en un campo «regla» del requisito en el formato del catálogo.
  - «No revisado», en la cita de la ejecución de D-041, significa no compilado por el entrenamiento.
  - Va a `10-model` como vigente, en un módulo nuevo, `model-training`, que recibe la sección «Entrenamiento y ejecución» de `demand-model`. El diagrama no fija el vocabulario de rasgos, la forma operativa de las métricas ni el formato del informe: [OQ-47](open-questions.md).
- **Consecuencias:** nuevo módulo [model-training](../10-model/model-training.md) 1.0; [demand-model](../10-model/demand-model.md#entrenamiento-y-ejecución) 2.4; [study-class](../10-model/study-class.md#criterio-de-especialización) 1.2; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.6; D-039 precisada; I-17 e I-19 anotadas; OQ-02 y OQ-46 anotadas; nueva OQ-47; glosario (entrenamiento, ejecución, marco, regla inducida, catálogo compilado, bloque de requisitos, criterio de especialización); índice de `docs/README.md`.
- **Relacionado:** D-022, D-033, D-034, D-035, D-036, D-038, D-039, D-040, D-041, D-043, I-17, I-19, OQ-02, OQ-46, OQ-47.

### D-045

**Operación del entrenamiento, primera versión: rasgos, reglas de importancia por el árbol de Shopify y métricas.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-training-operation`, tarea T-019. [OQ-47](open-questions.md) dejaba abiertos el vocabulario de rasgos, la forma operativa de las métricas, el informe agregado y los casos de entrenamiento; [I-19](issues.md#i-19), la versión de los bloques en la clave y el estado de los bloques generados en ejecución. Claude propuso un plan para una primera versión. El usuario objetó que las reglas de importancia se miraran a nivel global («Lo único que no me encaja es que se mire a nivel global. Estas reglas deberían ser al menos para clases generales»). Claude respondió que lo global contradice D-035 («principal» es relativo a la clase) y arrastraría el sesgo textil del catálogo, y que solo por clase no generaliza; el usuario aprobó la opción C (por el árbol de Shopify) y el resto del plan. Después, con su matiz sobre el entrenamiento a escala ([D-046](#d-046)), aprobó los ajustes de los casos y de la cobertura.
- **Decisión:**
  - **Rasgos:** el rasgo principal de un requisito es qué resuelve la cuestión, de una lista cerrada (identidad, contenido, medida que fija lo vendido, medida descriptiva, material, construcción, prestación, uso y compatibilidad, seguridad, cuidado, estética, certificación u origen), más la entidad, el origen, la aplicabilidad y la posición del bloque. Cada atributo de Shopify o propiedad de Amazon se etiqueta una sola vez y se reutiliza. (Enmendada por [D-056](#d-056): la lista deja de ser cerrada; los agentes proponen y votan rasgos.)
  - **Reglas de importancia por el árbol de Shopify:** la regla vive en la clase y sube a la categoría madre solo si vale para todas sus hijas (el principio de [D-043](#d-043), criterio 4). El crítico es global. Su prueba no depende de la clase: «sin la cuestión, ¿se sabe qué se vende, cuánto cuesta y si se puede adquirir?». A una clase sin regla no se le aplica la de otra rama: se usa la importancia que propone el agente, provisional y encolada. Las importancias de partida salen del catálogo y de los votos de los agentes con las pruebas de [D-035](#d-035); manda la regla compilada. El marco pone límites que ninguna regla puede saltarse: «ninguna regla puede hacer crítica la estética, ni tocar la capa general ni el criterio de las medidas». (Enmendada por [D-055](#d-055): el crítico se decide por requisito y clase con esa misma prueba, y la medida descriptiva puede ser crítica.) (Enmendada por [D-058](#d-058): un requisito cuyos votos contradicen la regla de su rasgo en una clase tiene su propia regla, y cualquier propiedad puede ser crítica; desaparece el límite «ninguna regla puede hacer crítica la estética».)
  - **Métricas, sin umbrales:** cobertura (en el conjunto de control, cuestiones clave esperadas presentes; en el catálogo de entrenamiento, hechos declarados sin pregunta en el modelo); estabilidad (mismo resultado en dos ejecuciones: composición, bloques e importancia); coherencia (cuántos requisitos con los mismos rasgos tienen importancias distintas). Una regla se acepta si ninguna métrica empeora y al menos una mejora.
  - **Casos:** el conjunto de entrenamiento es un catálogo grande capturado con el motor de captura compartido ([D-046](#d-046)); los 14 casos actuales son el conjunto de control.
  - **Alcance de la primera versión:** solo se induce la importancia; para composición, especializaciones, relevancia de Amazon e inferidas se miden las divergencias y el informe las agrupa por patrón.
  - **I-19:** la clave del modelo lleva la versión de cada bloque; un bloque generado en ejecución lleva el estado «no compilado» hasta que el entrenamiento lo compila.
  - **Ejecución:** un comando de Claude Code (`/demand-model URL`) que lanza los agentes y llama al código determinista, para probar productos reales; el entrenamiento a escala, por lotes con la API (T-020). (Enmendada por [D-054](#d-054): el entrenamiento a escala clasifica con agentes de Claude Code.)
- **Interpretaciones adoptadas:**
  - La opción C sustituye solo el ámbito global del punto 2 («lo único que no me encaja es que se mire a nivel global»); el resto del mecanismo explicado se mantiene: etiquetas, regla que sale de las importancias con la misma etiqueta, excepciones constantes como reglas específicas, votos, «manda la regla» y límites del marco.
  - Se incorpora a `10-model` como vigente, igual que D-044: es la operación aprobada para la primera versión; lo que no fija queda en OQ-48 y OQ-49.
  - «Vale para todas sus hijas» cuenta las hijas que tienen requisitos o votos de ese rasgo. Una regla sube cuando al menos dos hijas con datos la comparten y ninguna la contradice. Es un mínimo estructural, no un umbral de calidad: con una sola hija no se distingue la regla de la madre de la de la hija, y subir aplicaría a sus hermanas la regla de otra rama, que el artefacto excluye. Es la misma lectura que D-043, criterio 4, que trata de una propiedad «en varias categorías hermanas». Las hijas sin datos heredan la regla de la madre. Las reglas no suben por encima de las verticales de Shopify: una vertical sin datos no hereda reglas de otra.
  - En el ejemplo del artefacto, Cojines no es hija de Ropa de casa (cuelga de Decoración), así que su excepción no impide que la regla de la estética suba a Ropa de casa.
  - Dentro de una misma clase, la regla es la importancia mayoritaria de sus requisitos y votos («la regla sale de mirar qué importancia tienen hoy los requisitos con la misma etiqueta»). En un empate, Claude elige la más alta, por analogía con que la duda no baja la importancia ([D-035](#d-035)); es una elección propia, revisable en el marco.
  - La importancia de un requisito en un modelo se resuelve desde la clase del producto hacia arriba: la regla más específica del rasgo en la cadena de la categoría. En un juego, desde cada pieza a la que se aplica el bloque, y se toma la más alta. (Enmendada por [D-058](#d-058): primero la excepción del requisito, si la tiene.)
  - «El crítico es global» y su prueba («¿se sabe qué se vende, cuánto cuesta y si se puede adquirir?»): solo pueden ser críticos los rasgos que dicen qué se vende (identidad, contenido, medida que fija lo vendido). La medida que fija lo vendido es siempre crítica y la medida descriptiva siempre principal (D-043, criterio 1). Para identidad y contenido, si son críticos lo decide una regla global; si no lo son, el árbol decide entre principal y complementario. Un voto crítico en otro rasgo cuenta como principal y el informe lo señala. El artefacto solo excluye expresamente la estética; la restricción a tres rasgos es lectura de Claude (el catálogo solo tiene críticos de esos rasgos) y tiene un riesgo: una cuestión de compatibilidad o de seguridad que fijara qué se vende no podría ser crítica. Se revisa en el marco si el informe lo muestra. (Enmendada por [D-055](#d-055): el crítico se decide por requisito y clase, y la medida descriptiva puede ser crítica; por [D-056](#d-056), también pueden serlo los rasgos nuevos que dicen qué se vende.) (Sustituida por [D-058](#d-058) en cuanto a qué rasgos pueden ser críticos: cualquier propiedad, si sus votos lo dicen.)
  - «Coherencia» se mide dentro de cada clase: requisitos con el mismo rasgo en la misma clase. Una excepción legítima de una clase (la estética de Cojines) no cuenta como incoherencia, porque la opción C la admite. (Precisada por [D-055](#d-055): un crítico por requisito tampoco es incoherencia.) (Generalizada por [D-058](#d-058): ninguna excepción por requisito cuenta como incoherencia.)
  - «No tocar la capa general»: sus importancias quedan fijas como parte del marco, y ninguna regla, general ni específica, las revisa por clase. Enmienda en este punto [D-034](#d-034) («revisables por clase con justificación») y la interpretación de D-044 sobre la revisión por clase, que queda para los bloques de categoría. La capa general no tiene estado de compilación: no es «no compilado» ni se encola.
  - «Compila al vuelo» un bloque generado en ejecución: se le aplican el índice de rasgos y las reglas vigentes; queda en estado «no compilado» («no revisada» en la cita de D-044) hasta que lo compila el entrenamiento. Si su rama no tiene regla, la importancia es el voto del agente, provisional.
  - **Quién decide cada cosa en la primera versión:** la importancia, las reglas compiladas (o el voto, sin regla); la composición, las especializaciones, las inferidas y la aplicación, el clasificador, con las especializaciones y las inferidas siempre provisionales; la relevancia de las propiedades de Amazon, la redacción automática del bloque cuando se genera. Las reglas de las demás decisiones quedan en OQ-49. (Enmendada por [D-055](#d-055) y [D-056](#d-056): el crítico lo deciden las reglas por requisito y clase, y el rasgo, los votos de los agentes.)
  - En el rasgo «certificación u origen», «origen» es el lugar de fabricación; no es el origen del requisito (referencias, inferida o normativa), que es otro rasgo.
  - Un requisito toma el rasgo de sus fuentes. Las cuestiones inferidas y las de especialización, sin fuente de referencia, se etiquetan en el propio requisito. (Enmendada por [D-056](#d-056): manda el rasgo votado del requisito; el de las fuentes es el de partida.)
  - Los votos los emite el agente de cada caso para los requisitos de categoría, especialización e inferidos de su modelo, no para la capa general, que es fija. Se registran con la clase en que se emiten.
  - **Cobertura:** las cuestiones clave esperadas se miden en el conjunto de control; los hechos declarados sin pregunta, en todos los casos. Cuentan todos los hechos declarados menos lo estético y lo promocional (el artefacto) y los beneficios reclamados, que [D-025](#d-025) deja fuera de la clase.
  - **Informe agregado:** métricas frente a la versión anterior, reglas añadidas o retiradas con el número de requisitos que decide cada una, votos que contradicen el marco, lo usado sin compilar y las divergencias de las decisiones no inducidas agrupadas por patrón.
  - **Estados:** los estados del bloque de [D-038](#d-038) (propuesta o validado) pasan a ser no compilado o compilado. El catálogo actual está no compilado hasta la primera compilación.
  - **Versión en la clave:** cada bloque se escribe `<bloque>@<versión>`.
- **Consecuencias:**
  - módulos: [model-training](../10-model/model-training.md#operación-de-la-primera-versión) 1.1, [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.5 y [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.7;
  - decisiones: D-034 enmendada (capa general fija), D-038 enmendada (estados y clave), D-040 y D-044 precisadas;
  - registros: OQ-47 cerrada, I-19 resuelta, I-17 y OQ-02 anotadas; nuevas OQ-48 (selección del catálogo de entrenamiento) y OQ-49 (inducción de las demás decisiones);
  - glosario: rasgo, voto, conjunto de control, regla inducida y catálogo compilado.
- **Relacionado:** D-025, D-034, D-035, D-038, D-040, D-043, D-044, D-046, I-17, I-19, OQ-02, OQ-47, OQ-48, OQ-49.

### D-046

**Motor de captura compartido por el MPIR y el entrenamiento del modelo de demanda.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-training-operation`, tareas T-019 y T-020. El motor de captura se construyó para la capa original del MPIR (T-013, [D-042](#d-042)). Al plantear el entrenamiento del modelo de demanda, el usuario fijó su alcance.
- **Decisión:**
  - Palabras del usuario: «El entrenamiento lo vamos a hacer con un catálogo de miles de productos de diferentes tipos. Deberá usar el motor de captura del MPIR, que está preparado para el scraping. Entonces el motor de captura ya no es algo exclusivo del MPIR. Es algo que nos permite capturar información de ecommerce de referencia. Tenemos un motor de captura compartido para el modelo de taxo y MPIR».
  - El catálogo de entrenamiento ([D-045](#d-045)) se captura con ese motor, sin Amazon.es.
  - El código se traslada a un módulo de captura común en una tarea aparte (T-020), porque otra sesión trabaja con el motor (T-014, T-015). En la documentación solo se declara que es compartido.
- **Interpretaciones adoptadas:**
  - «Modelo de taxo» es el modelo de demanda que construye `demand-engine` con la taxonomía.
  - Las políticas de acceso del motor ([D-042](#d-042): robots.txt y reservas de minería de textos y datos) se aplican igual a las capturas del entrenamiento, porque son del motor. Lo demás de D-042 sigue siendo propio de la capa original del MPIR.
  - La selección de tiendas y fichas queda abierta: [OQ-48](open-questions.md).
- **Consecuencias:** [model-training](../10-model/model-training.md#operación-de-la-primera-versión) 1.1; mapa del código en `CLAUDE.md` y en `demand-engine/README.md`; glosario (motor de captura); nueva OQ-48.
- **Relacionado:** D-042, D-045, OQ-11, OQ-12, OQ-48.

### D-047

**El modelo de demanda va con el producto; la aplicación, con la oferta.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-offer-application`, tarea T-019. [D-033](#d-033) y [D-038](#d-038) identificaban el modelo por sus bloques más la aplicación, y el nombre terminaba en la aplicación («— unidad no nueva, con descuento»). El usuario propuso tratar las promociones como requisitos siempre presentes y, al estudiarlo, sacar la aplicación de la denominación.
- **Decisión:**
  - Palabras del usuario: «Consideremos sacar la aplicación de la denominación. Ya que parecen ser cuestiones de estado temporal. Entonces las vinculamos a la oferta y no al producto. Modelo de demanda se vincula al producto, aplicación a la oferta».
  - **Modelo de demanda (producto):** bloques de categoría y especialización. Clave: sus bloques con versión. Nombre: «Categorías (alias) · especializaciones».
  - **Aplicación (oferta):** las condiciones activas de esa oferta. No entra en la clave ni en el nombre del modelo; se registra con la oferta. Una oferta sin condiciones activas es **estándar**: es un resultado comprobado, no una ausencia.
  - Lo que se audita es la oferta: el modelo de su producto más su aplicación. Los requisitos condicionados que no se dan en esa oferta quedan en gris, como NA justificado; la pregunta universal nunca es NA.
  - `gen.elementos-digitales` es del producto: entra en el modelo, como un bloque más de la clave («Televisores · con elementos digitales»). Las variantes son de la oferta.
- **Interpretaciones adoptadas:**
  - «Estado temporal» se lee como todo lo que depende de la oferta y no del producto: variantes ofrecidas, unidad no nueva, descuento, cantidad limitada, precio personalizado y suscripción o depósito. Los elementos digitales no son un estado de la oferta.
  - Lo que pone en gris un requisito condicionado es el hecho declarado, como en [D-037](#d-037). Si la ficha no declara la condición, sus requisitos son NA, el estado del canon que «se justifica y se separa de las unidades pertinentes». En el descuento, la duda de si lo hay se valora una sola vez, en la pregunta universal de promociones ([D-049](#d-049)). Las demás condiciones (precio personalizado, suscripción…) no tienen pregunta universal: sin hecho declarado, sus requisitos son NA.
  - **La capa general forma parte de todo modelo.** El artefacto dice que el detalle condicionado «está siempre en el modelo» y vive «en el modelo del producto». Por eso todo modelo incluye la capa general completa, universal y condicionada con su disparador. Lo que distingue un modelo son sus bloques de categoría y de especialización y los condicionados del producto; la aplicación es la lista de condiciones de la oferta que se dan, no un conjunto de bloques.
  - La clave empieza por la versión de la capa general (`gen@<versión>`), común a todos los modelos, para que un cambio del marco quede trazado; después van los bloques que distinguen el modelo, con su versión ([D-045](#d-045)).
  - En el nombre del modelo, un bloque de la capa general que sea del producto se nombra tras las especializaciones con su nombre breve («con elementos digitales»).
  - «Estándar» sustituye al «—» del estudio. Se descartan «por defecto», ya usado para la importancia, y «general», que choca con «capa general». Significa que el clasificador no encuentra ninguna condición declarada; no afirma los hechos (unidad nueva, precio sin rebaja…), y cuándo vale como «no» lo que la ficha calla lo fija la auditoría ([OQ-50](open-questions.md)).
- **Consecuencias:**
  - módulos: [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.6, [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.8 y [cases](../20-methods/product-taxonomy/cases.md) 1.6;
  - decisiones: D-033 y D-038 enmendadas en la identidad, la clave y el nombre; D-034 precisada (elementos digitales);
  - glosario: aplicación, ahora de la oferta, y oferta estándar.
- **Relacionado:** D-033, D-034, D-037, D-038, D-048, D-049.

### D-048

**La oferta no aporta requisitos: activa requisitos condicionados de la clase.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-offer-application`, tarea T-019. Con [D-047](#d-047), el usuario preguntó cómo se resuelve que la aplicación traiga requisitos que no podrían haberse inferido sin ella: la salud de la batería de un móvil reacondicionado, que [D-037](#d-037) dejaba como posible especialización de oferta.
- **Decisión:**
  - La oferta nunca aporta requisitos: solo activa requisitos condicionados que viven en el modelo del producto (capa general o bloques de la clase).
  - Una cuestión que solo procede con una condición de la oferta es un requisito condicionado del bloque de la clase (p. ej., en smartphones, la salud de la batería, aplicable si la unidad no es nueva). El producto nuevo y el reacondicionado comparten modelo; en la oferta estándar la pregunta está en gris.
  - Se descubre como cuestión inferida de la clase con esa aplicabilidad: provisional y encolada, hasta que el entrenamiento la incorpora al bloque como nueva versión.
  - Una condición de oferta que la capa general no tenga (p. ej., preventa o reserva) es un hueco del marco: el informe del entrenamiento la señala y no se inventa.
- **Interpretaciones adoptadas:**
  - Sustituye [D-027](#d-027): no hay especializaciones de oferta, y la condición 1 del criterio de especialización solo admite características del producto. El requisito condicionado es el de [D-024](#d-024).
  - Precisa D-037: la salud de la batería del reacondicionado, su ejemplo hipotético, pasa a ser un requisito condicionado de la clase. El otro ejemplo (repuestos y accesorios de bienes de fin de serie) no tiene disparador en la capa general (un fin de serie puede ser nuevo): sería un hueco del marco, según el último punto de la decisión.
  - La «clase de oferta» (BASE §4) se lee como las ofertas de una clase de producto, cada una evaluada con el modelo de su producto más su aplicación; no crea clases. Anota OQ-37.
  - El ejemplo de la batería es hipotético; ninguno de los 14 casos lo tiene.
- **Consecuencias:**
  - módulos: [study-class](../10-model/study-class.md#criterio-de-especialización) 1.3 (condición 1) y [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#cuestiones-inferidas) 1.8;
  - registros: OQ-37 anotada;
  - glosario: especialización, especialización de oferta (retirada) y requisito condicionado.
- **Relacionado:** D-024, D-027, D-037, D-041, D-045, D-047.

### D-049

**Pregunta universal de promociones y descuentos.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-offer-application`, tarea T-019. La capa general solo tenía la parte condicionada del descuento (`gen.descuento`). El usuario propuso tratar promociones y descuentos como requisitos siempre presentes, porque «responder que no hay promoción o descuento podría ser útil y esto podría aplicar a cualquier producto del mundo».
- **Decisión:** la capa general añade una cuestión universal sobre si la oferta tiene alguna promoción o descuento vigente y en qué consiste. Un «no» fundamentado la resuelve. Los detalles siguen en `gen.descuento`, condicionado a la oferta, y quedan en gris cuando no hay descuento ([D-047](#d-047)).
- **Interpretaciones adoptadas:**
  - Con D-047, la aplicación ya no forma parte de la identidad. De la propuesta queda la pregunta universal, como recomendó Claude («para las promociones basta añadir la pregunta universal «¿tiene promoción o descuento?», si se quiere que un «no» cuente»), aprobada con «todo aparece OK».
  - Redacción del borrador: «¿Tiene la oferta alguna promoción o descuento vigente (rebaja, cupón, regalo, unidades gratis…) y en qué consiste?». Importancia por defecto: complementaria, la del borrador. Es un valor de la capa general, que es marco ([D-045](#d-045)).
  - Las dos preguntas condicionadas del borrador (precio anterior y cuánto se rebaja; condiciones y vigencia) no se incorporan, siguiendo «los detalles siguen siendo condiciones de la oferta»: queda `gen.descuento/01`, que pregunta por el precio de referencia y las condiciones, pero no por la vigencia, y solo se activa con descuento, no con promociones sin rebaja (regalo, unidades gratis). Ese hueco queda en OQ-50.
  - Cuándo vale derivar el «no» de una ficha que no lo dice (precio sin tachar ni etiqueta) es una regla de la auditoría: [OQ-50](open-questions.md).
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.8 (fila nueva en la capa general); `demand-engine/catalog/gen.json` (`gen/16`, capa general en la versión 0.2); nueva OQ-50.
- **Relacionado:** D-034, D-037, D-045, D-047.

### D-050

**Filtro de relevancia aprendido: lo no relevante sale del modelo de la clase.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-relevance-origin`. En la pasada de control, el modelo del pienso incluía el color, el estampado y el material, heredados de los bloques de sector de Productos para mascotas y Productos para perros ([D-040](#d-040)), y los agentes los votaron «complementario» porque no tenían otra opción. El usuario: «Nuestro modelo solo debe incluir cuestiones relevantes, las complementarias siendo las de menor relevancia».
- **Decisión** (opción A de Claude, aprobada con «OK»):
  - Antes de la importancia, cada requisito pasa una prueba de relevancia: «¿informa sobre algo que importa para evaluar o comparar ofertas de esta clase?». Si no la pasa, sale del modelo de esa clase. No es un cuarto nivel de importancia: la escala sigue siendo crítico, principal y complementario.
  - Lo decide el entrenamiento: los agentes votan con un cuarto valor, «no relevante», y se inducen reglas de relevancia por requisito y clase a lo largo del árbol de Shopify, con el mismo mecanismo que la importancia ([D-045](#d-045)).
  - Sin regla compilada, la duda no excluye: un requisito votado «no relevante» se queda en el modelo, marcado como provisional («relevancia dudosa»), y se encola.
  - Nunca se excluyen la capa general, los requisitos normativos ni la medida que fija lo vendido.
  - Lo excluido se lista aparte con su regla. No es NA: no forma parte de lo que se audita.
  - La validación añade la coherencia de relevancia y una salvaguarda de cobertura: una exclusión que deja sin pregunta un hecho que declaran las fichas de la clase empeora la cobertura, y la regla se descarta.
- **Interpretaciones adoptadas:**
  - Los datos de partida son el catálogo (un requisito incluido en un bloque es relevante en su categoría) y los votos, registrados en la clase del producto. La regla es la mayoría en la clase; en empate, relevante. Sube a la madre con el mínimo estructural de D-045 (al menos dos hijas con datos, sin ninguna en contra) y no por encima de las verticales.
  - Se amplía el alcance de la primera versión de D-045: además de la importancia, se induce la relevancia. Las demás decisiones siguen en [OQ-49](open-questions.md).
  - «Se queda como complementario» (artefacto) se aplica cuando el requisito no tiene regla de importancia. Si la tiene, conserva su nivel: manda la regla compilada (D-045), y la duda no baja la importancia ([D-035](#d-035)).
  - La prueba es la de la condición 3 del criterio de especialización: cuestiones «relevantes para evaluar la clase, no para un comprador concreto» ([D-022](#d-022)). Se descartan la opción B (decidirlo solo al redactar el bloque, que no resuelve los bloques de sector) y la C (resolverlo en la auditoría con NA, que mezcla «no aplica» con «no importa»).
  - El filtro va antes de la importancia. El marco fija la importancia de lo relevante, no su relevancia: una medida descriptiva o una identidad pueden excluirse en una clase si sus votos lo dicen. Solo protegen de la exclusión la capa general, lo normativo y la medida que fija lo vendido.
  - En un modelo de varias piezas, un requisito solo se excluye si lo excluyen todas las clases a las que se aplica. El dato del catálogo cuenta como un voto «relevante» en la categoría del bloque.
  - Con la relevancia de las propiedades de Amazon ([D-039](#d-039)) se distinguen dos decisiones: incluir la propiedad en el bloque (la redacción del bloque) y excluirla en una clase concreta (este filtro). La salvaguarda de cobertura evita en parte el hueco de [I-17](issues.md#i-17).
  - Hay tres casos distintos: «no relevante para la clase» (este filtro); «no aplica al producto», como el número de hilos en unas sábanas de coralina, que es un requisito condicionado a un hecho del producto ([D-024](#d-024)) y queda en gris en la auditoría; y «no aplica a la oferta» ([D-047](#d-047)).
  - En la pasada de control no había votos «no relevante» (el valor no existía): las primeras reglas de relevancia saldrán de las próximas ejecuciones.
- **Consecuencias:**
  - módulos: [model-training](../10-model/model-training.md#relevancia) 1.2, [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.7 y [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.9;
  - registros: I-17 anotada y retitulada, OQ-49 anotada;
  - glosario: filtro de relevancia;
  - motor: votos de relevancia, reglas `rel:` y lista de excluidos.
- **Relacionado:** D-022, D-024, D-035, D-039, D-040, D-045, D-047, I-17, OQ-49.

### D-051

**Peso, grosor y gramaje: rasgo «magnitud física», fuera de la regla de las medidas.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-relevance-origin`. La regla del marco «la medida descriptiva es principal» ([D-043](#d-043), criterio 1) tuvo 27 votos en contra en la pasada de control con las reglas 1 (informe `demand-engine/training/reports/2026-10-25-v2-report.md` de entonces). Claude explicó en la conversación que el criterio habla de «la medida o la talla», con dimensiones y tallas como ejemplos, y que el peso, el grosor y el gramaje habían entrado en «medida descriptiva» por la definición del vocabulario que él redactó. Los votos sobre esas tres magnitudes dependen de la clase: el gramaje es principal en toallas y en la manta polar, y complementario en fundas nórdicas y en el protector.
- **Decisión** (opción A, «2. Confirmo»): el peso, el grosor y el gramaje salen de «medida descriptiva» y pasan a un rasgo propio, **magnitud física**, sin regla fija: su importancia la decide el árbol por clase. D-043, criterio 1, se aplica a las dimensiones y las tallas.
- **Interpretaciones adoptadas:**
  - El vocabulario cerrado de D-045 pasa a tener 13 rasgos. (Enmendada por [D-056](#d-056): son el vocabulario de partida, que amplían los agentes.)
  - Las dimensiones de detalle (altura de tacón, medidas de uso del sofá, largo reclinado) siguen bajo D-043, criterio 1, hasta tener datos del entrenamiento a escala: [OQ-51](open-questions.md).
  - Una pregunta que mezcla una dimensión con un peso se etiqueta por su parte dominante.
- **Consecuencias:** [model-training](../10-model/model-training.md#rasgos) 1.2; glosario (rasgo); catálogo reetiquetado y recompilado; nueva OQ-51.
- **Relacionado:** D-043, D-045, OQ-51.

### D-052

**Fabricante, país de fabricación y seguridad en la capa general, según su origen.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-relevance-origin`. Seguían pendientes dos propuestas de Claude para la capa general. La primera, el país de fabricación, era casi el único hecho declarado sin pregunta en la pasada de control. La segunda era el art. 19 del Reglamento (UE) 2023/988 de seguridad general de los productos (GPSR), comprobado antes en la sesión: fabricante y contacto, persona responsable en la UE, identificación del producto, y advertencias e información de seguridad. El usuario respondió: «Según su origen. Si es claramente por normativa, lo ponemos en normativa».
- **Decisión:**
  - Lo que exige el art. 19 del GPSR entra en la capa general con origen «normativa»:
    - la marca, el modelo y los identificadores (gen/02 y gen/03) pasan de «inferida» a «normativa» (art. 19.a y 19.c);
    - nuevas cuestiones: fabricante y contacto (19.a), complementaria; persona responsable en la UE si el fabricante no está establecido en ella (19.b), complementaria y condicionada; advertencias e información de seguridad (19.d), principal.
  - El país de fabricación entra como cuestión universal, complementaria, con origen «referencias»: no hay una obligación legal general comprobada, y lo recoge una referencia común a todos los tipos de producto.
- **Interpretaciones adoptadas:**
  - «Según su origen» se lee como el campo de origen de cada requisito: «normativa» solo si una norma lo exige con claridad; si no, la fuente que lo apoya. Las importancias son las de las propuestas de Claude, que el usuario no objetó. La capa general es marco ([D-045](#d-045)).
  - Se descarta otra lectura: que lo no normativo entre por el camino de su fuente, es decir, `country_of_origin` en los bloques de categoría ([D-039](#d-039), [D-040](#d-040)). La propiedad está en los 1.877 PTD de Amazon (`amazon-ptd@2026-10-24`; etiqueta «País de origen», y «País de publicación» en 33 PTD de mascotas). Ir por los bloques la repetiría en todos ellos, con la inestabilidad que ya se vio: los agentes la pusieron como inferida en tres bloques distintos. Una cuestión de cualquier producto va en la capa general. Esto amplía D-039, que solo admitía los PTD como fuente de la categoría. El apoyo es la presencia de la propiedad en el PTD, no su obligatoriedad, que es un requisito de la plataforma.
  - El GPSR no se aplica a alimentos ni piensos, entre otras exclusiones (art. 2.3). Las cuestiones del fabricante y de las advertencias siguen siendo universales: tienen sentido en cualquier producto, y un «no» o los datos del operador las resuelven. Su origen es normativo por el GPSR, y fuera de su ámbito su apoyo normativo está por comprobar ([OQ-45](open-questions.md)). Lo mismo vale para la marca, el modelo y los identificadores.
  - La persona responsable en la UE es un requisito condicionado a un hecho del producto (el fabricante no está establecido en la UE) dentro del bloque universal, como los requisitos condicionados de los bloques de categoría ([D-024](#d-024)). Lo evalúa la auditoría y no distingue el modelo. Precisa [D-034](#d-034) y [D-047](#d-047): un bloque universal puede llevar requisitos condicionados a un hecho del producto; sus demás cuestiones se aplican siempre.
  - La «imagen» que pide el art. 19.c no es una cuestión nueva: es un medio de responder qué es el producto (gen/01) y su identificación. (Enmendada por [D-144](#d-144): la imagen sostiene la identificación como parte del mínimo de representación, pero no resuelve gen/01 ni gen/24.)
  - La capa general pasa a la versión 0.3.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.9; [demand-model](../10-model/demand-model.md#capa-general) 2.7; `demand-engine/catalog/gen.json`; OQ-45 anotada.
- **Relacionado:** D-024, D-034, D-038, D-039, D-040, D-045, D-047, D-049, OQ-45.

### D-053

**Catálogo de entrenamiento, primera selección: El Corte Inglés, amplitud de tipos y piloto.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-training-catalog-selection`, tareas T-020 y T-024. [OQ-48](open-questions.md) dejaba abierta la selección del catálogo de entrenamiento ([D-045](#d-045), [D-046](#d-046)). El usuario pidió «una lista representativa de productos para entrenamiento. utiliza un grupo pequeño de productos de cada categoría, pero quiero suficiente variedad de categorías», a partir del sitemap de variantes de El Corte Inglés, y fijó «3 fichas», 300 fichas en una misma jornada de captura y un piloto: «empecemos con 30 para validar el sistema de entrenamiento». Para la captura eligió un ritmo moderado y «no apliques la técnica del scroll. entra y descarga el html de primera carga».
- **Decisión:**
  - **Amplitud antes que profundidad:** pocas fichas de cada tipo de producto (3) y tantos tipos como sea posible.
  - **Primera tienda:** El Corte Inglés (generalista, con muchos departamentos). Sin Amazon.es.
  - **Tamaño:** 300 fichas (100 tipos); antes, un **piloto de 30** (10 tipos de departamentos distintos) valida el sistema de entrenamiento.
  - **Captura del catálogo de entrenamiento:** con el motor de captura, a ritmo moderado (pausa de 10–30 s; pausa larga de 1–3 min cada 20–30 fichas), con las 300 fichas en una misma jornada, por encima del tope por defecto del motor (150 visitas por sitio y día), y **sin desplazamiento**: se conserva el HTML de la primera carga.
- **Interpretaciones adoptadas** (criterio aplicado por Claude, pendiente de que el usuario lo revise):
  - Que el piloto valide «el sistema de entrenamiento» se lee como recorrer la cadena completa: captura, clasificación, ciclo de entrenamiento e informe.
  - «Categoría» se lee como **tipo de producto conocido antes de capturar**: la primera palabra del nombre del producto en la URL, en singular y sin palabras vacías, dentro de cada departamento; solo cuentan los tipos que nombra alguna categoría de la tienda. Es una aproximación: la clase de cada ficha es la que le da el clasificador. Las excepciones operativas (en los departamentos de títulos, como libros, cine y música, el tipo es el departamento; mínimo de productos por tipo; departamentos excluidos porque sus nombres empiezan por la marca) están en `demand-engine/training/selection/README.md`.
  - «Representativa» se lee como un sorteo determinista (semilla fija) por rondas de departamentos, sin repetir tipo, con una ficha por producto (las variantes cuentan una vez) y reservas para las fichas que ya no existan. Quedan fuera los departamentos que no venden productos (entradas, tarifa plana, tarjetas y cajas regalo).
  - «Evitar bloqueos» se lee como no provocarlos (ritmo, robots.txt, reservas TDM, parada ante desafíos), no como eludirlos ([D-042](#d-042), [D-046](#d-046)).
  - El artefacto limita la captura sin desplazamiento a «lo que necesitamos», es decir, al catálogo de entrenamiento: el MPIR y la captura suelta (`taxo page fetch`) siguen desplazándose para que cargue lo diferido.
- **Consecuencias:** [model-training](../10-model/model-training.md#casos-alcance-y-ejecución) 1.3; glosario (catálogo de entrenamiento); OQ-48 anotada: siguen abiertas otras tiendas y la relación con el panel de referentes del MPIR. Criterio operativo y selección en `demand-engine/training/selection/` (`eci-2026-10-25.json`: 100 tipos de 26 departamentos, 300 fichas y 200 reservas).
- **Relacionado:** D-042, D-045, D-046, OQ-11, OQ-12, OQ-48.

### D-054

**El entrenamiento a escala clasifica con agentes de Claude Code, no con la API.** · aceptada · 2026-10-25

- **Contexto:** `INTAKE 2026-10-25-training-classifier`, tareas T-020 y T-026. [D-045](#d-045) reservaba Claude Code para probar productos reales y preveía, para el entrenamiento con miles de fichas, «llamadas a la API por lotes». Con el piloto de 30 fichas ya capturado ([D-053](#d-053)), Claude propuso clasificarlo con la API de Anthropic y pidió una clave. El usuario respondió: «para clasificar usamos claude code».
- **Decisión:** la clasificación del catálogo de entrenamiento se hace con agentes de Claude Code, como `/demand-model`, y no con llamadas a la API. Enmienda el punto «Ejecución» de D-045.
- **Interpretación adoptada:** «Claude Code» se lee como agentes lanzados desde una sesión de Claude Code, con el mismo reglamento, la misma salida y la misma comprobación que la ejecución. El reparto de las fichas entre agentes es detalle del procedimiento (T-026).
- **Consecuencias:** [model-training](../10-model/model-training.md#casos-alcance-y-ejecución) 1.4; T-026 pasa de la API a un procedimiento de clasificación por lotes con agentes; no hace falta `ANTHROPIC_API_KEY`.
- **Relacionado:** D-045, D-053.

### D-055

**Crítico por requisito y clase; la medida descriptiva puede ser crítica.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-training-v4-review`, apartados 1 y 2, tras el ciclo de entrenamiento de reglas 4 (T-028, informe `demand-engine/training/reports/2026-10-26-v4-report.md`). Con la lectura de [D-045](#d-045), una regla global por rasgo decide si la identidad y el contenido son críticos; como casi todas las cuestiones de identidad no lo son, la regla da «no crítico» en todo el catálogo y ninguna clase puede tener una identidad crítica (el artista de un CD queda principal, como el género musical). Los votos ven críticas, entre otras, qué piezas incluye un juego, el formato de una grabación, el artista de un CD o LP, el tipo de joya para piercing y el tipo de sofá. La medida descriptiva, fija en principal ([D-043](#d-043), criterio 1), recibe votos «crítico» donde la medida en centímetros es la variante que se vende (manta 140×200, cojín 50×50). Hay requisitos compartidos por varias clases: la medida en centímetros del sector Ropa de cama es crítica en los votos de mantas y plaids, y principal en los de sábanas, fundas y protectores.
- **Decisión:**
  - Opción elegida: «Por requisito: misma prueba para todas las clases, aplicada a cada pregunta», por requisito y clase, como la relevancia.
  - Sobre la medida descriptiva, Claude propuso reetiquetar como «medida que fija lo vendido» la medida que define la variante. Palabras del usuario: «¿no estaría resuelto con la pregunta anterior?». Opción elegida: «Sí, extender: la medida descriptiva es principal salvo que los votos de su clase la hagan crítica. Las dimensiones de detalle (tacón, largo reclinado) siguen abiertas en OQ-51 hasta T-029.»
- **Interpretaciones adoptadas:**
  - Se mantiene la prueba de crítico de D-045 («sin la cuestión, ¿se sabe qué se vende, cuánto cuesta y si se puede adquirir?»), que es la misma en todas las clases. Se sustituye la regla global de identidad y contenido.
  - El mecanismo es el de la relevancia ([D-050](#d-050)): por requisito y clase, la mayoría de los votos del requisito en la clase, con la importancia del catálogo como voto de partida, igual que en la importancia. Sube a la madre con el mismo mínimo estructural y no pasa de las verticales. En un empate se queda lo que había, como en la relevancia y en el rasgo (D-056); así, un solo voto «crítico» frente a la importancia del catálogo no basta para hacer crítico un requisito.
  - Pueden ser críticos la identidad, el contenido, la medida descriptiva y los rasgos que dicen qué se vende ([D-056](#d-056)). La medida que fija lo vendido sigue siendo siempre crítica (D-043, criterio 1); la estética, nunca; la capa general sigue fija. (Sustituida por [D-058](#d-058): cualquier propiedad puede ser crítica.)
  - Si un requisito no es crítico, su importancia se decide como hasta ahora: el árbol por rasgo, y la medida descriptiva en principal por el marco. Un voto «crítico» en un rasgo que no lo admite cuenta como principal. (Enmendada por [D-058](#d-058): entre principal y complementario manda la excepción del requisito, si la tiene; el voto crítico cuenta como principal en la regla del rasgo y como crítico en la excepción.)
  - En un juego, como la importancia: se resuelve desde cada pieza y se toma la más alta.
  - La coherencia sigue comparando lo que decide el árbol: un crítico por requisito no cuenta como incoherencia frente a otros requisitos de su rasgo y clase, igual que una excepción de la opción C. Es un cambio de una métrica del marco que la decisión necesita. (Generalizada por [D-058](#d-058): ninguna excepción por requisito cuenta como incoherencia.)
  - Con esa exclusión, ninguna métrica de D-045 puede mejorar con una regla de crítico, y la validación nunca la aceptaría. Por analogía con la coherencia de relevancia de D-050, se añade la **coherencia del crítico**: requisitos cuya importancia contradice la mayoría de sus votos de crítico en su clase. Debe bajar. Es lectura de Claude, revisable en el marco. (Generalizada por [D-058](#d-058): coherencia por requisito.)
  - Las reglas de crítico se escriben `crit:<requisito>@<clase>` y, como las de relevancia, mandan sobre el voto; sin regla, decide el voto, provisional. (Enmendada por [D-058](#d-058): son excepciones por requisito, `imp:<requisito>@<clase>`.)
  - Descartado (apartado 6 del artefacto): contar las dos ejecuciones de un caso como un solo voto en la inducción. La simulación solo cambia dos reglas de los juguetes para perros; las de pantuflas y sofás cama salen de la granularidad por rasgo y de un solo caso por clase.
- **Consecuencias:** [model-training](../10-model/model-training.md#reglas-de-importancia) 1.5; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#criterios-de-redacción-del-catálogo) 1.10; glosario (regla inducida); D-043, criterio 1, y D-045 enmendadas; nueva métrica, coherencia del crítico; I-20 resuelta en lo que toca al crítico; OQ-51 anotada (en parte); el código del entrenamiento se adapta en una tarea aparte.
- **Relacionado:** D-035, D-043, D-045, D-050, D-051, D-056, I-20, OQ-51.

### D-056

**Vocabulario de rasgos abierto: rasgos propuestos y votados por los agentes.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-training-v4-review`, apartado 3. Los bloques generados en ejecución etiquetan algunos requisitos con rasgos que no encajan (el sabor de una confitura como material, la viscosidad SAE de un aceite como prestación, la especie de destino como uso, la duración de una grabación como medida descriptiva), y el índice de rasgos propaga la etiqueta por fuente a todas las categorías ([I-20](issues.md#i-20)).
- **Decisión:**
  - Palabras del usuario: «Se deberían proponer nuevos rasgos a medida que van siendo necesarios. Se aprueban solos si los agentes los van votando. Sabor en material no tiene sentido. Quizás un rasgo de sabor es más adecuado, pero esto lo dejamos a criterio de los agentes que los van encontrando.»
  - Mecanismo aceptado:
    1. **Proponer:** un agente que redacta un bloque o vota un requisito puede proponer un rasgo nuevo cuando ninguno encaja, con nombre y una frase de definición. Lo encuentra el agente.
    2. **Votar:** cada agente que vota un requisito vota también su rasgo: mantiene el actual o propone otro, de la lista o nuevo.
    3. **Aprobarse solo:** «mayoría de votos de rasgo en el requisito (empate: se queda el actual); entra en el vocabulario en cuanto gana en alguno. Luego, la validación de siempre de las reglas.»
  - Qué rasgos pueden ser críticos: «al proponer un rasgo, el agente indica si dice qué se vende; solo esos (y identidad, contenido, medidas) pueden ser críticos.» (Sustituido por [D-058](#d-058): cualquier propiedad puede ser crítica y el agente ya no indica si el rasgo dice qué se vende.)
- **Interpretaciones adoptadas:**
  - Sustituye «de una lista cerrada» de D-045 y el «vocabulario cerrado» de [D-051](#d-051): los 13 rasgos actuales son el vocabulario de partida.
  - Manda el rasgo votado del requisito. El índice por fuentes solo da el rasgo de partida a lo que no tiene votos, incluidos los requisitos de un bloque generado en ejecución. Una fuente toma el rasgo de sus requisitos cuando todos coinciden; si sus requisitos tienen rasgos distintos, sale del índice, como ya pasa con `amazon-ptd-prop:BOOT.toe_style` y `ley:CE-767/2009-11.3`.
  - «Mayoría» se lee como el rasgo más votado del requisito (mayoría relativa), porque puede haber más de dos candidatos.
  - El voto de rasgo lo emiten los mismos agentes que votan la importancia (D-045), para los requisitos que votan. Sin votos, se queda el rasgo actual.
  - «Medidas» son la medida que fija lo vendido y la medida descriptiva. La magnitud física no, porque D-051 la sacó de la regla de las medidas; un agente puede proponer otro rasgo si alguna magnitud dice qué se vende. (Sin efecto desde [D-058](#d-058).)
  - Un rasgo nuevo sin regla en una clase recibe la importancia del voto, provisional y encolada, como cualquier requisito sin regla (D-045).
  - El artefacto no dice qué pasa cuando dos agentes proponen nombres distintos para el mismo rasgo, ni si se retira un rasgo que deja de ganar, ni el estado de un rasgo propuesto por quien redacta un bloque mientras nadie lo ha votado (se usa como provisional): [OQ-52](open-questions.md).
- **Consecuencias:** [model-training](../10-model/model-training.md#rasgos) 1.5; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.10; glosario (rasgo); D-045 y D-051 enmendadas; I-20 resuelta; nueva OQ-52; el código del entrenamiento, el reglamento y `catalog/DRAFTING.md` se adaptan en una tarea aparte.
- **Relacionado:** D-045, D-051, D-055, I-20, OQ-49, OQ-52.

### D-057

**Composición y aplicación: hoja más específica, hermana como alias y unidad de exposición.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-training-v4-review`, apartado 4. En la pasada de control de reglas 4, los agentes dudan si una hoja registrada como vacía ([D-043](#d-043), criterio 7) entra como categoría o como alias, rechazan como duplicada una hermana que el caso de control espera como alias (Sofás de dos plazas en el sofá cama) y no activan la unidad no nueva en el Stressless, que [D-037](#d-037) lleva a la aplicación ([I-21](issues.md#i-21), [I-22](issues.md#i-22)).
- **Decisión** (opciones elegidas):
  - «La hoja más específica entra como categoría aunque herede todo; una hermana que nombra otra característica (dos plazas), como alias.»
  - «La unidad de exposición que la ficha identifica como tal cuenta como estado declarado; "outlet" solo, no.»
- **Interpretaciones adoptadas:**
  - La hoja más específica que cumple el producto es el componente por el que entran los requisitos de sus madres ([D-029](#d-029)): los aporta al producto, aunque su bloque esté vacío, y por eso no es alias. Una hermana del mismo nivel trae por herencia esos mismos requisitos, ya aportados, y no añade ninguno sin duplicarlo ([D-023](#d-023)): nombra otra característica y es alias. Responde en parte a [OQ-39](open-questions.md); cómo se elige la hoja más específica entre dos hermanas que el producto cumple queda en [OQ-43](open-questions.md).
  - Una hermana que nombra otra característica del producto no es una entrada duplicada: la duplicada sigue siendo otra entrada para el mismo tipo de producto (el plaid, [OQ-43](open-questions.md)).
  - La unidad de exposición se lee con D-037: es un estado de la unidad declarado en la ficha, que activa `gen.unidad-no-nueva`; la etiqueta «outlet» sola no basta como estado declarado.
- **Consecuencias:** [study-class](../10-model/study-class.md#composición-de-la-clase) 1.4; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.10; glosario (alias, clasificación objetiva); D-033 y D-037 precisadas; I-21 e I-22 resueltas; OQ-39 y OQ-43 anotadas; el reglamento del clasificador (`demand-engine/classifier/rulebook.md`, pasos 2 y 6) se adapta en una tarea aparte.
- **Relacionado:** D-023, D-028, D-033, D-037, I-21, I-22, OQ-39, OQ-43.

### D-058

**Excepciones de importancia por requisito y clase en cualquier propiedad, también para el crítico.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-color-and-requirement-exceptions`, tras la revisión del ciclo de reglas 4 (T-028). Palabras del usuario: «Duda sobre el color en el rasgo de estética. No sé si con estos cambios ya quedaría resuelto. En los casos de control veo que el color se está estableciendo como complementario, pero esto no tiene sentido. En muchos casos el color es principal o incluso crítico, por ejemplo en zapatillas o sofás. No puedes compararlo si no sabes el color.» Los votos dan el color principal en calzado (10 de 10), sofás y sofás cama (4 de 4) y cojines (2 de 2), y la regla de la estética lo deja complementario en todas esas clases: el color comparte rasgo con el estampado, el estilo, el acabado o las patas, que los agentes votan complementarios. Pasa lo mismo con el abrigo de las pantuflas y el mecanismo de apertura del sofá cama; en el piloto, 97 de 375 combinaciones de requisito y clase tienen una mayoría clara de votos contra el nivel que aplica la regla. Ningún agente ha votado el color crítico; cuando el color es lo que se elige entre variantes, la capa general ya lo pregunta como crítico (`gen.variantes/01`). [D-055](#d-055) solo decidía el crítico, y el marco prohibía hacer crítica la estética.
- **Decisión:**
  - Opción elegida (A): «Excepción por requisito: la regla por rasgo es la general; si los votos de un requisito en una clase la contradicen, ese requisito tiene su propia regla (mayoría; empate, se queda lo que había). D-055 pasa a ser un caso de esto.»
  - Sobre el color, opción elegida: «Sí, si sus votos lo dicen: el color se excepciona de la prohibición de la estética: puede ser crítico por requisito y clase si los votos lo hacen crítico.» Precisión del usuario: «Esto no solo es para el color, es para cualquier propiedad.» Y después, sobre su alcance (`INTAKE 2026-10-26-any-property-precision`): «Me refería a las 2 respuestas. No solo a que pueda ser crítico, también como principal.»
- **Interpretaciones adoptadas:**
  - «Cualquier propiedad» vale para las dos respuestas: la excepción por requisito y el crítico. Se lee como cualquier requisito de un bloque de categoría o de especialización, o inferido: puede tener su propia importancia en una clase (principal, complementario o crítico) si sus votos contradicen la regla de su rasgo. Desaparecen el límite del marco «ninguna regla puede hacer crítica la estética» (INTAKE 2026-10-25-training-operation, [D-045](#d-045)), la lista de rasgos que podían ser críticos (D-055) y la indicación de si un rasgo propuesto dice qué se vende ([D-056](#d-056)), que solo servía para eso. La capa general sigue fija y la medida que fija lo vendido, siempre crítica.
  - El mecanismo es el de D-055 en todos los niveles. La regla `imp:<requisito>@<clase>` es la mayoría de los votos del requisito en la clase, con la importancia del catálogo como voto de partida. En un empate se queda lo que da la regla del rasgo. Sube a la madre con el mismo mínimo estructural, no pasa de las verticales y manda sobre la regla del rasgo; sin votos, decide la regla del rasgo. Las reglas de crítico de D-055 son excepciones de este tipo.
  - La regla por rasgo sigue decidiendo entre principal y complementario y no da crítico: ya no lo daba con D-045 (salvo la regla global de identidad y contenido), y D-055 llevó el crítico al requisito. Un voto «crítico» cuenta como principal en la regla del rasgo y como crítico en la excepción del requisito.
  - Las excepciones no bajan lo que fija el marco: la medida descriptiva no baja de principal ([D-043](#d-043), criterio 1; las dimensiones de detalle siguen en [OQ-51](open-questions.md)). Tampoco la composición textil, que es principal por su origen normativo según las interpretaciones de D-043 (Reglamento (UE) 1007/2011, art. 16.1); es lectura de Claude, porque D-043 forma parte del marco ([D-044](#d-044)).
  - Una excepción no cuenta como incoherencia. La métrica de aceptación de D-055 pasa a ser la **coherencia por requisito**: requisitos cuya importancia contradice la mayoría de sus votos en su clase. Debe bajar.
- **Consecuencias:** [model-training](../10-model/model-training.md#reglas-de-importancia) 1.6 y 1.7 (precisión `INTAKE 2026-10-26-any-property-precision`); glosario (regla inducida, rasgo); D-045, D-055 y D-056 enmendadas; I-20 anotada; nueva I-24; el código del entrenamiento se adapta en T-030.
- **Relacionado:** D-035, D-043, D-045, D-050, D-055, D-056, OQ-51.

### D-059

**«Críticos pocos» no es un objetivo del marco.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-critical-count-not-a-goal`. El marco del entrenamiento ([D-044](#d-044), diagrama de `INTAKE 2026-10-25-induced-rules`, redactado por Claude y aprobado por el usuario con «documenta») incluía «críticos pocos» entre los objetivos y características del resultado. Tras [D-058](#d-058), Claude registró [I-24](issues.md#i-24): ninguna métrica vigila que haya pocos críticos.
- **Decisión:** palabras del usuario: «Eso era una suposición, no una regla. Podría haber muchos críticos si así se determina.» «Críticos pocos» sale de los objetivos y características del resultado del marco.
- **Interpretaciones adoptadas:**
  - Cuántos requisitos son críticos lo determinan la prueba de crítico ([D-045](#d-045), [D-055](#d-055)) y las reglas que salen de los votos ([D-058](#d-058)); el marco no pone límite a su número.
  - Siguen en el marco los demás objetivos y características del resultado: identidad por bloques, especificidad necesaria y nada de conjeturas.
- **Consecuencias:** [model-training](../10-model/model-training.md#marco) 1.8; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#pruebas-de-importancia) 1.12 (se retira «los críticos son pocos y casi todos generales»); D-044 precisada; I-24 resuelta (no aplica); en T-030 se retiran las frases equivalentes del reglamento del clasificador («Los críticos son pocos») y de `catalog/DRAFTING.md` («Los críticos son raros fuera de la capa general»), que sesgan los votos.
- **Relacionado:** D-044, D-045, D-055, D-058, I-24.

### D-060

**Formulación de las cuestiones del catálogo: condiciones, una necesidad por requisito y componentes con fuente.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-question-formulation`, antes del escalado del entrenamiento (T-029). Palabras del usuario: «Veo que los requisitos se están construyendo con unas preguntas muy extensas, abarcando demasiado análisis en cada uno. También veo que muchas de estas preguntas contienen subpreguntas condicionales»; pidió estudiar si convenía ya una regla o esperar a trabajar más a fondo la valoración de los AC. En el catálogo (409 requisitos), unas 104 cuestiones hacen dos o más preguntas y 19 llevan una condición dentro. Con una parte basta para que la disponibilidad efectiva sea 1, y la ausencia de las demás baja a Concreción 1; cada GSC juzga varios hechos con un solo valor; las partes secundarias heredan el rasgo y la importancia de la cabeza (2 de los 5 rasgos mal etiquetados de [I-20](issues.md#i-20) son cuestiones compuestas). Dividir después del escalado invalidaría los votos, los rasgos y las reglas por requisito ligados a su identificador. Una muestra con el modelo `sofa-cama-luna` (v4-b) confirmó el enfoque; tras ella, la regla de dividir se estrechó.
- **Decisión** (opción C, regla estrecha ahora y granularidad después; «Aplícalo así»):
  - Cuatro reglas para formular las cuestiones del catálogo: (1) ninguna condición sobre la existencia de la información («si se indica», «si procede»); (2) una condición sobre un hecho que afecta solo a una parte se convierte en un requisito condicionado propio, con la condición en `applicability`, y la pregunta de sí o no seguida de su detalle se mantiene, porque un «no» fundamentado lo resuelve todo; (3) una necesidad por RI: se divide cuando las partes se responden por separado, cada una sirve por sí sola para comparar y tomarían otro rasgo u otra importancia; tras la muestra, estrecha: «solo divide cuando las partes tomarían otro rasgo u otra importancia»; (4) cada componente de la cuestión tiene fuente y, si no la tiene, va como cuestión inferida. Texto literal en [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formulación-de-las-cuestiones).
  - Aplazado al trabajo de los AC: la granularidad cuando las partes comparten rasgo e importancia (par `cat.sofas/13` frente a `cat.sofas/05`) y qué hacer con las listas de ejemplos. La capa general, que es marco, no se toca: `gen/01`, `gen/12` y `gen/15` quedan como candidatas para decisión del usuario.
- **Interpretaciones adoptadas:**
  - Son criterios de método que se añaden a los de [D-043](#d-043) (`requirement-blocks`, propuesta) y, como ellos, forman parte del marco ([D-044](#d-044)). No crean conceptos: usan el requisito condicionado ([D-048](#d-048)), la cuestión inferida ([D-036](#d-036), [D-041](#d-041)), el rasgo ([D-056](#d-056)) y la importancia, y aplican la neutralidad de la formulación de un RI ([demand-model](../10-model/demand-model.md#reglas-e-invariantes)). «Necesidad», en la regla 3, es la necesidad de conocimiento del RI; las «necesidades constitutivas» de la RI-03 del perfil del RI son sus componentes.
  - Las reglas 1 a 3 se aplican a las cuestiones de los bloques de categoría y de especialización y a las inferidas, es decir, a todo lo que redactan la redacción de bloques y el clasificador. La regla 4, a las cuestiones con fuente de referencia (origen «referencias» o «normativa»): las de especialización y las inferidas no la tienen ([D-045](#d-045)). La capa general no cambia sin decisión del usuario.
  - Regla 1: la condición prohibida es la que no nombra un hecho del producto o de la oferta. Si corresponde a un hecho identificable, se nombra ese hecho y rige la regla 2.
  - Regla 2: el detalle del mismo hecho es lo que solo existe si la respuesta es sí. Si ese detalle reúne varias necesidades, rige la regla 3.
  - Regla 3: las tres condiciones se cumplen a la vez. El rasgo y la importancia son los que tomaría cada parte por sí sola con el vocabulario y las reglas vigentes. Cuando las partes comparten rasgo e importancia, la cuestión no se divide por esta regla; sigue rigiendo el criterio 2 de D-043 (un atributo con valores de temas distintos se divide por tema).
  - Regla 4: la fuente es un atributo, una propiedad o un valor de las `sources` del requisito, o la norma en el origen «normativa». El componente sin fuente sale de la cuestión y se propone como cuestión inferida, con sus controles; la valida el entrenamiento ([D-044](#d-044)).
  - Las listas de ejemplos siguen la RI-07 del perfil del RI: son ayudas de interpretación, no componentes.
  - El catálogo vigente se corrige con estas reglas antes del escalado. La implantación queda fuera de la documentación: `demand-engine/catalog/DRAFTING.md` y el reglamento del clasificador, en T-030; la nueva redacción del catálogo, en T-031.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formulación-de-las-cuestiones) 1.11 y 1.13 (revisión independiente); [demand-model](../10-model/demand-model.md#reglas-e-invariantes) 2.8 (enlace a las reglas); D-043 ampliada; OQ-22 y OQ-45 anotadas; el catálogo de `demand-engine/catalog/cat/` se corrige con estas reglas (tareas del código).
- **Relacionado:** D-036, D-041, D-043, D-044, D-048, D-056, I-20, OQ-22, OQ-45.

### D-061

**Tipos de información potencialmente resolutiva: forma de la respuesta, con vocabulario cerrado.** · sustituida por [D-062](#d-062) · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-answer-form`. El usuario pidió revisar en el canon la estructura de propiedades del requisito («¿Qué está faltando?»). El canon ([demand-model](../10-model/demand-model.md#requisito-informativo-ri), FUND §3.3) nombra como registro opcional del catálogo los «tipos de información potencialmente resolutiva», sin definirlos; ni el método ni el catálogo los registraban. Claude presentó tres lecturas: forma de la respuesta, soporte donde suele aparecer, o las dos.
- **Decisión:** palabras del usuario: «Empezaremos por añadir este campo: "Tipos de información que pueden resolverlo".» Opción elegida, «Forma de la respuesta (Recomendado)»: «Qué clase de dato o afirmación responde la cuestión, con vocabulario cerrado. Se deduce en parte de las fuentes; sirve a Precisión, Comparabilidad y a los ámbitos pertinentes.» Vocabulario cerrado (borrador): valor con unidad, valor de lista, sí/no, relación, condición, identidad, acreditación y descripción, con los ejemplos del artefacto. Descartadas: «Soporte donde aparece» y «Ambas, en dos listas».
- **Interpretaciones adoptadas:**
  - El campo conserva el nombre del canon, «tipos de información potencialmente resolutiva», con la etiqueta «forma de la respuesta». Su definición va al canon (`demand-model`); el vocabulario, por ser borrador, como propuesta en el mismo módulo.
  - «Añadir este campo» se lee como pasar de registro opcional a campo del catálogo: cada requisito lleva uno o varios valores del vocabulario (los ejemplos del artefacto combinan dos, «sí/no · valor con unidad»). Se registra en todos los requisitos, también en la capa general, como en los ejemplos del artefacto (`gen/06`, relación; `gen/11`, condición); en ella, que es marco, se fija con la capa general, sin cambiar sus preguntas ni sus importancias.
  - «Potencialmente» y el principio de independencia de un campo o formato ([demand-model](../10-model/demand-model.md#reglas-e-invariantes)): el campo no prescribe un formato de publicación ni excluye una respuesta de otra forma que esté fundamentada, y no es una lista de respuestas esperadas (objetivo y límite del perfil del RI; RI-06). Su finalidad es la que da la opción elegida: servir a la Precisión, la Comparabilidad y los ámbitos pertinentes. La localización, función de la opción descartada «Soporte donde aparece», no se le atribuye.
  - «Se deduce en parte de las fuentes»: lo registra quien redacta el requisito (la redacción del bloque o el clasificador), apoyándose en el tipo de sus fuentes. No lo inducen ni lo votan las reglas del entrenamiento.
  - Los usos que cita la opción (Precisión, Comparabilidad, ámbitos pertinentes) son su finalidad; no cambian las guías de los AC ni deciden por sí solos los ámbitos pertinentes, que siguen sin registrarse.
  - No es el rasgo ([D-056](#d-056)): el rasgo dice qué resuelve la cuestión; la forma, cómo es la respuesta. «Identidad» está en los dos vocabularios con sentidos distintos: como rasgo, la cuestión que dice qué se vende; como forma, una respuesta que es un nombre, una dirección o un identificador.
  - El vocabulario es cerrado: un valor nuevo o un cambio requieren decisión. Cómo se ajusta con el uso queda abierto ([OQ-53](open-questions.md)).
- **Consecuencias:** [demand-model](../10-model/demand-model.md#requisito-informativo-ri) 2.9 y 2.10 (revisión independiente); [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.14 y 1.15 (campos de un requisito); glosario (nueva entrada); nueva OQ-53. La implantación (formato del catálogo y de la salida del clasificador, comprobación con el vocabulario, registro en los requisitos existentes) queda fuera de la documentación: T-030 y T-031.
- **Relacionado:** D-034, D-044, D-045, D-056, D-060, OQ-03.

### D-062

**Información resolutiva: los tipos de información que pueden resolver cada requisito, para localizar y recomendar.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-resolving-information`. Tras [D-061](#d-061), el usuario pidió un sistema de reglas del motor que determinara el campo y una muestra simulada con el modelo `sofa-cama-luna`. Ante el resultado: «No me convence el resultado. Revisa en el canon para qué sirve "Tipos de información que pueden resolverlo": 1. localizar información pertinente; 2. recomendación.» El canon nombra el campo sin definirlo (FUND §3.3), pero lo sitúa en esas dos funciones: localizar la información que puede responder un RI (núcleo de conocimiento y perfil de resolución, FUND §3.6) y recomendar con acciones verificables (FUND §9.5). La forma de la respuesta de D-061 describe cómo es el dato, no qué información resuelve la cuestión, y D-061 llegó a excluir la localización.
- **Decisión** (respuesta del usuario: «Sí»):
  - Definición propuesta por Claude: para cada requisito, los tipos de información comercial (datos, afirmaciones, relaciones o contenidos) que pueden contribuir a resolverlo, cada uno ligado al componente de la cuestión al que aporta; orientativa y no exhaustiva (RI-07), admite otras representaciones (RI-06), no impone formato ni ubicación (PR-06) y no son valores esperados. Se retira el vocabulario de formas.
  - Alcance, en palabras del usuario: «Solo me interesa la columna "Tipos de información que pueden resolverlo" (por ahora).»
  - Denominación, elegida entre «Información resolutiva», «Guía de resolución», «Contribuciones posibles» y «Repertorio de información»: «Información resolutiva (Recomendado)», forma corta del término del canon; la definición conserva el «potencialmente».
  - Las reglas del motor que la determinan se diseñan después, con el contenido ya fijado.
- **Interpretaciones adoptadas:**
  - Sustituye a D-061 en todo: definición, finalidad, contenido y vocabulario. El catálogo la sigue registrando en cada requisito («para cada requisito»), como D-061 había decidido para el campo.
  - «Solo la columna» delimita el campo a la lista de tipos de información de cada requisito; las demás columnas de la muestra quedan fuera del campo.
  - Las dos funciones son finalidad del campo; no cambian las reglas de la exploración, la pertinencia, la cobertura ni las recomendaciones de la auditoría (`audit-gsc`), que lo usan como apoyo.
  - No es el rasgo ([D-056](#d-056)): el rasgo dice qué resuelve la cuestión; la información resolutiva, qué información puede resolverla.
  - Quién la registra y con qué reglas queda abierto ([OQ-54](open-questions.md)); mientras tanto no se registra en el catálogo. [OQ-53](open-questions.md), sobre el vocabulario de formas, deja de aplicar. (Resuelto por [D-063](#d-063), que añade a cada tipo su origen, su respaldo y las tiendas en que se observa.)
- **Consecuencias:** [demand-model](../10-model/demand-model.md#requisito-informativo-ri) 2.11 y 2.12 (revisión independiente); [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.16 y 1.17; glosario (la entrada pasa a «Información resolutiva»); OQ-53 cerrada; nueva OQ-54. Los criterios de D-061 en T-030 y T-031 se retiran hasta que se diseñen las reglas.
- **Relacionado:** D-044, D-056, D-060, D-061, OQ-03.

### D-063

**Información resolutiva: cuatro orígenes compilados por el entrenamiento y aceptación en dos tiendas distintas.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-resolving-information-rules`. [D-062](#d-062) dejó abiertas las reglas del motor que determinan la información resolutiva ([OQ-54](open-questions.md)). Ante la tanda de control con los 14 casos de referencia, el usuario eligió diseñarlas antes de T-030, para que esa tanda las mida también. Claude presentó la propuesta con una muestra de datos reales de las ejecuciones v4 y del control: las 31 fichas con hechos de `gen/11` vienen de solo 4 tiendas.
- **Decisión** («OK»): una lista por requisito con cuatro orígenes, que compila el entrenamiento. Cada tipo lleva su componente, su origen y respaldo y las tiendas en que se ha observado, que son evidencia, no un peso ni una importancia.
  - **Marco** (capa general): de la ley que ya es fuente del requisito; la decide el usuario y se fija como el resto de la capa general.
  - **Referencias:** el código extrae los títulos y las descripciones de las propiedades de Amazon (y de sus subpropiedades) y los atributos de Shopify con sus valores; quien redacta los convierte en tipos ligados a componentes.
  - **Fichas reales:** el clasificador indica qué tipo de la lista es cada hecho declarado o propone uno nuevo ligado a un componente; el entrenamiento lo acepta cuando aparece en dos tiendas distintas y aporta a un componente de la pregunta.
  - **Inferida:** la propone quien redacta; queda provisional y marcada.
  - Ningún tipo se retira por no observarse. Mínimo de aceptación: «dos tiendas distintas», no «dos fichas».
- **Interpretaciones adoptadas:**
  - Es un concepto del canon con definición, finalidad y reglas propias, y `demand-model` y `model-training` están en el límite de longitud: va a un módulo nuevo, [resolving-information](../10-model/resolving-information.md), que recibe la definición de D-062; `demand-model` la enlaza.
  - «Tú», en la tabla del artefacto, es el usuario. Las listas de la capa general las redacta Claude a partir de la ley y las aprueba el usuario, como dice el artefacto.
  - Capa general frente a D-045 («ninguna regla puede tocar la capa general»): la muestra acepta en `gen/11` un tipo observado en las fichas. Se lee así: los tipos de origen «marco» los fija el usuario; el entrenamiento solo añade tipos observados, sin tocar las preguntas ni las importancias de la capa general, que es lo que D-045 protege. Es lectura de Claude.
  - Amplía el alcance de la primera versión del entrenamiento ([D-045](#d-045): «inducción solo para la importancia»), como ya hizo [D-050](#d-050) con la relevancia: la regla de las dos tiendas es una regla inducida de la información resolutiva.
  - Cada tipo registra las tiendas en que se ha observado, sea cual sea su origen; la regla de las dos tiendas solo decide la entrada de los tipos nuevos propuestos desde las fichas.
  - Cómo deja de ser provisional un tipo inferido no lo dice el artefacto: [OQ-55](open-questions.md).
  - «Aporta a un componente de la pregunta» es la condición que excluye lo próximo al tema (invariante 10); en la muestra, el plazo de cambio se rechaza en `gen/11`.
  - Las tiendas en que se observa un tipo se guardan como evidencia para localizar y recomendar; no entran en el GSC, en el IR ni en la importancia.
  - La relación con los componentes y las expresiones de ejemplo del perfil del RI, que OQ-54 también recogía, no la resuelve el artefacto: pasa a [OQ-03](open-questions.md).
- **Consecuencias:** nuevo módulo [resolving-information](../10-model/resolving-information.md) 1.0; [demand-model](../10-model/demand-model.md#requisito-informativo-ri) 2.13 y 2.14; [model-training](../10-model/model-training.md#conexiones-y-principios) 1.9 y 1.10 (capa general y quién decide); [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.18 y 1.19; D-045 ampliada (como D-050); nueva OQ-55; glosario; índice de `docs/README.md`; OQ-54 cerrada; OQ-03 anotada. La implantación va en T-030 (formato, salida del clasificador y `bin/train`: extracción de referencias, aceptación e informe) y T-031 (listas de los requisitos de categoría).
- **Relacionado:** D-044, D-045, D-056, D-060, D-062, OQ-03, OQ-54.

### D-064

**«Aportación resolutiva»: nombre de cada entrada de la información resolutiva.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-resolving-contribution-name`. [D-062](#d-062) y [D-063](#d-063) llaman «tipo» a cada entrada de la lista de información resolutiva de un requisito. Ante una interpretación de D-063 sobre la capa general, el usuario preguntó: «¿A qué te refieres con "tipos"?». Claude lo explicó: es una clase de información que puede contribuir a responder la pregunta («plazo para desistir o devolver» en `gen/11`), no el valor que publica una tienda, ni el rasgo, ni las formas retiradas de D-061.
- **Decisión:** «Vamos a cambiar el nombre. A algo más claro y alineado con información resolutiva.» Entre «Aportación resolutiva», «Tipo de información resolutiva», «Ítem de información resolutiva» y «Dato resolutivo», opción elegida: «Aportación resolutiva (Recomendado)», que «enlaza con la propia definición ("pueden contribuir… cada uno ligado al componente al que aporta") y con la pertinencia del canon ("contribución identificable")».
- **Interpretaciones adoptadas:**
  - Cambia el nombre, no el concepto: las reglas de D-063 se aplican igual a las aportaciones.
  - La lista sigue llamándose «información resolutiva», y la definición literal de D-062 conserva «tipos de información», el término general del canon (FUND §3.3). Las citas literales de las fuentes de D-062 y D-063 conservan «tipo», con una nota que remite a esta decisión.
  - De la explicación del artefacto sale una distinción nueva en el módulo: aportación frente a valor publicado («plazo» frente a «30 días»).
  - D-062 y D-063 no se reescriben, porque el registro de decisiones es de solo adición; su fila en la tabla remite a esta.
  - El artefacto dice que el nombre «no choca con nada», pero el MPIR usa «aportación» en otro sentido («tipos de aportación» al modelo de demanda). No se resuelve en silencio: [I-25](issues.md#i-25).
- **Consecuencias:** [resolving-information](../10-model/resolving-information.md) 1.1; [demand-model](../10-model/demand-model.md#requisito-informativo-ri) 2.15; [model-training](../10-model/model-training.md) 1.11; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.20; glosario (nueva entrada «Aportación resolutiva» y entrada de información resolutiva); OQ-55 anotada en su texto. T-030, T-031 y T-032 adoptan el nombre.
- **Relacionado:** D-062, D-063, OQ-55.

### D-065

**Formulación de la capa general: reglas de D-060, también para las partes de igual importancia, y aportaciones sin ley como inferidas.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-general-layer-formulation` e `INTAKE 2026-10-26-general-layer-formulation-2`. En T-031, Claude presentó desde la ley el borrador de la información resolutiva de la capa general ([D-063](#d-063): la redacta Claude y la aprueba el usuario). El usuario no aprobó las aportaciones de origen marco: «sigo viendo varios con requsisitos compuestos». La capa general, que es marco, había quedado fuera de las reglas de [D-060](#d-060) sin decisión del usuario, con `gen/01`, `gen/12` y `gen/15` como candidatas ([OQ-45](open-questions.md)). Hubo dos rondas:
  - **Primera ronda.** Claude propuso aplicar las cuatro reglas con la regla 3 estrecha. El usuario eligió «Reglas de D-060 tal cual (Recomendado)», frente a «Dividir también lo de igual importancia» y «No tocar la capa general».
  - **Segunda ronda.** Al presentarle de nuevo las aportaciones, el usuario respondió: «aun veo algunos compuestos que deberians epararse. pe: el del precio. peor hay otros». Claude propuso separar también las partes de igual importancia, y el usuario eligió «Sí, como en la tabla (Recomendado)», frente a «También gen/17, gen/18 y gen/19».
- **Decisión:** la capa general se formula con las cuatro reglas de D-060, pero la regla 3 no se limita a las partes de otro rasgo u otra importancia: se separan las partes que se responden por separado. Divisiones:
  - `gen/01` → qué es el producto, y qué incluye exactamente la oferta (los dos críticos);
  - `gen/02` → marca, y modelo;
  - `gen/04` → precio con impuestos incluidos, y coste del envío a España (los dos críticos, 97.1.e);
  - `gen/06` → si está disponible, y en `gen.variantes`, qué variantes están disponibles;
  - `gen/11` → si se puede desistir o devolver, en qué plazo y condiciones (97.1.j); qué coste de devolución asume el comprador (k); cuándo no procede o se pierde el derecho (m);
  - `gen/12` → garantía legal de conformidad (97.1.n), y dos requisitos condicionados (97.1.ñ, «cuando proceda»): si tiene garantía comercial, cuál y en qué condiciones; si tiene asistencia o servicios posventa, cuáles y en qué condiciones;
  - `gen/15` → opiniones de compradores, y un requisito condicionado «si publica opiniones»: cómo garantiza que son de compradores reales;
  - `gen.variantes` → qué variantes hay; en qué se diferencian; qué variantes están disponibles;
  - `gen.unidad-no-nueva` → marcas o defectos (principal); qué unidad se entrega (principal); motivo (complementario);
  - `gen.descuento` → desde qué precio de referencia; en qué condiciones se aplica;
  - `gen.precio-personalizado` → si el precio está personalizado por una decisión automatizada (97.1.f), y una cuestión inferida, con qué parámetros (regla 4: no están en la ley);
  - `gen.elementos-digitales` → funcionalidad y medidas técnicas de protección (97.1.s); compatibilidad e interoperabilidad (97.1.t): cuatro requisitos;
  - `gen.suscripcion` → duración o, si es indefinido o se prorroga solo, condiciones de resolución (97.1.p); duración mínima (q); depósitos y sus condiciones (r).
  - Quedan juntos `gen/17` y `gen/18` (nombre y dirección: ejemplo literal de D-060 de lo que solo tiene sentido unido), `gen/16` (pregunta de sí o no con su detalle, regla 2) y `gen/19` (advertencias o información de seguridad: una sola exigencia del GPSR, art. 19.d). `gen/09` solo pasa a forma de pregunta.
  - Aportaciones de la capa general sin apoyo en la ley: opción elegida «Inferidas provisionales (Recomendado)», frente a «Como marco» y «Retirarlas»: «Se registran con origen "inferida", como en los bloques de categoría, hasta que se decida cómo dejan de ser provisionales (OQ-55)».
- **Interpretaciones adoptadas:**
  - La regla 3 más amplia solo vale para la capa general: en los bloques de categoría y de especialización sigue la estrecha de D-060, y la granularidad de las partes que comparten rasgo e importancia sigue aplazada al trabajo de los AC ([OQ-22](open-questions.md)).
  - Importancias: las de las tablas; donde no se dijo, cada parte conserva la del requisito original. La suscripción sigue por fijar ([OQ-45](open-questions.md)). Siguen siendo fijas como parte del marco ([D-045](#d-045)).
  - Los requisitos condicionados nuevos (garantía comercial; asistencia o servicios posventa; autenticidad de las opiniones publicadas) dependen de hechos de la oferta. Los artefactos no dicen en qué bloque van: van en el bloque universal con su condición en la aplicabilidad, como la persona responsable en la UE ([D-052](#d-052)), que era un hecho del producto; los evalúa la auditoría y no son disparadores nuevos de la aplicación ([D-047](#d-047)), cuya lista no cambia. Es una lectura de Claude que amplía D-052 a hechos de la oferta y choca con la definición de la aplicación del canon: [I-26](issues.md#i-26), con la alternativa de bloques condicionados propios.
  - Origen de las cuestiones: sigue su fuente, como en toda la capa general; la de los parámetros del precio personalizado es inferida. En la capa general, el origen «inferida» de una cuestión no la hace provisional: es marco fijado por el usuario, como `gen/06`, `gen/07` o `gen/15`.
  - Redacciones de Claude que los artefactos no fijan: «qué incluye exactamente la oferta» con entidad oferta; «¿Qué unidad se entrega?»; el motivo conserva su lista de ejemplos (exposición, devolución, tara, fin de serie…); la compatibilidad y la interoperabilidad se refieren a aparatos y programas, como el art. 97.1.t.
  - `gen.precio-personalizado/01` repite el hecho de su disparador: con el bloque activo, la respuesta es siempre sí. No se resuelve en silencio: [I-27](issues.md#i-27).
  - Las aportaciones de origen marco se presentan al usuario tras la división: siguen pendientes de su aprobación. Las que se redactan sin apoyo en la ley se registran como inferidas y provisionales, como en los bloques de categoría ([OQ-55](open-questions.md)).
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.21 (tabla de la capa general y alcance de las reglas de formulación); [resolving-information](../10-model/resolving-information.md) 1.3 (orígenes en la capa general); [model-training](../10-model/model-training.md) 1.12; D-034, D-052, D-060 y D-063 anotadas en la tabla; OQ-45 anotada (candidatas resueltas); nuevas I-26 e I-27. La implantación en `demand-engine/catalog/gen.json` va en T-031: la capa general pasa a la versión 0.4.
- **Relacionado:** D-034, D-038, D-045, D-047, D-052, D-060, D-063, OQ-22, OQ-45, OQ-55.

### D-066

**Garantía comercial, asistencia posventa y opiniones publicadas: bloques condicionados de la capa general.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-general-layer-issues`. [D-065](#d-065) dejó en el bloque universal tres requisitos condicionados a hechos de la oferta (la garantía comercial, la asistencia o los servicios posventa, la autenticidad de las opiniones publicadas), fuera de la aplicación, que el canon define como las condiciones de la oferta que se dan ([D-047](#d-047)). Incidencia [I-26](issues.md#i-26). Claude presentó dos opciones y recomendó la de bloques propios, frente a la propuesta escrita en la incidencia.
- **Decisión:** «Bloques condicionados propios (Recomendado)»: «gen.garantia-comercial, gen.posventa y gen.opiniones, con su disparador; entran en la aplicación como el descuento. El canon no cambia.» Descartada: «Seguir en el bloque universal».
- **Interpretaciones adoptadas:**
  - Disparadores: `gen.garantia-comercial`, si tiene garantía comercial; `gen.posventa`, si tiene asistencia o servicios posventa; `gen.opiniones`, si publica opiniones de compradores. Alcance: la oferta. Como en los demás bloques condicionados, los activa el hecho declarado ([D-037](#d-037)) y, si la ficha no lo declara, sus requisitos quedan en gris (NA).
  - Cada bloque lleva el requisito que estaba en el bloque universal, con la pregunta sin la condición, que pasa al disparador; conserva su importancia, su origen y su información resolutiva. Los ids nuevos son `gen.garantia-comercial/01`, `gen.posventa/01` y `gen.opiniones/01`; sustituyen a `gen/22`, `gen/28` y `gen/23`, que no se reutilizan ([D-038](#d-038)).
  - Relación con las preguntas universales: la garantía legal de conformidad no activa `gen.garantia-comercial`, porque la responde `gen/12`. Las opiniones las pregunta `gen/15` en toda oferta; si la ficha publica opiniones, `gen.opiniones` añade su autenticidad. Es como el descuento: la pregunta universal de promociones ([D-049](#d-049)) convive con el bloque `gen.descuento`. Así se matiza [D-047](#d-047), según la cual, salvo el descuento, las condiciones no tienen pregunta universal. Si las opiniones sobre la tienda, y no sobre el producto, activan el bloque: [I-29](issues.md#i-29).
  - «El canon no cambia» se lee como que no cambia la definición de la aplicación; su lista de condiciones (canon y glosario) se amplía con las tres nuevas, como pide el principio de una sola fuente de verdad.
  - El bloque universal vuelve a llevar un solo requisito condicionado, el de la persona responsable en la UE ([D-052](#d-052)), y queda sin efecto la ampliación de D-052 a hechos de la oferta que hizo D-065.
  - Consecuencia: una oferta que declara garantía comercial, asistencia posventa u opiniones deja de ser una oferta estándar, porque estas condiciones entran en su aplicación. El reglamento del clasificador las lista entre las condiciones que activa.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.17 (lista de la aplicación); glosario (aplicación); [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.22 (tabla y disparadores); D-034, D-047, D-052 y D-065 anotadas en la tabla; I-26 resuelta; nueva I-29 (opiniones de la tienda). La implantación en `demand-engine/catalog/gen.json` (capa general 0.5) y en el reglamento del clasificador va en T-033.
- **Relacionado:** D-037, D-047, D-052, D-065, I-26.

### D-067

**Se retira la pregunta del precio personalizado que repite su disparador.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-general-layer-issues`. Tras [D-065](#d-065), `gen.precio-personalizado/01` preguntaba «¿Está personalizado el precio por una decisión automatizada?» dentro de un bloque cuyo disparador es ese mismo hecho declarado: con el bloque activo, la respuesta es siempre sí. Incidencia [I-27](issues.md#i-27).
- **Decisión:** «Retirarla (Recomendado)»: «El 97.1.f queda como apoyo del disparador; el bloque conserva la pregunta de los parámetros.» Descartadas: «Pregunta universal sí/no» y «Dejarla como está».
- **Interpretaciones adoptadas:**
  - El art. 97.1.f sigue en las referencias del bloque `gen.precio-personalizado` como apoyo de su disparador. La aportación de origen marco que llevaba la pregunta retirada («indicación de que el precio se ha personalizado») sale con ella.
  - El bloque queda con un solo requisito, `gen.precio-personalizado/02`, que conserva su id, su importancia (principal) y su origen inferido. El id `gen.precio-personalizado/01` no se reutiliza.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.22; D-034 y D-065 anotadas en la tabla; I-27 resuelta. La implantación va en T-033.
- **Relacionado:** D-047, D-065, I-27.

### D-068

**La norma que es fuente de un requisito de categoría da aportaciones de origen «referencias».** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-general-layer-issues`. [D-063](#d-063) reserva el origen «marco» a la capa general y describe las referencias como las propiedades de Amazon y los atributos de Shopify. Las aportaciones que salen de la norma de un requisito de categoría (composición textil, información alimentaria, piensos, confituras) no encajaban en ninguno de los dos. En T-031 se registraron con origen «referencias» y la ley en el respaldo. Incidencia [I-28](issues.md#i-28).
- **Decisión:** «Referencias, con la ley en el respaldo (Recomendado)»: «Se precisa que «referencias» incluye la norma que es fuente del requisito. Ya está así en el catálogo.» Descartada: «Marco, con tu aprobación».
- **Interpretaciones adoptadas:**
  - Las aportaciones que salen de una norma, en un bloque de categoría, las redacta quien redacta el bloque, como las demás de referencias, sin aprobación del usuario. El marco sigue siendo solo de la capa general.
  - Solo recogen lo que esa norma exige.
- **Consecuencias:** [resolving-information](../10-model/resolving-information.md#orígenes) 1.4; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.22; D-063 anotada en la tabla; I-28 resuelta.
- **Relacionado:** D-063, D-065, I-28.

### D-069

**Información resolutiva de la capa general aprobada.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-general-layer-resolving-approval`. [D-063](#d-063) dispone que Claude redacta desde la ley las listas de la capa general y que el usuario las aprueba. [D-065](#d-065) las dejó pendientes de aprobación tras dividir la capa general. Tras dos rondas de división, Claude presentó la tercera versión: 60 aportaciones de origen marco, 28 inferidas y 1 de referencias.
- **Decisión:** «Aprobar (Recomendado)»: «Se fijan en catalog/gen.json con la letra de la ley en su respaldo, junto con las 28 inferidas provisionales y la de referencias de gen/20.» Descartada: «Aplazar».
- **Interpretaciones adoptadas:**
  - La aprobación se dio sobre la capa general de D-065. Los cambios posteriores de D-066 y D-067 mueven listas aprobadas sin cambiar su contenido, salvo la aportación de la pregunta retirada, que sale con ella. Las listas siguen aprobadas.
  - Las aportaciones inferidas siguen siendo provisionales ([OQ-55](open-questions.md)).
- **Consecuencias:** [resolving-information](../10-model/resolving-information.md#ejemplo-mínimo) 1.5 (ejemplo y pendientes); D-065 anotada en la tabla. Implantado en `demand-engine/catalog/gen.json` (T-031).
- **Relacionado:** D-063, D-065, D-066, D-067, OQ-55.

### D-070

**El estado «vigente» incluye lo que un intake procesado formula como vigente.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-open-issues-resolution`. [I-11](issues.md#i-11): `docs/CLAUDE.md` definía «vigente» como lo definido en los documentos rectores (CTX, BASE) o en FUND, mientras que desde [D-016](#d-016) lo que un intake formula como vigente se incorpora como vigente. El usuario pidió contexto y Claude se lo dio: la regla escrita y la práctica no coincidían.
- **Decisión:** «Cambiar el texto (Recomendado)»: «La regla pasa a decir lo que ya se hace. Ningún módulo cambia de estado.» Descartada: «Dejarlo».
- **Interpretaciones adoptadas:** el texto es el de la propuesta de I-11; vale también para los updates descritos en la conversación, que la skill transcribe como artefactos archivados.
- **Consecuencias:** `docs/CLAUDE.md` (estados); I-11 resuelta.
- **Relacionado:** D-016, I-11.

### D-071

**Casos de taxonomía corregidos: polar, tapicería de piel y `warmth-level`.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-open-issues-resolution`. [I-13](issues.md#i-13) e [I-15](issues.md#i-15): dos casos no aplicaban del todo la regla de las cuestiones propias, y uno citaba mal un atributo de Shopify. El usuario pidió contexto y Claude lo dio con los datos comprobados.
- **Decisión:** I-13: «Corregir los dos (Recomendado)»: «Cambia el texto de los ejemplos; las conclusiones (polar y piel son especializaciones) se mantienen.» I-15: «Corregir el dato (Recomendado)»: «Se añaden las otras dos categorías que lo tienen; el resultado del caso no cambia.»
- **Interpretaciones adoptadas:**
  - Polar: trae bolitas, electricidad estática y pérdida de pelo; el gramaje y la transpirabilidad ya los pregunta la base (el polar cambia sus valores); el abrigo lo trae «uso invernal» (anotación de I-13).
  - Tapicería de piel: apoyo en el atributo `material` de Sofás en Shopify («Piel», «Cuero») y en `SOFA.upholstery.fabric_type` de Amazon («Cuero»), que cumple la condición 4 del criterio de especialización.
  - `warmth-level`: asignado a Juegos de cama, Colchas y edredones y Cubrecolchones (*Mattress Toppers*), que no son componentes del caso.
- **Consecuencias:** [subclasses](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina) 1.7; [cases](../20-methods/product-taxonomy/cases.md#sofá-reclinable-de-exposición) 1.8; I-13 e I-15 resueltas.
- **Relacionado:** D-024, D-026, I-13, I-15.

### D-072

**El efecto de la relevancia sobre la base de D-030 lo mide la validación automática.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-open-issues-resolution`. [I-17](issues.md#i-17): si una propiedad de Amazon que cuenta como base para decidir una especialización ([D-030](#d-030)) queda fuera del modelo de una clase por la relevancia ([D-039](#d-039), [D-050](#d-050)), una característica podría quedarse sin pregunta.
- **Decisión:** «Cerrar con la salvaguarda (Recomendado)»: «El efecto sobre D-030 se mide en la validación automática: no se acepta una relevancia que deje hechos declarados sin pregunta (D-050).» Descartada: «Comprobación de base explícita».
- **Interpretaciones adoptadas:** es la segunda alternativa de las anotaciones de I-17; la salvaguarda es la métrica «hechos declarados sin pregunta», que ya valida cada ciclo del entrenamiento. Alcance que se acepta al cerrar: un bloque generado en ejecución no se valida hasta que se compila, y su relevancia de Amazon la decide la redacción ([D-045](#d-045), [OQ-49](open-questions.md)); la salvaguarda tampoco alcanza hechos que no declaran las fichas de la clase (D-050 la describe como protección «en parte»).
- **Consecuencias:** [demand-model](../10-model/demand-model.md#sistema-de-construcción-vigente) 2.18; I-17 resuelta.
- **Relacionado:** D-030, D-039, D-050, I-17.

### D-073

**En el MPIR se renderiza siempre con un navegador real.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-open-issues-resolution`. [I-18](issues.md#i-18): `sampling-capture` decía que el renderizado se usaría «selectivamente», pero el motor de captura que aprobó el usuario ([D-042](#d-042)) abre siempre Chrome real.
- **Decisión:** «Actualizarlo (Recomendado)»: «sampling-capture dice que se renderiza siempre, con el motivo de los bloqueos, como hace el motor que aprobaste.» Descartada: «Dejarlo».
- **Interpretaciones adoptadas:** el renderizado deja de ser selectivo; las interacciones (desplegables, selectores, comparadores) siguen haciéndose cuando son pertinentes. Se mantiene que la presencia de JavaScript no es una limitación metodológica.
- **Consecuencias:** [sampling-capture](../20-methods/mpir/sampling-capture.md#contenido-dinámico-e-interacción-selectiva) 1.4; [MPIR](../20-methods/mpir/README.md) 1.2 y [operation-validation](../20-methods/mpir/operation-validation.md) 1.1 (fase de captura); D-042 anotada en la tabla; I-18 resuelta.
- **Relacionado:** D-042, I-18.

### D-074

**Mensajes comunes de la tienda: cuentan si fijan una condición comprobable para la oferta.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-open-issues-resolution`. [I-23](issues.md#i-23): mensajes que la tienda repite en todas sus fichas («envío gratis desde 49 €», «manta de regalo en pedidos de más de 99 €») unos agentes los contaban como información de la oferta y otros como afirmaciones genéricas.
- **Decisión:** «Sí, si fijan una condición comprobable (Recomendado)»: «Un importe, un plazo o un coste que vale para esta oferta cuenta en la pregunta que responde; las frases genéricas no cuentan.» Descartada: «No, nunca».
- **Interpretaciones adoptadas:** cuenta como hecho declarado de la oferta en la pregunta que responde (coste del envío, promociones…) y, como el disparador es el hecho declarado ([D-037](#d-037)), también activa el bloque condicionado que declara (un descuento para toda la tienda activa `gen.descuento`); un mensaje sin condición comprobable sigue siendo una afirmación genérica de la tienda, que no cuenta.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.23; I-23 resuelta. La implantación en el reglamento del clasificador (paso 1) va en T-034.
- **Relacionado:** D-049, I-23, OQ-50.

### D-075

**«Aportación» siempre con su complemento: resolutiva o al modelo de demanda.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-open-issues-resolution`. [I-25](issues.md#i-25): «aportación» nombraba dos cosas, la aportación resolutiva ([D-064](#d-064)) y lo que un resultado del MPIR aporta al modelo de demanda (confirmación, ampliación…). Hubo tres rondas:
  1. El usuario eligió «Renombrar el del MPIR».
  2. Eligió «Hallazgo (Recomendado)». Claude lo había presentado como un nombre que no coincidía con nada del canon.
  3. Antes de aplicarlo, Claude comprobó que «hallazgo» ya es un término de la auditoría y se lo dijo al usuario, que eligió «Siempre con su adjetivo» frente a «Resultado del contraste (Recomendado)», «Efecto sobre el modelo» y «Hallazgo igualmente».
- **Decisión:** «Siempre con su adjetivo»: «No se renombra: «aportación resolutiva» y «aportación al modelo de demanda».»
- **Interpretaciones adoptadas:**
  - Prevalece la tercera respuesta, que vuelve a abrir la elección; la segunda se basaba en un dato erróneo de Claude. En la primera ronda, «Siempre con su adjetivo» era la opción recomendada y se descartó.
  - El «adjetivo» del MPIR es el complemento «al modelo de demanda». Regla única: Fuera de `resolving-information`, la aportación resolutiva lleva siempre su adjetivo, y la del MPIR, siempre «al modelo de demanda».
- **Consecuencias:** [interpretation-transfer](../20-methods/mpir/interpretation-transfer.md#tipos-de-aportación-al-modelo-de-demanda) 1.1, [operation-validation](../20-methods/mpir/operation-validation.md) 1.1 y [concepts-architecture](../20-methods/mpir/concepts-architecture.md) 1.1; [resolving-information](../10-model/resolving-information.md#definición) 1.6; [model-training](../10-model/model-training.md) 1.13, [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo), glosario (nueva entrada «Aportación al modelo de demanda») y OQ-03 con «aportación resolutiva»; D-064 anotada en la tabla; I-25 resuelta.
- **Relacionado:** D-064, I-25.

### D-076

**Solo las opiniones del producto o de la oferta cuentan como opiniones publicadas.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-open-issues-resolution`. [I-29](issues.md#i-29): [D-066](#d-066) no decía si las opiniones sobre la tienda (reseñas en Google o Tripadvisor, valoración global del comercio) responden `gen/15` y activan `gen.opiniones`.
- **Decisión:** «Solo las del producto u oferta (Recomendado)»: «Las de la tienda no responden gen/15 ni activan gen.opiniones.» Descartada: «También las de la tienda».
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.23; I-29 resuelta. La implantación en el reglamento del clasificador (pasos 1 y 6) va en T-034.
- **Relacionado:** D-066, D-074, I-29.

### D-077

**El nombre del modelo de demanda muestra la composición completa, con los sectores.** · aceptada · 2026-10-26

- **Contexto:** `INTAKE 2026-10-26-model-name-full-composition`. Por [D-038](#d-038), «los bloques universales y los de sector no se nombran»: el nombre empezaba por las categorías de la clase y solo la clave llevaba los sectores. En la versión de Shopify usada (v2026-08), 311 nombres de categoría se repiten y afectan a 702 categorías, así que dos modelos distintos podían llevar el mismo nombre. Claude propuso tres alternativas y recomendó nombrar el sector solo cuando el nombre de la categoría se repite.
- **Decisión:** palabras del usuario: «Me interesa que figure la composición completa». Los bloques de sector se nombran delante de las categorías. Sustituye en ese punto a D-038 y a la sintaxis del nombre de [D-047](#d-047). Descartadas: dejar el nombre como estaba y nombrar el sector solo cuando el nombre se repite.
- **Interpretaciones adoptadas:**
  - Sintaxis: «Sectores › Categorías (alias) · especializaciones». Los sectores van de lo general a lo particular, en el orden de la clave, separados por «›»; los del mismo nivel de Shopify se unen con «+», como las categorías; un último «›» los separa de las categorías. Ejemplo: «Casa y jardín › Ropa de casa › Ropa de cama › Sábanas + Fundas de almohada y de cojines › Sábanas planas + Sábanas ajustables + Fundas de almohada · juego».
  - «Composición completa» son los bloques del modelo: se nombran los sectores que tienen bloque. Un nivel de Shopify sin bloque no forma parte de la composición y no se nombra; las categorías de la clase y los alias se siguen nombrando aunque no tengan bloque, como hasta ahora. El ejemplo de la opción B del artefacto («Casa y jardín › Ropa de casa › Toallas · juego») omitía las categorías de la clase sin bloque; con esta lectura, ese producto se nombra «Casa y jardín › Ropa de casa › Toallas › Toallas de baño + Toallas de mano · juego».
  - La capa general sigue sin nombrarse (el bloque universal y los condicionados de la oferta): está en todos los modelos y la clave ya la abre con su versión. Los bloques generales del producto siguen tras las especializaciones.
  - Los sectores y las categorías se nombran con su nombre en Shopify, en la versión fijada, no con el nombre del bloque, que puede diferir («Cojines decorativos» frente a «Cojines»).
- **Consecuencias:** [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.19; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#denominación) 1.24 (ejemplos); [cases](../20-methods/product-taxonomy/cases.md) 1.9 (nombre del caso del Stressless); glosario (modelo de demanda); motor de demanda (`demand-engine/src/demand_engine/demand/model.py`, ensamblado del nombre).
- **Relacionado:** D-033, D-038, D-040, D-047.

### D-078

**Un descuento de toda la tienda activa `gen.descuento` aunque dependa de una acción del comprador.** · aceptada · 2026-10-26

- **Contexto:** [I-30](issues.md#i-30). En la tanda de control T-032, el mensaje común «Suscríbete a la news y ahorra un 10 %» de burritoblanco.com activa `gen.descuento` en 11 de las 14 salidas sin rebaja propia y en 3 no; la oferta de tres casos cambia entre las dos ejecuciones. [D-074](#d-074) dice que un descuento para toda la tienda activa el bloque, pero no si cuenta uno que depende de una acción del comprador.
- **Decisión:** palabras del usuario: «Aplica según recomendado». Se acepta la propuesta de I-30: un descuento de toda la tienda activa `gen.descuento` aunque dependa de una acción del comprador (suscribirse, un código, la primera compra o un importe mínimo); sus condiciones las pregunta `gen.descuento/02`. Descartada: que solo active el bloque una rebaja que se aplica sin otra acción del comprador.
- **Interpretación adoptada:** sigue haciendo falta una condición comprobable (D-074): un importe o un porcentaje. Un mensaje sin cifra («descuentos exclusivos para suscriptores») sigue siendo una afirmación genérica.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.25 (mensajes comunes de la tienda); D-074 anotada en la tabla; I-30 resuelta; reglamento del clasificador (paso 1), T-035.
- **Relacionado:** D-049, D-074, I-30.

### D-079

**La ficha identifica la unidad de exposición cuando sitúa en la exposición la unidad que se vende.** · aceptada · 2026-10-26

- **Contexto:** [I-31](issues.md#i-31). [D-057](#d-057) cuenta como estado declarado «la unidad de exposición que la ficha identifica como tal». La ficha del Stressless no usa esa expresión: «Visita la exposición en Les Corts para aprovechar la última unidad». En T-032 una ejecución activó `gen.unidad-no-nueva` y la otra no; el caso de control lo espera activado.
- **Decisión:** palabras del usuario: «Aplica según recomendado». Se acepta la propuesta de I-31: la ficha identifica la unidad de exposición cuando sitúa en la exposición de la tienda la unidad que se vende, aunque no use esa expresión («la última unidad, en exposición»; «visita la exposición para aprovechar la última unidad»). «Outlet», «revisado» o una garantía reducida, por sí solos, no bastan.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.25 (valores de oferta); D-057 anotada en la tabla; I-31 resuelta; reglamento del clasificador (paso 6), T-035.
- **Relacionado:** D-037, D-057, I-22, I-31.

### D-080

**Quien comercializa el producto con su nombre o marca responde la pregunta del fabricante.** · aceptada · 2026-10-26

- **Contexto:** [I-32](issues.md#i-32). Las fichas de burritoblanco.com dicen «Importado y comercializado por Burrito Blanco, S.L.U.» sin nombrar al fabricante, y el producto lleva la marca de la tienda. En T-032, las 18 salidas de la tienda llevan ese hecho a `gen/18` (9), `gen/13` (6), `gen/17` (3) o a ninguna pregunta (1).
- **Decisión:** palabras del usuario: «Aplica según recomendado». Se acepta la propuesta de I-32:
  - El Reglamento (UE) 2023/988 (art. 3, punto 8) considera fabricante a quien encarga el diseño o la fabricación de un producto y lo comercializa con su nombre o marca: quien vende el producto con su marca responde `gen/17`.
  - La lista de información resolutiva de `gen/17` suma la aportación «nombre o marca de quien encarga el diseño o la fabricación y comercializa el producto con su marca», de origen «marco», con el art. 3.8 como fuente. (Con [D-084](#d-084), las listas de la capa general ya no requieren aprobación.)
  - `gen/18` queda para el fabricante establecido fuera de la UE.
- **Interpretación adoptada:** «Importado y comercializado por X», sin otra marca en el producto que la de X, se lee como que X lo comercializa con su marca. Si el producto lleva la marca de otro, X es el importador y no responde `gen/17`.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.25 (apoyo de la pregunta del fabricante); D-052 y D-069 anotadas en la tabla; I-32 resuelta; `demand-engine/catalog/gen.json` (`gen/17`, capa general 0.6) y reglamento del clasificador (paso 8), T-035.
- **Relacionado:** D-052, D-063, D-069, I-32.

### D-081

**Una garantía nombrada sin contenido ni condiciones no activa `gen.garantia-comercial`.** · aceptada · 2026-10-26

- **Contexto:** [I-33](issues.md#i-33). «Garantía de calidad: Burrito Blanco, S.L.U.», en una lista de responsables y sin alcance, plazo ni condiciones, activa la garantía comercial en las dos ejecuciones de las toallas de T-032 y no en las otras 16 salidas de la tienda.
- **Decisión:** palabras del usuario: «Aplica según recomendado». Se acepta la propuesta de I-33: una garantía nombrada sin contenido ni condiciones no permite saber que es distinta de la legal y no activa `gen.garantia-comercial`; activarla sería suponer un hecho que la ficha no declara. La activa una garantía que declara algo que la legal no da: más plazo, otra cobertura u otro garante. Descartada: activarla siempre que la ficha nombre una garantía distinta de la legal.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.25 (disparadores); D-066 anotada en la tabla; I-33 resuelta; reglamento del clasificador (paso 6), T-035.
- **Relacionado:** D-037, D-066, I-33.

### D-082

**Varias opciones visibles en un selector activan `gen.variantes`; una sola, no.** · aceptada · 2026-10-26

- **Contexto:** [I-34](issues.md#i-34). En las toallas de T-032, el selector «Color» muestra seis muestras cuyos nombres solo están en atributos HTML: una ejecución activa `gen.variantes` y la otra no. Los selectores de una sola opción (cojín, protector, plaid) no lo activan en ninguna ejecución, pero ninguna regla lo decía.
- **Decisión:** palabras del usuario: «Aplica según recomendado». Se acepta la propuesta de I-34: un selector con varias opciones visibles en la ficha declara que hay variantes y activa `gen.variantes`, aunque sus nombres estén solo en atributos; esos nombres no cuentan como valores declarados. Un selector de una sola opción no lo activa.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.25 (disparadores); I-34 resuelta; reglamento del clasificador (pasos 1 y 6), T-035.
- **Relacionado:** D-037, D-047, I-34.

### D-083

**Política de cambios: bloque condicionado `gen.cambios` de la capa general.** · sustituida por [D-085](#d-085) · 2026-10-26

- **Contexto:** [I-35](issues.md#i-35). Por [D-064](#d-064), un plazo de cambio no aporta a la pregunta de desistimiento (`gen/11`), y ningún requisito de la capa general pregunta por los cambios. En T-032, el plazo de cambio de 14 días de burritoblanco.com es 18 de los 66 hechos sin pregunta.
- **Decisión:** palabras del usuario: «Aplica según recomendado». Se acepta la recomendación de I-35: la política de cambios es una condición de la oferta, con un bloque condicionado propio, `gen.cambios`, como los de [D-066](#d-066). Disparador: si admite cambios. Alcance: la oferta. Descartada: dejarla fuera del modelo.
- **Segunda ronda (2026-10-26).** La revisión independiente señaló que la importancia, la división del coste y la lista de información resolutiva eran del usuario: la capa general no cambia sin su decisión ([D-045](#d-045), [D-069](#d-069)). El usuario eligió:
  - «Principal (Recomendado)», frente a «Complementario» (lo que Claude había aplicado) y «Por fijar»;
  - «Requisito propio (Recomendado)» para el coste del cambio, frente a dejarlo como aportación;
  - las cuatro aportaciones propuestas para `gen.cambios/01`.
- **Interpretaciones adoptadas:**
  - `gen.cambios/01`: «¿En qué plazo y en qué condiciones se puede cambiar el producto?». Plazo y condiciones van juntos, como en `gen/11` (D-060, regla 3: lo que solo tiene sentido unido). La pregunta no repite el disparador («¿se puede cambiar?»), como pide [D-067](#d-067). Importancia principal: el cambio es un criterio para elegir entre ofertas ([D-035](#d-035)), como la garantía comercial.
  - `gen.cambios/02`: «¿Qué coste del cambio asume el comprador?», paralelo al coste de devolución (`gen/26`), que [D-065](#d-065) separó de `gen/11`. Toma su importancia, principal, por ese paralelo.
  - Entidad «condiciones»; origen «inferida», porque ninguna norma obliga a admitir cambios; sin fuentes.
  - Información resolutiva, inferida:
    - de `gen.cambios/01`, aprobada por el usuario: plazo para solicitar el cambio; qué se puede cambiar (otra talla, medida, color u otro producto); estado en que debe estar el producto para cambiarlo; forma de solicitar el cambio;
    - de `gen.cambios/02`: coste del cambio para el comprador. Es la pregunta misma. Con [D-084](#d-084) no requiere aprobación.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.20 y glosario (lista de la aplicación); [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.25 (tabla y disparadores); D-034, D-047 y D-069 anotadas en la tabla; I-35 resuelta; `demand-engine/catalog/gen.json` (capa general 0.6) y reglamento del clasificador (pasos 6 y 8), T-035.
- **Relacionado:** D-034, D-035, D-045, D-047, D-064, D-065, D-066, D-067, D-069, I-35.

### D-084

**La información resolutiva de la capa general no requiere la aprobación del usuario.** · aceptada · 2026-10-26

- **Contexto:** [D-063](#d-063) y [D-069](#d-069) disponen que el usuario aprueba las listas de información resolutiva de la capa general. En D-083 quedó pendiente de esa aprobación la aportación de `gen.cambios/02`, y Claude la presentó al usuario.
- **Decisión:** palabras del usuario: «No he de aprobarlo, es cosa orgánica de los agentes. La revisión, si hace falta, ya la solicito yo. Aplica lo que consideres y cambia el canon.» Las listas de información resolutiva de la capa general no requieren su aprobación. Sustituye en ese punto a D-063 y a D-069.
- **Interpretaciones adoptadas:**
  - Las redacta Claude o el agente que redacta: las que salen de la ley, con origen «marco» y la norma como respaldo; las que no, como inferidas ([D-065](#d-065)). El entrenamiento les añade las observadas en las fichas ([D-063](#d-063)), como hasta ahora.
  - El usuario las revisa cuando lo pide. Las listas aprobadas por D-069 siguen como están.
  - La decisión es sobre la información resolutiva. Las preguntas, los disparadores y las importancias de la capa general siguen siendo parte del marco, que no cambia sin decisión del usuario ([D-045](#d-045)).
- **Consecuencias:** [resolving-information](../10-model/resolving-information.md) 1.7 y [model-training](../10-model/model-training.md) 1.14; D-063 y D-069 anotadas en la tabla; D-080 y D-083 anotadas; `demand-engine/catalog/gen.json` (nota de la información resolutiva).
- **Relacionado:** D-045, D-063, D-065, D-069, D-080, D-083.

### D-085

**Los cambios son condiciones de devolución y cambio: van en `gen/11` y `gen/26`, no en la aplicación.** · aceptada · 2026-10-26

- **Contexto:** [D-083](#d-083) creó el bloque condicionado `gen.cambios`, cuyo disparador («admite cambios») entraba en la aplicación de la oferta. Al explicárselo, el usuario lo corrigió: «eso son condiciones de devolución, cambio; no es una característica de la oferta».
- **Decisión:** el usuario eligió «Dentro de `gen/11`», frente a «Universales, junto a devolución (Recomendado)», que creaba dos requisitos universales nuevos. Sustituye a D-083 y cambia el ejemplo de [D-064](#d-064), en el que un plazo de cambio no aportaba a la pregunta de desistimiento.
  - Se retiran `gen.cambios` y su disparador; los ids `gen.cambios/01` y `/02` no se reutilizan ([D-038](#d-038)). La aplicación vuelve a la lista de [D-066](#d-066).
  - `gen/11` pasa a «¿Se puede desistir, devolver o cambiar, en qué plazo y en qué condiciones?». Las aportaciones de `gen.cambios/01` pasan a su lista, con origen «inferida», junto a una que no tenía: la posibilidad de cambiar el producto.
- **Interpretaciones adoptadas:**
  - El coste del cambio sigue al coste de devolución: `gen/26` pasa a «¿Qué coste de devolución o de cambio asume el comprador?», con la aportación «coste del cambio para el comprador», inferida. Así se respeta la división de [D-065](#d-065) entre plazo y condiciones (`gen/11`) y coste (`gen/26`).
  - Las importancias (principal), las fuentes (97.1.j y 97.1.k) y los orígenes de los requisitos no cambian. La parte del cambio no tiene norma, y por eso sus aportaciones son inferidas ([D-065](#d-065)).
  - Un «no admite cambios» fundamentado responde la parte del cambio, como en las demás preguntas universales.
- **Consecuencias:**
  - [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.21 y glosario: la lista de la aplicación sin «cambios admitidos».
  - [resolving-information](../10-model/resolving-information.md#ejemplo-mínimo) 1.8: el ejemplo de `gen/11`.
  - [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.26 y [cases](../20-methods/product-taxonomy/cases.md) 1.11.
  - D-034, D-047, D-064 y D-083 anotadas en la tabla.
  - `demand-engine/catalog/gen.json`, capa general 0.6, que aún no había usado ningún modelo, y el reglamento del clasificador (secciones 0, 6 y 8).
- **Relacionado:** D-038, D-064, D-065, D-066, D-083, I-35.

### D-086

**La especialización «juego» aporta qué piezas incluye y cuántas de cada una; las medidas, los bloques de cada pieza.** · aceptada · 2026-10-26

- **Contexto:** [I-36](issues.md#i-36). [study-class](../10-model/study-class.md#composición-de-la-clase) decía que «juego» aporta «qué piezas incluye, cuántas y en qué medidas». Las medidas de cada pieza ya las preguntan los bloques de su categoría, y la regla 3 de [D-060](#d-060) separa el contenido de la medida. En T-032, 3 de las 8 salidas con `esp.juego` añaden un requisito de medidas y 5 no, y los requisitos de la especialización cambian entre A y B.
- **Decisión:** palabras del usuario: «Resuelve todas las incidencias con tus propias recomendaciones». Se acepta la propuesta de I-36. «Juego» aporta lo que es del conjunto: qué piezas incluye y cuántas de cada una; si cambian con la medida elegida, va en la aplicabilidad, por variante. Las medidas de cada pieza las preguntan los bloques de su categoría, y solo son requisito del juego si ningún bloque de las piezas las pregunta.
- **Consecuencias:** [study-class](../10-model/study-class.md#composición-de-la-clase) 1.5 (enmienda del texto del intake); [subclasses](../20-methods/product-taxonomy/subclasses.md) 1.8 y [cases](../20-methods/product-taxonomy/cases.md) 1.12; I-36 resuelta; reglamento del clasificador (paso 4), T-036.
- **Relacionado:** D-023, D-032, D-060, I-36.

### D-087

**La regla 3 prevalece sobre la forma de sí o no con detalle.** · aceptada · 2026-10-26

- **Contexto:** [I-37](issues.md#i-37). La regla 2 de [D-060](#d-060) mantiene la pregunta de sí o no seguida de su detalle; la regla 3 divide cuando las partes tomarían otro rasgo u otra importancia. `cat.sofas-cama/02` tenía las dos formas: el «incluye colchón», votado crítico, y la medida y la retirada del colchón, que son medida y construcción.
- **Decisión:** palabras del usuario: «Resuelve todas las incidencias con tus propias recomendaciones». Se acepta la propuesta de I-37. La forma de sí o no con detalle se mantiene solo si el detalle toma el mismo rasgo y la misma importancia que la pregunta; si no, el detalle pasa a requisitos condicionados al hecho.
- **Interpretaciones adoptadas:** la revisión de los tres requisitos citados en I-37, con el vocabulario de rasgos:
  - `cat.sofas-cama/02` pasa a «¿Incluye colchón?»; nuevos `/18`, «¿De qué medida es el colchón que incluye?» (medida), y `/19`, «¿Se puede retirar el colchón que incluye?» (construcción), los dos condicionados a que lo incluya.
  - `cat.juguetes-para-perros/06` pasa a «¿Qué pilas o batería usa y es recargable?»; nuevo `/16`, «¿Se incluyen las pilas o la batería?» (contenido).
  - `cat.mantas/05` («¿Qué peso y qué grosor tiene la manta?») no cambia: peso y grosor son magnitud ([D-051](#d-051)) y toman la misma importancia. En cambio, `cat.cojines-decorativos/01` («¿Qué medidas tiene (largo, ancho y grosor)?»), que un agente señaló en T-032, mezclaba medida y magnitud: pasa a «largo y ancho» y el grosor va a `/14` (magnitud).
  - Las partes nuevas conservan sus fuentes y sus aportaciones; su rasgo y su importancia los resuelven las reglas 6, como en la compilación. Las partes que conservan el id son las que mantienen el rasgo del requisito original, como en T-031.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formulación-de-las-cuestiones) 1.27 (regla 2); D-060 anotada en la tabla; I-37 resuelta; `demand-engine/catalog/DRAFTING.md`, el reglamento del clasificador (paso 4), el índice de rasgos y los bloques citados, T-036.
- **Relacionado:** D-051, D-060, D-065, I-37.

### D-088

**Una cuestión con fuente que el bloque ni pregunta ni excluye es una propuesta al bloque.** · aceptada · 2026-10-26

- **Contexto:** [I-38](issues.md#i-38). Las cuestiones inferidas no tienen fuente (D-060, regla 4), y el clasificador no debe duplicar la base, que incluye las propiedades del PTD de Amazon ([D-030](#d-030), [D-039](#d-039)). En T-032, un agente redactó inferidas con fuente en el PTD, que el bloque no recogía, y otro dudó si podía preguntar lo que solo estaba en el PTD.
- **Decisión:** palabras del usuario: «Resuelve todas las incidencias con tus propias recomendaciones». Se acepta la propuesta de I-38:
  - Lo que recoge una referencia de la base y el bloque ni pregunta ni excluye es una omisión del bloque.
  - El clasificador lo redacta como cuestión inferida con su fuente, que es una propuesta al bloque, y el entrenamiento la incorpora al catálogo al compilar.
  - «Sin duplicar la base» se lee como no duplicar los requisitos de los bloques ni los de la capa general.
- **Interpretaciones adoptadas:**
  - Mientras no se compila, la propuesta va en el modelo como las inferidas: provisional y fuera de la clave, con origen «referencias».
  - La comprobación de la salida rechaza una fuente que no existe en las referencias o que el bloque ya pregunta o excluye.
  - Al compilar, cada propuesta entra en su bloque con un id que el bloque no ha usado, con la importancia que votó el agente como etiqueta de partida. El rasgo y la importancia los deciden las reglas, como en todo requisito.
  - Una sola por fuente: si dos casos proponen la misma fuente, entra la primera.
  - No hace falta verla en dos casos, porque la fuente es la prueba.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.27 y [model-training](../10-model/model-training.md) 1.15; D-036 anotada en la tabla; I-38 resuelta; reglamento del clasificador (paso 5) y código del motor (`bin/model check`, `bin/train compile` y el informe), T-036.
- **Relacionado:** D-030, D-036, D-039, D-041, D-044, D-060, I-38.

### D-089

**Precio anterior y precio por unidad de medida en la capa general, con su norma.** · aceptada · 2026-10-26

- **Contexto:** [I-39](issues.md#i-39). En T-032, los agentes propusieron desde las fichas el «precio más bajo aplicado en los 30 días anteriores» para `gen.descuento/01` y el «precio por unidad de medida» para `gen/04`. Los fija la norma, pero las listas de la capa general no los tenían.
- **Decisión:** palabras del usuario: «Resuelve todas las incidencias con tus propias recomendaciones». Se acepta la propuesta de I-39. Con [D-084](#d-084), las listas no requieren aprobación.
  - `gen.descuento/01` suma la aportación «precio más bajo aplicado en los 30 días anteriores», de origen «marco». Su fuente es la Ley 7/1996, de Ordenación del Comercio Minorista, art. 20.1 (texto consolidado del BOE a 30/03/2022; redacción del Real Decreto-ley 24/2021, que traspone la Directiva (UE) 2019/2161): «se entenderá por precio anterior el menor que hubiese sido aplicado sobre productos idénticos» en los treinta días anteriores.
  - `gen/04` suma la aportación «precio por unidad de medida», de origen «marco». Su fuente es el Real Decreto 3423/2000, art. 3.2 (BOE a 28/12/2000), que traspone la Directiva 98/6/CE.
- **Interpretaciones adoptadas:**
  - Con una norma que lo exige con claridad, el origen de `gen.descuento/01` pasa de «inferida» a «normativa».
  - El precio unitario queda como aportación de `gen/04` y no como requisito propio; la alternativa de I-39 se descarta.
  - Identificadores de fuente: `ley:LOCM-20.1@2022-03-30` y `ley:RD-3423/2000-3.2@2000-12-28`.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.27 (apoyo de `gen/04` y de `gen.descuento/01`); I-39 resuelta; `demand-engine/catalog/gen.json` (capa general 0.6), T-036.
- **Relacionado:** D-034, D-063, D-065, D-084, I-39.

### D-090

**Derivar una prestación de un atributo no resuelve el requisito de la prestación.** · aceptada (enmendada por [D-119](#d-119): se decide en la pertinencia, no en la valoración de los AC) · 2026-10-27

- **Contexto:** `INTAKE 2026-10-26-choice-criteria-and-descriptions` §1, a partir de las sondas de People Also Ask sobre el modelo de demanda de sábanas Coralina. Palabras del usuario: «derivar frescura de «percal 100 % algodón» no es aceptable. Demasiado nivel de derivación. pero eso ya es tarea de la valoración de criterios de aceptación. pero para ello sí necesitamos requisitos informativos para hacer esa evaluación».
- **Decisión:**
  - Que una ficha declare el tejido o la composición («percal», «100 % algodón») no resuelve un requisito sobre la prestación («¿qué sensación térmica ofrece?»).
  - Quien lo dictamina es la valoración de los [criterios de aceptación](../10-model/acceptance-criteria.md#interpretación), en la auditoría, no el modelo de demanda.
  - Para que la auditoría pueda dictaminarlo, el requisito de la prestación tiene que existir en el modelo.
- **Interpretación adoptada:** el artefacto dice que la derivación «tiene demasiados pasos y se apoya en conocimiento del dominio». La regla 7 de los criterios de aceptación prohíbe penalizar una derivación válida por su número de pasos y no presentar como publicado lo que se completa con conocimiento externo no acreditado. Se lee que la derivación no es válida porque completa una prestación no declarada con conocimiento del dominio; el número de pasos sigue sin ser un criterio. Así no se contradice la regla 7 ni la invariante 9; si el usuario quería limitar el número de pasos, habría que enmendar ambas. La frontera operativa con el reconocimiento semántico legítimo (`InStock`) queda en [OQ-56](open-questions.md).
- **Consecuencias:** [acceptance-criteria](../10-model/acceptance-criteria.md#interpretación) 1.1; [choice-criteria](../10-model/choice-criteria.md#prestación-derivada-de-un-atributo) 1.0; [resolving-information](../10-model/resolving-information.md#reglas-e-invariantes) 1.9 (regla 6); OQ-56.
- **Relacionado:** D-062, D-091, OQ-21, OQ-56.

### D-091

**Un criterio de elección genera un requisito cuando cumple las condiciones C1–C4.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-26-choice-criteria-and-descriptions` §2. Las preguntas valorativas de People Also Ask no son requisitos informativos (no preguntan por una oferta, no son neutrales y dependen del comprador), pero revelan los **criterios de elección** de la clase. La expresión ya aparecía en el MPIR; se prefiere a «criterios de evaluación», que se confundiría con los criterios de aceptación. Palabras del usuario: «Entonces los criterios de elección en algunos casos sí deberían generar requisitos».
- **Decisión:** regla propuesta por Claude, que el usuario aprobó registrar («OK»). Un criterio de elección genera un requisito cuando cumple todas estas condiciones:
  - C1: ningún requisito existente lo responde sin derivar;
  - C2: es un hecho que la oferta puede declarar (una prestación, un resultado de ensayo, una indicación de uso);
  - C3: se aplica a toda la clase o a una especialización, no a un comprador;
  - C4: se puede formular neutral y sobre la oferta.

  El requisito resultante es un requisito ordinario (en el catálogo de rasgos, casi siempre `prestacion`) y no se crea un concepto nuevo en el modelo. El criterio de elección queda como su fundamento. Su información resolutiva es la declaración de la prestación, un ensayo o una certificación, nunca el atributo del que se deduciría la prestación ([D-090](#d-090)). Que los compradores usen un criterio para elegir no prueba su importancia relativa, que sigue saliendo de las reglas.
- **Interpretaciones adoptadas:**
  - «Aprobó registrarla» se lee como aprobación de la regla: se incorpora como vigente.
  - «No se crea un concepto nuevo» se refiere al requisito resultante. El criterio de elección, que el canon ya usaba sin definir, recibe módulo y entrada de glosario para fijar su sentido y sus distinciones.
  - La vía por la que se reconocen los criterios de elección (MPIR; PAA, sin adoptar) no cambia: si PAA se adopta como vía de construcción y la excepción a D-042 que exigiría quedan fuera del artefacto ([OQ-57](open-questions.md)).
- **Consecuencias:** módulo nuevo [choice-criteria](../10-model/choice-criteria.md) 1.0; [demand-model](../10-model/demand-model.md#sistema-de-construcción-vigente) 2.22; [resolving-information](../10-model/resolving-information.md#reglas-e-invariantes) 1.9; [MPIR](../20-methods/mpir/README.md) (enlace); glosario. Los requisitos candidatos de la clase de sábanas (sensación térmica, arrugas, durabilidad) y la aplicación de la regla en el clasificador y en la redacción de bloques quedan para la implantación (T-040).
- **Relacionado:** D-036, D-056, D-090, OQ-57.

### D-092

**Los requisitos informativos llevan una descripción de tres partes.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-26-choice-criteria-and-descriptions` §3. Palabras del usuario: «Los requisitos informativos necesitan una descripción. A veces el título puede ser bastante abstracto y la descripción debe ayudar a concretarlo».
- **Decisión:** cada requisito informativo lleva una descripción que concreta el título. El usuario aceptó este patrón:
  1. qué se pregunta en concreto, con ejemplos de lo que abarca;
  2. qué tipo de información lo responde;
  3. qué no lo responde y con qué requisito vecino no se confunde.

  Los cuatro ejemplos del artefacto (`cat.fundas-de-almohada/06`, la sensación térmica de la sábana, `gen/21` y `cat.sabanas-ajustables/01`) quedan como ejemplos aceptados (los dos primeros, actualizados por [D-108](#d-108)).
- **Interpretación adoptada:** el «título» es la pregunta del requisito. «Necesitan» se lee como registro obligatorio en el catálogo, como la información resolutiva, y no opcional como los demás registros operativos de BASE §4.1.
- **Consecuencias:** módulo nuevo [requirement-description](../10-model/requirement-description.md) 1.0; [demand-model](../10-model/demand-model.md#requisito-informativo-ri) 2.22; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.28 (campos de un requisito); glosario. Implantación en el catálogo y en la redacción de bloques: pendiente.
- **Relacionado:** D-060, D-062, D-093, OQ-03.

### D-093

**La descripción es prosa y no repite la información resolutiva.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-26-choice-criteria-and-descriptions` §3, punto abierto para el procesamiento. Las partes 2 y 3 de la descripción ([D-092](#d-092)) se solapan con la información resolutiva (D-062 a D-064) y con el perfil de resolución y pertinencia ([OQ-03](open-questions.md)). Propuesta de Claude en el artefacto, sin decidir: «la descripción es prosa para personas y agentes, y la información resolutiva es la lista estructurada. La descripción no repite esa lista».
- **Decisión:** se adopta la propuesta. La descripción es prosa para personas y agentes; la información resolutiva, la lista estructurada de aportaciones resolutivas. La descripción no repite esa lista.
- **Interpretaciones adoptadas:**
  - El artefacto deja el punto al procesamiento; se decide con la propuesta que trae, la única formulada.
  - La parte 2 dice en prosa qué tipo de información responde, como en los ejemplos aceptados («una declaración del vendedor o del fabricante […] o el resultado de un ensayo»), sin enumerar las aportaciones.
  - La relación de las partes 1 y 3 con los componentes, las expresiones de ejemplo y los casos fronterizos del perfil del RI no la resuelve el artefacto: se anota en OQ-03.
- **Consecuencias:** [requirement-description](../10-model/requirement-description.md#reglas-e-invariantes) 1.0; [resolving-information](../10-model/resolving-information.md#distinciones) 1.9; OQ-03 anotada.
- **Relacionado:** D-062, D-063, D-064, D-092, OQ-03.

### D-094

**People Also Ask (PAA): vía de construcción del modelo de demanda.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-construction-route` §1, tarea T-039. Las sondas de PAA sobre la clase de sábanas (2026-10-26) y el motor PAA (T-037) revelaron criterios de elección. [D-091](#d-091) dejó fuera si PAA se adoptaba como vía ([OQ-57](open-questions.md)). Objetivo de T-039, fijado con el usuario: «adopte PAA como vía de construcción del modelo de demanda (enmienda D-009 y D-036, MPIR aparcado)».
- **Decisión:**
  - Las preguntas de «Más preguntas» de google.es, recogidas para un conjunto de semillas de una clase, son una vía de construcción del modelo de demanda. Sirven para reconocer criterios de elección (a los que se aplica C1–C4), confirmar requisitos del catálogo y confirmar o revisar cuestiones inferidas.
  - Solo se conservan las preguntas. Las respuestas, texto de la IA de Google, no son evidencia de ninguna página: ni se leen ni se cargan. PAA no aporta información resolutiva.
  - PAA no prueba por sí sola la importancia relativa, que sigue saliendo de las reglas. Que una pregunta aparezca, o en qué posición, no se puntúa.
  - La estrategia de semillas es operativa: vive en el README del motor y está calibrada con una sola clase.
- **Interpretaciones adoptadas:**
  - Enmienda [D-009](#d-009) (BASE §4.2): se añade una vía de referencia a la taxonomía y al MPIR. Enmienda [D-036](#d-036): la confirmación o revisión de las cuestiones inferidas que se encargaba al MPIR «cuando exista» la hace PAA; el régimen provisional y su validación en el entrenamiento ([D-044](#d-044)) no cambian.
  - PAA contrasta el catálogo con preguntas de compradores filtradas por Google: avanza [OQ-01](open-questions.md) (contraste con fuentes empíricas), pero no la cierra, porque no son consultas reales sin filtrar ni investigación de usuarios.
  - El contraste de las especializaciones con el MPIR ([study-class](../10-model/study-class.md)) no se encarga a PAA: el artefacto no lo dice.
- **Consecuencias:** [construction-routes](../10-model/construction-routes.md) 1.0; [choice-criteria](../10-model/choice-criteria.md) 1.1; glosario (PAA); OQ-57 cerrada; OQ-01 anotada. Clasificación de las preguntas con agentes: T-040.
- **Relacionado:** D-009, D-036, D-091, D-095, D-096, D-097, OQ-01, OQ-57.

### D-095

**El MPIR queda aparcado.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-construction-route` §2, tarea T-039 («MPIR aparcado»). PAA cumple el papel del MPIR en la construcción del modelo ([D-094](#d-094)).
- **Decisión:** el método del MPIR sigue en el canon como propuesta, pero no se ejecuta ni se desarrolla por ahora. Mientras esté aparcado:
  - su papel en la construcción (reconocer criterios de elección y confirmar cuestiones inferidas) lo cumple PAA;
  - sus cuestiones abiertas siguen abiertas, sin trabajarse;
  - el motor de captura sigue en uso, porque es compartido con el entrenamiento ([D-046](#d-046)).

  Retomarlo es una decisión nueva.
- **Interpretación adoptada:** el alcance de «aparcado» lo propuso Claude en el artefacto, por encargo de T-039. Las referencias del canon al MPIR como vía o como contraste posterior se mantienen, porque el método no se retira; se leen como suspendidas mientras dure el aparcamiento.
- **Consecuencias:** [construction-routes](../10-model/construction-routes.md) 1.0; [mpir](../20-methods/mpir/README.md) (aviso de estado); glosario (MPIR).
- **Relacionado:** D-009, D-046, D-094.

### D-096

**Excepción a D-042: el motor PAA no aplica el robots.txt de Google.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-construction-route` §3, tarea T-039. El robots.txt de Google excluye `/search` para cualquier agente, y sus condiciones de servicio (España, vigentes desde el 30-07-2026) prohíben el acceso automatizado que lo contravenga. El motor de captura aplica robots.txt a todas sus capturas ([D-042](#d-042), [D-046](#d-046)); el motor PAA no lo hace.
- **Decisión:**
  - Es una excepción que decidió el usuario para **investigación y uso interno**, no para ofrecer un servicio. Se limita a las búsquedas del motor PAA en google.es; toda otra captura sigue con las políticas de acceso de D-042.
  - Del principio del motor de captura se mantiene lo demás: Chrome estable con ventana, sin banderas de automatización, con perfil y puerto propios; una sola ventana y una sola sesión; bloqueo de las respuestas de IA como un bloqueador de contenido, sin modificar el navegador ni el JavaScript de la página; ante un desafío (`/sorry/`, CAPTCHA, 403/429) para, sin resolverlo, sin rotar IP ni aplicar parches antidetección.
  - Límites de ejecución, decididos por el usuario el 2026-10-26 y el 2026-10-27: una búsqueda a la vez; 5 s entre búsquedas; sin pausa larga, horario, tope diario ni tope por hora; 8 clics por búsqueda, con parada tras 2 sin nada nuevo; ante un bloqueo, para todo el motor, reintenta a las 6 h y, tras el segundo, queda parado hasta que una persona lo desbloquea.
  - Los límites se endurecen cuando Google bloquee, no antes: primero una pausa larga cada cierto número de búsquedas y, si no basta, una pausa mayor entre búsquedas, con los valores que se observen en ese bloqueo.
  - Riesgo asumido: la IP es la de la conexión desde la que se ejecuta; si Google la marca, también verá CAPTCHAs quien busque desde ella.
- **Interpretación adoptada:** la excepción cubre el robots.txt y la condición de servicio que remite a él. Las reservas de minería de textos y datos de D-042 no se mencionan en el artefacto y no se tratan aquí. Los valores operativos (perfil, puerto, campos del conjunto) viven en el README del motor PAA.
- **Consecuencias:** [construction-routes](../10-model/construction-routes.md) 1.0 (nota de legitimidad); README del motor PAA, `demand-engine/README.md` y `CLAUDE.md` sin la marca «pendiente de registrar».
- **Relacionado:** D-042, D-046, D-094.

### D-097

**Origen «paa» para los requisitos que entran solo por PAA.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-construction-route` §4, tarea T-039 («Etiqueta de origen definida para los requisitos que salgan de PAA»). Los requisitos llevaban origen «referencias», «normativa» o «inferida» ([D-036](#d-036), [D-068](#d-068)).
- **Decisión:**
  - Un requisito que entra en el catálogo solo por PAA (un criterio de elección que cumple C1–C4 y que ninguna referencia recoge) lleva origen **«paa»**, con las preguntas que lo apoyan como fuentes.
  - Si una referencia o una norma lo recoge, conserva su origen; las preguntas PAA se añaden como apoyo.
  - Una cuestión inferida que PAA confirma pasa a origen «paa», con sus preguntas como fuentes.
  - «paa» es un origen de requisitos, no de aportaciones resolutivas.
  - Como con las inferidas, la auditoría puede informar con ellos y sin ellos.
- **Interpretación adoptada:** propuesta de Claude en el artefacto, por encargo de T-039. Razonamiento de Claude, no del artefacto: se nombra por la fuente concreta, como «normativa», y no por una categoría genérica de consultas.
- **Consecuencias:** [construction-routes](../10-model/construction-routes.md) 1.0; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#cuestiones-inferidas) 1.29; glosario (Origen de un requisito… en la entrada PAA). La validación de `bin/model` aún no admite el origen: T-040.
- **Relacionado:** D-036, D-068, D-091, D-094.

### D-098

**La construcción del modelo de demanda pasa a un módulo propio.** · aceptada · 2026-10-27

- **Contexto:** al incorporar `INTAKE 2026-10-27-paa-construction-route` ([D-094](#d-094) a [D-097](#d-097)), [demand-model](../10-model/demand-model.md) llegaba a 274 líneas, por encima del máximo de 250 de `docs/CLAUDE.md`, que manda dividir por subtema.
- **Decisión:** la sección «Sistema de construcción vigente» (vías, cuestiones inferidas, origen de un requisito y recorrido) pasa, sin cambiar su contenido, al módulo nuevo [construction-routes](../10-model/construction-routes.md). Demand-model conserva la sección con un resumen y el enlace, para que sigan valiendo las anclas que la citan; el entrenamiento y la ejecución siguen en demand-model.
- **Consecuencias:** [demand-model](../10-model/demand-model.md#sistema-de-construcción-vigente) 3.0; [construction-routes](../10-model/construction-routes.md) 1.0; enlaces del glosario, [study-class](../10-model/study-class.md) 1.6 (enlace y nota del MPIR aparcado), [choice-criteria](../10-model/choice-criteria.md) 1.1 y [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#cuestiones-inferidas) 1.29 al módulo nuevo; índice de docs/README (4g). Al revisar, product-taxonomy README 1.8 y sources 1.2 dejan de presentar el MPIR como vía activa (D-095).
- **Relacionado:** D-094, D-095, D-096, D-097.

### D-099

**PAA propone requisitos nuevos, también desde preguntas factuales.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-new-requirements`. Palabras del usuario: «PAA tambien ayuda a la creación de nuevos requsisitos no?». Una pregunta factual sobre la oferta, no valorativa, que ningún requisito responde no tenía vía: para las preguntas factuales, [D-094](#d-094) solo preveía confirmar requisitos existentes, y [D-097](#d-097) limitaba el origen «paa» a los criterios de elección. Claude propuso lo que sigue y el usuario respondió: «si».
- **Decisión:**
  - Cuarto uso de PAA: **proponer requisitos nuevos**, por un solo camino: la pregunta está dentro del perímetro y trata de la clase, no de una marca ni de una tienda; ningún requisito del catálogo la responde sin derivar; cumple C1–C4 ([D-091](#d-091)); entra como requisito candidato, con origen «paa» y la pregunta como fuente.
  - Las preguntas valorativas siguen pasando por su criterio de elección.
  - Un requisito que entra solo por PAA lleva origen «paa» tanto si sale de un criterio de elección como de una pregunta factual. El resto de D-097 no cambia.
- **Interpretación adoptada:** C1–C4 se definieron para criterios de elección; aplicadas a una pregunta factual, se leen sobre la propia pregunta, como dice el artefacto (C2 a C4 «sirven igual»). La regla no crea un concepto: el requisito resultante es ordinario y la pregunta es su fuente, no su fundamento.
- **Consecuencias:** enmienda D-094 y D-097. [construction-routes](../10-model/construction-routes.md) 1.1; nueva [OQ-58](open-questions.md) (entrada del candidato en el catálogo y formato de la pregunta como fuente, que el artefacto no fija); [choice-criteria](../10-model/choice-criteria.md) 1.2; glosario (PAA); README del motor PAA. Aplicación en la clasificación de las preguntas: T-040.
- **Relacionado:** D-091, D-094, D-097, OQ-58.

### D-100

**Lectura sobre la oferta de las preguntas PAA de clase.** · aceptada (enmendada por [D-141](#d-141): el perímetro va antes) · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-classification-criteria` §1. En la primera clasificación con un agente (T-040), C2 se aplicó a la pregunta tal como está escrita, y cayeron en C2 cosas muy distintas («¿Qué es una sábana encimera?», «¿Qué significa 144 hilos?», «¿Cómo coser una bajera?», «¿Cada cuánto se cambian las sábanas?»). Claude propuso y el usuario decidió.
- **Decisión:**
  - Antes de aplicar C2 a una pregunta de clase, se relee sobre la oferta: «¿… esta oferta?». Si un hecho que la oferta puede declarar la responde, la pregunta confirma ese requisito o propone un candidato. C2 solo se aplica cuando ningún hecho de la oferta la responde (hábitos, saber doméstico).
  - La confección casera (coser, hacer o arreglar la pieza) queda fuera del perímetro: no hay compra.
  - La misma lectura vale para el perímetro dudoso: «¿Cuáles son las contraindicaciones del bambú?» va dentro, porque responde a las advertencias y a los efectos sobre la piel que declara la oferta; «¿Qué país produce la mejor seda?» también, porque es el origen de la fibra. Las curiosidades («¿Cuál es la seda más cara?») siguen fuera. (Enmendado por [D-141](#d-141): la lectura ya no resuelve el perímetro.)
- **Interpretación adoptada:** es una lectura de C2 ([D-091](#d-091)) para las preguntas factuales de [D-099](#d-099), que ya decía que C2 a C4 «sirven igual» sobre la pregunta; no cambia C2 para los criterios de elección.
- **Consecuencias:** [choice-criteria](../10-model/choice-criteria.md) 1.3; [construction-routes](../10-model/construction-routes.md) 1.2; glosario (Lectura sobre la oferta); reglamento del agente (`demand-engine/classifier/paa.md`, v2).
- **Enmienda ([D-141](#d-141)):** la lectura sobre la oferta ya no resuelve el perímetro. El perímetro va antes y las preguntas sobre otro producto quedan fuera siempre; los dos ejemplos de dentro siguen dentro porque tratan del material del producto de la clase.
- **Relacionado:** D-091, D-099, D-101, D-141.

### D-101

**Confirmaciones y aportaciones de precisión que salen de PAA.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-classification-criteria` §2 y §11. Decisiones del usuario sobre la propuesta de Claude.
- **Decisión:**
  - Una pregunta por el significado de un término («¿La microfibra es plástico?», «¿Qué significa 144 hilos?», «¿Qué significa *full*?») confirma el requisito del atributo y propone aportaciones de precisión para él (la denominación de la fibra según el Reglamento (UE) 1007/2011, la unidad del recuento de hilos, la equivalencia en cm de una denominación de talla). No genera requisitos nuevos.
  - Una pregunta de tienda o de marca que nombra un atributo («¿Dónde comprar sábanas 100 % algodón?») confirma el requisito de ese atributo (quien compra busca y filtra por él: función Descubrir). Sigue sin proponer requisitos ([D-099](#d-099)).
  - El precio sin tienda («¿Cuánto cuesta una sábana de lino?») es una pregunta de clase y confirma `gen/04`.
  - La verificación («¿Cómo saber si es 100 % algodón?») confirma la composición y propone la aportación «certificación del contenido o del origen de la fibra».
- **Consecuencias:** [construction-routes](../10-model/construction-routes.md) 1.2; reglamento del agente. Las aportaciones propuestas entran en el catálogo por el entrenamiento.
- **Relacionado:** D-094, D-099, D-100, D-104.

### D-102

**Basta una pregunta para apoyar un candidato de PAA.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-classification-criteria` §3. En la primera clasificación (informe de T-040, `demand-engine/var/paa/sets/sabanas/report.md`), el agente dudó de un candidato, el tacto, apoyado por una sola pregunta.
- **Decisión:** basta una pregunta para que un candidato que cumple C1–C4 entre como tal. La presencia de una pregunta no se puntúa ([D-094](#d-094)) y D-099 admite la pregunta como fuente. Este apoyo es para que el requisito exista; para separarlo hace falta otra prueba ([D-103](#d-103)).
- **Consecuencias:** [choice-criteria](../10-model/choice-criteria.md) 1.3; reglamento del agente.
- **Relacionado:** D-094, D-099, D-103.

### D-103

**Separación por dimensión en los atributos de lista.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-classification-criteria` §4. `cat.fundas-de-almohada/06` agrupa 11 valores de `special_feature` de Amazon de tres temas. El agente separó las arrugas solo porque les votó otra importancia. Palabras del usuario: «no lo planteo como una regla universal. quiero que entendamos y construyamos un criterio de esta reflexión». De la discusión salió el criterio; el usuario lo aprobó con las dos pruebas.
- **Decisión:**
  - Ámbito: un atributo de lista de una referencia (como `special_feature`), cuyos valores son reclamos que la oferta marca o no. No es una regla universal de formulación.
  - La lista se mantiene agrupada como la plantea la referencia: sus valores son extras, que importan solo si la oferta los reclama.
  - Un valor se separa en requisito propio cuando PAA muestra que es una dimensión de comparación de la clase (algo que quien compra quiere saber de cualquier oferta, la reclame o no), con las dos pruebas: (a) transversal, se pregunta sobre dos o más valores del rasgo que más condiciona las prestaciones (el material o el tejido); (b) comparativa o de elección («¿qué se arruga más?», «¿cuáles se arrugan menos?»).
  - Es un criterio de estructura (cuándo partir), no de existencia ([D-102](#d-102)).
  - Lo que no pertenece al tema de la lista sale de ella aunque la referencia lo incluya (el «dobladillo con doble vuelta» es confección, no resistencia).
- **Consecuencias:** complementa [D-043](#d-043), criterio 2, y [D-060](#d-060), regla 3. [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md); glosario (Separación por dimensión); reglamento del agente. Aplicación en sábanas: [D-108](#d-108).
- **Relacionado:** D-043, D-060, D-102, D-108.

### D-104

**Criterios de elección intermedios; PAA y la pertinencia de los AC, en propuesta.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-classification-criteria` §6. El criterio valorativo «material» reunía 40 preguntas («¿Qué es mejor, lino o algodón?», «beneficios del bambú») y el agente lo dio por cubierto solo con la composición. Palabras del usuario: «Podría ser un requisito. Se me ocurre buen candidato para evaluar los AC. Si es muy comparable, verificable, etc. No sirve para evaluar si existen las funciones informativas para saberlo». Tras el estudio, eligió la síntesis.
- **Decisión:**
  - Un criterio intermedio («material», «calidad») queda cubierto y se descompone en las prestaciones. El «material» lo cubre la composición en cuanto a qué material es (funciones Comprender y Comparar); en cuanto a si es mejor, se descompone en las prestaciones (función Evaluar): nivel térmico, arrugas, duración y resistencia, humedad, tacto y piel. Deducir esas prestaciones del material es lo que [D-090](#d-090) no admite.
  - Una pregunta genérica («¿es bueno el lino?») no nombra ninguna prestación: apoya la composición, no a una prestación concreta, y no cuenta para las pruebas de [D-103](#d-103). Solo apoya una prestación la pregunta que la nombra.
  - **Propuesta, sin decidir:** PAA como prueba de qué criterios de aceptación son pertinentes para un requisito (Comparabilidad, Precisión, Fiabilidad para la composición; Comparabilidad para el precio). Sería un uso nuevo de PAA, no de importancia. (Adoptada por [D-115](#d-115): el entrenamiento de PAA escribe reglas de AC por requisito.)
- **Interpretación adoptada:** el artefacto presenta la pertinencia de los AC como propuesta; se registra como cuestión abierta y no cambia [acceptance-criteria](../10-model/acceptance-criteria.md).
- **Consecuencias:** [choice-criteria](../10-model/choice-criteria.md) 1.3; glosario (Criterio de elección intermedio); nueva [OQ-59](open-questions.md); reglamento del agente.
- **Relacionado:** D-090, D-091, D-094, D-103, OQ-59.

### D-105

**Tacto por tipo y rasgo «sensorial».** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-classification-criteria` §7.
- **Decisión:**
  - El tacto cumple C2 si se pregunta por el tipo de tacto (sedoso o liso, crujiente, afelpado, fresco al tacto); no si se pregunta por el grado de suavidad, que solo admite más o menos.
  - Rasgo nuevo «sensorial» en el vocabulario ([D-056](#d-056)). El entrenamiento reclasifica los requisitos de tacto existentes (`cat.toallas/05` y `cat.mantas/08`, hoy `prestacion`).
- **Interpretación adoptada:** el rasgo lo decide el usuario, no los votos de los agentes que prevé D-056; entra en el vocabulario de partida y el entrenamiento lo aplica.
- **Consecuencias:** [choice-criteria](../10-model/choice-criteria.md) 1.3; [model-training](../10-model/model-training.md) (rasgos); vocabulario `demand-engine/catalog/traits.json` en el entrenamiento.
- **Relacionado:** D-056, D-091, D-108.

### D-106

**Un requisito de certificación cubre la prestación cuya declaración recoge.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-classification-criteria` §8. Claude propuso como regla general que un requisito de certificación no cubre la prestación que certifica; el usuario no la adoptó.
- **Decisión:** si el requisito de certificaciones recoge la declaración de una prestación (por ejemplo, «hipoalergénico»), la cubre. Para la piel en sábanas, el usuario decidió mover esa declaración al requisito de la prestación ([D-108](#d-108)); revisado por [D-113](#d-113): cubierta.
- **Interpretación adoptada:** «la cubre» se lee como C1 ([D-091](#d-091)): ese requisito responde la prestación sin derivar.
- **Consecuencias:** [choice-criteria](../10-model/choice-criteria.md) 1.3.
- **Relacionado:** D-091, D-108.

### D-107

**Requisitos repetidos en bloques hermanos: misma pregunta y misma descripción.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-classification-criteria` §10. El agente propuso subir a `cat.ropa-de-cama` requisitos que no valen para todas sus hijas (doseles, cubrecanapés, almohadas).
- **Decisión:**
  - [D-043](#d-043), criterio 4, tal cual: lo que no vale para todas las hijas no sube a la madre; se repite en las hermanas.
  - Un requisito repetido en bloques hermanos lleva la misma pregunta y la misma descripción. Palabras del usuario: «lo de la descripción que digo quizás es un tema de construcción de presentación. Así que la respuesta correcta es la primera».
- **Interpretación adoptada:** adaptar la descripción a la pieza queda como posible tema de presentación, sin decidir: nueva [OQ-60](open-questions.md).
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md); [requirement-description](../10-model/requirement-description.md) 1.1; reglamento del agente.
- **Relacionado:** D-043, D-092, OQ-60.

### D-108

**Candidatos PAA de la clase de sábanas.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-classification-criteria` §4, §5, §8, §9 y §12. Aplicación de D-100 a D-107 a la clase de sábanas, decidida por el usuario.
- **Decisión:**
  - **Arrugas:** requisito propio (pasan las dos pruebas de [D-103](#d-103)). La duración, el encogimiento y el secado quedan en una lista encabezada por la duración («¿Qué duración y resistencia al uso y al lavado tiene…?»); el dobladillo sale a construcción.
  - **Dimensión térmica:** frescor y abrigo son una sola dimensión con dos polos. `inf/01` se reformula como «¿Qué nivel de abrigo o de frescor ofrece (fresca de verano, para todo el año, cálida de invierno)?» y pasa a origen «paa» ([D-097](#d-097)). La transpiración y la gestión de la humedad y el sudor, lista agrupada (`fundas/05` sin el frescor). El «efecto frío al tacto» va al tacto ([D-105](#d-105)).
  - **Piel** *(revisado por [D-113](#d-113): cubierta por `cat.sabanas/02`; sigue vigente la partición de `fundas/04`)*: candidato en sábanas (rasgo `prestacion`, origen «paa»); la hipoalergenicidad y la aptitud para pieles sensibles pasan de `cat.sabanas/02` a él, que queda en certificaciones y estándares. `cat.fundas-de-almohada/04` se parte por tema: piel y cabello / protección de la almohada.
  - **Tacto:** candidato por tipo de tacto, rasgo «sensorial», origen «paa»: ninguna referencia lo recoge en sábanas ni fundas ([D-105](#d-105)).
  - **Variedad o calidad de la fibra** (algodón Pima o de fibra larga, seda de morera…): se explora como candidato, separada del tratamiento del hilo (peinado, mercerizado), que es construcción.
  - **Origen de la fibra** (país o región de cultivo o producción: lino europeo, algodón egipcio…): candidato propio, de origen «paa», distinto del país de fabricación de `gen/20`. Palabras del usuario: «Es posible que aquí haya requisito nuevo, pero derivado de PAA (porque se pregunta)».
  - **Bloques:** los de sábanas, en `cat.sabanas`; los cambios de fundas, en `cat.fundas-de-almohada` ([D-107](#d-107)).
  - Son candidatos: entran en el catálogo por el entrenamiento, no a mano.
- **Consecuencias:** [choice-criteria](../10-model/choice-criteria.md) 1.3 (ejemplo mínimo); [requirement-description](../10-model/requirement-description.md) 1.1 (ejemplos). La entrada en el catálogo sigue pendiente ([OQ-58](open-questions.md)).
- **Relacionado:** D-090, D-097, D-103, D-105, D-106, D-107, OQ-58.

### D-109

**Precisiones de la separación por dimensión.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-classification-criteria-2` §1, §2 y §3. Con el reglamento PAA v2, el agente separó el secado con una sola pregunta comparativa que nombra dos materiales. En sábanas, donde no hay lista de Amazon, convirtió cada valor preguntado en un candidato suelto. Y con [D-106](#d-106) dio por cubierta la piel. El usuario decidió paso a paso.
- **Decisión:**
  - La prueba (a) exige **preguntas distintas** sobre dos o más materiales o tejidos. Una misma pregunta no cuenta para (a) y (b) a la vez.
  - Si la clase no tiene la lista y un bloque hermano sí, el candidato es **la misma lista**, con la misma pregunta ([D-107](#d-107)) y sin los valores que se separaron. Las preguntas sueltas apoyan esa lista. Si no hay lista en ningún hermano, los valores se agrupan por tema ([D-043](#d-043), criterio 2).
  - La separación por dimensión vale para **cualquier atributo de lista** de una referencia, de Amazon o de Shopify, incluidas las listas de certificaciones. D-106 rige cuando PAA no muestra la dimensión.
  - Sacar un valor de su lista porque no pertenece a su tema no necesita preguntas de apoyo.
- **Consecuencias:** precisa [D-103](#d-103) y acota D-106. *(El ejemplo de la piel queda retirado por [D-113](#d-113): la piel de D-108 no pasa las pruebas, porque «¿Por qué es bueno dormir con funda de seda?» es genérica, D-104.)* [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#separación-por-dimensión); [choice-criteria](../10-model/choice-criteria.md) 1.4; glosario (Separación por dimensión); reglamento PAA v3.
- **Relacionado:** D-043, D-103, D-106, D-107, D-108.

### D-110

**Preguntas de grado: C2 se juzga sobre el requisito.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-classification-criteria-2` §4. El agente no generó el tacto porque la única pregunta («¿Por qué las sábanas de los hoteles son tan suaves?») pregunta por el grado ([D-105](#d-105)); el ejemplo del canon la releía sobre la oferta y generaba.
- **Decisión:**
  - Una pregunta de grado («tan suaves», «las más frescas», «cuál se arruga menos») indica el aspecto. C2 se juzga sobre el requisito, formulado por tipo o por declaración: si la oferta puede declarar el tipo, la pregunta de grado apoya ese requisito.
  - No genera cuando el aspecto solo admite más o menos y ninguna categoría declarable lo resuelve (la marca, C4).
  - D-105 es la aplicación de esta regla al tacto: el tacto genera.
- **Consecuencias:** [choice-criteria](../10-model/choice-criteria.md) 1.4; reglamento PAA v3.
- **Relacionado:** D-091, D-100, D-105.

### D-111

**Sujeción de la bajera, candidato PAA.** · sustituida por [D-112](#d-112) · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-classification-criteria-2` §5. El agente propuso «¿Qué sujeción al colchón ofrece la bajera (se mantiene en su sitio sin salirse ni desplazarse)?», apoyado por «¿Cómo hacer para que no se salga la sábana de abajo?» y «¿Qué sábanas no se salen?». El ejemplo de [choice-criteria](../10-model/choice-criteria.md#ejemplo-mínimo) lo daba por cubierto con `inf/02` y `cat.sabanas-ajustables/01`.
- **Decisión:** genera candidato (rasgo `prestacion`, en `cat.sabanas-ajustables`; origen «paa» por [D-097](#d-097)). De cómo se ajusta la bajera y hasta qué altura llega solo se deduciría que no se sale ([D-090](#d-090)); la resuelve la declaración de sujeción o un ensayo del elástico.
- **Consecuencias:** sustituye la fila «Ajuste de la bajera» del ejemplo mínimo de choice-criteria (1.4); añade un candidato a [D-108](#d-108).
- **Relacionado:** D-090, D-108.

### D-112

**Sujeción de la bajera: cubierta.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-bottom-sheet-hold`. Con el reglamento PAA v3, el agente volvió a darla por cubierta. El usuario repasó la cuestión desde el principio. Solo dos preguntas piden la prestación: «¿Qué sábanas no se salen?» y «¿Cómo hacer para que no se salga la sábana de abajo?».
- **Decisión:** cubierto, sin candidato.
  - Saber cómo se ajusta la bajera (`inf/02`) y hasta qué altura de colchón llega (`cat.sabanas-ajustables/01`) basta.
  - Que se salga depende sobre todo de que el bolsillo encaje con el colchón de quien compra. Eso lo resuelve `cat.sabanas-ajustables/01`; lo que queda depende del comprador (C3).
- **Consecuencias:** sustituye [D-111](#d-111). Vuelve la fila «Ajuste de la bajera» del ejemplo mínimo de [choice-criteria](../10-model/choice-criteria.md#ejemplo-mínimo) (1.5).
- **Relacionado:** D-090, D-108, D-111.

### D-113

**Piel en sábanas: cubierta.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-skin-covered`. Con el reglamento PAA v3, el agente dio la piel en sábanas por cubierta con `cat.sabanas/02` ([D-106](#d-106)). Con las reglas vigentes, no pasa la separación por dimensión ([D-109](#d-109)): solo «¿Qué hace el bambú en la piel?» nombra la piel, y «¿Por qué es bueno dormir con funda de seda?» es genérica ([D-104](#d-104)). Claude reconoció que su argumento anterior la contaba como prueba (b) en contra de D-104.
- **Decisión:** cubierto.
  - La piel en sábanas la cubre `cat.sabanas/02`.
  - [D-108](#d-108) retira el candidato de piel en sábanas y el traslado de la hipoalergenicidad.
  - D-109 deja de presentar la piel como ejemplo.
  - La partición de `cat.fundas-de-almohada/04` por tema sigue vigente.
- **Consecuencias:** revisa D-108 (piel) y D-109 (ejemplo). El reglamento PAA v3 ya lo aplica así.
- **Relacionado:** D-104, D-106, D-108, D-109.

### D-114

**Entrenamiento propio de PAA: qué refina, sus límites y el piloto de medición.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-training` (T-042). La regla de semillas y las reglas de lectura de las preguntas ([D-100](#d-100) a [D-113](#d-113)) salen de una sola clase, sábanas. El usuario quiere que PAA se refine con datos de otras clases.
- **Decisión:**
  - PAA tiene un entrenamiento propio, independiente del de taxo ([model-training](../10-model/model-training.md)), con pasadas solo de PAA, «para que se autorefine en reglas, criterios, definición de semillas» (palabras del usuario).
  - Refina solo tres cosas: la estrategia de semillas, el vocabulario de criterios de elección (como el de rasgos, [D-056](#d-056)) y la calibración de reglas.
  - Calibrar una regla es ajustar sus parámetros dentro de las reglas vigentes (p. ej., cuántas preguntas o materiales exige la prueba (a) de [D-103](#d-103)), validado contra los casos de control de PAA y con informe.
  - Crear o retirar reglas sigue siendo decisión del usuario. Nada se acepta si empeora una métrica frente al control. El número de candidatos no es objetivo.
  - Empieza por un piloto de medición con 3-4 clases muy distintas, de las ya ejecutadas, sin inducción: mide qué varía entre clases (semillas, clics, criterios y dudas). Cada conjunto se clasifica una vez, sin doble pasada de estabilidad, con la versión del catálogo anotada. Lo esperado de los casos de control de PAA lo decide el usuario, con sábanas entre ellos. (Enmendada por [D-116](#d-116): las clases del piloto son las de los 14 casos de referencia.)
  - Riesgos: el volumen de búsquedas en Google (primer bloqueo probable, [D-096](#d-096)), el sobreajuste a sábanas y la dependencia de la versión del catálogo. Coste orientativo por clase: ~10 búsquedas (~5 min) y 0,7-1,3 M tokens, casi todo caché.
- **Interpretación adoptada:**
  - Los límites los propuso Claude «a confirmar en el intake»; el update los da por confirmados y se incorporan como vigentes.
  - La nota de la tarea compara el número de candidatos con D-076, que trata de las opiniones publicadas. El paralelo es [D-059](#d-059) («críticos pocos» no es un objetivo); se enlaza esa.
  - Las métricas del entrenamiento de PAA no están definidas: se abre [OQ-64](open-questions.md).
- **Consecuencias:** nuevo módulo [paa-training](../10-model/paa-training.md) 1.0; [construction-routes](../10-model/construction-routes.md) 1.3; [model-training](../10-model/model-training.md) 1.17 (enlace); glosario (Entrenamiento de PAA); nueva OQ-64. El piloto es T-042.
- **Relacionado:** D-056, D-059, D-094, D-096, D-100–D-113, D-115.

### D-115

**El entrenamiento de PAA escribe en el catálogo: cuatro papeles y un solo escritor por requisito.** · aceptada (papel 2 precisado por [D-125](#d-125): las «reglas de AC» son las pistas de valoración) · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-training` (segunda nota de T-042, que sustituye a la primera en esto). La propuesta inicial era que PAA no escribiera el catálogo, para mantener un solo escritor. El usuario lo corrigió: PAA ha de «aportar nuevos requisitos, aportar reglas para AC de un requisito constituido y confirmar requisitos inferidos. […] Si es así no habría conflicto».
- **Decisión:** el entrenamiento de PAA modifica el catálogo con cuatro papeles, todos aditivos o sobre lo que es de PAA:
  1. requisitos nuevos, con id propio y origen «paa» ([D-097](#d-097), [D-099](#d-099));
  2. reglas de AC por requisito, un artefacto nuevo;
  3. confirmar o revisar las cuestiones inferidas ([D-094](#d-094)), p. ej. `inf/01` con los dos polos ([D-108](#d-108));
  4. aportaciones aditivas de precisión y de sustento a requisitos existentes ([D-101](#d-101)).

  Las revisiones estructurales de requisitos que nacen de las referencias (separar, sacar, partir) entran a la compilación de taxo: PAA deja un registro que lee el próximo entrenamiento de taxo, que las reevalúa al compilar. Un solo escritor por requisito.
- **Interpretación adoptada:**
  - «Reglas para AC» se lee como reglas de pertinencia de los criterios de aceptación de un requisito, el uso que proponía D-104 ([acceptance-criteria](../10-model/acceptance-criteria.md), reglas 5 y 6). No puntúan, no ponderan ni fijan umbrales: no cambian el GSC ni las invariantes 4 y 7. Su contenido y formato quedan en [OQ-61](open-questions.md).
  - «Requisito constituido» es uno que ya está en el catálogo, de cualquier origen.
  - Los requisitos de origen «normativa» siguen la regla de los de «referencias»: los escribe taxo.
  - El artefacto no dice por cuál de los dos entrenamientos entran los candidatos ya decididos de sábanas ([D-108](#d-108)). Como son requisitos «paa» (papel 1), entran por el de PAA.
  - Cierra el fondo de [OQ-58](open-questions.md) (quién escribe lo que propone PAA: su entrenamiento) y de [OQ-59](open-questions.md) (PAA sí prueba la pertinencia de los AC). Lo que dejaban sin resolver pasa a OQ-61, [OQ-62](open-questions.md) (paso de aceptación, estado y formato de la fuente) y [OQ-63](open-questions.md) (formato del registro).
- **Consecuencias:** cierra OQ-58 y OQ-59; nuevas OQ-61 a OQ-63. [paa-training](../10-model/paa-training.md) 1.0; [construction-routes](../10-model/construction-routes.md) 1.3; [choice-criteria](../10-model/choice-criteria.md) 1.6 (pendiente); glosario (Reglas de AC de un requisito; Registro de revisiones de PAA). [choice-criteria](../10-model/choice-criteria.md) recoge la entrada de los candidatos de sábanas.
- **Relacionado:** D-094, D-097, D-099, D-101, D-103, D-104, D-108, D-114, OQ-58, OQ-59.

### D-116

**Clases del piloto de PAA: las de los 14 casos de referencia.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-paa-pilot-classes` (T-042). [D-114](#d-114) fijaba un piloto con 3-4 clases muy distintas, de las ya ejecutadas. Claude propuso botas, comida para perros y sofás cama, con juguetes para perros como cuarta.
- **Decisión:** «usaremos los 14 casos de referencia» (palabras del usuario). El piloto de medición del entrenamiento de PAA se hace con las clases de los 14 casos del conjunto de control del entrenamiento del modelo de demanda ([D-045](#d-045)).
- **Interpretación adoptada:**
  - Un conjunto de semillas por clase distinta, no por caso, porque las semillas salen de la clave del modelo. Los dos juegos de funda nórdica comparten clave, y la manta y el plaid también: son 12 clases, sábanas incluida.
  - El artefacto no dice si los casos de control de PAA cubren las 12 clases o un subconjunto: se mantiene lo de D-114 (lo esperado lo decide el usuario, con sábanas entre ellos).
  - El resto de D-114 no cambia. El volumen sube a unas 120 búsquedas (12 × ~10, estimación) y el riesgo de bloqueo con él.
- **Consecuencias:** enmienda D-114. [paa-training](../10-model/paa-training.md) 1.1; glosario (Entrenamiento de PAA).
- **Relacionado:** D-045, D-096, D-114.

### D-117

**Los criterios de aceptación se aplican siempre; NE es una incidencia.** · aceptada (la excepción pendiente, el NA de Comparabilidad, la decide [D-126](#d-126)) · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-ac-applicability-and-reliability` §1. El usuario dudaba de que un criterio pudiera ser NA o NE: «Los criterios siempre se evalúan y aplican. Confirmémoslo.» Tras el análisis de Claude (solo Comparabilidad podía ser NA; solo Fiabilidad tenía NE estructural): «No hay NA, NE es una incidencia. NA de comparabilidad aún no podemos decidir (depende de esta sesión).»
- **Decisión:**
  - Con disponibilidad efectiva 1, los seis criterios se aplican y se valoran siempre. No hay NA de criterio.
  - Excepción pendiente: el NA de Comparabilidad, que se decide con las reglas de AC por requisito ([OQ-65](open-questions.md)).
  - **NE es una incidencia de la auditoría** en cualquiera de los seis criterios: queda fuera de la escala (NE ≠ 0) y se registra qué comprobación falló. Deja de absorber el caso «nada confirma ni refuta el dato» en Fiabilidad ([D-121](#d-121)).
  - El NA del requisito se mantiene.
- **Interpretación adoptada:**
  - Enmienda BASE §6.1 y FUND §8.1 en cuanto al criterio «no aplicable» y a la situación «no evaluable», y el ejemplo de FUND §10.1. En ese ejemplo, la Comparabilidad NA se conserva mientras OQ-65 siga abierta; la Fiabilidad NE se sustituye.
  - «Incidencia» se lee como la imposibilidad de hacer una comprobación (un recurso que no se pudo inspeccionar, un registro externo que no respondió), paralela a la comprobación inconclusa de la disponibilidad (analogía de Claude en el análisis previo). No es falta de evidencia sobre lo publicado: esa se resuelve con el grado.
  - El NA del requisito (un requisito condicionado que no se activa, o un RI que no corresponde a un ámbito, FUND §3.5) es otro estado. Claude lo dio por mantenido y el usuario no lo objetó.
- **Consecuencias:** [scoring-systems](../10-model/scoring-systems.md#grado-de-satisfacción-de-criterio-gsc) 1.2; [acceptance-criteria](../10-model/acceptance-criteria.md) 1.2; gsc-decision 0.2, ac-guides 0.2, calibration, evidence, qa, execution, inputs-outputs, availability-coverage, dossier y README (auditoría); paa-training (nota sobre las reglas de AC); glosario (NA, NE, Árbol de decisión GSC); `CLAUDE.md` raíz (invariante 4); OQ-21 anotada; nueva OQ-65.
- **Relacionado:** D-006, D-118, D-121, OQ-21, OQ-65.

### D-118

**Comparabilidad: el contraste se exige cuando la respuesta es una dimensión de comparación de la clase.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-ac-applicability-and-reliability` §1. Problema planteado por Claude: un RI que trata de una sola oferta, ¿requiere contraste? Usuario: «es como propones».
- **Decisión:** el contraste se exige cuando la respuesta es una **dimensión por la que se comparan las ofertas de la clase** (gramaje, composición, precio…). Entonces Comparabilidad evalúa si se expresa sobre bases contrastables (unidad, denominación normalizada, escala oficial), aunque el RI trate de una sola oferta. Las preguntas comparativas de PAA son evidencia de que una dimensión es de comparación ([D-104](#d-104)).
- **Interpretación adoptada:** precisa la regla 6 de los criterios de aceptación («se evalúa cuando la cuestión requiere contraste»): no hace falta que el RI pida comparar varias ofertas. Qué corresponde cuando la respuesta no es una dimensión de comparación queda en [OQ-65](open-questions.md).
- **Consecuencias:** [acceptance-criteria](../10-model/acceptance-criteria.md#reglas-e-invariantes) 1.2 (regla 6); ac-guides (Comparabilidad); glosario (Comparabilidad).
- **Relacionado:** D-104, D-117, OQ-65.

### D-119

**La prestación derivada de un atributo se decide en la pertinencia.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-ac-applicability-and-reliability` §2. Claude planteó dos sitios para lo que dictamina [D-090](#d-090): la pertinencia (A) o la valoración de los AC (B), con sus consecuencias. Usuario: «A. El recomendado.»
- **Decisión:**
  - Un atributo (tejido, material, composición) **por sí solo** no es información pertinente para un requisito sobre una prestación: solo aporta una tendencia, no un vínculo fundado. Sin nada más, la disponibilidad efectiva es 0, el IR es 0 y no se valoran los AC. La recomendación es declarar la prestación.
  - Si la ficha declara la prestación («percal, fresca para verano»), el atributo puede acompañarla como contexto.
  - Lo dictamina la **pertinencia** en la auditoría, no la valoración de los AC. Sigue en pie que no lo dictamina el modelo de demanda y que el requisito de la prestación tiene que existir en el modelo.
- **Interpretación adoptada:**
  - Enmienda D-090. Sus palabras originales («eso ya es tarea de la valoración de criterios de aceptación») se leen, como dice el artefacto, «es tarea de la auditoría, no del modelo de demanda».
  - Lo pertinente pero insuficiente es el mismo hecho con menos detalle o con otro alcance; lo no pertinente es otro hecho que solo se correlaciona. Es lo que el canon ya hacía con «producto muy vendido» frente a la disponibilidad (PF-07, GSC0 §6.5) y encaja con la regla 6 de la información resolutiva, con CT-08 y con la invariante 10.
  - Cuándo una derivación desde otro hecho es admisible lo fija [D-120](#d-120).
- **Consecuencias:** enmienda D-090; [effective-availability](../10-model/effective-availability.md#pertinencia-de-lo-derivado) 1.1; [acceptance-criteria](../10-model/acceptance-criteria.md#interpretación) 1.2; [choice-criteria](../10-model/choice-criteria.md#prestación-derivada-de-un-atributo) 1.7; relevance (PF-03); glosario (Prestación derivada de un atributo).
- **Relacionado:** D-090, D-120, OQ-56.

### D-120

**Prueba de derivación: conclusión necesaria con reglas generales, descriptivas y citadas.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-ac-applicability-and-reliability` §3. Claude propuso como frontera de [OQ-56](open-questions.md) «¿podría ser falsa la conclusión aunque todo lo publicado sea verdad?». Al repasarla con casos, propuso precisarla y descartar una condición previa («interpreta o combina, no aporta»). Usuario: «sí».
- **Decisión:**
  > Una derivación se admite si su conclusión **no puede ser falsa cuando lo publicado es verdad**, aplicando reglas:
  > - **generales:** valen para cualquier oferta (definiciones, lógica, aritmética, hechos generales del mundo). Un hecho particular del producto tomado de fuera (un registro, la web del fabricante, lo que el auditor sepa del modelo) no es una regla y solo sirve para contrastar.
  > - **descriptivas:** dicen qué son las cosas. Una norma solo cuenta para fijar el significado de un término («seda», qué exige GOTS), no para dar por hecho que la oferta cumple lo que obliga: la ley dice lo que debe ser, no lo que la oferta es.
  > - **citadas con su fuente y sin contrafuente:** si una fuente admisible o la realidad documentada del mercado la contradice, la regla no es necesaria.
  >
  > Si la información trata la misma cuestión, aunque sea con menos detalle, en general o con otro alcance, no hay derivación: es pertinente y la juzgan los AC.
- **Interpretación adoptada:**
  - Sirve a tres usos: la pertinencia ([D-119](#d-119)), las derivaciones de los AC (regla 7, Concreción) y la refutación por conocimiento del dominio en Fiabilidad ([D-122](#d-122)), que usa solo la parte de necesidad.
  - No cuenta pasos ni es una escala de grado de derivación: respeta la regla 7, la invariante 9 y [D-006](#d-006).
  - «Hecho particular tomado de fuera» concreta CT-08 y GSC0 §2.3: las referencias externas contrastan, no completan.
  - La condición descartada excluía un «no» fundado sobre otra cuestión («100 % lana» → «¿apto para veganos?» → «no»), contra la invariante 13, y obligaba a juzgar si la publicación «trata» la cuestión, que es un juicio de proximidad temática (invariante 10).
- **Consecuencias:** cierra OQ-56; [effective-availability](../10-model/effective-availability.md#pertinencia-de-lo-derivado) 1.1; [acceptance-criteria](../10-model/acceptance-criteria.md#reglas-e-invariantes) 1.2 (regla 7); [choice-criteria](../10-model/choice-criteria.md) 1.7 (pendiente); relevance (PF-03); calibration (matriz); glosario (Prueba de derivación); `CLAUDE.md` raíz (invariante 9).
- **Relacionado:** D-006, D-090, D-119, D-122, OQ-56.

### D-121

**Fiabilidad: nueva definición y lectura refutadora.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-ac-applicability-and-reliability` §4. Usuario: «Para la propiedad de corrección: hay que establecer cómo se evalúa (conocimiento del modelo, estructura del dato, hay que profundizar). Actualidad (quita esta propiedad, no hay forma de evaluarla).» Claude planteó una lectura refutadora (G1) y una corroboradora (G2). Usuario: «1. sí, G1. 2. sí. 3. elige tú. 4. sí. 5. sí.», respuesta numerada a las cinco propuestas de Claude en la sesión (1, lectura de Fiabilidad; 2, límites del conocimiento del dominio; 3, identificador ausente; 4, definición; 5, forma de la consistencia transversal). El artefacto cita la respuesta sin esa correspondencia, que se registra aquí.
- **Decisión:**
  - Definición de Fiabilidad, que sustituye a la de BASE §5.2: «La información supera las comprobaciones de corrección y consistencia proporcionadas a su naturaleza: no se acreditan errores ni contradicciones materiales.»
  - Lectura refutadora: **2**, supera las comprobaciones que tocan a ese tipo de dato; **1**, hay un defecto no material, o uno que afecta solo a parte de lo examinado; **0**, hay un defecto material.
  - El registro enumera las comprobaciones hechas y el resultado dice «sin defectos detectados en…», nunca «exacto».
  - Un dato que nada refuta ni confirma recibe el grado que corresponda a las comprobaciones superadas, no NE ([D-117](#d-117)).
- **Interpretación adoptada:**
  - Compatible con [D-006](#d-006) («no inferir verdad de la ausencia de contradicciones») y con la invariante 12: el 2 afirma que se superaron las comprobaciones, no que el dato sea verdadero.
  - Se descartó la lectura corroboradora porque trataba la ausencia de corroboración como limitación (invariante 12), funcionaba como un tope (invariante 7) y castigaba al ecommerce por que no exista registro para un tipo de dato. Consecuencia asumida: Fiabilidad discrimina cuando hay defectos; la mayoría de los datos estables sin defectos obtendrán 2.
  - La lectura es canon; los anclajes de la guía de la auditoría la desarrollan (propuesta V1).
- **Consecuencias:** [acceptance-criteria](../10-model/acceptance-criteria.md#fiabilidad-lectura-refutadora-y-comprobaciones) 1.2; ac-guides 0.2; gsc-decision 0.2; calibration (casos A y J); qa; glosario (Fiabilidad); OQ-25 cerrada.
- **Relacionado:** D-006, D-117, D-122, D-123.

### D-122

**Comprobaciones de corrección: tres familias, límites del conocimiento del dominio e identificador ausente.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-ac-applicability-and-reliability` §4. Usuario: «conocimiento del modelo, estructura del dato, hay que profundizar». Sobre las propuestas de Claude: «2. sí» (límites del conocimiento del dominio) y «3. elige tú» (identificador ausente); la correspondencia de la numeración está en [D-121](#d-121).
- **Decisión:**
  - Tres familias de comprobación: **estructura del dato** (las reglas que el dato lleva consigo; refuta con certeza), **conocimiento del dominio** (reglas generales; solo refuta) y **fuente independiente** (hechos particulares en registros públicos; refuta o corrobora, solo en algunos tipos de dato).
  - Límites del conocimiento del dominio: solo refuta; un dato es defecto solo si **no puede** ser verdad según una regla general y descriptiva, citada con su fuente y sin contrafuente (la parte de necesidad de [D-120](#d-120)); si solo es improbable, es una sospecha, que se anota y no gradúa; regla citada con su fuente (M10).
  - Cuando existe una fuente independiente para un tipo de dato (certificaciones, clase energética, GTIN), consultarla forma parte de las comprobaciones que le tocan.
  - **Identificador ausente:** si el ecommerce no da el identificador que permitiría la comprobación externa (p. ej., el número de certificado), cuenta en Justificación (P18), no en Fiabilidad.
  - Frontera con la evaluación técnica: una sintaxis inválida es técnica; una sintaxis válida con un valor imposible es Fiabilidad.
  - **Consistencia por ámbito:** dentro de las representaciones de cada ámbito, y cuenta en su GSC de Fiabilidad.
- **Interpretación adoptada:**
  - «Conocimiento del modelo» se lee, como dice el artefacto, como el del modelo de IA que audita.
  - El identificador ausente lo decidió Claude por delegación del usuario: con la lectura refutadora, Fiabilidad gradúa los defectos que encuentran las comprobaciones, y la falta del identificador no es un error de corrección, sino la falta de una base para verificar. Así no se cuenta dos veces (EV-13).
  - Las reglas generales son el conocimiento del dominio y los hechos particulares, la fuente independiente: la misma distinción que separa derivación de contraste en D-120.
  - Qué comprobaciones tocan a cada tipo de dato y qué reglas del dominio guarda el modelo de demanda quedan en [OQ-66](open-questions.md).
- **Consecuencias:** [acceptance-criteria](../10-model/acceptance-criteria.md#fiabilidad-lectura-refutadora-y-comprobaciones) 1.2; [quality-properties](../10-model/quality-properties.md#asociaciones-orientativas-con-los-criterios) 1.3; ac-guides 0.2; property-checks 0.2 (P14, P18 y tabla de relaciones); evidence 0.2 (EV-14, tabla por tipo, alcance de las referencias externas); nueva OQ-66.
- **Relacionado:** D-120, D-121, D-123, OQ-66.

### D-123

**Se retira la propiedad P15 · Actualidad.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-ac-applicability-and-reliability` §5. Usuario: «Actualidad (quita esta propiedad, no hay forma de evaluarla)».
- **Decisión:**
  - P15 · Actualidad se retira del catálogo de propiedades. El ID no se reutiliza, como los retirados en [D-007](#d-007).
  - Fiabilidad ya no juzga la actualidad ([D-121](#d-121)). Sus asociaciones orientativas son P14 y P16; P18 sale de Fiabilidad y queda en Justificación ([D-122](#d-122)).
- **Interpretación adoptada:**
  - Lo detectable sigue cubierto por otras vías: una fecha de validez vencida en la captura (estructura del dato), un feed desfasado frente a la web (consistencia transversal, [D-124](#d-124)) y «Agotado» visible con `InStock` en el marcado (consistencia dentro de Web). Lo que se pierde es juzgar si un dato sin fecha está al día, que ya no era evaluable (EV-10).
  - Enmienda BASE §5.3 y FUND §7 en el catálogo de propiedades. La regla EV-10 de la auditoría se reformula en ese sentido.
- **Consecuencias:** [quality-properties](../10-model/quality-properties.md) 1.3; [commercial-information](../10-model/commercial-information.md#dos-dimensiones-de-evaluación) 1.1 (nota sobre la vigencia de CTX §3); [acceptance-criteria](../10-model/acceptance-criteria.md#distinciones) 1.2; property-checks 0.2; evidence 0.2 (EV-10, EV-14 y tabla por tipo); ac-guides 0.2; glosario (Propiedades de calidad, P14–P18); `CLAUDE.md` raíz (invariante 5); OQ-25 cerrada.
- **Relacionado:** D-007, D-121, D-122, D-124.

### D-124

**Consistencia transversal: nueva dimensión de análisis por RI × par de ámbitos.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-ac-applicability-and-reliability` §6. Usuario: la consistencia «se puede evaluar para cada ámbito y a nivel transversal adquiere una nueva dimensión de análisis». Claude planteó dos formas (T1, hallazgos sin escala; T2, estado cualitativo por RI). Usuario: «sí» a T1.
- **Decisión:**
  - **Unidad:** RI × par de ámbitos, distinta de la valoración RI × ámbito.
  - **Forma: hallazgos sin escala.** Por RI y par de ámbitos: hecho, valores, momento, materialidad, y si la diferencia es legítima (p. ej., un precio propio de un canal, declarado). Una diferencia legítima y declarada no es incoherencia.
  - **No modifica el GSC de ningún ámbito ni se agrega.**
  - **Pares:** Catálogos distribuidos ↔ Web; Catálogos distribuidos ↔ Web Schema.org; HTML ↔ Web Schema.org; entre perfiles de Catálogos distribuidos.
  - **Condiciones de operación:** captura de los ámbitos en un momento comparable; identidad de la entidad entre ámbitos; acceso al feed.
  - Un estado cualitativo por RI (T2) queda para más adelante.
- **Interpretación adoptada:**
  - Es una dimensión de análisis, no un indicador ni una escala. No altera las invariantes 1 y 2: la valoración sigue siendo RI × ámbito y Web y Web Schema.org no se agregan.
  - Es coherente con el caso H (FUND §10.4): el contraste entre HTML y marcado sigue siendo evidencia de la coherencia de Web y no completa Web Schema.org; además se registra como hallazgo transversal (el mismo hallazgo, reutilizado, EV-13).
  - Su canon va con la complementariedad y coherencia entre representaciones, en el módulo de los ámbitos.
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#consistencia-transversal) 1.1; [scoring-systems](../10-model/scoring-systems.md#lectura-integrada-sin-confundir-unidades) 1.2; calibration (caso H, matriz); glosario (Consistencia transversal); `CLAUDE.md` raíz (invariante 2); nueva OQ-67.
- **Relacionado:** D-010, D-122, D-123, OQ-67.

### D-125

**Pistas de valoración: nombre, tres niveles y alcance.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-assessment-hints` §1–2, continuación de [D-117](#d-117) a [D-124](#d-124). El encargo era «un marco general y luego cada requisito fija algún matiz para orientar la evaluación». Claude probó la hipótesis de tres niveles con nueve requisitos del catálogo que aplican a unas sábanas. Usuario: «todo es OK» y «a esto le vamos a llamar "pistas de valoración"».
- **Decisión:**
  - Las **pistas de valoración** son lo que cada requisito fija para orientar la valoración de sus criterios de aceptación. Sustituyen a las «reglas de AC de un requisito» de [D-115](#d-115).
  - **Tres niveles:** marco general para todos los AC; tipo de requisito (rasgo × entidad) para Aplicabilidad y Fiabilidad; requisito para Precisión y Comparabilidad. Concreción y Justificación no necesitan pistas nuevas.
  - **Alcance:** las pistas dicen qué mirar, no cuánto pesa cada criterio; el peso es de la síntesis del IR (OQ-28).
- **Interpretación adoptada:**
  - Precisa el papel 2 de D-115: su lectura «reglas de pertinencia de los AC» queda sustituida. Con los seis criterios aplicados siempre (D-117), la pertinencia se reduce a la marca de dimensión de comparación ([D-126](#d-126)).
  - La consistencia entre requisitos del mismo ámbito que mostró la prueba es consistencia por ámbito (P16, [D-122](#d-122)) y sale del tipo; no es un concepto nuevo.
  - Canon en un módulo nuevo, porque el concepto sirve al modelo de demanda (lo escribe el entrenamiento) y a la auditoría (orienta los AC).
- **Consecuencias:** nuevo módulo [assessment-hints](../10-model/assessment-hints.md) 1.0; [acceptance-criteria](../10-model/acceptance-criteria.md) 1.3; [paa-training](../10-model/paa-training.md) 1.3; [construction-routes](../10-model/construction-routes.md) y [choice-criteria](../10-model/choice-criteria.md) (pendientes); [demand-model](../10-model/demand-model.md) 3.1 y [model-training](../10-model/model-training.md) 1.18 (enlaces); glosario (Pistas de valoración, que sustituye a Reglas de AC de un requisito); índice; OQ-61 cerrada; nueva OQ-68.
- **Relacionado:** D-104, D-115, D-117, D-122, D-126, D-127, D-128, OQ-28, OQ-61, OQ-68.

### D-126

**Marca de dimensión de comparación y NA de Comparabilidad.** · aceptada (cómo se fija: [D-139](#d-139)) · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-assessment-hints` §3; [OQ-65](open-questions.md). Usuario: «sí» a «marcamos "no se compara" en los requisitos que no se usan para comparar».
- **Decisión:**
  - El requisito lleva una **marca de dimensión de comparación** (sí / no) en el modelo de demanda. Si no lo es, **Comparabilidad es NA** en ese requisito. Lo decide el modelo, no el auditor.
  - Ejemplos que no son dimensiones de comparación: tamaño de cama (un filtro), variantes disponibles, garantía legal (la misma para todos), identificadores (emparejan ofertas, no las comparan).
- **Interpretación adoptada:**
  - Cierra la excepción que [D-117](#d-117) dejaba pendiente: es la única excepción a la aplicación de los seis criterios. Precisa [D-118](#d-118): la marca registra si la respuesta es una dimensión de comparación de la clase.
  - Motivo, del artefacto: valorar Comparabilidad en esos requisitos daría un 2 automático o repetiría lo que ya mira Precisión.
  - Cómo se fija la marca (valor por defecto y qué prueba la establece) queda en [OQ-69](open-questions.md).
- **Consecuencias:** cierra OQ-65; [assessment-hints](../10-model/assessment-hints.md) 1.0; [acceptance-criteria](../10-model/acceptance-criteria.md) 1.3; [scoring-systems](../10-model/scoring-systems.md) 1.3; gsc-decision, ac-guides, calibration, qa y execution (auditoría); glosario (NA, Comparabilidad, Marca de dimensión de comparación); `CLAUDE.md` raíz (invariante 4); nueva OQ-69.
- **Relacionado:** D-104, D-117, D-118, D-125, OQ-65, OQ-69.

### D-127

**Quién escribe las pistas de valoración.** · aceptada (la «tabla por tipo» es parte del catálogo de pistas de [D-134](#d-134)) · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-assessment-hints` §4: «sí» a «taxo y PAA escriben las pistas». Antes, en `INTAKE 2026-10-27-ac-applicability-and-reliability` §7: «los matices de AC por requisito no solo dependen de PAA. Taxo también puede calibrarlos».
- **Decisión:**
  - **Pistas por tipo:** una tabla de reglas por rasgo × entidad, como la de importancia, que compila el entrenamiento.
  - **Pistas por requisito:** las escriben taxo (desde las referencias, la normativa que es fuente del requisito y la justificación del requisito) y PAA (desde sus preguntas).
  - Cada pista lleva su **origen**. Las pistas **se suman y nunca se quitan**.
- **Interpretación adoptada:** no choca con «un solo escritor por requisito» ([D-115](#d-115)): esa regla protege la estructura del requisito (separar, partir, sacar). La información resolutiva ya admite aportaciones de varios orígenes y PAA ya añade aportaciones aditivas (papel 4).
- **Consecuencias:** [assessment-hints](../10-model/assessment-hints.md) 1.0; [paa-training](../10-model/paa-training.md) 1.3; OQ-61 cerrada (escritores); OQ-66 anotada (la tabla por tipo).
- **Relacionado:** D-055, D-101, D-115, D-125, OQ-61, OQ-66.

### D-128

**Las pistas de valoración son criterios breves apoyados en las propiedades, no listas.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-assessment-hints` §5–6. Usuario: «aunque sean matices por requisito debemos intentar siempre trabajar con reglas y/o criterios, no deben ser comparaciones deterministas. Esto no sería una práctica correcta: "una lista de vocabulario admitido"»; «lo único es evitar ser demasiado verboso. Las pistas deben ser breves pero suficientemente claras»; «¿Estás teniendo en cuenta que para valorar los AC lo que se estudia son las propiedades de calidad, verdad?» y «sí» a que cada pista nombre la propiedad y los AC.
- **Decisión:**
  - Una pista es un criterio que el auditor aplica razonando, no una lista contra la que se compara palabra por palabra. Es breve pero suficientemente clara y dice su porqué.
  - Los ejemplos solo ilustran, nunca cierran. Las fuentes justifican la pista, no son lo que se busca; si una norma fija una lista cerrada, la pista es «usa la denominación legal» y la norma se cita como fuente.
  - El entrenamiento rechaza las pistas que sean una lista o una frase exacta y las reformula como criterio.
  - Las comprobaciones de estructura del dato son cálculos exactos, pero son reglas generales: encajan.
  - Cada pista dice qué propiedad hay que observar y a qué AC afecta; una pista puede servir a varios AC; las pistas nunca puntúan propiedades.
- **Interpretación adoptada:** coherente con [D-006](#d-006) (no se adopta una equivalencia entre pertinencia y coincidencia literal) y con la invariante 5 (las propiedades no reciben puntuación).
- **Consecuencias:** [assessment-hints](../10-model/assessment-hints.md) 1.0; glosario (Pistas de valoración).
- **Relacionado:** D-006, D-125, D-127.

### D-129

**web-audit: sistema de la evaluación técnica de Web y Web Schema.org.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-web-schema-technical-framework` §1, tarea T-044. El usuario pidió crear «un nuevo sistema web-audit» con «una skill de creación y mantenimiento de documentación de referencia con los criterios de evaluación» y, más adelante, «el sistema de auditado». En la sesión de planificación, Claude recomendó que fuera solo técnico. Usuario: «solo técnico».
- **Decisión:**
  - **web-audit** es el sistema de la evaluación técnica de los ámbitos Web y Web Schema.org (unidad: requisito técnico × ámbito). Empieza por Web Schema.org.
  - No hace la evaluación informativa (disponibilidad efectiva, AC, GSC); la auditoría GSC es otro sistema. Esa auditoría puede consultar la referencia técnica para interpretar el marcado, sin que los requisitos técnicos se conviertan en criterios informativos.
  - Primera pieza: la documentación de referencia con los criterios de la evaluación técnica ([D-133](#d-133)) y una skill para crearla y mantenerla. El sistema de auditado viene después.
- **Interpretación adoptada:** la consulta de la referencia por la auditoría GSC es de interpretación (qué significa un tipo o una propiedad); no altera la independencia de [D-006](#d-006) ni la invariante 8: un incumplimiento técnico sigue sin descontar el GSC.
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#requisitos-técnicos-generales) 1.2. El directorio, su README y la fila del mapa de `CLAUDE.md` se crean con el código (T-045).
- **Relacionado:** D-006, D-130, D-133, OQ-30.

### D-130

**Perfil de implementación: definición y tres niveles en Web Schema.org.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-web-schema-technical-framework` §2. BASE §6.2 usa «perfil de implementación» en la tasa de cumplimiento técnico sin definirlo ([OQ-30](open-questions.md#f-evaluación-técnica)). Al estudiar el inventario de fuentes de Schema.org, Claude observó que Schema.org es permisivo por diseño (los rangos son tipos esperados, admite texto donde espera una entidad y no tiene propiedades obligatorias), que las condiciones de sintaxis salen de la serialización y que las propiedades exigidas y recomendadas salen de los consumidores. Propuso tres niveles. Usuario: «sí. versión más reciente 30.1 (ahora)».
- **Decisión:**
  - El **perfil de implementación** es el conjunto de especificaciones aplicables respecto del cual se determinan los requisitos técnicos pertinentes de un ámbito y su naturaleza obligatoria o recomendada.
  - La naturaleza obligatoria o recomendada de un requisito técnico es relativa al perfil que la establece. La fija la especificación, nunca el auditor.
  - En Web Schema.org, tres niveles: **serialización** (JSON-LD 1.1 con su procesado, Microdata y RDFa 1.1); **vocabulario** (Schema.org, versión fijada **30.1**); **consumidor** (Google Search: fichas de comerciante, variantes de producto, políticas de devolución y de envío, organización y fragmentos de producto).
  - La versión del vocabulario se fija y queda registrada con cada resultado; cambiarla obliga a revisar los requisitos que dependen de ella.
  - Google Merchant Center pertenece a Catálogos distribuidos; en Web Schema.org solo sirve para la consistencia transversal ([D-124](#d-124)).
  - (Enmendada por [D-145](#d-145): del consumidor, lo que exige es técnico; la presencia de lo que solo recomienda es, en general, apoyo del modelo de demanda del ámbito, con las salvedades de D-145; precisada después por [D-155](#d-155): sin ámbito, y localizador en la ficha de Web Schema.org.)
- **Interpretación adoptada:** el «sí» aprueba la recomendación sin añadir otros consumidores (Bing u otros); pueden añadirse después con la skill, como perfil nuevo. Los perfiles de Web (sin marcado) y de Catálogos distribuidos siguen en OQ-30 (el de Web, fijado después por [D-159](#d-159)).
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#perfil-de-implementación) 1.2; [scoring-systems](../10-model/scoring-systems.md#tasa-de-cumplimiento-técnico) 1.4; glosario (Perfil de implementación, Requisito técnico general); OQ-30 anotada.
- **Relacionado:** D-124, D-131, D-132, OQ-30.

### D-131

**Estados del requisito técnico.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-web-schema-technical-framework` §3. BASE §3.1 y FUND §4.2 piden documentar para cada requisito técnico «los estados de satisfacción, aplicabilidad y evaluación» sin fijar sus valores. Claude propuso fijar ahora solo los estados y dejar abierto el sistema cuantitativo. Usuario: «sí».
- **Decisión:**
  - **Satisfacción:** satisfecho o no satisfecho, según la comprobación de su método.
  - **Aplicabilidad:** no aplicable (NA) cuando el requisito no corresponde al perfil o al recurso examinado; se justifica y se separa de los pertinentes.
  - **Evaluación:** no evaluable (NE) es una incidencia de la auditoría (una comprobación que no se pudo hacer), no una puntuación, y no equivale a «no satisfecho». Es el mismo tratamiento que en la evaluación informativa ([D-117](#d-117)).
  - El sistema cuantitativo sigue abierto: cómo entran las obligatorias y las recomendadas en la tasa de cumplimiento técnico, umbrales y cobertura. No se fijan pesos.
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#estados-del-requisito-técnico) 1.2; [scoring-systems](../10-model/scoring-systems.md#tasa-de-cumplimiento-técnico) 1.4; glosario (Estados del requisito técnico); OQ-30 anotada.
- **Relacionado:** D-117, D-130, OQ-30.

### D-132

**Solo una especificación aplicable fundamenta un requisito técnico.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-web-schema-technical-framework` §4. El inventario de fuentes de Schema.org (`tmp/inventario_fuentes_auditoria_schema_org.md`, base del estudio que cita el artefacto) reúne especificaciones, directrices de consumidores, buenas prácticas, validadores y skills de terceros. Claude propuso la función de cada clase de fuente, aprobada con el plan.
- **Decisión:**
  - Solo una **especificación aplicable** (de serialización, de vocabulario o de un consumidor) fundamenta un requisito técnico. (Ampliada por [D-159](#d-159): también de protocolo y de documento, según el perfil del ámbito. Enmendada por [D-162](#d-162): por excepción, también una condición del proyecto adoptada en el canon, que el requisito nombra en lugar de citar una especificación.)
  - Las demás clases tienen otra función: instrumento del sistema (SHACL, PROV-O); principios generales (W3C Data on the Web Best Practices); método de comprobación (Schema Markup Validator, Rich Results Test), que no es fuente de criterios ni equivale a calidad informativa; práctica de terceros (skills de auditoría SEO), sin autoridad; antecedente histórico (GS1 SmartSearch, 2015); datos comerciales distribuidos (Merchant Center), para Catálogos distribuidos y la consistencia transversal.
  - Un requisito técnico expresa una sola condición comprobable.
  - Cada requisito técnico cita literalmente su especificación: fuente, sección y versión congelada.
- **Interpretación adoptada:** la condición única por requisito sigue el mismo criterio que la formulación de los requisitos informativos ([D-060](#d-060)): una necesidad, una condición.
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#fuentes-de-los-requisitos-técnicos) 1.2; glosario (Especificación aplicable).
- **Relacionado:** D-060, D-130, D-133.

### D-133

**Referencia técnica en web-audit: datos gobernados por el canon, decididos por los agentes.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-web-schema-technical-framework` §5. En la sesión de planificación, Claude comparó tres ubicaciones para la documentación de referencia y recomendó la A: datos y fichas en `web-audit/reference/`. El artefacto solo recoge la elegida. Usuario: «sí, A».
- **Decisión:**
  - La documentación de referencia vive en `web-audit/reference/`, como datos y fichas gobernados por el canon, igual que el catálogo de bloques de demand-engine: las fuentes, congeladas por versión (fuera de git y desechables); una ficha por fuente, con citas literales; y los requisitos técnicos, con los campos que pide el canon, su perfil y su cita.
  - Los requisitos técnicos los deciden los agentes, siempre con cita. El usuario los revisa si lo pide.
  - Una skill los crea y los mantiene: añadir una fuente, actualizar ante una versión nueva y validar. No crea conceptos, estados, pesos ni fórmulas; si le falta algo, va al intake.
- **Interpretación adoptada:**
  - El artefacto dice «los siete campos del canon»; el canon enumera seis (ámbito, especificación aplicable, naturaleza, método, evidencia y estados). Se lee como «los campos que pide el canon».
  - Es el mismo reparto que con el modelo de demanda ([D-044](#d-044), [D-084](#d-084)): el usuario fija el marco (perfiles, estados, función de las fuentes) y los agentes escriben el contenido. El canon prevalece sobre la referencia.
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#fuentes-de-los-requisitos-técnicos) 1.2. Formato, validador y skill: T-046.
- **Relacionado:** D-044, D-084, D-129, D-132.

### D-134

**Catálogo de pistas con destinatario; encontrarlas es código.** · aceptada (enmendada por [D-140](#d-140): las pistas de un requisito viven en él) · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-hints-catalog`. Usuario: «¿Dónde viven las reglas de pistas? Me interesa montar un sistema eficiente que reduzca al máximo la duplicidad, usando algún sistema de catálogo y referencias.» Claude comparó pistas dentro de cada requisito, un catálogo con destinatario y un catálogo con referencias desde cada requisito, y recomendó el segundo. Usuario: «podría ser» y, sobre encontrarlas solo con código, «Así es».
- **Decisión:**
  - Las pistas viven en un catálogo propio del motor de demanda. Cada pista se escribe una vez y va dirigida, con una de tres llaves, a un tipo de requisito (rasgo × entidad, o uno de los dos), a los requisitos que citan una misma fuente o a un requisito por su id.
  - Los requisitos no copian ni referencian sus pistas. Al montar el modelo, el motor junta las de las tres llaves sin repetir; el modelo lleva las pistas resueltas.
  - Encontrar las pistas de un requisito es una búsqueda por etiquetas exactas, solo con código. Aplicarlas lo hace el auditor razonando.
- **Interpretación adoptada:** la «tabla de reglas por rasgo × entidad» de [D-127](#d-127) pasa a ser el conjunto de pistas dirigidas a un tipo dentro de este catálogo; quién las escribe no cambia. Los campos exactos y el lugar en el perfil del RI siguen en [OQ-68](open-questions.md); la marca de dimensión de comparación podría usar las mismas llaves (posibilidad sustituida por [D-139](#d-139)) (OQ-69).
- **Consecuencias:** [assessment-hints](../10-model/assessment-hints.md) 1.1 (reglas 6 a 8, pendiente); [demand-model](../10-model/demand-model.md) 3.2; [model-training](../10-model/model-training.md) 1.19; glosario (Pistas de valoración); OQ-68 y OQ-69 anotadas.
- **Enmienda ([D-140](#d-140)):** la tercera llave (un requisito por su id) queda sustituida: las pistas de un requisito viven en el propio requisito, y «los requisitos no copian ni referencian sus pistas» vale solo para las de tipo y de fuente.
- **Relacionado:** D-125, D-127, D-128, D-140, OQ-68, OQ-69.

### D-135

**Campos de una pista de valoración, quién escribe las dirigidas a una fuente y cómo llegan al auditor.** · aceptada (precisada por [D-140](#d-140): `para`) · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-hint-fields`; cierra [OQ-68](open-questions.md). Claude propuso seis campos, un escritor por destino y un campo en el perfil del RI. Usuario: «OK», con «ok al id, pero sin 0s delante» y «olvida lo de los índices por ahora».
- **Decisión:**
  - Campos: `id` (número del sistema sin ceros delante: `PV-1`, `PV-2`…), `pista` (criterio y porqué en una o dos frases), `propiedad`, `ac`, `para` (tipo, fuente o requisito) y `origen` (quién y en qué se apoya).
  - Escritores por destino: tipo, el entrenamiento; fuente, taxo; requisito, taxo o PAA.
  - Al montar el modelo, el código guarda las pistas resueltas de cada requisito; el perfil del RI las recibe en `pistas_valoracion`, que se rellena solo.
- **Interpretación adoptada:** el índice generado de pistas por requisito queda aplazado como cuestión abierta ([OQ-70](open-questions.md)); hasta entonces el código recorre las pistas al montar el modelo ([D-134](#d-134)).
- **Consecuencias:** cierra OQ-68; nueva OQ-70. [assessment-hints](../10-model/assessment-hints.md) 1.2 (reglas 6, 9 y 10, pendiente); [ri-profile](../20-methods/audit-gsc/ri-profile.md) 0.2 (campo `pistas_valoracion`); glosario (Pistas de valoración).
- **Precisión ([D-140](#d-140)):** `para` vale para un tipo o una fuente; las pistas de un requisito viven en él y no llevan `para`.
- **Relacionado:** D-127, D-128, D-134, D-140, OQ-68, OQ-70.

### D-136

**Gobierno de las pistas de valoración: aceptación, duplicadas, retiradas y orígenes.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-hints-governance` §1, §3–5 y §7. Claude estudió si ya estaba todo lo necesario para definir las pistas y propuso lo que faltaba. Usuario: «te acepto todas las recomendaciones. Lo demás vayamos resolviendo poco a poco».
- **Decisión:**
  - Las pistas las redactan los agentes sin aprobación del usuario, que las revisa cuando quiere. Entran si pasan comprobaciones automáticas: seis campos, destino existente, criterio y no lista. Por ahora no hay métrica de calidad.
  - Antes de añadir una pista se busca otra con el mismo destino y la misma propiedad: si dice lo mismo, no se añade; si la contradice, se marca como duda.
  - Una pista no se borra: se retira, y su número no se reutiliza. «Nunca se quitan» ([D-127](#d-127)) vale entre escritores, no para corregir.
  - Valores de `origen`: «marco», «normativa», «referencias» y «paa».
  - Orden de trabajo aceptado: gobierno; OQ-69; piloto con las pistas de los nueve requisitos de sábanas y sus tipos, para probar el formato antes de automatizar; después el paso de taxo, el lote por tipo y T-043.
- **Interpretación adoptada:** «marco» es aquí el origen de las pistas por tipo que redacta Claude, no el origen «marco» de la capa general de la información resolutiva; no son el mismo origen. La métrica de calidad queda en [OQ-72](open-questions.md).
- **Consecuencias:** precisa D-127 y D-128; [assessment-hints](../10-model/assessment-hints.md) 1.3 (reglas 9, 11 y 13); nueva OQ-72.
- **Relacionado:** D-127, D-128, D-135, D-137, OQ-72.

### D-137

**Cuándo se definen las pistas de valoración.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-hints-governance` §2. Usuario: «mediante una pasada manual de Claude podemos construir pistas. Pero luego las pistas se irán definiendo al crear modelos de demanda, incluso cuando se realizan entrenamientos».
- **Decisión:**
  - Arranque: una pasada manual de Claude construye un primer lote; sus pistas por tipo las redacta Claude por rasgo × entidad, desde la guía de los AC y las tres familias de comprobación, y el entrenamiento las guarda y las coloca.
  - Después las pistas se van definiendo al crear modelos de demanda y en los entrenamientos.
- **Interpretación adoptada** (de Claude, recogida en el artefacto para que el usuario la corrija): encaja en el mecanismo de [D-045](#d-045). Al crear un modelo, el motor escribe también las pistas de los bloques o requisitos nuevos, que quedan «sin compilar» y se encolan; los entrenamientos de taxo y de PAA añaden pistas y consolidan las encoladas. En qué paso y con qué material, y qué `origen` llevan esas pistas, queda en [OQ-71](open-questions.md).
- **Consecuencias:** [assessment-hints](../10-model/assessment-hints.md) 1.3 (regla 12); [model-training](../10-model/model-training.md) 1.20; OQ-66 anotada; nueva OQ-71.
- **Relacionado:** D-045, D-127, D-135, D-136, OQ-66, OQ-71.

### D-138

**Pistas de valoración: niveles no exclusivos, sin ámbito, trazabilidad y versión.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-hints-governance` §6 («te acepto todas las recomendaciones»).
- **Decisión:**
  - Los niveles no son exclusivos: dicen dónde se concentran las pistas, no que un tipo solo pueda tocar dos AC.
  - Las pistas no dicen ámbito; el auditor las aplica a lo que vea en cada ámbito. Si una pista solo tiene sentido en uno, se añade el campo.
  - El registro del GSC cita las pistas que usó el auditor (`PV-n`).
  - El modelo de una ficha anota qué versión del catálogo de pistas usó.
- **Consecuencias:** precisa [D-125](#d-125); [assessment-hints](../10-model/assessment-hints.md) 1.3 (reglas 1 y 10); [gsc-decision](../20-methods/audit-gsc/gsc-decision.md) 0.4 (GSC-12 y plantilla YAML: `pistas_usadas`).
- **Relacionado:** D-125, D-135, D-136.

### D-139

**Cómo se fija la marca de dimensión de comparación.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-comparison-mark`; cierra [OQ-69](open-questions.md). Claude propuso decidir la marca requisito a requisito, con un criterio y «se compara» por defecto. Usuario: «en principio es tal cual propones», con la duda de si el valor por defecto era adecuado. Un estudio rápido (70 requisitos al azar, clasificados por Claude) dio 49 % se compara, 43 % no y 9 % dudoso. Usuario: «todo OK».
- **Decisión:**
  - Marca por requisito, no por tipo.
  - Criterio: se compara si la respuesta cambia de una oferta a otra y el comprador elige por ese valor; no se compara si (a) es igual en todas las ofertas, (b) solo sirve para encajar con una necesidad o un gusto (un filtro) o (c) identifica la oferta o su estado.
  - Sin valor por defecto: marca explícita con un motivo corto; los dudosos, «se compara» mientras no haya pruebas, para no quitar un criterio sin motivo.
  - Pruebas: preguntas comparativas de PAA, la justificación del requisito en taxo, una ley que exista para comparar.
  - Quién y cuándo: como las pistas ([D-137](#d-137)); contradicciones, como duda ([D-136](#d-136)).
- **Interpretación adoptada:** el estudio es orientativo (muestra pequeña, un solo clasificador). Cuando dos fuentes se contradicen y la marca queda como duda, se trata como dudosa: «se compara» mientras se resuelve. Sustituye la posibilidad, anotada en [D-134](#d-134) y OQ-69, de fijar la marca con las mismas llaves que las pistas.
- **Consecuencias:** precisa [D-126](#d-126); cierra OQ-69. [assessment-hints](../10-model/assessment-hints.md) 1.4 (regla 5, pendiente); [demand-model](../10-model/demand-model.md) 3.3; glosario (Marca de dimensión de comparación).
- **Relacionado:** D-118, D-126, D-134, D-136, D-137, OQ-69.

### D-140

**Las pistas dirigidas a un requisito viven en el requisito.** · aceptada · 2026-10-27

- **Contexto:** `INTAKE 2026-10-27-requirement-hints-location`, tras el piloto de T-050. El usuario preguntó por qué un catálogo de pistas «de uso general» tenía pistas vinculadas a un requisito. Claude explicó las tres llaves de [D-134](#d-134) y la alternativa descartada entonces («pistas dentro de cada requisito»). Usuario: «sí. Es mejor que vivan en el requisito».
- **Decisión:**
  - Las pistas dirigidas a un requisito concreto viven en el propio requisito del catálogo de demanda, no en el catálogo de pistas.
  - Las dirigidas a un tipo y a una fuente siguen en el catálogo de pistas.
- **Interpretación adoptada:**
  - El requisito lleva sus pistas en una lista propia, como la información resolutiva. Cada pista tiene los mismos campos que en el catálogo salvo `para`: su destino es el requisito que la contiene.
  - Los `id` (`PV-n`) siguen siendo únicos en todo el sistema, estén en el catálogo de pistas o en un requisito, porque el registro del GSC los cita ([D-138](#d-138)).
  - Llegan por el árbol de bloques a todas las clases que heredan el requisito, como antes.
  - Taxo y PAA las escriben en el requisito; se suman entre escritores, se retiran para corregirlas y se comprueban igual ([D-136](#d-136)).
  - La búsqueda sigue siendo código sin LLM: junta las pistas de tipo y de fuente del catálogo con las que lleva el requisito, sin repetir.
  - La versión del catálogo de pistas que anota el modelo ([D-138](#d-138)) cubre las de tipo y de fuente; las de un requisito van con la versión de su bloque.
  - No cambia ninguna incidencia abierta: I-43 sigue para las llaves de tipo y fuente; I-44 sigue, porque una pista del requisito puede repetir una de tipo o de fuente; I-45 sigue (origen de las pistas propias de un requisito de la capa general).
- **Consecuencias:** enmienda [D-134](#d-134) (los requisitos ya no se limitan a encontrar sus pistas por etiquetas) y precisa [D-135](#d-135) (`para`). [assessment-hints](../10-model/assessment-hints.md) 1.6 (reglas 6 a 10); [demand-model](../10-model/demand-model.md) 3.4; glosario (Pistas de valoración); OQ-73 anotada.
- **Relacionado:** D-127, D-134, D-135, D-136, D-138, I-43, I-44, I-45, OQ-73.

### D-141

**Productos vecinos fuera del perímetro de PAA, antes de la lectura sobre la oferta.** · aceptada (la categoría madre y el material, enmendados por [D-146](#d-146)) · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-paa-control-review-rules`, paso 2. Al revisar los casos de control de PAA (T-042), el agente había metido dentro preguntas sobre el calzado en general (pantuflas, botas) o sobre almohadas (cojines), releyéndolas sobre la oferta. Comentario del usuario en la hoja de revisión: «No es de pantuflas» (notas de T-042).
- **Decisión:**
  - Las preguntas sobre **otro producto** quedan **fuera** del perímetro siempre: la categoría madre en general («calzado», «zapatos») o un hermano (almohadas, zapatillas deportivas).
    (Enmendado por [D-146](#d-146): la parte de la categoría madre ya no rige; la pregunta sobre la madre va dentro si pregunta por algo que la clase hereda de su bloque.)
  - **El perímetro va antes de la lectura sobre la oferta.** La lectura solo decide si una pregunta sobre el producto de la clase pide un hecho declarable.
  - Un producto vecino nunca apoya requisitos de la clase (invariante 10).
  - Su presencia es una señal para las semillas ([D-114](#d-114)).
- **Interpretación adoptada:**
  - Enmienda la cláusula de [D-100](#d-100) según la cual «la misma lectura vale para el perímetro dudoso». Lectura de Claude: sus dos ejemplos siguen dentro, pero por el perímetro, porque las contraindicaciones del bambú y el origen de la seda tratan del material del producto de la clase, que el paso de perímetro del reglamento ya ponía dentro.
  - «Señal para las semillas» se lee como un dato para el entrenamiento de PAA (la estrategia de semillas, [D-114](#d-114)). No se fija aquí ninguna regla nueva de semillas; cómo se usa esa señal queda para el entrenamiento de PAA.
- **Consecuencias:** enmienda D-100. [choice-criteria](../10-model/choice-criteria.md) 1.10; [construction-routes](../10-model/construction-routes.md) (perímetro); glosario (Lectura sobre la oferta, Producto vecino); reglamento del agente (`demand-engine/classifier/paa.md`, v5); casos de control de PAA (`demand-engine/cases/paa/`).
- **Enmienda ([D-146](#d-146)):** la categoría madre ya no queda fuera siempre: va dentro cuando la pregunta trata de algo que la clase hereda de su bloque, y fuera si solo tiene sentido para otro producto. La pregunta sobre un material que la clase tiene o hereda va dentro.
- **Relacionado:** D-094, D-100, D-114, D-142, D-146.

### D-142

**Moda, popularidad, preferencia general y alternativa de producto en PAA.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-paa-control-review-rules`, pasos 3 y 4. En los casos de control (notas de T-042), los agentes trataron de forma distinta la tendencia (botas y pantuflas «no genera»; el estilo de sofás cama, «genera»), la popularidad, el «¿cuál es el mejor?» y la elección entre dos productos.
- **Decisión:**
  - **La moda o tendencia nunca genera** («¿qué X se llevan?», «¿qué X están de moda?»): «estar de moda» depende del mercado y del momento (C2/C4). Es un caso de la excepción de [D-110](#d-110).
  - **La popularidad** («la más vendida») no genera: es reputación (C4; invariante 14).
  - **La preferencia general** («¿cuál es el mejor X?») es un **criterio intermedio** ([D-104](#d-104)): cubierto y descompuesto en las prestaciones, como «calidad» en sábanas. No es «no genera».
  - **La alternativa de producto** («¿sofá cama o cama abatible?») no genera (C3).
- **Interpretación adoptada:**
  - Lectura de Claude de «caso de la excepción de D-110»: estar de moda es un aspecto que ninguna categoría declarable por la oferta resuelve; una oferta puede declarar su estilo, pero no que esté de moda. El efecto lo fijó el usuario en la revisión: sale el candidato de estilo de sofás cama.
  - Lectura de Claude de la alternativa de producto: C3 porque depende de la situación de quien compra (un escenario, como en la tabla de C1–C4), no de la oferta.
- **Consecuencias:** precisa D-104 y D-110. [choice-criteria](../10-model/choice-criteria.md) 1.10; glosario (Criterio de elección intermedio); reglamento del agente (`demand-engine/classifier/paa.md`, v5); casos de control de PAA.
- **Relacionado:** D-091, D-104, D-110, D-141.

### D-143

**Mínimo de representación de la oferta.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-minimum-representation-image`. Al estudiar cómo se reparten la evaluación técnica y la de calidad informativa en Web Schema.org, el usuario planteó que hay datos fundamentales para poder representar la oferta (nombre, descripción, imagen, url…) cuya frontera no conseguía dibujar, y que podrían examinarse desde las dos evaluaciones: si existen y están bien formados, desde la técnica; la calidad de lo que transmiten, desde la informativa. Confirmó que el mínimo incluye también los datos que solo sostienen la representación.
- **Decisión:**
  - **Definición:** el mínimo de representación son los datos sin los que no existe una representación de la oferta: los que hacen falta para descubrirla, acceder a ella e identificarla, según las [funciones informativas de la IA](../10-model/ai-functions.md). Lo que sirve para comprender, comparar, evaluar y justificar es contenido.
  - **Dos tipos:** los datos que llevan un hecho comercial (el nombre, los identificadores) y los que solo sostienen la representación y no responden a ninguna cuestión (la url, el identificador de la entidad, que el Product esté enlazado a su Offer, la imagen).
  - **Evaluación:** si existen y están bien formados lo dice la evaluación técnica; los que llevan un hecho comercial los juzga también la informativa por lo que transmiten (disponibilidad efectiva y criterios de aceptación); los de sostén solo la técnica.
  - **No es doble cómputo:** cada sistema informa en sus propios términos, y un incumplimiento técnico sigue sin descontar el GSC (invariante 8).
  - **No crea requisitos técnicos:** sus comprobaciones son las de las especificaciones del perfil. Si un dato del mínimo no tiene requisito en el perfil de un ámbito, se registra el hueco; no se inventa el requisito.
  - Qué datos lo forman, salvo la imagen ([D-144](#d-144)), queda abierto ([OQ-74](open-questions.md)). (Cerrada para Web Schema.org por [D-147](#d-147).)
- **Interpretaciones adoptadas:**
  - El concepto va en [commercial-information](../10-model/commercial-information.md), junto a la representación y las dos dimensiones de evaluación. Es una clasificación de datos que dice qué evaluación mira cada aspecto: no es una escala, un indicador ni una unidad de puntuación. Usar las funciones de la IA para trazar la frontera es orientar el estudio, que es lo que permiten (ai-functions, regla 1).
  - El ejemplo de doble cómputo (sin nombre: requisito técnico no satisfecho y disponibilidad 0 en las cuestiones que solo él responde) es hipotético.
  - La frontera general entre las dos evaluaciones (la técnica mira la forma; la informativa, la presencia y la suficiencia) y el tratamiento como informativos de los 83 requisitos técnicos apartados en el triaje siguen en estudio: [OQ-75](open-questions.md). (Cerrada por [D-145](#d-145).)
- **Consecuencias:** [commercial-information](../10-model/commercial-information.md) 1.2; [evaluation-scopes](../10-model/evaluation-scopes.md) 1.3 (punto de contacto); glosario (nueva entrada Mínimo de representación); nuevas OQ-74 y OQ-75.
- **Relacionado:** D-129, D-130, D-144.

### D-144

**La imagen: sostén del mínimo de representación; lo que muestra no es información.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-minimum-representation-image`. El usuario tenía dudas sobre si la imagen forma parte del mínimo de representación aunque no responda a ninguna cuestión, y pidió a Claude que lo estudiara a fondo y propusiera. Claude reunió lo que dicen el canon (D-052, disponibilidad efectiva, funciones de la IA), el art. 19.c del GPSR (comprobado en el texto oficial alemán), las referencias de Google, Merchant Center, Amazon y Schema.org, y las fichas congeladas, y comparó tres alternativas. El usuario eligió la A.
- **Decisión:**
  - La imagen **forma parte del mínimo de representación como sostén**: por Identificar (el art. 19.c del GPSR exige que la oferta a distancia incluya información que permita identificar el producto, incluida una imagen suya) y por Descubrir (image es obligatoria en las fichas de comerciante de Google).
  - Se evalúa en la **evaluación técnica**: que exista, que su URL sea válida, que se pueda recuperar y que tenga un formato admitido (en Web Schema.org, `ws-consumer/003`–`010` y `185`–`186`).
  - **Lo que la imagen muestra no es información; la información explícita que lleva sí lo es.** Tres papeles:
    - sostiene la identificación: evaluación técnica;
    - expresa información explícita (plano acotado, tabla de tallas, etiqueta energética, advertencias): es información si el ámbito permite leerla; en Web Schema.org, solo si está en texto en el marcado (`caption`, `embeddedTextCaption`); en Web, según las pruebas de legibilidad;
    - muestra lo que no afirma (color, piezas, aspecto): no es información pertinente, no da disponibilidad, no resuelve ningún RI y no sirve para refutar en Fiabilidad; puede crear una necesidad que el texto debe resolver (descripción de `gen/21`).
  - Si la foto es genérica o de otra variante, no se juzga como información: en Catálogos distribuidos es una regla de contenido de Merchant Center, cuando exista ese perfil; en Web Schema.org no se juzga, porque el contraste del marcado con la página o con la realidad quedó fuera en el triaje del 2026-10-28 (bloque «marcado frente a página»).
  - **Catálogo:** la aportación «imagen que permite identificar el producto» de `gen/24` deja de ser aportación. Se enmienda la interpretación de [D-052](#d-052): la imagen no resuelve `gen/01` ni `gen/24`. Con esto desaparece también la discrepancia entre D-052, que hablaba de `gen/01`, y el catálogo, que la tenía en `gen/24`.
  - Alternativas descartadas: B, un requisito propio valorado con los AC (crea una cuestión nueva, contra D-052; los AC están pensados para afirmaciones; el juicio visual es difícil de reproducir); C, una propiedad recomendada más (Google la exige y el GPSR la liga a la identificación).
- **Interpretaciones adoptadas:**
  - La regla de la imagen va en [effective-availability](../10-model/effective-availability.md), dentro de la pertinencia, porque decide qué cuenta como información pertinente; «no sirve para refutar» se refleja en [acceptance-criteria](../10-model/acceptance-criteria.md#fiabilidad-lectura-refutadora-y-comprobaciones).
  - Si el texto dentro de una imagen cuenta como legible en Web no abre una OQ nueva: es parte de las pruebas de obtención y legibilidad, y se anota en [OQ-20](open-questions.md).
  - El «plano o imagen acotada» de [resolving-information](../10-model/resolving-information.md#ejemplo-mínimo) sigue valiendo: es información explícita.
  - La implantación en `demand-engine/catalog/gen.json` (quitar la aportación de `gen/24` y subir la versión de la capa general) queda como tarea T-054, como las implantaciones anteriores del catálogo; afecta también a `demand-engine/catalog/rules/resolving.json`, que lista la aportación en `gen/24`.
- **Consecuencias:** enmienda una interpretación de D-052. [effective-availability](../10-model/effective-availability.md) 1.2; [acceptance-criteria](../10-model/acceptance-criteria.md) 1.5; [commercial-information](../10-model/commercial-information.md) 1.2 (miembro del mínimo); OQ-20 anotada; catálogo (`gen.json`, `rules/resolving.json`), por implantar en T-054.
- **Relacionado:** D-052, D-119, D-120, D-130, D-143.

### D-145

**Frontera entre la evaluación técnica y la informativa: decide la naturaleza que fija la especificación.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-technical-informative-frontier`. Responde a [OQ-75](open-questions.md). El usuario propuso que la evaluación técnica mire, con la representación que hay, si se cumplen las pautas y requisitos técnicos, y que la de calidad informativa estudie la suficiencia a través de la disponibilidad; y que de las referencias se pueden extraer requisitos informativos para el ámbito Web Schema.org. Claude clasificó los 414 requisitos técnicos que siguen en pie tras el triaje del 2026-10-28 por lo que comprueban: unos 280 son técnicos con cualquier regla (sintaxis y vocabulario, acceso, forma del valor, estructura y completitud de lo exigido, 71) y la frontera solo afecta a los 136 que piden que se publique algo (presencia de primer nivel: 10 obligatorios y 48 recomendados; completitud recomendada: 78). Comparó tres reglas. Usuario: «lo que has recomendado».
- **Decisión (alternativa A):**
  - **Evaluación técnica:** cómo está construido lo que se publica (sintaxis y vocabulario; acceso y exposición; forma del valor; estructura y relaciones; completitud de lo publicado que el consumidor exige), más la presencia de lo que el consumidor **exige**.
  - **Evaluación informativa:** si se publica lo que el consumidor solo **recomienda**, como cualquier otra cuestión del modelo de demanda.
  - **El criterio es la naturaleza que fija la especificación**, no un juicio del auditor, igual en el primer nivel y en lo anidado.
  - **Excepción:** los recomendados que sirven para interpretar un valor ya publicado (`bestRating`, `worstRating`, la unidad del peso, la URL del logo) siguen en la técnica. (Precisada por [D-148](#d-148): es el punto 2 de la formación estructural, que también recoge la completitud de lo exigido.)
  - **Doble lectura, solo en lo exigido:** si falta el precio, la técnica dice que el consumidor lo exige y falta, y la informativa, que la cuestión no tiene respuesta en el ámbito. No es doble cómputo.
  - **Mínimo de representación:** mantiene en la técnica los datos del mínimo que el consumidor recomienda sin exigir ([OQ-74](open-questions.md), candidatos: url de la oferta, identificadores, marca). (Cerrada por [D-147](#d-147): marca, GTIN y MPN, fuera.)
  - **Lo recomendado, al modelo de demanda del ámbito Web Schema.org:** cuenta que la propiedad aparezca en la referencia, no su naturaleza; la importancia la decide el modelo, como con los PTD de Amazon ([D-052](#d-052)). Una propiedad no es un RI por sí misma: apoya un requisito o una aportación existentes, o propone un candidato. Incluirlo en el motor de demanda es una tarea aparte, por indicación del usuario: T-056. (Precisada por [D-155](#d-155): la propiedad recomendada es apoyo de demanda sin ámbito y localizador en la ficha de Web Schema.org; desaparece «del ámbito».)
  - **Referencia técnica:** los 126 requisitos de presencia recomendada (48 de primer nivel y 78 de completitud) salen, salvo los que OQ-74 incluya en el mínimo (nueve, [D-147](#d-147)), y se conservan en un registro con su motivo. De los 83 que el usuario apartó en el triaje, 29 pasan a la informativa y 54 siguen técnicos (atributos 11/5, certificaciones 2/6, fragmentos de producto 9/18, reseñas 7/25). Retirada en `web-audit/reference/` (estos y los 26 que no se auditan): T-055, después de OQ-74.
  - **Perfil de implementación:** el nivel del consumidor deja de fijar «propiedades exigidas y recomendadas»: lo exigido es técnico y la presencia de lo recomendado es apoyo del modelo de demanda. Enmienda [D-130](#d-130).
  - Alternativas descartadas: B, decide la función (obliga a juzgar dato a dato y a separar el primer nivel de lo anidado sin criterio firme); C, todo el perfil es técnico (ruido y la misma ausencia informada dos veces).
- **Interpretaciones adoptadas:**
  - La forma del valor de lo recomendado (p. ej., `ws-consumer/043`, un solo valor de `sku`, y `064`, `priceValidUntil` en ISO 8601) sigue siendo técnica: el artefacto la cuenta entre lo técnico con cualquier regla y solo saca de la técnica la presencia. Así se lee la fila del consumidor del perfil: lo que exige y la forma de lo que se publica.
  - «No es doble cómputo» se apoya en lo que ya dice el punto de contacto entre las evaluaciones: la incidencia técnica y su efecto sobre la disponibilidad se registran por separado.
  - La regla vive en [evaluation-scopes](../10-model/evaluation-scopes.md), junto al perfil y al punto de contacto; el destino de lo recomendado, en [demand-model](../10-model/demand-model.md#relación-con-los-ámbitos-de-evaluación). La tabla de la clasificación es evidencia de la decisión, no canon.
  - Cómo entra lo recomendado en el modelo de demanda (vía de construcción, mapeo, ámbito pertinente, versión de la referencia) es una cuestión metodológica además de una tarea: nueva [OQ-76](open-questions.md), que T-056 resuelve con `/docs-update`.
- **Consecuencias:** enmienda D-130; precisa D-143; cierra OQ-75; OQ-74 y OQ-30 anotadas; nueva OQ-76. [evaluation-scopes](../10-model/evaluation-scopes.md) 1.4; [commercial-information](../10-model/commercial-information.md) 1.3; [demand-model](../10-model/demand-model.md) (relación con los ámbitos); glosario (Perfil de implementación). Fuera de `docs/`: T-055 (referencia técnica y skill `/web-reference`) y T-056 (motor de demanda).
- **Relacionado:** D-052, D-129, D-130, D-131, D-143, D-144.

### D-146

**La categoría madre y el material en el perímetro de PAA.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-paa-parent-and-material`. Resuelve [I-48](issues.md#i-48). En la pasada de control con el reglamento PAA v5 (T-052), los agentes aplicaron al pie de la letra «la categoría madre en general, fuera siempre» de [D-141](#d-141) y sacaron 63 preguntas más que los casos de control: 35 sobre «el sofá» sin más en sofás cama y 26 sobre «zapatos» o «calzado» en botas y pantuflas. Con ellas se perdían aportaciones esperadas y el criterio de moda de sofás cama. En pantuflas, además, la revisión del usuario (T-042) había puesto fuera dos preguntas sobre el cuero que el agente v5 dejaba dentro.
- **Decisión (opción B):**
  - **Categoría madre:** una pregunta sobre la categoría madre va **dentro** cuando pregunta por algo que la clase hereda de su bloque: el cuidado del ante (`cat.calzado/13`) en botas, la firmeza (`cat.sofas/12`) en sofás cama, «¿Qué sofá me compro?» (preferencia general, [D-142](#d-142)) en sofás cama. Va **fuera** si solo tiene sentido para otro producto (calzado para la montaña, podólogos) o si trata de un hermano.
  - **Material:** una pregunta sobre el material va **dentro** si la clase tiene o hereda ese material, como la seda en sábanas. «Zapatillas» sin señal de deporte o calle se lee como la clase (pantuflas).
  - **Semillas:** no cambian. «Sofás» sigue en el núcleo de sofás cama ([D-114](#d-114)).
  - Alternativas descartadas: A, la madre fuera siempre y semillas solo de la clase; C, solo la madre genérica («calzado», «muebles») fuera.
- **Interpretaciones adoptadas:**
  - «Algo que la clase hereda de su bloque» se lee como un requisito o una aportación de un bloque que la clase hereda, o un criterio de elección que vale igual para el producto de la clase; el último es el caso de la preferencia general de «¿Qué sofá me compro?», que el artefacto cita entre los ejemplos de dentro.
  - El hermano y la pregunta que solo tiene sentido para otro producto siguen siendo **productos vecinos**: fuera, sin apoyar requisitos, y señal para las semillas. La madre deja de ser vecino en lo que la clase hereda.
  - La lectura de «zapatillas» es un ejemplo del artefacto para pantuflas, no una regla de denominaciones para otras clases: una denominación ambigua se lee como la clase cuando no hay señal del vecino.
  - En pantuflas se corrige la revisión del 2026-10-27 (`INTAKE 2026-10-28-paa-control-review-rules`, paso 2): «¿Cómo saber si unas zapatillas son de piel?», «¿Cómo saber si es 100% cuero?» y «¿Cuáles son los 3 tipos de cuero?» vuelven dentro y sus tres aportaciones de cuero pasan a esperadas. El resto del efecto de aquel paso en pantuflas y botas (N1 y el criterio de salud del pie) no lo toca el artefacto.
- **Consecuencias:** enmienda D-141; resuelve I-48. [choice-criteria](../10-model/choice-criteria.md) 1.11; [construction-routes](../10-model/construction-routes.md) 1.7 (perímetro); glosario (Producto vecino). Fuera de `docs/`: reglamento del agente (`demand-engine/classifier/paa.md`, v6) y casos de control de PAA (`demand-engine/cases/paa/`), en T-053.
- **Relacionado:** D-100, D-104, D-114, D-141, D-142.

### D-147

**Datos del mínimo de representación en Web Schema.org.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-minimum-members-structural-formation` §1. Responde a [OQ-74](open-questions.md). Con la frontera de [D-145](#d-145), lo que el consumidor exige ya es técnico, y el mínimo de representación decide qué datos que el consumidor solo recomienda se quedan en la técnica. El usuario preguntó si se tenía en cuenta lo que Google exige, también lo condicional. Claude lo comprobó en las fuentes congeladas de Google Search y de Merchant Center. Usuario, ante la propuesta conjunta con [D-148](#d-148): «yes».
- **Decisión:**
  - **Dos pruebas:** función (¿hace falta para descubrir la oferta, acceder a ella o identificarla?, [D-143](#d-143)) y universalidad (¿lo tiene toda oferta a la que se aplica? Si un producto puede no tenerlo legítimamente, su ausencia puede ser un hecho del producto, que resuelve la informativa con un «no» fundamentado; la técnica no puede distinguir «no tiene» de «no lo publica»).
  - **Datos del mínimo en Web Schema.org:** de sostén, la url de la oferta (`ws-consumer/066`, y `202` para el grupo en un sitio de una sola página), el enlace Product → Offer (`001`, `153`), la relación variante ↔ grupo (`193`, `032`, `034`, `192`), variesBy (`205`), el identificador de la entidad (`@id`, sin requisito: hueco que se registra) y la imagen ([D-144](#d-144)); con hecho, el nombre del producto y del grupo (`002`, `150`, `187`), el SKU (`042`) y el nombre del vendedor (`339`).
  - **Fuera del mínimo en Web Schema.org:** GTIN y MPN (gen/03), la marca (gen/02), la descripción, la categoría y los datos legales, de contacto, la url y el logo del vendedor (gen/13, gen/14). Su presencia la juzga la informativa.
  - **Nueve recomendados se quedan en la técnica** por ser parte del mínimo (`032`, `034`, `042`, `066`, `153`, `192`, `202`, `205`, `339`); unos 117 de presencia recomendada pasan a la informativa (T-055), antes de separar las partes de interpretación y de coherencia que D-148 mantiene en la técnica.
  - **Lo obligatorio, también lo condicional, es técnico** (D-145): 169 obligatorios del consumidor, 9 universales y 160 condicionales, con la condición en su aplicabilidad. Google Search exige un identificador por variante (`195`) y el del grupo (`193`), técnicos con independencia del mínimo.
  - **GTIN, MPN y marca** son recomendados en Google Search y quedan fuera del mínimo por la prueba de universalidad. En Merchant Center, que pertenece a Catálogos distribuidos ([D-130](#d-130)), el GTIN es «It depends», muy recomendado si existe, y el MPN (si no hay GTIN) y la marca (en productos nuevos) son obligaciones condicionales; al definir ese perfil, D-145 hará técnicas esas obligaciones, y el perfil decidirá el GTIN. `identifier_exists` de Merchant Center confirma la prueba de universalidad; el marcado Schema.org no tiene un campo equivalente.
- **Interpretaciones adoptadas:**
  - La lista vale para Web Schema.org, el único ámbito con perfil. Los datos del mínimo en Web y en Catálogos distribuidos se fijarán con sus perfiles ([OQ-30](open-questions.md)); OQ-74 se cierra para Web Schema.org. (El perfil de Web lo fija [D-159](#d-159) sin decidir su mínimo, que pasa a [OQ-84](open-questions.md#f-evaluación-técnica).)
  - La prueba de universalidad se lee como un segundo filtro de [D-143](#d-143), no como un concepto nuevo: concreta «hace falta» con la invariante de neutralidad (un «no» fundamentado resuelve la cuestión).
  - El registro del hueco del `@id` se hace en la referencia técnica, dentro de T-055.
- **Consecuencias:** precisa D-143; cierra OQ-74; OQ-30 anotada. [commercial-information](../10-model/commercial-information.md) 1.4; [evaluation-scopes](../10-model/evaluation-scopes.md) 1.5; glosario (Mínimo de representación). T-055 queda desbloqueada.
- **Relacionado:** D-130, D-143, D-144, D-145, D-148.

### D-148

**Formación estructural.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-minimum-members-structural-formation` §2. El usuario preguntó por los datos obligatorios de una estructura opcional que se incluye, y propuso verlo como «formación estructural: que una estructura de datos que debe tener varias partes no quede incompleta». En [D-145](#d-145) eso era la «completitud de lo publicado que el consumidor exige», con una excepción aparte para los recomendados que sirven para interpretar un valor publicado. Usuario, ante la propuesta conjunta con [D-147](#d-147): «yes».
- **Decisión:**
  - **Formación estructural** (técnica): cuando se publica una estructura, (1) tiene las partes que el consumidor exige para ella; (2) tiene las partes sin las que un valor publicado no se puede interpretar (la unidad del peso, la escala de una valoración, el sistema de tallas, la moneda de un precio unitario); (3) sus partes son coherentes entre sí (con `doesNotShip` no hay tarifa; con devolución gratuita no hay importe de devolución).
  - Las partes que solo añaden otro hecho (tipo de reembolso, tarifa de reposición, tiempo de preparación de un servicio de envío) son presencia de lo recomendado → informativa.
  - La estructura puede ser opcional y estar incluida: lo que cuenta es que, si se publica, no quede incompleta.
  - Absorbe la excepción de D-145 (punto 2).
  - **Lo técnico** queda en tres categorías (sintaxis y vocabulario; acceso y exposición; formación estructural, que incluye la forma del valor) más dos presencias (los datos exigidos de primer nivel y los datos del mínimo de representación).
- **Interpretaciones adoptadas:**
  - La «estructura y relaciones» de D-145 queda dentro de la formación estructural como coherencia entre partes (punto 3), porque el artefacto deja lo técnico en tres categorías sin ella. Los ejemplos son requisitos de la referencia: una sola moneda (`ws-consumer/147`, `174`) y URL distintas por variante (`200`). Es una lectura de Claude: el punto 3 habla de las partes de una estructura, y esto lo extiende al marcado de la página.
  - El ejemplo del envío en la oferta y la tabla de estructuras de la referencia son ilustración y evidencia de la decisión, con requisitos reales (`105`, `122`).
- **Consecuencias:** precisa D-145. [evaluation-scopes](../10-model/evaluation-scopes.md) 1.5 (frontera); [demand-model](../10-model/demand-model.md) 3.6; glosario (nueva entrada Formación estructural; Perfil de implementación); OQ-30 anotada. T-055 separa requisito a requisito las partes de interpretación y las reglas de coherencia.
- **Relacionado:** D-130, D-143, D-145, D-147.

### D-149

**Sistema references: custodia común de las fuentes externas congeladas.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-references-system`. demand-engine (taxonomías de Shopify, Google y Amazon.es) y web-audit (Schema.org y los documentos de las especificaciones) custodiaban cada uno sus fuentes externas por separado. Contexto añadido por Claude: eran dos almacenes de versiones con dos versiones fijadas, y cuando demand-engine necesite citar fuentes de la referencia técnica ([OQ-76](open-questions.md)) las dos custodias divergirían. Usuario, en la reorganización de las referencias: opción A.
- **Decisión:**
  - Las fuentes externas congeladas por versión viven en un sistema propio de primer nivel, `references/`: registro (`references/sources.json`, con `uses`, los sistemas que usan cada fuente), versiones congeladas fuera de git y desechables (`references/var/`), una sola versión fijada por fuente (`pins.json`), diff entre versiones y lectores por formato.
  - Las fuentes se comparten; su interpretación sigue en cada sistema: el catálogo de bloques y el material de taxonomía, en demand-engine; las fichas de fuente y los requisitos técnicos (la referencia técnica), en `web-audit/reference/`.
- **Interpretaciones adoptadas:**
  - La referencia técnica de D-133 deja de incluir las fuentes congeladas, pero sigue citándolas a la versión fijada (D-132).
  - Lectura de Claude: como la versión fijada es una sola para todos los sistemas, un cambio de versión fijada lo revisa cada sistema de `uses` con lo que interpreta de la fuente.
- **Consecuencias:** enmienda D-133. [evaluation-scopes](../10-model/evaluation-scopes.md#fuentes-de-los-requisitos-técnicos) 1.6 (regla 4); glosario (nueva entrada references; web-audit). Fuera de `docs/`: T-059 (construir y probar `references/`), T-060 (corte de datos y consumidores) y T-061 (propiedades de Google Search para demand-engine).
- **Relacionado:** D-045, D-129, D-132, D-133.

### D-150

**Sistema capture: motor de captura y almacén común de fichas congeladas.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-capture-system`, tareas T-063 (estudio) y T-066. El motor de captura ([D-046](#d-046)) y las fichas congeladas vivían en demand-engine. Contexto añadido por Claude: web-audit ([D-129](#d-129)) también los necesita, porque el contraste de los requisitos técnicos lee fichas congeladas y el auditado técnico tendrá que capturar; es el mismo caso que las fuentes externas, que pasaron a un sistema común ([D-149](#d-149)). Usuario, en el estudio T-063: alternativa B. Descartadas: A (el motor y las fichas siguen en demand-engine y web-audit depende de demand-engine), C (solo el motor en común, con capturas duplicadas por sistema) y D (dentro de references: otra ejecución, otra naturaleza, sin versión fijada).
- **Decisión:**
  - El motor de captura y el almacén de fichas congeladas viven en un sistema propio de primer nivel, `capture/`, compartido por demand-engine, web-audit y la futura auditoría, para que todos evalúen la misma instantánea de una ficha.
  - La captura se comparte; su interpretación sigue en cada sistema.
  - Regla del almacén: un ID que ya tiene ficha se rechaza y la captura nueva lleva otro ID. Nunca se sustituye una ficha congelada.
- **Interpretaciones adoptadas:**
  - Lectura de Claude: un intento de captura rechazado o bloqueado deja su instantánea pero no ficha, así que su ID sigue libre.
  - Las políticas de acceso del motor ([D-042](#d-042), D-046) no cambian: siguen siendo del motor y se aplican igual a todas las capturas, también a las de web-audit y la auditoría.
- **Consecuencias:** enmienda D-046 en dónde vive el motor (el código pasa de demand-engine a `capture/`). [model-training](../10-model/model-training.md#casos-alcance-y-ejecución) 1.21 (motor de captura); glosario (nueva entrada capture; motor de captura); enlaces al README del motor en [sampling-capture](../20-methods/mpir/sampling-capture.md) 1.5, OQ-14 e I-18. Fuera de `docs/`: T-066 (construir y probar `capture/`, sin mover datos ni consumidores: hasta el corte, demand-engine sigue con su copia del motor y sus fichas) y T-067 (corte: mover las fichas y el perfil de Chrome sin volver a capturar ni alterar ninguna ficha, y repuntar los consumidores).
- **Relacionado:** D-042, D-046, D-129, D-149.

### D-151

**Perfil de consumo base de Web: la respuesta HTTP sin ejecutar JavaScript.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-informative-audit-v1` §1, al empezar el sistema de valoración de calidad. El canon pedía que el perfil de consumo no interactivo de Web precisara qué se puede recuperar y leer sin operar la página, sin fijar cuál. Las fichas congeladas de [capture](../../capture/README.md) ([D-150](#d-150)) guardan las dos lecturas posibles: la respuesta HTTP y el DOM tras la carga. Claude propuso la respuesta HTTP como perfil base y el DOM cargado como segundo perfil versionado, más adelante. Usuario: «perfil correcto».
- **Decisión:**
  - El **perfil de consumo base de Web** es la **respuesta HTTP del recurso, sin ejecutar JavaScript** ni operar la página (en capture, `response.html`).
  - El **DOM tras la carga sin interacción** (`dom.html`) queda como posible segundo perfil, versionado, más adelante (retirado por [D-156](#d-156)).
- **Interpretación adoptada:**
  - Claude aplica el mismo perfil a **Web Schema.org**: su marcado es el que trae la respuesta HTTP. Web incluye el marcado, y si los dos ámbitos leyeran representaciones distintas de la misma página, sus resultados no serían comparables. El marcado que se inyecta con JavaScript queda abierto en [OQ-77](open-questions.md#f-evaluación-técnica) (cerrada por [D-156](#d-156)).
  - Es el perfil de consumo de la evaluación informativa (qué información se obtiene y se lee), no el perfil de implementación de la técnica ([D-130](#d-130)). Los perfiles de implementación de Web y de Catálogos distribuidos siguen en [OQ-30](open-questions.md#f-evaluación-técnica).
  - Que un dato solo aparezca tras ejecutar JavaScript no es una prohibición técnica: bajo este perfil, ese dato no es utilizable y su efecto se refleja en la disponibilidad efectiva (caso C de [calibration](../20-methods/audit-gsc/calibration.md#caso-c--ausencia-de-información-pertinente-bajo-el-perfil)).
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#perfil-de-consumo-no-interactivo) 1.7; [inputs-outputs](../20-methods/audit-gsc/inputs-outputs.md#perfil-de-consumo) 0.4; glosario (perfil de consumo); anotaciones en OQ-20 y OQ-30; nueva OQ-77.
- **Relacionado:** D-130, D-150, D-152, D-156.

### D-152

**Ámbitos de la V1 de la auditoría informativa: Web y Web Schema.org.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-informative-audit-v1` §2. Claude propuso Web y Web Schema.org para la V1 y aplazar Catálogos distribuidos, porque no hay feeds con que auditarlo. Usuario: «web + web schema».
- **Decisión:** la V1 de la auditoría informativa examina **Web** y **Web Schema.org**. **Catálogos distribuidos** queda aplazado.
- **Interpretación adoptada:** es un alcance de la V1 del método, no del modelo: Catálogos distribuidos sigue siendo uno de los tres ámbitos ([evaluation-scopes](../10-model/evaluation-scopes.md)). Mientras esté aplazado, la consistencia transversal de la V1 solo examina el par Web ↔ Web Schema.org.
- **Consecuencias:** [audit-gsc](../20-methods/audit-gsc/README.md) 0.3; [inputs-outputs](../20-methods/audit-gsc/inputs-outputs.md) 0.4.
- **Relacionado:** D-013, D-124, D-151.

### D-153

**Ejecución del auditor en dos fases: disponibilidad por ficha × ámbito, AC por lotes.** · propuesta · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-informative-audit-v1` §3. Un modelo de demanda real tiene entre 44 y 72 RI (unos 55 de mediana; recuento de Claude sobre los modelos ensamblados de los 14 casos de control): unos 110 RI × ámbito y hasta 660 juicios de AC por ficha. Claude comparó cinco unidades de trabajo del agente: A, un agente por ficha (salida inmanejable); B, ficha × ámbito en un solo paso (en Web, unos 330 juicios); C, lotes de RI sin fase común (ninguno ve la página entera para probar una ausencia, invariante 11); D, un agente por RI (más de cien agentes por ficha); E, dos fases. Usuario: «2 ok a E».
- **Decisión (propuesta V1):**
  - **Fase 1, un agente por ficha × ámbito:** exploración, pertinencia y disponibilidad efectiva de **todos** los RI (OP-03…07). Mira la página entera una vez y deja la prueba de cobertura de cada ausencia. Los RI con disponibilidad 0 terminan aquí (IR = 0).
  - **Fase 2, agentes por lote de RI con disponibilidad 1** (un bloque o una entidad, unos 10–15 RI): los seis AC con sus pistas (OP-08…10). Reciben las evidencias localizadas y la representación completa del ámbito, para poder reabrir la búsqueda. En Web ven juntos el HTML y el Schema.org.
  - **Entre las dos fases, el código** comprueba que cada fragmento citado existe literalmente en la representación del ámbito.
  - **Mitigación:** un 0 sin registro de cobertura no pasa el validador; la calibración mide sobre todo los falsos 0.
- **Interpretación adoptada:** es una forma admitida de procesar varios RI sobre la misma representación ([execution](../20-methods/audit-gsc/execution.md#orden-de-procesamiento-y-eficiencia)); no cambia la unidad RI × ámbito ni sus registros. Se incorpora como propuesta, como el resto de la V1: el reparto en lotes y su tamaño se ajustan en la calibración.
- **Consecuencias:** [execution](../20-methods/audit-gsc/execution.md#ejecución-en-dos-fases) 0.4; [availability-coverage](../20-methods/audit-gsc/availability-coverage.md) 0.3; [qa](../20-methods/audit-gsc/qa.md) 0.4 (QA-15).
- **Relacionado:** D-152.

### D-154

**Fiabilidad sin fuentes externas y conocimiento del modelo como regla asimétrica.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-informative-audit-v1` §4. [D-122](#d-122) incluía en Fiabilidad una tercera familia, la fuente independiente (registros públicos: OEKO-TEX, EPREL, GS1). Claude propuso limitarla a los registros concluyentes; en 45 fichas congeladas no había ninguna certificación con número ni clase energética, y el GTIN aparecía en 43. Usuario: «no voy a validar certificaciones. Replantea como se evalua este AC». Ante el replanteo, el usuario preguntó: «¿Podrías usar el conocimiento del modelo?». Claude distinguió tres tipos de conocimiento del modelo y propuso una regla asimétrica. Usuario: «OK».
- **Decisión:**
  - **La auditoría no consulta nada externo a lo que publica el ecommerce.** Usa la representación del ámbito y reglas generales citadas: definiciones, normas que fijan el significado de un término y especificaciones de formato. Ningún hecho particular del producto tomado de fuera (un registro, la web del fabricante, lo que el auditor sepa del modelo) entra en la auditoría como regla ni como evidencia, ni siquiera para contrastar; lo que el auditor sepa de un caso concreto solo puede frenar una refutación o quedar como sospecha (regla asimétrica, abajo). Enmienda la frase de [D-120](#d-120) «solo sirve para contrastar».
  - **La definición de Fiabilidad no cambia** ([D-121](#d-121)), ni su escala: 0, defecto material; 1, defecto no material o que afecta a parte de lo examinado; 2, sin defectos detectados. No hay estado nuevo.
  - **Tres familias de comprobación**, que sustituyen a las de D-122: **estructura del dato** (refuta con certeza), **conocimiento del dominio** (solo refuta: una regla general citada y sin contrafuente, o una imposibilidad física o lógica; si el dato solo es improbable, sospecha) y **consistencia dentro del ámbito** (entre las representaciones del ámbito y entre requisitos del mismo ámbito). Desaparece la fuente independiente.
  - **Conocimiento del modelo, regla asimétrica:**

    > El conocimiento del modelo puede **frenar** una refutación libremente, pero solo puede **producirla** con una regla general citada o con una imposibilidad física o lógica. Lo que el modelo sepa de un producto, una marca o un modelo concretos es una **sospecha**: se anota con su motivo, no gradúa y pasa al informe como «a verificar por el ecommerce». — INTAKE 2026-10-28-informative-audit-v1
  - **El registro** dice qué familias se aplicaron: «sin defectos detectados en estructura, dominio y consistencia del ámbito; sin contraste externo». Si a un dato solo le toca la consistencia, también es 2 y el registro lo dice.
  - **Certificaciones:** se juzgan por lo publicado, no se validan. Fiabilidad: solo estructura, dominio y consistencia (una fecha de validez vencida, un sello incompatible con la composición). Justificación: que se publiquen el número y el organismo, porque son la base que permite a cualquiera, IA incluida, verificarlos. Precisión: «OEKO-TEX» sin decir qué norma. Aplicabilidad: que la certificación se atribuya al producto que se vende y no a una materia prima.
  - **Límite de interpretación:** Fiabilidad mide la corrección y la coherencia interna de lo publicado, no su veracidad frente al mundo. Un 2 no acredita que una certificación, una clase energética o un GTIN sean válidos.
- **Motivos de la regla asimétrica** (de la propuesta aceptada): el hecho particular que el modelo «sabe» no es reexaminable (M10); la memoria del modelo puede estar desfasada o confundir versiones, variantes y mercados; el resultado dependería del auditor (M12, invariante 14); trataría distinto a marcas conocidas y desconocidas; un falso 0 daña al cliente sin fundamento; y es el espíritu de la invariante 9 (no se completan hechos ausentes con conocimiento externo; tampoco se destruyen con él). Frenar es seguro: usar lo que el modelo sabe como contrafuente solo evita penalizar.
- **Interpretaciones adoptadas:**
  - La imposibilidad física o lógica es una regla general en el sentido de la [prueba de derivación](../10-model/effective-availability.md#prueba-de-derivación) (lógica, aritmética, hechos generales del mundo); no es un tercer tipo de regla.
  - Con la fuente independiente desaparece el ejemplo de NE «un registro externo que no respondió». En Fiabilidad, NE queda casi limitado a no poder leer una representación que pide la comprobación de consistencia.
  - La falta del identificador que permitiría verificar un dato (el número de certificado) sigue contando en Justificación (P18), como en D-122: la auditoría no lo verifica, pero el identificador es la base que permite verificarlo.
  - La consistencia transversal no es una fuente externa: compara representaciones del propio ecommerce y sigue como dimensión aparte ([D-124](#d-124)).
- **Consecuencias:**
  - Enmienda D-122 (familias y fuente independiente) y D-120 (el hecho particular tomado de fuera ya no contrasta).
  - [acceptance-criteria](../10-model/acceptance-criteria.md#fiabilidad-lectura-refutadora-y-comprobaciones) 1.6; [effective-availability](../10-model/effective-availability.md#prueba-de-derivación) 1.3; [scoring-systems](../10-model/scoring-systems.md) 1.5; [assessment-hints](../10-model/assessment-hints.md) 1.7; [quality-properties](../10-model/quality-properties.md) 1.4; [scope](../00-context/scope.md#límite-de-interpretación) 1.2.
  - Método: [audit-gsc](../20-methods/audit-gsc/README.md) 0.3, [ac-guides](../20-methods/audit-gsc/ac-guides.md) 0.5, [evidence](../20-methods/audit-gsc/evidence.md) 0.3, [property-checks](../20-methods/audit-gsc/property-checks.md) 0.3, [gsc-decision](../20-methods/audit-gsc/gsc-decision.md) 0.5, [qa](../20-methods/audit-gsc/qa.md) 0.4, [calibration](../20-methods/audit-gsc/calibration.md) 0.4, [availability-coverage](../20-methods/audit-gsc/availability-coverage.md) 0.3, [dossier](../20-methods/audit-gsc/dossier.md) 0.3 (sospechas en el informe).
  - Glosario (Fiabilidad, prueba de derivación, sospecha); OQ-66 reducida a las tres familias.
  - Fuera de `docs/` (código, pendiente): en `demand-engine/catalog/hints.json`, retirar PV-5 y PV-39 (el número ha de existir en el registro); retirar PV-6 y PV-40 y reescribirlas como pistas de Aplicabilidad con número nuevo. PV-4 y PV-38 (número de certificado y organismo, Justificación) se mantienen.
- **Relacionado:** D-006, D-119, D-120, D-121, D-122, D-124, D-128.

### D-155

**Un modelo de demanda y una ficha por ámbito: pertinencia por excepción y localización.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-scope-sheet`. Responde a [OQ-76](open-questions.md). Antes de implantar T-056, el usuario pidió analizar críticamente que cada ámbito tenga sus requisitos aplicables y quizá sus pistas, y preguntó si el modelo es uno y lo que cambia es una ficha de aplicabilidad. El canon decía que el catálogo relaciona cada RI con sus ámbitos pertinentes (FUND §3.5) y que cada ámbito tiene su propio conjunto de RI pertinentes (regla 4 de [evaluation-scopes](../10-model/evaluation-scopes.md#reglas-e-invariantes)), pero esa relación no se había registrado ([D-061](#d-061), sustituida por [D-062](#d-062)). Claude comparó tres alternativas: A, un campo de ámbitos en cada RI del catálogo; B, un modelo y una ficha por ámbito; C, sin aplicabilidad. Usuario: «si como dices».
- **Decisión (alternativa B):**
  - **El modelo de demanda es uno.** Preguntas, importancia, información resolutiva y pistas de valoración no dependen del ámbito.
  - **Cada ámbito tiene una ficha propia, versionada,** con dos partes:
    - **Pertinencia:** por defecto, todo RI del modelo es pertinente en el ámbito. Las excepciones son NA fundamentados en la función del ámbito, formulados como reglas (por entidad o componente), no RI a RI. La falta de una propiedad o un campo en el vocabulario del ámbito no es motivo (independencia de un campo o formato, invariante 14). Web no tiene excepciones.
    - **Localización:** el vocabulario del ámbito (por ejemplo, las propiedades de Schema.org, citadas `fuente:Tipo.propiedad@versión`) relacionado con las aportaciones de la información resolutiva. Llega al auditor como expresiones ilustrativas del perfil del RI: orienta, no cierra la búsqueda ni decide la pertinencia.
  - **La auditoría compone modelo × ficha** para obtener las unidades RI × ámbito y registra la versión de la ficha.
  - **Las pistas de valoración siguen sin ámbito:** lo que cambia por ámbito es localización, no valoración.
  - **La no pertinencia, solo a nivel de RI** (la unidad es RI × ámbito): no hay aportaciones no exigibles por ámbito.
  - **Precisa [D-145](#d-145):** una propiedad que un consumidor del perfil de Web Schema.org recomienda sin exigir tiene dos papeles separados: **apoyo de demanda** (origen «referencias», sin ámbito, como los PTD de Amazon, [D-052](#d-052)) y **localizador** en la ficha de Web Schema.org. Desaparece «apoyo del modelo para ese ámbito».
  - Alternativas descartadas: A, un campo de ámbitos en cada RI (reparte el conocimiento del ámbito por todo el catálogo y deja la pertinencia al juicio RI a RI, con la tentación de «hay propiedad, luego es pertinente»); C, sin aplicabilidad (contradice FUND §3.5 donde la función del ámbito sí limita, como en Catálogos distribuidos).
- **Interpretaciones adoptadas:**
  - «El catálogo relaciona cada RI con sus ámbitos pertinentes» (FUND §3.5) se cumple a través de la ficha: la relación es la composición del catálogo con la ficha de cada ámbito, no un campo del catálogo. La regla 4 de evaluation-scopes (cada ámbito tiene su propio conjunto de RI pertinentes) se lee igual.
  - El NA de la ficha es el NA del requisito que ya prevén las AC («un RI que no corresponde a un ámbito», FUND §3.5); no es un estado nuevo.
  - Los motivos de excepción que el artefacto admite son la función del ámbito (fundamentada) y, en parte, la entidad. Claude lo leyó así: la entidad es una forma de formular la regla, y la razón sigue siendo la función.
  - OQ-76 se cierra con esta decisión: vía (referencias como apoyo y ficha de ámbito), mapeo (propiedad → requisito o aportación, o candidato si ninguno la cubre), ámbito pertinente (ficha, por excepción) y versión (citas con `@versión` a la versión fijada compartida en references, comprobadas con `bin/model refs`, [D-149](#d-149)).
  - Dónde vive la ficha y su formato son de implantación (T-056), no de canon.
  - Implantación (T-056): una cuestión o aportación de la capa general que era inferida y gana su primer apoyo de referencia pasa a «referencias», como manda D-052 («según su origen»): disponibilidad (gen/06), estado de la unidad (gen/07), opiniones (gen/15) y promociones (gen/16). Las propiedades que no cubre ningún requisito ni aportación quedan como candidatos (programa de fidelización, origen del envío) o descartadas con su motivo (número de ofertas; modelo 3D y logotipo, por D-144).
  - Que la localización no decida la pertinencia se apoya, en lectura de Claude, en la invariante 10 (pertinencia ≠ proximidad temática): una propiedad cercana no prueba que su valor responda al RI.
- **Consecuencias:** precisa D-145; cierra OQ-76. [demand-model](../10-model/demand-model.md#relación-con-los-ámbitos-de-evaluación) 3.7; [evaluation-scopes](../10-model/evaluation-scopes.md) 1.8; [construction-routes](../10-model/construction-routes.md) 1.8; [assessment-hints](../10-model/assessment-hints.md) 1.8; método: [inputs-outputs](../20-methods/audit-gsc/inputs-outputs.md) 0.5 y [ri-profile](../20-methods/audit-gsc/ri-profile.md) 0.3; glosario (nueva entrada Ficha de ámbito); [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.33. Fuera de `docs/`: T-056 (ficha de Web Schema.org y apoyo «referencias» en demand-engine).
- **Relacionado:** D-010, D-052, D-062, D-135, D-145, D-149, D-152, OQ-76.

### D-156

**Un solo perfil de consumo: sin JavaScript y con todo el documento.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-single-consumption-profile`, tras la investigación «Perfil de consumo de agentes IA» (informe en `reports/`). La investigación encontró dos vías de lectura: la lectura en vivo de los asistentes pide el HTML sin ejecutar JavaScript y casi siempre lo reduce a texto visible, de modo que el JSON-LD casi nunca llega al modelo; la vía de índice puede renderizar (Google siempre, Bing a veces, OpenAI quizá). Propuso dos perfiles (A: respuesta HTTP; B: DOM tras la carga) y señaló una tensión: Web es HTML + Schema.org, pero la lectura en vivo solo entrega el texto visible. Usuario: «vamos dejar solo un perfil que no ejecuta js y utiliza todo el DOM» y «Nos basamos en que es más compatible y preferible generalmente que la información no dependa de ejecución de javascript (aunque algunos sistemas sí puedan leerla). Es una condición que decidimos adoptar ahora.»
- **Decisión:**
  - Web y Web Schema.org tienen **un solo perfil de consumo**: la respuesta HTTP **sin ejecutar JavaScript**, de la que se usa **todo el documento**, no solo el texto visible.
  - **Fundamento:** es más compatible, y es preferible en general que la información no dependa de ejecutar JavaScript, aunque algunos sistemas sí puedan leerla. Es una **condición adoptada** por el proyecto, no una afirmación de que ningún sistema de IA ejecute JavaScript.
  - Enmienda [D-151](#d-151): desaparece el DOM tras la carga como posible segundo perfil.
- **Interpretaciones adoptadas:**
  - Lectura de Claude: «todo el DOM» es el documento de la respuesta HTTP analizado sin ejecutar JavaScript (en capture, `response.html`), no el DOM tras la carga (`dom.html`), que exige ejecutarlo. Incluye el texto visible, los atributos y el marcado (JSON-LD, microdatos, RDFa) y `<noscript>`.
  - Según Claude, así se resuelve la tensión de la investigación: Web sigue siendo HTML + Schema.org y cuenta todo el documento; que la lectura en vivo de un asistente reduzca la página a texto visible no excluye el marcado de Web. Web Schema.org sigue limitado al marcado ([D-010](#d-010) y [evaluation-scopes](../10-model/evaluation-scopes.md)).
  - Lo que solo aparece al ejecutar JavaScript, incluido el marcado inyectado, no es utilizable bajo el perfil: su efecto se refleja en la disponibilidad efectiva. Cierra [OQ-77](open-questions.md#f-evaluación-técnica).
  - Los datos que la página lleva dentro de scripts que no son marcado (el estado de la aplicación en JSON, variables de JavaScript) están en el documento, pero leerlos como información comercial es otra cuestión: queda en [OQ-79](open-questions.md#d-auditoría-informativa-localización-evidencias-gsc).
  - El usuario no se pronunció sobre el contexto de la petición que señaló la investigación (estado, `Accept-Language`, IP de origen, user agent, robots.txt, sondas): queda en [OQ-78](open-questions.md#d-auditoría-informativa-localización-evidencias-gsc).
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#perfil-de-consumo-no-interactivo) 1.9; [inputs-outputs](../20-methods/audit-gsc/inputs-outputs.md#perfil-de-consumo) 0.6; glosario (perfil de consumo); OQ-77 cerrada; anotación en OQ-20; nuevas OQ-78 y OQ-79.
- **Relacionado:** D-010, D-151, D-152, D-155.

### D-157

**Contexto de la petición del perfil de consumo y datos en scripts que no son marcado.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-request-context-and-scripts`. Cierra [OQ-78](open-questions.md#d-auditoría-informativa-localización-evidencias-gsc) y [OQ-79](open-questions.md#d-auditoría-informativa-localización-evidencias-gsc), abiertas por [D-156](#d-156). Claude vio que el motor de captura está hecho para parecer un Chrome corriente y evitar bloqueos (perfil persistente, user agent real, `es-ES`, sin banderas de automatización; políticas de [D-042](#d-042) y [D-046](#d-046)). Propuso separar cómo se obtiene la ficha (el motor) de qué contexto de petición define la representación, y corregir solo lo que sesga el resultado y es barato. Usuario: «si. matiz sobre el perfil. Mantenemos el navegador real para evitar bloqueos. pero es un navegador que no ejecuta js.»
- **Decisión:**
  - **El perfil es un navegador real que no ejecuta JavaScript.** Navegador real, para evitar bloqueos; sin ejecutar JavaScript, como fija D-156.
  - **Contexto de la petición:**
    - **Estado limpio por ficha:** antes de cada captura se borran las cookies y el almacenamiento del dominio, y nunca se acepta un banner (precisado por [D-163](#d-163): un contexto de navegador nuevo por ficha). Un desafío es una incidencia, no una ausencia; el efecto en la tasa de desafíos se mide en el piloto.
    - **`Accept-Language: es-ES`**, registrado en la ficha.
    - **IP de origen en España**, con su país y su ASN registrados; sin proxies.
    - **User agent: el real del navegador.** No se reabren D-042 ni D-046: un token propio aumenta los bloqueos, y suplantar a un bot desde una IP que no es suya es un bot falso para el WAF.
    - **robots.txt por bot**, registrado en la ficha (GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Googlebot, Google-Extended, Bingbot y los de Meta y Amazon) como hecho técnico. No afecta al GSC (invariante 8).
    - **Sin sondas** desde EE. UU. ni con `en-US`. Si un cliente vende fuera de España, se añadirá un perfil nuevo.
  - **Datos en scripts que no son marcado** (el estado de la aplicación en JSON, variables de JavaScript): **no cuentan como información**. No dan disponibilidad ni sirven de base a los AC. Solo sirven de diagnóstico: si el dato existe ahí pero no en el HTML ni en el marcado, se registra como hallazgo («el dato existe en el estado de la aplicación, pero no se publica»).
  - **Frontera del documento:** cuentan el texto del HTML (también el oculto), los atributos y el marcado. De los scripts, solo `application/ld+json`.
- **Motivos** (de la propuesta aceptada): el comprador español es el perímetro; todas las IA llegan sin estado, y el consentimiento heredado es el sesgo más claro; los navegadores agénticos envían el idioma y la IP del usuario; omitir `Accept-Language` exige interceptar peticiones y es una señal de bot; una IP de EE. UU. exige proxy y podría auditar otra tienda. Los scripts que no son marcado son estructuras internas para JavaScript, con claves sin significado publicado; las lecturas en vivo los descartan, y contarlos contradiría el fundamento de D-156. Descartadas en OQ-79: contarlos como información (A) y decidir caso a caso (C, contra M10).
- **Interpretaciones adoptadas:**
  - Claude lee el matiz del usuario como una condición sobre la lectura: la representación es la de un navegador real (su user agent, sus cabeceras) que no ejecuta JavaScript. Cómo lo cumple el motor de captura no lo decidió el usuario. Hoy Chrome ejecuta JavaScript al cargar, y desactivarlo puede impedir pasar desafíos antibot, así que queda en [OQ-80](open-questions.md#d-auditoría-informativa-localización-evidencias-gsc).
  - El hallazgo de diagnóstico de los scripts no es un estado nuevo: es un hallazgo del expediente ([dossier](../20-methods/audit-gsc/dossier.md#diagnóstico)).
  - Es coherente con el caso C de [calibration](../20-methods/audit-gsc/calibration.md#caso-c--ausencia-de-información-pertinente-bajo-el-perfil): un contenedor vacío en el HTML da disponibilidad 0 aunque el dato esté en el estado de la aplicación.
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#perfil-de-consumo-no-interactivo) 2.0; [inputs-outputs](../20-methods/audit-gsc/inputs-outputs.md#perfil-de-consumo) 0.7; [dossier](../20-methods/audit-gsc/dossier.md#diagnóstico) 0.4; glosario (perfil de consumo); OQ-78 y OQ-79 cerradas; nueva OQ-80. Fuera de `docs/` (código de capture, pendiente): estado limpio por ficha, registro de `Accept-Language`, IP, país y ASN, y matriz de robots.txt por bot.
- **Relacionado:** D-042, D-046, D-150, D-156.

### D-158

**Catálogo de entrenamiento curado: candidatos, filtros, motivos de admisión, topes y casos manuales.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-curated-training-catalog`. Tras la idea de entrenar con los modelos de una auditoría completa ([OQ-81](open-questions.md#b-taxonomía-de-clases-de-producto)), el usuario propuso «mantener un catálogo de casos relevantes para entrenamiento», al que cada caso evaluado puede entrar como candidato si el sistema lo considera y al que él puede añadir casos a mano, para «basarnos en un catálogo curado, no en cualquier ficha que hayamos auditado». Claude lo revisó y propuso criterios. Ante la pregunta de si lo llevaba al canon y las tres confirmaciones (topes de partida de 3 y 1, conservar las fichas del catálogo y poder retirar a mano los casos manuales), el usuario respondió «sí».
- **Decisión:**
  - El entrenamiento solo aprende del **catálogo de entrenamiento**, en git y con versión. Se entra por la selección inicial ([D-053](#d-053)), por un caso evaluado (auditoría o `/demand-model`) que el sistema admite o por un caso que el usuario añade a mano. Una ficha evaluada es candidata, no caso.
  - **Filtros:** validez (F1), ficha de producto (F2), sin duplicados por tienda y clave (F3) y topes (F4): de partida, 3 por clase y 1 por tienda y clase, parámetros del usuario.
  - **Motivos de admisión:** clase poco representada (A1), algo no compilado (A2), contradicción de una regla compilada (A3), huecos de cobertura (A4), tienda nueva para la clase (A5) y composición nueva (A6). Entra el candidato que pasa los filtros y aporta al menos uno.
  - **Clase en su tope:** solo entra lo que aporta A2 o A3, sustituyendo a un caso que no aporte nada de eso; el sustituido se retira con registro, sin borrarse.
  - **Casos manuales:** pasan F1 y F2, sin topes, con origen «manual» y un motivo; el usuario puede retirarlos a mano.
  - **Registro de cada caso:** origen, motivo, fecha, tienda, clave de entrada y versión del reglamento.
  - **Conservación:** las fichas congeladas de los casos del catálogo se conservan.
  - Enmienda el paso 1 del entrenamiento y la conexión «la ejecución deja en la cola […] y el entrenamiento lo convierte en casos» de [D-044](#d-044) ([model-training](../10-model/model-training.md#entrenamiento)): lo evaluado, también lo encolado, es candidato.
- **Interpretaciones adoptadas:**
  - El «sí» del usuario aprueba la decisión y las tres confirmaciones.
  - **Admisión:** la decide el sistema («si el sistema lo considera»); el usuario solo añade y retira casos manuales.
  - **Casos manuales y F3:** el artefacto dice «salvo el último» en los filtros (F1 a F3) y «pasan F1 y F2» en los casos manuales. El canon recoge F1 y F2 y deja F3 sin decidir ([OQ-83](open-questions.md#b-taxonomía-de-clases-de-producto)).
  - **Retirada a mano:** el usuario confirmó que puede retirar los casos manuales. Si puede retirar también los que admitió el sistema queda sin decidir (OQ-83).
  - **Conservación:** afecta solo a las fichas del catálogo. El resto de `capture/var/` sigue siendo desechable ([D-150](#d-150)).
  - **Lecturas de Claude, no confirmadas por el usuario,** que el módulo marca como propuesta (OQ-83): la clase de los topes es cada categoría de Shopify de la composición (un juego cuenta en cada una); la admisión ocurre al reunir los casos y un caso retirado deja de aportar votos; se sustituye el más antiguo de los que no aportan A2 ni A3, nunca un caso manual; la selección de D-053 entra tal cual y los topes rigen para los candidatos.
- **Consecuencias:** módulo nuevo [training-catalog](../10-model/training-catalog.md) 1.0; [model-training](../10-model/model-training.md#casos-alcance-y-ejecución) 1.22 (citas anotadas y el catálogo pasa al módulo nuevo); glosario (catálogo de entrenamiento); índice de `docs/`. OQ-81, punto 1 cerrado (los topes F3 y F4 sustituyen el voto por tienda) y punto 4 reformulado; OQ-48 anotada; nuevas [OQ-82](open-questions.md#b-taxonomía-de-clases-de-producto) (fichas de clientes) y OQ-83 (lecturas propuestas y lo no decidido). Fuera de `docs/` (código de demand-engine y capture, pendiente): registro del catálogo, admisión en `bin/train`, casos manuales y conservación de sus fichas.
- **Relacionado:** D-044, D-045, D-053, D-054, D-063, D-150, OQ-48, OQ-81.

### D-159

**Perfil de implementación de Web: protocolo, documento y consumidor (Google Search y operadores de IA).** · aceptada (enmendada por [D-168](#d-168)) · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-web-implementation-profile` §1, §2, §4 y §5, tarea T-072. El usuario pidió construir los requisitos técnicos de «todo el recurso web» sobre un documento base de 19 requisitos (RT-HTML-01…14, RT-WEB-15…19; anexo A del artefacto). El canon solo tenía el perfil de Web Schema.org ([D-130](#d-130)); el de Web seguía en [OQ-30](open-questions.md#f-evaluación-técnica), y según [D-133](#d-133) lo fija el usuario. Claude comprobó en origen el texto de las fuentes candidatas y propuso un perfil de tres niveles y el reparto de los 19 RT. Usuario: consumidor «Google Search y operadores de IA» (Claude recomendaba solo Google Search) y «Apruebo».
- **Decisión:**
  - **Perfil de implementación de Web**, tres niveles:
    - **Protocolo:** HTTP Semantics (RFC 9110) y Robots Exclusion Protocol (RFC 9309): la respuesta (estado, redirecciones, `Content-Type`, `Content-Encoding`) y cómo se leen las reglas de robots.txt.
    - **Documento:** HTML (WHATWG Living Standard: sintaxis, codificación de caracteres, enlaces y errores de análisis) y Encoding (WHATWG): la codificación declarada y UTF-8, la sintaxis del documento y la forma de los enlaces.
    - **Consumidor:** Google Search (requisitos técnicos de Search Essentials, enlaces rastreables, robots.txt, meta robots y `X-Robots-Tag`, bloqueo de la indexación, códigos de estado HTTP, redirecciones, tipos de fichero indexables, JavaScript y las directrices generales de datos estructurados, para la presencia del marcado) y los **operadores de IA** OpenAI, Anthropic y Perplexity, cada uno con su página de bots: lo que el consumidor exige o recomienda para rastrear, indexar o recuperar la página.
  - Como en Web Schema.org, la naturaleza la fija la especificación: un operador de IA da requisito solo donde su página dice must, should o recommend.
  - El marcado Schema.org se examina en Web solo por su **presencia**; su sintaxis, estructura y conformidad son de Web Schema.org.
- **Interpretaciones adoptadas:**
  - Amplía [D-132](#d-132): las especificaciones aplicables son de serialización, de vocabulario, de protocolo, de documento o de un consumidor, según el perfil del ámbito.
  - El reparto de los 19 RT (§2 del artefacto) es contenido de la referencia técnica, que deciden los agentes ([D-133](#d-133)); el canon recoge solo por qué seis no dan requisito, porque se sigue del propio canon: el RT-06 (condiciones de solicitud) es el [perfil de consumo](../10-model/evaluation-scopes.md#perfil-de-consumo-no-interactivo) ([D-157](#d-157)), la condición de todas las comprobaciones; el RT-10 (DOM utilizable) es una condición previa, porque un analizador HTML conforme siempre da un DOM (si no se obtiene el documento, es NE común); los RT-12, 13 y 14 (JavaScript, recursos dependientes, interacción) se siguen del perfil único sin JavaScript ni operación de la página ([D-156](#d-156)): el 12 se reduce al 11, el 13 nunca se aplica y lo que exige interactuar tiene efecto informativo; y el RT-01 (direccionabilidad) no tiene texto con must ni should (Google solo dice «Don't use fragments»), y el recurso se pide por su URL.
  - Lo que dice D-130 de no añadir otros consumidores vale para Web Schema.org. En Web, los operadores de IA son los tres que nombró la propuesta. Lectura de Claude, por analogía con D-130: otros se añadirían como perfil nuevo.
  - El **mínimo de representación de Web**, que [D-147](#d-147) dejaba para cuando se fijara su perfil, no se decidió: queda en [OQ-84](open-questions.md#f-evaluación-técnica).
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#perfil-de-implementación) 2.1; glosario (perfil de implementación, especificación aplicable); OQ-30 anotada; nueva OQ-84. Fuera de `docs/` (T-072): en la referencia técnica de web-audit, el ámbito `Web`, sus niveles, un fichero por nivel e ids `w-<nivel>/NNN`, y la validación de la naturaleza acepta «requirement(s)» como término de lo obligatorio (Search Essentials dice «minimum technical requirements»); registrar en references las fuentes del perfil (pendiente, T-072). En capture (T-069): los bytes originales del cuerpo (hasta entonces, la codificación real y el BOM son NE) y robots.txt por bot.
- **Relacionado:** D-130, D-132, D-133, D-147, D-156, D-157, D-160, OQ-30, OQ-84.

### D-160

**Frontera entre la evaluación técnica y la informativa en Web.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-web-implementation-profile` §2 (nota del RT-11) y §3. La frontera de [D-145](#d-145) se formuló para el perfil de Web Schema.org, donde lo que el consumidor solo recomienda suele ser otro hecho comercial. En Web, las recomendaciones del consumidor son sobre el acceso y la forma (permitir un bot en robots.txt, enlaces `<a href>`).
- **Decisión:**
  - **Técnico** en Web: el acceso y la recuperación del recurso, la forma de la respuesta y del documento, y la presencia de lo que el consumidor exige para la página (no bloqueado, 200, contenido indexable, marcado). Las recomendaciones del consumidor sobre el acceso y la forma son técnicas: no añaden un hecho comercial.
  - **Informativo:** si la información comercial pertinente está en el documento y se puede leer (disponibilidad efectiva y AC). Que haya contenido indexable es técnico; que ese contenido sea la información comercial, no.
- **Interpretaciones adoptadas:**
  - La «lectura» que [evaluation-scopes](../10-model/evaluation-scopes.md#ámbitos-de-evaluación) cuenta entre las áreas técnicas de Web es la del documento (tipo, codificación, análisis); si se puede leer la información comercial es de la informativa.
  - Es la lectura de D-145 en Web, no una excepción: D-145 lleva a la informativa la presencia de lo recomendado porque añade otro hecho, y una recomendación de acceso o de forma no lo añade (como la forma de lo recomendado, que D-145 ya deja en la técnica).
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#frontera-entre-la-evaluación-técnica-y-la-informativa) 2.1.
- **Relacionado:** D-145, D-147, D-148, D-159.

### D-161

**Vistas general y particular de la evaluación técnica; tipos de página.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-technical-views-and-sitemaps` §1, tarea T-074. Tras el triaje de Web, el usuario propuso una «evaluación técnica con una visión general (aquellos que aplican de forma general) y con una visión particular (aquellos que aplican al caso (página de producto, categoría, página de contenido, etc.))». Claude propuso las dos vistas, los tipos de página y tres formas de marcarlas. Usuario: «Sí, opción A».
- **Decisión:**
  - **Vista general:** lo que se evalúa una vez por sitio u origen, sus recursos de sitio y las entidades de nivel de sitio. Ejemplos: robots.txt (estado y forma del fichero, campo `sitemap:` y política por bot) y los sitemaps (su forma); en Web Schema.org, la organización y sus políticas.
  - **Vista particular:** lo que se evalúa en cada página auditada, según su tipo.
  - **Tipos de página:** ficha de producto, categoría o listado, políticas y contenido (envíos, devoluciones, contacto, aviso legal) y portada.
  - Cada requisito técnico dice su vista y, si es particular, los tipos de página a los que se aplica (opción A: un campo en cada requisito).
  - Valen para Web y Web Schema.org, y para Catálogos distribuidos cuando tenga perfil (el feed frente al artículo).
  - La vista general se acota al descubrimiento y al acceso de las páginas que llevan la información comercial. Sigue sin ser una auditoría integral del rastreo.
- **Interpretaciones adoptadas:**
  - La vista es una dimensión del requisito técnico, no un ámbito ni un perfil. No cambia la unidad (requisito técnico × ámbito), los estados ni el perfil de implementación.
  - La evaluación informativa sigue partiendo de la ficha de producto. Qué páginas de cada tipo entran en una auditoría no lo decidió el usuario: queda en [OQ-85](open-questions.md#f-evaluación-técnica).
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#vistas-de-la-evaluación-técnica) 2.2 (sección nueva y regla 7); glosario (vista de la evaluación técnica, tipo de página); nueva OQ-85. Fuera de `docs/` (T-074): campos `view` y `page_types` en la referencia técnica y su validación; capture tendrá que congelar robots.txt, los sitemaps y las páginas de cada tipo.
- **Relacionado:** D-129, D-131, D-159, D-162, OQ-85.

### D-162

**Descubribilidad: toda página auditada está en los sitemaps (condición del proyecto).** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-technical-views-and-sitemaps` §2 y §3. El usuario pidió considerar «sitemaps.xml» para el descubrimiento. Claude comprobó que las fuentes fijan la forma de un sitemap publicado (sitemaps.org, Google) y la del campo `sitemap:` de robots.txt, pero que ninguna exige ni recomienda tener uno. Usuario: «lo que fijan las fuentes. Pero añado un criterio nuestro. Toda página que se audita debe estar en el sitemaps. lo asumo como requisito de descubribilidad.» Sobre los enlaces internos: «No, solo sitemaps».
- **Decisión:**
  - De los sitemaps entran como requisitos técnicos los de forma que fijan las fuentes, con su naturaleza.
  - **Condición del proyecto:** toda página que se audita debe estar en los sitemaps del sitio. Es un requisito técnico de descubribilidad, obligatorio.
  - Sin sitemap, ninguna página está en él. No hay un requisito aparte de existencia.
  - Los enlaces internos no se auditan: el bloque «rastreo del sitio» del triaje de Web sigue fuera.
  - **Enmienda [D-132](#d-132):** un requisito técnico lo funda una especificación aplicable o, por excepción, una condición del proyecto adoptada en el canon, que fija su naturaleza y que el requisito nombra en lugar de una cita.
- **Interpretaciones adoptadas:**
  - «Debe estar» fija la naturaleza obligatoria.
  - Es una condición adoptada, como el perfil sin JavaScript ([D-156](#d-156)). No afirma que los sistemas de IA lean los sitemaps.
  - **Lectura de Claude, no confirmada por el usuario:** lo evalúa la vista particular, porque se evalúa en cada página auditada, aunque su evidencia sean recursos de sitio, y se aplica a todos los tipos de página.
  - «Los sitemaps» son los que publica el sitio. Cuáles cuentan (los que declara robots.txt, el de la raíz, los índices de sitemaps) es método de la referencia técnica.
  - **Lectura de Claude, no confirmada por el usuario:** «lo que fijan las fuentes» amplía el perfil de Web ([D-159](#d-159)). El protocolo de sitemaps (sitemaps.org) entra en el nivel protocolo, y la guía de sitemaps de Google en el consumidor.
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#vistas-de-la-evaluación-técnica) 2.2 («Fuentes de los requisitos técnicos», puntos 1 y 3, y regla 7); glosario (requisito técnico general, condición del proyecto). Fuera de `docs/` (T-074): fuentes de los sitemaps, sus requisitos y el campo del requisito que nombra la decisión.
- **Relacionado:** D-132, D-156, D-159, D-161. (D-159 queda ampliada en su perfil: sitemaps.org y la guía de sitemaps de Google.)

### D-163

**Cómo cumple la captura el perfil de consumo: JavaScript desactivado y un contexto de navegador nuevo por ficha.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-capture-profile-no-js`, tarea T-069. Cierra [OQ-80](open-questions.md#d-auditoría-informativa-localización-evidencias-gsc). Claude propuso tres vías para que el motor de captura cumpliera «navegador real que no ejecuta JavaScript» ([D-157](#d-157)):
  - A: desactivar JavaScript en Chrome;
  - B: cargar con JavaScript y leer la respuesta HTTP;
  - C: A y, solo ante un desafío, un intento con JavaScript para que se resuelva, con recarga sin él.

  Recomendó A, medir la tasa de desafíos y añadir C solo si los datos lo piden. Usuario: «A, y C si hace falta». Para el estado limpio por ficha, propuso un contexto de navegador nuevo por ficha, y el usuario lo eligió. Sobre una IP de origen no española o que no se pueda comprobar, el usuario dijo: «ignora lo de la ip. no hace falta que lo tengas en cuenta».
- **Decisión:**
  - **El navegador real no ejecuta JavaScript:** el motor de captura lo desactiva en Chrome (vía A). Un desafío que exige JavaScript no se pasa: es una incidencia, no una ausencia, como fija D-157.
  - **La vía C (JavaScript solo para resolver un desafío) se añadirá solo si la tasa de desafíos lo pide.** Datos del lote de prueba (22 portadas de tiendas españolas, una visita por perfil, 2026-10-28): con este perfil, 1 desafío de 22 (DataDome, 403 con CAPTCHA en la primera respuesta, antes de que pudiera ejecutarse JavaScript; C no lo resolvería); con el Chrome persistente con JavaScript del motor, 0 de 22. Con estos datos, C no se adopta.
  - **Estado limpio por ficha:** cada ficha se captura en un **contexto de navegador nuevo**, que se desecha al terminar: sin cookies, almacenamiento ni caché de ningún sitio, y sin consentimiento heredado. Precisa el «se borran las cookies y el almacenamiento del dominio» de D-157, de forma más estricta.
- **Motivos** (de la propuesta aceptada): con A, lo que se lee es lo que recibe un navegador real que no ejecuta JavaScript. Con B, una navegación, una recarga o las cookies hechas por JavaScript cambian sin rastro el documento leído. El contexto nuevo no deja estado de ningún sitio y no toca el perfil persistente que usan otras capturas; su riesgo, que un antibot lo detecte, se ve en la tasa de desafíos.
- **Interpretaciones adoptadas:**
  - Lectura de Claude sobre la IP: la IP de origen, su país y su ASN **se registran**, como pide D-157, pero **no se comprueban** ni condicionan la captura.
  - En el motor de captura, este perfil es un **perfil de captura** con nombre, distinto del perfil de siempre (el que se usa por defecto), que no cambia. Es implementación de capture, no un concepto del canon ([capture/README.md](../../capture/README.md#perfiles-de-captura)).
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#perfil-de-consumo-no-interactivo) 2.3; [inputs-outputs](../20-methods/audit-gsc/inputs-outputs.md#perfil-de-consumo) 0.8; glosario (perfil de consumo); OQ-80 cerrada. Fuera de `docs/` (T-069, hecho): el perfil de captura `audit-es` de capture.
- **Relacionado:** D-042, D-046, D-150, D-156, D-157, D-159.

### D-164

**Las unidades de un conjunto no son partes de la cuestión: las valoran los AC.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-shipping-zones`, tarea T-076. El usuario pidió tratar de forma específica las zonas de envío de España, «tanto si se envía como si no». Claude propuso primero requisitos por zona. El usuario dudó: «Tanta especificidad me hace dudar si debería ser un requisito general único de envío y modular el cumplimiento a través de los AC […] No puedo crear un requisito para cada tipo; ¿es más bien si se puede determinar por precisión? Quizás es una cuestión de reformular la pregunta». Claude comparó las dos vías y recomendó un requisito con el conjunto explícito. Usuario: «todo si».
- **Decisión:** precisa la regla 3 de [D-060](#d-060), ampliada en la capa general por [D-065](#d-065).
  - **Partes de la cuestión:** necesidades distintas (el precio y el coste del envío; el plazo y el coste de una devolución). Las sigue dividiendo la regla 3.
  - **Unidades de un conjunto:** la misma necesidad repetida sobre varios destinos, modalidades de entrega, variantes o momentos del pedido. No son partes y **no se divide por ellas**. El requisito declara su conjunto (en la pregunta o en la descripción) y lo valoran los AC:
    - **Concreción:** la cobertura de las unidades;
    - **Aplicabilidad:** la atribución de cada valor a su unidad;
    - **Precisión:** el significado de lo expresado («nacional», «24/48 h»).
  - Es el tratamiento que el canon ya daba a las variantes: «¿Qué variantes están disponibles?» es un solo requisito, y la falta de una talla es Concreción 1 y Aplicabilidad 1 ([ejemplo mínimo](../10-model/acceptance-criteria.md#ejemplo-mínimo-hipotético); RI-02 y GSC-09).
- **Severidad asumida:** el silencio sobre una unidad del conjunto es cobertura parcial (Concreción), no disponibilidad 0 del requisito. La frontera 0/1 de Concreción depende de la prueba de materialidad ([OQ-22](open-questions.md)).
- **Interpretación adoptada:** la regla vale para cualquier requisito, no solo para la capa general; el intake la formula en general («las unidades de un conjunto […] no son partes de la cuestión»).
- **Consecuencias:** [acceptance-criteria](../10-model/acceptance-criteria.md#unidades-de-un-conjunto) 1.7; [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formulación-de-las-cuestiones) 1.34; anotación en OQ-22. Aplicación en la capa general: [D-165](#d-165).
- **Relacionado:** D-060, D-065, D-117, D-165.

### D-165

**Envío y plazos por zona de España en la capa general; impuestos y aduana de Canarias, Ceuta y Melilla.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-shipping-zones`, tarea T-076. Aplica [D-164](#d-164) al envío. Canarias está fuera del territorio del IVA; Ceuta y Melilla, fuera del IVA y del territorio aduanero de la UE (Ley 37/1992, art. 3; Directiva 2006/112/CE, art. 6; Reglamento (UE) 952/2013, art. 4): allí el precio con IVA no es el que se paga. El art. 97.1.e TRLGDCU exige el precio total «incluidos los impuestos y tasas» y «cualquier otro gasto».
- **Decisión:**
  - **`gen/25` se reformula:** «¿A qué zonas de España se envía y cuánto cuesta el envío a cada una?». El conjunto, en su descripción: Península, Baleares, Canarias, y Ceuta y Melilla. La información resolutiva lleva el coste de cada zona como componente, y el requisito, una pista de Aplicabilidad: un coste vale solo para la zona a la que se atribuye.
  - **Requisito condicionado nuevo,** si se envía a Canarias, Ceuta o Melilla: «¿Qué impuestos y gastos de aduana asume el comprador en los envíos a Canarias, Ceuta y Melilla?». Origen normativa (97.1.e), con apoyo en las tres normas territoriales. **Crítico**, por el mismo argumento con el que [D-038](#d-038) hizo crítico el envío: forma el precio total. Impuestos y aduana son otra parte de la cuestión, no una unidad del conjunto.
  - **`gen/08` se reformula:** «¿En qué plazo se entrega, según la zona y la modalidad de entrega?». Conjunto: destino, modalidad, variante o disponibilidad y momento del pedido. Pistas de Precisión: envío no es entrega; días hábiles o naturales; desde cuándo cuenta el plazo.
  - **Candidatos del mismo criterio:** `gen/26` (coste de devolver desde las islas) y `gen/09` (recogida solo en la Península), sin crear requisitos ([OQ-86](open-questions.md)).
- **Interpretaciones adoptadas:**
  - El requisito condicionado va en un bloque condicionado propio, `gen.envio-canarias-ceuta-melilla`, de alcance oferta: su disparador es un hecho de la oferta ([D-047](#d-047), [D-066](#d-066)) y entra en la aplicación.
  - Ceuta y Melilla son una sola zona del conjunto, como en el intake; tienen el mismo régimen.
  - La importancia de `gen/25` (crítico) y de `gen/08` (principal) no cambia: el intake no la toca.
  - El conjunto vive en la descripción de cada requisito ([D-092](#d-092)). En el catálogo ningún requisito la llevaba aún (comprobado en `demand-engine/catalog/`); estos tres son los primeros.
- **Consecuencias:** [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.34; [demand-model](../10-model/demand-model.md) (aplicación); glosario (aplicación); OQ-86. Fuera de `docs/` (T-076): `demand-engine/catalog/gen.json` 0.9; reglamento del clasificador (paso 6); localización de la ficha de Web Schema.org; normas registradas en `references/` (`es-liva`, `eu-dir-2006-112`, `eu-reg-952-2013`).
- **Relacionado:** D-038, D-060, D-065, D-066, D-092, D-155, D-164.

### D-166

**Tasa de cumplimiento técnico: una sola tasa con desglose por naturaleza y cobertura; agregación por tipo de página.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-technical-rate-pages-web-minimum` §1 y §2, tarea T-077. El sistema cuantitativo técnico seguía abierto en [OQ-30](open-questions.md#f-evaluación-técnica) ([D-131](#d-131)). Claude propuso cuatro formas (dos tasas sin tasa conjunta, dos tasas y un estado «conforme», una tasa con desglose, sin tasa) y tres de agregación. Usuario: «Una tasa y desglose» y «Por tipo de página».
- **Decisión:**
  - **Una sola tasa por ámbito y vista:** satisfechos / evaluados, con evaluados = pertinentes − NA − NE. Obligatorias y recomendadas entran **sin pesos**: cada requisito cuenta uno.
  - **Desglose obligatorio** por naturaleza (obligatorias, recomendadas), con el mismo cálculo en cada parte.
  - **Cobertura al lado:** evaluados / pertinentes. NE es una incidencia: no entra en el denominador y se informa en la cobertura.
  - **Sin umbrales** ni estados derivados de la tasa.
  - **Vista particular:** la tasa de un tipo de página cuenta los casos requisito × página; además, por requisito, la proporción de páginas del tipo en que se satisface (sobre las páginas en que se evaluó), y el resultado de cada página. La vista general se evalúa una vez por sitio y da su propia tasa.
  - Web y Web Schema.org no se suman ni se promedian.
- **Interpretación adoptada:** «pertinentes» son los requisitos del perfil del ámbito que corresponden a la vista y al tipo de página; NA los separa de los pertinentes, como ya decía el canon. La tasa de un tipo de página no se combina con la de la vista general ni con la de otro tipo: el artefacto no lo pide. Con la tasa fijada, de OQ-30 solo queda el perfil de Catálogos distribuidos: los requisitos concretos, su método y su evidencia viven en la referencia técnica, que deciden los agentes ([D-133](#d-133)), y la cobertura es la de la tasa.
- **Consecuencias:** [scoring-systems](../10-model/scoring-systems.md#tasa-de-cumplimiento-técnico) 1.6; [evaluation-scopes](../10-model/evaluation-scopes.md#estados-del-requisito-técnico) 2.4; glosario (tasa de cumplimiento técnico); OQ-30 anotada (queda el perfil de Catálogos distribuidos). Fuera de `docs/`: el auditor de web-audit (T-049) calcula la tasa así.
- **Relacionado:** D-017, D-131, D-161, OQ-30.

### D-167

**Páginas de una auditoría: fichas del encargo, portada, políticas, categoría inmediata, robots.txt y sitemaps.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-technical-rate-pages-web-minimum` §3, tarea T-077. Cierra [OQ-85](open-questions.md#f-evaluación-técnica), abierta por [D-161](#d-161). Claude propuso tres alternativas (encargo y páginas fijas, muestra del sitemap, solo fichas y políticas). Usuario: «Encargo + fijas».
- **Decisión:**
  - **Fichas de producto:** las del encargo, las mismas URL y la misma instantánea que la auditoría informativa.
  - **Portada:** siempre.
  - **Políticas y contenido:** siempre: envíos, devoluciones, contacto y aviso legal, localizadas desde la portada y su pie. La que no se localiza se registra como no localizada; no se sustituye por otra.
  - **Categoría o listado:** la inmediata de cada ficha, por sus migas de pan. Si la ficha no tiene migas, se registra.
  - **Recursos de la vista general:** robots.txt y los sitemaps (los declarados en robots.txt o, si no hay ninguno, `/sitemap.xml`; con sus índices y gzip).
  - Todo se captura con el perfil de auditoría (`audit-es`, [D-157](#d-157), [D-163](#d-163)).
- **Interpretación adoptada:** una página no localizada no es un requisito no satisfecho: sus requisitos no se evalúan y queda registrada. Si dos fichas comparten categoría inmediata, se captura una vez.
- **Consecuencias:** [evaluation-scopes](../10-model/evaluation-scopes.md#vistas-de-la-evaluación-técnica) 2.4; OQ-85 cerrada. Fuera de `docs/`: capture debe congelar robots.txt, los sitemaps y las páginas de cada tipo de una auditoría (tarea nueva); hasta entonces los requisitos que los necesitan son NE.
- **Relacionado:** D-157, D-161, D-162, D-163, OQ-85.

### D-168

**Mínimo de representación de Web: url, título y URL canónica; Open Graph condicional en el perfil de Web.** · aceptada · 2026-10-28

- **Contexto:** `INTAKE 2026-10-28-technical-rate-pages-web-minimum` §4, tarea T-077. Cierra [OQ-84](open-questions.md#f-evaluación-técnica). [D-147](#d-147) dejó el mínimo de Web para cuando tuviera perfil; [D-159](#d-159) lo fijó sin decidirlo. Claude exploró `title`, `meta description`, `rel=canonical` y Open Graph con las dos pruebas de D-147 (función y universalidad) y con el texto de las fuentes: WHATWG exige exactamente un `title`; Google recomienda una canónica que apunte a la propia página y da reglas de su forma; Open Graph exige `og:title`, `og:type`, `og:image` y `og:url` en toda página que lo use, no tiene tipo de producto, y Google usa `og:title` como una de las fuentes del título. Usuario: «Título + canónica + OG condicional».
- **Decisión:**
  - **Forman el mínimo de Web:**
    - la **url de la página**, cubierta por los requisitos de acceso (200, indexable, sin bloqueo);
    - el **título del documento** (`<title>`), con hecho comercial (el nombre): lo juzgan la técnica y la informativa ([D-143](#d-143));
    - la **URL canónica** (`link rel=canonical`), de sostén: su presencia, que recomienda Google, se queda en la técnica ([D-145](#d-145)); su forma (en `<head>`, absoluta, sin fragmento, sin canónicas contradictorias) es técnica;
    - la **imagen**, cubierta por `og:image` cuando la página usa Open Graph; si no, hueco registrado.
  - **Enmienda [D-159](#d-159):** el protocolo **Open Graph** entra en el perfil de Web, en el nivel de documento, **de forma condicional**: si la página publica alguna propiedad `og:`, lleva las cuatro que el protocolo exige para toda página, bien formadas, y `og:url` coincide con la URL canónica. Sin Open Graph, esos requisitos son NA.
  - **Fuera del mínimo:** `meta description` (contenido) y el idioma del documento.
  - **No técnico:** que coincidan `title`, `og:title`, el encabezado principal y el `name` del marcado es un juicio informativo (Fiabilidad dentro del ámbito o consistencia transversal).
- **Motivo (del artefacto):** Open Graph es la única declaración formal de la imagen y de la URL canónica de la página fuera de Schema.org, y Google usa `og:title` como fuente del título, aunque ningún consumidor del perfil lo exija.
- **Interpretación adoptada:** Open Graph es una especificación del documento, no un consumidor, por eso entra en ese nivel; su naturaleza la fija el propio protocolo. Las páginas de Google sobre la canonicalización y los títulos se suman al consumidor Google Search. Las comprobaciones concretas son requisitos de la referencia técnica, que deciden los agentes con cita ([D-133](#d-133)).
- **Consecuencias:** [commercial-information](../10-model/commercial-information.md#mínimo-de-representación) 1.6; [evaluation-scopes](../10-model/evaluation-scopes.md#perfil-de-implementación) 2.4; glosario (mínimo de representación, perfil de implementación); OQ-84 cerrada. Fuera de `docs/`: registrar y congelar Open Graph y la página de canonicalización de Google, y escribir los requisitos del mínimo de Web (T-077).
- **Relacionado:** D-143, D-144, D-145, D-147, D-159, D-160, OQ-84.
