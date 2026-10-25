---
id: product-taxonomy-subclasses
title: Taxonomía — subclases y paso de la clase al modelo de demanda
layer: method
status: propuesta
version: 1.6
updated: 2026-10-25
sources: [TAX §5, TAX §6, TAX §7, INTAKE 2026-10-24-define-class, INTAKE 2026-10-24-specialization-criterion, INTAKE 2026-10-25-class-composition, INTAKE 2026-10-25-own-questions-offer, INTAKE 2026-10-25-objective-classification, INTAKE 2026-10-25-requirements-purpose]
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

Esta prueba rige la creación de subclases o niveles jerárquicos de la taxonomía. Para incorporar una especialización a la clase de estudio rige el [criterio de especialización](../../10-model/study-class.md#criterio-de-especialización) del canon ([D-022](../../30-governance/decisions.md#d-022)).

## Cuatro salidas posibles del análisis

- **Conservar clase única:** no existe diferencia informativa suficientemente fundamentada.
- **Conservar la clase y condicionar requisitos:** algunas cuestiones aplican solo bajo determinadas características, sin construir un modelo independiente.
- **Crear una faceta transversal:** una dimensión (uso, estilo, protección) segmenta productos de diversas clases.
- **Crear una subclase con modelo propio:** cambia de forma estable un conjunto importante de cuestiones, con una definición clara y evidencias suficientes.

Cómo se representan estas salidas al componer una [clase de estudio](../../10-model/study-class.md) está pendiente ([OQ-37](../../30-governance/open-questions.md)). Para las distinciones que no cumplen la condición 4 del criterio, [D-024](../../30-governance/decisions.md#d-024) ya usa la salida «conservar la clase y condicionar requisitos».

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

## Caso de trabajo: juego de sábanas de coralina

> **Caso ilustrativo.** Muestra cómo se aplican el [eje de base](../../10-model/study-class.md#clase-general-el-eje-de-base), la [composición de la clase](../../10-model/study-class.md#composición-de-la-clase) y el [criterio de especialización](../../10-model/study-class.md#criterio-de-especialización); **no es una clase aprobada**. Fuentes: `INTAKE 2026-10-24-specialization-criterion`; para la composición por piezas, `INTAKE 2026-10-25-class-composition`; para las cuestiones propias del polar, `INTAKE 2026-10-25-own-questions-offer`; para los apoyos en la base heredada, `INTAKE 2026-10-25-objective-classification`; y para la redacción del juego y del polar, `INTAKE 2026-10-25-requirements-purpose`.

**Producto:** juego de sábanas Coralina de burritoblanco.com, marfil, diseño trenzado, 100 % poliéster, declarado «de invierno», con 7 medidas de cama.

**Clase general: composición por piezas.** Shopify no tiene «juego de sábanas», así que el juego entra como candidata a especialización, y cada pieza aporta los requisitos de su categoría:

| Pieza | Shopify | Amazon.es |
|---|---|---|
| Encimera | `hg-15-1-2-2` Sábanas planas | `3250024031` Sábanas encimeras, PTD `FLAT_SHEET` |
| Bajera | `hg-15-1-2-1` Sábanas ajustables | `3250023031` Bajeras ajustables, PTD `FITTED_SHEET` |
| Fundas | `hg-15-1-8-2` Fundas de almohada (→ Google `2927`) | `3250027031`, PTD `PILLOWCASE` |

- Se descarta Shopify `hg-15-1-11` «Juegos de cama» (*Bedding Sets*): Google la mapea a la genérica `569`, y sus atributos («Nivel de calidez» *«del edredón o la colcha»*) corresponden a juegos de edredón.

| Candidata | Tipo | Apoyo en las referencias | Efecto sobre las cuestiones | Resultado |
|---|---|---|---|---|
| Juego | Función o composición | Shopify: atributo `bedding-pieces-included` de Sábanas, madre de Sábanas planas y Sábanas ajustables, en la base heredada de esas piezas ([D-029](../../30-governance/decisions.md#d-029)). Amazon: nodo `3250028031` «Juegos de sábanas y fundas de almohada», PTD `BED_LINEN_SET` (`included_components`, `number_of_pieces`) | Aporta los requisitos del conjunto: qué piezas incluye, cuántas y en qué medidas ([D-023](../../30-governance/decisions.md#d-023), [D-032](../../30-governance/decisions.md#d-032)) | Especialización |
| Uso invernal | Uso | Declarado en la página. Amazon: PTD `BED_LINEN_SET`, `seasons` = Invierno. Shopify: `warmth-level` «Cálido (invierno)», solo asignado a Juegos de cama | Añade abrigo y temporada | Especialización |
| Tejido polar | Material | Shopify: `fabric__fleece` (etiqueta «Vellón») en el atributo «Tejido» de Sábanas, heredado por Sábanas planas y Sábanas ajustables ([D-029](../../30-governance/decisions.md#d-029)), y `fleece-finish-surface`, cuya definición vincula el acabado con la formación de bolitas. Amazon: «Forro polar» como material en unos 120 tipos PTD | Añade bolitas, electricidad estática, transpirabilidad, abrigo y gramaje, pérdida de pelo; el número de hilos deja de aplicarse. Con la regla de las cuestiones propias ([D-026](../../30-governance/decisions.md#d-026)), polar «trae bolitas, electricidad estática y pérdida de pelo»; el gramaje está en la base (⚠ Ver [I-13](../../30-governance/issues.md#i-13)). En la pieza de las fundas, las bolitas y la electricidad estática también están en la base (`PILLOWCASE` `special_feature`); la pérdida de pelo no está en ninguna base, así que el polar sigue siendo especialización. Leer la base pieza a pieza o para todo el juego no altera el resultado ([D-032](../../30-governance/decisions.md#d-032)) | Especialización |
| Diseño trenzado, color marfil | Valores estéticos | — | — | Descartada (condición 1) |
| Medida de 90 cm | Variante | — | — | Descartada (condición 1) |
| Infantil | — | — | — | Descartada (no declarado) |

**Nivel del tejido (condición 5).** «Coralina» no existe en ninguna referencia y es el valor declarado del tejido. «Tejido de pelo» es demasiado amplio: la franela y el terciopelo no comparten las cuestiones. «Coralina» no añade cuestiones frente a otros polares: cambian los valores.

**Clase de estudio:** Sábanas planas + Sábanas ajustables + Fundas de almohada → juego + uso invernal + tejido polar, con la coralina como valor del tejido.

**Observaciones del caso:**

- Las especializaciones salieron de atributos (temporada, tejido, piezas), no de nodos de los árboles.
- Shopify asigna atributos de forma incompleta: `warmth-level` no está en Sábanas.
- El anclaje más preciso de «juego» vino de Amazon.
- Google solo confirmó la clase general.

Los demás casos de evaluación del método están en [cases](cases.md).

## De la clase al modelo de demanda

El canon fija la clase objeto del modelo de demanda, la **[clase de estudio](../../10-model/study-class.md)**: clase general más todas las especializaciones aplicables, que pueden ser facetas concurrentes ([D-020](../../30-governance/decisions.md#d-020)). También fija el método general de construcción del catálogo: **observar atributos e información comercial publicada; inferir cuestiones relevantes; formular y normalizar requisitos; justificar su inclusión e importancia relativa** ([modelo de demanda](../../10-model/demand-model.md)). La taxonomía organiza la **selección de la clase y la detección de diferencias**, no modifica ese procedimiento.

Para cada clase aprobada se recomienda mantener una **matriz de continuidad**: requisitos comunes de la familia, requisitos específicos, requisitos condicionados y cuestiones excluidas por no aplicables. Cada requisito conservará su pregunta, dimensión, entidad, alcance, aplicabilidad, importancia relativa, fundamento y fuentes. Un mismo requisito podrá asociarse a varias clases sin duplicar su definición.

Hay tres separaciones necesarias:

1. **Clasificación frente a demanda:** la taxonomía describe el dominio; el requisito formula una necesidad de conocimiento.
2. **Requisito informativo frente a atributo del feed:** el atributo puede contribuir a una respuesta, pero ni define automáticamente el requisito ni su importancia.
3. **Clases frente a interfaces:** la pregunta pertenece al modelo de demanda; su pertinencia y capacidad de resolución se evalúan posteriormente en Catálogos distribuidos, Web y Web Schema.org, según sus funciones y condiciones ([ámbitos](../../10-model/evaluation-scopes.md)).

La [disponibilidad efectiva](../../10-model/effective-availability.md), los [criterios de aceptación](../../10-model/acceptance-criteria.md), las [propiedades P06–P18](../../10-model/quality-properties.md) y la valoración por requisito e interfaz pertenecen al sistema de auditoría posterior. No deben introducirse como criterios técnicos de fusiones taxonómicas ni utilizarse para decidir qué es una clase.
