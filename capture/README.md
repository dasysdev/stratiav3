# capture

Sistema del **motor de captura y el almacén común de fichas congeladas** ([D-150](../docs/30-governance/decisions.md#d-150), que enmienda [D-046](../docs/30-governance/decisions.md#d-046) en dónde vive el motor). Todos los sistemas que evalúan una ficha (demand-engine, web-audit y, después, la auditoría) la leen del mismo almacén, para evaluar la misma instantánea.

- **La captura se comparte; su interpretación, no.** Lo que una ficha significa para un sistema queda en ese sistema: los requisitos y el modelo de demanda, en [demand-engine](../demand-engine/README.md); el contraste de los requisitos técnicos, en [web-audit](../web-audit/README.md).
- Es uno de los sistemas del proyecto: un directorio de primer nivel y un miembro del workspace de uv ([pyproject.toml](../pyproject.toml)). Depende de `websockets` (CDP); leer el almacén solo usa la biblioteca estándar.
- **Consumidores:** en demand-engine, taxo (la captura suelta, `taxo page fetch`, y la lectura de fichas), el entrenamiento (`train discover` y `train capture`), el MPIR y PAA (su navegador, no su legitimidad); web-audit, las fichas de su contraste. Las fichas de todos están aquí.

Captura páginas de ecommerce de dos formas:

- **Por lotes** (`crawl`): a ritmo de lector, con un sitio por ventana. Lo usan el MPIR y la captura del catálogo de entrenamiento (`demand-engine/bin/train capture`).
- **Una página suelta** (`once`): la usan `bin/pages fetch` y `demand-engine/bin/taxo page fetch` para congelar una ficha.
- **El rastreo de una auditoría** (`spider`, [D-170](../docs/30-governance/decisions.md#d-170)): `bin/pages crawl`, siempre con `audit-es`: el sitio, sus sitemaps y el universo (ver *Rastreo de una auditoría*).
- **Las páginas de una auditoría** (`audit`, [D-167](../docs/30-governance/decisions.md#d-167)): `bin/pages audit` las elige sobre el rastreo, sin capturar nada (ver *Páginas de una auditoría*).
- **Los recursos de una auditoría** (`resources`): `bin/pages resources` pide con GET una lista de URL (las imágenes del marcado) y guarda el estado y las cabeceras, sin el cuerpo (ver *Recursos de una auditoría*).

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
| Quién lo usa | PAA, el entrenamiento, el MPIR y cualquier captura que no nombre otro | La auditoría informativa de Web y Web Schema.org (`pages audit`, `pages crawl`) y la captura suelta que lo nombre |
| Estado | Perfil de Chrome persistente | Un contexto de navegador nuevo por ficha (sin cookies, almacenamiento ni caché de ningún sitio), que se desecha al terminar |
| JavaScript | Se ejecuta | No se ejecuta (`Emulation.setScriptExecutionDisabled`): `<noscript>` es marcado |
| Interacción | Desplazamiento con la rueda (por lotes, a ritmo de lector) | Primera carga, sin desplazamiento ni permanencia |
| La ficha (`ID.html`) | El DOM renderizado (o de la primera carga) | El documento de la respuesta HTTP, en UTF-8, decodificado con la codificación que usó el navegador |
| Además | — | Los bytes originales del cuerpo (`response.html.gz`, con su BOM), el contexto de la petición y robots.txt por bot |

- **Un desafío que exige JavaScript no se pasa sin él.** Con `audit-es` no se espera a que se resuelva: queda `blocked`, una incidencia y no una ausencia ([OQ-80](../docs/30-governance/open-questions.md)).
- **Nunca se acepta un banner:** el motor no pulsa nada, y con `audit-es` ninguna ficha hereda un consentimiento.
- **Contexto de la petición** (`request_context`, con `audit-es`):
  - `Accept-Language` y user agent, tal como salieron;
  - el origen: IP, prefijo, país y ASN, consultados en RIPEstat. Se registran, no se comprueban: un fallo de la consulta queda escrito y la captura sigue. Se consulta una vez por ejecución (una auditoría, un rastreo, un lote) y se registra en cada página.
- **robots.txt por bot** (`robots_bots`, con `audit-es`): para cada bot de `capture.profiles.BOTS`, el grupo que obedece (el suyo, `*` o ninguno) y si puede pedir la URL y la raíz. Los bots son GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Googlebot, Google-Extended, Bingbot, Meta-ExternalAgent, Meta-ExternalFetcher, FacebookBot y Amazonbot. Es un hecho técnico que se registra: no nos aplica y no afecta al GSC.
- Las cabeceras de cada salto de redirección (`redirects[].headers`) y la IP del servidor (`http.remote_ip`) se registran con todos los perfiles.

## Legitimidad

1. **robots.txt según la RFC 9309.**
   - Se aplican los grupos de `stratia-cic` o, si ninguno lo nombra, los de `*`.
   - Gana la regla más específica, con `*` y `$`; ante un empate gana Allow.
   - Si responde 4xx, todo está permitido. Si responde 5xx o 429, o no responde, no se captura nada.
   - Que excluya a bots de IA (GPTBot, ClaudeBot…) se avisa para que lo revises, pero no nos aplica.
2. **Reserva TDM:** `/.well-known/tdmrep.json`, la cabecera `tdm-reservation` y la meta `tdm-reservation`. Si hay reserva, no se conserva ningún contenido.
   - En una auditoría, una reserva además para el proceso ([D-171](../docs/30-governance/decisions.md#d-171)). Ver *Páginas de una auditoría*.
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
| `robots.txt` · `tdmrep.json` | Evidencia de la legitimidad (captura suelta; en el MPIR va con la comprobación del referente). |

Solo se guarda contenido si la página no es un desafío, un error o una reserva TDM. Las negativas por robots.txt o por reserva también dejan su `meta.json`. No hay capturas de pantalla ([D-042](../docs/30-governance/decisions.md#d-042)) ni MHTML ([D-172](../docs/30-governance/decisions.md#d-172)): nada lee los recursos de la página en su instantánea (las imágenes del marcado se piden aparte, sin su cuerpo: *Recursos de una auditoría*). Las instantáneas anteriores pueden llevar `page.mhtml.gz`.

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

`capture.audit` elige, sobre el rastreo de una auditoría (*Rastreo de una auditoría*), las páginas que fija [D-167](../docs/30-governance/decisions.md#d-167). La auditoría solo trabaja sobre el resultado del rastreo: no pide nada al sitio y no necesita Chrome ([D-170](../docs/30-governance/decisions.md#d-170)). Cada página lleva la instantánea de la visita del rastreo y su ID (`page-NNNNN`). El resultado es `audit.json`, en la carpeta del rastreo; no se sustituye.

| Tipo (`type`) | Cuáles | Cómo se localizan |
|---|---|---|
| `product` | Las fichas del encargo (la lista que se da) o, sin lista, todas las fichas del universo | Por su URL, su URL final o su URL canónica en el universo |
| `home` | La portada | La URL de inicio del rastreo |
| `policy` | Envíos, devoluciones, contacto y aviso legal | Por los enlaces de la portada: el texto o la dirección (sin acentos) los nombra; primero el pie (`footer`, `role=contentinfo`), luego el texto antes que la dirección, del mismo sitio o un subdominio |
| `category` | Todas las categorías del universo y la categoría inmediata de cada ficha ([D-215](../docs/30-governance/decisions.md#d-215)) | El tipo `category` del universo, sin su paginación; y las migas de cada ficha: el marcado (`breadcrumb`, `migas`, `BreadcrumbList` en microdatos) y, si no hay, el JSON-LD; la inmediata es el último enlace que no es la ficha ni la raíz |

- **Lo que falta se registra, no se sustituye ni se pide:**
  - una política sin enlace queda `not_located` (`home_not_captured` si no se capturó la portada), y una localizada que el rastreo no capturó, `not_captured`;
  - una ficha sin migas queda `none`; con migas sin categoría, `no_category`; si el rastreo no capturó su categoría inmediata, `category_page` es `null`;
  - una ficha del encargo fuera del universo no se audita: `in_universe` es `no` si el rastreo terminó completo e `undetermined` si no (una ausencia exige la cobertura completa); si está en el universo y no se capturó, `yes`.
- **Si la ficha está en los sitemaps** (`in_sitemaps`): el valor del universo, `yes` (con `by`: `url`, `url_final` o `canonical`), `no` o `undetermined`.
- **Reserva TDM:** si el rastreo paró por una reserva ([D-171](../docs/30-governance/decisions.md#d-171)), no se audita nada; `pages audit` termina con el código 3 y un mensaje en stderr.
- **Un rastreo auditado no se reanuda:** `--resume` se rechaza si ya existe `audit.json`.

`audit.json` lleva: sitio, perfil, origen y legitimidad del rastreo, `crawl` (su cobertura y el resumen del universo), `sitemaps`, `pages` (cada página con su `id`, `type`, URL, resultado, URL final, estado HTTP e instantánea), `products` (página, `type_in_universe`, `canonical`, `in_sitemaps`, migas y `category_page`, o `in_universe`) y `policies`. Es la forma que lee web-audit.

## Recursos de una auditoría

`capture.resources` pide con GET una lista de URL de recurso de una auditoría y registra sus respuestas sin el cuerpo. Hoy la usa web-audit para las imágenes del marcado (T-087). capture no lee el marcado: la lista la da quien la pide.

- **Requisito:** la auditoría ya eligió sus páginas (`audit.json`). Una auditoría parada por una reserva TDM no pide nada.
- **Cómo pide:** una ventana y un contexto nuevos por URL, con `audit-es`. Chrome sigue las redirecciones y aborta la última respuesta tras las cabeceras (`Fetch.failRequest` en la fase de respuesta). capture no lee ni guarda ningún byte del cuerpo.
- **robots.txt de cada host:** si el rastreo estuvo en el host, vale el suyo (`sites/` de sus ejecuciones) con el estado que registró. Si no (un CDN), capture congela robots.txt y `tdmrep.json` en `resources/sites/HOST/`.
- **Legitimidad:** si robots.txt no permite la URL a nuestro bot, o no responde, capture no la pide. La registra como `disallowed`, con la regla que decide.
- **Reserva TDM** (D-171): un `tdmrep.json` que reserva algo o la cabecera `tdm-reservation` de una respuesta paran la ejecución y la auditoría. `pages resources` termina con el código 3.
- **Ritmo:** una petición por segundo a cada host como máximo, o su Crawl-delay si es mayor. El origen de la petición (RIPEstat), una vez por ejecución.
- **Sin repetir:** una URL ya registrada no se vuelve a pedir. Excepción: una respuesta 429 para la ejecución y la URL se pide en la siguiente.

Resultados de cada URL (`outcome`): `answered` (una respuesta, de cualquier estado: un 404 o un 403 son datos para web-audit), `failed` (sin respuesta), `disallowed`, `reserved`, `blocked` (429) e `invalid` (no es http(s)).

| Fichero | Contenido |
|---|---|
| `resources.json` | El manifiesto: `runs` (pedidas, origen, parada), `hosts` (el robots.txt de cada uno: estado, fichero y `source`, `crawl` o `resources`), `outcomes` y `resources`: cada URL con su resultado, estado, URL final, cabeceras de la última respuesta, `redirects` (estado y cabeceras de cada salto), `rule` si robots.txt la excluye y `requested_at` |
| `resources.jsonl` | El diario: una línea por ejecución, por host nuevo y por URL |
| `resources/sites/HOST/` | robots.txt y `tdmrep.json` de cada host que la auditoría no tenía |

Las cabeceras que llegan en varias líneas (`X-Robots-Tag`, por ejemplo) se unen con un salto de línea, como en `meta.json`.

## Rastreo de una auditoría

`capture.spider` descubre las páginas de un sitio desde la portada y captura cada una con `audit-es` en la misma visita que lee sus enlaces ([D-170](../docs/30-governance/decisions.md#d-170)). Los enlaces solo descubren: no se valoran. Todo queda en `var/audits/AUDIT/`, como una auditoría.

- **Qué enlaces sigue:** los `<a href>` del documento de la respuesta HTTP, sin JavaScript (la primera `<base href>` fija la base). Sigue un enlace si cumple todo esto:
  - es `http` o `https`;
  - es del host de la URL de inicio o del host final de la portada (`x.es` → `www.x.es`);
  - no lleva parámetros (`?`): las facetas no se rastrean ([D-173](../docs/30-governance/decisions.md#d-173)). Excepción: la paginación, si es el único parámetro y su valor es numérico (`page`, `p`, `pag`, `pagina`, `pg`; [D-204](../docs/30-governance/decisions.md#d-204));
  - no es un recurso que no es una página, por su extensión (PDF, imágenes, vídeo, ficheros, CSS, JS…).
- **El fragmento se quita.** Una URL se compara con el esquema y el host en minúsculas.
- **`nofollow`:** se sigue y se registra, en el enlace y en la página que descubre (`found_by_nofollow`).
- **Orden: políticas, y después categoría a categoría** ([D-204](../docs/30-governance/decisions.md#d-204), [D-215](../docs/30-governance/decisions.md#d-215)). La araña lo aprende en el propio rastreo, sin configuración por sitio:
  - **Ficha:** una página capturada cuyo documento lo señala: `og:type` `product`, o un `Product` (con su `ProductGroup`, como mucho) en lo alto del JSON-LD o de los microdatos. Los productos de un listado (dentro de un `ItemList`) no cuentan.
  - **Forma** de una URL: su ruta con los textos (`W`) y los números (`N`) abstraídos y el marcador que precede a los números (`-p-`, `-c-`). Ejemplos: `/W-p-N.html`, `/W-c-N`, `/W-c-N?page`, `/products/W`.
  - **Categoría:** cada enlace de las migas de una ficha capturada, en todos los niveles, y cualquier URL con la forma de esas categorías. Se buscan todas las categorías, no solo la inmediata de cada ficha.
  1. Las políticas de la auditoría (envíos, devoluciones, contacto y aviso legal), localizadas en los enlaces de la portada como en *Páginas de una auditoría* (`audit`).
  2. Categoría a categoría: la categoría (`category`), toda su paginación (`pagination`) y después las fichas que listan sus páginas (`listed`); luego, la siguiente categoría (primero las de las migas, después por su forma). La paginación sigue mientras la página lista fichas. Una categoría capturada antes de saberse que lo era se recorre igual, sin volver a pedirla.
  3. Las fichas encontradas en otras páginas (`product`); una vez, cada forma aún no capturada (`probe`); el resto (`other`), primero las formas cuyas páginas encontraron más fichas.
  - Antes de confirmar la primera ficha, van primero las fichas y las formas nuevas, en anchura. El orden solo importa si el rastreo se corta: completo, alcanza las mismas páginas.
  - Medida en burritoblanco (2026-10-29): en 60 URL, la portada, 3 políticas, «lo más nuevo» con sus 5 páginas y 49 fichas.
- Cada URL se pide una sola vez; la que ya se alcanzó por una redirección no se vuelve a pedir.
- **Ritmo:** una página por segundo como máximo, o el `Crawl-delay` si es mayor. Sin horario. Cada página, en una ventana y un contexto nuevos.
- **Tope:** 50.000 URL procesadas (`--max-urls`).
- **Legitimidad y paradas:** las de cualquier captura, por origen (robots.txt para `stratia-cic` y reserva TDM); cada instantánea registra además robots.txt por bot. Un bloqueo para el rastreo. **Una reserva TDM lo para y avisa** ([D-171](../docs/30-governance/decisions.md#d-171)):
  1. Antes de capturar nada, el motor lee robots.txt y `tdmrep.json` del sitio. Si una entrada de `tdmrep.json` reserva alguna ruta, no se captura nada.
  2. La portada es la primera página que se visita, antes de los sitemaps. Su cabecera y su meta `tdm-reservation` completan la comprobación. Si la portada tiene reserva, no se conserva su contenido y no se captura nada más.
  3. Si después aparece una reserva (la cabecera o la meta de una página, o el `tdmrep.json` de otro origen o de un sitemap), el rastreo para allí. Esa página no se conserva; las anteriores, sí.
  - `stopped` dice dónde paró y `reservation` guarda la evidencia: `where` (`tdmrep.json`, `sitemaps` o el ID de la página), `url`, `source` y el fichero de `tdmrep.json` o la instantánea con la cabecera, la meta y `tdm-policy`. La orden termina con el código 3.
- **Sitemaps** (D-170): los declarados en robots.txt o, si no hay, `/sitemap.xml`. El rastreo los lee una vez, después de la portada. Sigue los índices y los guarda tal como llegan, gzip incluido, en `sitemaps/`, hasta un tope (50 ficheros y 200 MB; `--sitemap-files`, `--sitemap-mb`). Lo que no se leyó queda en `sitemaps.pending`. Un 4xx de un sitemap es que no existe, no un fallo.
- **URL de los sitemaps no alcanzadas:** cuando no queda nada que rastrear, la araña captura una vez cada URL de los sitemaps que el rastreo no alcanzó (`sitemap` en `chosen_as`, `source: sitemaps`). Puede llevar parámetros. Sus enlaces se registran pero no se siguen, y no enseñan nada al orden. Una URL de los sitemaps que es la URL, la URL final o la URL canónica de una página del rastreo es esa página. Las de otro host o los recursos no se capturan.
- **Cobertura** (`crawl.coverage`): completa si no queda nada pendiente, se leyeron los enlaces de todas las páginas y se leyeron todos los sitemaps. Si no, `reasons` dice por qué: `limit`, `blocked`, `reserved`, `interrupted`, `failed` (páginas con error, cuyos enlaces no se leyeron) o `sitemaps`. Una página excluida por robots.txt o un 404 no la dejan incompleta. `crawl_complete` dice si el rastreo, sin las URL de los sitemaps, terminó completo. `crawl.pending` lista lo que falta.
- **Reanudación** (`--resume`): un rastreo interrumpido, bloqueado o detenido por el tope sigue desde su diario (`crawl.jsonl`). No vuelve a pedir nada de lo procesado; una página bloqueada se reintenta primero. Una parada por reserva TDM no se reanuda, ni un rastreo ya auditado (`audit.json`). Cada reanudación vuelve a leer robots.txt y `tdmrep.json`.

**Universo** (`universe`; resumen en `crawl.universe`): cada URL del rastreo y de los sitemaps, una vez, con:

- `page` (la página que la capturó, o `null`) y `outcome` (el de la página, `pending` o `skipped`, con `skip`, para las de los sitemaps que no se capturan);
- `reached`: `yes` si el rastreo la alcanzó; `no` si solo está en los sitemaps y el rastreo terminó completo; `undetermined` si no terminó;
- `in_sitemaps`: `yes` por su URL, su URL final o su URL canónica (`sitemaps_by` si no es la URL); `no` si la lectura de los sitemaps fue completa; `undetermined` si no;
- `type`, por varias señales, no solo el marcado. Lo dudoso queda sin tipo (`null`):
  - `home`: la URL de inicio; `policy`: una política localizada en la portada;
  - `product`: señales de ficha en su documento y una forma de URL de ficha;
  - `category`: en las migas de una ficha o con su forma (también su paginación), lista URL con forma de ficha y no tiene señales de ficha;
  - `other`: ninguna de esas señales;
  - una página no capturada, que no es HTML o de otro host no tiene tipo.

| Fichero | Contenido |
|---|---|
| `crawl.json` | El manifiesto: sitio, perfil, `runs` (cada ejecución con su origen, su legitimidad y el tope de los sitemaps), `crawl` (inicio, hosts, tope, descubiertas, procesadas, resultados, enlaces no seguidos por motivo, `product_pages`, `shapes`, `audit_pages`, cobertura, pendientes y resumen del universo), `sitemaps`, `universe`, `pages`, `stopped` y `reservation` |
| `audit.json` | Las páginas auditadas, que elige `pages audit` (*Páginas de una auditoría*) |
| `crawl.jsonl` | El diario: una línea por ejecución, por URL procesada (con las URL nuevas que descubrió) y por la lectura de los sitemaps |
| `pages/page-NNNNN/<instante>/` | La instantánea de cada página y `links.json.gz`: cada `<a href>` con su texto, `nofollow` y por qué no se siguió (`skip`) |
| `sites/HOST/` · `resumes/NN/HOST/` | robots.txt y `tdmrep.json` de cada origen, de la primera ejecución y de cada reanudación |
| `sitemaps/NNN-nombre` | Cada sitemap tal como llegó (si se leyeron en una reanudación, `resumes/NN/sitemaps/`) |

Cada página de `pages` lleva `id`, `url`, `depth`, `found_from` (la página que la descubrió), `shape`, `chosen_as` (`audit`, `category`, `pagination`, `listed`, `product`, `probe`, `other`, `sitemap` o `retry`), `audit_page` (la política o la categoría de D-167 para la que se eligió), `product_signals` si es una ficha, `canonical` si declara alguna, resultado, URL final, estado HTTP, instantánea y `links` (total, `nofollow`, nuevas y no seguidas por motivo). `crawl.shapes` resume cada forma: capturadas, fichas, si cuenta como ficha, fichas descubiertas por página y pendientes. `crawl.audit_pages` lista las políticas y las categorías de las migas, con la página que las capturó; `crawl.category_shapes`, las formas de categoría. El diario anota además `{"group": URL}` cuando se recorre una categoría ya capturada. Además, si procede: `source: sitemaps`, `same_as` (una redirección a una página ya capturada), `offsite` (la URL final es de otro host: no se leen sus enlaces), `not_html`, `recovered` (instantánea recuperada tras una parada brusca) y `attempts`.

Medida en burritoblanco (2026-10-29): 2,2–3,0 s por página y unos 110 KB de disco por página.

`audit.manifest(AUDIT)` y `audit.read(AUDIT, PÁGINA)` leen una auditoría o un rastreo (el documento de la respuesta, en UTF-8) sin Chrome. La interpretación de las páginas es de quien las evalúa (web-audit, la auditoría informativa).

## Uso

`capture/bin/pages fetch ID URL [--profile reader|audit-es]`: congela una ficha suelta con el perfil que se nombre (por defecto, `reader`). Desde el host, delega en el contenedor (`bin/run dev up` si no está levantado); un ID ya ocupado se rechaza en el host, sin lanzar nada.

`capture/bin/pages crawl AUDIT URL [--max-urls N] [--sitemap-files N] [--sitemap-mb N]`: rastrea y captura el sitio desde su portada, y sus sitemaps. `capture/bin/pages crawl AUDIT --resume [--max-urls N]` sigue un rastreo interrumpido; con `--max-urls`, sube el tope. Delega en el contenedor. Ctrl+C lo interrumpe y deja el manifiesto escrito.

`capture/bin/pages audit AUDIT [URL …] [--from FICHERO]`: elige las páginas de la auditoría sobre el rastreo `AUDIT`. Las fichas son las del encargo (las URL o un fichero con una por línea; `#` comenta); sin ellas, todas las del universo. Se ejecuta en el host, sin Chrome, y no pide nada al sitio.

`capture/bin/pages resources AUDIT [URL …] [--from FICHERO]`: pide las URL de recurso que se den (o un fichero con una por línea; `-`, la entrada estándar) y las registra en `resources.json`. Delega en el contenedor y le pasa la lista por la entrada estándar. Ctrl+C lo interrumpe y deja el manifiesto escrito; lo pendiente se pide en otra ejecución.

## Módulos

| Módulo | Qué hace |
|---|---|
| `browser` · `cdp` | Chrome: arranque o conexión al que ya corre (un Chrome y un perfil por contenedor, en `var/`), ventanas (en el perfil persistente o en un contexto propio, con o sin JavaScript), lectura de la página y diagnóstico (`signals`). |
| `profiles` | Los perfiles de captura, los bots de robots.txt que se registran y el origen de la petición (RIPEstat). |
| `robots` · `tdm` · `detect` · `legitimacy` | Legitimidad, desafíos y antibot. |
| `pacing` · `crawl` | Ritmo de lector y lotes: un hilo por sitio (`SiteRun`). Quien llama pone los elementos, dónde va cada instantánea y qué hace con cada resultado. |
| `visit` · `once` · `files` | Una visita y su instantánea, la captura suelta, y la escritura y lectura de ficheros. |
| `sitemaps` | Descubrimiento de URL en los sitemaps, desde la ventana del propio sitio. |
| `audit` | Las páginas de una auditoría (D-167), elegidas sobre el rastreo; enlaces y migas de un documento, políticas de la portada y lectura de los sitemaps. |
| `spider` | El rastreo de una auditoría (D-170): descubrimiento por enlaces, sitemaps, captura, diario, reanudación, cobertura y universo con el tipo de cada página. |
| `resources` | Los recursos de una auditoría: GET de cada URL de una lista, solo el estado y las cabeceras, con robots.txt de cada host. |
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
│                           visit, once, files, sitemaps, audit, spider,
│                           resources), el almacén (pages) y cli
├── tests/                  pruebas
└── var/                    desechable: pages/ (las fichas y sus instantáneas), audits/ y el perfil de Chrome
```

## Qué entra en git

En git va **lo que gobierna el sistema**: código y pruebas. `var/` es desechable y no tiene copia; git no es una copia de seguridad. Una ficha perdida no se recupera igual: una captura nueva da otra instantánea, con otro ID, y lo construido sobre la perdida (casos, modelos, contrastes) habrá que revisarlo.

## Pruebas

`bin/run dev test capture/tests` (todas las del proyecto: `bin/run dev test`): robots.txt, desafíos, ritmo y reservas; el almacén (congelar, leer, el rechazo de un ID existente y los ID no válidos); los perfiles; y, con Chrome, `pages fetch` de extremo a extremo contra un servidor local, incluidas una URL que robots.txt excluye y la repetición de un ID, y `audit-es` frente a `reader` en el mismo dominio (sin cookies heredadas ni JavaScript, bytes originales, cabeceras de cada salto y robots.txt por bot); las páginas de una auditoría (políticas y migas, sitemaps con índice y gzip, cobertura) y su captura de extremo a extremo; el rastreo contra un sitio local (enlace creado por JavaScript, `nofollow`, ruta prohibida en robots.txt, redirecciones, paginación frente a facetas, facetas sin fin en la ruta, las fichas primero, las formas de URL y las señales de ficha, el tope, la reanudación tras Ctrl+C y tras una parada brusca, la reserva TDM y el origen una vez por ejecución); los recursos de una auditoría contra dos hosts locales, la tienda y un CDN con robots.txt propio (200, 404, 403, redirección, `X-Robots-Tag` en dos líneas, URL excluidas con su regla, sin cuerpo guardado, sin repetir, 429 y reservas TDM).
