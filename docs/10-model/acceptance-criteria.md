---
id: acceptance-criteria
title: Criterios de aceptación
layer: model
status: vigente
version: 1.0
updated: 2026-10-24
sources: [BASE §5.2, FUND §6, FUND §10.1, GSC0 §6.4]
---

# Criterios de aceptación (AC)

## Definición

> Los **criterios de aceptación** son las condiciones evaluativas con las que se juzgan aspectos diferenciados de la capacidad de la información comercial expuesta en una interfaz para resolver un requisito informativo. — BASE §5.2

| Criterio | Condición evaluada |
|---|---|
| **Concreción** | La información cubre los componentes de la cuestión con la extensión y el detalle necesarios, directamente o mediante derivaciones justificadas. |
| **Precisión** | El significado de afirmaciones, términos, valores y relaciones puede interpretarse inequívocamente. |
| **Aplicabilidad** | La información puede atribuirse con claridad a la entidad, el alcance y las condiciones concretas que plantea el requisito. |
| **Comparabilidad** | La información permite efectuar o evaluar el contraste requerido sobre bases equivalentes o equivalencias justificadas. |
| **Fiabilidad** | La corrección, actualidad y consistencia de la información están suficientemente sustentadas mediante comprobaciones y evidencias pertinentes. |
| **Justificación** | La información expuesta aporta una base identificable y suficiente para sostener y reconstruir la respuesta mediante afirmaciones y relaciones de soporte justificadas. |

Cada criterio se valora con el **GSC** (0/1/2, o los estados NA y NE). Ver [scoring-systems](scoring-systems.md#grado-de-satisfacción-de-criterio-gsc).

## Reglas e invariantes

1. **Solo se valoran si la [disponibilidad efectiva](effective-availability.md) = 1.** La disponibilidad no forma parte de este catálogo.
2. **No son indicadores de resolución.** Valoran condiciones específicas y preceden a la síntesis por requisito (IR).
3. **Su formulación se refiere siempre a la información pertinente efectivamente utilizable «en una interfaz»** y a la cuestión y el alcance examinados (FUND §6.1).
4. **Proporcionan juicios diferenciados y complementarios** (BASE §5.2). La regla operativa de no compensación encubierta entre AC es una propuesta V1 (M09, [audit-gsc](../20-methods/audit-gsc/README.md)). La síntesis del IR sigue pendiente.
5. **La pertinencia y el impacto relativo de cada criterio dependen del RI y del ámbito.** Algunas condiciones pueden ser indispensables: su insuficiencia condiciona el resultado aunque los demás criterios estén satisfechos. **No se trasladan al modelo vigente los antiguos pesos y topes numéricos.**
6. **Comparabilidad es contextual:** se evalúa cuando la cuestión requiere contraste. Puede apoyarse en conversiones o equivalencias justificadas, **sin imponer formatos idénticos** (FUND §6.2). Si el RI no requiere contraste, el ejemplo de FUND §10.1 la registra como NA.
7. **Derivaciones admitidas.** Una respuesta puede estar **expresada directamente** o ser **derivable mediante relaciones y operaciones justificadas** por la evidencia publicada.
   - Ninguna derivación válida se penaliza por requerir varios pasos.
   - El número de pasos no es una escala auxiliar del GSC.
   - No se presentan como datos publicados los estados, identidades, condiciones o relaciones que el agente complete con conjeturas o con conocimiento externo no acreditado.
8. **El GSC expresa la satisfacción de la condición**, no la capacidad compensatoria ni el esfuerzo computacional de un modelo. Una valoración baja no demuestra que ninguna IA pueda resolver la cuestión; una alta no garantiza el éxito de cualquier sistema.

## Distinciones

| Par | Diferencia |
|---|---|
| Disponibilidad frente a **Concreción** | La disponibilidad dice si existe información utilizable. La concreción dice si cubre la cuestión con la extensión y el detalle necesarios. |
| **Concreción** frente a **Precisión** | La primera comprueba si la cuestión queda cubierta; la segunda, si el significado de lo expresado es inequívoco. |
| **Precisión** frente a **Aplicabilidad** | Comprender «disponible» no determina **qué variante** está disponible. |
| **Aplicabilidad** frente a **Fiabilidad** | Atribuir bien una afirmación no garantiza su exactitud ni su vigencia. |
| **Fiabilidad** frente a **Justificación** | La fiabilidad depende del sustento de corrección, actualidad y coherencia. La justificación exige un soporte identificable para reconstruir la respuesta. Citar una fuente no demuestra su verdad, y la ausencia de contradicciones no demuestra exactitud. |
| **Evidencia compartida** | Un hallazgo puede afectar a varios criterios, pero hay que explicar la consecuencia específica para cada uno, sin tratarlo como varios defectos independientes. |

**Resumen:** la disponibilidad trata del acceso; la concreción, de la cobertura; la precisión, del significado; la aplicabilidad, de la atribución; la fiabilidad, de la confianza en lo afirmado; la justificación, del fundamento. La comparabilidad interviene cuando hay contraste.

## Interpretación

La interpretación semántica legítima y el razonamiento sustentado se distinguen de la **invención de hechos faltantes**. Por ejemplo (GSC0 PF-06, propuesta V1), el significado general de `InStock` puede reconocerse por conocimiento del dominio. En cambio, la identidad de la variante a la que se refiere, la oferta y el momento requieren sustento en las fuentes admitidas.

La relación orientativa entre criterios y propiedades que sustentan su análisis está en [quality-properties](quality-properties.md#asociaciones-orientativas-con-los-criterios).

## Ejemplo mínimo (hipotético)

**RI:** disponibilidad comercial de cada variante. **Ámbito:** Web. Ficha con tallas 41, 42 y 43 y la afirmación «Disponible para compra online» en la cabecera del modelo, sin estado por talla.

| AC | Valor ilustrativo | Motivo |
|---|---|---|
| Concreción | 1 | Hay información sobre el modelo, pero falta el desglose por variante. |
| Precisión | 2 | La expresión es interpretable; el problema está en la atribución. |
| Aplicabilidad | 1 | El estado se atribuye al modelo, no inequívocamente a la talla 42. |
| Comparabilidad | NA | El RI no requiere contraste. |
| Fiabilidad | NE | No hay evidencia suficiente sobre la corrección o vigencia del estado. |
| Justificación | 1 | Soporte parcial; no fundamenta una conclusión para la talla 42. |

Los valores son ilustrativos, no una auditoría real.

## Pendiente

- Guías por criterio con pruebas, evidencias, reglas interpretativas y anclajes 0/1/2 y NA/NE. Hay propuesta V1 en [ac-guides](../20-methods/audit-gsc/ac-guides.md), pendiente de calibración. Ver [open-questions](../30-governance/open-questions.md).

## Relacionado

- [quality-properties](quality-properties.md)
- [scoring-systems](scoring-systems.md)
- [gsc-decision](../20-methods/audit-gsc/gsc-decision.md): procedimiento de decisión (propuesta V1).
