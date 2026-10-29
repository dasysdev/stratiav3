---
id: audit-gsc-qa
title: Controles de calidad y resolución de incidencias
layer: method
status: propuesta
version: 0.5
updated: 2026-10-30
sources: [GSC0 §16, GSC0 Anexo D, FUND §12, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-27-assessment-hints, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-30-content-and-markup-scopes]
---

# Controles de calidad y resolución de incidencias

## Riesgos de procedimiento a vigilar

> **Estado: vigente** (FUND §12).

El procedimiento debe vigilar especialmente las **falsas ausencias**, la inclusión por simple asociación temática, el uso de conocimiento externo como si fuera información expuesta, las atribuciones entre entidades o momentos no comparables y la confusión entre hecho observado e interpretación. La independencia frente a modelos concretos de IA es metodológica y razonablemente reproducible; no equivale a invariancia absoluta del comportamiento de todos los agentes.

## Validaciones obligatorias (QA-01 a QA-15)

> **Estado: propuesta V1.**

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

**QA-11.** NE solo registra una incidencia (una comprobación que no se pudo hacer, con la comprobación fallida) y el NA de criterio solo se usa en Comparabilidad, cuando la marca de dimensión de comparación del requisito lo dice (el NA del requisito sigue su regla); ninguno encubre deficiencias, errores de búsqueda o falta de corroboración.

**QA-12.** Cada valoración AC cita hallazgos/evidencias y explica de manera propia el resultado frente a la condición del criterio.

**QA-13.** No se han introducido subpuntuaciones de propiedades, grados de derivación ni agregaciones IR/ICI no aprobadas.

**QA-14.** El informe remite a evidencias originales suficientes y distingue hallazgos de hipótesis, limitaciones y recomendaciones.

**QA-15.** *(Propuesta V1, [D-153](../../30-governance/decisions.md#d-153).)* Entre las dos fases de la [ejecución](execution.md#ejecución-en-dos-fases), el código comprueba que cada fragmento citado como evidencia existe literalmente en la representación de su ámbito (en Contenido, la salida del [filtro Alfa](filter-alfa.md); en Marcado, el marcado: [D-223](../../30-governance/decisions.md#d-223)) y que cada disponibilidad 0 lleva su registro de cobertura. Lo que no lo cumple no pasa a la fase 2.

| QA | Módulo que controla |
|---|---|
| QA-01, QA-02 | [inputs-outputs.md](inputs-outputs.md), [ri-profile.md](ri-profile.md) |
| QA-03 | [exploration.md](exploration.md), [evidence.md](evidence.md) |
| QA-04 a QA-07 | [relevance.md](relevance.md) |
| QA-08, QA-09 | [availability-coverage.md](availability-coverage.md) |
| QA-10 | [property-checks.md](property-checks.md) (P16) |
| QA-11 a QA-13 | [gsc-decision.md](gsc-decision.md) |
| QA-14 | [dossier.md](dossier.md) |
| QA-15 | [execution.md](execution.md#ejecución-en-dos-fases), [evidence.md](evidence.md) |

## Incidencias del procedimiento

| Incidencia | Acción preferente | Consecuencia si no se resuelve |
|---|---|---|
| Perfil RI ambiguo | Revisar delimitación; registrar diferencia sin alterar pregunta. | Bloqueo o valoración solo de parte delimitable, con alcance explícito. |
| Contenido no recuperable | Verificar perfil, repetir comprobación razonable y registrar fallo. | Disponibilidad 0 si se acredita imposibilidad efectiva; de lo contrario, inconclusa. |
| Candidato decisivo sin contexto | Ampliar inspección de recursos admitidos. | No fundamentar conclusiones incompatibles con la incertidumbre. |
| Contradicción entre afirmaciones | Comprobar entidad, condiciones, unidades y momento. | Registrar discrepancia sin inventar versión «correcta». |
| Falta de fuente para Fiabilidad | Documentar qué comprobaciones se hicieron (estructura, dominio, consistencia del ámbito); la auditoría no consulta fuentes externas ([D-154](../../30-governance/decisions.md#d-154)). | Grado según las comprobaciones superadas; ni 0 ni NE automáticos. |
| Evidencia descontextualizada | Recuperar soporte original y contexto. | El hallazgo no puede aceptarse hasta subsanar o declarar limitación. |
| El informe afirma más que el expediente | Revisar texto y vínculos evidenciales. | No publicar la conclusión no sustentada. |

## Auditoría de decisiones y desacuerdos

La revisión utiliza el mismo RI, perfil, ámbito, instantánea y reglas. Ante desacuerdo, clasificar la fuente:

- **interpretación del RI**;
- **cobertura y localización**;
- **pertinencia**;
- **atribución/contexto**;
- **lectura de propiedad**;
- **evidencia suficiente**;
- **anclaje GSC**.

Resolverlo documentando qué regla cambió o qué evidencia era distinta, **en lugar de promediar valoraciones discrepantes**. Los cambios de anclaje GSC, cobertura o exigencia de evidencia se identifican junto con sus efectos en evaluaciones anteriores y se actualizan los casos de prueba afectados ([calibration.md](calibration.md)).

## Relacionado

- [execution.md](execution.md) — OP-11 ejecuta estos controles.
- [calibration.md](calibration.md) — prueba de aceptación V1.
