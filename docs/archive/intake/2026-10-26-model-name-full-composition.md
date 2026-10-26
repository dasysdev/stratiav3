# Nombre del modelo de demanda con la composición completa

*Update descrito en la conversación del 2026-10-26 y transcrito para su trazabilidad. Lo forman dos mensajes del usuario y la respuesta de Claude entre ellos. La ortografía de los mensajes del usuario está normalizada.*

## 1. Pregunta

Usuario: «En las denominaciones del modelo de demanda no estamos incluyendo los sectores y categorías de nivel superior, ¿por qué?»

## 2. Respuesta de Claude (resumen)

- Es una regla aprobada, no un fallo del motor. La sintaxis del nombre viene de `INTAKE 2026-10-25-block-catalog` (D-038), citada en el canon: «Nombre, para personas: "Categorías (alias) · especializaciones". Los bloques universales y los de sector no se nombran». El motor la aplica tal cual: el nombre se forma con las categorías de la clase, los alias, las especializaciones y los bloques generales del producto.
- El intake no la justifica por escrito; la lógica es la redundancia. Los bloques de sector son las madres de la categoría en Shopify (D-040), así que, nombrada la categoría, el sector no distingue un modelo de otro. La identidad no se pierde porque la clave sí lleva los sectores (`gen@0.5 cat.casa-y-jardin@2 cat.ropa-de-casa@4 cat.toallas@2 esp.juego@0`).
- La lógica falla cuando el nombre de la categoría no basta para situarla. En la versión de Shopify usada (v2026-08), 311 nombres se repiten y afectan a 702 de sus 14 606 categorías; por ejemplo, «Leggings» está en ropa deportiva, en ropa de bebé y niño y en ropa de maternidad. Serían modelos distintos, con sectores y claves distintos, nombrados igual.
- Alternativas: A, dejarlo como está; B, nombrar siempre los sectores delante («Casa y jardín › Ropa de casa › Toallas · juego»); C, nombrar el sector solo cuando el nombre de la categoría se repite. Claude recomendó C.

## 3. Decisión del usuario

Usuario: «Me interesa que figure la composición completa.»
