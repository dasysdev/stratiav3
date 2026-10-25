# Entrenamiento y ejecución

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad (tarea T-016).*

## Planteamiento del usuario

Palabras del usuario: «la revisión humana solo debe ser en tiempo de entrenamiento, en tiempo de ejecución debe ser automático. ¿Esto está planteado así?».

Claude respondió que lo era en la intención, pero no estaba escrito, y que en dos puntos el canon podía leerse como bloqueante:

1. **Una categoría que aún no está en el catálogo.** D-040 dice que los bloques se revisan «una vez por categoría», pero no qué pasa en ejecución con una categoría no revisada.
2. **Las cuestiones inferidas.** En D-036, «el usuario valida siempre las críticas» puede leerse como bloqueante.

## Propuesta de Claude, aceptada por el usuario («si»)

Principio en dos modos:

- **Entrenamiento, con revisión humana.** El usuario revisa los bloques nuevos del catálogo, las cuestiones inferidas, las especializaciones y las importancias, y calibra con el conjunto de casos. Lo que aprueba pasa a estado «validado».
- **Ejecución, totalmente automática y sin esperar nunca a una persona.**
  - Si la categoría está en el catálogo, se usan sus bloques.
  - Si no, el motor genera el bloque solo, con el generador y la redacción automática, lo usa marcado «no revisado» y lo deja en cola para la siguiente revisión de entrenamiento.
  - Las inferidas y las especializaciones nuevas funcionan igual: se usan como provisionales y se encolan.
- **Trazabilidad.** Cada resultado indica qué partes del modelo usó sin revisar, para que la auditoría pueda informar con ellas y sin ellas, como ya prevé D-036.

Implica una decisión de canon que matiza D-022, D-036 y D-040. En el motor, implica convertir la redacción de bloques en un paso automático, con caché y cola de revisión.

## Propuesta de I-16, aceptada con el mismo «si»

Sobre las cuestiones inferidas dentro de un bloque de categoría de contenido fijo: «una cuestión inferida se usa en la ejecución como añadido provisional del modelo, marcado como tal y fuera de la clave; cuando se acepta en la revisión, se incorpora al bloque del catálogo como nueva versión. Se resolvería con la separación entre entrenamiento y ejecución planteada al usuario».

Resuelve I-16.
