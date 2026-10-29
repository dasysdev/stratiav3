---
id: quality-properties
title: Propiedades de calidad (P06–P18)
layer: model
status: vigente
version: 1.5
updated: 2026-10-30
sources: [BASE §5.3, FUND §7, FUND §4.2, GSC0 §9.3, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-30-content-and-markup-scopes]
---

# Propiedades de calidad (P06–P18)

## Definición

> Las **propiedades de calidad** son características observables de la información comercial y de sus condiciones de representación y exposición. Sirven para interpretar hallazgos y fundamentar las valoraciones de los criterios de aceptación. — BASE §5.3, enmendada por [D-007](../30-governance/decisions.md#d-007)

FUND §7 precisa que se consideran **desde el propósito informativo de un RI**. FUND §4.2 y §5.2 establecen que pertenecen exclusivamente al modelo informativo.

**Numeración:** empieza en P06. Los IDs anteriores correspondían a propiedades técnicas de un modelo previo; están **retirados y no se reutilizan** ([D-007](../30-governance/decisions.md#d-007)).

**P15 · Actualidad está retirada** porque no hay forma de evaluarla; el ID no se reutiliza ([D-123](../30-governance/decisions.md#d-123)), que enmienda BASE §5.3 y FUND §7. Lo detectable sigue cubierto por otras vías: una fecha de validez vencida en la captura es un defecto de estructura del dato; un feed desfasado frente a la web, un hallazgo de [consistencia transversal](evaluation-scopes.md#consistencia-transversal); «Agotado» en el contenido con `InStock` en el marcado, otro hallazgo de consistencia transversal, Contenido ↔ Marcado ([D-220](../30-governance/decisions.md#d-220)).

### Informativas y semánticas

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

### Fiabilidad y fundamentación

| ID | Propiedad | Definición |
|---|---|---|
| **P14** | **Exactitud** | Correspondencia de lo representado con los hechos comerciales comprobables. |
| **P16** | **Coherencia** | Consistencia entre afirmaciones referidas a una misma realidad comercial, bajo condiciones y momentos comparables. |
| **P17** | **Trazabilidad** | Posibilidad de identificar y seguir la procedencia y trayectoria de la información. |
| **P18** | **Verificabilidad** | Posibilidad de contrastar las afirmaciones con evidencias o referencias pertinentes. |

## Reglas e invariantes

1. **No son subpuntuaciones.** No se valoran con GSC, con 0/1/2 ni con pesos, y **no se suman ni se promedian** para producir el GSC.
2. **Relación de muchos a muchos con los criterios.** Una propiedad puede fundamentar varios criterios y un criterio puede depender de varias propiedades. La relación concreta depende del **RI, el ámbito y el hallazgo**.
3. **La consecuencia de cada propiedad se explica por separado** para cada criterio afectado.
4. **Pertenecen exclusivamente al modelo informativo.** No son unidades de evaluación del cumplimiento técnico ni sustituyen los controles generales de implementación, aunque ambos análisis observen el mismo recurso o compartan evidencias.
5. Se examinan **las propiedades necesarias** para comprender qué aporta o limita la información pertinente utilizable. No hay una lista obligatoria idéntica para todos los RI.

## Lectura efectiva frente a propiedades semánticas

La **obtención y legibilidad efectiva** de la información pertinente es la única condición de exposición técnica que la evaluación informativa comprueba directamente. Lo hace en la [disponibilidad efectiva](effective-availability.md), como puerta de entrada al análisis del RI. Cuando corresponde, se documenta además **como condición de uso de las evidencias** (FUND §7.3).

Esta legibilidad es **técnica u operativa**: que un dato pueda recuperarse y leerse. No debe confundirse con:

- **P09 · Claridad**, que examina si el significado de lo leído es inequívoco;
- **P10 · Estructuración semántica**, que examina la organización y las relaciones significativas de sus componentes.

Una información puede ser obtenible y legible, pero semánticamente ambigua. También puede estar muy bien redactada en una parte del recurso que el perfil de consumo no permite leer.

## Asociaciones orientativas con los criterios

| Criterio | Propiedades que pueden sustentar su análisis |
|---|---|
| **Concreción** | P06, P07, P08 y P12. |
| **Precisión** | P08, P09, P10 y P13. |
| **Aplicabilidad** | P10, P11 y P12; también P07 según el hallazgo ([D-014](../30-governance/decisions.md#d-014)). |
| **Comparabilidad** | P07, P10, P12 y P13. |
| **Fiabilidad** | P14 y P16. P18 queda en Justificación: la falta del identificador que permitiría verificar un dato cuenta allí ([D-122](../30-governance/decisions.md#d-122)). Sin fuentes externas, ambas se observan con lo publicado en el ámbito y con reglas generales citadas ([D-154](../30-governance/decisions.md#d-154)). |
| **Justificación** | P08, P17 y P18, además de las relaciones de soporte pertinentes. |

Estas asociaciones son **ilustrativas, no cerradas ni automáticas**. La propiedad relevante se elige a partir de la evidencia, el RI y el problema observado. Por ejemplo, la granularidad (P07) puede afectar tanto a la concreción de una respuesta como a su aplicabilidad a una variante concreta.

## Distinciones

- **P16 · Coherencia** frente a **P14 · Exactitud**. Que no haya contradicciones no demuestra exactitud (FUND §6.2); la coincidencia entre representaciones no demuestra exactitud (FUND §4.3).
- *(Propuesta V1, GSC0 EV-12.)* **P17 · Trazabilidad / P18 · Verificabilidad** frente al **registro del auditor**. Que el auditor conserve una captura no confiere esas propiedades a la información del ecommerce.
- **P18 · Verificabilidad** frente a la función **Justificar**. Ver [ai-functions](ai-functions.md#distinciones).

## Pendiente

- Concretar qué observar y cómo comprobar cada propiedad según el RI, el ámbito, la evidencia y la consecuencia informativa. Hay fichas operativas (propuesta V1) en [property-checks](../20-methods/audit-gsc/property-checks.md). Ver [open-questions](../30-governance/open-questions.md).

## Relacionado

- [acceptance-criteria](acceptance-criteria.md)
- [evaluation-architecture](evaluation-architecture.md)
