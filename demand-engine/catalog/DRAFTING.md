# Redacción de bloques de categoría

Instrucciones para redactar un bloque `cat.` a partir del plan de `bin/blocks plan` (en ejecución, cuando falta en el catálogo; el bloque queda «no compilado» hasta que lo compila el entrenamiento). Reglas de fondo: D-033 a D-045 (`docs/10-model/demand-model.md`, `docs/10-model/model-training.md`, `docs/20-methods/product-taxonomy/requirement-blocks.md`).

1. **Un fichero por bloque**, que se registra con `bin/model register FICHERO` (lo guarda en `catalog/runtime/<nombre>.json`). `<nombre>`: nombre propio en español, minúsculas y guiones, único y estable; no copies una etiqueta ambigua (los homónimos se distinguen).
2. **Requisitos de Shopify:** un requisito por atributo del bloque, como cuestión concreta, neutral y evaluable. Une en uno los atributos casi idénticos (con todas sus fuentes). Excluye solo lo que claramente no informa sobre la clase, con motivo.
3. **Requisitos de Amazon:** de los candidatos, solo los relevantes para evaluar ofertas de la clase. Excluye logística, datos de plataforma o de feed, identificadores, y dimensiones que ya cubre un atributo de Shopify de la cadena. Agrupa los valores de `special_feature` por tema en pocas cuestiones (cada una con los valores que cubre en `sources`). Origen «referencias».
4. **Ubicación:** si un candidato solo se aplica a una categoría hija del plan (p. ej., algo que solo tiene sentido en una subcategoría), ponlo en el bloque de esa hija y justifícalo en `rationale`.
5. **Rasgo y voto:** cada requisito lleva `trait` (qué resuelve la cuestión, del vocabulario de `catalog/traits.json`) y `vote`, la importancia que darías: crítico si sin resolverla la oferta deja de ser evaluable; principal si es criterio para comparar y elegir ofertas de la clase; complementario si es relevante sin ser central. Los críticos son raros fuera de la capa general. La duda no baja la importancia. La importancia la ponen las reglas compiladas; el voto solo cuenta donde no hay regla.
6. **No dupliques la capa general** (`catalog/gen.json`): precio, disponibilidad, marca, envío, devoluciones, garantía, estado, variantes…
7. **Bloques vacíos:** si un bloque no tiene atributos ni candidatos relevantes, no crees fichero: regístralo con `bin/model register --empty CAT_ID`.

Formato:

```json
{
  "id": "cat.<nombre>", "type": "categoría", "name": "…", "shopify": "<id>", "parent": "cat.<nombre de la madre> o null",
  "refs": ["shopify:…", "google:…", "amazon-ptd:…", "amazon-btg:…"],
  "requirements": [{"id": "cat.<nombre>/01", "question": "…", "dimension": "…", "entity": "producto|variante|oferta|entrega|condiciones|vendedor",
                    "trait": "…", "vote": "crítico|principal|complementario", "origin": "referencias", "sources": ["shopify-attr:…"],
                    "applicability": "universal o condición", "rationale": "…"}],
  "excluded": [{"source": "…", "reason": "…"}]
}
```

## Criterios transversales (D-043; forman parte del marco)

1. **Medidas.** Crítica si la medida o talla fija qué se vende (identifica la variante ofrecida: talla de calzado, medida de cama, colchón o almohada, medidas de la toalla); principal si solo describe el producto (medidas de un sofá, de un cojín, de la cama abierta).
2. **Atributos con muchos valores de temas distintos:** se dividen por tema en varias cuestiones, citando los valores que cubre cada una (`shopify-attr:<handle>=<valor>`, `amazon-ptd-prop:<TIPO>.<propiedad>=<valor>`).
3. **Solapes:** un bloque de categoría solo repite una cuestión de la capa general si la concreta con algo propio de la clase (la cantidad neta del pienso se queda). Las piezas incluidas no van en los bloques de categoría: las cubre la especialización `esp.juego`. Las extensiones de un atributo que ya está en la cadena (color de la funda frente a color) no se duplican.
4. **La misma propiedad de Amazon en categorías hermanas:** sube al bloque de la madre común solo si vale para todas sus hijas; si no, se queda repetida.
5. **Cuestiones de toda la clase que no recoge ninguna referencia:** se añaden como inferidas (origen «inferida», fuentes vacías, provisionales). Si una referencia sí la recoge, origen «referencias».
6. **Composición textil:** la composición en fibras de un producto textil tiene apoyo normativo (Reglamento (UE) 1007/2011, art. 16.1: visible antes de la adquisición, también por medios electrónicos): origen «normativa», fuente `ley:UE-1007/2011-16.1@2011-10-18`, importancia principal.
7. **El color** es una característica del producto (entidad «producto»); si es seleccionable, lo cubre además `gen.variantes`.
