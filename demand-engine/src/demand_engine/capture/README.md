# Motor de captura

Motor de [demand-engine](../../../README.md) compartido por el [MPIR](../mpir/README.md) y por el modelo de demanda ([D-046](../../../../docs/30-governance/decisions.md#d-046)). Captura páginas de ecommerce de referencia de dos formas:

- **Por lotes** (`crawl`): a ritmo de lector, con un sitio por ventana. Lo usan el MPIR y la captura del catálogo de entrenamiento (`bin/train capture`).
- **Una página suelta** (`once`): la usa `taxo page fetch` para congelar la ficha de un caso.

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

Estas políticas son del motor y se aplican igual a todas las capturas ([D-042](../../../../docs/30-governance/decisions.md#d-042), D-046).

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

Solo se guarda contenido si la página no es un desafío, un error o una reserva TDM. Las negativas por robots.txt o por reserva también dejan su `meta.json`. No hay capturas de pantalla ([D-042](../../../../docs/30-governance/decisions.md#d-042)).

**Resultados de una visita:**

| Resultado | Significado |
|---|---|
| `captured` | Capturada. |
| `blocked` | Bloqueada por un desafío o un 403/429. |
| `failed` | No recuperada por un error. |
| `gone` | No existe (404/410). |
| `disallowed` | Excluida por robots.txt. |
| `reserved` | Reserva TDM: no se conserva. |

## Módulos

| Módulo | Qué hace |
|---|---|
| `browser` · `cdp` | Chrome: arranque o conexión al que ya corre (un Chrome y un perfil por contenedor, en `var/capture/`), ventanas, lectura de la página y diagnóstico (`signals`). |
| `robots` · `tdm` · `detect` · `legitimacy` | Legitimidad, desafíos y antibot. |
| `pacing` · `crawl` | Ritmo de lector y lotes: un hilo por sitio (`SiteRun`). Quien llama pone los elementos, dónde va cada instantánea y qué hace con cada resultado. |
| `visit` · `once` · `files` | Una visita y su instantánea, la captura suelta, y la escritura y lectura de ficheros. |
| `sitemaps` | Descubrimiento de URL en los sitemaps, desde la ventana del propio sitio. |

## Configuración

| Variable (`.env`) | Valores |
|---|---|
| `CAPTURE_DISPLAY` | `:99` Xvfb (por defecto) · `:0` escritorio del host (WSLg), para ver las ventanas |
| `CAPTURE_DISABLE_GPU` | `1` por defecto en el contenedor |
| `CAPTURE_CDP_PORT` · `CAPTURE_PROFILE` | Puerto y perfil de Chrome (por defecto, 9223 y `var/capture/chrome-profile`) |

**Pendiente de la sonda (T-014):** en el contenedor no hay GPU y Chrome bloquea WebGL (`webgl: null` en `demand-engine/bin/mpir browser`), lo que es una señal delatora. La alternativa es que el motor controle el Chrome del host. Se decidirá con datos.

## Pruebas

En `tests/capture/` (robots.txt, desafíos, ritmo y reservas). Con Chrome hay dos pruebas de extremo a extremo contra un servidor local:
- `tests/mpir/test_e2e.py`: desplegables, contenido diferido, un desafío de Cloudflare, una reserva TDM y un 404;
- `tests/tools/test_taxo_pages.py`: `taxo page fetch`, incluida una URL que robots.txt excluye.
