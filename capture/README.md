# capture

Sistema del **motor de captura y el almacén común de fichas congeladas** ([D-150](../docs/30-governance/decisions.md#d-150), que enmienda [D-046](../docs/30-governance/decisions.md#d-046) en dónde vive el motor). Todos los sistemas que evalúan una ficha (demand-engine, web-audit y, después, la auditoría) la leen del mismo almacén, para evaluar la misma instantánea.

- **La captura se comparte; su interpretación, no.** Lo que una ficha significa para un sistema queda en ese sistema: los requisitos y el modelo de demanda, en [demand-engine](../demand-engine/README.md); el contraste de los requisitos técnicos, en [web-audit](../web-audit/README.md).
- Es uno de los sistemas del proyecto: un directorio de primer nivel y un miembro del workspace de uv ([pyproject.toml](../pyproject.toml)). Depende de `websockets` (CDP); leer el almacén solo usa la biblioteca estándar.
- **Consumidores:** en demand-engine, taxo (la captura suelta, `taxo page fetch`, y la lectura de fichas), el entrenamiento (`train discover` y `train capture`), el MPIR y PAA (su navegador, no su legitimidad); web-audit, las fichas de su contraste. Las fichas de todos están aquí.

Captura páginas de ecommerce de dos formas:

- **Por lotes** (`crawl`): a ritmo de lector, con un sitio por ventana. Lo usan el MPIR y la captura del catálogo de entrenamiento (`demand-engine/bin/train capture`).
- **Una página suelta** (`once`): la usan `bin/pages fetch` y `demand-engine/bin/taxo page fetch` para congelar una ficha.

## Principio

Usa **un navegador de verdad, a ritmo de lector, y para ante cualquier control**:

- Chrome estable con ventana (sobre Xvfb o el escritorio), perfil persistente y control por CDP directo, como `stratia.rpa` (ADR-002).
- No usa `--headless` ni banderas de automatización, y nunca envía `Runtime.enable`. El user-agent es el real del navegador.
- Nada de curl ni urllib para las páginas.

**No hace:**

- resolver CAPTCHAs ni desafíos;
- rotar IP o proxies;
- aplicar parches antidetección;
- eludir logins.

Además de lo que dice el método («no se eludirán bloqueos ni medidas anti-bot»), la excepción de minería de textos y datos (art. 67 TRLPI) tiene dos condiciones:
- exige un acceso **legítimo**;
- no se aplica si el titular la ha **reservado por medios de lectura mecánica**.

Estas políticas son del motor y se aplican igual a todas las capturas ([D-042](../docs/30-governance/decisions.md#d-042), D-046).

## Legitimidad

1. **robots.txt según la RFC 9309.**
   - Se aplican los grupos de `stratia-cic` o, si ninguno lo nombra, los de `*`.
   - Gana la regla más específica, con `*` y `$`; ante un empate gana Allow.
   - Si responde 4xx, todo está permitido. Si responde 5xx o 429, o no responde, no se captura nada.
   - Que excluya a bots de IA (GPTBot, ClaudeBot…) se avisa para que lo revises, pero no nos aplica.
2. **Reserva TDM:** `/.well-known/tdmrep.json`, la cabecera `tdm-reservation` y la meta `tdm-reservation`. Si hay reserva, no se conserva ningún contenido.
3. **Portada** (solo en `check_site`, y si robots.txt la permite): desafío, antibot detectado y `noai` en la meta robots.

`access` hace el paso 1 y el `tdmrep.json` del paso 2, que es lo que necesita cualquier captura; una captura suelta solo hace eso. `check_site` hace los tres pasos y da un veredicto:

| Veredicto | Significado |
|---|---|
| `ok` | Se puede capturar. |
| `reserved` | Hay reserva TDM. |
| `blocked` | Desafío o 403/429. |
| `unreachable` | robots.txt inaccesible. |

## Ritmo

**Por lotes** (`crawl`): cada sitio tiene su ventana y su hilo, y los sitios van en paralelo. Los valores son los de `capture.pacing.DEFAULTS`; el MPIR los toma de `pacing` en su `plan.json`.

| Parámetro | Por defecto |
|---|---|
| Permanencia en la página (incluye el desplazamiento) | 8–30 s |
| Pausa entre páginas | 20–60 s, más el `Crawl-delay` si es mayor |
| Pausa larga | 2–5 min cada 15–25 páginas |
| Tope diario por sitio | 150 visitas |
| Horario | 9–21 h, Europe/Madrid |
| Desplazamiento (`scroll`) | Sí. Con `false`, la visita guarda la primera carga, sin desplazamiento ni permanencia (catálogo de entrenamiento, D-053) |

Las duraciones tienden al límite inferior: la mayoría son cortas y unas pocas, largas. El desplazamiento se hace con la rueda del ratón, lo que carga el contenido diferido. Unas 25 páginas por sitio llevan una media hora.

**Una página suelta** (`once`): sin permanencia ni pausas. Solo se recorre la página con la rueda durante unos 8 s, para que cargue lo diferido. Desde el host tarda unos 15 s, contando el arranque de Chrome.

## Ante un bloqueo

Si aparece un 403/429 o una página de desafío (Cloudflare, Akamai, DataDome, PerimeterX, Imperva), la visita queda como `blocked` y se guarda la evidencia.

- Un desafío no interactivo («Just a moment») tiene 20 s para resolverse solo en el navegador, sin tocarlo.
- En un lote, ese sitio se para. Qué se hace después lo decide quien llama: el MPIR, por ejemplo, reintenta una sola vez pasadas 6 h.

## Qué se conserva

Cada visita deja su instantánea en el directorio que le da quien llama. Ese directorio es siempre nuevo y nunca se sobrescribe:

| Fichero | Contenido |
|---|---|
| `meta.json` | URL pedida y final, redirecciones, estado HTTP y cabeceras, navegador, acciones realizadas, resultado y sha256 de cada fichero. |
| `response.html.gz` | El documento tal como lo envió el servidor. |
| `dom.html.gz` | El DOM tras leer la página, con las *shadow roots* serializadas. La raíz de cada bloque oculto (desplegable cerrado, acordeón plegado, `display:none`) lleva `data-capture-hidden="1"`. |
| `page.mhtml.gz` | La página con sus recursos y marcos. |
| `robots.txt` · `tdmrep.json` | Evidencia de la legitimidad (captura suelta; en el MPIR va con la comprobación del referente). |

Solo se guarda contenido si la página no es un desafío, un error o una reserva TDM. Las negativas por robots.txt o por reserva también dejan su `meta.json`. No hay capturas de pantalla ([D-042](../docs/30-governance/decisions.md#d-042)).

**Resultados de una visita:**

| Resultado | Significado |
|---|---|
| `captured` | Capturada. |
| `blocked` | Bloqueada por un desafío o un 403/429. |
| `failed` | No recuperada por un error. |
| `gone` | No existe (404/410). |
| `disallowed` | Excluida por robots.txt. |
| `reserved` | Reserva TDM: no se conserva. |

## Almacén de fichas

`capture.pages` guarda las fichas congeladas en `var/pages/`, una por ID:

| Fichero | Contenido |
|---|---|
| `ID.html` | El DOM de la instantánea (renderizado, o de la primera carga en el entrenamiento). |
| `ID.json` | `url`, `fetched_at`, tamaño y sha256 del DOM, método (`chrome-cdp`), contenido, URL final, estado HTTP, user-agent y `snapshot`: la ruta de la instantánea (`var/pages/ID/AAAAMMDDTHHMMSS`, relativa a `capture/`). Quien congela puede añadir campos propios (el entrenamiento, `selection` y `category`). |
| `ID/<instante>/` | Cada intento de captura de ese ID, con su instantánea (ver *Qué se conserva*). |

- **Una ficha congelada nunca se sustituye.** `fetch` y `freeze` rechazan un ID que ya tiene ficha (`ID.html` o `ID.json`); la captura nueva del mismo producto lleva otro ID. `fetch` lo comprueba antes de visitar, y la escritura es exclusiva.
- Un intento rechazado o bloqueado solo deja su instantánea, sin ficha: el ID sigue libre y se puede reintentar.
- **ID:** kebab-case (minúsculas, dígitos y guiones), porque nombra ficheros.
- `fetch(ID, URL)` es la captura suelta y su congelación; `freeze(ID, URL, carpeta, meta)` congela una instantánea ya capturada (la usa la captura por lotes del entrenamiento).
- `read(ID)` y `page_path(ID)` leen la ficha. **Lectores de página**, sobre el HTML leído: `text_lines` (las líneas de texto, sin scripts ni estilos), `json_ld` (los bloques JSON-LD que se pueden leer) y `walk` (los nodos de un documento JSON-LD, siguiendo `@graph`, `mainEntity`, `itemListElement` y `hasVariant`).
- `engine_available()` dice si se puede capturar aquí (websockets y Chrome: en el contenedor sí, en el host no).

## Uso

`capture/bin/pages fetch ID URL`: congela una ficha suelta. Desde el host, delega en el contenedor (`bin/run dev up` si no está levantado); un ID ya ocupado se rechaza en el host, sin lanzar nada.

## Módulos

| Módulo | Qué hace |
|---|---|
| `browser` · `cdp` | Chrome: arranque o conexión al que ya corre (un Chrome y un perfil por contenedor, en `var/`), ventanas, lectura de la página y diagnóstico (`signals`). |
| `robots` · `tdm` · `detect` · `legitimacy` | Legitimidad, desafíos y antibot. |
| `pacing` · `crawl` | Ritmo de lector y lotes: un hilo por sitio (`SiteRun`). Quien llama pone los elementos, dónde va cada instantánea y qué hace con cada resultado. |
| `visit` · `once` · `files` | Una visita y su instantánea, la captura suelta, y la escritura y lectura de ficheros. |
| `sitemaps` | Descubrimiento de URL en los sitemaps, desde la ventana del propio sitio. |
| `pages` · `cli` | El almacén de fichas y sus lectores, y la línea de órdenes (`bin/pages`). |

## Configuración

| Variable (`.env`) | Valores |
|---|---|
| `CAPTURE_DISPLAY` | `:99` Xvfb (por defecto) · `:0` escritorio del host (WSLg), para ver las ventanas |
| `CAPTURE_DISABLE_GPU` | `1` por defecto en el contenedor |
| `CAPTURE_CDP_PORT` · `CAPTURE_PROFILE` | Puerto y perfil de Chrome (por defecto, 9223 y `capture/var/chrome-profile`; el registro de Chrome, en `capture/var/chrome.log`) |

**Pendiente de la sonda (T-014):** en el contenedor no hay GPU y Chrome bloquea WebGL (`webgl: null` en `demand-engine/bin/mpir browser`), lo que es una señal delatora. La alternativa es que el motor controle el Chrome del host. Se decidirá con datos.

## Estructura

```
capture/
├── pyproject.toml          miembro del workspace (websockets)
├── bin/pages               envoltorio de línea de órdenes (el código está en src/)
├── src/capture/            el motor (browser, cdp, robots, tdm, detect, legitimacy, pacing, crawl,
│                           visit, once, files, sitemaps), el almacén (pages) y cli
├── tests/                  pruebas
└── var/                    desechable: pages/ (las fichas y sus instantáneas) y el perfil de Chrome
```

## Qué entra en git

En git va **lo que gobierna el sistema**: código y pruebas. `var/` es desechable y no tiene copia; git no es una copia de seguridad. Una ficha perdida no se recupera igual: una captura nueva da otra instantánea, con otro ID, y lo construido sobre la perdida (casos, modelos, contrastes) habrá que revisarlo.

## Pruebas

`bin/run dev test capture/tests` (todas las del proyecto: `bin/run dev test`): robots.txt, desafíos, ritmo y reservas; el almacén (congelar, leer, el rechazo de un ID existente y los ID no válidos); y, con Chrome, `pages fetch` de extremo a extremo contra un servidor local, incluidas una URL que robots.txt excluye y la repetición de un ID.
