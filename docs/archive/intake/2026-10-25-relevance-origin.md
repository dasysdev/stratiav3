# Filtro de relevancia, magnitudes físicas y fabricante y origen en la capa general

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad (tras la tarea T-019). Lo forman tres mensajes del usuario y las propuestas de Claude que aprueban. La ortografía de los mensajes del usuario está normalizada.*

## 1. Requisitos no relevantes

Usuario: «Las votaciones parecen ok. Con el entrenamiento se perfeccionarán. Una cosa que me gustaría resolver. También hay opción de que un requisito no sea suficientemente relevante ni siquiera como complementario. Nuestro modelo solo debe incluir cuestiones relevantes, las complementarias siendo las de menor relevancia.»

Propuesta de Claude (resumen):

- Evidencia: en el modelo del pienso salen «¿De qué color o colores es?», «¿Qué estampado o motivo tiene, o es liso?» y «¿De qué material está hecho?», heredadas de los bloques de sector de Productos para mascotas y Productos para perros; los agentes las votaron «complementario» porque no tenían otra opción.
- Tres cosas distintas: **no relevante para la clase** (color de un pienso: no debe estar en el modelo); **no aplica al producto** (número de hilos en unas sábanas de coralina, que no son tejido de calada: requisito condicionado al producto, en gris); **no aplica a la oferta** (precio de referencia sin descuento: en gris, D-047). Casi toda la irrelevancia sale de los bloques de sector: un atributo de la categoría madre llega a todas sus hijas.
- **Opción A, filtro de relevancia aprendido:**
  1. No es un cuarto nivel de importancia: la escala sigue siendo crítico, principal y complementario. Antes de la importancia, cada requisito pasa una prueba: «¿informa sobre algo que importa para evaluar o comparar ofertas de esta clase?» (la condición 3 del criterio de especialización). Si no la pasa, sale del modelo de esa clase.
  2. Lo decide el entrenamiento con el mismo mecanismo que la importancia: los agentes votan con un cuarto valor posible, «no relevante»; el entrenamiento induce reglas de relevancia por el árbol (viven en la clase, suben a la madre si valen para todas sus hijas), por requisito y clase, no por rasgo.
  3. Sin regla compilada, la duda no excluye: el requisito se queda como complementario, marcado como provisional y encolado.
  4. Límites del marco: nunca se excluyen la capa general, los requisitos normativos ni la medida que fija lo vendido.
  5. Trazabilidad: lo excluido no desaparece; el modelo lo lista aparte con la regla que lo excluyó. No es NA: no forma parte de lo que se audita.
- B (solo en la redacción del bloque) y C (que la auditoría lo resuelva con NA) se descartan.

Usuario: «¿Cómo sería el filtro aprendido?»

Explicación de Claude (resumen):

1. El voto: crítico, principal, complementario o no relevante.
2. Los datos de partida: lo que dice el catálogo (si un requisito está en un bloque, la redacción lo consideró relevante en su categoría) y los votos, registrados en la clase del producto.
3. La regla: por requisito y clase (p. ej., `rel:cat.productos-para-mascotas/02@ap-2-3-3 → excluido`). Sube a la madre solo si todas sus hijas con datos coinciden; cuando haya collares o juguetes donde el color importa, no subirá. En empate, se queda: la duda no excluye.
4. La validación automática añade dos cosas: la coherencia de relevancia (cuántos requisitos siguen en el modelo con mayoría de votos «no relevante» en su clase: debe bajar) y la salvaguarda de cobertura (si las fichas de una clase declaran un hecho que solo responde el requisito excluido, la cobertura empeora y la regla se descarta: lo que las fichas cuentan no se puede declarar irrelevante).
5. En la ejecución, lo excluido se lista aparte («Excluidos en esta clase (no se auditan)») con su regla; un collar del mismo sector conserva el color; sin regla todavía, el requisito sigue como complementario, marcado «relevancia dudosa», y se encola.
6. En el informe, cada regla con su requisito, clase, votos y cuántos requisitos decide.

| | Importancia | Relevancia |
|---|---|---|
| Qué decide | Crítico, principal o complementario | Si está o no en el modelo de la clase |
| Clave de la regla | Rasgo × clase | Requisito × clase |
| Sin regla | Voto provisional | Se queda (la duda no excluye) |
| Salvaguarda | Marco (D-043, capa general) | Marco más la cobertura de hechos declarados |

## 2. Medidas

Propuesta de Claude, opción A: el peso, el grosor y el gramaje salen de «medida descriptiva» y pasan a un rasgo propio, «magnitud física», sin regla fija: los decide el árbol por clase. D-043, criterio 1, queda igual para las dimensiones («la medida o la talla»; sus ejemplos son dimensiones y tallas). Las dimensiones de detalle (altura de tacón, medidas de uso del sofá, largo reclinado) se dejan para cuando el entrenamiento a escala dé datos de muchas clases.

## 3. País de fabricación y GPSR

Propuestas de Claude pendientes:

- País de fabricación: casi el único hecho declarado sin pregunta en el modelo; los agentes lo pusieron como inferida en tres bloques distintos. Pregunta universal en la capa general: «¿Dónde se ha fabricado (país de fabricación)?», complementaria.
- Reglamento (UE) 2023/988 (seguridad general de los productos), art. 19, para la capa general: apoyo normativo para marca, modelo e identificadores; fabricante y contacto (complementaria); persona responsable en la UE (condicionada, complementaria); advertencias e información de seguridad (principal).

## 4. Respuesta del usuario

«OK. Y para las demás preguntas pendientes:
2. Confirmo.
3. Según su origen. Si es claramente por normativa, lo ponemos en normativa.»
