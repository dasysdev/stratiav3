# Criterios transversales del catálogo de bloques de categoría

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad (tarea T-016). Tres agentes redactaron por separado un borrador de 27 bloques, con criterios distintos. Claude propuso unos criterios comunes y el usuario los aprobó («si»).*

## Criterios aprobados

1. **Cuándo es crítica una medida.** Es crítica cuando la medida o la talla fija qué se vende: sin ella no se sabe qué variante es. Es principal cuando solo describe el producto.
   - Ejemplos del borrador: la talla de calzado y las medidas de cama y de toalla, frente a las medidas del sofá y del cojín.
2. **Atributos con muchos valores distintos.** Algunos atributos mezclan temas, como las características del zapato, del sofá o del protector. Se dividen por tema en varias cuestiones, citando los valores que cubre cada una.
3. **Solapes con la capa general y con el juego.** Un bloque de categoría solo repite una cuestión general si la concreta con algo propio de la clase.
   - La cantidad neta del pienso se queda.
   - Las piezas incluidas pasan a esp.juego.
4. **La misma propiedad de Amazon en varias categorías hermanas.** Por ejemplo, el número de hilos aparece en 4 bloques de ropa de cama. Se sube a la categoría madre común solo si vale para todas sus hijas; si no, se queda repetida. El número de hilos no vale para mantas, así que se queda repetido.
5. **Cuestiones inferidas que propusieron los agentes.** Se incluyen como provisionales, y en la revisión el usuario las aprueba una a una:
   - el mecanismo de apertura y el uso diario u ocasional, en sofás cama;
   - el ligamento, en sábanas y fundas de almohada;
   - el alimento completo o complementario y su composición analítica, en el pienso;
   - la seguridad del juguete;
   - si la talla del calzado viene grande o pequeña.

## Tareas sin decisión anunciadas por Claude, ya hechas

- **Normativa europea de etiquetado textil.** El artículo 16.1 del Reglamento (UE) 1007/2011 (DOUE L 272 de 18.10.2011) dice literalmente: «Cuando se comercialice un producto textil, las descripciones de la composición en fibras textiles contempladas en los artículos 5, 7, 8 y 9 se indicarán en los catálogos y la documentación comercial, en los embalajes, etiquetas y marcados de manera que sean legibles y visibles con facilidad, claras y con caracteres tipográficos uniformes en cuanto a su tamaño, estilo y fuente. Esta información será claramente visible para el consumidor antes de la adquisición, incluso en los casos en que esta se realice por medios electrónicos».
  - Consecuencia: la composición textil pasa a origen «normativa».
  - La importancia sigue siendo principal: la obligación legal no la hace crítica.
- **Generador.** Lee también el grupo de cumplimiento de Amazon donde está el gramaje: las propiedades descriptivas compliance_* y fabric_weight. No lee las de baterías, materiales peligrosos u obligaciones del vendedor.
- **Entidad del color.** Se unifica como «producto». Si el color es seleccionable, lo cubre además gen.variantes.
