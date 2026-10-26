# Revisión del ciclo de entrenamiento de reglas 4

*Update decidido en la conversación del 2026-10-26, al revisar las cuestiones abiertas, las incidencias y los cambios de reglas del ciclo de reglas 4 (T-028, informe `demand-engine/training/reports/2026-10-26-v4-report.md`). Se transcribe para su trazabilidad. Las decisiones se tomaron sobre opciones que Claude planteó con datos del piloto; se reproduce el texto de la opción elegida y, cuando el usuario escribió, sus palabras, con las erratas corregidas.*

## 1. Crítico por requisito y clase

**Contexto.** Con [D-045](../30-governance/decisions.md#d-045), una regla global por rasgo decide si la identidad y el contenido son críticos. Como casi todas las cuestiones de identidad no lo son, la regla da «no crítico» en todo el catálogo, y el código convierte cualquier voto crítico de identidad o contenido en principal. Ninguna clase puede tener una identidad crítica: el artista de un CD es principal, como el género musical. Los votos ven críticas, entre otras, qué piezas incluye un juego, el formato de una grabación, el artista de un CD o LP, el tipo de joya para piercing y el tipo de sofá. Hay requisitos compartidos por varias clases: la medida en centímetros del sector Ropa de cama recibe votos «crítico» en mantas y plaids, y «principal» en sábanas, fundas y protectores.

**Opción elegida.** «Por requisito: misma prueba para todas las clases, aplicada a cada pregunta.» Claude precisó que la decisión es por requisito y clase, como la relevancia, porque hay requisitos compartidos por varias clases.

## 2. Medida descriptiva (OQ-51)

**Contexto.** El marco ([D-043](../30-governance/decisions.md#d-043), criterio 1) fija la medida descriptiva en principal. En 125 votos, 11 la ven crítica donde la medida en centímetros es la variante que se vende (manta 140×200, cojín 50×50) y 38 la ven complementaria en dimensiones de detalle (altura de tacón, largo reclinado del sofá).

Palabras del usuario, ante la opción de reetiquetar la medida que define la variante: «¿no estaría resuelto con la pregunta anterior?».

**Opción elegida.** «Sí, extender: la medida descriptiva es principal salvo que los votos de su clase la hagan crítica. Las dimensiones de detalle (tacón, largo reclinado) siguen abiertas en OQ-51 hasta T-029.»

## 3. Rasgos propuestos por los agentes (I-20)

**Contexto.** Los bloques generados en ejecución etiquetan algunos requisitos con rasgos que no encajan: el sabor de una confitura como material, la viscosidad SAE de un aceite como prestación, la especie de destino como uso, la duración de una grabación como medida descriptiva. El índice de rasgos propaga la etiqueta por fuente a todas las categorías.

Palabras del usuario: «Se deberían proponer nuevos rasgos a medida que van siendo necesarios. Se aprueban solos si los agentes los van votando. Sabor en material no tiene sentido. Quizás un rasgo de sabor es más adecuado, pero esto lo dejamos a criterio de los agentes que los van encontrando.»

Mecanismo planteado por Claude y aceptado:

1. **Proponer.** Un agente que redacta un bloque o vota un requisito puede proponer un rasgo nuevo cuando ninguno encaja, con nombre y una frase de definición. Lo encuentra el agente.
2. **Votar.** Cada agente que vota un requisito vota también su rasgo: mantiene el actual o propone otro, de la lista o nuevo.
3. **Aprobarse solo.** Opción elegida: «Cuando gana en un requisito: mayoría de votos de rasgo en el requisito (empate: se queda el actual); entra en el vocabulario en cuanto gana en alguno. Luego, la validación de siempre de las reglas.»

**Qué rasgos pueden ser críticos.** Opción elegida: «Los que dicen qué se vende: al proponer un rasgo, el agente indica si dice qué se vende; solo esos (y identidad, contenido, medidas) pueden ser críticos.»

## 4. Reglamento del clasificador (I-21, I-22)

Opciones elegidas:

- **I-21:** «La hoja más específica entra como categoría aunque herede todo; una hermana que nombra otra característica (dos plazas), como alias.»
- **I-22:** «La unidad de exposición que la ficha identifica como tal cuenta como estado declarado; "outlet" solo, no.»

## 5. Banners de toda la tienda

**Contexto.** La tienda pone en todas sus fichas los mismos mensajes («manta de regalo en pedidos de más de 99 €», «envío gratis desde 49 €»). Unos agentes los cuentan como información de la oferta (promoción, coste de envío) y otros como afirmaciones genéricas de la tienda, que no cuentan como declaradas; el mismo producto sale con hechos distintos en dos ejecuciones.

**Opción elegida.** «Sí, registrarla: solo anotarla en issues.md con el problema y una propuesta; la regla se decide más adelante.»

## 6. Descartado

Contar las dos ejecuciones de un mismo caso como un solo voto en la inducción: la simulación muestra que solo cambia dos reglas de los juguetes para perros y no corrige las reglas de pantuflas y sofás cama, que salen de la granularidad por rasgo y de un solo caso por clase. Se descarta.
