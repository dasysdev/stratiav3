---
name: demand-model
description: Construye el modelo de demanda de un producto real a partir de la URL de su ficha con el motor de demanda (primera versión, D-045). Congela la ficha, lanza el clasificador (reglamento v4), genera los bloques que falten y ensambla el modelo con el catálogo compilado y las reglas de importancia. Úsala cuando el usuario pida el modelo de demanda, los requisitos informativos o la clase de una URL de producto, o probar el motor con un producto real.
---

# demand-model — modelo de demanda de un producto real

Ejecución de la primera versión del motor ([model-training](../../../docs/10-model/model-training.md#operación-de-la-primera-versión), D-044, D-045): automática y sin esperar a nadie. Lo no compilado se usa como provisional, se marca y se encola para el entrenamiento.

**Entrada:** `URL [ID]`. Si no hay URL, pídela.

## Procedimiento

Todo desde `demand-engine/`.

1. **Comprobar la URL.**
   - Amazon.es no se captura: si la URL es de Amazon, dilo y para.
   - `ID`: el que dé el usuario o, si no, un slug del último segmento de la ruta (minúsculas, guiones, como mucho 40 caracteres). Si `../capture/var/pages/ID.html` ya existe, añade un sufijo: una ficha congelada no se sustituye y `page fetch` rechaza el ID (D-150).
2. **Congelar la ficha:** `bin/taxo page fetch ID URL`. Captura con el motor de captura (Chrome real, robots.txt y reservas TDM) dentro del contenedor: si no está levantado, `bin/run dev up`. Si la tienda lo excluye o lo bloquea, la orden falla y deja la evidencia en `../capture/var/pages/ID/`.
   - Si falla o devuelve una página de desafío o bloqueo, dilo y para.
3. **Clasificar.** Carpeta `var/runs/live/`; salida `var/runs/live/ID.json`. Lanza **un** agente (`Agent`, `general-purpose`) con este encargo:
   - eres el clasificador del motor de demanda;
   - trabaja en `/home/gonwsl/projects/stratiav3/demand-engine` y sigue `classifier/rulebook.md`, y `catalog/DRAFTING.md` solo si falta un bloque;
   - caso `ID`, con la URL y la ficha congelada en `../capture/var/pages/ID.html`;
   - escribe la salida en `var/runs/live/ID.json` y comprueba con `bin/model check` hasta que diga «correcto»;
   - no leas `cases/`, `var/runs/` (salvo su salida) ni `docs/`;
   - no ejecutes `bin/model assemble` ni `bin/train`;
   - escribe las dudas y los motivos con frases cortas, en voz activa y con los términos del reglamento;
   - devuelve el nombre del modelo, los bloques generados y sus dudas principales.

   No le pases resultados esperados ni conclusiones tuyas.

   Si el agente registró un bloque nuevo con pistas (`hints` en `catalog/runtime/`), lanza un agente revisor (`Agent`, `general-purpose`) con `classifier/hint-review.md` y esas pistas (D-211). Si rechaza alguna, continúa el clasificador (`SendMessage`) con sus motivos: reescribe la pista y registra de nuevo con `--replace`.
4. **Ensamblar:** `bin/model assemble var/runs/live/ID.json`. Escribe `ID.model.json` e `ID.model.md` y deja en `var/queue.jsonl` lo usado sin compilar. Después, `bin/model scope var/runs/live/ID.model.json` compone el modelo con la ficha de cada ámbito (D-155) y escribe `ID.content.json` (Contenido) e `ID.markup.json` (Marcado, D-220), con sus unidades RI × ámbito y el perfil del RI de cada una (D-177). Un requisito sin información resolutiva o sin descripción queda en `pendientes_de_definicion`: no lo completes.
5. **Informar** al usuario, de forma breve:
   - el nombre y la clave del modelo;
   - el número de requisitos por importancia;
   - los bloques de categoría generados en esta ejecución, que quedan «no compilado»;
   - los requisitos sin regla (con la importancia del voto, provisional);
   - las especializaciones (del catálogo o registradas en esta ejecución, «no compilada») y las cuestiones inferidas (provisionales);
   - los hechos declarados sin pregunta (huecos de cobertura);
   - las dudas del clasificador.

   Enlaza `var/runs/live/ID.model.md`.

## Qué no hacer

- No corregir a mano el catálogo, las reglas ni la salida del clasificador: lo que esté mal se corrige en el entrenamiento (`bin/train`), no en la ejecución.
- No ejecutar el entrenamiento salvo que el usuario lo pida.
- No capturar Amazon.es.
