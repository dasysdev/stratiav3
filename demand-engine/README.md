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
| Catálogo de bloques | Esqueleto determinista de los bloques de categoría, catálogo compilado (`catalog/cat/`), bloques generados en ejecución (`catalog/runtime/`), rasgos (`catalog/traits.json`) y reglas de importancia (`catalog/rules/`). | `bin/blocks` · `catalog/` |
| Clasificador | Reglamento operativo v2 (elige bloques, vota la importancia y genera lo que falte), casos de control con lo esperado y ejecuciones. | `classifier/` · `cases/` · `var/runs/` |
| Motor de demanda | Ejecución: bloques de una clase, registro de bloques generados, ensamblado del modelo (clave versionada, nombre, lo no compilado, cola). Entrenamiento: índice de rasgos, inducción de reglas por el árbol de Shopify, validación, compilación e informe de cada ciclo (D-045). Comando `/demand-model URL`. | `src/demand_engine/demand/` · `bin/model` · `bin/train` · `training/reports/` · `var/queue.jsonl` |
| Motor de captura | Compartido (D-046): Chrome real por CDP, legitimidad (robots.txt, reservas TDM) y parada ante desafíos. Captura por lotes a ritmo de lector o una página suelta (`taxo page fetch`). | `src/demand_engine/capture/` · `var/capture/` · [manual](src/demand_engine/capture/README.md) |
| MPIR (capa A) | Plan de observación, fichas de referente, inventario de recursos e ingesta manual, sobre el motor de captura. | `src/demand_engine/mpir/` · `bin/mpir` · `studies/` · `var/mpir/` · [manual](src/demand_engine/mpir/README.md) |

## Estructura

```
demand-engine/
├── pyproject.toml        dependencias del sistema (miembro del workspace)
├── bin/                  envoltorios de línea de comandos (el código está en src/)
├── src/demand_engine/    paquete Python: refs, taxo, pages, blocks, compare, catalog_review,
│                         demand/ (motor de demanda), capture/ (motor de captura) y mpir/
├── tests/                pruebas, por módulo (tests/tools/, tests/demand/, tests/capture/, tests/mpir/)
├── classifier/ · cases/  reglamento del clasificador y conjunto de control
├── catalog/              catálogo compilado por el entrenamiento (bloques, reglas, rasgos)
├── training/reports/     informe de cada ciclo de entrenamiento
├── studies/              estudios del MPIR: plan, fichas de referente e inventario
├── .env.example          variables de .env (las credenciales, solo en .env)
└── var/                  desechable: runs/, refs/, pages/, capture/, mpir/, queue.jsonl
```

## Qué entra en git

En git va **lo que gobierna el sistema y los resultados del entrenamiento**. Lo demás vive en `var/`, que es desechable y no tiene copia: git no es una copia de seguridad.

| En git | En `var/` (desechable) | Fuera de todo |
|---|---|---|
| Código, pruebas, `pyproject.toml` | `runs/`: salida de la ejecución (salidas del clasificador y modelos de cada caso), que son también entradas del entrenamiento | `.env` (credenciales) |
| `classifier/` · `cases/` | `queue.jsonl`: cola de lo usado sin compilar | |
| `catalog/`: bloques compilados y `runtime/` (la ejecución siguiente los reutiliza), `rules/importance.json` con su procedencia (ejecuciones y versiones de las referencias) y sus métricas de aceptación, `traits.json`, `empty.json`, `skeleton.json`, `gen.json`, `amazon-map.json` | `catalog/rules/importance.candidate.json` y `catalog/REVIEW.md` (pasos intermedios y salida, ignorados en su sitio) | |
| `training/reports/`: informe de cada ciclo | `refs/`: referencias descargadas y la versión fijada (`pins.json`); se regeneran con `refs fetch` | |
| `studies/`: lo que define el MPIR | `pages/`: fichas de los casos (`taxo page fetch`); `mpir/`: comprobaciones, estado, instantáneas y log; `capture/`: perfil de Chrome | |

Si `var/` se pierde, se regenera. No se lleva registro de los cambios de las referencias: lo que importa es qué versión usó cada entrenamiento (`refs` en `catalog/rules/importance.json`) y cada modelo de demanda (`engine.refs` en su `.model.json`). En una ficha que cambió al volver a descargarla puede hacer falta revisar el caso.

## Ejecución

- **`refs`, `taxo`, `blocks`, `model`, `train`, `catalog-review` y `compare`** solo usan la biblioteca estándar y se ejecutan en el host. `catalog-review` (revisión manual del catálogo) quedó sin uso con D-044. Credenciales de Amazon: en `.env`, fuera de git y de las imágenes.
- **`mpir` y `taxo page fetch`** usan el motor de captura y se ejecutan en el contenedor, porque necesitan Chrome: `bin/run dev up` y después `demand-engine/bin/mpir …`. `taxo page fetch` se lanza igual desde el host y delega en el contenedor.
- Cada herramienta de `bin/` es un envoltorio de nueve líneas que llama al `main()` de su módulo (`bin/catalog-review` → `catalog_review`). La lectura de las referencias fijadas está en un solo sitio, `refs` (sección «Reading»), y las fichas congeladas de los casos en `pages`.
- **Pruebas:** `bin/run dev test`.
