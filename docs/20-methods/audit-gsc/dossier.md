---
id: audit-gsc-dossier
title: Expediente, informe, diagnóstico y recomendaciones
layer: method
status: propuesta
version: 0.5
updated: 2026-10-29
sources: [GSC0 §14.1, GSC0 §14.5, GSC0 §9.6, FUND §9.4, FUND §9.5, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-28-request-context-and-scripts, INTAKE 2026-10-29-oq-review]
---

# Expediente, informe, diagnóstico y recomendaciones

## Registro estructurado frente a informe

> **Estado: vigente** (FUND §9.4).

El **registro estructurado** conserva observaciones, decisiones y soportes. El **informe de auditoría** expresa los resultados, las limitaciones, los GSC y las recomendaciones verificables con vínculos al registro; no reemplaza las evidencias originales por una descripción resumida del agente.

## Objetos del expediente

> **Estado: propuesta V1** (modelo de datos).

| Objeto | Contenido | Cardinalidad conceptual |
|---|---|---|
| `perfil_ri` | Contrato informativo del RI. | Uno por RI/versión de perfil. |
| `caso_evaluado` | Recurso, oferta/entidad, ámbito, condiciones, momento y perfil. | Uno por unidad aplicada. |
| `recurso_obtenido` | Representación efectivamente consumida y soporte preservado. | Uno o varios por caso. |
| `candidato` | Elemento inicialmente reconocido y decisión de pertinencia. | Cero o varios por caso. |
| `evidencia` | Observación original individual o prueba identificable. | Cero o varias por recurso/comprobación. |
| `cobertura` | Alcance de inspección y limitaciones. | Al menos un registro de inspección por decisión que lo requiera. |
| `hallazgo` | Resultado interpretado con propiedades/RI/AC vinculados. | Cero o varios por caso. |
| `valoracion_ac` | AC, GSC o NE (incidencia), justificación y evidencias. | Un juicio por AC examinado con disponibilidad 1. |
| `revision` | Cambio justificado de evidencia, selección o juicio. | Si se produce revisión. |

Una evidencia puede sustentar varios hallazgos; un hallazgo puede apoyarse en varias evidencias; y un hallazgo puede tener **consecuencias diferentes para varios AC**. Estas relaciones se registran explícitamente. Plantillas: [ri-profile.md](ri-profile.md), [evidence.md](evidence.md), [gsc-decision.md](gsc-decision.md).

## Estructura del informe

El informe tiene dos niveles conectados:

**A. Ficha de resultado accesible:** unidad evaluada; disponibilidad; tabla de AC y GSC (o NE por incidencia); síntesis de hallazgos que explican los resultados; limitaciones y recomendaciones condicionadas; sospechas de Fiabilidad, como «a verificar por el ecommerce».

**B. Expediente reexaminable:** detalles de observación, recursos originales, contexto, método de obtención, cobertura, candidatos decisivos, rutas de relación, propiedades citadas en cada valoración de AC, fichas de las propiedades con defecto ([D-198](../../30-governance/decisions.md#d-198)), hallazgos, juicios y revisiones.

### Contenido mínimo de un hallazgo reportable

Cada hallazgo aporta: **qué se observó**, **qué faltó o qué quedó suficientemente resuelto**, **a qué componente del RI afecta**, **qué propiedad lo explica**, **qué consecuencia específica tiene para el AC**, **qué evidencia lo soporta** y **qué limitación impide conclusiones más amplias**.

Plantilla de redacción por regla general:

> **Hecho observado:** [...]. **Alcance y evidencia:** [...]. **Condición de calidad afectada:** [...]. **Consecuencia para el AC y RI:** [...]. **Valor GSC:** [...], porque [...]. **Límites y acción verificable:** [...].

## Diagnóstico

> **Estado: vigente** (FUND §9.5).

Si un dato existe en un script que no es marcado (estado de la aplicación) pero no en el HTML ni en el marcado, el diagnóstico lo registra como hallazgo («el dato existe en el estado de la aplicación, pero no se publica»), sin efecto en la disponibilidad ni en los GSC ([D-157](../../30-governance/decisions.md#d-157)).

El diagnóstico distingue **qué información se ha encontrado y podido leer, qué cuestión permite responder, qué limitación subsiste y cuál es su causa observada**. Cuando una incidencia de implementación afecta a un RI, se explica el efecto informativo y se remite el examen de conformidad al control técnico correspondiente.

## Recomendaciones

> **Estado: vigente** (FUND §9.5), con la tipología de corrección de GSC0 §14.5.

Las recomendaciones deben:

- Referirse a una deficiencia acreditada, sin atribuir causas no demostradas (organizativas o de implementación).
- Diferenciar si se necesita **publicar, concretar, aclarar, atribuir, normalizar, corregir, actualizar, relacionar o fundamentar** información, o mejorar su exposición técnica (remitir la incidencia al análisis técnico).
- Identificar la entidad, el ámbito, las condiciones y, cuando proceda, la relación informativa afectada.
- Guardar proporción con la importancia de la cuestión y el impacto de los criterios afectados, evitando prioridades numéricas no aprobadas.
- Distinguir acciones correctivas verificables de comprobaciones adicionales cuando falte evidencia.
- Presentar las **sospechas** de Fiabilidad (lo que hace improbable un dato sin refutarlo, o lo que el auditor sabe de un producto concreto) como «a verificar por el ecommerce», con su motivo y sin efecto en el GSC ([D-154](../../30-governance/decisions.md#d-154)).

Un mismo hallazgo puede afectar a diversos AC o RI, pero cada consecuencia se justifica de manera diferenciada. **No se multiplica el defecto por el número de criterios relacionados**, ni se degrada un criterio solo porque exista una incidencia técnica cuya repercusión informativa no está acreditada.

## Criterio de revisión humana

La ejecución de la auditoría es automática ([D-186](../../30-governance/decisions.md#d-186), que extiende [D-041](../../30-governance/decisions.md#d-041)). Antes de entregar, una persona revisa solo las NE y las comprobaciones inconclusas.

Un segundo evaluador debe poder responder desde el expediente: **qué preguntaba el RI, qué información se obtuvo, por qué se consideró pertinente, qué se comprobó, qué propiedad explicó el hallazgo, qué condición del AC quedó satisfecha o limitada y qué justifica el GSC**. Si no puede reconstruirlo, el registro es insuficiente aunque la cifra pueda parecer razonable.

## Relacionado

- [evidence.md](evidence.md) — EV-15 (vínculo registro–informe).
- [qa.md](qa.md) — QA-14 e incidencia «el informe afirma más que el expediente».
