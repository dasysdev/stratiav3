---
name: demand-model
description: Construye el modelo de demanda de un producto real con el motor de demanda (primera versión, D-045), a partir de la URL de su ficha o de una ficha ya congelada en capture (--page ID, de cualquier perfil). Congela la ficha (con --page, no), lanza el clasificador (reglamento v5), genera los bloques que falten y ensambla el modelo con el catálogo compilado y las reglas de importancia. Después, la fase PAA (D-224): semillas de la clave con taxo, búsqueda, clasificación y entrada provisional; ensambla de nuevo y compone por ámbito. Úsala cuando el usuario pida el modelo de demanda, los requisitos informativos o la clase de una URL de producto o de una ficha congelada, o probar el motor con un producto real.
---

# demand-model — modelo de demanda de un producto real

Ejecución de la primera versión del motor ([model-training](../../../docs/10-model/model-training.md#operación-de-la-primera-versión), D-044, D-045): automática y sin esperar a nadie. Lo no compilado se usa como provisional, se marca y se encola para el entrenamiento.

La ejecución tiene dos fases ([D-224](../../../docs/30-governance/decisions.md#d-224)): la fase 1 clasifica y ensambla (pasos 1 a 4); la fase 2, PAA, trabaja sobre ese modelo (paso 5). Si la fase 2 no termina, el resultado es el modelo de la fase 1.

**Entrada:** `URL [ID]` o `--page ID`. Si no hay ninguna de las dos, pide la URL.

- `URL [ID]`: el motor congela la ficha y el caso lleva su ID.
- `--page ID`: la skill usa una ficha ya congelada en `../capture/var/pages/ID.html`, de cualquier perfil de captura (`reader` o `audit-es`), y no captura nada. El clasificador lee la ficha por el ID del caso (`bin/taxo page`), así que el caso se llama como la ficha: `ID`. Así el modelo de demanda y la auditoría informativa usan la misma ficha.

## Procedimiento

Todo desde `demand-engine/`.

1. **Comprobar la URL** (entrada `URL [ID]`). Si la entrada es `--page ID`, ve al paso 1b.
   - Amazon.es no se captura: si la URL es de Amazon, dilo y para.
   - `ID`: el que dé el usuario o, si no, un slug del último segmento de la ruta (minúsculas, guiones, como mucho 40 caracteres). Si `../capture/var/pages/ID.html` ya existe, añade un sufijo: una ficha congelada no se sustituye y `page fetch` rechaza el ID (D-150).

   **1b. Comprobar la ficha** (entrada `--page ID`).
   - Si falta `../capture/var/pages/ID.html` o `ID.json`, dilo y para. No captures la ficha en su lugar.
   - Lee de `ID.json` la URL (`url`) y el perfil de captura (`profile`; si falta, es `reader`).
   - Si `var/runs/live/ID.json` ya existe, ya hay un caso sobre esa ficha: dilo y para. Si el usuario pide rehacerlo, la salida nueva lo sustituye.
   - Sigue en el paso 3: no ejecutes `page fetch`.
2. **Congelar la ficha** (solo con `URL`): `bin/taxo page fetch ID URL`. Captura con el motor de captura (Chrome real, robots.txt y reservas TDM) dentro del contenedor: si no está levantado, `bin/run dev up`. Si la tienda lo excluye o lo bloquea, la orden falla y deja la evidencia en `../capture/var/pages/ID/`.
   - Si falla o devuelve una página de desafío o bloqueo, dilo y para.
3. **Clasificar.** Carpeta `var/runs/live/`; salida `var/runs/live/ID.json`. Lanza **un** agente (`Agent`, `general-purpose`) con este encargo:
   - eres el clasificador del motor de demanda;
   - trabaja en `/home/gonwsl/projects/stratiav3/demand-engine` y sigue `classifier/rulebook.md`, y `catalog/DRAFTING.md` solo si falta un bloque;
   - caso `ID`, con la URL y la ficha congelada en `../capture/var/pages/ID.html` (con `--page`, la URL de `ID.json`);
   - escribe la salida en `var/runs/live/ID.json` y comprueba con `bin/model check` hasta que diga «correcto»;
   - no leas `cases/`, `var/runs/` (salvo su salida) ni `docs/`;
   - no ejecutes `bin/model assemble` ni `bin/train`;
   - escribe las dudas y los motivos con frases cortas, en voz activa y con los términos del reglamento;
   - devuelve el nombre del modelo, los bloques generados y sus dudas principales.

   No le pases resultados esperados ni conclusiones tuyas.

   Si el agente registró un bloque nuevo con pistas (`hints` en `catalog/runtime/`), lanza un agente revisor (`Agent`, `general-purpose`) con `classifier/hint-review.md` y esas pistas (D-211). Si rechaza alguna, continúa el clasificador (`SendMessage`) con sus motivos: reescribe la pista y registra de nuevo con `--replace`.
4. **Ensamblar** (fase 1): `bin/model assemble var/runs/live/ID.json`. Escribe `ID.model.json` e `ID.model.md` y deja en `var/queue.jsonl` lo usado sin compilar.
   - El modelo registra la ficha congelada usada en `page`: su ID (el del caso) y su perfil de captura.
   - Cada RI lleva su marca de comparación (`comparison`, D-126). Un RI sin marca queda en `pending_definition`, sin valor por defecto (D-139): no la decidas.
   - `engine.hints` anota la versión del catálogo de pistas (D-138).
   - Después, `bin/model scope var/runs/live/ID.model.json` compone el modelo con la ficha de cada ámbito (D-155). Escribe `ID.content.json` (Contenido) e `ID.markup.json` (Marcado, D-220), con sus unidades RI × ámbito, la marca de cada RI y su perfil (D-177).
   - Un requisito sin información resolutiva, sin descripción o sin marca queda en `pendientes_de_definicion`: no lo completes.
5. **Fase PAA** (fase 2, D-224). Si un paso falla o Google bloquea, para la fase: el resultado es el modelo del paso 4. Informa del motivo y de cómo reanudarla (`bin/paa run CONJUNTO` es reanudable).
   1. **Semillas:** `bin/paa seeds var/runs/live/ID.model.json` (en el host). Lee lo que muestra.
      - Si dice que el conjunto ya existe con la misma clave (D-116), usa ese conjunto y ve al paso 5.2.
      - Si dice «OQ-93» (clase sin calibrar), no elijas el rasgo de los valores. Pregunta al usuario cuál, con los atributos que lista. Si no lo decide, la fase 2 no termina.
      - Elige los valores del rasgo con uso en España (`--values`), como en los conjuntos de `paa/`.
      - Si el nombre de Shopify no es el que se usa en el mercado español, pon el nombre del mercado (`--seed BLOQUE=TEXTO` o `--seed VALOR=TEXTO`).
      - Si otro conjunto tiene una semilla con el mismo significado, usa su mismo texto: así su búsqueda se reutiliza.
      - Repite la orden con `--values` (y `--seed`). Escribe `paa/CONJUNTO.json` y dice cuántas búsquedas se reutilizan y cuántas son nuevas.
   2. **Búsqueda:** `bin/paa run CONJUNTO` (en el contenedor; si no está levantado, `bin/run dev up`). Reutiliza lo ya capturado en otros conjuntos y busca el resto en Google, con los límites del README del motor PAA (unos 30 s por búsqueda nueva). `bin/paa status CONJUNTO` muestra el estado. Si para por un bloqueo o un fallo, la fase 2 no termina.
   3. **Clasificación:** si el conjunto no tiene `var/paa/sets/CONJUNTO/classified.json`, clasifícalo con la skill `/paa-classify CONJUNTO`: sus pasos 1 a 5, sin `--compare` ni `--previous`, y el 6 solo si el conjunto tiene caso en `cases/paa/`. Esa skill lanza un agente clasificador y un agente revisor de las pistas.
   4. **Entrada provisional:** `bin/model assemble var/runs/live/ID.json --paa CONJUNTO`. Sustituye `ID.model.json`, `ID.model.md` y la entrada de la cola. Lo de PAA entra «no compilado», fuera de la clave, en `paa` del modelo.
      - Si dice que la clasificación no tiene todas las preguntas, clasifica de nuevo (paso 5.3) y repite este paso.
      - Si dice que el conjunto es de otra clave, para la fase 2 e informa.
   5. **Composición:** `bin/model scope var/runs/live/ID.model.json`, otra vez, para que las unidades RI × ámbito incluyan lo de PAA.
6. **Informar** al usuario, de forma breve:
   - el nombre y la clave del modelo;
   - la ficha congelada usada: su ID y su perfil de captura (`page`);
   - el número de requisitos por importancia;
   - los bloques de categoría generados en esta ejecución, que quedan «no compilado»;
   - los requisitos sin regla (con la importancia del voto, provisional);
   - las especializaciones (del catálogo o registradas en esta ejecución, «no compilada») y las cuestiones inferidas (provisionales);
   - los hechos declarados sin pregunta (huecos de cobertura);
   - los RI sin marca de comparación (pendientes de definición, D-139);
   - la fase PAA: el conjunto, las búsquedas reutilizadas y las nuevas, lo que entró como provisional (requisitos candidatos, confirmaciones, aportaciones, pistas y marcas) y lo que no entró; o, si no terminó, el motivo y cómo reanudarla;
   - las dudas del clasificador.

   Enlaza `var/runs/live/ID.model.md`.

## Qué no hacer

- No corregir a mano el catálogo, las reglas ni la salida del clasificador: lo que esté mal se corrige en el entrenamiento (`bin/train`), no en la ejecución.
- No ejecutar el entrenamiento salvo que el usuario lo pida.
- No capturar Amazon.es.
- Con `--page`, no capturar la ficha de nuevo, ni siquiera si falta.
- No ejecutar `bin/paa compile` ni `bin/paa control`: lo de PAA entra en el catálogo con la pasada del entrenamiento (D-178, D-180), no en la ejecución.
- No buscar en Google fuera de `bin/paa run` ni cambiar sus límites de ejecución (D-096).
- No elegir el rasgo de los valores en una clase sin calibrar (OQ-93).
