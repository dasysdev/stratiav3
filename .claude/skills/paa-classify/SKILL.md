---
name: paa-classify
description: Clasifica con un agente de Claude Code las preguntas PAA consolidadas de un conjunto de semillas (perímetro, objeto, contraste con el catálogo de la clase, criterios de elección y regla C1–C4) y saca los requisitos candidatos de origen «paa» (D-091, D-097, D-099). El resultado queda en var/paa/sets/CONJUNTO/ (classified.json y report.md). Úsala cuando el usuario pida clasificar las preguntas PAA de un conjunto o sacar de ellas criterios de elección o requisitos candidatos.
---

# paa-classify: clasificación de las preguntas PAA de un conjunto

Un agente clasifica todas las preguntas de un conjunto con el reglamento `demand-engine/classifier/paa.md`. Es uno solo para que nombre cada criterio una vez y lo aplique igual a todas las preguntas (T-040). Lo demás es determinista: `demand-engine/bin/paa classify` prepara la entrada, comprueba la salida y genera el resultado. Se ejecuta en el host, sin contenedor.

**Entrada:** `CONJUNTO [--compare CLASIFICACIÓN.json] [--previous CLASSIFIED.json]`.

- `CONJUNTO`: un conjunto de `demand-engine/paa/` con las preguntas ya consolidadas (`paa run`). Si no lo dan, `bin/paa list` muestra los conjuntos; pregunta cuál.
- `--compare` (opcional): una clasificación manual (`[{q, code}]`) con la que se contrasta el resultado, por ejemplo la de una sonda.
- `--previous` (opcional): una clasificación anterior del mismo conjunto (otro reglamento u otra ejecución). Antes de preparar, copia la anterior (`classified.json`, `report.md` y `classify/`) a `classify/vN/`.

## Procedimiento

Todo desde `demand-engine/`.

1. **Preparar:** `bin/paa classify prepare CONJUNTO`. Escribe `var/paa/sets/CONJUNTO/classify/input.md` con las preguntas numeradas y sus semillas, el catálogo de la clase (sacado del modelo del conjunto) y los rasgos. Si ya hay una salida (`classify/output.json`) de otra ejecución, bórrala antes: el agente empieza de cero.
2. **Clasificar:** lanza **un** agente (`Agent`, `general-purpose`) con el encargo de abajo y espera a que termine.
3. **Comprobar:** `bin/paa classify check CONJUNTO`.
   - Si no dice «correcto», continúa el mismo agente (`SendMessage`) con los problemas.
   - Si a la segunda sigue mal, para e informa.
4. **Tokens:** `bin/paa classify usage CONJUNTO TRANSCRIPCIÓN`.
   - `TRANSCRIPCIÓN` es el `output_file` que devuelve `Agent` al lanzarlo; no lo leas.
   - El `subagent_tokens` de la notificación no sirve: es el contexto de la última petición, no el consumo.
5. **Resultado:** `bin/paa classify report CONJUNTO [--compare CLASIFICACIÓN.json] [--previous CLASSIFIED.json]`. Escribe en `var/paa/sets/CONJUNTO/`:
   - `classified.json`: cada pregunta con su clasificación y su procedencia, más los criterios, los candidatos con sus fuentes `paa-q:`, las revisiones, las aportaciones y la pertinencia de AC;
   - `report.md`: reparto por tipo, criterios con C1–C4 y sus preguntas, candidatos, revisiones, aportaciones, pertinencia de AC, requisitos que PAA confirma, preguntas que no generan, contrastes, consumo y dudas.
6. **Informar** al usuario, de forma breve:
   - reparto por tipo;
   - criterios y su veredicto;
   - candidatos (bloques, rasgo) y revisiones de requisitos existentes;
   - inferidas confirmadas;
   - lo que más discrepa del contraste;
   - consumo.

   Si la ejecución pertenece a una tarea de `bin/pm`, deja el consumo y los hallazgos en la tarea con `bin/pm note`.

## Encargo del agente

- Eres el clasificador de preguntas PAA del motor de demanda.
- Trabaja en `/home/gonwsl/projects/stratiav3/demand-engine` y sigue `classifier/paa.md`.
- Para las reglas de formulación y del voto, lee también `catalog/DRAFTING.md`: regla 5 (voto) y regla 8 (formulación).
- La entrada está en `var/paa/sets/CONJUNTO/classify/input.md`. Escribe la salida en `var/paa/sets/CONJUNTO/classify/output.json`.
- Comprueba con `bin/paa classify check CONJUNTO` hasta que diga «correcto».
- No leas `docs/`, `var/runs/`, `var/paa/probe-*`, ni `classified.json` o `report.md` de ningún conjunto.
- Devuelve en pocas líneas: el reparto, los criterios que generan, los candidatos y tus dudas principales.

No le pases la clasificación manual, conclusiones de sondas anteriores ni las tuyas: el contraste solo vale si el agente no las conoce.

## Qué no hacer

- No corregir a mano la salida del agente ni el resultado.
- No llevar al catálogo los candidatos, las revisiones ni las aportaciones: se deciden en el entrenamiento (`bin/train`), con origen «paa» (D-097).
- No ejecutar `paa run`: buscar en Google es otro paso, con sus límites (D-096).
