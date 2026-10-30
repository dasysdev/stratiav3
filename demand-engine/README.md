# demand-engine

Sistema de **construcción del modelo de demanda** de stratia.cic. Determina la clase de estudio de un producto, compone su modelo de requisitos por bloques y reúne la evidencia de ecommerce referentes (MPIR).

- **Método:** [product-taxonomy](../docs/20-methods/product-taxonomy/README.md) y [mpir](../docs/20-methods/mpir/README.md).
- **Canon:** [demand-model](../docs/10-model/demand-model.md) y [study-class](../docs/10-model/study-class.md), que prevalecen sobre todo lo de aquí.

Es uno de los sistemas del proyecto. Cada sistema es un directorio de primer nivel y un miembro del workspace de uv ([pyproject.toml](../pyproject.toml)).

## Módulos

| Módulo | Qué hace | Dónde |
|---|---|---|
| Referencias | Material externo de la taxonomía (Shopify, Google, Amazon.es): las fuentes cuyo `uses` incluye demand-engine, custodiadas y leídas en [references](../references/README.md) ([D-149](../docs/30-governance/decisions.md#d-149)). Las versiones usadas quedan en cada resultado del entrenamiento y en cada modelo. | `references/bin/refs` · `references/var/` |
| Consulta | Categorías, atributos, PTD y páginas de producto congeladas (las del almacén de [capture](../capture/README.md#almacén-de-fichas)). | `bin/taxo` · `capture/var/pages/` |
| Catálogo de bloques | Esqueleto determinista de los bloques de categoría, catálogo compilado (`catalog/cat/`), bloques generados en ejecución (`catalog/runtime/`), rasgos (`catalog/traits.json`: vocabulario, propuestos y los elegidos por los votos), reglas de importancia y relevancia (`catalog/rules/importance.json`) e información resolutiva observada (`catalog/rules/resolving.json`). Propiedades que Google Search recomienda sin exigir como apoyo «referencias», sin ámbito ([D-155](../docs/30-governance/decisions.md#d-155)): las de la capa general, en sus fuentes (`gen.json`); las de los atributos de categoría y los candidatos, en `catalog/google-search.json`, que lleva además el contrato con los retirados de web-audit. Fichas de ámbito (`catalog/scopes/`: Web y Web Schema.org): pertinencia por excepción y localización. | `bin/blocks` · `catalog/` |
| Clasificador | Reglamento operativo v3 (elige bloques, vota la importancia y el rasgo, dice qué aportación de la información resolutiva es cada hecho declarado y genera lo que falte), casos de control con lo esperado y ejecuciones. | `classifier/` · `cases/` · `var/runs/` |
| Motor de demanda | Ejecución: bloques de una clase, registro de bloques generados, ensamblado del modelo (clave versionada, nombre, lo no compilado, cola) y su composición con la ficha de cada ámbito (`model scope`: unidades RI × ámbito con su NA y el perfil del RI que sale del modelo, D-155 y D-177: componentes y aportaciones de la información resolutiva; descripción entera en objeto, alcance y casos frontera; pistas de valoración resueltas al ensamblar, D-135; y localización como expresiones de ejemplo; lo que falta queda en `pendientes_de_definicion`, sin completar). Entrenamiento: selección del catálogo de entrenamiento en tiendas reales ([criterio](training/selection/README.md)), índice de rasgos, clasificación por lotes con agentes de Claude Code (D-054), inducción de reglas por el árbol de Shopify, validación, compilación e informe de cada ciclo (D-045). Comandos `/demand-model URL` (un producto) y `/classify-batch SELECCIÓN RUN` (el catálogo de entrenamiento). | `src/demand_engine/demand/` · `bin/model` · `bin/train` · `training/selection/` · `training/reports/` · `var/queue.jsonl` |
| Motor de captura | Sistema propio, compartido ([D-150](../docs/30-governance/decisions.md#d-150)): Chrome real por CDP, legitimidad (robots.txt, reservas TDM) y parada ante desafíos. Captura por lotes a ritmo de lector o una página suelta (`taxo page fetch`), y guarda las fichas congeladas; un ID que ya tiene ficha se rechaza. | `capture/` · `capture/var/` · [manual](../capture/README.md) |
| MPIR (capa A) | Aparcado ([D-095](../docs/30-governance/decisions.md#d-095)). Plan de observación, fichas de referente, inventario de recursos e ingesta manual, sobre el motor de captura. | `src/demand_engine/mpir/` · `bin/mpir` · `studies/` · `var/mpir/` · [manual](src/demand_engine/mpir/README.md) |
| Motor PAA | Preguntas de «Más preguntas» (People Also Ask) de google.es para un conjunto de semillas de una clase, con Chrome real a ritmo de persona y parada ante desafíos. Vía de construcción del modelo ([D-094](../docs/30-governance/decisions.md#d-094)), con excepción al robots.txt de Google para investigación y uso interno ([D-096](../docs/30-governance/decisions.md#d-096)). Clasificación de las preguntas con un agente (`/paa-classify`, reglamento `classifier/paa.md`): criterios de elección, regla C1–C4 y requisitos candidatos de origen «paa». | `src/demand_engine/paa/` · `bin/paa` · `paa/` · `classifier/paa.md` · `var/paa/` · [manual](src/demand_engine/paa/README.md) |

## Estructura

```
demand-engine/
├── pyproject.toml        dependencias del sistema (miembro del workspace)
├── bin/                  envoltorios de línea de comandos (el código está en src/)
├── src/demand_engine/    paquete Python: taxo, blocks, compare, catalog_review,
│                         demand/ (motor de demanda), mpir/ y paa/
├── tests/                pruebas, por módulo (tests/tools/, tests/demand/, tests/mpir/, tests/paa/)
├── classifier/ · cases/  reglamentos de los clasificadores y conjuntos de control (cases/paa/: lo esperado de PAA)
├── catalog/              catálogo compilado por el entrenamiento (bloques, reglas, rasgos)
├── training/selection/   selección del catálogo de entrenamiento: especificación y fichas elegidas
├── training/reports/     informe de cada ciclo de entrenamiento
├── studies/              estudios del MPIR: plan, fichas de referente e inventario
├── paa/                  conjuntos de semillas del motor PAA
└── var/                  desechable: runs/, mpir/, paa/, training/ (descubrimientos y registro de la captura), queue.jsonl
```

## Qué entra en git

En git va **lo que gobierna el sistema y los resultados del entrenamiento**. Lo demás vive en `var/`, que es desechable y no tiene copia: git no es una copia de seguridad.

| En git | En `var/` (desechable) |
|---|---|
| Código, pruebas, `pyproject.toml` | `runs/`: salida de la ejecución (salidas del clasificador y modelos de cada caso), que son también entradas del entrenamiento |
| `classifier/` · `cases/` | `queue.jsonl`: cola de lo usado sin compilar |
| `catalog/`: bloques compilados y `runtime/` (la ejecución siguiente los reutiliza), `rules/importance.json` con su procedencia (ejecuciones y versiones de las referencias) y sus métricas de aceptación, `rules/resolving.json`, `traits.json`, `empty.json`, `skeleton.json`, `gen.json`, `amazon-map.json`, `google-search.json` y las fichas de ámbito (`scopes/`) | `catalog/rules/importance.candidate.json` y `catalog/REVIEW.md` (pasos intermedios y salida, ignorados en su sitio) |
| `training/selection/` (especificación y selección) y `training/reports/` (informe de cada ciclo) | |
| `studies/`: lo que define el MPIR · `paa/`: los conjuntos de semillas del motor PAA | `mpir/`: comprobaciones, estado, instantáneas y log; `paa/`: estado, búsquedas, preguntas consolidadas y perfil de Chrome propio; `training/`: descubrimientos de la selección (`train discover`) y registro de su captura (`train capture`) |

Si `var/` se pierde, se regenera. Las fichas congeladas y el perfil de Chrome del motor viven en `capture/var/` (ver [capture](../capture/README.md#qué-entra-en-git)). Las referencias y su versión fijada viven en `references/var/` (ver [references](../references/README.md#qué-entra-en-git)). No se lleva registro de los cambios de las referencias: lo que importa es qué versión usó cada entrenamiento (`refs` en `catalog/rules/importance.json`) y cada modelo de demanda (`engine.refs` en su `.model.json`). Una ficha congelada no cambia: la captura nueva de un producto lleva otro ID, y el caso que pase a usarla puede necesitar revisión. Las citas del catálogo nombran su versión (`fuente:…@versión`; un atributo o una propiedad sin versión toma la de `refs` de su bloque): cuando otro sistema cambia una versión fijada (`refs pin`), `bin/model refs` lista las que han quedado en la anterior, y las de una tabla de propiedades de Google Search (`google-search-merchant-listing:Product.audience@2026-10-27`) han de existir en su versión. Las citas de normas (`ley:TRLGDCU-97.1.e@2026-02-28`) nombran la norma por su código (`cite` en el registro de references) y han de resolver a su artículo y apartado en esa versión. Las citas a fuentes sin registro se informan aparte.

## Ejecución

- **`taxo`, `blocks`, `model`, `train`, `catalog-review` y `compare`** solo usan la biblioteca estándar, `references` y la parte de `capture` que no necesita Chrome (leer el almacén), y se ejecutan en el host. `catalog-review` (revisión manual del catálogo) quedó sin uso con D-044. Descargar o fijar una versión de las referencias: `references/bin/refs`.
- **`mpir`, `taxo page fetch`, `train discover` y `train capture`** usan el motor de [capture](../capture/README.md), y **`paa`** su navegador (no su legitimidad); **`paa classify`**, no: se ejecuta en el host. Se ejecutan en el contenedor, porque necesitan Chrome: `bin/run dev up` y después `demand-engine/bin/mpir …` o `demand-engine/bin/paa …`. `taxo page fetch`, `train discover` y `train capture` se lanzan igual desde el host y delegan en el contenedor; `taxo page fetch` rechaza en el host, sin lanzar nada, un ID que ya tiene ficha.
- **Clasificación por lotes** (`/classify-batch`, D-054): la sesión de Claude Code lanza los agentes y `train batch` lleva el lote en `var/runs/RUN/` (`batch.json`, el plan; `usage.jsonl`, los tokens de cada agente). Fase 1: un caso por tipo, que genera los bloques que falten; fase 2: el resto, en tandas de hasta 10 agentes. `model register` rechaza un bloque de una categoría que ya lo tiene, así que dos agentes no lo generan dos veces. El ensamblado va de uno en uno (`train batch assemble`), porque los casos comparten la cola.
- Cada herramienta de `bin/` es un envoltorio de diez líneas que pone en la ruta `src/` y `references/src/` (`taxo` y `train`, también `capture/src/`) y llama al `main()` de su módulo (`bin/catalog-review` → `catalog_review`). La lectura de las referencias fijadas es la de `references.read`; las versiones que registra un resultado, `references.store.pins("demand-engine")`; las fichas congeladas, `capture.pages`.
- **Pruebas:** `bin/run dev test`.
