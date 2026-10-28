# Redacción de bloques de categoría

Instrucciones para redactar un bloque `cat.` a partir del plan de `bin/blocks plan` (en ejecución, cuando falta en el catálogo; el bloque queda «no compilado» hasta que lo compila el entrenamiento). Reglas de fondo: D-033 a D-064 (`docs/10-model/demand-model.md`, `docs/10-model/model-training.md`, `docs/10-model/resolving-information.md`, `docs/20-methods/product-taxonomy/requirement-blocks.md`).

1. **Un fichero por bloque**, que se registra con `bin/model register FICHERO` (lo guarda en `catalog/runtime/<nombre>.json`). `<nombre>`: nombre propio en español, minúsculas y guiones, único y estable; no copies una etiqueta ambigua (los homónimos se distinguen).
2. **Requisitos de Shopify:** un requisito por atributo del bloque, como cuestión concreta, neutral y evaluable. Une en uno los atributos casi idénticos (con todas sus fuentes). Excluye solo lo que claramente no informa sobre la clase, con motivo.
3. **Requisitos de Amazon:** de los candidatos, solo los relevantes para evaluar ofertas de la clase. Excluye logística, datos de plataforma o de feed, identificadores, y dimensiones que ya cubre un atributo de Shopify de la cadena. Agrupa los valores de `special_feature` por tema en pocas cuestiones (cada una con los valores que cubre en `sources`). Origen «referencias».
4. **Ubicación:** si un candidato solo se aplica a una categoría hija del plan (p. ej., algo que solo tiene sentido en una subcategoría), ponlo en el bloque de esa hija y justifícalo en `rationale`.
5. **Rasgo y voto:** cada requisito lleva `trait` (qué resuelve la cuestión) y `vote`, la importancia que darías: crítico si sin resolverla la oferta deja de ser evaluable (la misma prueba para cualquier requisito); principal si es criterio para comparar y elegir ofertas de la clase; complementario si es relevante sin ser central. La duda no baja la importancia. La importancia la ponen las reglas compiladas; el voto solo cuenta donde no hay regla. El vocabulario de rasgos es abierto (`catalog/traits.json`; D-056): si ninguno encaja, propón uno en `proposed_traits`, con nombre y una frase de definición, y úsalo en `trait`.
6. **No dupliques la capa general** (`catalog/gen.json`): precio, disponibilidad, marca, envío, devoluciones, garantía, estado, variantes…
7. **Bloques vacíos:** si un bloque no tiene atributos ni candidatos relevantes, no crees fichero: regístralo con `bin/model register --empty CAT_ID`.
8. **Formulación de las cuestiones** (D-060; forman parte del marco):
   1. Ninguna condición sobre la existencia de la información («si se indica», «si procede»): un componente forma parte de la necesidad o no. Si la condición corresponde a un hecho del producto o de la oferta, nombra ese hecho y aplica la regla 2.
   2. Una condición sobre un hecho que afecta solo a una parte de la cuestión se convierte en un requisito condicionado propio, con la condición en `applicability` (como `cat.sofas/17`, «si es reclinable»). La pregunta de sí o no seguida del detalle del mismo hecho se mantiene: un «no» fundamentado lo resuelve todo. Solo si el detalle toma el mismo rasgo y la misma importancia que la pregunta; si no, la regla 3 prevalece y el detalle pasa a requisitos condicionados al hecho («¿Incluye colchón?» y, si lo incluye, «¿De qué medida es?» y «¿Se puede retirar?»; D-087).
   3. Una necesidad por requisito: divide la cuestión cuando sus partes se responden por separado, cada una sirve por sí sola para comparar y tomarían otro rasgo u otra importancia (tipo de sofá y número de módulos; material del armazón y uniones). Mantén junto lo que solo tiene sentido unido (plazo y condiciones; nombre y dirección), y no dividas por esta regla lo que comparte rasgo e importancia.
   4. Cada componente de la cuestión tiene fuente en `sources` (un atributo, una propiedad o un valor, o la norma si el origen es «normativa»). Un componente sin fuente sale de la cuestión y se propone como cuestión inferida (por ejemplo, el material y el grosor del colchón de un sofá cama, que `SOFA.mattress` no recoge).
9. **Información resolutiva** (D-062 a D-064): cada requisito lleva en `resolving_info` sus **aportaciones resolutivas**, las clases de información que pueden contribuir a resolverlo, cada una con el componente de la pregunta al que aporta:
   - Las de origen «referencias» salen de sus fuentes: `bin/train resolving refs FUENTE…` muestra el título, la descripción, las partes y los valores de cada atributo o propiedad (por ejemplo, `SOFA.sleeping_area_dimensions` trae largo, ancho y altura desde el suelo del área para dormir). Indica en `support` la fuente.
   - Las de origen «inferida» resuelven aunque ninguna referencia las recoja (un certificado o un informe de ensayo); son provisionales.
   - Una norma que es fuente del requisito (`ley:…`, origen «normativa») da aportaciones de origen «referencias» con la ley en `support`: solo lo que esa norma exige (D-068).
   - Una cita de una norma nombra su código, el artículo y el apartado o la letra, y la versión fijada en references (`ley:TRLGDCU-97.1.e@2026-02-28`; códigos y versiones en `references/bin/refs status`). `references/bin/refs law CITA` muestra el pasaje citado: lo que no está en él no se apoya en la norma.
   - Una aportación es una clase de información («plazo para desistir o devolver»), no un valor («30 días»). La lista es orientativa y no exhaustiva: no impone formato ni ubicación, ni son valores esperados. Las aportaciones que publican las fichas reales las añade el entrenamiento cuando aparecen en dos tiendas distintas.
   - Todo requisito lleva al menos una aportación; las de origen «referencias», solo con fuentes del propio requisito en `support`, y las inferidas, con `support` vacío. `bin/model check --catalog` lo comprueba en todos los bloques y en la capa general.

Formato:

```json
{
  "id": "cat.<nombre>", "type": "categoría", "name": "…", "shopify": "<id>", "parent": "cat.<nombre de la madre> o null",
  "refs": ["shopify:…", "google:…", "amazon-ptd:…", "amazon-btg:…"],
  "requirements": [{"id": "cat.<nombre>/01", "question": "…", "dimension": "…", "entity": "producto|variante|oferta|entrega|condiciones|vendedor",
                    "trait": "…", "vote": "crítico|principal|complementario", "origin": "referencias", "sources": ["shopify-attr:…"],
                    "applicability": "universal o condición", "rationale": "…",
                    "resolving_info": [{"contribution": "…", "component": "…", "origin": "referencias|inferida", "support": ["shopify-attr:…"]}]}],
  "proposed_traits": [{"name": "…", "definition": "…"}],
  "excluded": [{"source": "…", "reason": "…"}]
}
```

## Criterios transversales (D-043; forman parte del marco)

1. **Medidas.** Crítica si la medida o talla fija qué se vende (identifica la variante ofrecida: talla de calzado, medida de cama, colchón o almohada, medidas de la toalla); principal si solo describe el producto (medidas de un sofá, de un cojín, de la cama abierta).
2. **Atributos con muchos valores de temas distintos:** se dividen por tema en varias cuestiones, citando los valores que cubre cada una (`shopify-attr:<handle>=<valor>`, `amazon-ptd-prop:<TIPO>.<propiedad>=<valor>`).
3. **Solapes:** un bloque de categoría solo repite una cuestión de la capa general si la concreta con algo propio de la clase (la cantidad neta del pienso se queda). Las piezas incluidas no van en los bloques de categoría: las cubre la especialización `esp.juego`. Las extensiones de un atributo que ya está en la cadena (color de la funda frente a color) no se duplican.
4. **La misma propiedad de Amazon en categorías hermanas:** sube al bloque de la madre común solo si vale para todas sus hijas; si no, se queda repetida.
5. **Cuestiones de toda la clase que no recoge ninguna referencia:** se añaden como inferidas (origen «inferida», fuentes vacías, provisionales). Si una referencia sí la recoge, origen «referencias».
6. **Composición textil:** la composición en fibras de un producto textil tiene apoyo normativo (Reglamento (UE) 1007/2011, art. 16.1: visible antes de la adquisición, también por medios electrónicos): origen «normativa», fuente `ley:UE-1007/2011-16.1@2018-02-15`, importancia principal.
7. **El color** es una característica del producto (entidad «producto»); si es seleccionable, lo cubre además `gen.variantes`.
