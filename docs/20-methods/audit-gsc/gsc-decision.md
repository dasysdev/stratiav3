---
id: audit-gsc-gsc-decision
title: Decisión de GSC, incidencias y control de materialidad
layer: method
status: propuesta
version: 0.8
updated: 2026-10-30
sources: [GSC0 §12, GSC0 §14.4, FUND §8.1, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-27-assessment-hints, INTAKE 2026-10-27-hints-governance, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-29-oq-review, INTAKE 2026-10-30-content-and-markup-scopes, INTAKE 2026-10-30-pilot-base-sanitation]
---

# Decisión de GSC, incidencias y control de materialidad

La escala GSC 0/1/2 y los estados NA/NE son canon ([sistemas de valoración](../../10-model/scoring-systems.md)). Los seis criterios se aplican siempre y NE es una incidencia de la auditoría ([D-117](../../30-governance/decisions.md#d-117)). Este módulo fija el **procedimiento de decisión** (propuesta V1).

## Procedimiento universal (GSC-01 a GSC-12)

**GSC-01 · Puerta de disponibilidad.** Solo valorar AC si disponibilidad efectiva = 1. Si es 0, fijar IR = 0 y dejar los AC **sin valoración**; no registrar NA o 0 por defecto en todos ellos.

**GSC-02 · Aplicación.** Los seis AC se aplican siempre. La única excepción es el NA de Comparabilidad cuando la marca de dimensión de comparación del requisito dice que no es dimensión de comparación ([D-126](../../30-governance/decisions.md#d-126)); lo fija el modelo, no el auditor. No usar NA porque falta información.

**GSC-03 · Base probatoria.** Verificar evidencias y cobertura suficientes para juzgar la condición específica. Si faltan, ampliar la comprobación. Si una comprobación **no se puede hacer** (un recurso que no se pudo inspeccionar), registrar **NE** como incidencia, con la comprobación que falló; no 0 automático. Que un dato no se pueda corroborar no es una incidencia: en Fiabilidad se resuelve con la lectura refutadora.

**GSC-04 · Condición satisfecha.** Si el AC está satisfecho suficientemente para el RI, asignar **2**, indicando componentes y evidencias favorables.

**GSC-05 · Condición parcial.** Si existe satisfacción parcial con limitaciones materiales acreditadas, asignar **1**, explicando la parte satisfecha y la parte limitada.

**GSC-06 · Condición no satisfecha.** Si la insatisfacción de la condición está acreditada, asignar **0**, explicando qué no queda satisfecho y por qué la evidencia es suficiente para afirmarlo.

**GSC-07 · Sin falsa precisión.** No transformar la escala ordinal en porcentajes, distancias métricas ni subpromedios de propiedades. No asignar pesos universales no aprobados.

**GSC-08 · Materialidad relativa.** Una limitación repercute en el GSC si afecta a la condición que define el AC respecto de la cuestión, entidad y alcance concretos.

**GSC-09 · Múltiples elementos del RI.** Una satisfacción mixta debe examinarse por unidades y componentes. No fijar un porcentaje universal de variantes resueltas para decidir 0/1/2; explicar qué elementos quedan cubiertos y si la condición global se satisface.

**GSC-10 · Evidencia compartida.** Un hallazgo puede fundamentar varios GSC, pero se requieren juicios específicos de cada AC.

**GSC-11 · Revisión de nueva evidencia.** Si un hallazgo o candidato altera materialmente un juicio, reabrir la comprobación afectada y documentar el cambio.

**GSC-12 · Decisión completa.** Todo GSC debe quedar acompañado de: criterio y condición, valor, hechos comprobados, propiedades relacionadas, pistas de valoración usadas (`PV-n`, [D-138](../../30-governance/decisions.md#d-138); ⚠ Ver [I-52](../../30-governance/issues.md#i-52)), evidencias citadas, cobertura, motivo de la decisión y limitaciones.

## Árbol de decisión operativo

```text
¿La unidad RI × ámbito es aplicable y está delimitada?
  NO  → Registrar NA del RI o bloqueo de preparación, según causa.
  SÍ  → ¿La disponibilidad efectiva puede determinarse con evidencia?
          NO  → Comprobación de disponibilidad inconclusa; no emitir AC.
          SÍ  → ¿Disponibilidad = 0?
                  SÍ → IR = 0; no emitir valoraciones de AC.
                  NO → Para cada AC:
                         ¿Se pudieron hacer las comprobaciones necesarias?
                           NO → Ampliar o repetir; si una no puede hacerse
                                → NE (incidencia, con la comprobación fallida).
                           SÍ → ¿Condición suficientemente satisfecha?
                                   SÍ → 2.
                                   NO → ¿Existe satisfacción parcial
                                          materialmente acreditada?
                                           SÍ → 1.
                                           NO → 0, con prueba de
                                                  insatisfacción.
   (Comparabilidad: NA, si el requisito está marcado como no
    dimensión de comparación, D-126.)
```

La última rama **no autoriza 0 por descarte lógico sin evidencia**: solo se llega a ella si previamente se verificó base probatoria suficiente para caracterizar una insatisfacción.

## Prueba de materialidad

### Materialidad

Una limitación es **material** cuando tiene consecuencia justificada para la condición del AC examinado respecto de la cuestión, entidad y alcance concretos. Ante un hallazgo aparentemente negativo, documentar:

1. **Condición:** ¿qué aspecto definido del AC podría verse afectado?
2. **Objeto:** ¿a qué componente, entidad, desagregación, relación o condición del RI afecta?
3. **Consecuencia:** ¿qué respuesta o parte del juicio se vuelve imposible, parcial, ambigua, inaplicable, no sustentada o no reconstruible?
4. **Soporte:** ¿qué evidencia demuestra esa limitación —o solo la sugiere—?
5. **Alcance:** ¿la limitación es material para la cuestión completa o accesoria? ¿El resto de la información la resuelve legítimamente?

**Solo las limitaciones con consecuencia justificada para la condición examinada deben reducir el GSC.** Esto impide puntuar defectos cosméticos o exigir información ajena al RI.

## Separación de estados de excepción

| Situación | Tratamiento correcto | Tratamiento incorrecto |
|---|---|---|
| RI no procede para la clase/oferta según aplicabilidad definida. | NA del RI, justificado. | Disponibilidad 0 sin analizar aplicabilidad. |
| RI aplicable, información pertinente ausente tras cobertura suficiente. | Disponibilidad 0, IR 0; no valorar AC. | Seis AC = 0 por defecto. |
| RI aplicable, comprobación previa inconclusa. | Estado procedimental «inconclusa»; disponibilidad sin valor emitido; no valorar AC. | Crear «disponibilidad 2» o fingir disponibilidad 0. |
| Disponibilidad 1, la respuesta no es una dimensión de comparación de la clase. | Comparabilidad NA, según la marca del requisito. | Darle 0 porque no se puede comparar. |
| Disponibilidad 1, una comprobación no se pudo hacer. | NE del AC como incidencia, con la comprobación fallida. | Dar 0 o 1 por incertidumbre general. |
| Disponibilidad 1, un dato que nada refuta ni confirma. | Fiabilidad según las comprobaciones superadas (lectura refutadora). | NE porque no hay corroboración. |
| Disponibilidad 1, deficiencia suficientemente acreditada. | GSC 0 o 1 según su consecuencia. | NE solo porque el resultado es negativo. |
| Disponibilidad 1, respuesta negativa correctamente sustentada. | Evaluar favorablemente los AC que cumpla. | Penalizar porque la oferta no satisface una preferencia. |

## Incertidumbre en Fiabilidad y Justificación

La **falta de pruebas para verificar un hecho** y la **ausencia de base expuesta para reconstruir una respuesta** no son lo mismo. Para Fiabilidad, el grado sale de las comprobaciones superadas: sin defectos detectados es 2, aunque nada corrobore el dato, y el registro dice qué se comprobó ([lectura refutadora](../../10-model/acceptance-criteria.md#fiabilidad-lectura-refutadora-y-comprobaciones)). Para Justificación, la falta **comprobada** de afirmaciones o conexiones de soporte en la información expuesta puede justificar 0/1 con una cobertura de inspección suficiente; también la falta del identificador que permitiría verificar un dato. No obligar a ambos criterios a recibir el mismo resultado.

## Salida separada por AC

Cada criterio mantiene su juicio propio. **No se calcula un GSC global ni una media de seis AC.** La síntesis del RI (IR) y del ámbito (ICI y otros indicadores) requiere reglas de agregación que **no forman parte de esta V1**, salvo el efecto vigente de disponibilidad 0 sobre IR.

## Plantilla de valoración por AC (YAML ilustrativo)

Los registros de la auditoría informativa son **JSON validado y versionado**, con el mismo patrón que web-audit ([D-199](../../30-governance/decisions.md#d-199)). Los campos exactos se fijan al implementar el auditor; hasta entonces, esta plantilla es solo ilustrativa.

`propiedades_consideradas` y `justificacion` registran las propiedades citadas y su efecto en el juicio. Una propiedad tiene ficha propia solo ante un defecto ([D-198](../../30-governance/decisions.md#d-198), [property-checks](property-checks.md#método-común-pr-01-a-pr-09)).

```yaml
caso_id: "AUD-XXX"
ri_id: "RI-XXX"
ambito: "Contenido"
disponibilidad_efectiva: 1
valoraciones:
  - criterio: "Aplicabilidad"
    estado: "valorado"  # valorado | NE (incidencia) | NA (solo Comparabilidad, según la marca)
    gsc: 1               # null si NE o NA
    condicion_evaluada: "<condicion vigente del AC>"
    propiedades_consideradas: ["P10", "P11", "P12"]
    pistas_usadas: ["PV-12"]
    evidencias: ["E-001", "E-002"]
    hallazgos: ["H-001"]
    parte_satisfecha: "<que esta suficientemente acreditado>"
    limitacion_material: "<que impide satisfaccion completa>"
    justificacion: "<relacion entre evidencia, condicion y valor>"
    cobertura: "<comprobacion de alcance/cobertura>"
    limitaciones_de_evaluacion: []
```

**Importante:** si disponibilidad es **0**, `valoraciones` no debe contener seis ceros ni seis NA: los AC **no se valoran**. Si la disponibilidad no puede determinarse, mantener `disponibilidad_efectiva: null` junto al campo **procedimental** `estado_disponibilidad: inconclusa`; no crear un nuevo nivel de disponibilidad. Si una comprobación no se pudo hacer, `estado: NE, gsc: null`, con la comprobación fallida en `limitaciones_de_evaluacion`; si el requisito no es dimensión de comparación, Comparabilidad lleva `estado: NA, gsc: null`.

## Relacionado

- [ac-guides.md](ac-guides.md) — anclajes por AC.
- [availability-coverage.md](availability-coverage.md) — puerta previa y estado inconcluso.
- [qa.md](qa.md) — QA-08, QA-11, QA-12, QA-13.
