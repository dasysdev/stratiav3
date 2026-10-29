---
id: scope
title: Problema, objeto y alcance del estudio
layer: context
status: vigente
version: 1.3
updated: 2026-10-30
sources: [CTX §1-5, FUND §1, FUND §2.1, FUND §12, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-30-content-and-markup-scopes]
---

# Problema, objeto y alcance del estudio

## Problema

Los buscadores, las plataformas publicitarias, los sistemas de recomendación y los agentes de IA utilizan la [información comercial](../10-model/commercial-information.md) para descubrir, interpretar, seleccionar, comparar y evaluar productos y ofertas. Su mera publicación no garantiza que puedan utilizarla adecuadamente: también debe ser accesible, suficientemente detallada, comprensible, atribuible a las entidades y condiciones correctas, coherente y capaz de fundamentar conclusiones.

> El problema que motiva el estudio es, por tanto, **en qué medida la información comercial y sus condiciones de representación y exposición permiten resolver las cuestiones informativas relevantes para evaluar una oferta**, más allá de la cantidad de datos publicados o del cumplimiento formal de un formato. — CTX §1

## Objeto

> El objeto del estudio es **la calidad de la información comercial y de sus condiciones de representación y exposición**, entendida como el grado en que la información publicada por un ecommerce y las interfaces que la presentan permiten **determinar y fundamentar respuestas suficientes a las cuestiones informativas relevantes para la demanda** de una clase de producto u oferta. — CTX §3

La evaluación tiene dos dimensiones, **técnica** e **informativa y semántica**. Se definen en [commercial-information](../10-model/commercial-information.md#dos-dimensiones-de-evaluación).

La calidad examinada se refiere a **la información comercial expuesta y su utilidad para la evaluación**, no a la calidad intrínseca del producto ni a su conveniencia para un comprador particular. Una respuesta suficientemente fundada puede establecer tanto la adecuación como la incompatibilidad de una oferta con una necesidad.

## Marco funcional: Agentic Commerce

El **Agentic Commerce** es un modelo de comercio en el que agentes de IA pueden intervenir en distintas fases del proceso de compra, desde la búsqueda y valoración de alternativas hasta, cuando estén habilitadas, determinadas operaciones comerciales.

La **Agentic Commerce Readiness** designa, en sentido amplio, el grado de preparación de un ecommerce para atender las capacidades que requieren esos agentes. **Este estudio no evalúa toda esa preparación**: se centra en las condiciones informativas y técnicas que favorecen el descubrimiento y la decisión de compra.

| Fase del ciclo de compra | Finalidad | Alcance |
|---|---|---|
| **Descubrimiento y decisión de compra** | Encontrar ofertas, interpretar características y condiciones, contrastar alternativas y valorar su adecuación a una necesidad. | **Incluida** |
| Preparación de la compra | Seleccionar o configurar productos y preparar la operación. | Excluida |
| Transacción | Autorizar y formalizar pedido y pago. | Excluida |
| Postcompra | Consultar o gestionar pedidos, entregas, cancelaciones, devoluciones y reembolsos. | Excluida |

> Las capacidades que un ecommerce puede ofrecer a estos agentes son de distinta naturaleza. Algunas permiten **descubrir, acceder, identificar, comprender, comparar y evaluar información comercial, así como justificar las respuestas obtenidas**; otras facilitan preparar o ejecutar operaciones de compra. Las interfaces son los medios técnicos mediante los que el comercio expone la información o habilita esas operaciones. La calidad de la información comercial y de su exposición condiciona el ejercicio efectivo de las capacidades informativas. — CTX §2

Las capacidades informativas se desarrollan como [funciones informativas de la IA](../10-model/ai-functions.md). Las transaccionales quedan fuera del alcance.

## Alcance y límites

- **Perímetro temporal y geográfico:** contexto relevante para **España desde octubre de 2026, con horizonte hasta, al menos, el primer trimestre de 2027**.
- **Fase examinada:** descubrimiento y decisión de compra.
- **Modalidad de interacción:** comercio agéntico **sin navegación interactiva**. Se consideran solo las vías de acceso y consumo que no exigen operar interactivamente las páginas o los procesos de compra.
- **Información examinada:** características de productos y variantes, ofertas, vendedores y condiciones comerciales, según su pertinencia para las cuestiones evaluadas.
- **Interfaces y ámbitos de evaluación:** **Catálogos distribuidos**, **Contenido** y **Marcado** ([evaluation-scopes](../10-model/evaluation-scopes.md)). CTX §5 queda enmendado por [D-013](../30-governance/decisions.md#d-013); los nombres, por [D-220](../30-governance/decisions.md#d-220) (antes, Web y Web Schema.org).
- **Ámbito de las comprobaciones:** la información publicada, sus representaciones y las condiciones técnicas de su exposición y distribución. No se auditan las operaciones de preparación, transacción o postcompra ni la infraestructura completa del ecommerce.

## Finalidad de la auditoría

> El estudio proporciona el marco para construir un **sistema de auditoría** que examine, mediante criterios explícitos y evidencias, la capacidad de la información comercial expuesta por un ecommerce para resolver las cuestiones relevantes de su demanda.
>
> La auditoría permite identificar limitaciones de acceso, comprensión, atribución, contraste y fundamentación; distinguir las condiciones técnicas, informativas y semánticas que las explican; y orientar recomendaciones de mejora verificables. — CTX §4

FUND §1.3 lo desarrolla: identificar limitaciones también de cobertura, significado y fiabilidad; separar sus causas técnicas e informativas; y explicar su impacto sobre las cuestiones pertinentes.

**Referencia evaluativa:** poder **determinar y justificar suficientemente la respuesta que corresponda** a cada cuestión, según la entidad, el alcance y las condiciones examinadas. La calidad no depende de acumular atributos ni de que la oferta satisfaga las preferencias de un comprador.

## Límite de interpretación

El estudio valora la información comercial expuesta y sus condiciones técnicas e informativas de utilización. Por tanto:

- **no mide** el comportamiento, la precisión ni la dificultad computacional de un agente de IA particular;
- **no garantiza** el éxito universal de resolución;
- **no acredita** por sí mismo efectos de visibilidad, recomendación o conversión;
- **no acredita la veracidad de lo publicado frente al mundo.** La auditoría no consulta fuentes externas: Fiabilidad mide la corrección y la coherencia interna de lo publicado. Un 2 no acredita que una certificación, una clase energética o un GTIN sean válidos ([D-154](../30-governance/decisions.md#d-154)).

La independencia frente a modelos concretos de IA es metodológica y razonablemente reproducible. No equivale a invariancia absoluta del comportamiento de todos los agentes. El fundamento se desarrolla en [ai-functions](../10-model/ai-functions.md#fundamento-interpretación-y-utilización-por-sistemas-de-ia).

### Riesgos que el procedimiento debe vigilar

- **Falsas ausencias.**
- **Inclusión por simple asociación temática.**
- **Uso de conocimiento externo** como si fuera información expuesta.
- **Atribuciones** entre entidades o momentos no comparables.
- **Confusión** entre hecho observado e interpretación.

## Referencias conceptuales externas

El modelo usa como referencias orientativas el **W3C Data Quality Vocabulary (DQV)** y la **ISO/IEC/IEEE 15939:2017**, en materia de calidad de datos y medición. **No debe atribuirse a esas referencias la definición o validación de los criterios, indicadores o reglas de síntesis del modelo.**

## Relacionado

- [business-model](business-model.md): encaje en la iniciativa de consultoría.
- [evaluation-architecture](../10-model/evaluation-architecture.md): arquitectura del sistema de evaluación.
