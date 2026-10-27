---
id: requirement-description
title: Descripción de un requisito
layer: model
status: vigente
version: 1.1
updated: 2026-10-27
sources: [INTAKE 2026-10-26-choice-criteria-and-descriptions, INTAKE 2026-10-27-paa-classification-criteria]
---

# Descripción de un requisito

## Definición

> Los requisitos informativos necesitan una descripción. A veces el título puede ser bastante abstracto y la descripción debe ayudar a concretarlo. — palabras del usuario, INTAKE 2026-10-26-choice-criteria-and-descriptions

La descripción concreta el título, que es la pregunta del [requisito informativo](demand-model.md#requisito-informativo-ri). El catálogo la registra en cada requisito ([D-092](../30-governance/decisions.md#d-092)).

## Reglas e invariantes

1. **Tres partes.** El usuario aceptó este patrón:

   > 1. qué se pregunta en concreto, con ejemplos de lo que abarca;
   > 2. qué tipo de información lo responde;
   > 3. qué no lo responde y con qué requisito vecino no se confunde.
   >
   > — INTAKE 2026-10-26-choice-criteria-and-descriptions

2. **No repite la información resolutiva.** La descripción es prosa para personas y agentes; la [información resolutiva](resolving-information.md), la lista estructurada de aportaciones resolutivas. La parte 2 dice en prosa qué tipo de información responde, sin enumerar esa lista ([D-093](../30-governance/decisions.md#d-093)).

## Distinciones

| Par | Diferencia |
|---|---|
| Descripción frente a **pregunta** | La pregunta es la cuestión evaluable; la descripción la concreta sin sustituirla. |
| Descripción frente a **información resolutiva** | La descripción es prosa; la información resolutiva, la lista de aportaciones, cada una con su componente, su origen y respaldo y las tiendas en que se ha observado. |
| Descripción frente a **perfil del RI** | El [perfil de resolución y pertinencia](demand-model.md#núcleo-de-conocimiento-y-perfil-de-resolución-y-pertinencia) es un instrumento auxiliar de la auditoría, en propuesta; su relación con las partes 1 y 3 está pendiente ([OQ-03](../30-governance/open-questions.md)). |

## Ejemplos

Ejemplos que el usuario dio por buenos:

> - **cat.fundas-de-almohada/06 · ¿Qué duración y resistencia al uso y al lavado tiene?** — Cuánto dura la pieza y si mantiene su aspecto y sus medidas con el uso y los lavados: si destiñe, encoge, forma bolitas, se mancha o se desgarra con facilidad, y si seca rápido. Lo responde una declaración del vendedor o del fabricante sobre esas prestaciones, o el resultado de un ensayo (solidez del color, estabilidad dimensional). No lo responden el material ni el tejido por sí solos («percal», «100 % algodón»). Tampoco las instrucciones de lavado: son otro requisito, `cat.ropa-de-casa/02`. *(Actualizado por [D-108](../30-governance/decisions.md#d-108): la lista se encabeza con la duración y las arrugas pasan a un requisito propio.)*
> - **inf/01 · ¿Qué nivel de abrigo o de frescor ofrece (fresca de verano, para todo el año, cálida de invierno)?** (candidato reformulado) — Si la sábana resulta fresca o abriga al dormir, y para qué temporada o clima está pensada. Lo responde una declaración expresa («fresca, para verano», «cálida, para invierno») o un ensayo térmico. No lo responden el tejido ni la composición («percal», «coralina»): deducir la sensación térmica de ellos es una derivación que no se admite. La transpiración y la gestión de la humedad son otro requisito. *(Actualizado por [D-108](../30-governance/decisions.md#d-108): frescor y abrigo, una sola dimensión.)*
> - **gen/21 · ¿Qué incluye exactamente la oferta?** — Todas las piezas, unidades y accesorios que recibe el comprador por el precio indicado. Incluye también lo que aparece en las imágenes o en el nombre pero no se entrega (por ejemplo, el relleno en la foto de una funda nórdica; ejemplo hipotético). En un juego, la composición de piezas es otro requisito, `esp.juego/01`.
> - **cat.sabanas-ajustables/01 · ¿Hasta qué altura de colchón se ajusta?** — La altura máxima de colchón, o el rango de alturas, que admite la bajera, normalmente como profundidad del bolsillo en cm. Cómo se sujeta al colchón es otra cuestión, `inf/02`.
>
> — INTAKE 2026-10-26-choice-criteria-and-descriptions

El segundo ejemplo aplica la regla de la [prestación derivada de un atributo](choice-criteria.md#prestación-derivada-de-un-atributo) ([D-090](../30-governance/decisions.md#d-090)).

## Pendiente

- Relación de las partes 1 y 3 con los componentes, las expresiones de ejemplo y los casos fronterizos del perfil del RI ([OQ-03](../30-governance/open-questions.md)).
- Registro en el catálogo y en la redacción de los bloques.
- Presentación de un requisito repetido en bloques hermanos según la pieza: la pregunta y la descripción son las mismas ([D-107](../30-governance/decisions.md#d-107), [OQ-60](../30-governance/open-questions.md)).

## Relacionado

- [demand-model](demand-model.md): requisito informativo.
- [resolving-information](resolving-information.md): información resolutiva.
- [choice-criteria](choice-criteria.md): criterios de elección.
- [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md#formato-del-catálogo): campos de un requisito (método).
