---
id: effective-availability
title: Disponibilidad efectiva
layer: model
status: vigente
version: 1.0
updated: 2026-10-24
sources: [BASE §5.1, FUND §5.3, FUND §7.3, FUND §10.1-10.2]
---

# Disponibilidad efectiva

## Definición

> La **disponibilidad efectiva** es el requerimiento previo que determina si existe información comercial pertinente para un requisito informativo que pueda obtenerse y leerse efectivamente bajo las condiciones de consumo establecidas para la interfaz evaluada. — BASE §5.1

**Pregunta de comprobación:** ¿puedo obtener y leer en esta interfaz, bajo las condiciones de consumo definidas, **al menos un dato, afirmación o relación que contribuya** a la necesidad informativa de este RI?

Se comprueba para cada **requisito informativo × interfaz pertinente**, con una valoración binaria:

| Valor | Condición |
|---|---|
| **0 — Sin disponibilidad efectiva** | No existe información pertinente utilizable, porque no está presente o porque no puede obtenerse y leerse bajo las condiciones previstas. |
| **1 — Con disponibilidad efectiva** | Existe al menos un dato, afirmación o relación pertinente que puede obtenerse y leerse efectivamente bajo las condiciones previstas. |

## Reglas e invariantes

1. **Es condición necesaria, pero no suficiente,** para la resolución del RI. No evalúa la suficiencia, el detalle, el significado, la atribución ni la fiabilidad: eso corresponde a los [criterios de aceptación](acceptance-criteria.md).
2. **Disponibilidad efectiva = 0 → IR = 0.** No se valoran los criterios de aceptación.
3. **Disponibilidad efectiva = 1 →** se valoran los criterios sobre la información pertinente efectivamente utilizable. La existencia de esa información no garantiza que sea suficiente.
4. **No es un criterio de aceptación** ni un séptimo criterio puntuable. Es una puerta previa.
5. **Declarar ausencia exige una inspección con alcance y cobertura adecuados.** Una búsqueda literal sin resultados no la acredita. Si el ámbito no se ha examinado suficientemente, la ausencia de evidencia no se convierte sin fundamento en un 0.
6. **La escala es binaria.** El tratamiento de una comprobación inconclusa requiere especificación, **sin introducir un tercer valor**. Propuesta operativa: [availability-coverage](../20-methods/audit-gsc/availability-coverage.md).
7. **Se comprueba desde el propósito informativo del RI**, no como evaluación del cumplimiento técnico de la interfaz. Se registran por separado **el efecto sobre la disponibilidad del RI** y **la incidencia técnica que lo provoca**, cuando esta se ha acreditado.
8. Los contenidos que no pueden obtenerse o leerse bajo las condiciones previstas **no contribuyen** a satisfacer ningún criterio.

## Distinciones

- **Disponibilidad efectiva frente a concreción.** La disponibilidad dice si existe información pertinente utilizable. La [concreción](acceptance-criteria.md) dice si esa información cubre los componentes de la cuestión con el detalle necesario. Una afirmación general sobre el modelo puede justificar **disponibilidad = 1** para una cuestión por variante aunque no satisfaga la desagregación requerida.
- **Legibilidad técnica u operativa frente a claridad.** Que un dato pueda recuperarse y leerse no implica que su significado sea inequívoco (P09). Ver [quality-properties](quality-properties.md#lectura-efectiva-frente-a-propiedades-semánticas).
- **Disponibilidad efectiva frente a requisitos técnicos.** La conformidad técnica general no sustituye esta comprobación contextual. Ver [evaluation-scopes](evaluation-scopes.md#punto-de-contacto-entre-la-evaluación-técnica-y-la-informativa).

## Ejemplo mínimo (hipotético)

**RI:** «¿Cuál es la disponibilidad comercial de cada variante del modelo?».

| Caso | Observación bajo el perfil de consumo | Resultado |
|---|---|---|
| **Con disponibilidad** | La ficha HTML muestra «Disponible para compra online» referido al modelo, sin estado por talla. | **1**: hay información pertinente legible. Los AC detectarán la falta de desagregación (p. ej. Concreción 1, Aplicabilidad 1). |
| **Sin disponibilidad** | El HTML obtenido sin ejecutar JavaScript contiene solo un contenedor vacío para variantes y disponibilidad. | **0 → IR = 0**: no se valoran los AC. El problema no es la mera presencia de JavaScript, sino que con ese perfil no se accede a ningún contenido pertinente. |

Casos completos de calibración: [calibration](../20-methods/audit-gsc/calibration.md).

## Pendiente

- Especificar las pruebas de obtención y legibilidad, los registros de cobertura y el tratamiento de las comprobaciones inconclusas. Ver [open-questions](../30-governance/open-questions.md).

## Relacionado

- [evaluation-architecture](evaluation-architecture.md)
- [scoring-systems](scoring-systems.md)
