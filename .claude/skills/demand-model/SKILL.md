---
name: demand-model
description: Construye el modelo de demanda de un producto real a partir de la URL de su ficha con el motor de demanda (primera versión, D-045). Congela la ficha, lanza el clasificador (reglamento v3), genera los bloques que falten y ensambla el modelo con el catálogo compilado y las reglas de importancia. Úsala cuando el usuario pida el modelo de demanda, los requisitos informativos o la clase de una URL de producto, o probar el motor con un producto real.
---

# demand-model — modelo de demanda de un producto real

Ejecución de la primera versión del motor ([model-training](../../../docs/10-model/model-training.md#operación-de-la-primera-versión), D-044, D-045): automática y sin esperar a nadie. Lo no compilado se usa como provisional, se marca y se encola para el entrenamiento.

**Entrada:** `URL [ID]`. Si no hay URL, pídela.

## Procedimiento

Todo desde `demand-engine/`.

1. **Comprobar la URL.**
   - Amazon.es no se captura: si la URL es de Amazon, dilo y para.
   - `ID`: el que dé el usuario o, si no, un slug del último segmento de la ruta (minúsculas, guiones, como mucho 40 caracteres). Si `var/pages/ID.html` ya existe y es de otra URL, añade un sufijo.
2. **Congelar la ficha:** `bin/taxo page fetch ID URL`. Captura con el motor de captura (Chrome real, robots.txt y reservas TDM) dentro del contenedor: si no está levantado, `bin/run dev up`. Si la tienda lo excluye o lo bloquea, la orden falla y deja la evidencia en `var/pages/ID/`.
   - Si falla o devuelve una página de desafío o bloqueo, dilo y para.
   - El motor de captura compartido (D-046) sustituirá esta descarga en T-020.
3. **Clasificar.** Carpeta `var/runs/live/`; salida `var/runs/live/ID.json`. Lanza **un** agente (`Agent`, `general-purpose`) con este encargo:
   - eres el clasificador del motor de demanda;
   - trabaja en `/home/gonwsl/projects/stratiav3/demand-engine` y sigue `classifier/rulebook.md`, y `catalog/DRAFTING.md` solo si falta un bloque;
   - caso `ID`, con la URL y la ficha congelada en `var/pages/ID.html`;
   - escribe la salida en `var/runs/live/ID.json` y comprueba con `bin/model check` hasta que diga «correcto»;
   - no leas `cases/`, `var/runs/` (salvo su salida) ni `docs/`;
   - no ejecutes `bin/model assemble` ni `bin/train`;
   - devuelve el nombre del modelo, los bloques generados y sus dudas principales.

   No le pases resultados esperados ni conclusiones tuyas.
4. **Ensamblar:** `bin/model assemble var/runs/live/ID.json`. Escribe `ID.model.json` e `ID.model.md` y deja en `var/queue.jsonl` lo usado sin compilar.
5. **Informar** al usuario, de forma breve:
   - el nombre y la clave del modelo;
   - el número de requisitos por importancia;
   - los bloques de categoría generados en esta ejecución, que quedan «no compilado»;
   - los requisitos sin regla (con la importancia del voto, provisional);
   - las especializaciones y las cuestiones inferidas (provisionales);
   - los hechos declarados sin pregunta (huecos de cobertura);
   - las dudas del clasificador.

   Enlaza `var/runs/live/ID.model.md`.

## Qué no hacer

- No corregir a mano el catálogo, las reglas ni la salida del clasificador: lo que esté mal se corrige en el entrenamiento (`bin/train`), no en la ejecución.
- No ejecutar el entrenamiento salvo que el usuario lo pida.
- No capturar Amazon.es.
