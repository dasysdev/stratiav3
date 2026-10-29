# Perímetro de PAA: prueba de la respuesta natural y especializaciones desde PAA

Fecha: 2026-10-29. Origen: revisión del usuario en T-058 de las dos propuestas que salieron del control PAA v6 (T-053, `var/paa/control/2026-10-28T110313/`).

## Situación de partida

- Pantuflas: el agente v6 deja dentro 10 preguntas de podólogos y pies doloridos («¿Qué calzado recomiendan los podólogos?», «¿Qué zapatos debo usar para que no me duelan los pies?»…). Las lee como criterio heredado de la madre (calzado). D-146 las pone fuera («solo tiene sentido para otro producto»), pero el reglamento v6 no da una prueba operativa.
- Botas: el caso de control es una bota de polo (equitación), con un modelo hecho con el reglamento v3, sin especializaciones. Las semillas son «botas» y cuatro materiales. D-146 pone «calzado para la montaña» como ejemplo de fuera, pero el caso deja dentro «¿Cuáles son las 10 mejores marcas de botas de montaña?» y el agente lee el uso montaña como confirmación de `cat.botas/19`.

## Decisión 1 · Prueba de la respuesta natural (propuesta de Claude, aceptada)

Si la pregunta pide elegir un producto de la madre para una necesidad, va dentro solo si un producto de la clase es una respuesta natural. Lo que la clase comparte (cuidado, material, precio) sigue dentro.

Ejemplos: en pantuflas, «¿Qué calzado recomiendan los podólogos?» y «¿Qué zapatos debo usar para que no me duelan los pies?», fuera; en botas, «¿Cómo cuidar los zapatos de ante?», dentro.

## Decisión 2 · PAA puede generar especializaciones (decisión del usuario)

Pregunta de Claude, literal: «Caso real del conjunto PAA de botas. Semillas: «botas», «botas de piel/ante/goma/polipiel». Producto de control: una bota de polo (equitación). Pregunta A: «¿Cuál es el mejor calzado para andar por la montaña?». Pregunta B: «¿Cuáles son las 10 mejores marcas de botas de montaña?». Hoy lo esperado pone A fuera y B dentro. […] ¿Cuál es el objeto del conjunto PAA cuando la montaña es otra especialización?» Opciones: la clase y todas sus especializaciones (recomendada); solo la clave del caso; revisarlo fuera de T-058. El usuario respondió con texto propio.

Respuestas literales del usuario:

> Dudas. Botas de montaña es una especialización. En general el estilo o tipo suele ser especialización. En el caso de control son botas de equitación. Revisemos esto con cuidado.

> En este caso esas preguntas no irían a la especialización de botas de equitación y no irían a las de botas en general sino a una nueva especialización: botas de montaña. Es decir PAA puede generar especializaciones. Este ejemplo es la prueba.
