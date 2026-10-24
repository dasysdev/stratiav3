---
id: open-questions
title: Cuestiones abiertas y parámetros pendientes de calibración
layer: governance
status: pendiente
version: 1.0
updated: 2026-10-24
sources: [FUND §12, GSC0 §18.1-18.3, TAX §11.3, MPIR §15.2, INTAKE 2026-10-24-prominencia-informativa]
---

# Cuestiones abiertas y parámetros pendientes de calibración

Registro consolidado de lo que falta especificar, validar o calibrar. En v0 estaba repartido en cuatro documentos.

- Al cerrar una cuestión, se registra la decisión en [decisions](decisions.md) y aquí se marca el estado `cerrada → D-NNN`.
- **Estados:** `abierta` · `propuesta V1` (hay propuesta operativa pendiente de calibración) · `cerrada`.

Los documentos rectores **ya fijan**:

- el objeto de estudio;
- el modelo de demanda;
- las funciones informativas;
- los tres ámbitos;
- los requisitos técnicos generales;
- la disponibilidad efectiva (binaria, con la regla 0 → IR = 0);
- los seis AC con escala GSC 0–2 y los estados NA/NE;
- las propiedades P06–P18;
- la arquitectura conceptual de los sistemas de valoración. — FUND §12

Los instrumentos operativos (perfiles de RI, pruebas de pertinencia, rutas de resolución) **no introducen nuevos RI, AC, propiedades, indicadores ni escalas**.

## A. Modelo de demanda

| ID | Cuestión | Estado | Dónde se trabaja | Fuente |
|---|---|---|---|---|
| OQ-01 | Contrastar los RI inferidos con fuentes empíricas (consultas reales, investigación de usuarios) y revisar pertinencia, cobertura, solapamientos y fragmentación. | abierta | [demand-model](../10-model/demand-model.md) | FUND §12 |
| OQ-02 | Calibrar las decisiones Crítico / Principal / Complementario con fundamentos y casos comparables. | abierta | [demand-model](../10-model/demand-model.md#importancia-relativa) | FUND §12 |
| OQ-03 | Perfil de resolución y pertinencia del RI: campos necesarios, mínimos reales, estructura, límites, ejemplos y procedimiento de elaboración y validación. | propuesta V1 | [ri-profile](../20-methods/audit-gsc/ri-profile.md) | FUND §12, GSC0 §18.3 |
| OQ-04 | Función de los escenarios de compra como extensión operativa y sus reglas propias de decisión. | abierta | [demand-model](../10-model/demand-model.md#escenarios-de-compra-posible-extensión-no-unidad-de-valoración) | FUND §12 |

## B. Taxonomía de clases de producto

| ID | Cuestión | Estado | Fuente |
|---|---|---|---|
| OQ-05 | ¿Las clases internas admiten varios padres, o habrá un padre principal más facetas y relaciones adicionales? | abierta | TAX §11.3 |
| OQ-06 | Criterios operativos y evidencia mínima para aprobar equivalencias y nuevas subclases. | abierta | TAX §11.3 |
| OQ-07 | Disponibilidad de acceso a SP-API para obtener el árbol vigente de Amazon.es y restricciones de reutilización. | abierta | TAX §11.3 |
| OQ-08 | Selección de ecommerce referentes y casos frontera para el piloto de botas (compartida con MPIR: OQ-11). | abierta | TAX §11.3 |
| OQ-09 | Grado de especialización que reduce la ambigüedad sin fragmentar innecesariamente los modelos de demanda. | abierta | TAX §11.3 |
| OQ-10 | Mecanismo de gobierno, revisión y calendario de actualización de las fuentes externas. | abierta | TAX §11.3 |

Métodos: [product-taxonomy](../20-methods/product-taxonomy/README.md).

## C. MPIR (ecommerce referentes)

| ID | Parámetro por calibrar en el piloto | Estado | Fuente |
|---|---|---|---|
| OQ-11 | Tamaño y combinación del panel de ecommerce por tipo de clase. | abierta | MPIR §15.2 |
| OQ-12 | Número de páginas y productos por perfil y segmento. | abierta | MPIR §15.2 |
| OQ-13 | Umbrales o reglas prácticas de suficiencia de cobertura y de saturación cualitativa. | abierta | MPIR §15.2, §11.2 |
| OQ-14 | Campos finales obligatorios/opcionales y almacenamiento físico de los recursos. | abierta | MPIR §15.2 |
| OQ-15 | Herramientas y selectores por plataforma, navegador y configuración de captura. | abierta | MPIR §15.2 |
| OQ-16 | Taxonomía fina de funciones o señales tras resolver casos fronterizos. | abierta | MPIR §15.2 |
| OQ-17 | Proporción y procedimiento de revisión humana, medición de errores y tratamiento de discrepancias. | abierta | MPIR §15.2 |
| OQ-18 | Política de actualización periódica y antigüedad tolerada de las evidencias. | abierta | MPIR §15.2 |

Métodos: [mpir](../20-methods/mpir/README.md).

## D. Auditoría informativa (localización, evidencias, GSC)

| ID | Cuestión | Estado | Propuesta V1 | Fuente |
|---|---|---|---|---|
| OQ-19 | Pautas de reconocimiento semántico, pertinencia funcional y candidatos fronterizos. Comprobar si los estados de candidato (inicial, pertinente, pendiente, no pertinente) mejoran los resultados sin introducir burocracia excesiva. | propuesta V1 | [relevance](../20-methods/audit-gsc/relevance.md) | FUND §12, GSC0 §18.3 |
| OQ-20 | Pruebas de obtención/legibilidad, registros de cobertura, cobertura suficiente sin porcentaje universal y tratamiento de las comprobaciones inconclusas sin modificar el binario. | propuesta V1 | [availability-coverage](../20-methods/audit-gsc/availability-coverage.md) | FUND §12, GSC0 §18.3 |
| OQ-21 | Guías de los seis AC: pruebas, evidencias, reglas interpretativas y anclajes GSC 0/1/2 y NA/NE. Fronteras 0/1, 1/2 y NE, sobre todo en Fiabilidad y Justificación. | propuesta V1 | [ac-guides](../20-methods/audit-gsc/ac-guides.md) | FUND §12, GSC0 §18.3 |
| OQ-22 | Prueba de materialidad en RI multiatributo o con muchas unidades (p. ej. 8 de 10 variantes con estado). | propuesta V1 | [gsc-decision](../20-methods/audit-gsc/gsc-decision.md) | GSC0 §18.3 |
| OQ-23 | Qué observar y cómo comprobar cada propiedad P06–P18 según el RI, el ámbito, la evidencia y la consecuencia. | propuesta V1 | [property-checks](../20-methods/audit-gsc/property-checks.md) | FUND §12 |
| OQ-24 | Mínimos del registro de evidencias: localización, contenido original, contexto, identidades, condiciones, método, cobertura, reexamen y tratamiento de cambios. | propuesta V1 | [evidence](../20-methods/audit-gsc/evidence.md) | FUND §12, GSC0 §18.3 |
| OQ-25 | Contrastes de exactitud y vigencia proporcionados al tipo de hecho: casos sin fuentes independientes o con actualización volátil. | propuesta V1 | [ac-guides](../20-methods/audit-gsc/ac-guides.md) | GSC0 §18.3 |
| OQ-26 | Formatos de intercambio: campos normalizados, validación y versionado (el YAML actual es ilustrativo). | propuesta V1 | [ri-profile](../20-methods/audit-gsc/ri-profile.md), [evidence](../20-methods/audit-gsc/evidence.md), [gsc-decision](../20-methods/audit-gsc/gsc-decision.md) | GSC0 §18.3 |
| OQ-27 | Calibración y consistencia entre auditores: casos suficientes, parciales, negativos, fronterizos y NA/NE; nivel de concordancia y causas de variación. | propuesta V1 | [calibration](../20-methods/audit-gsc/calibration.md) | FUND §12, GSC0 §18.3 |

## E. Síntesis e indicadores

| ID | Cuestión | Estado | Fuente |
|---|---|---|---|
| OQ-28 | Reglas de síntesis del IR a partir de los GSC: impacto relativo, aspectos indispensables, aplicabilidad y cobertura, **sin fórmulas asumidas**. La escala ya está fijada en 0–10 ([D-017](decisions.md#d-017)). | abierta | FUND §12, §8.2 |
| OQ-29 | ICI e indicadores generales: universo pertinente, importancia relativa, umbrales, estados y cobertura, **sin convertir automáticamente las categorías cualitativas en pesos**. | abierta | FUND §12, §8.3 |

Canon: [scoring-systems](../10-model/scoring-systems.md).

## F. Evaluación técnica

| ID | Cuestión | Estado | Fuente |
|---|---|---|---|
| OQ-30 | Requisitos técnicos por ámbito (perfiles de implementación, obligaciones, recomendaciones, métodos, cobertura) y su sistema cuantitativo. | abierta | FUND §12 |

Canon: [evaluation-scopes](../10-model/evaluation-scopes.md#requisitos-técnicos-generales).

## Qué queda definido de forma general (GSC0 §18.1)

- Contratos y roles: demanda, configuración, ejecución, revisión e informe.
- Ficha operativa del RI y prueba de su congruencia.
- Exploración general, dirigida y ampliada; selección por pertinencia funcional.
- Separación entre pertinencia, disponibilidad, satisfacción de AC y resolución del RI.
- Reglas sobre relaciones sustentadas y rechazo de conjeturas comerciales.
- Disponibilidad binaria, cobertura de ausencias y tratamiento procedimental de casos inconclusos.
- Registro de evidencias originales, contexto y conexiones; hallazgos y juicios separados.
- Preguntas y pruebas generales por P06–P18, con anclajes provisionales para cada AC.
- Reglas transversales 0/1/2, NA/NE, materialidad, QA y salida para informe.

## G. Prominencia informativa (propuesta)

| ID | Cuestión | Estado | Fuente |
|---|---|---|---|
| OQ-31 | Regla de normalización binaria del IR (0–10 → 0/1). | abierta | INTAKE 2026-10-24-prominencia-informativa |
| OQ-32 | Ubicación exacta de las zonas prominentes en HTML. | abierta | INTAKE 2026-10-24-prominencia-informativa |
| OQ-33 | Identificación de los componentes informativos que cuenta el IP (relación con los componentes sustantivos y auxiliares del perfil de RI) y tratamiento de las rutas alternativas de resolución, incluidas las respuestas derivadas no prominentes. | abierta | INTAKE 2026-10-24-prominencia-informativa, D-018 |
| OQ-34 | Fórmula y peso del modificador: calidad ajustada. | abierta | INTAKE 2026-10-24-prominencia-informativa |
| OQ-35 | Posibles duplicidades del IP con aspectos ya recogidos por los AC, y su encaje con FUND §2.3 y PR-06 (no imponer formato ni ubicación preferida). | abierta | INTAKE 2026-10-24-prominencia-informativa, D-018 |
| OQ-36 | Reglas de prominencia para Web Schema.org y Catálogos distribuidos, si procede (hasta entonces, IP = NA). | abierta | INTAKE 2026-10-24-prominencia-informativa |

Canon: [informative-prominence](../10-model/informative-prominence.md).

## Límites de generalización (GSC0 §18.2)

Cada modelo de demanda o auditoría debe aportar:

- la pregunta y la necesidad concretas del RI, con su dimensión, clase, objeto, aplicabilidad e importancia cualitativa;
- sus componentes constitutivos, desagregación, alcance, relaciones y condiciones;
- la pertinencia de cada ámbito y su perfil de consumo;
- la entidad u oferta concreta y sus recursos comerciales accesibles;
- la información realmente encontrada, sus condiciones y la materialidad de las limitaciones respecto de esa cuestión.

**No se pueden establecer universalmente** los atributos obligatorios, todas las unidades comerciales, la cantidad suficiente de variantes, los tiempos máximos de actualización ni el número de comprobaciones para toda clase de oferta.

## Orden metodológico recomendado (FUND §12)

1. Marco común de evaluación.
2. Caracterización de los RI.
3. Protocolo de localización y pertinencia.
4. Protocolo transversal de evidencias.
5. Guías de propiedades y de cada AC.
6. Fase de calibración.

La especificación de la búsqueda y de la evidencia **precede** al cierre de los anclajes GSC. Una posterior **Skill de auditoría** implementará las guías consolidadas, sin sustituirlas por decisiones libres del modelo.
