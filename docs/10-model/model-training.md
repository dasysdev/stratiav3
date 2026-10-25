---
id: model-training
title: Entrenamiento y ejecución del modelo de demanda
layer: model
status: vigente
version: 1.2
updated: 2026-10-25
sources: [INTAKE 2026-10-25-training-runtime, INTAKE 2026-10-25-induced-rules, INTAKE 2026-10-25-training-operation, INTAKE 2026-10-25-relevance-origin]
---

# Entrenamiento y ejecución del modelo de demanda

Parte del [modelo de demanda](demand-model.md). Define cómo se produce el modelo de demanda de un producto: un **entrenamiento** periódico que induce las reglas y compila el catálogo de bloques, y una **ejecución** automática que construye cada modelo con ellos. La persona responsable solo define el **marco** ([D-041](../30-governance/decisions.md#d-041), [D-044](../30-governance/decisions.md#d-044)). La operación de la primera versión está en [D-045](../30-governance/decisions.md#d-045).

## Definición

> No voy a revisarlo manualmente. Debe haber un sistema de reglas para determinar la categoría de importancia relativa. […] El sistema debe basarse en reglas o en configuraciones específicas. La parametrización específica puede formar parte del sistema, pero como un resultado compilado, no como un diseño específico. El entrenamiento es para definir los parámetros sobre los patrones usados en el entrenamiento. Pueden salir reglas generales y reglas específicas.
>
> Tampoco quiero revisar cada regla. Lo que defino es el marco general, objetivos, características del resultado, etc. Las reglas concretas deben ser producto del entrenamiento también.
>
> — INTAKE 2026-10-25-induced-rules (palabras del usuario)

## Marco

> - **Propósito:** establecer los requisitos informativos de una oferta.
> - **Objetivos y características del resultado:** identidad por bloques, especificidad necesaria, críticos pocos, nada de conjeturas.
> - **Criterios de éxito:** cobertura de cuestiones, estabilidad entre ejecuciones, coherencia de la importancia.
> - **Invariantes del canon** (D-020 a D-043): lo que ninguna regla puede violar.
>
> El usuario no revisa requisitos, bloques ni reglas sueltas: lee el informe agregado del entrenamiento y, si hace falta, ajusta el marco.
>
> — INTAKE 2026-10-25-induced-rules

Es la única intervención humana. Las decisiones ya aceptadas del canon forman parte del marco, en particular las pruebas de importancia ([D-035](../30-governance/decisions.md#d-035)), los criterios del catálogo ([D-043](../30-governance/decisions.md#d-043)) y la capa general ([D-034](../30-governance/decisions.md#d-034), [D-038](../30-governance/decisions.md#d-038)): las reglas inducidas operan dentro de ellas y no pueden modificarlas. Si el entrenamiento encuentra que alguna perjudica a los criterios de éxito, lo dice en el informe agregado; no la cambia ([D-044](../30-governance/decisions.md#d-044)).

## Entrenamiento

> 1. **Reunir los casos:** el conjunto de entrenamiento más lo acumulado en la cola de pendientes.
> 2. **Aplicar las reglas vigentes:** dos veces por caso.
> 3. **Medir contra el marco.**
> 4. **Detectar patrones:** agrupar divergencias e inestabilidades por rasgos comunes.
> 5. **Inducir reglas:** reglas generales, y específicas donde la general falla, para cada decisión del procedimiento:
>    - composición;
>    - especializaciones;
>    - relevancia de las propiedades de Amazon;
>    - cuestiones inferidas;
>    - importancia: rasgos del requisito → crítico, principal o complementario.
> 6. **Compilar el catálogo:** generador determinista de bloques y, encima, las reglas inducidas. Cada requisito guarda la regla que lo decidió.
> 7. **Validar automáticamente:** se aceptan si mejoran las métricas y no violan el marco; si no, se descartan.
> 8. **Publicar versión e informe agregado:** métricas, reglas añadidas o retiradas y sus efectos. El usuario lee el informe, no las reglas.
>
> — INTAKE 2026-10-25-induced-rules

Lo que antes validaba la persona responsable (las especializaciones, [D-022](../30-governance/decisions.md#d-022); las cuestiones inferidas, [D-036](../30-governance/decisions.md#d-036); la relevancia de las propiedades de Amazon, [D-039](../30-governance/decisions.md#d-039); los bloques del catálogo, [D-040](../30-governance/decisions.md#d-040); las importancias, [D-041](../30-governance/decisions.md#d-041)) lo valida ahora el entrenamiento contra el marco ([D-044](../30-governance/decisions.md#d-044)). El vocabulario de rasgos, las reglas de importancia, las métricas y los casos se fijan en la [operación de la primera versión](#operación-de-la-primera-versión) ([D-045](../30-governance/decisions.md#d-045)).

## Ejecución

> - **Ejecución, totalmente automática y sin esperar nunca a una persona.**
> […]
> - **Trazabilidad.** Cada resultado indica qué partes del modelo usó sin revisar, para que la auditoría pueda informar con ellas y sin ellas, como ya prevé D-036.
>
> — INTAKE 2026-10-25-training-runtime; «sin revisar» significa no compilado por el entrenamiento ([D-044](../30-governance/decisions.md#d-044))

> 1. Congelar la ficha.
> 2. Leer lo declarado.
> 3. Componer la clase.
> 4. **Seleccionar los bloques:**
>    - categoría compilada → se usan sus bloques;
>    - categoría nueva → se genera y compila al vuelo, marcada «no revisada», y se encola.
> 5. Especializaciones.
> 6. **Cuestiones inferidas:** añadido provisional fuera de la clave, encolado.
> 7. **Importancia:** la traen los bloques compilados; lo nuevo la recibe de las reglas de importancia.
> 8. Aplicación.
> 9. Denominación.
> 10. **Modelo de demanda:** incluye la lista de lo usado sin compilar.
>
> — INTAKE 2026-10-25-induced-rules; «no revisada» es el estado «no compilado», y lo nuevo sin regla en su rama recibe el voto del agente como provisional ([D-045](../30-governance/decisions.md#d-045))

Una cuestión inferida se usa en la ejecución como añadido provisional del modelo, marcado como tal y fuera de la clave; cuando el entrenamiento la acepta, pasa al bloque del catálogo como nueva versión ([D-041](../30-governance/decisions.md#d-041)). La clave del modelo lleva la versión de cada bloque, y un bloque generado en ejecución está «no compilado» hasta que el entrenamiento lo compila ([D-045](../30-governance/decisions.md#d-045)).

## Conexiones y principios

> - El entrenamiento publica reglas y catálogo compilados, que la ejecución solo lee.
> - La ejecución deja en la cola todo lo que usó sin compilar, y el entrenamiento lo convierte en casos y reglas.
> - El marco fija qué cuenta como buen resultado, y el entrenamiento solo acepta reglas que lo cumplen.
>
> — INTAKE 2026-10-25-induced-rules

> - **Identidad por bloques.**
> - **Reglas inducidas, no escritas:** las reglas concretas, generales y específicas, salen del entrenamiento; el humano define el marco.
> - **Catálogo como resultado:** ningún bloque ni importancia se diseña a mano; se compila desde referencias y reglas, y se regenera.
> - **Ejecución sin esperas.**
> - **Trazabilidad:** cada requisito dice de dónde sale y qué regla decidió su importancia.
> - **Referencias fijadas.**
>
> — INTAKE 2026-10-25-induced-rules

La identidad por bloques es la del [modelo de demanda](demand-model.md#composición-e-identidad-del-modelo); la ejecución sin esperas, la de la sección anterior; las referencias fijadas, las versiones congeladas de [sources](../20-methods/product-taxonomy/sources.md). La capa general no la compila el entrenamiento: es parte del marco ([D-044](../30-governance/decisions.md#d-044)).

## Operación de la primera versión

### Rasgos

> **Rasgos de un requisito.** Rasgo principal: qué resuelve la cuestión, de una lista cerrada: identidad, contenido, medida que fija lo vendido, medida descriptiva, material, construcción, prestación, uso y compatibilidad, seguridad, cuidado, estética y certificación u origen. Además, los rasgos que ya tenemos: entidad, origen, aplicabilidad y posición del bloque. Cada atributo de Shopify o propiedad de Amazon se etiqueta una sola vez y se reutiliza en todas las categorías; así una categoría nueva hereda casi todo ya etiquetado.
>
> — INTAKE 2026-10-25-training-operation

El vocabulario tiene además **magnitud física**: peso, grosor y gramaje, que salen de la medida descriptiva y no tienen regla fija ([D-051](../30-governance/decisions.md#d-051)). Un requisito toma el rasgo de sus fuentes. Las cuestiones inferidas y las de especialización, que no tienen fuente de referencia, se etiquetan en el propio requisito ([D-045](../30-governance/decisions.md#d-045)).

### Reglas de importancia

> **C. Por el árbol de Shopify:** la regla vive en la clase y sube a la categoría madre solo si vale para todas sus hijas.
>
> - **El crítico sí es global.** Su prueba no depende de la clase: sin la cuestión, ¿se sabe qué se vende, cuánto cuesta y si se puede adquirir? Por eso la capa general y la medida que fija lo vendido valen para todo.
> - **Si una clase no tiene regla todavía** (por ejemplo, el primer producto de electrónica), no se le aplica una regla de otra rama: se usa la importancia que propone el agente, marcada como provisional y encolada, como ya prevé D-044 para lo no compilado. Cuando haya suficientes casos de esa rama, el entrenamiento compila sus reglas.
>
> Ejemplo: «estética → complementario» sube a Ropa de casa si así está en mantas, sábanas y toallas; si en Cojines decorativos la estética es principal, esa regla se queda en Cojines y la de arriba no se aplica ahí.
>
> […] los agentes proponen en cada producto nuevo la importancia que darían («votos»), pero manda la regla; si muchos votos contradicen una regla, el entrenamiento la cambia si las métricas mejoran; el marco pone límites que ninguna regla puede saltarse (ninguna regla puede hacer crítica la estética, ni tocar la capa general ni el criterio de las medidas).
>
> — INTAKE 2026-10-25-training-operation; la opción C sustituye solo el ámbito global del mecanismo, que por lo demás se mantiene

Lectura operativa ([D-045](../30-governance/decisions.md#d-045)):

- **Subir a la madre.** Una regla sube a la madre cuando al menos dos hijas con datos de ese rasgo la comparten y ninguna la contradice (mínimo estructural, la lectura de D-043, criterio 4). Las hijas sin datos heredan la regla de la madre. Las reglas no suben por encima de las verticales de Shopify.
- **Regla de una clase.** Dentro de una clase, la regla es la importancia mayoritaria; en un empate se elige la más alta (elección de Claude, por analogía con [D-035](../30-governance/decisions.md#d-035): la duda no baja la importancia).
- **Resolución.** La importancia de un requisito se resuelve desde la clase del producto hacia arriba, con la regla más específica de su rasgo. En un juego se resuelve desde cada pieza y se toma la más alta. Las importancias de partida son las del catálogo y los votos.
- **Crítico.** Solo pueden ser críticos los rasgos que dicen qué se vende: identidad, contenido y medida que fija lo vendido.
  - La medida que fija lo vendido es siempre crítica y la medida descriptiva (dimensiones y tallas) siempre principal ([D-043](../30-governance/decisions.md#d-043), criterio 1). La magnitud física la decide el árbol ([D-051](../30-governance/decisions.md#d-051)).
  - Para identidad y contenido decide una regla global; si no son críticos, decide el árbol.
  - Un voto crítico en otro rasgo cuenta como principal.
  - La restricción a tres rasgos es lectura de Claude; el artefacto solo excluye expresamente la estética.
- **Capa general.** Queda fija: ninguna regla la revisa por clase, y no tiene estado de compilación.

### Relevancia

> Nuestro modelo solo debe incluir cuestiones relevantes, las complementarias siendo las de menor relevancia. — INTAKE 2026-10-25-relevance-origin (palabras del usuario)

> 1. No es un cuarto nivel de importancia: la escala sigue siendo crítico, principal y complementario. Antes de la importancia, cada requisito pasa una prueba: «¿informa sobre algo que importa para evaluar o comparar ofertas de esta clase?» (la condición 3 del criterio de especialización). Si no la pasa, sale del modelo de esa clase.
> 2. Lo decide el entrenamiento con el mismo mecanismo que la importancia: los agentes votan con un cuarto valor posible, «no relevante»; el entrenamiento induce reglas de relevancia por el árbol […], por requisito y clase, no por rasgo.
> 3. Sin regla compilada, la duda no excluye: el requisito se queda como complementario, marcado como provisional y encolado.
> 4. Límites del marco: nunca se excluyen la capa general, los requisitos normativos ni la medida que fija lo vendido.
> 5. Trazabilidad: lo excluido no desaparece; el modelo lo lista aparte con la regla que lo excluyó. No es NA: no forma parte de lo que se audita.
>
> — INTAKE 2026-10-25-relevance-origin

Lectura operativa ([D-050](../30-governance/decisions.md#d-050)):

- **Datos de partida.** Un requisito incluido en un bloque es relevante en su categoría: cuenta como un voto «relevante» en ella. Los votos se registran en la clase del producto.
- **Sin regla.** «Se queda como complementario» vale cuando el requisito no tiene regla de importancia; si la tiene, conserva su nivel y se marca como de relevancia dudosa. Manda la regla y la duda no baja la importancia.
- **Juegos.** En un modelo de varias piezas, un requisito solo se excluye si lo excluyen todas las clases a las que se aplica.
- **Marco.** El marco fija la importancia de lo relevante, no su relevancia: solo protegen de la exclusión la capa general, lo normativo y la medida que fija lo vendido.
- **Regla.** Es la mayoría en la clase; en empate, relevante. Sube a la madre con el mismo mínimo estructural que la importancia.
- **Dónde nace la irrelevancia.** Casi siempre en los bloques de sector, cuyos atributos llegan a todas las hijas: el color importa en un collar y no en un pienso.
- **Qué no es irrelevancia.** «No aplica al producto» (el número de hilos en unas sábanas de coralina) es un requisito condicionado a un hecho del producto, y «no aplica a la oferta», una condición de la oferta que no se da. Los dos quedan en gris.
- **En el modelo.** Lo excluido aparece en «Excluidos en esta clase (no se auditan)», con su regla. El informe da, por regla, el requisito, la clase, los votos y cuántos requisitos decide.
- **Amazon.** La inclusión de una propiedad de Amazon en el bloque la decide la redacción del bloque; su exclusión en una clase, este filtro.

### Métricas y aceptación

> - **Cobertura:** las cuestiones clave esperadas que aparecen en el modelo (solo en los casos que tienen resultado esperado). […] Con miles de fichas nadie escribe lo esperado. Se cuentan los hechos que declaran las fichas de una clase (materiales, medidas, funciones…) y cuántos no tienen ninguna pregunta en el modelo: cada hecho sin pregunta es un hueco. Lo estético y lo promocional no cuentan (el clasificador ya los separa). Se mide sola y mejora con el volumen.
> - **Estabilidad:** el mismo resultado en dos ejecuciones (composición, bloques, importancia).
> - **Coherencia:** cuántos requisitos con los mismos rasgos tienen importancias distintas.
> - Una regla se acepta si ninguna métrica empeora y al menos una mejora.
>
> — INTAKE 2026-10-25-training-operation

La primera parte de la cobertura se mide en el conjunto de control y la segunda en todos los casos. Los beneficios reclamados tampoco cuentan como hueco, porque [D-025](../30-governance/decisions.md#d-025) los deja fuera de la clase. La coherencia se mide dentro de cada clase: una excepción de la opción C no es incoherencia. Con la relevancia se añaden la **coherencia de relevancia** (requisitos que siguen en el modelo con mayoría de votos «no relevante» en su clase) que debe bajar, y una **salvaguarda de cobertura**: una exclusión que deja sin pregunta un hecho que declaran las fichas de la clase empeora la cobertura, y la regla se descarta, porque «lo que las fichas cuentan no se puede declarar irrelevante» ([D-050](../30-governance/decisions.md#d-050)). El informe agregado da:

- las métricas frente a la versión anterior;
- las reglas añadidas o retiradas, con cuántos requisitos decide cada una;
- los votos que contradicen el marco;
- lo usado sin compilar;
- las divergencias de las decisiones no inducidas, agrupadas por patrón ([D-045](../30-governance/decisions.md#d-045)).

### Casos, alcance y ejecución

> - **Casos de entrenamiento:** el conjunto de entrenamiento será un catálogo grande capturado por el motor. Los 14 casos actuales quedan como conjunto de control: son los únicos con resultado esperado y sirven para detectar si algo empeora.
> - **Alcance de esta versión:** Inducción solo para la importancia. Para la composición, las especializaciones, la relevancia de Amazon y las inferidas, se miden las divergencias y el informe las agrupa por patrón, pero sus reglas se inducen en la versión siguiente.
> - **I-19:** La clave del modelo lleva la versión de cada bloque. Un bloque generado en ejecución lleva el estado «no compilado» hasta que el entrenamiento lo compila.
> - **Ejecución:** para probar productos reales ahora, un comando de Claude Code; para entrenar con miles de fichas no escala y hacen falta llamadas a la API por lotes (tarea aparte).
>
> — INTAKE 2026-10-25-training-operation; desde [D-050](../30-governance/decisions.md#d-050) también se induce la relevancia

- **Motor de captura.** Es el motor de captura compartido con el MPIR ([D-046](../30-governance/decisions.md#d-046)).
- **Comando de prueba.** El comando es `/demand-model URL`: lanza los agentes y llama al código determinista.
- **Quién decide en la primera versión.** La importancia, las reglas (o el voto, sin regla); la relevancia, las reglas de relevancia (sin regla, el requisito se queda: [D-050](../30-governance/decisions.md#d-050)); la composición, las especializaciones, las inferidas y la aplicación, el clasificador, con especializaciones e inferidas siempre provisionales; la relevancia de Amazon, la redacción automática del bloque generado ([OQ-49](../30-governance/open-questions.md)).
- **Estados del bloque.** Pasan a ser «no compilado» o «compilado», y cada bloque se escribe en la clave como `<bloque>@<versión>` ([D-045](../30-governance/decisions.md#d-045)).

## Pendiente

Ver [open-questions](../30-governance/open-questions.md):

- selección del catálogo de entrenamiento ([OQ-48](../30-governance/open-questions.md));
- inducción de las reglas de composición, especializaciones, relevancia de Amazon e inferidas ([OQ-49](../30-governance/open-questions.md));
- extensión del principio al MPIR y a la auditoría ([OQ-46](../30-governance/open-questions.md)).

## Relacionado

- [demand-model](demand-model.md) — modelo de demanda, bloques y capa general
- [study-class](study-class.md) — clase de estudio y criterio de especialización
- [requirement-blocks](../20-methods/product-taxonomy/requirement-blocks.md) — catálogo de bloques (método, propuesta)
