---
id: study-class
title: Clase de estudio
layer: model
status: vigente
version: 1.5
updated: 2026-10-26
sources: [INTAKE 2026-10-24-define-class, INTAKE 2026-10-24-specialization-criterion, INTAKE 2026-10-25-class-composition, INTAKE 2026-10-25-own-questions-offer, INTAKE 2026-10-25-objective-classification, INTAKE 2026-10-25-requirements-purpose, INTAKE 2026-10-25-requirement-blocks, INTAKE 2026-10-25-training-runtime, INTAKE 2026-10-25-induced-rules, INTAKE 2026-10-25-offer-application, INTAKE 2026-10-26-training-v4-review]
---

# Clase de estudio

Parte del [modelo de demanda](demand-model.md). La clase de estudio es el medio para descubrir los bloques de requisitos que forman el modelo de demanda de un producto; la identidad del modelo la da esa composición de requisitos, no la clase ([D-033](../30-governance/decisions.md#d-033)).

> La **clase objeto del modelo de demanda** se define partiendo de una **clase general** e incorporando **tantas especializaciones como sean relevantes** para las necesidades informativas del producto estudiado. — INTAKE 2026-10-24-define-class

Es la «clase estudiada» a la que se refieren BASE §4.1 y §4.2 ([D-020](../30-governance/decisions.md#d-020)).

## Regla metodológica

> 1. **Identificar la clase general** a la que pertenece el producto.
> 2. **Reconocer las especializaciones pertinentes** por uso, material, función u otras características, siempre que introduzcan o modifiquen cuestiones informativas relevantes.
> 3. **Componer la clase de estudio** mediante la clase general y todas las especializaciones aplicables. No es necesario que formen una jerarquía estricta: pueden ser facetas que concurren.
> 4. **Construir el modelo de demanda** integrando los requisitos comunes y los específicos, sin duplicados y revisando su aplicabilidad e importancia relativa.
>
> — INTAKE 2026-10-24-define-class

> **Principio:** buscar la **especificidad informativa necesaria**, no el mayor número posible de subclases. — INTAKE 2026-10-24-define-class

> **Propósito:** «[…] el propósito es establecer requisitos informativos. Esto es lo más importante (+ el matiz de denominación que hemos especificado cuando tiene sentido aunque no aporte)». Lectura aceptada: la pregunta que manda es qué requisitos informativos produce la clase. Que algo sea especialización o valor es instrumental. Lo único que entra sin aportar requisitos es lo que nombra la clase por clasificación objetiva, cuando tiene sentido. — INTAKE 2026-10-25-requirements-purpose; el matiz es la [clasificación objetiva](#composición-de-la-clase) ([D-032](../30-governance/decisions.md#d-032)), que queda como alias ([D-033](../30-governance/decisions.md#d-033))

| Elemento | Papel en la clase de estudio |
|---|---|
| **Clase general** | Clase a la que pertenece el producto. Es el punto de partida. Es una categoría de la Shopify Standard Product Taxonomy, en la versión fijada ([eje de base](#clase-general-el-eje-de-base)), o la [composición](#composición-de-la-clase) de varias si el producto las abarca. |
| **Especialización** | Por uso, material, función u otras características del producto (no de la oferta: [D-048](../30-governance/decisions.md#d-048)). Se incorpora a la clase de estudio si es **pertinente**, es decir, si cumple el [criterio de especialización](#criterio-de-especialización). |
| **Variante** | «La medida de cama (por ejemplo, 90 cm) caracteriza una variante, pero no obliga por sí sola a crear otra clase». — INTAKE 2026-10-24-define-class |

El paso 4 se realiza con el recorrido del [sistema de construcción](demand-model.md#sistema-de-construcción-vigente) y produce un [modelo de demanda compuesto por bloques de requisitos](demand-model.md#composición-e-identidad-del-modelo) ([D-033](../30-governance/decisions.md#d-033)).

> - La especialización es la característica que forma un bloque: trae cuestiones que no se aplican a los demás productos de la clase.
> - Una característica declarada que revela una dimensión que tienen todos los productos de la clase no forma bloque. Ejemplos: el peinado y el mercerizado del algodón, o el bordado como decoración. Su cuestión va al bloque de la clase, para todos, y el valor declarado es la respuesta. Así, una página que informa menos no tiene menos requisitos.
>
> — INTAKE 2026-10-25-requirement-blocks; para una cuestión inferida, precisada por [D-041](../30-governance/decisions.md#d-041) y [D-044](../30-governance/decisions.md#d-044): entra en el bloque cuando el entrenamiento la acepta

## Clase general: el eje de base

> La clase general de una clase de estudio se fija en la Shopify Standard Product Taxonomy, en la versión fijada: es una categoría o, si el producto abarca varias, la composición de esas categorías. Lo que Shopify no distingue como categoría entra como especialización. — INTAKE 2026-10-24-specialization-criterion, enmendada por [D-023](../30-governance/decisions.md#d-023)

La versión fijada es la adoptada como referencia de Shopify: hoy, v2026-08 ([sources](../20-methods/product-taxonomy/sources.md#shopify-base-estructural-y-vocabulario-de-atributos)). Lo que Shopify no distingue como categoría entra como **candidata** a especialización y se examina con el [criterio de especialización](#criterio-de-especialización); no se incorpora automáticamente. La regla determina qué categoría o categorías forman la clase general; no convierte cada categoría de Shopify en una clase aprobada ([D-021](../30-governance/decisions.md#d-021)).

## Composición de la clase

> - El modelo de clase es un sistema de composición de requisitos. Cada componente (categoría de Shopify o especialización) aporta sus requisitos, y el modelo de demanda de la clase de estudio los integra sin duplicados.
> - Si el producto abarca varias categorías de Shopify (por ejemplo, un juego con piezas de categorías distintas), la clase general es la composición de esas categorías, no su ancestro común. […]
> - Una categoría entra en la composición si aporta requisitos al producto o a alguna de sus piezas. En un juego, cada pieza es una entidad. […]
> - La especialización «juego» aporta los requisitos del conjunto: qué piezas incluye y cuántas de cada una (enmendada por [D-086](../30-governance/decisions.md#d-086): las medidas de cada pieza las preguntan los bloques de su categoría).
>
> — INTAKE 2026-10-25-class-composition; la última frase del tercer punto, sustituida por [D-028](../30-governance/decisions.md#d-028); precisada por [D-033](../30-governance/decisions.md#d-033): la composición de la clase es el medio para descubrir los bloques, y la identidad la da la composición de requisitos

> **Clasificación objetiva:** una categoría candidata en la que el producto entra por clasificación objetiva forma parte de la composición aunque no aporte requisitos propios. **Base de una categoría de Shopify:** sus atributos propios más los de sus categorías madre (una categoría hija es un tipo de su madre). — INTAKE 2026-10-25-objective-classification

Una categoría aporta requisitos a una pieza aunque sean del mismo tipo que los de otra, porque recaen sobre otra entidad ([D-023](../30-governance/decisions.md#d-023)). Por clasificación objetiva, una categoría entra solo cuando tiene sentido: no entra por denominación una categoría que traería requisitos que no aplican ([D-032](../30-governance/decisions.md#d-032)). La que entra sin aportar requisitos es un **alias**: «el objetivo de esto es puramente de etiquetado, denominación» (INTAKE 2026-10-25-requirement-blocks); no forma parte de la identidad del modelo ([D-033](../30-governance/decisions.md#d-033)). La base de Shopify se aplica a la composición, a la condición 4 y a la regla de las cuestiones propias ([D-029](../30-governance/decisions.md#d-029)). Lo que se registra son los modelos, como composiciones de bloques ([D-033](../30-governance/decisions.md#d-033)). Siguen pendientes, en parte resueltas por [D-057](../30-governance/decisions.md#d-057), la prueba operativa de «aportar requisitos» ([OQ-39](../30-governance/open-questions.md)) y la de la clasificación objetiva ([OQ-43](../30-governance/open-questions.md)).

La hoja más específica que cumple el producto entra como categoría aunque herede todos sus requisitos de las madres: es el componente por el que entran en el producto. Una hermana que nombra otra característica del producto (Sofás de dos plazas en un sofá cama) trae por herencia esos mismos requisitos, ya aportados, y entra como alias por clasificación objetiva; no es una entrada duplicada ([D-057](../30-governance/decisions.md#d-057)):

> «La hoja más específica entra como categoría aunque herede todo; una hermana que nombra otra característica (dos plazas), como alias.»
>
> — INTAKE 2026-10-26-training-v4-review (opción elegida)

## Criterio de especialización

> Una característica es especialización de la clase de estudio cuando cumple las cinco condiciones:
>
> 1. **Es del producto y estable:** un uso, material o función declarados. No es una variante, ni un valor estético, ni una etiqueta promocional.
> 2. **Tiene un efecto comparativo.** Frente a la clase general sin esa característica, produce al menos uno de estos efectos, expresado como cuestión concreta y neutral respecto de la respuesta: añade una cuestión; cambia el alcance o la desagregación de una cuestión; cambia la aplicabilidad (incluido que una cuestión deje de aplicarse); cambia la importancia relativa.
> 3. **Las cuestiones afectadas son relevantes** para evaluar la clase, no para un comprador concreto.
> 4. **Tiene apoyo en las referencias:** al menos la dimensión existe en Shopify, Amazon o Google, y el valor queda anclado con una relación tipada (equivalente, más amplia…).
> 5. **Nivel:** la especialización se fija en el nivel más general cuyos miembros comparten las cuestiones que introduce. Solo se baja de nivel si el inferior añade o modifica cuestiones. El valor concreto del producto se registra como valor de esa dimensión. El anclaje se hace en ese nivel; si la referencia no lo tiene, se ancla con una relación tipada.
>
> **No cuentan:** un nodo o valor que solo existe en una referencia; un cambio de los valores esperados; una característica de variante; la proximidad temática; un requisito de plataforma o de feed.
>
> — INTAKE 2026-10-24-specialization-criterion; condición 1 enmendada por [D-027](../30-governance/decisions.md#d-027) y restablecida por [D-048](../30-governance/decisions.md#d-048) (solo características del producto)

La condición 1 solo admite características del producto: lo de la oferta activa requisitos condicionados de la capa general o de la clase y no forma especializaciones ([D-048](../30-governance/decisions.md#d-048), que sustituye a D-027); la condición 2 se aplica con la regla de las cuestiones propias cuando todo producto de la clase tiene la dimensión ([D-026](../30-governance/decisions.md#d-026)), ampliada a los valores que activan cuestiones condicionadas ([D-037](../30-governance/decisions.md#d-037)); la condición 4 se aplica en lectura estricta ([D-024](../30-governance/decisions.md#d-024)); las características especiales de los PTD cuentan como base y como apoyo ([D-030](../30-governance/decisions.md#d-030)); y los beneficios reclamados quedan excluidos ([D-025](../30-governance/decisions.md#d-025)), pero no el material reciclado ([D-031](../30-governance/decisions.md#d-031)). Estas reglas se citan a continuación.

> **Cuestiones propias:** para una dimensión que todo producto de la clase tiene, un valor es especialización solo si trae cuestiones propias, que no salen de las dimensiones de la clase general. Si solo cambia los valores, o solo hace que algunas cuestiones dejen de aplicarse, es un valor que condiciona (como en D-024). — INTAKE 2026-10-25-own-questions-offer

> Confirmado por el usuario: la condición de la unidad es un requisito general. Por tanto, outlet, liquidación, exposición o reacondicionado son valores de la oferta que condicionan cuestiones generales, no especializaciones, en cualquier producto.
>
> Extensión simétrica de D-026: un valor que **activa** cuestiones condicionadas ya previstas en la base también es un valor que condiciona. Solo es especialización si trae cuestiones que la base no prevé. […]
>
> — INTAKE 2026-10-25-requirement-blocks; sustituye la cita «Oferta» de INTAKE 2026-10-25-own-questions-offer ([D-037](../30-governance/decisions.md#d-037)); precisada por [D-048](../30-governance/decisions.md#d-048): en un valor de la oferta, esas cuestiones son requisitos condicionados de la clase, nunca especialización

El disparador es el estado declarado de la unidad: la unidad de exposición que la ficha identifica como tal cuenta como estado declarado; la etiqueta «outlet» sola, no ([D-057](../30-governance/decisions.md#d-057)).

> **Evidencia** […]: con las cinco condiciones razonadas en la ficha, la especialización queda provisional. La valida el usuario, como responsable. El contraste con ecommerce referentes (MPIR) la confirma o la revisa después, cuando exista. No se fija ningún umbral numérico. — INTAKE 2026-10-24-specialization-criterion

Validación precisada por [D-041](../30-governance/decisions.md#d-041) y [D-044](../30-governance/decisions.md#d-044): la hace el entrenamiento contra el marco que define la persona responsable, sin bloquear la ejecución; entretanto, la especialización se usa como provisional y se encola ([model-training](model-training.md)).

> **Condición 4, lectura estricta:** la dimensión debe existir en algún componente de la clase de estudio, en cualquiera de las tres referencias: atributos de la categoría de Shopify, nodo o PTD de Amazon, o categoría de Google. El apoyo en una categoría afín se anota en la ficha como evidencia complementaria, pero no basta por sí solo. Una distinción que no cumple la condición no se pierde: sus cuestiones quedan en la clase general como requisitos condicionados (la salida «conservar la clase y condicionar requisitos»). — INTAKE 2026-10-25-class-composition

> **Beneficios reclamados:** un beneficio que el producto reclama (por ejemplo, «favorece la higiene dental») no es especialización, salvo que las referencias tengan un tipo de producto definido por él. Su fundamento se evalúa en la auditoría, no en la clase. — INTAKE 2026-10-25-class-composition

> **Características especiales de un PTD:** los valores de la propiedad «Características especiales» (`special_feature`) de un PTD de Amazon cuentan como dimensiones de la base de la clase (regla de las cuestiones propias) y como apoyo (condición 4). — INTAKE 2026-10-25-objective-classification

> **Material reciclado:** es especialización, no beneficio reclamado: es composición verificable y trae cuestiones propias (qué proporción y en qué parte). «Sostenible» sí es beneficio reclamado. — INTAKE 2026-10-25-objective-classification

Lectura del criterio ([D-022](../30-governance/decisions.md#d-022)):

- La ficha es la [ficha de clase](../20-methods/product-taxonomy/data-model-governance.md#anexo-a-ficha-de-clase-propuesta). La validación ya no la hace un responsable, sino el entrenamiento ([D-044](../30-governance/decisions.md#d-044)).
- Las relaciones tipadas son las de las [correspondencias](../20-methods/product-taxonomy/integration.md#relaciones-que-debe-poder-registrar-un-mapeo).
- La lista de la condición 1 no es cerrada: se lee junto con «u otras características» de la regla metodológica. Lo decisivo es que la característica sea del producto, declarada y estable ([D-048](../30-governance/decisions.md#d-048)).
- «Un nodo o valor que solo existe en una referencia» significa que su mera existencia en una referencia no basta.
- El criterio rige la incorporación de una especialización a la clase de estudio. La [prueba de especialización](../20-methods/product-taxonomy/subclasses.md#prueba-de-especialización) sigue rigiendo la creación de subclases o niveles jerárquicos de la taxonomía.

## Ejemplo

Ilustrativo; no es una clase aprobada:

> **Juegos de sábanas** (clase general) + **uso invernal** (especialización) + **tejido de coralina** (especialización) → **clase de estudio: juegos de sábanas de coralina para invierno**. — INTAKE 2026-10-24-define-class

Al aplicar la composición por piezas, la clase general es la composición de Sábanas planas (encimera), Sábanas ajustables (bajera) y Fundas de almohada (fundas), y «juego» es candidata (Shopify no tiene «juego de sábanas») y cumple el criterio. Por la condición 5 del criterio, el tejido se fija en «polar» y la coralina queda como valor del tejido ([caso de trabajo](../20-methods/product-taxonomy/subclasses.md#caso-de-trabajo-juego-de-sábanas-de-coralina)).

## Relacionado

- [demand-model](demand-model.md) — modelo de demanda, composición por bloques y capa general
- [model-training](model-training.md) — entrenamiento y ejecución del modelo de demanda
- [product-taxonomy](../20-methods/product-taxonomy/README.md) (método, propuesta): [subclasses](../20-methods/product-taxonomy/subclasses.md), [cases](../20-methods/product-taxonomy/cases.md), [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md)
