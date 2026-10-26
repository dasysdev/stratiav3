# Selección del catálogo de entrenamiento

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad (tareas T-020 y T-024).*

## Planteamiento del usuario

Palabras del usuario: «quiero preparar un entrenamiento a escala. utiliza https://www.elcorteingles.es/sgfm/statics-front/front-msh3-eci-es/contents/sitemap-variants/sitemap.xml.gz. crea una lista representativa de productos para entrenamiento. utiliza un grupo pequeño de productos de cada categoría, pero quiero suficiente variedad de categorías para que sea de utilidad para el entrenamiento. usa el sistema de captura para evitar bloqueos».

Claude entendió «evitar bloqueos» como no provocarlos (ritmo de lector, legitimidad), no como eludirlos, y propuso 3 fichas por categoría con un objetivo de 300–500 fichas.

## Respuestas del usuario

- Tamaño y profundidad: «sí a 3 fichas»; 300 fichas en una misma jornada de captura («¿puedes apretar a 300 fichas para una misma sesión?»).
- Organización: «el objetivo es el entrenamiento completo. dividido en subtareas. se irán ejecutando una detrás de otra».
- Ritmo: de tres opciones (A, la del motor: unos 67 s por ficha; B, moderada: pausa de 10–30 s y pausa larga de 1–3 min cada 20–30 fichas; C, agresiva), el usuario eligió la B: «ves que B».
- Captura: «pero no apliques la técnica del scroll. entra y descarga el html de primera carga. es suficiente para lo que necesitamos».
- Piloto: «empecemos con 30 para validar el sistema de entrenamiento».

## Criterio aplicado por Claude (pendiente de que el usuario lo revise)

- «Categoría» se toma como tipo de producto conocido antes de capturar: la primera palabra del nombre del producto en la URL, en singular y sin palabras vacías, dentro de cada departamento de la tienda; solo tipos con una categoría de la tienda que los nombre. La clase es la que da el clasificador.
- Una ficha por producto (las variantes cuentan una vez); fuera los departamentos que no venden productos (entradas, tarifa plana, tarjetas y cajas regalo).
- Sorteo determinista con semilla fija, por rondas de departamentos, sin repetir tipo; 3 fichas y 2 reservas por tipo; 100 tipos; piloto = los 10 primeros tipos, de departamentos distintos.
- Resultado: `demand-engine/training/selection/eci-2026-10-25.json`, 100 tipos de 26 departamentos, 300 fichas y 200 reservas; criterio en `demand-engine/training/selection/README.md`.
