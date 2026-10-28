---
id: changelog
title: Registro de cambios de la documentación
layer: governance
status: vigente
version: 1.0
updated: 2026-10-28
sources: []
---

# Registro de cambios

Entradas en orden cronológico inverso. Cada entrada indica la fecha, los módulos afectados, el tipo de cambio y la decisión que lo motiva.

**Tipos:** `estructura` · `canon` (cambia una definición, regla, escala o indicador) · `método` · `editorial` (sin cambio de significado) · `gobernanza`.

## 2026-10-28 — Datos del mínimo de representación en Web Schema.org y formación estructural · aplicado

- **canon** — `INTAKE 2026-10-28-minimum-members-structural-formation` (preguntas del usuario sobre lo obligatorio y lo condicional de Google y sobre las estructuras opcionales incluidas; propuesta conjunta aprobada):
  - datos del mínimo en Web Schema.org, con dos pruebas (función y universalidad): url de la oferta, enlace Product → Offer, relación variante ↔ grupo, variesBy, `@id` (hueco), imagen, nombre, SKU y nombre del vendedor; GTIN, MPN y marca quedan fuera por la prueba de universalidad; en Merchant Center el GTIN es muy recomendado si existe, y el MPN (sin GTIN) y la marca (productos nuevos) son obligaciones condicionales, para el perfil de Catálogos distribuidos ([D-147](decisions.md#d-147));
  - formación estructural: una estructura publicada, aunque sea opcional, tiene las partes exigidas, las necesarias para interpretar sus valores y partes coherentes entre sí; absorbe la excepción de D-145 ([D-148](decisions.md#d-148)).
  - Módulos: [commercial-information](../10-model/commercial-information.md) 1.4, [evaluation-scopes](../10-model/evaluation-scopes.md) 1.5, [demand-model](../10-model/demand-model.md) 3.6; glosario (Mínimo de representación, Perfil de implementación y nueva entrada Formación estructural).
- **gobernanza** — OQ-74 cerrada; OQ-30 anotada; D-143 y D-145 anotadas. T-055 desbloqueada. Numeración: D-146 la tomó en paralelo otra sesión (perímetro de PAA); estas decisiones son D-147 y D-148.

## 2026-10-28 — La categoría madre y el material en el perímetro de PAA · aplicado

- **canon** — `INTAKE 2026-10-28-paa-parent-and-material` (decisión del usuario sobre I-48, a la vista de la pasada de control con el reglamento PAA v5; T-053):
  - la pregunta sobre la categoría madre va dentro cuando pregunta por algo que la clase hereda de su bloque, y fuera si solo tiene sentido para otro producto o trata de un hermano; las semillas no cambian; la pregunta sobre el material va dentro si la clase lo tiene o lo hereda ([D-146](decisions.md#d-146), que enmienda D-141);
  - en pantuflas, las tres preguntas de cuero vuelven dentro y sus aportaciones pasan a esperadas.
  - Módulos: [choice-criteria](../10-model/choice-criteria.md) 1.11, [construction-routes](../10-model/construction-routes.md) 1.7; glosario (Producto vecino).
- **gobernanza** — [I-48](issues.md#i-48) resuelta → D-146; D-141 anotada en la tabla. Fuera de `docs/`: reglamento PAA v6 y casos de control (T-053).

## 2026-10-28 — Frontera entre la evaluación técnica y la informativa · aplicado

- **canon** — `INTAKE 2026-10-28-technical-informative-frontier` (propuesta del usuario; clasificación de los 414 requisitos técnicos y alternativa A, elegida por el usuario):
  - la técnica mira cómo está construido lo que se publica más la presencia de lo que el consumidor exige; la informativa, si se publica lo que el consumidor solo recomienda; decide la naturaleza que fija la especificación ([D-145](decisions.md#d-145), que enmienda D-130 y precisa D-143);
  - la presencia de lo recomendado pasa a ser, en general, apoyo del modelo de demanda del ámbito Web Schema.org (salvo los recomendados que interpretan un valor publicado y los datos del mínimo que fije OQ-74).
  - Módulos: [evaluation-scopes](../10-model/evaluation-scopes.md) 1.4 (fila del consumidor y nueva subsección «Frontera entre la evaluación técnica y la informativa»), [commercial-information](../10-model/commercial-information.md) 1.3, [demand-model](../10-model/demand-model.md) 3.5; glosario (Perfil de implementación).
- **gobernanza** — OQ-75 cerrada; OQ-74 y OQ-30 anotadas; nueva OQ-76 (cómo entra lo recomendado en el modelo de demanda). D-130 y D-143 anotadas en la tabla. Fuera de `docs/`: T-055 (retirada en la referencia técnica de estos y de los 26 que no se auditan, después de OQ-74) y T-056 (motor de demanda).

## 2026-10-28 — Mínimo de representación de la oferta y papel de la imagen · aplicado

- **canon** — `INTAKE 2026-10-28-minimum-representation-image` (propuesta del usuario sobre los datos fundamentales de la representación; estudio de la imagen por Claude, alternativa A elegida por el usuario):
  - nuevo concepto, el mínimo de representación: los datos que hacen falta para descubrir la oferta, acceder a ella e identificarla; si existen y están bien formados lo dice la técnica, y lo que transmiten los que llevan un hecho comercial, la informativa ([D-143](decisions.md#d-143));
  - la imagen es un dato de sostén del mínimo y se evalúa en la técnica; lo que muestra no es información (no da disponibilidad, no resuelve ni refuta), y la información explícita que lleva sí lo es si el ámbito permite leerla ([D-144](decisions.md#d-144), que enmienda una interpretación de D-052).
  - Módulos: [commercial-information](../10-model/commercial-information.md) 1.2, [effective-availability](../10-model/effective-availability.md) 1.2, [acceptance-criteria](../10-model/acceptance-criteria.md) 1.5, [evaluation-scopes](../10-model/evaluation-scopes.md) 1.3; glosario (nueva entrada Mínimo de representación).
- **gobernanza** — nuevas OQ-74 (qué datos forman el mínimo) y OQ-75 (frontera general entre las dos evaluaciones y los 83 requisitos apartados en el triaje); OQ-20 anotada (texto dentro de una imagen); D-052 anotada en la tabla. Implantación en `demand-engine/catalog/gen.json` y `rules/resolving.json` (quitar la aportación de imagen de `gen/24`): T-054.

## 2026-10-28 — Reglas de la revisión de los casos de control de PAA · aplicado

- **canon** — `INTAKE 2026-10-28-paa-control-review-rules` (decisiones del usuario en la revisión de T-042, depositadas en T-052):
  - productos vecinos fuera del perímetro siempre; el perímetro va antes de la lectura sobre la oferta, que ya no lo decide ([D-141](decisions.md#d-141), que enmienda D-100);
  - la moda nunca genera; la popularidad no genera (C4); la preferencia general es un criterio intermedio; la alternativa de producto no genera (C3) ([D-142](decisions.md#d-142), que precisa D-104 y D-110).
  - Módulos: [choice-criteria](../10-model/choice-criteria.md) 1.10, [construction-routes](../10-model/construction-routes.md) 1.6; glosario (Lectura sobre la oferta, Criterio de elección intermedio, nueva entrada Producto vecino).
- **gobernanza** — nueva [I-48](issues.md#i-48): alcance de «la categoría madre en general» y de las preguntas sobre el material, a la vista de la pasada de control con el reglamento PAA v5 (T-052). Fila de [I-47](issues.md#i-47), que faltaba en la tabla.

## 2026-10-27 — Las pistas de un requisito viven en el requisito · aplicado

- **canon** — `INTAKE 2026-10-27-requirement-hints-location`: las pistas dirigidas a un requisito viven en el propio requisito; las de tipo y de fuente siguen en el catálogo de pistas ([D-140](decisions.md#d-140), que enmienda D-134 y precisa D-135).
  - Módulos: [assessment-hints](../10-model/assessment-hints.md) 1.6 (reglas 6 a 10), [demand-model](../10-model/demand-model.md) 3.4; glosario (Pistas de valoración).
- **gobernanza** — OQ-73 anotada.

## 2026-10-27 — Primera pasada de la referencia técnica · aplicado

- **gobernanza** — primera pasada del inventario de fuentes de Schema.org con `/web-reference` (T-047; referencia en `web-audit/reference/`, informe en `web-audit/reference/reports/2026-10-27-primera-pasada.md`). Sin intake ni decisiones: solo se registra lo que afecta al canon.
  - Nueva [I-47](issues.md#i-47): el GS1 Web Vocabulary no encaja en ninguna clase de fuente; propuesta de la clase «vocabulario complementario».
  - [I-41](issues.md#i-41) anotada: el dígito de control del GTIN lo recomienda Schema.org 30.1 (nivel de vocabulario); la página de fichas de comerciante solo pide la forma numérica.

## 2026-10-27 — Hallazgos del piloto de pistas de valoración · aplicado

- **gobernanza** — piloto de las pistas de valoración y de la marca de comparación con los nueve requisitos de sábanas (T-050; catálogo en `demand-engine/catalog/hints.json`). Sin intake ni decisiones: solo se registra lo que afecta al canon.
  - Nuevas incidencias: [I-42](issues.md#i-42) (separadores de la etiqueta de una fuente), [I-43](issues.md#i-43) (`para` con un solo valor ante temas repartidos, como las certificaciones), [I-44](issues.md#i-44) (duplicadas por llaves distintas), [I-45](issues.md#i-45) (pistas de tipo en la capa general) e [I-46](issues.md#i-46) (qué puede comprobar el código de «criterio, no lista»).
  - Nueva [OQ-73](open-questions.md) (corregir en su sitio una pista que no ha usado ningún modelo); OQ-66 y OQ-71 anotadas.
- **editorial** — marcas ⚠ I-42 a I-46 y OQ-73 en [assessment-hints](../10-model/assessment-hints.md) 1.5.

## 2026-10-27 — Marco de la evaluación técnica de Web Schema.org · aplicado

- **canon** — `INTAKE 2026-10-27-web-schema-technical-framework` (planificación del sistema web-audit, T-044):
  - **web-audit** es el sistema de la evaluación técnica de Web y Web Schema.org, solo técnico; empieza por Web Schema.org ([D-129](decisions.md#d-129));
  - **perfil de implementación**: definición; la naturaleza obligatoria o recomendada es relativa al perfil; en Web Schema.org, serialización (JSON-LD 1.1, Microdata, RDFa 1.1), vocabulario (Schema.org 30.1) y consumidor (Google Search); Merchant Center, solo para Catálogos y la consistencia transversal ([D-130](decisions.md#d-130));
  - **estados del requisito técnico**: satisfecho o no satisfecho, NA y NE como incidencia; el sistema cuantitativo sigue abierto ([D-131](decisions.md#d-131));
  - solo una **especificación aplicable** fundamenta un requisito técnico; función de las demás clases de fuente; una condición por requisito y cita literal ([D-132](decisions.md#d-132));
  - la **referencia técnica** vive en `web-audit/reference/`, gobernada por el canon; los requisitos los deciden los agentes con cita y una skill los mantiene ([D-133](decisions.md#d-133)).
  - Módulos: [evaluation-scopes](../10-model/evaluation-scopes.md) 1.2 (perfil de implementación, estados, fuentes de los requisitos técnicos), [scoring-systems](../10-model/scoring-systems.md) 1.4 (tasa de cumplimiento técnico y lectura integrada); glosario (Requisito técnico general; nuevas: Perfil de implementación, Estados del requisito técnico, Especificación aplicable, web-audit).
- **editorial** — marca ⚠ I-41 en [acceptance-criteria](../10-model/acceptance-criteria.md) 1.4 y [ac-guides](../20-methods/audit-gsc/ac-guides.md) 0.4 (frontera sintaxis/valor).
- **gobernanza** — OQ-30 anotada (queda lo operativo y el sistema cuantitativo); nueva I-41 (GTIN inválido: Fiabilidad o también requisito técnico de un perfil).

## 2026-10-27 — Cómo se fija la marca de comparación · aplicado

- **canon** — `INTAKE 2026-10-27-comparison-mark`: la marca de dimensión de comparación se fija por requisito, con un criterio (se compara si el comprador elige por ese valor; no si es igual para todos, un filtro de necesidad o gusto, o identifica la oferta o su estado), explícita y con motivo, sin valor por defecto; los dudosos, «se compara»; pruebas, escritores y momentos como las pistas ([D-139](decisions.md#d-139); precisa D-126). [assessment-hints](../10-model/assessment-hints.md) 1.4, [demand-model](../10-model/demand-model.md) 3.3; glosario.
- **gobernanza** — OQ-69 cerrada.

## 2026-10-27 — Gobierno de las pistas de valoración · aplicado

- **canon** — `INTAKE 2026-10-27-hints-governance`: las pistas las redactan los agentes sin aprobación y entran si pasan comprobaciones automáticas; duplicadas no se añaden, contradictorias quedan como duda; no se borran, se retiran; orígenes «marco», «normativa», «referencias» y «paa» ([D-136](decisions.md#d-136)). Nacen de una pasada manual de Claude y luego se van definiendo al crear modelos y en los entrenamientos; que queden sin compilar y encoladas es interpretación de Claude, pendiente de OQ-71 ([D-137](decisions.md#d-137)). Niveles no exclusivos, sin ámbito, el GSC cita las pistas usadas y el modelo anota la versión del catálogo de pistas ([D-138](decisions.md#d-138)). [assessment-hints](../10-model/assessment-hints.md) 1.3, [model-training](../10-model/model-training.md) 1.20; glosario (Pistas de valoración).
- **método** — [gsc-decision](../20-methods/audit-gsc/gsc-decision.md) 0.4: GSC-12 y `pistas_usadas` en la plantilla.
- **gobernanza** — OQ-66 anotada; nuevas OQ-71 (paso y material para escribir pistas) y OQ-72 (métrica de calidad).

## 2026-10-27 — Campos de una pista de valoración · aplicado

- **canon** — `INTAKE 2026-10-27-hint-fields`: seis campos (`id` `PV-1`… sin ceros delante, `pista`, `propiedad`, `ac`, `para`, `origen`); las pistas dirigidas a una fuente las escribe taxo; el perfil del RI las recibe resueltas en `pistas_valoracion` ([D-135](decisions.md#d-135)). [assessment-hints](../10-model/assessment-hints.md) 1.2; glosario (Pistas de valoración).
- **método** — [ri-profile](../20-methods/audit-gsc/ri-profile.md) 0.2: campo `pistas_valoracion`.
- **editorial** — paa-training, choice-criteria y construction-routes: pendientes que citaban OQ-68, actualizados.
- **gobernanza** — OQ-68 cerrada; nueva OQ-70 (índice de pistas por requisito, aplazado).

## 2026-10-27 — Catálogo de pistas de valoración · aplicado

- **canon** — `INTAKE 2026-10-27-hints-catalog`: las pistas viven en un catálogo propio del motor de demanda; cada una se escribe una vez y va dirigida a un tipo, a una fuente o a un requisito; los requisitos no las copian; encontrarlas es una búsqueda por etiquetas, solo con código; aplicarlas lo hace el auditor ([D-134](decisions.md#d-134); precisa D-127). [assessment-hints](../10-model/assessment-hints.md) 1.1, [demand-model](../10-model/demand-model.md) 3.2, [model-training](../10-model/model-training.md) 1.19; glosario (Pistas de valoración).
- **gobernanza** — OQ-68 y OQ-69 anotadas.

## 2026-10-27 — Pistas de valoración · aplicado

- **canon** — `INTAKE 2026-10-27-assessment-hints` (diseño del sistema de reglas de valoración de los AC, continuación):
  - las **pistas de valoración** son lo que cada requisito fija para orientar la valoración de sus AC; sustituyen a las «reglas de AC de un requisito»; tres niveles (marco; tipo para Aplicabilidad y Fiabilidad; requisito para Precisión y Comparabilidad); dicen qué mirar, no cuánto pesa cada criterio ([D-125](decisions.md#d-125); precisa el papel 2 de D-115);
  - marca de dimensión de comparación en el requisito: si no lo es, Comparabilidad es NA, decidido por el modelo ([D-126](decisions.md#d-126); cierra la excepción pendiente de D-117);
  - las escriben el entrenamiento (tabla por tipo), taxo y PAA (por requisito), con origen, y solo se suman ([D-127](decisions.md#d-127));
  - son criterios breves, no listas de vocabulario; cada una nombra la propiedad que observa y los AC a los que afecta ([D-128](decisions.md#d-128)).
- **estructura** — nuevo módulo [assessment-hints](../10-model/assessment-hints.md) 1.0; índice.
- **canon** (propagación) — [acceptance-criteria](../10-model/acceptance-criteria.md) 1.3, [scoring-systems](../10-model/scoring-systems.md) 1.3, [paa-training](../10-model/paa-training.md) 1.3, [construction-routes](../10-model/construction-routes.md) 1.4, [choice-criteria](../10-model/choice-criteria.md) 1.8, [demand-model](../10-model/demand-model.md) 3.1, [model-training](../10-model/model-training.md) 1.18 (enlaces); glosario (Pistas de valoración, que sustituye a Reglas de AC de un requisito; Marca de dimensión de comparación; NA; Comparabilidad); `CLAUDE.md` raíz (invariante 4).
- **método** — auditoría GSC: [gsc-decision](../20-methods/audit-gsc/gsc-decision.md), [ac-guides](../20-methods/audit-gsc/ac-guides.md), [calibration](../20-methods/audit-gsc/calibration.md), [qa](../20-methods/audit-gsc/qa.md), [execution](../20-methods/audit-gsc/execution.md) e [inputs-outputs](../20-methods/audit-gsc/inputs-outputs.md) 0.3 (NA de Comparabilidad según la marca; enlace a las pistas).
- **gobernanza** — OQ-61 y OQ-65 cerradas; OQ-62 y OQ-66 anotadas; nuevas OQ-68 (formato de las pistas y uso en el perfil del RI) y OQ-69 (cómo se fija la marca de dimensión de comparación).

## 2026-10-27 — Aplicación de los criterios, pertinencia de lo derivado y Fiabilidad · aplicado

- **canon** — `INTAKE 2026-10-27-ac-applicability-and-reliability` (diseño del sistema de reglas de valoración de los AC):
  - los seis criterios se aplican siempre; no hay NA de criterio, salvo el de Comparabilidad, pendiente; NE es una incidencia de la auditoría; el NA del requisito se mantiene ([D-117](decisions.md#d-117)). Enmienda BASE §6.1, FUND §8.1 y el ejemplo de FUND §10.1;
  - Comparabilidad exige contraste cuando la respuesta es una dimensión de comparación de la clase ([D-118](decisions.md#d-118));
  - la prestación derivada de un atributo se decide en la pertinencia: el atributo por sí solo no es pertinente, disponibilidad 0 ([D-119](decisions.md#d-119); enmienda D-090);
  - prueba de derivación: conclusión necesaria con reglas generales, descriptivas y citadas, sin contrafuente ([D-120](decisions.md#d-120));
  - Fiabilidad: nueva definición y lectura refutadora ([D-121](decisions.md#d-121)); tres familias de comprobación, límites del conocimiento del dominio, identificador ausente en Justificación, consistencia por ámbito ([D-122](decisions.md#d-122));
  - se retira P15 · Actualidad ([D-123](decisions.md#d-123)); enmienda BASE §5.3 y FUND §7;
  - consistencia transversal: nueva dimensión de análisis por RI × par de ámbitos, hallazgos sin escala que no modifican el GSC ([D-124](decisions.md#d-124)).
  - Módulos: [acceptance-criteria](../10-model/acceptance-criteria.md) 1.2, [effective-availability](../10-model/effective-availability.md) 1.1, [scoring-systems](../10-model/scoring-systems.md) 1.2, [quality-properties](../10-model/quality-properties.md) 1.3, [evaluation-scopes](../10-model/evaluation-scopes.md) 1.1, [choice-criteria](../10-model/choice-criteria.md) 1.7, [commercial-information](../10-model/commercial-information.md) 1.1 (nota sobre la vigencia), [paa-training](../10-model/paa-training.md) 1.2 (nota sobre las reglas de AC); índice; glosario (NA, NE, Comparabilidad, Fiabilidad, Propiedades de calidad, P14–P18, Prestación derivada de un atributo, Árbol de decisión GSC; nuevos: Prueba de derivación, Consistencia transversal); `CLAUDE.md` raíz (invariantes 2, 4, 5 y 9).
- **método** — auditoría GSC: [gsc-decision](../20-methods/audit-gsc/gsc-decision.md) 0.2 (GSC-02, GSC-03, árbol, estados de excepción, YAML), [ac-guides](../20-methods/audit-gsc/ac-guides.md) 0.2 (Comparabilidad y Fiabilidad reescritas), [property-checks](../20-methods/audit-gsc/property-checks.md) 0.2 (P14, P15 retirada, P18), [evidence](../20-methods/audit-gsc/evidence.md) 0.2 (EV-10, EV-14, tabla por tipo), [calibration](../20-methods/audit-gsc/calibration.md) 0.2 (casos A, H y J, matriz), [relevance](../20-methods/audit-gsc/relevance.md) 0.2 (PF-03), [availability-coverage](../20-methods/audit-gsc/availability-coverage.md) 0.2, [qa](../20-methods/audit-gsc/qa.md), [execution](../20-methods/audit-gsc/execution.md), [inputs-outputs](../20-methods/audit-gsc/inputs-outputs.md), [dossier](../20-methods/audit-gsc/dossier.md) y [README](../20-methods/audit-gsc/README.md) 0.2.
- **gobernanza** — OQ-56 cerrada (D-120); OQ-25 cerrada (D-121 a D-123; el resto pasa a OQ-66); OQ-21 y OQ-61 anotadas; nuevas OQ-65 (NA de Comparabilidad), OQ-66 (comprobaciones de corrección por tipo de dato y reglas del dominio en el modelo de demanda) y OQ-67 (estado cualitativo de la consistencia transversal).

## 2026-10-27 — Clases del piloto de PAA · aplicado

- **canon** — `INTAKE 2026-10-27-paa-pilot-classes` (T-042): el piloto de medición del entrenamiento de PAA usa las clases de los 14 casos de referencia (12 clases distintas por clave del modelo), no 3-4 clases elegidas ([D-116](decisions.md#d-116); D-114 enmendada). [paa-training](../10-model/paa-training.md) 1.1; glosario.

## 2026-10-27 — Entrenamiento propio de PAA · aplicado

- **canon** — `INTAKE 2026-10-27-paa-training` (T-042): PAA tiene un entrenamiento propio, independiente del de taxo, que refina solo las semillas, el vocabulario de criterios de elección y los parámetros de las reglas de lectura; crear o retirar reglas lo decide el usuario; empieza por un piloto de medición de 3-4 clases ([D-114](decisions.md#d-114)). Escribe en el catálogo con cuatro papeles aditivos (requisitos «paa», reglas de AC de un requisito, inferidas, aportaciones) y deja un registro para taxo sobre los requisitos de las referencias: un solo escritor por requisito ([D-115](decisions.md#d-115); D-104 enmendada).
- **estructura** — nuevo módulo [paa-training](../10-model/paa-training.md) 1.0; [construction-routes](../10-model/construction-routes.md) 1.3, [choice-criteria](../10-model/choice-criteria.md) 1.6 y [model-training](../10-model/model-training.md) 1.17 (enlaces y pendientes); índice; glosario (Entrenamiento de PAA, Reglas de AC de un requisito, Registro de revisiones de PAA).
- **gobernanza** — OQ-58 y OQ-59, cerradas en el fondo por D-115; nuevas OQ-61 (reglas de AC), OQ-62 (paso de aceptación y estado), OQ-63 (registro para taxo) y OQ-64 (métricas del entrenamiento de PAA).

## 2026-10-27 — Piel en sábanas: cubierta · aplicado

- **canon** — `INTAKE 2026-10-27-paa-skin-covered`: la piel en sábanas queda cubierta por `cat.sabanas/02` (D-106); D-108 retira el candidato de piel y D-109 su ejemplo, que contaba una pregunta genérica como prueba (b); la partición de `cat.fundas-de-almohada/04` por tema sigue vigente ([D-113](decisions.md#d-113)).

## 2026-10-27 — Sujeción de la bajera: cubierta · aplicado

- **canon** — `INTAKE 2026-10-27-paa-bottom-sheet-hold`: la sujeción de la bajera queda cubierta por `inf/02` y `cat.sabanas-ajustables/01`; lo que queda depende del colchón de quien compra (C3) ([D-112](decisions.md#d-112); sustituye D-111). [choice-criteria](../10-model/choice-criteria.md) 1.5 (ejemplo mínimo).

## 2026-10-27 — Criterios de clasificación de las preguntas PAA (segunda ronda) · aplicado

- **canon** — `INTAKE 2026-10-27-paa-classification-criteria-2` (divergencias de la reclasificación con el reglamento PAA v2, resueltas por el usuario en T-041): preguntas de grado, C2 sobre el requisito ([D-110](decisions.md#d-110)); sujeción de la bajera como candidato ([D-111](decisions.md#d-111), sustituida por [D-112](decisions.md#d-112)). [choice-criteria](../10-model/choice-criteria.md) 1.4 (lectura de las preguntas, salvedad de D-106 por D-109 y ejemplo mínimo).
- **método** — precisiones de la separación por dimensión: preguntas distintas para la prueba (a), cualquier atributo de lista, lista ausente en la clase, sacar sin preguntas ([D-109](decisions.md#d-109); precisa D-103 y acota D-106). [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.31; glosario (Separación por dimensión).

## 2026-10-27 — Criterios de clasificación de las preguntas PAA · aplicado

- **canon** — `INTAKE 2026-10-27-paa-classification-criteria` (dudas de la primera clasificación con un agente, T-040, resueltas por el usuario en T-041): lectura sobre la oferta antes de C2 y confección casera fuera del perímetro ([D-100](decisions.md#d-100)); confirmaciones y aportaciones de precisión que salen de PAA ([D-101](decisions.md#d-101)); basta una pregunta para apoyar un candidato ([D-102](decisions.md#d-102)); criterios de elección intermedios ([D-104](decisions.md#d-104)); tacto por tipo y rasgo «sensorial» ([D-105](decisions.md#d-105)); un requisito de certificación cubre la prestación cuya declaración recoge ([D-106](decisions.md#d-106)); candidatos PAA de la clase de sábanas ([D-108](decisions.md#d-108)). [choice-criteria](../10-model/choice-criteria.md) 1.3 (nueva sección «Lectura de las preguntas de PAA», ejemplo mínimo actualizado); [construction-routes](../10-model/construction-routes.md) 1.2; [requirement-description](../10-model/requirement-description.md) 1.1 (ejemplos actualizados); [model-training](../10-model/model-training.md) 1.16 (rasgo «sensorial»); glosario (Criterio de elección intermedio, Lectura sobre la oferta, Separación por dimensión, Rasgo).
- **método** — separación por dimensión en los atributos de lista ([D-103](decisions.md#d-103)) y requisitos repetidos en bloques hermanos con la misma pregunta y la misma descripción ([D-107](decisions.md#d-107)): [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.30.
- **gobernanza** — nuevas OQ-59 (PAA como prueba de la pertinencia de los AC, en propuesta) y OQ-60 (presentación de un requisito repetido según la pieza).

## 2026-10-27 — PAA propone requisitos nuevos · aplicado

- **canon** — `INTAKE 2026-10-27-paa-new-requirements`: PAA propone requisitos nuevos también desde preguntas factuales sobre la oferta que ningún requisito responde, si cumplen C1–C4; origen «paa» en ambos caminos ([D-099](decisions.md#d-099); enmienda D-094 y D-097). [construction-routes](../10-model/construction-routes.md) 1.1; [choice-criteria](../10-model/choice-criteria.md) 1.2; glosario (PAA); README del motor PAA.
- **gobernanza** — nueva OQ-58: entrada en el catálogo del requisito candidato de PAA y formato de la pregunta como fuente.

## 2026-10-27 — People Also Ask como vía de construcción, MPIR aparcado y excepción de legitimidad · aplicado

- **canon** — `INTAKE 2026-10-27-paa-construction-route` (T-039):
  - People Also Ask (PAA) de google.es es una vía de construcción del modelo de demanda: reconoce criterios de elección y confirma requisitos y cuestiones inferidas; solo preguntas, sin información resolutiva ([D-094](decisions.md#d-094); enmienda D-009 y D-036);
  - el MPIR queda aparcado: su papel en la construcción lo cumple PAA ([D-095](decisions.md#d-095));
  - excepción a D-042: el motor PAA no aplica el robots.txt de Google, para investigación y uso interno, con sus límites de ejecución ([D-096](decisions.md#d-096));
  - origen «paa» para los requisitos que entran solo por PAA y para las inferidas que confirma ([D-097](decisions.md#d-097)).
- **estructura** — la construcción del modelo pasa al módulo nuevo [construction-routes](../10-model/construction-routes.md) 1.0 por tamaño ([D-098](decisions.md#d-098)); [demand-model](../10-model/demand-model.md) 3.0; índice de docs/README (4g); glosario: vía de construcción, origen de un requisito, PAA y MPIR aparcado.
- **método** — [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#cuestiones-inferidas) 1.29 (origen «paa»; PAA confirma las inferidas); [MPIR](../20-methods/mpir/README.md) 1.4 (aviso de aparcado); [product-taxonomy](../20-methods/product-taxonomy/README.md) 1.8 y [sources](../20-methods/product-taxonomy/sources.md) 1.2: vías vigentes y MPIR aparcado; campos de un requisito con el origen «paa».
- **editorial** — [choice-criteria](../10-model/choice-criteria.md) 1.1 y [study-class](../10-model/study-class.md) 1.6: enlaces a construction-routes; study-class anota que el contraste de especializaciones con el MPIR queda suspendido.
- **gobernanza** — OQ-57 cerrada → D-094, D-096; OQ-01 anotada; sección C de open-questions marcada como aparcada. Fuera de docs: README del motor PAA, `demand-engine/README.md` y `CLAUDE.md` sin la marca «pendiente de registrar». Validación del origen «paa» en `bin/model`: T-040.

## 2026-10-27 — Criterios de elección, prestaciones derivadas y descripción de los requisitos · aplicado

- **canon** — `INTAKE 2026-10-26-choice-criteria-and-descriptions`:
  - derivar una prestación de un atributo no resuelve el requisito de la prestación; lo dictamina la valoración de los AC y el requisito tiene que existir en el modelo ([D-090](decisions.md#d-090)): [acceptance-criteria](../10-model/acceptance-criteria.md#interpretación) 1.1;
  - un criterio de elección genera un requisito cuando cumple C1–C4 ([D-091](decisions.md#d-091)): módulo nuevo [choice-criteria](../10-model/choice-criteria.md) 1.0;
  - los requisitos llevan una descripción de tres partes ([D-092](decisions.md#d-092)), que es prosa y no repite la información resolutiva ([D-093](decisions.md#d-093)): módulo nuevo [requirement-description](../10-model/requirement-description.md) 1.0;
  - [demand-model](../10-model/demand-model.md) 2.22 y [resolving-information](../10-model/resolving-information.md) 1.9 (regla 6 y distinción con la descripción).
- **método** — [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo) 1.28: la descripción entre los campos de un requisito y el criterio de elección como fundamento. [MPIR](../20-methods/mpir/README.md) 1.3: enlace a los criterios de elección.
- **estructura** — índice de [docs/README](../README.md) (4e, 4f) y glosario: descripción, criterio de elección y prestación derivada de un atributo.
- **gobernanza** — OQ-03 anotada (relación de la descripción con el perfil del RI); nuevas OQ-56 (frontera operativa de la prestación derivada en los AC) y OQ-57 (PAA como vía de construcción, que el artefacto deja fuera). Implantación de C1–C4: T-040; de la descripción en el catálogo: pendiente. Nueva [I-40](issues.md#i-40): estado de implantación de la información resolutiva en el catálogo, detectada por el revisor.

## 2026-10-26 — Resolución de I-36 a I-39 · aplicado

- **canon** — [study-class](../10-model/study-class.md#composición-de-la-clase) 1.5: «juego» aporta qué piezas incluye y cuántas de cada una; las medidas, los bloques de cada pieza ([D-086](decisions.md#d-086)). [model-training](../10-model/model-training.md) 1.15: una cuestión con fuente que el bloque ni pregunta ni excluye es una propuesta al bloque, que la compilación incorpora ([D-088](decisions.md#d-088)).
- **método** — [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) 1.27:
  - la regla 3 prevalece sobre la forma de sí o no con detalle ([D-087](decisions.md#d-087));
  - las propuestas al bloque (D-088);
  - el precio anterior (Ley 7/1996, art. 20.1) y el precio por unidad de medida (RD 3423/2000, art. 3.2) en la capa general ([D-089](decisions.md#d-089)).

  [subclasses](../20-methods/product-taxonomy/subclasses.md) 1.8 y [cases](../20-methods/product-taxonomy/cases.md) 1.12 con el alcance de «juego».
- **gobernanza** — I-36 a I-39 resueltas por decisión del usuario; no queda ninguna incidencia abierta. D-036 y D-060 anotadas en la tabla. Implantación (catálogo, `gen.json`, reglamento, DRAFTING y código): T-036.

## 2026-10-26 — Los cambios, en las condiciones de devolución · aplicado

- **canon** — [D-085](decisions.md#d-085), que sustituye a D-083: los cambios son condiciones de devolución y cambio, no de la oferta. Se retira `gen.cambios`; `gen/11` pregunta también por el cambio y `gen/26`, por su coste. La aplicación vuelve a la lista de D-066: [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.21 y glosario. El ejemplo de `gen/11` en [resolving-information](../10-model/resolving-information.md#ejemplo-mínimo) 1.8 ya no rechaza el plazo de cambio.
- **método** — [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.26 (tabla y disparadores) y [cases](../20-methods/product-taxonomy/cases.md) 1.11.
- **gobernanza** — D-034, D-047, D-064 y D-083 anotadas en la tabla; I-35 resuelta por D-085.

## 2026-10-26 — La información resolutiva de la capa general sin aprobación del usuario · aplicado

- **canon** — [D-084](decisions.md#d-084): las listas de información resolutiva de la capa general las redacta Claude sin aprobación del usuario, que las revisa cuando lo pide; sustituye en ese punto a D-063 y D-069. [resolving-information](../10-model/resolving-information.md) 1.7 y [model-training](../10-model/model-training.md) 1.14.
- **gobernanza** — D-063 y D-069 anotadas en la tabla; D-080, D-083 e I-39 sin el paso de aprobación.

## 2026-10-26 — Resolución de I-30 a I-35 (tanda de control T-032) · aplicado

- **canon** — la aplicación suma una condición de la oferta, los cambios admitidos, con su bloque condicionado `gen.cambios` ([D-083](decisions.md#d-083)): [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.20 y glosario (aplicación).
- **método** — [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#capa-general) 1.25:
  - un descuento de toda la tienda activa `gen.descuento` aunque dependa de una acción del comprador ([D-078](decisions.md#d-078));
  - la ficha identifica la unidad de exposición cuando sitúa en la exposición la unidad que se vende ([D-079](decisions.md#d-079));
  - quien comercializa el producto con su nombre o marca responde la pregunta del fabricante, con una aportación nueva de origen «marco» en `gen/17` ([D-080](decisions.md#d-080));
  - una garantía nombrada sin contenido ni condiciones no activa `gen.garantia-comercial` ([D-081](decisions.md#d-081));
  - varias opciones visibles en un selector activan `gen.variantes`; una sola, no ([D-082](decisions.md#d-082));
  - nuevo bloque `gen.cambios` en la tabla y en los disparadores, con dos requisitos principales: plazo y condiciones del cambio, y su coste ([D-083](decisions.md#d-083); importancia, división y lista elegidas por el usuario en una segunda ronda).
- **gobernanza** — I-30 a I-35 resueltas por decisión del usuario («Aplica según recomendado»); siguen abiertas I-36 a I-39. D-034, D-047, D-052, D-057, D-066, D-069 y D-074 anotadas en la tabla. Implantación en `demand-engine/catalog/gen.json` (capa general 0.6) y en el reglamento del clasificador: T-035.

## 2026-10-26 — Nombre del modelo de demanda con la composición completa · aplicado

- **canon** — [D-077](decisions.md#d-077): el nombre del modelo nombra los bloques de sector delante de las categorías («Sectores › Categorías (alias) · especializaciones»). Sustituye en ese punto a [D-038](decisions.md#d-038) («los bloques universales y los de sector no se nombran») y a la sintaxis del nombre de [D-047](decisions.md#d-047). Fuente: `INTAKE 2026-10-26-model-name-full-composition`.
  - [demand-model](../10-model/demand-model.md#composición-e-identidad-del-modelo) 2.19: sintaxis del nombre, ejemplo del juego de toallas y ejemplo hipotético de los televisores.
  - glosario: el nombre del modelo de demanda.
- **método** — ejemplos del nombre con sus sectores en [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#denominación) 1.24 y [cases](../20-methods/product-taxonomy/cases.md) 1.9.
- **gobernanza** — tabla de decisiones: D-038 y D-047 anotadas como sustituidas en el nombre por D-077.

## 2026-10-26 — Incidencias de la tanda de control T-032 · aplicado

- **gobernanza** — diez incidencias nuevas, abiertas y con propuesta. Salen de la tanda de control con el reglamento v3 y las reglas 6, comparada con la v4 (informe `demand-engine/training/reports/2026-10-26-t032-control-report.md`):
  - [I-30](issues.md#i-30): descuento de toda la tienda condicionado a una acción del comprador.
  - [I-31](issues.md#i-31): unidad de exposición que la ficha identifica sin nombrarla.
  - [I-32](issues.md#i-32): fabricante de un producto que la tienda importa y vende con su marca.
  - [I-33](issues.md#i-33): garantía nombrada sin contenido ni condiciones.
  - [I-34](issues.md#i-34): variantes con opciones visibles sin nombre y selectores de una sola opción.
  - [I-35](issues.md#i-35): política de cambios sin pregunta en la capa general.
  - [I-36](issues.md#i-36): alcance de la especialización «juego».
  - [I-37](issues.md#i-37): pregunta de sí o no con detalle cuyas partes toman otro rasgo o importancia.
  - [I-38](issues.md#i-38): cuestiones con fuente en las referencias que el bloque no recoge.
  - [I-39](issues.md#i-39): aportaciones que fija la norma ausentes de las listas de la capa general.

  No cambia el canon.

## 2026-10-26 — Update «resolución de las incidencias abiertas» · aplicado

- **canon** — `demand-model` 2.18: el efecto de la relevancia sobre la base de D-030 lo mide la validación automática ([D-072](decisions.md#d-072)). `resolving-information` 1.6, `model-training` 1.13 y glosario: «aportación» siempre con su complemento fuera de su módulo; nueva entrada «Aportación al modelo de demanda» ([D-075](decisions.md#d-075)).
- **método** — casos corregidos en `subclasses` 1.7 y `cases` 1.8: polar, tapicería de piel y `warmth-level` ([D-071](decisions.md#d-071)). `sampling-capture` 1.4, `mpir` (README) 1.2 y `operation-validation`: renderizado siempre con navegador real ([D-073](decisions.md#d-073)). `requirement-blocks` 1.23: mensajes comunes de la tienda, que también activan el bloque condicionado que declaran ([D-074](decisions.md#d-074)) y opiniones del producto u oferta ([D-076](decisions.md#d-076)). `interpretation-transfer`, `operation-validation` y `concepts-architecture` 1.1: «aportación al modelo de demanda».
- **gobernanza** — `docs/CLAUDE.md`: el estado «vigente» incluye lo que un intake procesado formula como vigente ([D-070](decisions.md#d-070)). I-11, I-13, I-15, I-17, I-18, I-23, I-25 e I-29 resueltas; no queda ninguna incidencia abierta. D-016, D-042, D-064 y D-066 anotadas en la tabla. Revisión independiente aplicada. Fuente: `INTAKE 2026-10-26-open-issues-resolution`. Implantación en el reglamento del clasificador (I-23, I-29): T-034.

## 2026-10-26 — Update «incidencias de la capa general» · aplicado

- **canon** — la aplicación suma tres condiciones de la oferta: garantía comercial, asistencia posventa y opiniones publicadas, con sus bloques condicionados `gen.garantia-comercial`, `gen.posventa` y `gen.opiniones` ([D-066](decisions.md#d-066)). `demand-model` 2.17 y glosario. En los bloques de categoría, la norma que es fuente de un requisito da aportaciones de origen «referencias» ([D-068](decisions.md#d-068)). Las listas de información resolutiva de la capa general quedan aprobadas ([D-069](decisions.md#d-069)). `resolving-information` 1.4 y 1.5: el ejemplo de `gen/11` se marca como anterior a la división, y los pendientes se ponen al día.
- **método** — `requirement-blocks` 1.22:
  - tabla de la capa general con los tres bloques nuevos;
  - disparadores con su relación con `gen/12` y `gen/15`;
  - el bloque universal vuelve a tener un solo condicionado (D-052), también en la tabla de bloques;
  - se retira `gen.precio-personalizado/01`, y el 97.1.f queda como apoyo del disparador ([D-067](decisions.md#d-067));
  - formato del catálogo: la información resolutiva ya se registra y admite la norma como fuente;
  - nota en los ejemplos de denominación, anteriores a D-066.

  `cases` con la misma nota en el sofá de exposición.
- **gobernanza** — I-26, I-27 e I-28 resueltas; nueva I-29 (opiniones sobre la tienda frente a las del producto); D-034, D-047, D-052, D-063 y D-065 anotadas en la tabla (D-052, con la ampliación de D-065 sin efecto). Revisión independiente aplicada. Fuentes: `INTAKE 2026-10-26-general-layer-issues` e `INTAKE 2026-10-26-general-layer-resolving-approval`. Implantación en `demand-engine/catalog/gen.json` (capa general 0.5) y en el reglamento del clasificador: T-033.

## 2026-10-26 — Update «reglas de formulación en la capa general» · aplicado

- **método** — las reglas de formulación de D-060 se aplican también a la capa general, con la regla 3 extendida a las partes de igual rasgo e importancia que se responden por separado ([D-065](decisions.md#d-065), dos rondas): se dividen `gen/01`, `gen/02`, `gen/04`, `gen/06`, `gen/11`, `gen/12`, `gen/15`, `gen.variantes`, `gen.unidad-no-nueva`, `gen.descuento`, `gen.precio-personalizado` (parámetros como inferida), `gen.elementos-digitales` y `gen.suscripcion`; quedan juntos `gen/16`, `gen/17`, `gen/18` y `gen/19`; `gen/09` pasa a pregunta. Los condicionados nuevos sobre hechos de la oferta van en el bloque universal (amplía D-052). `requirement-blocks` 1.21.
- **canon** — `resolving-information` 1.3 y `model-training` 1.12: en la capa general, las aportaciones que se redactan sin apoyo en la ley se registran como inferidas y provisionales (D-065, que anota D-063).
- **gobernanza** — D-034, D-052, D-060 y D-063 anotadas en la tabla; OQ-45 anotada (candidatas resueltas); nuevas I-26 (condicionados de la oferta fuera de la aplicación), I-27 (`gen.precio-personalizado/01` repite su disparador) e I-28 (origen de las aportaciones que salen de una norma en los bloques de categoría, registrada al implantar T-031); fila de I-25, que faltaba en la tabla. Revisión independiente aplicada. Fuentes: `INTAKE 2026-10-26-general-layer-formulation` e `INTAKE 2026-10-26-general-layer-formulation-2`. Implantación en `demand-engine/catalog/gen.json` (versión 0.4): T-031.

## 2026-10-26 — Update «aportación resolutiva» · aplicado

- **editorial** — cada entrada de la información resolutiva de un requisito, hasta ahora «tipo», se llama **aportación resolutiva** ([D-064](decisions.md#d-064)); el concepto y las reglas de D-063 no cambian. `resolving-information` 1.1 y 1.2 (con la distinción frente al valor publicado), `demand-model` 2.15 y 2.16, `model-training` 1.11, `requirement-blocks` 1.20, glosario (nueva entrada «Aportación resolutiva» y entrada de información resolutiva reescrita), filas de D-062 y D-063, OQ-03 y OQ-55. Las citas literales de las fuentes conservan «tipo» con nota.
- **gobernanza** — nueva I-25: «aportación» ya tenía otro sentido en el MPIR (aportación al modelo de demanda), contra lo que decía el artefacto; propuesta de distinguirlas con el adjetivo. Revisión independiente aplicada. Fuente: `INTAKE 2026-10-26-resolving-contribution-name`.

## 2026-10-26 — Update «reglas de la información resolutiva» · aplicado

- **estructura** — nuevo módulo `resolving-information` 1.0 (canon): recibe la definición de la información resolutiva (D-062) y sus reglas; índice de `docs/README.md`.
- **canon** — la información resolutiva de cada requisito la compila el entrenamiento desde cuatro orígenes (marco, referencias, fichas reales e inferida); cada tipo guarda su componente, su origen y las tiendas en que se ha observado; un tipo observado se acepta cuando aparece en dos tiendas distintas y aporta a un componente; ninguno se retira por no observarse ([D-063](decisions.md#d-063)). `demand-model` 2.13 (enlace), `model-training` 1.9.
- **método** — `requirement-blocks` 1.18: quién escribe cada origen en el catálogo y en la salida del clasificador.
- **gobernanza** — glosario; OQ-54 cerrada; OQ-03 anotada (relación con el perfil del RI); nueva OQ-55 (salida de los tipos inferidos). Revisión independiente aplicada (`model-training` 1.10, `demand-model` 2.14, `requirement-blocks` 1.19): la capa general admite tipos observados sin tocar preguntas ni importancias (lectura frente a D-045, que queda ampliada como con D-050), «respaldo» y «aporta a un componente» donde faltaban, fila de reembolso restaurada y lista no exhaustiva frente a la prueba de ausencia. Fuente: `INTAKE 2026-10-26-resolving-information-rules`.

## 2026-10-26 — Update «información resolutiva» · aplicado

- **canon** — `demand-model` 2.11: los «tipos de información potencialmente resolutiva» pasan a llamarse **información resolutiva** y se redefinen: para cada requisito, los tipos de información comercial que pueden contribuir a resolverlo, cada uno ligado al componente al que aporta; sirven para localizar información pertinente y para recomendar ([D-062](decisions.md#d-062), sustituye a D-061). Se retira el vocabulario de formas.
- **método** — `requirement-blocks` 1.16: campos de un requisito y ejemplos de la muestra `sofa-cama-luna`.
- **gobernanza** — D-061 sustituida; glosario (entrada renombrada); OQ-53 cerrada (no aplica); nueva OQ-54 (reglas del motor que la determinan). Revisión independiente aplicada (`demand-model` 2.12, `requirement-blocks` 1.17): cita literal, aviso de que aún no se registra, acciones de recomendación, muestra simulada y relación con el perfil del RI en OQ-54. Fuente: `INTAKE 2026-10-26-resolving-information`.

## 2026-10-26 — Update «forma de la respuesta» · aplicado

- **canon** — `demand-model` 2.9: los «tipos de información potencialmente resolutiva» pasan de registro opcional sin definir a campo de cada requisito: la forma de la respuesta, qué clase de dato o afirmación responde la cuestión, con uno o varios valores de un vocabulario cerrado (valor con unidad, valor de lista, sí/no, relación, condición, identidad, acreditación, descripción; en borrador, propuesta). Orienta la localización y el juicio sin prescribir formato ([D-061](decisions.md#d-061)).
- **método** — `requirement-blocks` 1.14: el campo entra en los campos de un requisito; lo registra quien redacta, apoyándose en el tipo de las fuentes, también en la capa general.
- **gobernanza** — glosario (nueva entrada); nueva OQ-53 (ajuste del vocabulario). Descartadas: soporte donde aparece y las dos listas. Revisión independiente aplicada (`demand-model` 2.10, `requirement-blocks` 1.15): el campo sale de la lista de registros opcionales, finalidad según el artefacto (no la localización), distinción frente al rasgo, cita del perfil del RI corregida, capa general fijada con el marco, ejemplos y OQ-53 en «Pendiente». Fuente: `INTAKE 2026-10-26-answer-form`.

## 2026-10-26 — Update «formulación de las cuestiones del catálogo» · aplicado

- **método** — `requirement-blocks` 1.11 y 1.13: nueva sección «Formulación de las cuestiones» con cuatro reglas que se añaden a los criterios de D-043: ninguna condición sobre la existencia de la información; una condición sobre un hecho que afecta solo a una parte pasa a requisito condicionado propio (se mantiene la pregunta de sí o no con su detalle); una necesidad por RI, con división solo cuando las partes tomarían otro rasgo u otra importancia; cada componente con fuente o como cuestión inferida ([D-060](decisions.md#d-060)). Aplazada al trabajo de los AC la granularidad cuando las partes comparten rasgo e importancia; la capa general no cambia sin decisión del usuario. Revisión independiente aplicada (1.13): la regla 4 solo para cuestiones con fuente de referencia, la regla 3 estrecha citada literal y sin anular el criterio 2 de D-043, «necesidad» frente a la RI-03, anclas y anotaciones ajustadas al artefacto.
- **editorial** — `demand-model` 2.8: enlace a las reglas desde los principios de formulación de un RI.
- **gobernanza** — D-043 ampliada; OQ-22 anotada (par de calibración `cat.sofas/13` frente a `cat.sofas/05` y listas de ejemplos); OQ-45 anotada (candidatas de la capa general: `gen/01`, `gen/12`, `gen/15`). Fuente: `INTAKE 2026-10-26-question-formulation` (muestra sobre `sofa-cama-luna`, v4-b).

## 2026-10-26 — «Críticos pocos» fuera del marco · aplicado

- **canon** — `model-training` 1.8: «críticos pocos» sale de los objetivos y características del resultado del marco; cuántos requisitos son críticos lo determinan la prueba y las reglas ([D-059](decisions.md#d-059), precisa D-044). **método** — `requirement-blocks` 1.12: se retira «los críticos son pocos y casi todos generales». I-24 resuelta (no aplica); el reglamento y `DRAFTING.md` se adaptan en T-030. Fuente: `INTAKE 2026-10-26-critical-count-not-a-goal`.

## 2026-10-26 — Precisión «cualquier propiedad» · aplicado

- **editorial** — `model-training` 1.7 y [D-058](decisions.md#d-058): «cualquier propiedad» vale para la excepción por requisito (cualquier propiedad puede ser principal, complementaria o crítica por sus votos en la clase) y para el crítico, no solo para el crítico. El mecanismo de D-058 ya era general; cambia dónde se cita la precisión. Revisión independiente aplicada: notas de enmienda en D-045 y D-055, empate de la excepción en el módulo, la composición textil como lectura de D-043 y título de D-058. Nueva I-24 («críticos pocos» sin métrica). Fuente: `INTAKE 2026-10-26-any-property-precision`.

## 2026-10-26 — Update «color y excepciones por requisito» · aplicado

- **canon** — `model-training` 1.6: la regla de importancia por rasgo es la general y un requisito cuyos votos la contradicen en una clase tiene su propia regla, `imp:<requisito>@<clase>`; cualquier propiedad puede ser crítica si sus votos lo dicen, y desaparece el límite del marco sobre la estética; la métrica de aceptación pasa a ser la coherencia por requisito ([D-058](decisions.md#d-058), enmienda D-045, D-055 y D-056). Glosario (regla inducida, rasgo). Fuente: `INTAKE 2026-10-26-color-and-requirement-exceptions` (T-028).

## 2026-10-26 — Update «revisión del ciclo de entrenamiento de reglas 4» · aplicado

- **canon** — `model-training` 1.5: el crítico se decide por requisito y clase, con la misma prueba en todas las clases, y la medida descriptiva puede ser crítica si lo dicen los votos de su clase; en un empate se queda lo que había; nueva métrica, coherencia del crítico ([D-055](decisions.md#d-055), enmienda D-045 y D-043, criterio 1); el vocabulario de rasgos queda abierto: los agentes proponen y votan rasgos, que entran cuando ganan en un requisito, y pueden ser críticos los que dicen qué se vende ([D-056](decisions.md#d-056), enmienda D-045 y D-051).
- **canon** — `study-class` 1.4: la hoja más específica entra como categoría aunque herede todos sus requisitos; una hermana que nombra otra característica, como alias; la unidad de exposición identificada en la ficha es estado declarado ([D-057](decisions.md#d-057), precisa D-033 y D-037).
- **método** — `requirement-blocks` 1.10: rasgo del vocabulario abierto y criterio 1 con D-055.
- **gobernanza** — I-20, I-21 e I-22 resueltas; nueva I-23 (mensajes comunes de la tienda); OQ-51, OQ-39 y OQ-43 anotadas (en parte); nueva OQ-52; glosario (rasgo, regla inducida, alias). Descartado: contar las dos ejecuciones de un caso como un solo voto. Fuente: `INTAKE 2026-10-26-training-v4-review` (T-028).

## 2026-10-26 — Hallazgos del ciclo de entrenamiento de reglas 4 · aplicado

- **gobernanza** — OQ-51 anotada con los datos del ciclo (125 votos sobre la medida descriptiva) y una propuesta para el marco, que sigue abierta. Incidencias nuevas: I-20 (rasgos mal etiquetados en los bloques generados en ejecución y fuentes con rasgo ambiguo), I-21 (entrada de una hoja sin requisitos propios y de una hermana) e I-22 (unidad no nueva en el outlet del caso Stressless). Sin cambio de canon. Fuente: informe `demand-engine/training/reports/2026-10-26-v4-report.md` (T-028).

## 2026-10-25 — Update «clasificación del entrenamiento con Claude Code» · aplicado

- **canon** — `model-training` 1.4: el catálogo de entrenamiento se clasifica con agentes de Claude Code, no con llamadas a la API por lotes ([D-054](decisions.md#d-054), enmienda el punto «Ejecución» de [D-045](decisions.md#d-045)). Fuente: `INTAKE 2026-10-25-training-classifier` (T-020, T-026).

## 2026-10-25 — Update «selección del catálogo de entrenamiento» · aplicado

- **canon** — `model-training` 1.3: catálogo de entrenamiento, primera selección: El Corte Inglés, 3 fichas por tipo de producto y 100 tipos (300 fichas), piloto de 30, captura sin desplazamiento ([D-053](decisions.md#d-053)).
- **gobernanza** — OQ-48 anotada (en parte: D-053); siguen abiertas otras tiendas y la relación con el panel del MPIR. Glosario: «Catálogo de entrenamiento». Fuente: `INTAKE 2026-10-25-training-catalog-selection` (T-024).

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
