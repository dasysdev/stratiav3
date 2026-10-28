# web-audit

Sistema de la **evaluación técnica** de los ámbitos Web y Web Schema.org (unidad: requisito técnico × ámbito). Empieza por Web Schema.org. Es **solo técnico**: la evaluación informativa (disponibilidad efectiva, AC, GSC) es de la auditoría GSC ([D-129](../docs/30-governance/decisions.md#d-129)).

- **Canon:** [evaluation-scopes](../docs/10-model/evaluation-scopes.md#requisitos-técnicos-generales): perfil de implementación, estados del requisito técnico y fuentes de los requisitos técnicos (D-129–D-133). Prevalece sobre todo lo de aquí.
- Es uno de los sistemas del proyecto: un directorio de primer nivel y un miembro del workspace de uv ([pyproject.toml](../pyproject.toml)).

## Módulos

| Módulo | Qué hace | Dónde |
|---|---|---|
| Referencias | Fuentes de la referencia técnica, congeladas por versión en [references](../references/README.md): el vocabulario Schema.org por release, en formato máquina, y los documentos publicados (páginas HTML con su texto, PDF y ficheros de datos). La versión que cita la referencia queda fijada. | `references/bin/refs` · `references/sources.json` · `references/var/` |
| Referencia técnica | Fichas de fuente con citas literales y requisitos técnicos ([D-133](../docs/30-governance/decisions.md#d-133)): una ficha por fuente y un fichero de requisitos por nivel del perfil. Se crea y se mantiene con la skill `/web-reference` y se valida con `bin/reqs check`; `bin/reqs section` muestra el texto citable de una fuente. Formato: [reference/README.md](reference/README.md). | `bin/reqs` · `reference/cards/` · `reference/requirements/` |
| Fichas reales | Las del almacén común de [capture](../capture/README.md#almacén-de-fichas) ([D-150](../docs/30-governance/decisions.md#d-150)), que comparte con demand-engine para evaluar la misma instantánea: el contraste de los requisitos técnicos (T-048) y, después, el auditado. Una ficha nueva se captura con `capture/bin/pages fetch ID URL`, con un ID nuevo; su interpretación técnica queda aquí. | `capture/var/pages/` · `capture/bin/pages` |
| Auditado | Más adelante (T-049). | — |

## Referencias

Las fuentes de la referencia técnica son las de [references](../references/README.md) cuyo `uses` incluye web-audit ([D-149](../docs/30-governance/decisions.md#d-149)): allí están su registro (`references/sources.json`), sus versiones congeladas, la versión fijada y el diff, y se descargan y se fijan con `references/bin/refs`. web-audit solo las interpreta: fichas de fuente y requisitos técnicos, en [reference/](reference/README.md).

- **Tipos de fuente** que usa: `schemaorg` (una release del vocabulario en formato máquina; la versión es la release, `30.1`, la que fija [D-130](../docs/30-governance/decisions.md#d-130)) y `document` (un documento publicado, versionado por la fecha de descarga). De una página HTML lo que cita una ficha es su texto (`text.md`): Markdown ligero, con el ancla de cada encabezado (`{#id}`) y una línea por fila de tabla. Los PDF y los ficheros de datos se guardan tal cual.
- **Versión fijada:** una ficha cita la fijada. Cambiarla (`references/bin/refs pin`) obliga a revisar las fichas y los requisitos que citan la anterior (`references/bin/refs diff`); `bin/reqs check` falla hasta entonces.
- **Idioma:** las páginas de Google se congelan en inglés, que es la versión original; las traducciones pueden ir con retraso.
- **Fuera del registro:** los validadores (Schema Markup Validator, Rich Results Test), que son aplicaciones y método de comprobación, y las skills de terceros, que no tienen autoridad ([D-132](../docs/30-governance/decisions.md#d-132)). `ref.gs1.org/voc/` es una aplicación JavaScript: se congela el fichero del vocabulario que carga.
- **Descargas:** puntuales y a petición, con un segundo entre documentos. El robots.txt de todos los orígenes las permite (comprobado el 2026-10-27).

## Estructura

```
web-audit/
├── pyproject.toml        miembro del workspace (solo biblioteca estándar)
├── bin/reqs              envoltorio de línea de comandos (el código está en src/)
├── src/web_audit/        paquete Python: reqs
├── tests/                pruebas
└── reference/            referencia técnica: inventory.md, cards/ (fichas), requirements/
                          (requisitos por nivel), reports/ (informes de las pasadas); formato en su README
```

## Qué entra en git

Todo lo de web-audit: código, pruebas, `pyproject.toml` y `reference/` (fichas y requisitos técnicos). Las fuentes congeladas y su versión fijada son de `references/var/`, desechable y fuera de git: si se pierden, las citas a una versión que no se recupere igual habrá que revisarlas (ver [references](../references/README.md#qué-entra-en-git)).

## Ejecución

- **`reqs`** se ejecuta en el host (`web-audit/bin/reqs …`) y solo usa la biblioteca estándar y `references`.
- **Pruebas:** `bin/run dev test web-audit/tests` (todas las del proyecto: `bin/run dev test`).
