---
id: product-taxonomy-requirement-blocks
title: Taxonomía — bloques de requisitos, capa general e importancia
layer: method
status: propuesta
version: 1.9
updated: 2026-10-25
sources: [INTAKE 2026-10-25-requirement-blocks, INTAKE 2026-10-25-block-catalog, INTAKE 2026-10-25-amazon-source-blocks, INTAKE 2026-10-25-training-runtime, INTAKE 2026-10-25-catalog-criteria, INTAKE 2026-10-25-induced-rules, INTAKE 2026-10-25-training-operation, INTAKE 2026-10-25-offer-application, INTAKE 2026-10-25-relevance-origin]
---

# Taxonomía — bloques de requisitos, capa general e importancia

Parte de [Taxonomía de clases de producto](README.md).

> **Estado: propuesta.** Punto de partida aceptado por el usuario «para empezar, lo iremos perfeccionando». El canon de la composición por bloques, la capa general y la importancia relativa está en [demand-model](../../10-model/demand-model.md#composición-e-identidad-del-modelo); este módulo recoge su operación inicial ([D-033](../../30-governance/decisions.md#d-033) a [D-036](../../30-governance/decisions.md#d-036) y [D-038](../../30-governance/decisions.md#d-038) a [D-041](../../30-governance/decisions.md#d-041), [D-043](../../30-governance/decisions.md#d-043) a [D-045](../../30-governance/decisions.md#d-045) y [D-047](../../30-governance/decisions.md#d-047) a [D-052](../../30-governance/decisions.md#d-052)). Fuentes: `INTAKE 2026-10-25-requirement-blocks`, `INTAKE 2026-10-25-block-catalog`, `INTAKE 2026-10-25-amazon-source-blocks`, `INTAKE 2026-10-25-training-runtime`, `INTAKE 2026-10-25-catalog-criteria`, `INTAKE 2026-10-25-induced-rules`, `INTAKE 2026-10-25-training-operation`, `INTAKE 2026-10-25-offer-application` e `INTAKE 2026-10-25-relevance-origin`.

## Bloques

La [identidad de un modelo de demanda](../../10-model/demand-model.md#composición-e-identidad-del-modelo) es su conjunto de bloques de requisitos; la aplicación es de la oferta ([D-047](../../30-governance/decisions.md#d-047)). Tipos de bloque, en el orden de la pila:

| Bloque | Qué contiene | De dónde sale |
|---|---|---|
| General universal | Cuestiones que se aplican a cualquier oferta | [Capa general](#capa-general) |
| General condicionado | Cuestiones que se aplican si se da un hecho declarado de la oferta (variantes, descuento, unidad no nueva…) o, en los elementos digitales, del producto | [Capa general](#capa-general) |
| Categoría (`cat.`) | Atributos propios de una categoría de Shopify que no lista ninguna de sus madres ([D-040](../../30-governance/decisions.md#d-040)), propiedades del PTD de Amazon relevantes para la clase ([D-039](../../30-governance/decisions.md#d-039)) y cuestiones inferidas aceptadas de la categoría. Es un único tipo: los bloques de las categorías madre forman el sector y el de la categoría del producto, la categoría; solo se distinguen por su posición | Referencias, base heredada ([D-029](../../30-governance/decisions.md#d-029)) y [cuestiones inferidas](#cuestiones-inferidas) |
| Especialización | Cuestiones que trae una característica y que no se aplican a los demás productos de la clase (juego, polar, piel…) | [Criterio de especialización](../../10-model/study-class.md#criterio-de-especialización) |

> Construir los bloques de categoría de forma determinista: un atributo repetido va siempre al bloque de la categoría más general que lo lista, para que un bloque de sector no cambie según el producto.
>
> Además, crear un catálogo de bloques cat. (preguntas e importancia por defecto), generado con la herramienta y revisado una vez por categoría. El clasificador elegiría bloques en lugar de redactarlos, lo que reduce la variación y el coste.
>
> — INTAKE 2026-10-25-amazon-source-blocks; la revisión por categoría la sustituye la compilación en el entrenamiento ([D-044](../../30-governance/decisions.md#d-044))

Así la parte de cada bloque `cat.` que sale de las referencias tiene un contenido fijo, que no depende del producto; las cuestiones inferidas solo entran en el bloque cuando se aceptan ([D-041](../../30-governance/decisions.md#d-041)), y la base heredada no se cuenta dos veces ([D-040](../../30-governance/decisions.md#d-040)). Formato e identificadores: [formato del catálogo](#formato-del-catálogo).

## Pruebas de importancia

Lectura operativa de las [definiciones del canon](../../10-model/demand-model.md#importancia-relativa), sin escala nueva. Forman parte del marco: las reglas de importancia inducidas en el entrenamiento operan dentro de ellas y no las modifican ([D-044](../../30-governance/decisions.md#d-044)):

| Nivel | Prueba |
|---|---|
| Crítico | Si esta cuestión no se resuelve, ¿la oferta deja de ser evaluable? (no se sabe qué se vende, cuánto cuesta o si se puede adquirir) |
| Principal | ¿Es uno de los criterios con los que se comparan y eligen ofertas de la clase? |
| Complementario | Relevante, pero no indispensable ni central para comparar |

- El canon pregunta si la oferta es **evaluable**, no si se puede comprar.
- Ejemplo del usuario: el mecanismo de un sofá cama es principal o complementario: «no impide comprar, no está al mismo nivel que precio, saber qué producto es».
- Los críticos son pocos y casi todos generales.
- La confianza en un requisito es independiente de su importancia ([canon](../../10-model/demand-model.md#reglas-e-invariantes)).

## Capa general

Cuestiones universales y condicionadas, con importancia por defecto ([canon](../../10-model/demand-model.md#capa-general), [D-034](../../30-governance/decisions.md#d-034)).

Contrastada con el artículo 97.1 del texto refundido de la Ley General para la Defensa de los Consumidores y Usuarios (RDL 1/2007; versión consolidada del BOE a 28/02/2026), que regula la información previa a una venta a distancia en España ([D-038](../../30-governance/decisions.md#d-038)), y con el artículo 19 del Reglamento (UE) 2023/988 de seguridad general de los productos (GPSR), que no se aplica a alimentos ni piensos, entre otros ([D-052](../../30-governance/decisions.md#d-052)). La columna «Apoyo» indica la letra del artículo; el origen de cada cuestión sigue su fuente: «normativa» solo si una norma la exige con claridad.

| Bloque | Entidad | Cuestión | Importancia por defecto | Apoyo |
|---|---|---|---|---|
| `gen` | Producto | ¿Qué es el producto y qué incluye exactamente? | Crítico | 97.1.a (también los bloques de clase) |
| `gen` | Producto | ¿Qué marca y modelo es? | Principal | GPSR 19.a, 19.c ([D-052](../../30-governance/decisions.md#d-052)) |
| `gen` | Producto | ¿Qué identificadores tiene (EAN/GTIN, referencia)? | Principal | GPSR 19.c |
| `gen` | Producto | ¿Quién es el fabricante (nombre, nombre comercial registrado o marca) y cuál es su dirección postal y electrónica? | Complementario | GPSR 19.a (en su ámbito) |
| `gen` | Producto | Si el fabricante no está establecido en la UE, ¿quién es la persona responsable en la UE y cuál es su dirección postal y electrónica? | Complementario | GPSR 19.b (en su ámbito) |
| `gen` | Producto | ¿Qué advertencias o información de seguridad acompañan al producto? | Principal | GPSR 19.d (en su ámbito) |
| `gen` | Producto | ¿Dónde se ha fabricado (país de fabricación)? | Complementario | — (referencias: `country_of_origin`, presente en todos los PTD de Amazon) |
| `gen` | Oferta | ¿Cuál es el precio total que paga el comprador, con impuestos y envío a España? | Crítico | 97.1.e |
| `gen` | Entrega | ¿De qué depende el coste del envío? | Principal | 97.1.e |
| `gen` | Oferta | ¿Está disponible y en qué variantes? | Crítico | — |
| `gen` | Oferta | ¿Tiene la oferta alguna promoción o descuento vigente (rebaja, cupón, regalo, unidades gratis…) y en qué consiste? Un «no» fundamentado la resuelve | Complementario | — ([D-049](../../30-governance/decisions.md#d-049); [OQ-50](../../30-governance/open-questions.md)) |
| `gen` | Oferta | ¿En qué estado se vende la unidad que se entrega? | Principal | — |
| `gen` | Entrega | ¿En qué plazo se entrega? | Principal | 97.1.h |
| `gen` | Entrega | Modalidades de entrega o recogida | Complementario | 97.1.h |
| `gen` | Oferta | ¿Qué medios de pago se aceptan? | Complementario | 97.1.h |
| `gen` | Condiciones | ¿Se puede desistir o devolver, en qué condiciones y plazo, con qué coste de devolución, y cuándo no procede? | Principal | 97.1.j, k, m |
| `gen` | Condiciones | ¿Qué garantía legal y, si las hay, qué garantías comerciales y asistencia posventa tiene? | Principal | 97.1.n, ñ |
| `gen` | Vendedor | ¿Quién vende la oferta? | Principal | 97.1.b |
| `gen` | Vendedor | ¿Cómo se contacta con el vendedor? | Complementario | 97.1.c, d |
| `gen` | Oferta | ¿Qué opiniones de compradores tiene y, si se publican, cómo se garantiza que proceden de compradores reales? | Complementario | — (directiva Omnibus, trasposición por comprobar) |
| `gen.cantidad-limitada` | Oferta | ¿En qué cantidad está disponible? | Crítico | — |
| `gen.variantes` | Variante | ¿Qué variantes hay y en qué se diferencian? | Crítico | — |
| `gen.unidad-no-nueva` | Oferta | ¿Por qué motivo (exposición, devolución, tara, fin de serie…) y con qué marcas o defectos se vende, y qué unidad se entrega? | Principal | — |
| `gen.descuento` | Oferta | ¿Desde qué precio de referencia y en qué condiciones se aplica el descuento? | Complementario | — |
| `gen.precio-personalizado` | Oferta | ¿El precio está personalizado por una decisión automatizada y con qué parámetros? | Principal | 97.1.f |
| `gen.elementos-digitales` | Producto (entra en el modelo, no en la aplicación) | ¿Qué funcionalidad y qué compatibilidad e interoperabilidad tiene? | Principal | 97.1.s, t |
| `gen.suscripcion` | Oferta | ¿Qué duración, duración mínima, condiciones de resolución y depósitos tiene? | Por fijar ([OQ-45](../../30-governance/open-questions.md)) | 97.1.p, q, r |

Disparadores: `gen.cantidad-limitada`, si la cantidad es limitada; `gen.variantes`, si hay variantes; `gen.unidad-no-nueva`, si la unidad no es nueva; `gen.descuento`, si hay descuento; `gen.precio-personalizado`, si el precio está personalizado; `gen.elementos-digitales`, si el bien tiene elementos digitales; `gen.suscripcion`, si es una suscripción o hay depósito. Quedan fuera de la capa las letras g, i, o y u (coste del medio de comunicación, lengua, códigos de conducta, resolución extrajudicial). Toda la capa general está en todo modelo. El bloque universal lleva además un requisito condicionado a un hecho del producto, la persona responsable en la UE si el fabricante no está establecido en ella, que evalúa la auditoría y no distingue el modelo ([D-052](../../30-governance/decisions.md#d-052)). Los disparadores de los condicionados son hechos de la oferta, cuya lista de condiciones que se dan es la aplicación, salvo `gen.elementos-digitales`, que es del producto y distingue el modelo; en la oferta que no cumple el disparador, sus requisitos quedan en gris, como NA justificado ([D-047](../../30-governance/decisions.md#d-047)).

- **Medios de pago:** entran porque es información previa a la compra, aunque la transacción quede fuera del alcance (97.1.h).
- La letra l (gastos de un servicio iniciado antes de desistir) no se recoge: está pendiente en [OQ-45](../../30-governance/open-questions.md).
- **Otras fuentes de apoyo posibles** (no definen el requisito): grupo de oferta de los PTD de Amazon y propiedades de oferta de Schema.org.
- **Valores de oferta.** Outlet, liquidación, exposición o reacondicionado son valores que activan o condicionan estas cuestiones; no forman bloque ([D-037](../../30-governance/decisions.md#d-037)). Si traen cuestiones que la capa general y la base de la clase no prevén (ejemplo hipotético: salud de la batería en un móvil reacondicionado), esas cuestiones son requisitos condicionados del bloque de la clase, aplicables si se da el hecho de la capa general que declara ese valor (si la unidad no es nueva): la oferta no aporta requisitos. Un valor sin disparador en la capa general (fin de serie, que puede ser nuevo) es un hueco del marco ([D-048](../../30-governance/decisions.md#d-048)).

## Formato del catálogo

El catálogo se guardará como datos en `demand-engine/catalog/`. Los identificadores son **propios**: no dependen de las referencias, para que un cambio de versión de Shopify, Amazon o Google no los altere ([D-038](../../30-governance/decisions.md#d-038)). La trazabilidad con las referencias va en un campo aparte.

| Elemento | Identificador | Ejemplos |
|---|---|---|
| Bloque general universal | `gen` | `gen` |
| Bloque general condicionado | `gen.<hecho>` | `gen.descuento`, `gen.unidad-no-nueva` |
| Bloque de categoría (sector o categoría, según su posición) | `cat.<nombre>` | `cat.ropa-de-cama`, `cat.mantas-decorativas`, `cat.toppers-de-colchon` |
| Bloque de especialización | `esp.<nombre>` | `esp.juego`, `esp.tejido-polar` |
| Requisito | `<bloque>/<nn>` | `gen/04`, `esp.juego/02` |

- `<nombre>` es un nombre propio en español, en minúsculas y con guiones, único en el catálogo y estable. No se deriva automáticamente de las etiquetas de las referencias; los homónimos se distinguen (las dos «Cubrecolchones» de Shopify son `cat.cubrecolchones` y `cat.toppers-de-colchon`).
- Un bloque de categoría contiene los atributos **propios** de su categoría que no lista ninguna de sus madres: un atributo repetido en varios niveles va al bloque de la categoría más general que lo lista ([D-040](../../30-governance/decisions.md#d-040)). Contiene también las propiedades del PTD de Amazon relevantes para la clase, con origen «referencias» y fuente `amazon-ptd-prop:…` ([D-039](../../30-governance/decisions.md#d-039)). Qué propiedades entran en el bloque lo deciden las reglas inducidas en el entrenamiento ([D-044](../../30-governance/decisions.md#d-044)); en la primera versión aún no se inducen y lo decide la redacción automática del bloque ([D-045](../../30-governance/decisions.md#d-045), [OQ-49](../../30-governance/open-questions.md)). Su exclusión en una clase concreta la decide el filtro de relevancia ([D-050](../../30-governance/decisions.md#d-050)). Las propiedades de un PTD van al bloque de la categoría que la tabla `catalog/amazon-map.json` asocia a ese PTD (una por categoría; si varias de la cadena comparten PTD, la más general); una propiedad que solo se aplica a una categoría hija va al bloque de la hija; y una propiedad que repite una dimensión ya cubierta por un atributo de Shopify no se duplica ([D-040](../../30-governance/decisions.md#d-040)).
- **Catálogo de bloques de categoría:** se genera con la herramienta del motor y se compila en el entrenamiento con las reglas inducidas, sin revisión manual ([D-044](../../30-governance/decisions.md#d-044)); hasta entonces, el bloque está en estado «no compilado» ([D-045](../../30-governance/decisions.md#d-045)). En ejecución, el clasificador elige bloques del catálogo y solo redacta las cuestiones inferidas y las especializaciones nuevas; si la categoría no está en el catálogo, el motor genera el bloque y lo compila al vuelo con el índice de rasgos y las reglas vigentes (si su rama no tiene regla, la importancia es el voto del agente, provisional), lo usa en estado «no compilado» y lo encola para el entrenamiento ([D-041](../../30-governance/decisions.md#d-041), [D-044](../../30-governance/decisions.md#d-044)).
- **Campos de un bloque:** identificador, tipo, nombre, disparador (si es condicionado o especialización), versión, estado («no compilado» o «compilado», [D-045](../../30-governance/decisions.md#d-045); la capa general no tiene estado de compilación, porque es parte del marco), referencias y requisitos. En la clave del modelo, cada bloque se escribe `<bloque>@<versión>`.
- **Referencias del bloque:** lista de `<fuente>:<identificador>@<versión>`, por ejemplo `shopify:hg-15-1-4-2@v2026-08`, `google:1985@2021-09-21`, `amazon-ptd:BLANKET@2026-10-24`, `amazon-btg:3250001031@2026-10-24`, `ley:TRLGDCU-97.1.e@2026-02-28`. Si cambia una referencia, se actualiza este campo y el identificador se mantiene.
- **Campos de un requisito:** identificador, pregunta, dimensión, entidad (producto, variante, oferta, entrega, condiciones o vendedor), importancia por defecto, origen (referencias, inferida o normativa), fundamento, fuentes (con el mismo formato, a nivel de atributo cuando proceda: `shopify-attr:fabric`, `amazon-ptd-prop:BLANKET.special_feature`), aplicabilidad, rasgo (qué resuelve la cuestión, de la lista cerrada de [model-training](../../10-model/model-training.md#rasgos), [D-045](../../30-governance/decisions.md#d-045)) y regla (la regla inducida que decidió su inclusión y su importancia: «cada requisito guarda la regla que lo decidió», [D-044](../../30-governance/decisions.md#d-044)).
- **Relevancia:** un requisito del catálogo puede quedar excluido del modelo de una clase por una regla de relevancia inducida en el entrenamiento (`rel:<requisito>@<clase>`); el modelo lo lista aparte con su regla y no se audita ([D-050](../../30-governance/decisions.md#d-050)).
- Las cuestiones inferidas aceptadas van en el bloque de su categoría, con origen «inferida» en cada requisito; antes de aceptarse son un añadido provisional del modelo ([D-041](../../30-governance/decisions.md#d-041)).

## Criterios de redacción del catálogo

Criterios aprobados por el usuario para los bloques de categoría ([D-043](../../30-governance/decisions.md#d-043)). Con [D-044](../../30-governance/decisions.md#d-044) el catálogo ya no se redacta a mano, sino que se compila; estos criterios forman parte del marco dentro del que operan las reglas inducidas:

> 1. **Cuándo es crítica una medida.** Es crítica cuando la medida o la talla fija qué se vende: sin ella no se sabe qué variante es. Es principal cuando solo describe el producto.
> 2. **Atributos con muchos valores distintos.** […] Se dividen por tema en varias cuestiones, citando los valores que cubre cada una.
> 3. **Solapes con la capa general y con el juego.** Un bloque de categoría solo repite una cuestión general si la concreta con algo propio de la clase.
>    - La cantidad neta del pienso se queda.
>    - Las piezas incluidas pasan a esp.juego.
> 4. **La misma propiedad de Amazon en varias categorías hermanas.** […] Se sube a la categoría madre común solo si vale para todas sus hijas; si no, se queda repetida.
> 5. **Cuestiones inferidas que propusieron los agentes.** Se incluyen como provisionales, y en la revisión el usuario las aprueba una a una.
>
> — INTAKE 2026-10-25-catalog-criteria

Criterio 1: se aplica a dimensiones y tallas; el peso, el grosor y el gramaje son magnitud física, sin regla fija ([D-051](../../30-governance/decisions.md#d-051)). Criterio 5: la aprobación una a una la sustituye la validación automática del entrenamiento ([D-044](../../30-governance/decisions.md#d-044)).

- **Composición textil:** tiene apoyo normativo en el artículo 16.1 del Reglamento (UE) 1007/2011, según el cual la composición en fibras «será claramente visible para el consumidor antes de la adquisición, incluso en los casos en que esta se realice por medios electrónicos». Origen «normativa», fuente `ley:UE-1007/2011-16.1@2011-10-18`; la importancia sigue siendo principal.
- **Propiedades de Amazon fuera del grupo de detalles del producto:** el generador lee también las propiedades descriptivas del grupo de cumplimiento (`compliance_*` y `fabric_weight`, donde está el gramaje), y no las de baterías, materiales peligrosos u obligaciones del vendedor.
- **Color:** entidad «producto»; si es seleccionable, lo cubre además `gen.variantes`.

## Denominación

La sintaxis (clave y nombre) está en el [canon](../../10-model/demand-model.md#composición-e-identidad-del-modelo). Ejemplos: «Sofás · tapicería de piel» (su oferta del caso: unidad no nueva, con descuento, cantidad limitada); «Sofás cama (Sofás de dos plazas)»; «Sábanas planas + Sábanas ajustables + Fundas de almohada · juego, uso invernal, tejido polar» (oferta: con variantes); «Cojines · material reciclado» (oferta estándar); «Botas · uso de equitación» (oferta: con variantes); «Televisores · con elementos digitales» (hipotético: el bloque general del producto se nombra tras las especializaciones). La aplicación es de la oferta y no entra en el nombre; una oferta sin condiciones declaradas es estándar ([D-047](../../30-governance/decisions.md#d-047)).

## Cuestiones inferidas

Cuestiones de toda la clase que ninguna referencia recoge (p. ej., el mecanismo de apertura de un sofá cama). Las propone el clasificador y, en ejecución, entran como añadido provisional del modelo, fuera de la clave; cuando el entrenamiento las acepta ([D-044](../../30-governance/decisions.md#d-044)), pasan al bloque de su categoría como nueva versión ([D-041](../../30-governance/decisions.md#d-041)) ([canon](../../10-model/demand-model.md#sistema-de-construcción-vigente), [D-036](../../30-governance/decisions.md#d-036)). Controles:

1. Solo cuestiones de toda la clase, neutrales, justificadas y que no dupliquen la base. Pueden estar condicionadas por un hecho de la oferta (p. ej., «si la unidad no es nueva»): así se descubren las cuestiones que solo trae una condición de la oferta ([D-048](../../30-governance/decisions.md#d-048)).
2. Origen marcado: «referencias» o «inferida».
3. El entrenamiento las valida contra el marco, sin revisión manual; el MPIR las confirma o revisa cuando exista ([D-041](../../30-governance/decisions.md#d-041), [D-044](../../30-governance/decisions.md#d-044); estados: [D-045](../../30-governance/decisions.md#d-045)). En la primera versión del entrenamiento siguen siempre provisionales.
4. La auditoría puede informar con ellas y sin ellas.
5. Estabilidad medida con dos ejecuciones por caso.

Una característica declarada que revela una dimensión de toda la clase no forma bloque: si alguna referencia (incluidos los PTD de Amazon) recoge la dimensión, su cuestión entra en el bloque de su categoría con origen «referencias», para todos los productos de la clase; si no, es inferida: en ejecución se usa como añadido provisional fuera de la clave y entra en el bloque al aceptarse ([D-041](../../30-governance/decisions.md#d-041)). El valor declarado es la respuesta ([study-class](../../10-model/study-class.md#regla-metodológica), [D-039](../../30-governance/decisions.md#d-039)). Por ejemplo, el acabado del algodón (mercerizado) está en el PTD `BED_LINEN_SET` (`finish_type`); la preparación (peinado) no está en ninguna referencia y es inferida.

## Relacionado

- [demand-model](../../10-model/demand-model.md) — composición por bloques, capa general e importancia (canon)
- [study-class](../../10-model/study-class.md) — clase de estudio (canon)
- [cases](cases.md) — casos de evaluación
