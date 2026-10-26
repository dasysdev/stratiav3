# Color y excepciones de importancia por requisito y clase

*Update decidido en la conversación del 2026-10-26, tras la revisión del ciclo de entrenamiento de reglas 4 (T-028). Se transcribe para su trazabilidad; las palabras del usuario, con las erratas corregidas, y el texto de las opciones que eligió.*

## Planteamiento del usuario

«Duda sobre el color en el rasgo de estética. No sé si con estos cambios ya quedaría resuelto. En los casos de control veo que el color se está estableciendo como complementario, pero esto no tiene sentido. En muchos casos el color es principal o incluso crítico, por ejemplo en zapatillas o sofás. No puedes compararlo si no sabes el color.»

## Datos que aportó Claude

- Votos al color con las reglas 4: en calzado (botas, pantuflas, zapatillas infantiles), principal 10 de 10; en sofás y sofás cama, principal 4 de 4; en cojines, principal 2 de 2. Las reglas lo resuelven como complementario en todas esas clases.
- Causa: la regla de importancia es por rasgo y clase, y el color comparte «estética» con el estampado, el estilo, el acabado o las patas, que los agentes votan complementarios; esa mayoría arrastra al color.
- El mismo fallo aparece en el abrigo de las pantuflas y en el mecanismo de apertura del sofá cama (principal 4 de 4 en los votos; complementario por la regla). En el piloto, 97 de 375 combinaciones de requisito y clase tienen una mayoría clara de votos contra el nivel que aplica la regla.
- Ningún agente ha votado el color crítico. Cuando el color es lo que se elige entre variantes, la capa general ya lo pregunta como crítico (`gen.variantes/01`, «¿Qué variantes hay y en qué se diferencian?»).

## Decisiones

1. **Opción elegida (A):** «Excepción por requisito: la regla por rasgo es la general; si los votos de un requisito en una clase la contradicen, ese requisito tiene su propia regla (mayoría; empate, se queda lo que había). D-055 pasa a ser un caso de esto.»
2. **¿Puede el color llegar a crítico? Opción elegida:** «Sí, si sus votos lo dicen: el color se excepciona de la prohibición de la estética: puede ser crítico por requisito y clase si los votos lo hacen crítico.»
3. **Precisión del usuario,** a continuación: «Esto no solo es para el color, es para cualquier propiedad.»
