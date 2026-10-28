# web-audit

Sistema de la **evaluación técnica** de los ámbitos Web y Web Schema.org (unidad: requisito técnico × ámbito). Empieza por Web Schema.org. Es **solo técnico**: la evaluación informativa (disponibilidad efectiva, AC, GSC) es de la auditoría GSC ([D-129](../docs/30-governance/decisions.md#d-129)).

- **Canon:** [evaluation-scopes](../docs/10-model/evaluation-scopes.md#requisitos-técnicos-generales): perfil de implementación, estados del requisito técnico y fuentes de los requisitos técnicos (D-129–D-133). Prevalece sobre todo lo de aquí.
- Es uno de los sistemas del proyecto: un directorio de primer nivel y un miembro del workspace de uv ([pyproject.toml](../pyproject.toml)).

## Módulos

| Módulo | Qué hace | Dónde |
|---|---|---|
| Referencias | Fuentes de la referencia técnica, congeladas por versión: el vocabulario Schema.org por release, en formato máquina, y los documentos publicados (páginas HTML con su texto, PDF y ficheros de datos). La versión que cita la referencia queda fijada. | `bin/refs` · `reference/sources.json` · `var/refs/` |
| Referencia técnica | Fichas de fuente con citas literales y requisitos técnicos ([D-133](../docs/30-governance/decisions.md#d-133)): una ficha por fuente y un fichero de requisitos por nivel del perfil. Se crea y se mantiene con la skill `/web-reference` y se valida con `bin/reqs check`; `bin/reqs section` muestra el texto citable de una fuente. Formato: [reference/README.md](reference/README.md). | `bin/reqs` · `reference/cards/` · `reference/requirements/` |
| Auditado | Más adelante (T-049). | — |

## Referencias

`web-audit/bin/refs status | check | fetch | diff | pin` (`--help`). Solo usa la biblioteca estándar y se ejecuta en el host.

- **Registro:** [reference/sources.json](reference/sources.json), una entrada por fuente: `id` (kebab-case; es el que nombra una cita), `kind`, `title`, `publisher` y `url`. Opcionales: `inventory` (código en el inventario de partida) y `note`.
- **Tipos de fuente** (`kind`):
  - `schemaorg`: una release del vocabulario (GitHub `schemaorg/schemaorg`, `data/releases/<versión>/`). Se guardan el JSON-LD vigente, el JSON-LD con los términos retirados (ático), los CSV de tipos y propiedades y el contexto JSON-LD. Cada fichero se comprueba con su sha de git. La versión es la release (`30.1`, la que fija [D-130](../docs/30-governance/decisions.md#d-130)).
  - `document`: un documento publicado, versionado por la fecha de descarga. Una página HTML se guarda tal cual (`page.html`) y con su texto (`text.md`), que es lo que cita una ficha. El texto es Markdown ligero, con el ancla de cada encabezado (`{#id}`) y una línea por fila de tabla. La página cuenta por su texto: un cambio solo de marcado no crea versión. Los PDF y los ficheros de datos se guardan tal cual.
- **Versiones:** `var/refs/<fuente>/<versión>/`, con sus ficheros y un `MANIFEST.json`: origen, tamaño, sha256, fecha y, si la página la declara, su marca de versión («Last updated» de Google, «Schema.org V30.1», «This version» del W3C). Las versiones no se sobrescriben, y una descarga igual a la última se descarta.
- **Versión fijada:** `var/refs/pins.json`. La primera versión de una fuente se fija sola. Después solo la cambia `refs pin`, porque obliga a revisar las fichas y los requisitos que citan la anterior (`refs diff`).
- **Idioma:** las páginas de Google se congelan en inglés, que es la versión original; las traducciones pueden ir con retraso.
- **Fuera del registro:** los validadores (Schema Markup Validator, Rich Results Test), que son aplicaciones y método de comprobación, y las skills de terceros, que no tienen autoridad ([D-132](../docs/30-governance/decisions.md#d-132)). `ref.gs1.org/voc/` es una aplicación JavaScript: se congela el fichero del vocabulario que carga.
- **Descargas:** puntuales y a petición, como las de `demand-engine/bin/refs`, con un segundo entre documentos. El robots.txt de todos los orígenes las permite (comprobado el 2026-10-27).

## Estructura

```
web-audit/
├── pyproject.toml        miembro del workspace (solo biblioteca estándar)
├── bin/refs, bin/reqs    envoltorios de línea de comandos (el código está en src/)
├── src/web_audit/        paquete Python: refs, reqs
├── tests/                pruebas
├── reference/            referencia técnica: sources.json (registro de fuentes), inventory.md,
│                         cards/ (fichas), requirements/ (requisitos por nivel), reports/
│                         (informes de las pasadas); formato en su README
└── var/                  desechable: refs/ (fuentes congeladas y pins.json)
```

## Qué entra en git

En git va **lo que gobierna el sistema**. Lo demás vive en `var/`, que es desechable y no tiene copia: git no es una copia de seguridad.

| En git | En `var/` (desechable) |
|---|---|
| Código, pruebas, `pyproject.toml` | `refs/`: fuentes descargadas y la versión fijada (`pins.json`); se regeneran con `refs fetch` |
| `reference/`: registro de fuentes, fichas y requisitos técnicos | |

Si `var/` se pierde, se regenera, pero la versión de un documento lleva la fecha de su descarga: la nueva tendrá otra fecha, y si la página cambió en origen, otro texto. Las citas a la versión perdida habrá que revisarlas. La release de Schema.org sí se recupera igual.

## Ejecución

- **`refs` y `reqs`** se ejecutan en el host: `web-audit/bin/refs …`, `web-audit/bin/reqs …`.
- **Pruebas:** `bin/run dev test web-audit/tests` (todas las del proyecto: `bin/run dev test`).
