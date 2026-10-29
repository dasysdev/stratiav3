---
id: informative-prominence
title: Prominencia informativa, IP y calidad ajustada
layer: model
status: propuesta
version: 1.2
updated: 2026-10-30
sources: [INTAKE 2026-10-24-prominencia-informativa, INTAKE 2026-10-29-oq-review, INTAKE 2026-10-30-content-and-markup-scopes]
---

# Prominencia informativa, IP y calidad ajustada

> **Estado: propuesta.** Es una propuesta metodológica provisional, incorporada desde el intake ([D-018](../30-governance/decisions.md#d-018)). Sigue activa, con las zonas prominentes fijadas, y se trabaja después de la síntesis del IR ([D-203](../30-governance/decisions.md#d-203)). Fórmula y peso de la calidad ajustada, identificación de componentes, duplicidades con los AC y reglas fuera de HTML están pendientes, en espera de la síntesis del IR.

## Definición

> **Objetivo:** incorporar la **prominencia de la información** a la valoración de calidad sin confundir la ubicación de las evidencias con la capacidad de resolver un requisito informativo (RI). — INTAKE 2026-10-24-prominencia-informativa

### Clasificación binaria de prominencia (HTML)

| Valor | Condición | Zonas |
|---|---|---|
| **1 — Prominente** | La información que sustenta el componente aparece en una zona de alta prominencia. | Solo `<title>` (metatítulo), metadescripción y `H1`. |
| **0 — No prominente** | No existe soporte suficiente para ese componente en una de esas zonas. | Resto del contenido, incluidas la descripción inicial, las descripciones extensas, las tablas, las especificaciones y las secciones secundarias. |

Zonas prominentes enmendadas por [D-203](../30-governance/decisions.md#d-203): la «descripción inicial o síntesis destacada» del intake sale de la lista.

> La clasificación se aplica **a cada componente informativo**, no al RI completo. Una simple mención en una zona prominente no basta: debe aportar el contenido necesario para sustentar el componente. — INTAKE

### IP

> **IP (0–100 %):** expresa el porcentaje de componentes informativos efectivamente resueltos que cuentan con soporte suficiente en ubicaciones prominentes. — INTAKE

**IP = 100 × (C / N)**

- **C:** número de componentes informativos efectivamente resueltos con soporte suficiente en una ubicación prominente.
- **N:** número total de componentes informativos efectivamente resueltos considerados en la evaluación.

### Calidad ajustada

> **Calidad ajustada:** utiliza el IP como modificador secundario, sin cambiar el IR original ni su clasificación binaria. — INTAKE

La fórmula y el peso del modificador están **pendientes**, en espera de la síntesis del IR ([OQ-34](../30-governance/open-questions.md#g-prominencia-informativa-propuesta)). No se calcula mientras no se definan.

## Reglas e invariantes

1. **El IR no se modifica.** El IP no altera el [IR](scoring-systems.md#indicador-de-resolución-de-requisito-informativo-ir) ni su [estado binario de resolución](scoring-systems.md#estado-binario-de-resolución).
2. **Influencia limitada.** El IP diferencia la calidad **dentro de un mismo estado binario de resolución**.
3. **Sin compensación.** Una mayor prominencia no convierte un RI insuficientemente resuelto en suficiente ni compensa carencias informativas.
4. **Recuento.** Cada componente se cuenta una sola vez, aunque aparezca repetido. No se fragmenta artificialmente la información para aumentar el número de componentes.
5. **N = 0 → IP no aplicable** (NA).
6. **La prominencia no presupone suficiencia.** La lista de zonas prominentes ([D-203](../30-governance/decisions.md#d-203)) no presupone que los contenidos no prominentes tengan menor suficiencia o precisión.
7. **Registro separado.** Se registran por separado **IR, estado binario, IP y calidad ajustada**.
8. **Nivel y ámbito** (interpretación de [D-018](../30-governance/decisions.md#d-018)):
   - se calcula por **RI × ámbito**, como el IR;
   - la clasificación está definida para HTML, es decir, para el ámbito **Contenido** (antes Web, [D-220](../30-governance/decisions.md#d-220)). La metadescripción no forma parte de Contenido: ⚠ [OQ-91](../30-governance/open-questions.md#g-prominencia-informativa-propuesta);
   - en **Marcado** y **Catálogos distribuidos** el IP es **NA** ([D-203](../30-governance/decisions.md#d-203)). Las reglas específicas, si proceden, esperan a la síntesis del IR ([OQ-36](../30-governance/open-questions.md#g-prominencia-informativa-propuesta)).

## Distinciones

- **IP frente a IR.** El IR mide la capacidad de resolución mediante los criterios de aceptación. El IP mide **dónde** está el soporte de lo ya resuelto. Mide una característica de la representación, no la suficiencia.
- **IP frente a [disponibilidad efectiva](effective-availability.md).** La disponibilidad pregunta si existe información pertinente obtenible y legible. El IP solo cuenta componentes **ya resueltos** y clasifica su ubicación.
- **IP frente a AC y propiedades P06–P18.** El IP no es un criterio de aceptación ni una propiedad de calidad. Las posibles duplicidades con aspectos ya recogidos por los AC están pendientes de validar ([OQ-35](../30-governance/open-questions.md#g-prominencia-informativa-propuesta)).
- **Prominencia informativa frente a «prominencia editorial» del [MPIR](../20-methods/mpir/README.md).** En el MPIR, la prominencia editorial de los referentes **no** se convierte en importancia relativa de los RI. Aquí, la prominencia es una característica observada en el ecommerce auditado que modifica la calidad ajustada. Son conceptos distintos.

## Relación con el canon previo

El intake prevalece ([D-016](../30-governance/decisions.md#d-016)). Hay dos tensiones con el canon que se mantienen como pendientes de validar, sin bloquear la propuesta:

- **FUND §2.3 y PR-06.** Ambos dicen que facilitar la interpretación no equivale a imponer un formato único ni a penalizar la representación por no usar una ubicación preferida. El IP atenúa esa tensión porque no toca el IR y no presupone menor suficiencia de lo no prominente ([OQ-35](../30-governance/open-questions.md#g-prominencia-informativa-propuesta)).
- **Respuestas derivadas** ([D-006](../30-governance/decisions.md#d-006)). Los componentes resueltos mediante rutas de relación (p. ej. `talla → SKU → estado`) pueden no estar en zonas prominentes. Su resolución (IR) no se penaliza; su tratamiento en el IP es parte de las «rutas alternativas de resolución» pendientes ([OQ-33](../30-governance/open-questions.md#g-prominencia-informativa-propuesta)).

## Ejemplo mínimo

De cuatro componentes resueltos, dos están sustentados en zonas prominentes: **IP = 50 %**. — INTAKE

## Pendiente

Ver [open-questions §G](../30-governance/open-questions.md#g-prominencia-informativa-propuesta). OQ-33 a OQ-36 esperan a la síntesis del IR (OQ-28, [D-203](../30-governance/decisions.md#d-203)):

- OQ-33: identificación de componentes y rutas alternativas;
- OQ-34: fórmula y peso de la calidad ajustada;
- OQ-35: duplicidades con los AC;
- OQ-36: reglas para Marcado y Catálogos distribuidos.
- [OQ-91](../30-governance/open-questions.md#g-prominencia-informativa-propuesta): la metadescripción como zona prominente, fuera del ámbito Contenido.

La regla de normalización binaria del IR (OQ-31) está en [open-questions §E](../30-governance/open-questions.md#e-síntesis-e-indicadores) y se decide con OQ-28 ([D-174](../30-governance/decisions.md#d-174)).

## Relacionado

- [scoring-systems](scoring-systems.md)
- [acceptance-criteria](acceptance-criteria.md)
- [ri-profile](../20-methods/audit-gsc/ri-profile.md): componentes de respuesta del RI (propuesta V1).
