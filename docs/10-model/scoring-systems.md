---
id: scoring-systems
title: Sistemas de valoración
layer: model
status: vigente
version: 1.4
updated: 2026-10-27
sources: [BASE §6, FUND §8, INTAKE 2026-10-24-prominencia-informativa, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-27-assessment-hints, INTAKE 2026-10-27-web-schema-technical-framework]
---

# Sistemas de valoración

> Los **sistemas de valoración** expresan los resultados de la auditoría desde la satisfacción de cada criterio hasta la resolución de los requisitos y la lectura conjunta de la información comercial y de las interfaces examinadas. — BASE §6

**Denominaciones canónicas:** las de BASE. Las de FUND se admiten como alias ([D-003](../30-governance/decisions.md#d-003)).

## Calidad informativa

### Grado de satisfacción de criterio (GSC)

> Valora **cada criterio de aceptación para un requisito informativo y una interfaz**, a partir de la evidencia observada. Utiliza una escala ordinal de tres niveles […]. La valoración considera la pertinencia del criterio, la suficiencia de la evidencia y la distinción entre una deficiencia comprobada, un criterio **no aplicable** y una situación **no evaluable**. — BASE §6.1

En estas definiciones, «interfaz» y «ámbito» son sinónimos ([D-010](../30-governance/decisions.md#d-010)).

| Valor | Denominación | Interpretación |
|---|---|---|
| **0** | **No** | El aspecto requerido no queda satisfecho, según evidencia suficiente. |
| **1** | **Parcialmente** | Se satisface con limitaciones relevantes para la cuestión y las condiciones examinadas. |
| **2** | **Sí, es suficiente** | Se satisface adecuadamente para esa cuestión y ese ámbito. |

Estados que **no son puntuaciones**:

| Estado | Cuándo procede | Tratamiento |
|---|---|---|
| **No aplicable (NA)** | El requisito no corresponde al ámbito o a la cuestión definida. **No hay NA de criterio**: los seis se aplican siempre; la única excepción es el NA de Comparabilidad en los requisitos que no son dimensión de comparación ([D-126](../30-governance/decisions.md#d-126)). | Se justifica y se separa de las unidades pertinentes. |
| **No evaluable (NE)** | **Incidencia de la auditoría:** una comprobación de un criterio no se pudo hacer (un recurso que no se pudo inspeccionar, un registro externo que no respondió). No es falta de evidencia sobre lo publicado. | **No se equipara a 0.** Se registra qué comprobación falló y su efecto sobre la interpretación. |

El criterio «no aplicable» y la situación «no evaluable» de BASE §6.1 y FUND §8.1 están enmendados por [D-117](../30-governance/decisions.md#d-117) — INTAKE 2026-10-27-ac-applicability-and-reliability.

**Reglas del GSC:**

1. Un **2** expresa la suficiencia del criterio. No implica necesariamente la resolución del requisito completo ni garantiza que cualquier IA responda correctamente.
2. Un **0** expresa la insatisfacción acreditada de la condición del criterio. No implica la imposibilidad universal de resolver la cuestión.
3. **Las cifras son etiquetas ordinales:** sus distancias no son porcentajes ni magnitudes de calidad.
4. **Insatisfacción acreditada no es lo mismo que falta de evidencia.** La insatisfacción tras una comprobación apropiada justifica una valoración negativa. La imposibilidad de hacer una comprobación **requiere un tratamiento diferenciado** (FUND §8.1): es una incidencia (NE). Que un dato no se pueda corroborar no es una incidencia: en Fiabilidad se resuelve con la [lectura refutadora](acceptance-criteria.md#fiabilidad-lectura-refutadora-y-comprobaciones) ([D-121](../30-governance/decisions.md#d-121)). El procedimiento está en [gsc-decision](../20-methods/audit-gsc/gsc-decision.md).
5. **No se declara falsa** una afirmación solo porque no se haya podido verificar externamente.
6. **El juicio se fundamenta en lo observado.** No se decide primero la puntuación para buscar después ejemplos que la respalden.

### Indicador de resolución de requisito informativo (IR)

> Sintetiza el **grado de resolución de cada requisito informativo por interfaz**. Depende de la satisfacción de sus criterios de aceptación y del **impacto relativo** que cada uno tiene sobre la posibilidad de determinar y fundamentar la respuesta. También considera la existencia de criterios indispensables, la aplicabilidad y la cobertura efectiva de la evaluación. — BASE §6.1

Considera, por tanto:

- el **impacto relativo** de cada criterio para la cuestión;
- la existencia de criterios indispensables;
- la aplicabilidad;
- la **cobertura efectiva** de la evaluación.

- **Disponibilidad efectiva = 0 → IR = 0** (regla vigente).
- **No se obtiene** de una suma o media automática de los seis GSC ni tratando la disponibilidad como un séptimo criterio.
- **Escala: IR (0–10)**: mide la capacidad de resolución del RI mediante los criterios de aceptación — INTAKE 2026-10-24-prominencia-informativa. Enmienda FUND §8.2, que no fijaba escala ([D-017](../30-governance/decisions.md#d-017)).
- La **fórmula de agregación** de los GSC en el IR sigue **sin fijar**. Una insuficiencia en un criterio indispensable puede condicionar la resolución aunque los demás se satisfagan. Su traducción a reglas cuantitativas está **pendiente**.

### Estado binario de resolución

> **Estado: propuesta.**

> **Normalización binaria del IR (0/1):** distingue resolución suficiente e insuficiente; la regla de normalización está pendiente de definir. — INTAKE 2026-10-24-prominencia-informativa

Es la noción de RI **«suficientemente resuelto»** que usa la [TRI](#tasa-de-resolución-informativa-tri) ([D-019](../30-governance/decisions.md#d-019)). La regla para pasar del IR (0–10) al estado 0/1 está pendiente ([OQ-31](../30-governance/open-questions.md#g-prominencia-informativa-propuesta)).

### IP y calidad ajustada

> **Estado: propuesta.** El canon está en [informative-prominence](informative-prominence.md).

El **IP (0–100 %)** es el porcentaje de componentes resueltos con soporte en ubicaciones prominentes. La **calidad ajustada** lo usa como modificador secundario, sin cambiar el IR ni su estado binario. Se registran por separado IR, estado binario, IP y calidad ajustada.

### Indicador de calidad informativa (ICI)

> Sintetiza la **calidad informativa de la información comercial expuesta en una interfaz** a partir de los resultados de resolución de sus requisitos pertinentes y de la **importancia relativa** de estos dentro del modelo de demanda. Su interpretación considera las dimensiones informativas, la aplicabilidad de los requisitos y la cobertura de la evaluación. La importancia de un requisito y el impacto de un criterio actúan en niveles distintos. — BASE §6.1

- **El impacto de un criterio** (sobre un RI) y **la importancia de un requisito** (en el catálogo) actúan en niveles distintos.
- Las clases Crítico, Principal y Complementario **no tienen coeficientes numéricos preaprobados**.

### Tasa de resolución informativa (TRI)

*Alias en FUND: «indicador general de resolución informativa».*

> Expresa la **proporción de requisitos informativos suficientemente resueltos** respecto del conjunto pertinente para el ámbito evaluado. Permite apreciar la extensión de la resolución y analizarla **por interfaz, dimensión e importancia relativa**. Su lectura considera las unidades evaluadas, la aplicabilidad, los resultados parciales y la disponibilidad de evidencia suficiente para establecer la resolución. — BASE §6.1

FUND §8.4 precisa que la lectura distingue requisitos resueltos, parcialmente resueltos, no aplicables y no evaluables.

Es un indicador del **alcance de la resolución**. Es distinto del ICI, que también considera la importancia relativa de las necesidades evaluadas.

## Requisitos técnicos

### Tasa de cumplimiento técnico

*Alias en FUND: «indicador general de resolución técnica».*

> Expresa la **proporción de requisitos técnicos generales satisfechos por interfaz** respecto de los que resultan pertinentes para su perfil de implementación. Su interpretación considera la cobertura de las comprobaciones, la naturaleza obligatoria o recomendada de cada condición y los estados de aplicabilidad y evaluación. Caracteriza la capacidad técnica de las interfaces para exponer y hacer consumible la información comercial. — BASE §6.2

FUND §8.5 añade: **No sustituye al diagnóstico informativo ni demuestra por sí misma la resolución de RI.**

- El **perfil de implementación** (respecto del cual un requisito es pertinente, obligatorio o recomendado) y los **estados del requisito técnico** (satisfecho o no satisfecho; NA; NE como incidencia, que no equivale a «no satisfecho») están en [evaluation-scopes](evaluation-scopes.md#perfil-de-implementación) ([D-130](../30-governance/decisions.md#d-130), [D-131](../30-governance/decisions.md#d-131)).
- Cómo entran las obligatorias y las recomendadas en la tasa, sus umbrales y su cobertura siguen **sin fijar**. No se presuponen pesos.

## Lectura integrada, sin confundir unidades

| Nivel | Pregunta de interpretación | Salida |
|---|---|---|
| Disponibilidad efectiva × RI × ámbito | ¿Existe información pertinente efectivamente utilizable? | **0 o 1**. Si es 0, **IR = 0**. |
| Criterio × RI × ámbito | ¿Se satisface este aspecto sobre la información utilizable? | **GSC 0/1/2**; NE si hay una incidencia; NA de Comparabilidad si el requisito no es dimensión de comparación. |
| RI × par de ámbitos | ¿Afirman los ámbitos lo mismo sobre la misma realidad comercial? | **[Consistencia transversal](evaluation-scopes.md#consistencia-transversal):** hallazgos sin escala; no modifican el GSC ni se agregan. |
| RI × ámbito | ¿Puede determinarse y fundamentarse suficientemente la respuesta? | **IR (0–10)** y **estado binario 0/1** (propuesta) |
| RI × ámbito (Web) | ¿Qué parte de lo resuelto tiene soporte en zonas prominentes? | **IP (0–100 %)** y **calidad ajustada** (propuesta; NA en Web Schema.org y Catálogos) |
| Conjunto de RI de un ámbito | ¿Qué calidad informativa ofrece el ámbito respecto de las necesidades relevantes? | **ICI** |
| Cobertura resolutiva | ¿Qué proporción de cuestiones pertinentes se resuelve suficientemente? | **TRI** |
| Requisito técnico × ámbito | ¿Se cumple esta condición de su perfil de implementación? | **Satisfecho / no satisfecho**; NA si no corresponde; NE si hay una incidencia. |
| Controles técnicos por ámbito | ¿Qué proporción de requisitos técnicos pertinentes se cumple? | **Tasa de cumplimiento técnico** |

Los indicadores de **Web** y **Web Schema.org** se interpretan por separado y **no se suman ni se promedian**, porque Web incluye la información de Web Schema.org.

## Pendiente

Ver [open-questions](../30-governance/open-questions.md):

- reglas de síntesis del IR (impacto relativo, aspectos indispensables, aplicabilidad, cobertura) en su escala 0–10;
- regla de normalización binaria del IR, y fórmula y peso de la calidad ajustada (§G);
- universo, importancia, umbrales y estados del ICI y la TRI;
- sistema cuantitativo técnico.

**No deben presuponerse** fórmulas, pesos universales ni límites numéricos por criticidad.

## Relacionado

- [acceptance-criteria](acceptance-criteria.md)
- [effective-availability](effective-availability.md)
- [gsc-decision](../20-methods/audit-gsc/gsc-decision.md): árbol de decisión del GSC (propuesta V1).
- [informative-prominence](informative-prominence.md): IP y calidad ajustada (propuesta).
