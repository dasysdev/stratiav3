# web-audit

Sistema de la **evaluación técnica** de los ámbitos Web y Web Schema.org (unidad: requisito técnico × ámbito): la referencia técnica y el auditado, que produce el expediente técnico de un sitio. Empezó por Web Schema.org; el perfil de Web (protocolo, documento y consumidor) es de [D-159](../docs/30-governance/decisions.md#d-159). Es **solo técnico**: la evaluación informativa (disponibilidad efectiva, AC, GSC) es de la auditoría GSC ([D-129](../docs/30-governance/decisions.md#d-129)).

- **Canon:** [evaluation-scopes](../docs/10-model/evaluation-scopes.md#requisitos-técnicos-generales): perfil de implementación, estados del requisito técnico y fuentes de los requisitos técnicos (D-129–D-133). Prevalece sobre todo lo de aquí.
- Es uno de los sistemas del proyecto: un directorio de primer nivel y un miembro del workspace de uv ([pyproject.toml](../pyproject.toml)).

## Módulos

| Módulo | Qué hace | Dónde |
|---|---|---|
| Referencias | Fuentes de la referencia técnica, congeladas por versión en [references](../references/README.md): el vocabulario Schema.org por release, en formato máquina, y los documentos publicados (páginas HTML con su texto, PDF y ficheros de datos). La versión que cita la referencia queda fijada. | `references/bin/refs` · `references/sources.json` · `references/var/` |
| Referencia técnica | Fichas de fuente con citas literales y requisitos técnicos ([D-133](../docs/30-governance/decisions.md#d-133)): una ficha por fuente, un fichero de requisitos por nivel del perfil y el registro de los retirados. Se crea y se mantiene con la skill `/web-reference` y se valida con `bin/reqs check`; `bin/reqs section` muestra el texto citable de una fuente. Formato: [reference/README.md](reference/README.md). | `bin/reqs` · `reference/cards/` · `reference/requirements/` |
| Fichas reales | Las del almacén común de [capture](../capture/README.md#almacén-de-fichas) ([D-150](../docs/30-governance/decisions.md#d-150)): el contraste de los requisitos técnicos (T-048). Una ficha nueva se captura con `capture/bin/pages fetch ID URL`, con un ID nuevo; su interpretación técnica queda aquí. | `capture/var/pages/` · `capture/bin/pages` |
| Auditado | El expediente técnico de un sitio (T-049): aplica cada requisito técnico a las páginas de una auditoría de capture y calcula la tasa de cumplimiento técnico ([D-166](../docs/30-governance/decisions.md#d-166)). Lo que pide juicio lo decide un agente con la skill `/web-audit`. Ver *Auditado*. | `bin/audit` · `src/web_audit/checks/` · `var/audits/` |

## Referencias

Las fuentes de la referencia técnica son las de [references](../references/README.md) cuyo `uses` incluye web-audit ([D-149](../docs/30-governance/decisions.md#d-149)): allí están su registro (`references/sources.json`), sus versiones congeladas, la versión fijada y el diff, y se descargan y se fijan con `references/bin/refs`. web-audit solo las interpreta: fichas de fuente y requisitos técnicos, en [reference/](reference/README.md).

- **Tipos de fuente** que usa: `schemaorg` (una release del vocabulario en formato máquina; la versión es la release, `30.1`, la que fija [D-130](../docs/30-governance/decisions.md#d-130)) y `document` (un documento publicado, versionado por la fecha de descarga). De una página HTML lo que cita una ficha es su texto (`text.md`): Markdown ligero, con el ancla de cada encabezado (`{#id}`) y una línea por fila de tabla. Los PDF y los ficheros de datos se guardan tal cual.
- **Versión fijada:** una ficha cita la fijada. Cambiarla (`references/bin/refs pin`) obliga a revisar las fichas y los requisitos que citan la anterior (`references/bin/refs diff`); `bin/reqs check` falla hasta entonces.
- **Idioma:** las páginas de Google se congelan en inglés, que es la versión original; las traducciones pueden ir con retraso.
- **Fuera del registro:** los validadores (Schema Markup Validator, Rich Results Test), que son aplicaciones y método de comprobación, y las skills de terceros, que no tienen autoridad ([D-132](../docs/30-governance/decisions.md#d-132)). `ref.gs1.org/voc/` es una aplicación JavaScript: se congela el fichero del vocabulario que carga.
- **Descargas:** puntuales y a petición, con un segundo entre documentos. El robots.txt de todos los orígenes las permite (comprobado el 2026-10-27; los del perfil de Web, el 2026-10-28).

## Auditado

Lee las páginas que capture congeló con `audit-es` para una auditoría ([D-167](../docs/30-governance/decisions.md#d-167); `capture/var/audits/AUDIT/`, la misma instantánea que la auditoría informativa) y las respuestas a las imágenes del marcado (`resources.json`), y escribe el expediente técnico en `var/audits/AUDIT/`. El método de cada requisito es el de la referencia; el código lo aplica y, si el método y el código discrepan, prevalece el método.

1. **Casos** ([D-161](../docs/30-governance/decisions.md#d-161)): un requisito `general` da un caso para el sitio; uno `particular`, un caso por página de la auditoría cuyo tipo está en `page_types`. Las páginas no localizadas no dan casos y se registran (D-167). Una página sin documento (un bloqueo, un 404) da NE en Web Schema.org; los requisitos de Web deciden con lo que haya de la respuesta.
2. **Extracción** (`site`, `html`, `jsonld`, `microdata`, `rdfa`, `graph`): el documento de la respuesta, sin JavaScript ([D-156](../docs/30-governance/decisions.md#d-156)), el marcado de las tres sintaxis como un solo grafo (los nodos con el mismo identificador son una entidad, también entre páginas en la vista general), robots.txt de cada origen y los sitemaps en sus formatos. Schema.org es la release fijada (30.1, `vocab`); el contexto de Schema.org, el congelado. Solo biblioteca estándar.
3. **Comprobaciones** (`checks/`): una por requisito, registrada por su id; las pruebas fallan si un requisito de la referencia no tiene la suya. La mayoría son primitivas sobre rutas del grafo (`markup`: presencia, cardinalidad, formato del valor, enumeración, condicionales, tipo del valor); las demás, funciones propias. Una comprobación devuelve el estado, la evidencia y, en NA y NE, su motivo.
4. **Pendientes:** si el método pide un juicio (un soft 404 con indicios de error, el nombre de un autor) o el contenido visible (si la página muestra variantes, un precio tachado o un precio por unidad), el caso queda `pendiente` con la pregunta. Los decide un agente con `/web-audit`, que escribe `judgments.json`; `bin/audit check` lo valida.
5. **Expediente** (`bin/audit finish`): `dossier.json` (cada caso con su estado, quién lo decidió y la evidencia, y las tasas) y `report.md`. La tasa es la de D-166 y D-169: por ámbito y vista, y en la particular por tipo de página con los casos requisito × página; satisfechos / evaluados, con evaluados = pertinentes − NA − NE; el mismo cálculo por naturaleza; cobertura = evaluados / (pertinentes − NA), que solo bajan las NE; por requisito, la proporción de páginas en que se satisface; y el resultado de cada página. Web y Web Schema.org no se suman.

- **Imágenes del marcado** (T-087): `bin/audit images AUDIT` extrae de todas las páginas las URL de imagen del marcado (image, logo, thumbnailUrl y el contentUrl, o el url, de cada ImageObject) y se las pasa a capture (`capture/bin/pages resources`, T-086). capture pide cada una con GET y registra el estado y las cabeceras, sin el cuerpo, y el robots.txt de cada host nuevo (un CDN). Se ejecuta antes de `run`.
  - **Rastreable** (ws-consumer/004, 185): no satisfecho si robots.txt de su host la bloquea a Googlebot-Image (o, sin grupo propio, a Googlebot o a `*`) o si la respuesta final no es 2xx. El logo (334) solo mira robots.txt.
  - **Indexable** (005, 186, 335): no satisfecho si la cabecera X-Robots-Tag de la respuesta lleva noindex o none para todos o para Googlebot (y Googlebot-Image en 005 y 186).
  - **NE:** una URL que capture no pidió, que no respondió o que no pudo pedir (robots.txt para nuestro bot, reserva TDM, 429, no http(s)), con su motivo. Si otra URL del caso no cumple, el caso es no satisfecho.
- **NE por falta de material:** las dimensiones, la relación de aspecto y el formato de las imágenes (ws-consumer/007–010, 333, 336) son NE: fuera de V1, no se descargan las imágenes. El DOM renderizado no existe con `audit-es`: lo que compara HTML servido y renderizado es NE.
- **Uso:** `web-audit/bin/audit images AUDIT` (`--list`: solo la lista) · `run AUDIT` · `pending AUDIT` · `text AUDIT PÁGINA` (el texto visible, para el agente) · `check AUDIT` · `finish AUDIT`. Lo normal es la skill `/web-audit`.

## Estructura

```
web-audit/
├── pyproject.toml        miembro del workspace (solo biblioteca estándar)
├── bin/reqs · bin/audit  envoltorios de línea de comandos (el código está en src/)
├── src/web_audit/        paquete Python: reqs (referencia); audit, site, html, jsonld, microdata,
│                         rdfa, graph, vocab y checks/ (auditado)
├── tests/                pruebas
└── reference/            referencia técnica: inventory.md, cards/ (fichas), requirements/
                          (requisitos por nivel), retired.json (retirados, con su motivo),
                          reports/ (informes de las pasadas); formato en su README
└── var/audits/AUDIT/     expediente técnico de cada auditoría (fuera de git)
```

## Qué entra en git

Todo lo de web-audit salvo `var/`: código, pruebas, `pyproject.toml` y `reference/` (fichas y requisitos técnicos). `var/` (los expedientes) es desechable y se rehace con `bin/audit run` mientras exista la auditoría de capture. Las fuentes congeladas y su versión fijada son de `references/var/`, desechable y fuera de git: si se pierden, las citas a una versión que no se recupere igual habrá que revisarlas (ver [references](../references/README.md#qué-entra-en-git)).

## Ejecución

- **`reqs`** y **`audit`** se ejecutan en el host (`web-audit/bin/reqs …`, `web-audit/bin/audit …`) y solo usan la biblioteca estándar, `references` y, `audit`, la lectura de capture. `audit images` llama a `capture/bin/pages resources`, que delega en el contenedor.
- **Pruebas:** `bin/run dev test web-audit/tests` (todas las del proyecto: `bin/run dev test`).
