# capture

Sistema del **motor de captura y el almacén común de fichas congeladas** ([D-150](../docs/30-governance/decisions.md#d-150), que enmienda [D-046](../docs/30-governance/decisions.md#d-046) en dónde vive el motor). Todos los sistemas que evalúan una ficha (demand-engine, web-audit y, después, la auditoría) la leen del mismo almacén, para evaluar la misma instantánea.

- **La captura se comparte; su interpretación, no.** Lo que una ficha significa para un sistema queda en ese sistema: los requisitos y el modelo de demanda, en [demand-engine](../demand-engine/README.md); el contraste de los requisitos técnicos, en [web-audit](../web-audit/README.md).
- Es uno de los sistemas del proyecto: un directorio de primer nivel y un miembro del workspace de uv ([pyproject.toml](../pyproject.toml)). Depende de `websockets` (CDP); leer el almacén solo usa la biblioteca estándar.
- **Consumidores:** en demand-engine, taxo (la captura suelta, `taxo page fetch`, y la lectura de fichas), el entrenamiento (`train discover` y `train capture`), el MPIR y PAA (su navegador, no su legitimidad); web-audit, las fichas de su contraste. Las fichas de todos están aquí.

Captura páginas de ecommerce de dos formas:

- **Por lotes** (`crawl`): a ritmo de lector, con un sitio por ventana. Lo usan el MPIR y la captura del catálogo de entrenamiento (`demand-engine/bin/train capture`).
- **Una página suelta** (`once`): la usan `bin/pages fetch` y `demand-engine/bin/taxo page fetch` para congelar una ficha.
- **Las páginas de una auditoría** (`audit`, [D-167](../docs/30-governance/decisions.md#d-167)): `bin/pages audit`, siempre con `audit-es` (ver *Páginas de una auditoría*).

Las dos formas leen la página con el **perfil de captura** que elige quien la pide (ver *Perfiles de captura*).

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

## Perfiles de captura

Un perfil fija **cómo se lee la página**. Quien pide la captura lo elige; si no nombra ninguno, se usa `reader`. Los perfiles se definen en el código (`capture.profiles`) y todos usan el mismo Chrome, con su user agent, `es-ES` y sin banderas de automatización.

| | `reader` (por defecto) | `audit-es` ([D-156](../docs/30-governance/decisions.md#d-156), [D-157](../docs/30-governance/decisions.md#d-157)) |
|---|---|---|
| Quién lo usa | PAA, el entrenamiento, el MPIR y cualquier captura que no nombre otro | La auditoría informativa de Web y Web Schema.org, cuando se pida |
| Estado | Perfil de Chrome persistente | Un contexto de navegador nuevo por ficha (sin cookies, almacenamiento ni caché de ningún sitio), que se desecha al terminar |
| JavaScript | Se ejecuta | No se ejecuta (`Emulation.setScriptExecutionDisabled`): `<noscript>` es marcado |
| Interacción | Desplazamiento con la rueda (por lotes, a ritmo de lector) | Primera carga, sin desplazamiento ni permanencia |
| La ficha (`ID.html`) | El DOM renderizado (o de la primera carga) | El documento de la respuesta HTTP, en UTF-8, decodificado con la codificación que usó el navegador |
| Además | — | Los bytes originales del cuerpo (`response.html.gz`, con su BOM), el contexto de la petición y robots.txt por bot |

- **Un desafío que exige JavaScript no se pasa sin él.** Con `audit-es` no se espera a que se resuelva: queda `blocked`, una incidencia y no una ausencia ([OQ-80](../docs/30-governance/open-questions.md)).
- **Nunca se acepta un banner:** el motor no pulsa nada, y con `audit-es` ninguna ficha hereda un consentimiento.
- **Contexto de la petición** (`request_context`, con `audit-es`):
  - `Accept-Language` y user agent, tal como salieron;
  - el origen: IP, prefijo, país y ASN, consultados en RIPEstat. Se registran, no se comprueban: un fallo de la consulta queda escrito y la captura sigue.
- **robots.txt por bot** (`robots_bots`, con `audit-es`): para cada bot de `capture.profiles.BOTS`, el grupo que obedece (el suyo, `*` o ninguno) y si puede pedir la URL y la raíz. Los bots son GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Googlebot, Google-Extended, Bingbot, Meta-ExternalAgent, Meta-ExternalFetcher, FacebookBot y Amazonbot. Es un hecho técnico que se registra: no nos aplica y no afecta al GSC.
- Las cabeceras de cada salto de redirección (`redirects[].headers`) y la IP del servidor (`http.remote_ip`) se registran con todos los perfiles.

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
| `meta.json` | URL pedida y final, perfil, redirecciones (con las cabeceras de cada salto), estado HTTP, cabeceras e IP del servidor, navegador, acciones realizadas, resultado y sha256 de cada fichero. Con `audit-es`, también el contexto de la petición, robots.txt por bot y `response_body` (`original` si se guardaron los bytes originales). |
| `response.html.gz` | El documento tal como lo envió el servidor: decodificado a UTF-8 por Chrome con `reader`, y sus bytes originales con `audit-es`. |
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
| `ID.html` | Según el perfil: el DOM de la instantánea (renderizado, o de la primera carga en el entrenamiento) o el documento de la respuesta HTTP (`audit-es`). |
| `ID.json` | `url`, `fetched_at`, tamaño y sha256 de la ficha, método (`chrome-cdp`), `profile` (una ficha anterior a los perfiles, sin el campo, es `reader`), contenido, URL final, estado HTTP, user-agent, con `audit-es` `request_context` y `robots_bots`, y `snapshot`: la ruta de la instantánea (`var/pages/ID/AAAAMMDDTHHMMSS`, relativa a `capture/`). Quien congela puede añadir campos propios (el entrenamiento, `selection` y `category`). |
| `ID/<instante>/` | Cada intento de captura de ese ID, con su instantánea (ver *Qué se conserva*). |

- **Una ficha congelada nunca se sustituye.** `fetch` y `freeze` rechazan un ID que ya tiene ficha (`ID.html` o `ID.json`); la captura nueva del mismo producto lleva otro ID. `fetch` lo comprueba antes de visitar, y la escritura es exclusiva.
- Un intento rechazado o bloqueado solo deja su instantánea, sin ficha: el ID sigue libre y se puede reintentar.
- **ID:** kebab-case (minúsculas, dígitos y guiones), porque nombra ficheros.
- `fetch(ID, URL, profile=None)` es la captura suelta y su congelación (un perfil desconocido se rechaza antes de visitar); `freeze(ID, URL, carpeta, meta)` congela una instantánea ya capturada (la usa la captura por lotes del entrenamiento).
- `read(ID)` y `page_path(ID)` leen la ficha. **Lectores de página**, sobre el HTML leído: `text_lines` (las líneas de texto, sin scripts ni estilos), `json_ld` (los bloques JSON-LD que se pueden leer) y `walk` (los nodos de un documento JSON-LD, siguiendo `@graph`, `mainEntity`, `itemListElement` y `hasVariant`).
- `engine_available()` dice si se puede capturar aquí (websockets y Chrome: en el contenedor sí, en el host no).

## Páginas de una auditoría

`capture.audit` captura, con `audit-es`, las páginas que [D-167](../docs/30-governance/decisions.md#d-167) fija para la auditoría de un sitio. Todo queda en `var/audits/AUDIT/`, un directorio por auditoría que nunca se sustituye (un ID existente se rechaza); estas páginas no pasan al almacén de fichas.

| Tipo (`type`) | Cuáles | Cómo se localizan |
|---|---|---|
| `product` | Las fichas del encargo (`product-01`…) | La lista que se da; todas del mismo sitio |
| `home` | La portada | `/` del sitio |
| `policy` | Envíos, devoluciones, contacto y aviso legal (`policy-shipping`, `-returns`, `-contact`, `-legal`) | Por los enlaces de la portada: el texto o la dirección (sin acentos) los nombra; primero el pie (`footer`, `role=contentinfo`), luego el texto antes que la dirección, del mismo sitio o un subdominio |
| `category` | La categoría inmediata de cada ficha (`category-01`…) | Sus migas: el marcado (`breadcrumb`, `migas`, `BreadcrumbList` en microdatos) y, si no hay, el JSON-LD; es el último enlace que no es la ficha ni la raíz. Una categoría compartida se captura una vez |

- **Lo no localizado se registra, no se sustituye:** una política sin enlace queda `not_located` (`home_not_captured` si no se capturó la portada); una ficha sin migas, `none`, y con migas sin categoría, `no_category`.
- **robots.txt y los sitemaps:** robots.txt (y `tdmrep.json`) de cada origen visitado, en `sites/HOST/`. Los sitemaps son los declarados en robots.txt o, si no hay, `/sitemap.xml`; se siguen los índices y se guardan tal como llegan, gzip incluido, en `sitemaps/`, hasta un tope (50 ficheros y 200 MB; `--sitemap-files`, `--sitemap-mb`). Lo que no se leyó queda en `pending`.
- **Si la ficha está en los sitemaps** (`in_sitemaps`), por su URL pedida, su URL final o la canónica que declara (`link rel=canonical`, que se registra en `canonical`), en ese orden, sin fragmento y literal; `by` dice cuál coincidió: `yes`, `no`, o `undetermined` si quedaron sitemaps sin leer o fallidos (una ausencia exige la cobertura completa). Un 4xx de un sitemap es que no existe, no un fallo.
- **Ritmo:** cada página, en una ventana y un contexto nuevos; 3–8 s entre páginas, o el `Crawl-delay` si es mayor. Un bloqueo para la auditoría y lo que falta queda `pending`.
- **Legitimidad:** la de cualquier captura, por origen (robots.txt para `stratia-cic` y reserva TDM); cada instantánea registra además robots.txt por bot.

| Fichero | Contenido |
|---|---|
| `audit.json` | El manifiesto: sitio, perfil, legitimidad, sitemaps (leídos, pendientes, si la lectura es completa, número de URL), `pages` (cada página con su `id`, `type`, URL, resultado, URL final, estado HTTP e instantánea), `products` (página, `canonical`, `in_sitemaps`, migas y `category_page`), `policies` y `stopped` |
| `pages/PÁGINA/<instante>/` | La instantánea de cada página (ver *Qué se conserva*); su `meta.json` lleva `audit` y `page_type` |
| `sites/HOST/` | robots.txt y `tdmrep.json` de cada origen |
| `sitemaps/NNN-nombre` | Cada sitemap tal como llegó |

`audit.manifest(AUDIT)` y `audit.read(AUDIT, PÁGINA)` leen una auditoría (el documento de la respuesta, en UTF-8) sin Chrome. La interpretación de las páginas es de quien las evalúa (web-audit, la auditoría informativa).

## Uso

`capture/bin/pages fetch ID URL [--profile reader|audit-es]`: congela una ficha suelta con el perfil que se nombre (por defecto, `reader`). Desde el host, delega en el contenedor (`bin/run dev up` si no está levantado); un ID ya ocupado se rechaza en el host, sin lanzar nada.

`capture/bin/pages audit AUDIT [URL …] [--from FICHERO]`: captura las páginas de una auditoría a partir de las fichas del encargo (las URL o un fichero con una por línea; `#` comenta). Como `fetch`, delega en el contenedor; una auditoría de una ficha lleva unos 3 min.

## Módulos

| Módulo | Qué hace |
|---|---|
| `browser` · `cdp` | Chrome: arranque o conexión al que ya corre (un Chrome y un perfil por contenedor, en `var/`), ventanas (en el perfil persistente o en un contexto propio, con o sin JavaScript), lectura de la página y diagnóstico (`signals`). |
| `profiles` | Los perfiles de captura, los bots de robots.txt que se registran y el origen de la petición (RIPEstat). |
| `robots` · `tdm` · `detect` · `legitimacy` | Legitimidad, desafíos y antibot. |
| `pacing` · `crawl` | Ritmo de lector y lotes: un hilo por sitio (`SiteRun`). Quien llama pone los elementos, dónde va cada instantánea y qué hace con cada resultado. |
| `visit` · `once` · `files` | Una visita y su instantánea, la captura suelta, y la escritura y lectura de ficheros. |
| `sitemaps` | Descubrimiento de URL en los sitemaps, desde la ventana del propio sitio. |
| `audit` | Las páginas de una auditoría (D-167): localización de políticas y categorías, sitemaps y manifiesto. |
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
├── src/capture/            el motor (browser, cdp, profiles, robots, tdm, detect, legitimacy, pacing, crawl,
│                           visit, once, files, sitemaps, audit), el almacén (pages) y cli
├── tests/                  pruebas
└── var/                    desechable: pages/ (las fichas y sus instantáneas), audits/ y el perfil de Chrome
```

## Qué entra en git

En git va **lo que gobierna el sistema**: código y pruebas. `var/` es desechable y no tiene copia; git no es una copia de seguridad. Una ficha perdida no se recupera igual: una captura nueva da otra instantánea, con otro ID, y lo construido sobre la perdida (casos, modelos, contrastes) habrá que revisarlo.

## Pruebas

`bin/run dev test capture/tests` (todas las del proyecto: `bin/run dev test`): robots.txt, desafíos, ritmo y reservas; el almacén (congelar, leer, el rechazo de un ID existente y los ID no válidos); los perfiles; y, con Chrome, `pages fetch` de extremo a extremo contra un servidor local, incluidas una URL que robots.txt excluye y la repetición de un ID, y `audit-es` frente a `reader` en el mismo dominio (sin cookies heredadas ni JavaScript, bytes originales, cabeceras de cada salto y robots.txt por bot); las páginas de una auditoría (políticas y migas, sitemaps con índice y gzip, cobertura) y su captura de extremo a extremo.
