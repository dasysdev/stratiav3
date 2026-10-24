---
id: commercial-information
title: Información comercial, representación, exposición y calidad
layer: model
status: vigente
version: 1.0
updated: 2026-10-24
sources: [BASE §1, CTX §1, CTX §3, FUND §1.1-1.2]
---

# Información comercial, representación, exposición y calidad

## Definición

### Información comercial

> La **información comercial** es el conjunto de contenidos, datos, afirmaciones y relaciones mediante los que un ecommerce describe sus productos, variantes, ofertas, vendedores y condiciones de comercialización. Comprende los hechos expresados, su significado, las relaciones entre entidades, su atribución y las circunstancias en las que resultan válidos. — BASE §1

### Representación y exposición

> La **representación** es la forma concreta en que esa información se expresa y organiza en una interfaz; la **exposición** comprende las condiciones bajo las que se publica, distribuye, recupera y consume. Una misma realidad comercial puede disponer de distintas representaciones, con niveles de detalle y funciones diferentes. — BASE §1

| Concepto | Significado en el sistema |
|---|---|
| **Información comercial** | Contenidos, datos, afirmaciones y relaciones que describen la realidad comercial, sus entidades y condiciones. |
| **Representación** | Forma concreta en que esa información se expresa y organiza en una interfaz. |
| **Exposición** | Condiciones bajo las que la información se publica, distribuye, recupera y consume. |

### Calidad

> La calidad se determina por la **capacidad de la información comercial y de sus condiciones de representación y exposición para resolver cuestiones informativas relevantes**, proporcionando respuestas suficientes, interpretables, atribuibles y fundamentadas para la entidad y las condiciones consideradas. — BASE §1

### Dos dimensiones de evaluación

- **Técnica:** condiciones de publicación, acceso, legibilidad, estructura, conformidad y distribución que permiten localizar, recuperar y consumir la información comercial mediante las interfaces pertinentes. — CTX §3
- **Informativa y semántica:** suficiencia, detalle, significado, relaciones, atribución, vigencia, coherencia y fundamento de la información necesaria para resolver las cuestiones relevantes. — CTX §3

## Reglas e invariantes

1. **Información, representación y exposición no son sinónimos.** La representación es una dimensión del objeto de estudio, pero **no sustituye a la información comercial como objeto principal**.
2. **Las dos dimensiones no son equivalentes.** Una interfaz técnicamente conforme puede exponer información insuficiente para responder una cuestión de compra. A su vez, que una respuesta pueda fundamentarse en una interfaz no elimina las limitaciones técnicas o informativas de otra.
3. **Lo que separa ambas dimensiones es el objeto de la pregunta evaluativa:**
   - la técnica examina **cómo se implementa y expone la interfaz** conforme a sus especificaciones;
   - la informativa examina, para una cuestión de demanda concreta, **qué información pertinente puede obtenerse y leerse y qué permite determinar y fundamentar**.
4. **La calidad evaluada es la de la información expuesta**, no la del producto. Una respuesta suficientemente fundamentada puede acreditar tanto la adecuación como la incompatibilidad de una oferta con una necesidad.
5. **La calidad no se mide por acumulación** de atributos ni por cumplimiento formal de un formato.

## Distinciones

| Frente a | Diferencia |
|---|---|
| Calidad del producto | Se evalúa la información sobre el producto, no el producto. |
| Conveniencia para un comprador | Se evalúa si puede determinarse la respuesta, no si la respuesta es favorable. |
| Conformidad técnica | No basta para resolver cuestiones, y su incumplimiento no determina por sí mismo una insuficiencia informativa. Solo cuenta su efecto sobre la información pertinente utilizable. Ver [evaluation-scopes](evaluation-scopes.md#punto-de-contacto-entre-la-evaluación-técnica-y-la-informativa). |
| Cantidad de datos | Más atributos no implica mayor capacidad de resolver las cuestiones pertinentes. |

## Interpretación

Una misma realidad comercial (un producto, sus variantes, una oferta) puede aparecer en varias representaciones: el HTML de la ficha, el marcado Schema.org o el feed de un catálogo. Esas representaciones tienen funciones, alcances y niveles de detalle distintos. Para interpretar información de varias representaciones hay que preservar la identidad de las entidades, el alcance, las condiciones y el momento de cada afirmación. Ver [evaluation-scopes](evaluation-scopes.md#complementariedad-y-coherencia-entre-representaciones).

## Relacionado

- [scope](../00-context/scope.md): problema y objeto del estudio.
- [ai-functions](ai-functions.md): qué operaciones de conocimiento debe favorecer la información.
- [demand-model](demand-model.md): las cuestiones que la información debe poder resolver.
- [evaluation-architecture](evaluation-architecture.md): cómo se evalúan ambas dimensiones.
