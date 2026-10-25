---
id: changelog
title: Registro de cambios de la documentación
layer: governance
status: vigente
version: 1.0
updated: 2026-10-25
sources: []
---

# Registro de cambios

Entradas en orden cronológico inverso. Cada entrada indica la fecha, los módulos afectados, el tipo de cambio y la decisión que lo motiva.

**Tipos:** `estructura` · `canon` (cambia una definición, regla, escala o indicador) · `método` · `editorial` (sin cambio de significado) · `gobernanza`.

## 2026-10-25 — Informes del entrenamiento fuera de runs/ · aplicado

- **editorial** — Los informes de cada ciclo pasan a `demand-engine/training/reports/` (versionados, como resultados del entrenamiento) y `runs/` a `demand-engine/var/runs/` (salida desechable) (T-023). Menciones actualizadas en el contexto de la decisión sobre la medida descriptiva (`decisions`) y en OQ-51. Sin cambio de significado.

## 2026-10-25 — Enlaces al motor de captura común · aplicado

- **editorial** — El motor de captura pasa a su módulo común `demand-engine/src/demand_engine/capture/` (T-021, en aplicación de D-046); `mpir/` queda con lo propio del MPIR. Los enlaces «motor de captura» de `sampling-capture` 1.3, OQ-14 e I-18 apuntan a su README. Sin cambio de significado.

## 2026-10-25 — Update «filtro de relevancia, magnitudes físicas y fabricante y origen» · aplicado

- **canon** — `model-training` 1.2:
  - nueva sección «Relevancia»: lo que no informa sobre nada que importe para la clase sale de su modelo, por reglas inducidas por requisito y clase a partir de votos «no relevante»; sin regla, la duda no excluye; nunca se excluyen la capa general, lo normativo ni la medida que fija lo vendido ([D-050](decisions.md#d-050));
  - nuevo rasgo «magnitud física» (peso, grosor y gramaje), sin regla fija ([D-051](decisions.md#d-051));
  - métricas de coherencia de relevancia y salvaguarda de cobertura.

  `demand-model` 2.7: la capa general se contrasta también con el art. 19 del GPSR; filtro de relevancia.
- **método** — `requirement-blocks` 1.9: la capa general añade fabricante y contacto, persona responsable en la UE y advertencias de seguridad (normativa, GPSR art. 19) y el país de fabricación (referencias: `country_of_origin`, presente en todos los PTD de Amazon); marca, modelo e identificadores pasan a origen normativo ([D-052](decisions.md#d-052)); exclusión por relevancia en el formato del catálogo.
- **gobernanza** — D-043 (criterio 1) precisada; D-045 ampliada (D-050) y precisada (D-051); D-034 y D-039 ampliadas; D-035 anotada; I-17 anotada y retitulada; OQ-45 y OQ-49 anotadas; nueva OQ-51 (dimensiones de detalle). Glosario: rasgo, voto, regla inducida y filtro de relevancia. Revisión independiente aplicada: preguntas del fabricante y de las advertencias universales, con el GPSR como apoyo en su ámbito; persona responsable en la UE como requisito condicionado del producto; «se queda como complementario» solo sin regla de importancia. Update transcrito en `archive/intake/2026-10-25-relevance-origin.md`.

## 2026-10-25 — Update «modelo del producto, aplicación de la oferta y promociones» · aplicado

- **canon** — `demand-model` 2.6: el modelo de demanda va con el producto (bloques; clave y nombre sin aplicación) y la aplicación, con la oferta; la oferta sin condiciones activas es «estándar»; los requisitos condicionados que no se dan quedan en gris (NA justificado); los elementos digitales son del producto ([D-047](decisions.md#d-047)). La oferta no aporta requisitos: lo que solo trae una condición de la oferta es un requisito condicionado de la clase ([D-048](decisions.md#d-048)). `study-class` 1.3: la condición 1 solo admite características del producto.
- **método** — `requirement-blocks` 1.8: pregunta universal de promociones y descuentos en la capa general ([D-049](decisions.md#d-049)); elementos digitales en el modelo; valores de oferta con cuestiones propias como requisitos condicionados de la clase; denominación sin aplicación; inferidas condicionadas por la oferta. `cases` 1.6: denominación del Stressless.
- **gobernanza** — D-027 sustituida por D-048; D-033 y D-038 enmendadas, y D-034 y D-037 precisadas; OQ-37 anotada; nueva OQ-50 (cuándo vale el «no» de la pregunta de promociones). Glosario: aplicación (de la oferta), oferta estándar, requisito condicionado, especialización y especialización de oferta (retirada). Revisión independiente aplicada: condición 1 restablecida en la cita; citas de D-033 y D-038 recortadas; la capa general forma parte de todo modelo y la clave empieza por `gen@<versión>`; «estándar» como «ninguna condición declarada»; ejemplo de fin de serie llevado a hueco del marco; glosario sin «especialización de oferta». Update transcrito en `archive/intake/2026-10-25-offer-application.md`.

## 2026-10-25 — Update «operación del entrenamiento y motor de captura compartido» · aplicado

- **canon** — `model-training` 1.1: nueva sección «Operación de la primera versión», con:
  - los rasgos de los requisitos;
  - las reglas de importancia inducidas por el árbol de Shopify, con el crítico global y, en una clase sin regla, la propuesta del agente como provisional;
  - las métricas (cobertura, también por hechos declarados sin pregunta; estabilidad; coherencia) y la aceptación por mejora sin empeoramiento;
  - el conjunto de control (los 14 casos) y el catálogo de entrenamiento capturado;
  - el alcance de la primera versión ([D-045](decisions.md#d-045)).

  `demand-model` 2.5: la clave lleva la versión de cada bloque. El motor de captura pasa a ser compartido por el MPIR y el entrenamiento del modelo de demanda ([D-046](decisions.md#d-046)).
- **método** — `requirement-blocks` 1.7: estados «no compilado» y «compilado»; nuevo campo «rasgo» del requisito.
- **gobernanza** — D-034 enmendada (capa general fija) y D-038 enmendada (estados y clave) por D-045; D-040 y D-044 precisadas; OQ-47 cerrada → D-045; I-19 resuelta → D-045; I-17 y OQ-02 anotadas; nuevas OQ-48 (selección del catálogo de entrenamiento) y OQ-49 (inducción de las demás decisiones). Glosario: entradas nuevas (rasgo, voto, conjunto de control, motor de captura) y modificadas (regla inducida, catálogo compilado). Mapa del código en `CLAUDE.md` y `demand-engine/README.md`. Revisión independiente aplicada (coherencia por clase, capa general fija, límites literales del marco, ejemplo de la opción C). Update transcrito en `archive/intake/2026-10-25-training-operation.md`.

## 2026-10-25 — Update «marco humano y reglas inducidas» · aplicado

- **canon** — Nuevo módulo `model-training` 1.0: el usuario solo define el marco (propósito, objetivos y características del resultado, criterios de éxito, invariantes); el entrenamiento induce reglas generales y específicas, compila el catálogo y se valida solo contra el marco; la ejecución es automática ([D-044](decisions.md#d-044)). `demand-model` 2.4: la sección «Entrenamiento y ejecución» pasa a `model-training`. `study-class` 1.2: la validación de las especializaciones la hace el entrenamiento.
- **método** — `requirement-blocks` 1.6: catálogo compilado sin revisión manual; inferidas validadas por el entrenamiento.
- **estructura** — Nuevo módulo en el índice de `docs/README.md`.
- **gobernanza** — D-041 y D-036 enmendadas por D-044; D-022, D-039 y D-040 precisadas; criterio 5 de D-043 sustituido; I-17, I-19, OQ-02 y OQ-46 anotadas; nueva OQ-47. Glosario: entradas nuevas (entrenamiento, marco, regla inducida, catálogo compilado) y modificadas (ejecución, bloque de requisitos, criterio de especialización). Revisión independiente aplicada (restos de revisión humana, citas literales, campo «regla» del requisito, capa general dentro del marco). Update transcrito en `archive/intake/2026-10-25-induced-rules.md`.

## 2026-10-25 — Rutas del motor de captura tras la reestructuración del código · aplicado

- **editorial** — El motor de captura del MPIR pasa de `mpir/` a `demand-engine/src/demand_engine/mpir/` y su corpus a `demand-engine/var/mpir/` (T-017: cada sistema es un directorio de primer nivel). Enlaces actualizados en `sampling-capture` 1.2, OQ-14 e I-18. Sin cambio de significado.

## 2026-10-25 — Update «criterios del catálogo de bloques» · aplicado

- **método** — `requirement-blocks` 1.5: nueva sección «Criterios de redacción del catálogo» (medida crítica si fija qué se vende; atributos divididos por tema; solapes con la capa general y con el juego; propiedades de Amazon repetidas en hermanas; inferidas provisionales), composición textil con apoyo normativo (Reglamento (UE) 1007/2011, art. 16.1), propiedades descriptivas del grupo de cumplimiento de Amazon y color como característica del producto ([D-043](decisions.md#d-043)).
- **gobernanza** — Update transcrito en `archive/intake/2026-10-25-catalog-criteria.md`.

## 2026-10-25 — Update «motor de captura del MPIR» · aplicado

- **método** — `sampling-capture` 1.1: la capa original no conserva capturas de pantalla, y el motor aplica robots.txt (RFC 9309) y las reservas de minería de textos y datos (art. 67.3 TRLPI) entre las políticas aplicables ([D-042](decisions.md#d-042)). Marca ⚠ I-18 en el renderizado selectivo.
- **gobernanza** — I-18 abierta: el método prevé renderizar «selectivamente» y el motor renderiza siempre, con propuesta. OQ-14 y OQ-15 anotadas con lo que fija el motor de forma provisional, sin cerrarse. Update transcrito en `archive/intake/2026-10-25-mpir-capture-engine.md`.

## 2026-10-25 — Update «entrenamiento y ejecución» · aplicado

- **canon** — `demand-model` 2.3: nueva subsección «Entrenamiento y ejecución»: la revisión humana se hace en entrenamiento y la ejecución es automática; lo no revisado se usa como provisional, se marca y se encola; las cuestiones inferidas son un añadido provisional fuera de la clave hasta que se aceptan ([D-041](decisions.md#d-041)). `study-class` 1.1: la validación de especializaciones no bloquea la ejecución.
- **método** — `requirement-blocks` 1.4: catálogo revisado en entrenamiento y generado automáticamente en ejecución si falta la categoría; inferidas fuera del bloque hasta su aceptación.
- **gobernanza** — D-022, D-036 y D-040 matizadas por D-041; I-16 resuelta → D-041. Glosario: entrenamiento y ejecución. Update transcrito en `archive/intake/2026-10-25-training-runtime.md`. Revisión independiente aplicada: citas matizadas marcadas, inferidas fuera del bloque hasta su aceptación también en `cases` 1.5 y en el método, D-038 matizada, alcance declarado (nueva OQ-46), términos del glosario acotados, nueva I-19 (estados y versiones del catálogo en ejecución) e I-17 anotada.

## 2026-10-25 — Update «Amazon como fuente y bloques deterministas» · aplicado

- **canon** — `demand-model` 2.2: los PTD de Amazon, incluidos los valores de special_feature, pueden ser fuente de requisitos de la categoría cuando son relevantes para la clase ([D-039](decisions.md#d-039), enmienda D-009); un atributo repetido va al bloque de la categoría más general que lo lista y los bloques de categoría salen de un catálogo revisado ([D-040](decisions.md#d-040)).
- **método** — `requirement-blocks` 1.2 (bloques de categoría con propiedades de Amazon, asignación determinista, catálogo revisado); `sources` 1.1 y README de product-taxonomy 1.7 (papel de los PTD).
- **gobernanza** — D-009 enmendada por D-039; D-038 precisada por D-040. Glosario: bloque de requisitos. Update transcrito en `archive/intake/2026-10-25-amazon-source-blocks.md`. Revisión independiente aplicada: Google y el árbol de Amazon siguen siendo solo de apoyo; reglas de ubicación de las propiedades de Amazon en el método; el acabado del algodón pasa a requisito de referencias en `cases` 1.4; `data-model-governance` actualizado; nuevas I-16 (inferidas dentro de un bloque fijo) e I-17 (relevancia de D-039 frente a D-030).

## 2026-10-25 — Update «catálogo de bloques (OQ-44)» · aplicado

- **canon** — `demand-model` 2.1: denominación en dos niveles, clave y nombre; identificadores de bloque propios, con las referencias aparte ([D-038](decisions.md#d-038)).
- **método** — `requirement-blocks` 1.1: capa general contrastada con el art. 97.1 del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios (precio total con envío, crítico; medios de pago, contacto y opiniones, complementarias; desistimiento y garantías reformulados; nuevas condicionadas de precio personalizado, elementos digitales y suscripción); formato del catálogo e identificadores; denominación.
- **gobernanza** — OQ-44 cerrada → D-038; nueva OQ-45; D-034 con el borrador revisado. Glosario: bloque de requisitos. Update transcrito en `archive/intake/2026-10-25-block-catalog.md`. Revisión independiente aplicada: cita literal de la denominación, sector y categoría como un único tipo `cat.`, resto del bloque B y precisiones de formato declarados en D-038, cantidad limitada como condicionada, letra l en OQ-45.

## 2026-10-25 — Update «bloques de requisitos, capa general e importancia» · aplicado

- **canon** — `demand-model` 2.0 (reestructurado): la identidad del modelo de demanda es una composición de bloques de requisitos más su aplicación a una oferta; las categorías por clasificación objetiva que no aportan requisitos son alias ([D-033](decisions.md#d-033)); capa general universal y condicionada con importancias por defecto revisables ([D-034](decisions.md#d-034)); la confianza es independiente de la importancia ([D-035](decisions.md#d-035)); tercera vía de construcción, las cuestiones inferidas provisionales ([D-036](decisions.md#d-036)). Nuevo módulo `study-class` 1.0: los valores de oferta (outlet, exposición, reacondicionado…) condicionan la capa general y un valor que activa cuestiones condicionadas es valor que condiciona ([D-037](decisions.md#d-037)); la especialización es la característica que forma un bloque.
- **estructura** — La sección «Clase de estudio» sale de `demand-model` a `10-model/study-class.md`; 36 enlaces actualizados en `docs/`. Índice de `docs/README.md` actualizado.
- **método** — Nuevo módulo `requirement-blocks` 1.0 (propuesta): bloques, pruebas de importancia, catálogo inicial de la capa general y controles de las cuestiones inferidas. `cases` 1.3: Stressless (Sofás → tapicería de piel; reclinable y outlet como valores), sofá cama Luna (mecanismo no declarado, cuestión inferida) y funda bordada (peinado y mercerizado como respuestas a una cuestión inferida). `product-taxonomy` (README) 1.6.
- **gobernanza** — D-026 ampliada por D-037; ejemplo de D-027 sustituido; D-028 y D-032 precisadas por D-033; OQ-42 cerrada → D-037; OQ-01, OQ-02 y OQ-37 anotadas; I-11 ampliada. Glosario: modelo de demanda, clase de estudio, especialización de oferta, clasificación objetiva, importancia relativa y nuevas entradas (bloque de requisitos, aplicación, alias, capa general, cuestión inferida). Update transcrito en `archive/intake/2026-10-25-requirement-blocks.md`. Revisión independiente aplicada: citas literales del artefacto en `demand-model` y `study-class`; tercera vía en los README de product-taxonomy y mpir (D-009 ampliada por D-036); D-020 precisada por D-033; aplicación y alias sin redefinir en el método; sector y categoría sin doble cómputo; descuento como disparador en los casos; nueva OQ-44 (catálogo de bloques y dudas de la capa general).

## 2026-10-25 — Update «propósito de la clase de estudio» · aplicado

- **canon** — `demand-model` 1.7: principio de propósito, según el cual la clase de estudio se juzga por los requisitos informativos que produce, con su lectura aceptada; la clasificación objetiva solo da entrada a una categoría cuando tiene sentido, y no si traería requisitos que no aplican ([D-032](decisions.md#d-032)).
- **editorial** — `demand-model`: se retira la frase que repetía el paso 3 de la regla metodológica.
- **método** — `cases` 1.2: la tela del sofá cama Luna y el mordedor pasan a valor que condiciona, y sus requisitos se mantienen; el lavado de la cuerda queda en la base; apoyo del polar de la manta documentado; protector de colchón revisado; nuevo caso del juego de funda nórdica bordada, en el que Juegos de cama no entra. `subclasses` 1.6: efecto del juego con los requisitos del conjunto y base de la pieza de las fundas en el polar. `product-taxonomy` (README) 1.5.
- **gobernanza** — I-14 resuelta → D-032; D-028 precisada por D-032; consecuencia de D-026 sobre el sofá cama revisada; OQ-43 e I-13 anotadas; I-11 ampliada. Glosario: clase de estudio, componente de la clase de estudio y clasificación objetiva. Update transcrito en `archive/intake/2026-10-25-requirements-purpose.md`. Revisión independiente aplicada: lectura aceptada citada en `demand-model`, D-032 completada con todas las afirmaciones del update, el juego de funda nórdica Salvia con los requisitos del conjunto, atributos distintivos de Juegos de cama corregidos, mordedor marcado como interpretación provisional y nueva I-15 (`warmth-level` no está solo en Juegos de cama).

## 2026-10-25 — Update «clasificación objetiva y base de la clase» · aplicado

- **canon** — `demand-model` 1.6: una categoría candidata en la que el producto entra por clasificación objetiva forma parte de la composición aunque no aporte requisitos propios ([D-028](decisions.md#d-028)); la base de una categoría de Shopify incluye los atributos de sus madres ([D-029](decisions.md#d-029)); las características especiales (`special_feature`) de un PTD cuentan como dimensiones de la base y como apoyo ([D-030](decisions.md#d-030)); el material reciclado es especialización y «sostenible», beneficio reclamado ([D-031](decisions.md#d-031)).
- **método** — `cases` 1.1: el sofá cama Luna pasa a Sofás cama + Sofás de dos plazas, y cinco casos nuevos (manta, plaid, zapatillas de baño, protector de colchón, cojín). `subclasses` 1.5: los apoyos de «juego» y «tejido polar» del caso de las sábanas quedan en la base heredada de las piezas. `product-taxonomy` (README) 1.4: índice de casos.
- **gobernanza** — D-023 modificada por D-028 y precisada por D-029; D-024 y D-026 precisadas por D-029 y D-030; D-025 precisada por D-031. I-12 resuelta → D-029; I-11 ampliada; OQ-39 anotada; nueva OQ-43. Glosario: componente de la clase de estudio, especialización, criterio de especialización y nueva entrada «clasificación objetiva». Update transcrito en `archive/intake/2026-10-25-objective-classification.md`. Revisión independiente aplicada: regla de clasificación objetiva citada literalmente en `demand-model`, alcance de «categorías madre» como interpretación de D-029, glosario completado, cuestiones del cojín y lista de casos de `subclasses` corregidas, I-13 anotada y nueva I-14 (casos documentados que cambian con la base ampliada).

## 2026-10-25 — Update «cuestiones propias y especializaciones de oferta» · aplicado

- **canon** — `demand-model` 1.5: regla de las cuestiones propias para dimensiones que todo producto tiene ([D-026](decisions.md#d-026)) y condición 1 ampliada a la oferta, con especializaciones de oferta ([D-027](decisions.md#d-027)).
- **método** — Nuevo módulo `cases` 1.0, con los casos de evaluación que estaban en `subclasses` (1.4) y cuatro casos nuevos (bota de equitación, sofá reclinable de exposición, funda nórdica, pienso). El sofá cama Luna se corrige: la tela pasa a especialización. `product-taxonomy` (README) 1.3: índice con `cases`.
- **gobernanza** — D-022 precisada por D-026 y con la condición 1 enmendada por D-027. OQ-37 anotada (clases de oferta resueltas); I-11 ampliada. Glosario: especialización, criterio de especialización y nueva entrada «especialización de oferta». Update transcrito en `archive/intake/2026-10-25-own-questions-offer.md`. Revisión independiente aplicada: lectura del criterio con «del producto o de la oferta», razones de las consecuencias citadas, observaciones separadas por fuente, nuevas OQ-41 y OQ-42, nueva I-13 e I-12 añadida a la tabla de incidencias.

## 2026-10-25 — Update «composición de la clase» · aplicado

- **canon** — `demand-model` 1.4: nueva sección «Composición de la clase» (el modelo de clase es un sistema de composición de requisitos; si el producto abarca varias categorías, la clase general es su composición; una categoría entra si aporta requisitos al producto o a alguna de sus piezas, [D-023](decisions.md#d-023)); la cita del eje de base queda enmendada. En el criterio: condición 4 en lectura estricta ([D-024](decisions.md#d-024)) y exclusión de los beneficios reclamados ([D-025](decisions.md#d-025)). Nota del ejemplo: las sábanas se componen por piezas.
- **método** — `subclasses` 1.3: caso de las sábanas recompuesto por piezas y nueva sección «Casos de evaluación del método» (toallas, sofá cama, juguete de cuerda) con sus observaciones. `product-taxonomy` (README): índice actualizado.
- **gobernanza** — D-021 modificada por D-023; D-022 precisada por D-024 y ampliada por D-025. OQ-05 y OQ-37 anotadas; I-11 ampliada. Glosario: clase general, especialización, criterio de especialización y nueva entrada «componente de la clase de estudio». Update descrito por el usuario y transcrito en `archive/intake/2026-10-25-class-composition.md`. Revisión independiente aplicada: cita de D-021 sustituida por su formulación enmendada, nuevas OQ-39 (prueba de «aportar requisitos») y OQ-40 (beneficios en la auditoría), nueva I-12 (apoyo del caso de las sábanas en una categoría que ya no es componente).

## 2026-10-24 — Update «criterio de especialización» · aplicado

- **canon** — `demand-model` 1.3: nuevas secciones «Clase general: el eje de base» (la clase general es una categoría de Shopify; lo que Shopify no distingue es candidato a especialización, [D-021](decisions.md#d-021)) y «Criterio de especialización» (cinco condiciones y exclusiones; la especialización que las cumple queda provisional hasta su validación, [D-022](decisions.md#d-022)). Nueva subsección «Ejemplo»: el tejido se fija en «polar» y la coralina queda como valor.
- **método** — `subclasses` 1.2: caso de trabajo ilustrativo del juego de sábanas de coralina y delimitación entre el criterio (clase de estudio) y la prueba de especialización (subclases o niveles jerárquicos). `integration` 1.2: el umbral de la clase de estudio remite al criterio. `product-taxonomy` (README): índice con el caso.
- **gobernanza** — OQ-38 cerrada → D-022; OQ-06, OQ-09 y OQ-37 anotadas; I-11 ampliada con D-021, D-022 y los updates conversacionales. Glosario: clase general, especialización y nueva entrada «criterio de especialización». Update descrito por el usuario y transcrito en `archive/intake/2026-10-24-specialization-criterion.md`. Revisión independiente aplicada.

## 2026-10-24 — Intake «definición de la clase» · aplicado

- **canon** — `demand-model` 1.2: nueva sección «Clase de estudio». La clase objeto del modelo de demanda se compone de la clase general y de todas las especializaciones relevantes, que pueden ser facetas concurrentes. Incluye una regla en cuatro pasos y el principio de especificidad informativa necesaria ([D-020](decisions.md#d-020)).
- **método** — `product-taxonomy`, `subclasses`, `integration` y `data-model-governance` pasan a la versión 1.1: enlazan la clase de estudio, y el grado de especialización sale de las decisiones pendientes.
- **gobernanza** — OQ-09 cerrada → D-020; nuevas OQ-37 y OQ-38. Glosario: clase de estudio, clase general y especialización. Nueva incidencia I-11, sobre la definición de `vigente` frente al intake, detectada en la revisión. Artefacto archivado en `archive/intake/2026-10-24-define-class.md`.

## 2026-10-24 — Intake «prominencia informativa» · aplicado

- **gobernanza** — El intake prevalece sobre el contenido existente y se aplica sin aprobación previa ([D-016](decisions.md#d-016)). Skill `docs-update` reescrita.
- **canon** — `scoring-systems` 1.1: escala del IR fijada en **0–10** ([D-017](decisions.md#d-017)) y nuevo **estado binario de resolución** (propuesta, [D-019](decisions.md#d-019)).
- **canon** — Nuevo módulo `informative-prominence` 1.0 (propuesta): prominencia informativa, IP y calidad ajustada ([D-018](decisions.md#d-018)). Se reformula la invariante 7 del `CLAUDE.md` raíz.
- **gobernanza** — Nuevas OQ-31 a OQ-36 (sección G). OQ-28 anotada. Artefacto archivado en `archive/intake/2026-10-24-prominencia-informativa.md`.

## 2026-10-24 — Intake y skill docs-update

- **estructura** — Nueva bandeja `docs/intake/` y nueva skill `/docs-update` para procesar updates ([D-015](decisions.md#d-015)). El validador admite la clave de fuente `INTAKE <stem>` (comprueba que exista en `archive/intake/`) e ignora `intake/`.

## 2026-10-24 — Resolución de I-01, I-04, I-07, I-09 e I-10

- **canon** — `scope` 1.1: CTX §5 enumera los tres ámbitos ([D-013](decisions.md#d-013)). `quality-properties` 1.2: P07 entra en las asociaciones orientativas de Aplicabilidad ([D-014](decisions.md#d-014)).
- **editorial** — Denominaciones confirmadas: TRI y Tasa de cumplimiento técnico, con los alias de FUND ([D-003](decisions.md#d-003)); «Taxonomía de clases de producto» ([D-012](decisions.md#d-012)). Nombre del proyecto: **stratia.cic** ([D-011](decisions.md#d-011)).
- **gobernanza** — Todas las incidencias I-01 a I-10 quedan resueltas.

## 2026-10-24 — Resolución de I-02 e I-03

- **canon** — `demand-model` 1.1: el modelo de demanda tiene dos vías de construcción, la taxonomía de clases de producto y el MPIR (BASE §4.2 enmendada, [D-009](decisions.md#d-009)).
- **canon** — «Interfaz» y «ámbito» son sinónimos en la unidad de evaluación ([D-010](decisions.md#d-010), sustituye a D-004). Se retiran las marcas ⚠ I-03 de `evaluation-scopes`, `evaluation-architecture`, `scoring-systems`, `acceptance-criteria`, `inputs-outputs`, `integration` e `interpretation-transfer`.
- **gobernanza** — I-02 e I-03 resueltas. Se reformula la propuesta de I-04.

## 2026-10-24 — Resolución de I-05, I-06 e I-08

- **canon** — `quality-properties` 1.1: la definición de propiedades (BASE §5.3) queda enmendada y se elimina «y los requisitos técnicos generales». Las propiedades son exclusivamente informativas y P01–P05 quedan retirados ([D-007](decisions.md#d-007)).
- **gobernanza** — I-05 e I-08 resueltas por D-007; I-06 resuelta por [D-008](decisions.md#d-008): antecedentes no incorporados y documentos de apoyo no disponibles.

## 2026-10-24 — Línea base 1.0

- **estructura** — Reorganización del corpus v0 en capas y módulos ([D-001](decisions.md#d-001)). Originales archivados en `archive/v0-2026-10-24/` ([D-002](decisions.md#d-002)).
- **estructura** — Nuevos: `CLAUDE.md` raíz, `docs/CLAUDE.md`, `docs/README.md`, `docs/glossary.md` y `tools/check_docs.py`.
- **canon** — Sin cambios de significado. Definiciones normativas trasladadas literalmente desde CTX/BASE; interpretación condensada desde FUND.
- **editorial** — Correcciones tras la revisión independiente de fidelidad. Se restituyen citas literales de CTX/BASE en `scope`, `scoring-systems` y `demand-model`. Se corrige la «conformidad técnica como requisito necesario» (`commercial-information`). Se retira «no hay compensación entre criterios» como regla vigente y se remite a M09 (propuesta). Se restituyen matices de FUND §3.6, §4.1, §4.3, §6.2, §7.3 y §12. Se marca la procedencia GSC0 donde correspondía. En `20-methods/`: se restituyen las condiciones de los casos de calibración G, H, J, K y L, la tabla de dimensiones del registro de FUND §9.4 (`evidence`) y GSC0 §18.1–18.2 (`open-questions`); se marcan los bloques vigentes de FUND; se unifica la definición de evidencia y hallazgo. La matriz de cobertura de GSC0 §19 es metadocumentación del borrador v0 y **no se traslada**: se consulta en el archivo.
- **gobernanza** — Incidencias I-01 a I-10 registradas; cuestiones abiertas consolidadas (OQ-01 a OQ-30); decisiones provisionales D-003 y D-004.
- **método** — GSC0, TAX y MPIR divididos en módulos de `20-methods/`, con los IDs de reglas originales.
