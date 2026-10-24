---
id: ai-functions
title: Funciones informativas de la IA
layer: model
status: vigente
version: 1.0
updated: 2026-10-24
sources: [BASE §2, FUND §2.2-2.3, CTX §2]
---

# Funciones informativas de la IA

## Definición

> Las **funciones informativas de la IA** describen las operaciones de conocimiento que la información comercial y sus condiciones de exposición deben favorecer durante el descubrimiento y la decisión de compra. — BASE §2

| Función | Capacidad que debe facilitar la información comercial |
|---|---|
| **Descubrir** | Localizar productos, ofertas y recursos informativos pertinentes. |
| **Acceder** | Obtener y consultar la información comercial expuesta. |
| **Identificar** | Distinguir productos, variantes, ofertas y vendedores, y reconocer sus relaciones. |
| **Comprender** | Interpretar atributos, valores, afirmaciones y condiciones comerciales. |
| **Comparar** | Contrastar alternativas sobre dimensiones equivalentes o equivalencias justificadas. |
| **Evaluar** | Determinar la adecuación de una oferta a necesidades, preferencias y restricciones de compra. |
| **Justificar** | Sostener y reconstruir las conclusiones mediante información y relaciones de soporte identificables. |

## Reglas e invariantes

1. Las funciones **no son criterios de aceptación ni unidades de puntuación**. Orientan el estudio, pero no se valoran.
2. Una respuesta que fundamenta la **incompatibilidad** de una oferta con una necesidad puede resolver adecuadamente la cuestión planteada.

## Distinciones

- **Justificar** (función) frente a **P18 · Verificabilidad** (propiedad). Justificar es sostener y reconstruir respuestas. La verificabilidad caracteriza la posibilidad de contrastar afirmaciones con evidencias o referencias pertinentes. Están relacionadas, pero no son equivalentes. Ver [quality-properties](quality-properties.md).
- *(Nota editorial, sin fuente rectora.)* **Justificar** (función) frente a **Justificación** (criterio). El criterio juzga si la información expuesta aporta la base que la función necesita. Ver [acceptance-criteria](acceptance-criteria.md).

### Cadena conceptual

| Elemento | Responde a |
|---|---|
| Interfaces | **Por qué medios técnicos** se expone la información. |
| Funciones informativas | **Qué actividades de conocimiento** deberían resultar posibles. |
| Requisitos informativos | **Qué cuestiones concretas** importa resolver. |
| Criterios de aceptación | **Si la información expuesta puede resolverlas.** |

## Fundamento: interpretación y utilización por sistemas de IA

Los sistemas de IA que intervienen en el descubrimiento y la decisión de compra son heterogéneos: difieren en modelos, herramientas, conocimientos complementarios y capacidades de interpretación. Por eso la auditoría **no toma como patrón** la ejecución de un modelo o agente específico, ni la capacidad máxima de inferencia de un sistema especialmente avanzado.

El modelo usa criterios y propiedades vinculados a condiciones generales del significado y del uso de la información:

- disponer de los componentes relevantes;
- distinguir las entidades;
- comprender las afirmaciones e interpretar sus contextos;
- relacionar datos y establecer equivalencias;
- contrastar hechos;
- reconstruir el fundamento de una respuesta.

Estas condiciones dan una base de aplicación amplia, pero no garantizan compatibilidad ni éxito con cualquier IA.

> **Premisa metodológica:** cuanto más facilite la información comercial una interpretación y utilización fundamentadas, más favorables serán las condiciones para que una diversidad de sistemas pueda resolver las cuestiones informativas de compra. — FUND §2.3

Facilitar ese tratamiento **no equivale** a imponer un formato único, repetir todos los datos, exigir literalidad ni optimizar el contenido para un proveedor concreto. Significa evitar que la resolución dependa de suplir carencias relevantes con suposiciones o con conocimientos no sustentados en el ámbito evaluado.

Una IA puede resolver correctamente una cuestión pese a una representación deficiente, o fallar ante información suficiente. Ninguna de esas situaciones cambia por sí misma la calidad observada de la información. La evaluación **no mide** latencia, número de inferencias, consumo de recursos ni probabilidad de recomendación: juzga el soporte informativo que se ofrece para la cuestión.

## Relacionado

- [commercial-information](commercial-information.md)
- [acceptance-criteria](acceptance-criteria.md)
- [scope](../00-context/scope.md#límite-de-interpretación)
