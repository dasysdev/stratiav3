---
id: product-taxonomy-subclasses
title: Taxonomía — subclases y paso de la clase al modelo de demanda
layer: method
status: propuesta
version: 1.1
updated: 2026-10-24
sources: [TAX §5, TAX §6, TAX §7, INTAKE 2026-10-24-define-class]
---

# Taxonomía — subclases y paso de la clase al modelo de demanda

Parte de [Taxonomía de clases de producto](README.md).

## La subclase debe expresar diferencia informativa, no solo una etiqueta

Una subclase justifica su existencia cuando identifica un conjunto estable de productos con **función, uso o características que generan cuestiones informativas centrales distintas**, cambios materiales de aplicabilidad o una importancia relativa justificablemente diferente respecto de la clase base.

El mero hecho de que Amazon disponga de un nodo adicional o Shopify ofrezca un valor de estilo **no obliga** a crear una nueva clase. También puede ser innecesaria una subclase si las preguntas son esencialmente las mismas y solo cambian los valores esperados, como negro frente a marrón.

## Prueba de especialización

| Pregunta de control | Criterio de decisión |
|---|---|
| ¿Hay una definición positiva clara? | Se puede explicar la pertenencia sin definir la clase como simple resto de otra. |
| ¿Existe una diferencia funcional estable? | El uso o función no depende solo de una etiqueta promocional. |
| ¿Cambian preguntas relevantes? | Aparecen cuestiones nuevas o diferencias sustantivas en alcance, aplicabilidad o importancia relativa. |
| ¿Hay respaldo observable? | La distinción tiene apoyo en fuentes taxonómicas y/o ecommerce referentes. |
| ¿Se resuelve con una condición? | Si basta con una regla de aplicabilidad en el mismo modelo, evitar duplicar clases. |
| ¿Se solapa transversalmente? | Si cruza múltiples ramas, considerar faceta o pertenencia múltiple en lugar de un único hijo. |

## Cuatro salidas posibles del análisis

- **Conservar clase única:** no existe diferencia informativa suficientemente fundamentada.
- **Conservar la clase y condicionar requisitos:** algunas cuestiones aplican solo bajo determinadas características, sin construir un modelo independiente.
- **Crear una faceta transversal:** una dimensión (uso, estilo, protección) segmenta productos de diversas clases.
- **Crear una subclase con modelo propio:** cambia de forma estable un conjunto importante de cuestiones, con una definición clara y evidencias suficientes.

Cómo se representan estas salidas al componer una [clase de estudio](../../10-model/demand-model.md#clase-de-estudio) está pendiente ([OQ-37](../../30-governance/open-questions.md)).

Cuando hay herencia de requisitos, la clase hija puede **reutilizar preguntas compartidas**, pero la aplicabilidad y la importancia relativa se revisan expresamente. No se hereda automáticamente la criticidad ni se asignan pesos numéricos universales ([importancia relativa](../../10-model/demand-model.md)).

## Ejemplo metodológico: botas urbanas y botas de montaña

> **Ejemplo hipotético.** Expresa la estrategia; **no certifica una jerarquía vigente de Amazon.es**.

### De la fuente al concepto interno

Se parte de una categoría amplia Shopify de botas. En sus valores descriptivos pueden existir estilos o usos orientados al senderismo; Amazon puede proponer rutas especializadas de calzado deportivo o de exterior, pero el nodo español específico deberá verificarse antes de incorporar su ID. Google puede ofrecer una categoría de calzado más general y datos descriptivos, sin aportar necesariamente la subclase buscada [R1, R5, R9].

| Elemento observado | Uso en el piloto | Precaución |
|---|---|---|
| Shopify: botas | Clase base candidata. | No supone que todas las botas compartan un modelo homogéneo. |
| Shopify: atributo o valor asociado a senderismo | Evidencia de una posible faceta de uso. | Un valor de atributo no es automáticamente un nuevo nodo. |
| Amazon: posible nodo de actividad o calzado de exterior | Especialización candidata por contrastar en Amazon.es. | No declarar equivalencia exacta sin revisar inclusiones y rutas. |
| Google: calzado y atributos comerciales | Contraste de categoría y dimensiones. | `product_type` del comerciante no es taxonomía de Google. |
| Ecommerce referentes | Evidencia de diferenciación informativa real. | Una estructura de menú aislada no demuestra demanda general. |

### Definiciones iniciales como hipótesis, no clases aprobadas

- **Botas de uso urbano o casual:** calzado tipo bota cuyo contexto predominante es el uso cotidiano y/o de moda. Debe definirse con criterios positivos; no basta decir «todas las botas que no son de montaña».
- **Botas de senderismo:** botas diseñadas o comercializadas para rutas a pie en terrenos naturales, con necesidades posibles sobre agarre, terreno, protección, impermeabilidad y estabilidad.
- **Botas de seguridad:** producto cuyo uso protector puede implicar requisitos de certificaciones y protecciones específicas.

Los tres conceptos pueden tener fronteras no excluyentes y deben validarse.

### Diferencias de cuestiones candidatas

| Cuestiones compartidas | ¿En qué puede diferir la demanda? |
|---|---|
| Talla y sistema de medidas; composición y materiales; variantes; precio, disponibilidad y condiciones de comercialización. | Urbano/casual: estilo, diseño, altura de caña, tipo de cierre o ajuste. Senderismo: terreno previsto, agarre, impermeabilidad, soporte, protección y características de suela. Seguridad: protección declarada, certificaciones, condiciones de uso y limitaciones. |

Estos son **candidatos a requisitos**, no un catálogo ya validado. Su formulación definitiva deberá ser una cuestión evaluable: por ejemplo, «¿Para qué tipos de terreno y condiciones de uso está diseñada la bota?». Una vez formulada, se justifica su relevancia, aplicabilidad y clase de importancia, sin inferirla de una etiqueta de Shopify o Amazon.

### Decisión del piloto

La pregunta no es «¿dónde está en el árbol de Amazon?», sino **«¿la distinción entre ambos usos cambia suficientemente lo que debemos poder conocer para evaluar la oferta?»**. Si la respuesta está fundamentada, se crea la subclase o faceta correspondiente; si no, se conserva la clase y se condicionan los requisitos relevantes. El acceso a la estructura Amazon mejoraría el fundamento, pero no reemplaza el análisis informativo.

## De la clase al modelo de demanda

El canon fija la clase objeto del modelo de demanda, la **[clase de estudio](../../10-model/demand-model.md#clase-de-estudio)**: clase general más todas las especializaciones aplicables, que pueden ser facetas concurrentes ([D-020](../../30-governance/decisions.md#d-020)). También fija el método general de construcción del catálogo: **observar atributos e información comercial publicada; inferir cuestiones relevantes; formular y normalizar requisitos; justificar su inclusión e importancia relativa** ([modelo de demanda](../../10-model/demand-model.md)). La taxonomía organiza la **selección de la clase y la detección de diferencias**, no modifica ese procedimiento.

Para cada clase aprobada se recomienda mantener una **matriz de continuidad**: requisitos comunes de la familia, requisitos específicos, requisitos condicionados y cuestiones excluidas por no aplicables. Cada requisito conservará su pregunta, dimensión, entidad, alcance, aplicabilidad, importancia relativa, fundamento y fuentes. Un mismo requisito podrá asociarse a varias clases sin duplicar su definición.

Hay tres separaciones necesarias:

1. **Clasificación frente a demanda:** la taxonomía describe el dominio; el requisito formula una necesidad de conocimiento.
2. **Requisito informativo frente a atributo del feed:** el atributo puede contribuir a una respuesta, pero ni define automáticamente el requisito ni su importancia.
3. **Clases frente a interfaces:** la pregunta pertenece al modelo de demanda; su pertinencia y capacidad de resolución se evalúan posteriormente en Catálogos distribuidos, Web y Web Schema.org, según sus funciones y condiciones ([ámbitos](../../10-model/evaluation-scopes.md)).

La [disponibilidad efectiva](../../10-model/effective-availability.md), los [criterios de aceptación](../../10-model/acceptance-criteria.md), las [propiedades P06–P18](../../10-model/quality-properties.md) y la valoración por requisito e interfaz pertenecen al sistema de auditoría posterior. No deben introducirse como criterios técnicos de fusiones taxonómicas ni utilizarse para decidir qué es una clase.
