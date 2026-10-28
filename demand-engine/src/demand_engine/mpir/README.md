# MPIR: capa A

Captura recursos de ecommerce referentes para el [MPIR](../../../../docs/20-methods/mpir/README.md): la capa **A** (corpus de recursos originales) de su [arquitectura](../../../../docs/20-methods/mpir/concepts-architecture.md#arquitectura-de-información). La estructuración (capa B) es T-015.

Aquí está lo propio del MPIR: el plan de observación, las fichas de referente, el inventario de recursos y la ingesta manual. La captura la hace el [motor de captura](../../../../capture/README.md) compartido. Su principio, la legitimidad, el ritmo, lo que hace ante un bloqueo y los ficheros de cada instantánea están en su README.

## Uso

Módulo de [demand-engine](../../../README.md). Todo se ejecuta dentro del contenedor (`bin/run dev up`); `demand-engine/bin/mpir` lanza `python -m demand_engine.mpir` en él.

```bash
demand-engine/bin/mpir study new ropa-de-cama-2026-10 --class "Ropa de cama: sábanas y fundas nórdicas"
demand-engine/bin/mpir site add tienda https://www.tienda.es --type especialista --reason "…"
demand-engine/bin/mpir site check tienda                         # legitimidad; veredicto en la ficha
demand-engine/bin/mpir discover tienda --match '/sabanas|/fundas' --limit 300
demand-engine/bin/mpir add tienda URL… --profile product --segment invierno --reason "…"
demand-engine/bin/mpir capture                                   # todos los referentes en paralelo
demand-engine/bin/mpir status
demand-engine/bin/mpir ingest tienda URL demand-engine/var/mpir/inbox/pagina.mhtml   # página guardada a mano
demand-engine/bin/mpir browser                                   # user-agent y señales del Chrome
```

Con más de un estudio, se indica cuál con `-s ID` o con `MPIR_STUDY`. `demand-engine/bin/mpir --help` lista los comandos.

## Lo que añade el MPIR al motor

- **Comprobación del referente** (`site check`): la del motor, guardada en la ficha, más un aviso si las condiciones de uso no están revisadas (`terms_reviewed`, que marcas tú).
- **Para capturar** hace falta una comprobación `ok` de menos de 7 días (`check_max_age_days` en el plan).
- **El ritmo** sale de `pacing` en `plan.json`.
- **Ante un bloqueo** se para el referente.
  - Pasadas 6 h (`block_retry_hours`) se intenta una vez más.
  - Tras un segundo bloqueo, el referente queda parado hasta que lo revises (`site unblock`).
  - La alternativa es que guardes tú la página con tu navegador y la incorpores con `ingest`.

## Ficheros

Lo que se define va en git, en `demand-engine/studies/<estudio>/`:

| Ruta | Contenido |
|---|---|
| `plan.json` | Plan de observación: clase, segmentos, perfiles, matriz de cobertura y ritmo. |
| `sites/<referente>.json` | Ficha de selección: tipo, motivo, grupo editorial, sesgos, condiciones de uso revisadas. |
| `resources.json` | Inventario: qué recursos se capturan, con qué perfil y segmento, y por qué. |

Lo que produce el motor es desechable, en `demand-engine/var/mpir/studies/<estudio>/`:

| Ruta | Contenido |
|---|---|
| `site-state/<referente>.json` | Comprobaciones y bloqueos del referente. |
| `resource-state.json` | Estado, instantáneas y última visita de cada recurso. |
| `checks/<referente>/<fecha>/` | Evidencia de cada comprobación (`robots.txt`, `tdmrep.json`). |
| `snapshots/<referente>/<recurso>/<fecha>/` | Instantánea de cada visita (formato del motor). |
| `discovery/<referente>-<fecha>.json` | URL candidatas de los sitemaps. |
| `log.jsonl` | Una línea por visita, comprobación y cambio. |

`mpir/store.py` une las dos mitades: una ficha o un recurso se leen y escriben completos.

**Estados de un recurso:** `pending` (no inspeccionado) o el resultado de su última visita (`captured`, `blocked`, `failed`, `gone`, `disallowed` o `reserved`; ver el motor).

## Pruebas

`tests/mpir/`: plan, inventario e ingesta manual, y la prueba de extremo a extremo (comprobación, descubrimiento y captura en paralelo de dos referentes).
