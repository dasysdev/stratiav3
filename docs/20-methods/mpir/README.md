---
id: mpir
title: MPIR — Modelo de Prácticas Informativas de Referencia
layer: method
status: propuesta
version: 1.2
updated: 2026-10-26
sources: [MPIR Resumen, MPIR §1, MPIR §2, INTAKE 2026-10-25-requirement-blocks, INTAKE 2026-10-26-open-issues-resolution]
---

# MPIR — Modelo de Prácticas Informativas de Referencia

*Estrategia de observación, extracción, estructuración y análisis de información comercial publicada por ecommerce referentes para apoyar la construcción sistemática de modelos de demanda.*

Versión 1.0 — metodología inicial consolidada para aplicación y calibración. Es el documento metodológico de la **segunda vía de construcción del modelo de demanda**. No es un catálogo de requisitos informativos, una auditoría de ecommerce ni una especificación cerrada de software.

## Resumen

El **Modelo de Prácticas Informativas de Referencia (MPIR)** es una base de conocimiento estructurada que documenta **cómo los ecommerce referentes presentan, explican, relacionan y utilizan información comercial para facilitar el descubrimiento, la comprensión, la comparación y la evaluación de sus ofertas**. Su utilidad es ofrecer **evidencia indirecta sobre posibles necesidades informativas de la demanda** de una clase de producto u oferta.

El MPIR complementa la [Taxonomía de clases de producto](../product-taxonomy/README.md), basada en la integración semántica de Shopify, Amazon y Google. La taxonomía delimita las clases y facilita reconocer atributos, facetas y dimensiones del dominio. El MPIR permite observar **qué preguntas se anticipan, qué criterios de elección se emplean, qué contextos y relaciones se explican y cómo se ayuda a tomar decisiones**. Las dos fuentes se utilizan posteriormente para inferir, formular y justificar requisitos informativos del [modelo de demanda](../../10-model/demand-model.md).

> El canon reconoce dos vías de construcción del modelo de demanda: la [taxonomía de clases de producto](../product-taxonomy/README.md) y este MPIR ([D-009](../../30-governance/decisions.md#d-009)); y, como tercera vía provisional, las cuestiones inferidas ([D-036](../../30-governance/decisions.md#d-036)), que el MPIR confirmará o revisará.

La estrategia de adquisición será **híbrida, estructural y semántica**, con responsabilidades separadas: **capturar y preservar las fuentes originales → construir un corpus estructurado de unidades informativas → identificar señales y prácticas candidatas → consolidar patrones entre referentes → transferir evidencia contrastada al proceso de construcción de requisitos informativos**. Las etapas pueden ejecutarse en ciclos incrementales; la interpretación no sustituye ni altera la evidencia conservada.

La hipótesis del método es que ecommerce reconocidos o especializados **pueden** reflejar, a través de sus decisiones informativas, conocimiento acumulado sobre las necesidades de sus compradores. **No se presupone** que sus prácticas sean correctas, universales o representativas de la frecuencia real de la demanda. El MPIR es una fuente **inferencial y cualitativa**, no una medición directa del mercado.

## Decisiones metodológicas adoptadas

| Cuestión | Decisión |
|---|---|
| Función del MPIR | Recoger y normalizar evidencias de prácticas informativas utilizadas como indicios indirectos de necesidades de demanda. |
| Relación con taxonomías | Complementaria: no duplicar mecánicamente atributos ni limitar la exploración a dimensiones taxonómicas conocidas. |
| Material de observación | Recursos informativos de ecommerce referentes relevantes para el descubrimiento y la decisión de compra. |
| Estrategia de extracción | Scraping orientado por recursos y bloques del DOM, renderizados siempre con navegador real ([D-073](../../30-governance/decisions.md#d-073)), con interacción selectiva y análisis semántico posterior. |
| Persistencia | Conservar tanto el recurso original como las unidades estructuradas y las interpretaciones versionadas. |
| Unidad básica de evidencia | Unidad de contenido contextualizada, que puede contener texto, datos, opciones, entidades o relaciones y remite al recurso original. |
| Identificación de prácticas | Posterior y lógicamente independiente de la captura, con anotaciones preliminares permitidas durante el procesamiento. |
| Operación | Ciclos de extracción, análisis, revisión y ampliación; no esperar a completar todo el universo antes de analizar. |
| Inferencia | Separar lo publicado, la práctica interpretada y la necesidad informativa candidata. |
| Valoración | Sin puntuaciones de calidad ni conversión automática de frecuencia, prominencia o presencia en importancia del requisito. |

## Propósito y alcance

### Finalidad

La finalidad es **identificar y documentar de forma sistemática indicios de qué cuestiones informativas se consideran útiles para comprender, comparar y evaluar ofertas de una clase**, observando cómo las tratan ecommerce referentes. Este conocimiento alimenta la inferencia del modelo de demanda sin sustituir su proceso de justificación.

El problema que aborda esta vía no es «¿qué atributos publica una tienda?» ni «¿qué ecommerce informa mejor?», sino:

> **¿Qué necesidades de conocimiento de la demanda podemos reconocer a partir de las decisiones informativas de ecommerce referentes que no se desprenden, o no quedan suficientemente desarrolladas, de las taxonomías de producto?**

El análisis puede producir confirmaciones, nuevas cuestiones, mayor profundidad de preguntas conocidas o diferencias de aplicabilidad entre clases y subclases.

### Alcance funcional

Se mantiene el perímetro del estudio ([alcance](../../00-context/scope.md)): **descubrimiento y decisión de compra**, en el contexto relevante para **España desde octubre de 2026**, con horizonte hasta al menos el primer trimestre de 2027. Se atiende a productos, variantes, ofertas, vendedores y condiciones comerciales **cuando su conocimiento interviene antes de decidir la compra**.

La exploración de referentes puede incluir páginas y herramientas interactivas como **fuentes para conocer prácticas informativas**. Ello no modifica el alcance **no interactivo** de la auditoría posterior de información comercial: son actividades y finalidades distintas.

No se investigan la preparación operativa de la compra, la ejecución de pagos, los procesos postcompra ni la infraestructura general de los ecommerce. Sí pueden observarse políticas de devolución o garantía en la medida en que **su conocimiento previo** sea relevante para valorar una oferta, sin auditar los procesos operativos correspondientes.

### Relación con las vías de referencia

| Vía | Objeto observado | Contribución principal | Límite |
|---|---|---|---|
| **Taxonomía de clases de producto** | Categorías, especializaciones, facetas, atributos, valores y correspondencias de Shopify, Amazon y Google. | Delimitar la clase e identificar dimensiones y distinciones candidatas. | No equivale al conjunto de preguntas necesarias para evaluar una oferta. |
| **MPIR** | Contenidos, estructuras y mecanismos informativos utilizados por ecommerce referentes. | Reconocer criterios de elección, preguntas anticipadas, contextos, relaciones, limitaciones y patrones de explicación/comparación. | No acredita por sí mismo frecuencia de demanda, corrección de las prácticas o importancia de los requisitos. |
| **Modelo de demanda** | Cuestiones informativas relevantes, inferidas y justificadas. | Definir los requisitos informativos de la clase con dimensión, alcance, aplicabilidad e importancia relativa. | No se obtiene copiando literalmente campos o contenidos de ninguna de las dos fuentes. |

La taxonomía propia es la **referencia para delimitar la muestra por clase**, pero el análisis comercial mantiene una **vía exploratoria abierta** para encontrar información que dicha taxonomía no haya anticipado.

**Precedencia.** Las definiciones de modelo de demanda, requisito informativo, relevancia, importancia relativa, interfaces y evaluación provienen del canon ([`10-model/`](../../10-model/demand-model.md)); la taxonomía fija la relación entre clases internas y fuentes externas. Este marco operacionaliza **solo la vía de ecommerce referentes** y no modifica esos conceptos.

## Hipótesis de observación y límites de inferencia

La hipótesis de trabajo es que algunos ecommerce especializados o con experiencia comercial significativa han invertido recursos en conocer a sus compradores y en organizar contenidos que anticipan necesidades de información. La observación de dichas decisiones permite aprovechar **indirectamente** ese conocimiento.

Cautelas:

1. **Práctica observada ≠ necesidad demostrada.** Una FAQ, filtro o comparador ofrece un indicio razonable, no una prueba de demanda real.
2. **Autoridad comercial ≠ validación metodológica.** La escala o notoriedad de un ecommerce no asegura que todas sus decisiones informativas sean correctas.
3. **Frecuencia observada ≠ prevalencia en el mercado.** Cinco comercios que incluyen una cuestión no prueban cuántos compradores la necesitan.
4. **Prominencia editorial ≠ importancia relativa.** Posición visual, extensión del contenido y repetición pueden responder a SEO, publicidad, diferenciación, limitaciones de plataforma o estrategia de marca.
5. **Ausencia editorial ≠ irrelevancia.** Que una cuestión no aparezca en los referentes observados no implica que no deba incluirse en el modelo de demanda.
6. **Información del referente ≠ respuesta de una oferta auditada.** La evidencia usada para construir el modelo no puede incorporarse después como si fuera información publicada por el ecommerce objeto de auditoría.

Por tanto, el MPIR debe registrar **observaciones, interpretaciones, incertidumbres y fundamentos**. Si procede, el modelo de demanda podrá contrastarse después con consultas reales o investigación de usuarios, sin exigir que esa contrastación forme parte de esta fase inicial.

## Índice del marco

| Módulo | Contenido | Secciones v0 |
|---|---|---|
| [concepts-architecture.md](concepts-architecture.md) | Definiciones operativas, arquitectura de capas A–E, modelo lógico de datos. | MPIR §3, §13 |
| [sampling-capture.md](sampling-capture.md) | Diseño de la muestra y estrategia técnica de captura/scraping. | MPIR §4–5 |
| [corpus-signals.md](corpus-signals.md) | Corpus estructurado (unidad mínima, segmentación) y tipología de señales SI-01–SI-08. | MPIR §6–7 |
| [interpretation-transfer.md](interpretation-transfer.md) | Análisis semántico, uso de IA, consolidación de patrones y transferencia al modelo de demanda. | MPIR §8–10 |
| [operation-validation.md](operation-validation.md) | Cobertura, ciclo operativo, piloto, riesgos, entregables y conclusión. | MPIR §11–12, §14–18 |

**Nota de procedencia:** el nombre **MPIR**, la separación en corpus y capas, la tipología `SI-01`–`SI-08`, los registros propuestos y el procedimiento de scraping/consolidación son **decisiones de diseño metodológico** que deberán verificarse operativamente en el piloto. No se ha realizado una extracción real ni se atribuyen a ecommerce concretos los ejemplos ilustrativos.
