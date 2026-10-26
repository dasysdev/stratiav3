# Formulación de las cuestiones del catálogo de bloques

*Update decidido en la conversación del 2026-10-26, antes del escalado del entrenamiento (T-029). Se transcribe para su trazabilidad: las palabras del usuario, con las erratas corregidas, y el texto de la propuesta que aprobó.*

## Planteamiento del usuario

«Vamos a echar un vistazo a cómo se evalúan los requisitos a través de los AC y el GSC. Veo que los requisitos se están construyendo con unas preguntas muy extensas, abarcando demasiado análisis en cada uno. También veo que muchas de estas preguntas contienen subpreguntas condicionales.

1. Explícame lo que has entendido.
2. Estudia esto para ver si ya conviene crear alguna regla para modificar cómo se están construyendo o conviene esperar a trabajar más a fondo la valoración de los AC.»

## Datos que aportó Claude

- Catálogo (`gen.json` y `catalog/cat/`, 409 requisitos), recuento aproximado por heurística: unas 104 cuestiones con dos o más preguntas, 19 con una condición dentro de la pregunta y 131 con una lista de cuatro o más valores entre paréntesis.
- Tres tipos de condición interna: sobre la existencia de la información («y, si se indica, hasta qué temperatura», `cat.botas/07`; «y, si procede, el compositor», `cat.cd-de-musica/01` y `cat.discos-y-lp/01`); sobre un hecho del producto («y, si lleva piel con pelo…», «y, si tiene plataforma, qué altura»); y una pregunta de sí o no seguida de su detalle («¿Tiene ruedas y asa telescópica? Si las tiene, ¿cuántas ruedas y de qué tipo?»).
- Efectos en la evaluación: basta con que haya una parte para que la disponibilidad efectiva sea 1, y la ausencia de las demás baja a Concreción 1 (en `cat.toallas/01`, crítica, una ficha que dice «toalla de ducha» sin medidas); cada GSC tiene que juzgar varios hechos con un solo valor; «si se indica» hace que la parte no pueda faltar; una condición interna no deja un NA visible para la parte que no aplica.
- Efectos en el modelo de demanda: un requisito tiene un solo rasgo y una sola importancia, y las partes secundarias heredan los de la cabeza. 2 de los 5 rasgos mal etiquetados de I-20 son cuestiones compuestas (`cat.alimentos/06`, `cat.joyeria/01`). Los votos de importancia no son más dispersos en las compuestas (fracción minoritaria media del 7,4 %, frente al 8,0 % en las simples).
- Opciones: A, regla completa ahora, granularidad incluida; B, esperar al trabajo de los AC; C, regla estrecha ahora y granularidad después. Recomendada la C, porque T-029 acumula votos, rasgos y reglas por requisito ligados a su identificador y dividir después invalidaría esos datos.
- Muestra pedida por el usuario («Para validar el enfoque haz una muestra con `demand-engine/var/runs/2026-10-26-v4-b/sofa-cama-luna.model.md`»), con la ficha congelada y valores ilustrativos:
  - De los 34 requisitos de categoría, 28 quedan igual. Se dividen `cat.sofas/01` (tipo y configuración; piezas o módulos), `cat.sofas/06` (material del armazón; uniones), `cat.sofas/11` (material del relleno; densidad de la espuma, condicionada a que lleve espuma) y `cat.sofas/16` (partes regulables y mecanismo; plazas y posiciones de reclinación, condicionadas a que sea reclinable, como ya hace `cat.sofas/17`). En `cat.sofas-cama/02` el material y el grosor del colchón no tienen fuente (`SOFA.mattress` es la medida), y en `cat.sofas/18` tampoco «cómo se alimentan».
  - Aparecen ausencias que el «parcial» ocultaba (`cat.sofas/01`; en la capa general, la posventa de `gen/12` y la autenticidad de las opiniones de `gen/15`). Ningún caso pierde información.
  - La regla de dividir no resuelve el par `cat.sofas/13` (tipo de asiento y cojines: dividir ganaría) frente a `cat.sofas/05` (seis medidas de uso: dividir perdería). Las partes comparten rasgo e importancia en los dos; decidir depende de cómo trate la Concreción un RI de varios componentes (OQ-22).

## Propuesta aprobada

Reglas, con el texto de la conversación:

1. «Ninguna condición sobre la existencia de la información («si se indica», «si procede»). Un componente forma parte de la necesidad o no.»
2. «Una condición sobre un hecho que afecta solo a una parte se convierte en un requisito condicionado propio, con la condición en `applicability`. La pregunta de sí o no seguida de su detalle se mantiene, porque un «no» fundamentado lo resuelve todo.»
3. «Una necesidad por RI. Se divide cuando las partes se responden por separado, cada una sirve por sí sola para comparar y tomarían otro rasgo u otra importancia. Se mantiene junto lo que solo tiene sentido unido: plazo y condiciones del desistimiento, o nombre y dirección del fabricante.» Tras la muestra, estrecha: «solo divide cuando las partes tomarían otro rasgo u otra importancia».
4. «Cada componente de la cuestión tiene fuente; si no la tiene, va como cuestión inferida.»

Alcance y aplazamientos, con el texto de la conversación:

- «Las reglas 1, 2, 3 (estrecha) y 4 entrarían ahora, por intake y en T-030. La granularidad cuando las partes comparten rasgo e importancia esperaría al trabajo de los AC, con el par sofas/13–sofas/05 anotado en OQ-22.»
- «En la capa general, que es marco y la decides tú, hay candidatas: gen/12, gen/15 y gen/01.»
- Lo que conviene esperar al trabajo de los AC incluye también qué hacer con las listas de ejemplos; mientras tanto rige la RI-07 (los ejemplos son ayudas, no una lista de componentes).

## Decisión del usuario

«Aplícalo así.»
