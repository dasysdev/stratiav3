---
name: classify-batch
description: Clasifica por lotes, con agentes de Claude Code en paralelo, las fichas capturadas de una selección del catálogo de entrenamiento (D-054). Fase 1, un caso por tipo, que genera los bloques que falten; fase 2, el resto en paralelo. Cada salida queda en var/runs/RUN/ID.json, comprobada con bin/model check y ensamblada; se registran los tokens de cada agente. Úsala cuando el usuario pida clasificar el catálogo de entrenamiento, el piloto o un lote de fichas congeladas.
---

# classify-batch — clasificación del catálogo de entrenamiento por lotes

Clasificación a escala con agentes de Claude Code ([D-054](../../../docs/30-governance/decisions.md#d-054)): el mismo reglamento, la misma salida y la misma comprobación que `/demand-model`, repartidos entre agentes. El código del lote es `bin/train batch` (plan, estado, tokens y ensamblado).

**Entrada:** `SELECCIÓN RUN [--pilot] [--only ID…]`.
- `SELECCIÓN`: un `training/selection/STORE-FECHA.json` con fichas ya capturadas (`bin/train capture`).
- `RUN`: carpeta de la ejecución, `var/runs/FECHA-STORE-NOMBRE` (p. ej. `var/runs/2026-10-25-eci-pilot`).

Si falta la selección o el nombre de la ejecución, pídelos.

## Procedimiento

Todo desde `demand-engine/`.

1. **Plan:** `bin/train batch plan SELECCIÓN RUN [--pilot] [--only ID…]`.
   - Escribe `RUN/batch.json` con las fichas capturadas y su fase, y muestra el estado de cada caso.
   - Si `batch.json` ya existe, lo reutiliza y no cambia los casos: la ejecución es reanudable.
   - **Fase 1:** el primer caso de cada tipo. **Fase 2:** el resto.
   - Los estados son pendiente, con problemas, comprobada y ensamblada.
2. **Fase 1.** Lanza un agente por cada caso pendiente o con problemas de la fase 1, todos en paralelo, con un máximo de 10 por mensaje (`Agent`, `general-purpose`, el encargo de abajo).
   - Los casos de tipos distintos pueden generar a la vez el bloque de una madre común: `bin/model register` admite solo el primero, y el reglamento indica al otro agente que reutilice ese bloque.
   - Espera a que terminen **todos** los de la fase 1 antes de pasar a la fase 2: así esta encuentra los bloques en el catálogo y no los vuelve a generar.
3. **Fase 2.** Igual que la fase 1, con los casos pendientes o con problemas de la fase 2, en tandas de hasta 10 agentes. Lanza una tanda cuando termine la anterior.
4. **Tokens.** Cuando termina cada agente, registra su consumo con `bin/train batch usage RUN ID TRANSCRIPCIÓN`. `TRANSCRIPCIÓN` es el `output_file` que devuelve `Agent` al lanzarlo; no lo leas.
   - La orden suma el consumo de todas sus peticiones: entrada, escritura y lectura de caché, y salida.
   - El `subagent_tokens` de la notificación no sirve: es el contexto de la última petición, no el consumo.
   - Si un caso se repite, el último registro sustituye al anterior.
5. **Repaso:** `bin/train batch status RUN`.
   - Si queda algún caso con problemas, relanza **un** agente para él: el mismo encargo y los problemas de `status`.
   - Si un agente falla dos veces con el mismo caso, déjalo y anótalo para el informe.
6. **Ensamblar:** `bin/train batch assemble RUN`. Ensambla uno tras otro los casos comprobados, porque comparten `var/queue.jsonl`. **No** ensambles en paralelo.
7. **Informar** al usuario, de forma breve:
   - casos ensamblados y casos sin terminar;
   - bloques de categoría generados (`catalog/runtime/`, «no compilado»);
   - consumo de tokens por caso, por fase y en total (`status`);
   - las dudas del clasificador que se repitan.

   Si la ejecución pertenece a una tarea de `bin/pm`, deja el consumo y los hallazgos en la tarea con `bin/pm note`.

## Encargo de cada agente

Mismo encargo que en `/demand-model`, con la carpeta de la ejecución:

- eres el clasificador del motor de demanda;
- trabaja en `/home/gonwsl/projects/stratiav3/demand-engine` y sigue `classifier/rulebook.md`, y `catalog/DRAFTING.md` solo si falta un bloque;
- caso `ID`, con la URL (de `RUN/batch.json`) y la ficha congelada en `var/pages/ID.html`;
- escribe la salida en `RUN/ID.json` y los bloques que generes en `RUN/`;
- comprueba con `bin/model check RUN/ID.json` hasta que diga «correcto»;
- si `bin/model register` rechaza un bloque porque la categoría ya lo tiene, aplica el paso 3 del reglamento;
- no leas `cases/`, `var/runs/` (salvo tu salida y tus bloques), las salidas de otros casos ni `docs/`;
- no ejecutes `bin/model assemble` ni `bin/train`;
- devuelve en pocas líneas el nombre del modelo, los bloques generados y sus dudas principales.

No le pases resultados esperados, el tipo de la selección ni conclusiones tuyas o de otros agentes. El tipo es una aproximación previa a la captura; la clase la decide el clasificador.

## Qué no hacer

- No corregir a mano el catálogo, las reglas ni las salidas: se corrigen en el entrenamiento (`bin/train`).
- No inducir ni compilar (`bin/train induce` y `compile`): es otro paso del ciclo.
- No borrar ni rehacer `RUN/batch.json` para cambiar los casos: usa otra carpeta de ejecución.
