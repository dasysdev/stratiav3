---
id: audit-gsc-gsc-decision
title: Decisión de GSC, NA, NE y control de materialidad
layer: method
status: propuesta
version: 0.1
updated: 2026-10-24
sources: [GSC0 §12, GSC0 §14.4, FUND §8.1]
---

# Decisión de GSC, NA, NE y control de materialidad

La escala GSC 0/1/2 y los estados NA/NE son canon ([sistemas de valoración](../../10-model/scoring-systems.md)). Este módulo fija el **procedimiento de decisión** (propuesta V1).

## Procedimiento universal (GSC-01 a GSC-12)

**GSC-01 · Puerta de disponibilidad.** Solo valorar AC si disponibilidad efectiva = 1. Si es 0, fijar IR = 0 y dejar los AC **sin valoración**; no registrar NA o 0 por defecto en todos ellos.

**GSC-02 · Aplicabilidad.** Para cada AC, determinar si su condición corresponde al RI y ámbito. Si no corresponde, **NA justificado**. No usar NA porque falta información para un criterio pertinente.

**GSC-03 · Base probatoria.** Verificar evidencias y cobertura suficientes para juzgar la condición específica. Si faltan y no pueden completarse, **NE**, no 0 automático.

**GSC-04 · Condición satisfecha.** Si el AC está satisfecho suficientemente para el RI, asignar **2**, indicando componentes y evidencias favorables.

**GSC-05 · Condición parcial.** Si existe satisfacción parcial con limitaciones materiales acreditadas, asignar **1**, explicando la parte satisfecha y la parte limitada.

**GSC-06 · Condición no satisfecha.** Si la insatisfacción de la condición está acreditada, asignar **0**, explicando qué no queda satisfecho y por qué la evidencia es suficiente para afirmarlo.

**GSC-07 · Sin falsa precisión.** No transformar la escala ordinal en porcentajes, distancias métricas ni subpromedios de propiedades. No asignar pesos universales no aprobados.

**GSC-08 · Materialidad relativa.** Una limitación repercute en el GSC si afecta a la condición que define el AC respecto de la cuestión, entidad y alcance concretos.

**GSC-09 · Múltiples elementos del RI.** Una satisfacción mixta debe examinarse por unidades y componentes. No fijar un porcentaje universal de variantes resueltas para decidir 0/1/2; explicar qué elementos quedan cubiertos y si la condición global se satisface.

**GSC-10 · Evidencia compartida.** Un hallazgo puede fundamentar varios GSC, pero se requieren juicios específicos de cada AC.

**GSC-11 · Revisión de nueva evidencia.** Si un hallazgo o candidato altera materialmente un juicio, reabrir la comprobación afectada y documentar el cambio.

**GSC-12 · Decisión completa.** Todo GSC debe quedar acompañado de: criterio y condición, valor, hechos comprobados, propiedades relacionadas, evidencias citadas, cobertura, motivo de la decisión y limitaciones.

## Árbol de decisión operativo

```text
¿La unidad RI × ámbito es aplicable y está delimitada?
  NO  → Registrar NA del RI o bloqueo de preparación, según causa.
  SÍ  → ¿La disponibilidad efectiva puede determinarse con evidencia?
          NO  → Comprobación de disponibilidad inconclusa; no emitir AC.
          SÍ  → ¿Disponibilidad = 0?
                  SÍ → IR = 0; no emitir valoraciones de AC.
                  NO → Para cada AC:
                         ¿El criterio corresponde al RI?
                           NO → NA motivado.
                           SÍ → ¿Hay cobertura/evidencia suficiente para juzgarlo?
                                   NO → Ampliar prueba; si persiste → NE.
                                   SÍ → ¿Condición suficientemente satisfecha?
                                           SÍ → 2.
                                           NO → ¿Existe satisfacción parcial
                                                  materialmente acreditada?
                                                   SÍ → 1.
                                                   NO → 0, con prueba de
                                                          insatisfacción.
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
| Disponibilidad 1, un AC no corresponde a la cuestión. | NA del AC. | Darle 0 porque no se puede comparar. |
| Disponibilidad 1, AC pertinente, evidencias insuficientes para juzgar. | NE del AC y motivo. | Dar 0 o 1 por incertidumbre general. |
| Disponibilidad 1, deficiencia suficientemente acreditada. | GSC 0 o 1 según su consecuencia. | NE solo porque el resultado es negativo. |
| Disponibilidad 1, respuesta negativa correctamente sustentada. | Evaluar favorablemente los AC que cumpla. | Penalizar porque la oferta no satisface una preferencia. |

## Incertidumbre en Fiabilidad y Justificación

La **falta de pruebas para verificar un hecho** y la **ausencia de base expuesta para reconstruir una respuesta** no son lo mismo. Para Fiabilidad, cuando el auditor no puede establecer la corrección/vigencia con fundamento suficiente, estudiar NE. Para Justificación, la falta **comprobada** de afirmaciones o conexiones de soporte en la información expuesta puede justificar 0/1 con una cobertura de inspección suficiente. No obligar a ambos criterios a recibir el mismo resultado.

## Salida separada por AC

Cada criterio mantiene su juicio propio. **No se calcula un GSC global ni una media de seis AC.** La síntesis del RI (IR) y del ámbito (ICI y otros indicadores) requiere reglas de agregación que **no forman parte de esta V1**, salvo el efecto vigente de disponibilidad 0 sobre IR.

## Plantilla de valoración por AC (YAML ilustrativo)

```yaml
caso_id: "AUD-XXX"
ri_id: "RI-XXX"
ambito: "Web"
disponibilidad_efectiva: 1
valoraciones:
  - criterio: "Aplicabilidad"
    estado: "valorado"  # valorado | NA | NE
    gsc: 1               # null si NA o NE
    condicion_evaluada: "<condicion vigente del AC>"
    propiedades_consideradas: ["P10", "P11", "P12"]
    evidencias: ["E-001", "E-002"]
    hallazgos: ["H-001"]
    parte_satisfecha: "<que esta suficientemente acreditado>"
    limitacion_material: "<que impide satisfaccion completa>"
    justificacion: "<relacion entre evidencia, condicion y valor>"
    cobertura: "<comprobacion de alcance/cobertura>"
    limitaciones_de_evaluacion: []
```

**Importante:** si disponibilidad es **0**, `valoraciones` no debe contener seis ceros ni seis NA: los AC **no se valoran**. Si la disponibilidad no puede determinarse, mantener `disponibilidad_efectiva: null` junto al campo **procedimental** `estado_disponibilidad: inconclusa`; no crear un nuevo nivel de disponibilidad. Si no procede un AC, `estado: NA, gsc: null`; si no se puede juzgar, `estado: NE, gsc: null`.

## Relacionado

- [ac-guides.md](ac-guides.md) — anclajes por AC.
- [availability-coverage.md](availability-coverage.md) — puerta previa y estado inconcluso.
- [qa.md](qa.md) — QA-08, QA-11, QA-12, QA-13.
