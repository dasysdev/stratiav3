# demand-engine

Sistema de **construcción del modelo de demanda** de stratia.cic. Determina la clase de estudio de un producto, compone su modelo de requisitos por bloques y reúne la evidencia de ecommerce referentes (MPIR).

- **Método:** [product-taxonomy](../docs/20-methods/product-taxonomy/README.md) y [mpir](../docs/20-methods/mpir/README.md).
- **Canon:** [demand-model](../docs/10-model/demand-model.md) y [study-class](../docs/10-model/study-class.md), que prevalecen sobre todo lo de aquí.

Es uno de los sistemas del proyecto. Cada sistema es un directorio de primer nivel y un miembro del workspace de uv ([pyproject.toml](../pyproject.toml)).

## Módulos

| Módulo | Qué hace | Dónde |
|---|---|---|
| Referencias | Material externo de la taxonomía (Shopify, Google, Amazon.es), congelado por versión. Las versiones usadas quedan en cada resultado del entrenamiento y en cada modelo. | `bin/refs` · `var/refs/` |
| Consulta | Categorías, atributos, PTD y páginas de producto congeladas. | `bin/taxo` · `var/pages/` |
| Catálogo de bloques | Esqueleto determinista de los bloques de categoría, catálogo compilado (`catalog/cat/`), bloques generados en ejecución (`catalog/runtime/`), rasgos (`catalog/traits.json`: vocabulario, propuestos y los elegidos por los votos), reglas de importancia y relevancia (`catalog/rules/importance.json`) e información resolutiva observada (`catalog/rules/resolving.json`). | `bin/blocks` · `catalog/` |
| Clasificador | Reglamento operativo v3 (elige bloques, vota la importancia y el rasgo, dice qué aportación de la información resolutiva es cada hecho declarado y genera lo que falte), casos de control con lo esperado y ejecuciones. | `classifier/` · `cases/` · `var/runs/` |
| Motor de demanda | Ejecución: bloques de una clase, registro de bloques generados, ensamblado del modelo (clave versionada, nombre, lo no compilado, cola). Entrenamiento: selección del catálogo de entrenamiento en tiendas reales ([criterio](training/selection/README.md)), índice de rasgos, clasificación por lotes con agentes de Claude Code (D-054), inducción de reglas por el árbol de Shopify, validación, compilación e informe de cada ciclo (D-045). Comandos `/demand-model URL` (un producto) y `/classify-batch SELECCIÓN RUN` (el catálogo de entrenamiento). | `src/demand_engine/demand/` · `bin/model` · `bin/train` · `training/selection/` · `training/reports/` · `var/queue.jsonl` |
| Motor de captura | Compartido (D-046): Chrome real por CDP, legitimidad (robots.txt, reservas TDM) y parada ante desafíos. Captura por lotes a ritmo de lector o una página suelta (`taxo page fetch`). | `src/demand_engine/capture/` · `var/capture/` · [manual](src/demand_engine/capture/README.md) |
| MPIR (capa A) | Aparcado ([D-095](../docs/30-governance/decisions.md#d-095)). Plan de observación, fichas de referente, inventario de recursos e ingesta manual, sobre el motor de captura. | `src/demand_engine/mpir/` · `bin/mpir` · `studies/` · `var/mpir/` · [manual](src/demand_engine/mpir/README.md) |
| Motor PAA | Preguntas de «Más preguntas» (People Also Ask) de google.es para un conjunto de semillas de una clase, con Chrome real a ritmo de persona y parada ante desafíos. Vía de construcción del modelo ([D-094](../docs/30-governance/decisions.md#d-094)), con excepción al robots.txt de Google para investigación y uso interno ([D-096](../docs/30-governance/decisions.md#d-096)). Clasificación de las preguntas con un agente (`/paa-classify`, reglamento `classifier/paa.md`): criterios de elección, regla C1–C4 y requisitos candidatos de origen «paa». | `src/demand_engine/paa/` · `bin/paa` · `paa/` · `classifier/paa.md` · `var/paa/` · [manual](src/demand_engine/paa/README.md) |

## Estructura

```
demand-engine/
├── pyproject.toml        dependencias del sistema (miembro del workspace)
├── bin/                  envoltorios de línea de comandos (el código está en src/)
├── src/demand_engine/    paquete Python: refs, taxo, pages, blocks, compare, catalog_review,
│                         demand/ (motor de demanda), capture/ (motor de captura), mpir/ y paa/
├── tests/                pruebas, por módulo (tests/tools/, tests/demand/, tests/capture/, tests/mpir/, tests/paa/)
├── classifier/ · cases/  reglamentos de los clasificadores y conjuntos de control (cases/paa/: lo esperado de PAA)
├── catalog/              catálogo compilado por el entrenamiento (bloques, reglas, rasgos)
├── training/selection/   selección del catálogo de entrenamiento: especificación y fichas elegidas
├── training/reports/     informe de cada ciclo de entrenamiento
├── studies/              estudios del MPIR: plan, fichas de referente e inventario
├── paa/                  conjuntos de semillas del motor PAA
├── .env.example          variables de .env (las credenciales, solo en .env)
└── var/                  desechable: runs/, refs/, pages/, capture/, mpir/, paa/, training/ (descubrimientos), queue.jsonl
```

## Qué entra en git

En git va **lo que gobierna el sistema y los resultados del entrenamiento**. Lo demás vive en `var/`, que es desechable y no tiene copia: git no es una copia de seguridad.

| En git | En `var/` (desechable) | Fuera de todo |
|---|---|---|
| Código, pruebas, `pyproject.toml` | `runs/`: salida de la ejecución (salidas del clasificador y modelos de cada caso), que son también entradas del entrenamiento | `.env` (credenciales) |
| `classifier/` · `cases/` | `queue.jsonl`: cola de lo usado sin compilar | |
| `catalog/`: bloques compilados y `runtime/` (la ejecución siguiente los reutiliza), `rules/importance.json` con su procedencia (ejecuciones y versiones de las referencias) y sus métricas de aceptación, `rules/resolving.json`, `traits.json`, `empty.json`, `skeleton.json`, `gen.json`, `amazon-map.json` | `catalog/rules/importance.candidate.json` y `catalog/REVIEW.md` (pasos intermedios y salida, ignorados en su sitio) | |
| `training/selection/` (especificación y selección) y `training/reports/` (informe de cada ciclo) | `refs/`: referencias descargadas y la versión fijada (`pins.json`); se regeneran con `refs fetch` | |
| `studies/`: lo que define el MPIR · `paa/`: los conjuntos de semillas del motor PAA | `pages/`: fichas de los casos (`taxo page fetch`); `mpir/`: comprobaciones, estado, instantáneas y log; `paa/`: estado, búsquedas, preguntas consolidadas y perfil de Chrome propio; `capture/`: perfil de Chrome; `training/`: descubrimientos de la selección (`train discover`) | |

Si `var/` se pierde, se regenera. No se lleva registro de los cambios de las referencias: lo que importa es qué versión usó cada entrenamiento (`refs` en `catalog/rules/importance.json`) y cada modelo de demanda (`engine.refs` en su `.model.json`). En una ficha que cambió al volver a descargarla puede hacer falta revisar el caso.

## Ejecución

- **`refs`, `taxo`, `blocks`, `model`, `train`, `catalog-review` y `compare`** solo usan la biblioteca estándar y se ejecutan en el host. `catalog-review` (revisión manual del catálogo) quedó sin uso con D-044. Credenciales de Amazon: en `.env`, fuera de git y de las imágenes.
- **`mpir`, `taxo page fetch`, `train discover` y `train capture`** usan el motor de captura, y **`paa`** su navegador (no su legitimidad); **`paa classify`**, no: se ejecuta en el host. Se ejecutan en el contenedor, porque necesitan Chrome: `bin/run dev up` y después `demand-engine/bin/mpir …` o `demand-engine/bin/paa …`. `taxo page fetch`, `train discover` y `train capture` se lanzan igual desde el host y delegan en el contenedor.
- **Clasificación por lotes** (`/classify-batch`, D-054): la sesión de Claude Code lanza los agentes y `train batch` lleva el lote en `var/runs/RUN/` (`batch.json`, el plan; `usage.jsonl`, los tokens de cada agente). Fase 1: un caso por tipo, que genera los bloques que falten; fase 2: el resto, en tandas de hasta 10 agentes. `model register` rechaza un bloque de una categoría que ya lo tiene, así que dos agentes no lo generan dos veces. El ensamblado va de uno en uno (`train batch assemble`), porque los casos comparten la cola.
- Cada herramienta de `bin/` es un envoltorio de nueve líneas que llama al `main()` de su módulo (`bin/catalog-review` → `catalog_review`). La lectura de las referencias fijadas está en un solo sitio, `refs` (sección «Reading»), y las fichas congeladas de los casos en `pages`.
- **Pruebas:** `bin/run dev test`.
