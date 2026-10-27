---
id: audit-gsc-execution
title: Procedimiento integral de ejecución
layer: method
status: propuesta
version: 0.3
updated: 2026-10-27
sources: [GSC0 §13, GSC0 Anexo A, FUND §9.3, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-27-assessment-hints]
---

# Procedimiento integral de ejecución

## Secuencia de referencia

> **Estado: vigente** (FUND §9.3). La obtención de evidencias se mantiene en todas las fases.

1. **Delimitar** el RI, el ámbito, las entidades y condiciones, el perfil de consumo y su estructura de resolución/pertinencia.
2. **Obtener y preservar** los recursos admisibles y registrar las limitaciones de recuperación o lectura.
3. **Explorar y localizar** candidatos, datos, afirmaciones, entidades, relaciones y contexto con una cobertura apropiada.
4. **Fundamentar la pertinencia** de los candidatos y formar el conjunto pertinente contextualizado.
5. **Comprobar la disponibilidad efectiva.** Si es 0 con evidencia adecuada, establecer **IR = 0** y no valorar AC; si es 1, continuar.
6. **Examinar las propiedades y sus efectos** sobre cada uno de los seis AC, recurriendo a comprobaciones y evidencias específicas.
7. **Asignar y motivar el GSC** de cada AC, o registrar NE si una comprobación no pudo hacerse (NA de Comparabilidad si el requisito no es dimensión de comparación).
8. **Sintetizar el IR**, cuando se disponga de las reglas correspondientes, y elaborar el informe con referencias al registro de evaluación.

La evaluación técnica se ejecuta conforme a sus requisitos y su sistema cuantitativo. Una misma observación puede alimentar ambos expedientes, pero en el informativo se describe el **efecto sobre la cuestión** y en el técnico se valora **la implementación conforme a su especificación**.

## Secuencia operativa detallada (OP-01 a OP-12)

> **Estado: propuesta V1.** Desarrolla la secuencia anterior; el paso 8 (síntesis IR) queda fuera de V1.

| Paso | Acción del agente | Control de salida obligatorio |
|---|---|---|
| **OP-01** | Identificar RI, ámbito, entidad, recurso, condiciones y fecha de referencia. | Contrato de entrada revisado; aplicabilidad determinada. |
| **OP-02** | Cargar o construir controladamente el perfil operativo del RI. | Componentes sustantivos/auxiliares, desagregación y límites de pertinencia claros. |
| **OP-03** | Delimitar el perfil de consumo y obtener los recursos admitidos. | Recursos/instantáneas, fecha, vía y restricciones registrados. |
| **OP-04** | Ejecutar exploración general y dirigida. | Inventario de candidatos con localizadores y contexto inicial. |
| **OP-05** | Aplicar prueba de pertinencia a los candidatos. | Decisiones pertinentes/pendientes/excluidas relevantes, con función y soporte. |
| **OP-06** | Construir el conjunto pertinente contextualizado. | Sujetos, afirmaciones, relaciones y condiciones vinculados a las fuentes. |
| **OP-07** | Verificar cobertura y disponibilidad efectiva. | 0/1 sustentado o comprobación inconclusa; rama de ejecución correcta. |
| **OP-08** | Planificar las pruebas de propiedades de los seis AC. | Plan de comprobación por criterio, con evidencias requeridas. |
| **OP-09** | Ejecutar comprobaciones y ampliar localización si hace falta. | Hallazgos con evidencia original y cobertura suficiente o limitación explícita. |
| **OP-10** | Aplicar prueba de materialidad y reglas de GSC. | Decisión por AC: 0/1/2, o NE por incidencia, con explicación diferenciada. |
| **OP-11** | Ejecutar controles de integridad, contradicciones y atribución. | Expediente consistente y decisiones revisables; incidencias registradas. |
| **OP-12** | Publicar salida estructurada y generar informe desde el expediente. | GSC, evidencias, límites, acciones verificables; no inventar IR/ICI. |

| OP | Módulo de referencia |
|---|---|
| OP-01 | [inputs-outputs.md](inputs-outputs.md) |
| OP-02 | [ri-profile.md](ri-profile.md) |
| OP-03, OP-04 | [exploration.md](exploration.md) |
| OP-05, OP-06 | [relevance.md](relevance.md) |
| OP-07 | [availability-coverage.md](availability-coverage.md) |
| OP-08, OP-09 | [property-checks.md](property-checks.md), [evidence.md](evidence.md) |
| OP-10 | [ac-guides.md](ac-guides.md), [gsc-decision.md](gsc-decision.md) |
| OP-11 | [qa.md](qa.md) |
| OP-12 | [dossier.md](dossier.md) |

## Orden de procesamiento y eficiencia

Es admisible obtener primero una **representación comercial completa** y utilizarla para varios RI del mismo recurso, siempre que cada evaluación conserve su pertinencia, cobertura y GSC **por unidad RI × ámbito**. También es admisible reutilizar evidencias capturadas una sola vez y vinculadas a varios RI o AC si identidad, momento, contenido y condiciones siguen siendo aplicables.

No se requiere repetir descargas o análisis evidenciales idénticos sin necesidad. La eficiencia de proceso **no sustituye** la comprobación de cobertura y la distinción de ámbitos.

## Reapertura controlada

Una duda posterior de AC puede revelar información contextual omitida. El agente debe: registrar la cuestión; volver a inspeccionar las representaciones permitidas; añadir evidencias; revisar la pertinencia y los hallazgos afectados; reevaluar el AC; y documentar el motivo del cambio. No modificar silenciosamente la puntuación final sin reflejar la nueva base.

## Hoja rápida de ejecución por RI

```text
IDENTIFICACIÓN
[ ] RI, objeto, dimensión, ámbito y entidad concretos
[ ] Desagregación, alcance, condiciones y aplicabilidad
[ ] Perfil de consumo y recursos examinables

LOCALIZACIÓN
[ ] Recurso/instantánea original y contexto preservados
[ ] Exploración general y dirigida
[ ] Componentes del RI vinculados a candidatos
[ ] Prueba contribución–función–fundamento
[ ] Candidatos decisivos pendientes revisados

DISPONIBILIDAD
[ ] Al menos un elemento pertinente utilizable → 1
[ ] O ausencia/inaccesibilidad acreditada → 0, IR 0, sin AC
[ ] O procedimiento inconcluso documentado, sin 0/1 ni AC

VALORACIÓN
[ ] Pruebas de los seis AC planificadas
[ ] Propiedades pertinentes comprobadas, sin subpuntuación
[ ] Evidencias y cobertura adecuadas para cada hallazgo
[ ] Materialidad razonada frente a la condición del AC
[ ] 0/1/2 (o NE por incidencia) por AC, con justificación

CONTROL E INFORME
[ ] Confrontadas identidades, condiciones y momentos
[ ] No se añadieron hechos comerciales no publicados
[ ] Las evidencias originales son reexaminables
[ ] Informe enlazado al expediente
[ ] Limitaciones y revisiones registradas
```

## Relacionado

- [README.md](README.md) — cadena de decisión y razonamiento permitido.
- [qa.md](qa.md) — validaciones obligatorias.
