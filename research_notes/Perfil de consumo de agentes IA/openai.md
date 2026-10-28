# Perfil de consumo de OpenAI (ChatGPT search, shopping y agentes) sobre fichas de producto — estado a 28-10-2026

Nota de investigación. Distingue **[oficial]** (documentación de OpenAI) de **[terceros]** (estudios, prensa, proveedores). Limitación de método: help.openai.com y openai.com/index devolvieron 403 al fetcher de esta sesión; su contenido se cita a través de resultados de búsqueda o de terceros y se marca así. Las páginas developers.openai.com y los JSON de IPs sí se leyeron directamente el 28-10-2026.

## 1. GPTBot, OAI-SearchBot, ChatGPT-User (y OAI-AdsBot): propósito, user agent, robots.txt, IPs, JavaScript

### Takeaway
OpenAI documenta hoy cuatro rastreadores con user agent propio, IPs publicadas y control por robots.txt (salvo ChatGPT-User, que no aplica robots.txt). La documentación oficial no dice nada sobre JavaScript. Las pruebas empíricas (Vercel 2024, Resoneo 2026) coinciden en que **no ejecutan JavaScript**: leen la respuesta HTML cruda. Solo hay un informe anecdótico en contra.

### Cited Findings
- **[oficial, leído 28-10-2026]** La página de bots se mudó de platform.openai.com/docs/bots (301) a developers.openai.com/api/docs/bots. Recoge cuatro agentes: OAI-SearchBot, OAI-AdsBot, GPTBot y ChatGPT-User. Los ajustes de robots.txt de cada uno son independientes — [OpenAI, Overview of OpenAI Crawlers](https://developers.openai.com/api/docs/bots)
- **OAI-SearchBot [oficial]:** sirve para mostrar y enlazar sitios en las funciones de búsqueda de ChatGPT. Un sitio excluido no aparece en las respuestas de búsqueda, aunque puede salir como enlace de navegación. Un cambio en robots.txt tarda unas 24 h en aplicarse.
  - UA literal: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36; compatible; OAI-SearchBot/1.4; +https://openai.com/searchbot`.
  - Las peticiones de robots.txt pueden llevar la marca `robots.txt;` en el UA. La versión puede cambiar.
  - IPs: https://openai.com/searchbot.json
  - [OpenAI bots](https://developers.openai.com/api/docs/bots)
- **GPTBot [oficial]:** rastrea contenido que puede usarse para entrenar los modelos fundacionales. Bloquearlo indica que el contenido no se use para entrenamiento. Con GPTBot y OAI-SearchBot permitidos, OpenAI «puede usar un solo rastreo para ambos fines».
  - UA: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; GPTBot/1.4; +https://openai.com/gptbot`.
  - IPs: https://openai.com/gptbot.json
  - [OpenAI bots](https://developers.openai.com/api/docs/bots)
- **ChatGPT-User [oficial]:** cubre acciones iniciadas por el usuario en ChatGPT y en los Custom GPTs, como visitar una página para responder una pregunta o las GPT Actions. Robots.txt **no se aplica** a estas acciones ni controla la elegibilidad en Search, que va por OAI-SearchBot.
  - UA: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; ChatGPT-User/1.0; +https://openai.com/bot`.
  - IPs: https://openai.com/chatgpt-user.json
  - [OpenAI bots](https://developers.openai.com/api/docs/bots)
- **OAI-AdsBot [oficial]:** solo visita páginas de destino enviadas como anuncios en ChatGPT, para comprobar su seguridad y su relevancia. No se usa para entrenamiento.
  - UA: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko); compatible; OAI-AdsBot/1.0; +https://openai.com/adsbot`.
  - IPs: https://openai.com/adsbot.json
  - [OpenAI bots](https://developers.openai.com/api/docs/bots)
- **[oficial, descargados el 28-10-2026]** Ficheros de IPs:

  | Fichero | `creationTime` | Prefijos |
  |---|---|---|
  | searchbot.json | 2026-01-02 | 39 |
  | gptbot.json | 2026-09-22 | 18 |
  | chatgpt-user.json | 2026-10-27 | 235 |
  | adsbot.json | 2026-05-12 | 2 |

  Ejemplos de prefijos: 104.210.140.128/28, 13.66.216.176/28, 172.182.193.224/28, 20.125.66.80/28. — [searchbot.json](https://openai.com/searchbot.json), [gptbot.json](https://openai.com/gptbot.json), [chatgpt-user.json](https://openai.com/chatgpt-user.json), [adsbot.json](https://openai.com/adsbot.json)
- **[oficial]** La página de bots no menciona ejecución ni renderizado de JavaScript, Web Bot Auth, ChatGPT agent ni Atlas — [OpenAI bots](https://developers.openai.com/api/docs/bots)
- **[terceros, Vercel/MERJ, 17-12-2024]** Medición en el tráfico de nextjs.org y de la red de Vercel:
  - «None of the major AI crawlers currently render JavaScript»: GPTBot, OAI-SearchBot y ChatGPT-User incluidos.
  - Los rastreadores de ChatGPT descargan ficheros JS (11,50 % de sus peticiones) pero no los ejecutan. El contenido presente en la respuesta HTML inicial, incluidos datos JSON incrustados, sí puede leerse.
  - GPTBot hizo 569 millones de peticiones en un mes. El 57,70 % fueron HTML; el 34,82 %, 404, y el 14,36 %, redirecciones.
  - Operan desde centros de datos de EE. UU. (Des Moines, Iowa, y Phoenix, Arizona): «All AI crawlers we measured operate from U.S. data centers».
  - [Vercel, The rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- **[terceros, Resoneo «Sentinel», enero de 2026]** Página de prueba con 15 métodos de inyección y un centinela por método. Se pidió a cada asistente visitar la página. Resultado para ChatGPT-User:
  - «parses raw HTML source without any JS execution».
  - Ve texto HTML visible, microdatos, `<noscript>` y `<template>`.
  - **No** ve: JS en línea o diferido, contenido cargado por `fetch()`, Shadow DOM, iframes ni atributos `data-*`.
  - **No extrae el JSON-LD** de `<script type="application/ld+json">` (marcado ✗).
  - UA observado: `ChatGPT-User/1.0`; IP observada: 20.215.220.188.
  - No probó GPTBot ni OAI-SearchBot.
  - [Resoneo, AI Search crawler test results](https://think.resoneo.com/sentinel/geo-llm-crawler-report.html)
- **[terceros, anecdótico]** Un desarrollador afirma que OAI-SearchBot y GPTBot empezaron a ejecutar JavaScript, según sus logs cotejados con las IPs publicadas. Él mismo dice que no puede probar la causalidad. Página no accesible (403), conocida solo por el resumen del buscador — [Indie Hackers](https://www.indiehackers.com/post/traffic-from-chatgpt-jumped-is-it-because-its-crawlers-now-run-javascript-5dea2e48d0)

### Inferences
- Para los tres fetchers clásicos, el perfil «respuesta HTTP sin ejecutar JavaScript» es el que respaldan las pruebas.
- Lo que el modelo usa en ChatGPT-User parece ser el texto visible del HTML. Según Resoneo, el JSON-LD en `<script>` no le llega. Conviene separar en la auditoría dos cosas:
  - lo que hay en el HTML crudo (incluido el JSON-LD, que otros sistemas sí indexan);
  - lo que hay en el texto visible del HTML crudo, que es lo que lee el fetcher en tiempo real.
- Los prefijos de IP (20.x, 13.66.x, 104.208–210.x, 172.182.x) parecen de Microsoft Azure. Las mediciones de Vercel y Willison sitúan el origen en EE. UU., aunque OpenAI no publica la región de cada prefijo.

### Gaps
- No hay declaración oficial de OpenAI sobre ejecución de JS. Tampoco hay pruebas controladas de 2026 sobre OAI-SearchBot y GPTBot, que podrían renderizar en su canal de indexación.
- No se verificó en esta sesión desde cuándo ChatGPT-User dejó de aplicar robots.txt. La redacción anterior de la documentación decía que lo respetaba; no tengo fuente fechada.
- No se observaron cabeceras `Accept-Language` de GPTBot, OAI-SearchBot ni ChatGPT-User en ninguna fuente fiable.

## 2. ChatGPT search y shopping: índice, proveedores, construcción de resultados de producto, feeds, ACP, datos estructurados

### Takeaway
ChatGPT search combina un índice propio, alimentado por OAI-SearchBot, con varios proveedores externos. Bing es uno de ellos, pero no el único.

Los resultados de producto (carruseles, «shopping research») se construyen con tres fuentes:
- **metadatos estructurados de proveedores de primera y tercera parte**: feeds de comerciante, Shopify Catalog y proveedores de datos;
- **lectura de las fichas de producto publicadas**;
- contenido de terceros, como reseñas.

Desde 2026 el feed de comerciante (especificación de OpenAI dentro del ecosistema ACP) gana mucho peso. Su disponibilidad para España no está confirmada.

### Cited Findings
- **[terceros, Peec, septiembre de 2026]** «ChatGPT's search results come from its own index plus at least eight external providers — not from Bing alone».
  - Proveedores identificados en los eventos del servidor: Web IQ de Microsoft, rascadores de SERP de Google (Bright Data, Oxylabs y otro etiquetado «serp»), Yelp, TripAdvisor y canales internos de Google Maps.
  - El índice propio se llamaría «Labrador».
  - Bing aparece sobre todo en Deep Research.
  - No trata proveedores de shopping.
  - [Peec, ChatGPT search result providers](https://docs.peec.ai/research/chatgpt-search-result-providers)
- **[oficial, citado por terceros en 2024]** OpenAI «leverages third-party search providers, as well as content provided directly by our partners». Varias guías SEO consideran que Bing era el proveedor principal en 2024–2025 — [Search Engine Journal](https://www.searchenginejournal.com/chatgpt-search/), [Yoast](https://yoast.com/chatgpt-search/)
- **[oficial, help.openai.com art. 11128490, leído a través del buscador; varias versiones en caché sin fecha]**
  - Los resultados de producto se eligen de forma independiente y no son anuncios.
  - ChatGPT pondera «structured metadata from first- and third-party providers», como precio y descripción, además de otro contenido de terceros.
  - La lista de comerciantes de un producto se construye con metadatos de producto y comerciante de terceros o de los propios comerciantes. Se ordena por disponibilidad, precio, calidad y si el comerciante fabrica o vende principalmente el artículo.
  - Shopify se integra a través de Shopify Catalog; los demás comerciantes pueden solicitar acceso de feed directo.
  - Los resúmenes de reseñas los genera el modelo a partir de webs públicas.
  - Los precios pueden ir con retraso respecto a los del comerciante.
  - [OpenAI Help, Shopping in ChatGPT](https://help.openai.com/en/articles/11128490-shopping-in-chatgpt)
- **[oficial, anuncio del 24-11-2025, leído a través de terceros]** «Shopping research» funciona con una versión de GPT-5 mini entrenada para **leer fichas de producto** de minoristas reputados, citar fuentes y sintetizar datos de la web. Los resultados son orgánicos y salen de «publicly available retail sites». Los comerciantes pueden seguir un proceso de *allowlisting* para ser elegibles y ofrecer un feed directo — [Axios, 24-11-2025](https://www.axios.com/2025/11/24/chatgpt-shopping-research-openai-black-friday), [OpenAI, shopping research](https://openai.com/index/chatgpt-shopping-research) (403 en esta sesión)
- **[oficial, leído el 28-10-2026] Especificación del feed de producto:**
  - JSONL, CSV o TSV en UTF-8.
  - Nueve campos obligatorios para el descubrimiento: `item_id`, `title`, `description`, `url`, `brand`, `seller_name`, `image_url`, `availability`, `price`.
  - Moneda en ISO 4217; `target_countries` en ISO 3166-1 alfa-2.
  - El formato compartido cubre «US, CA, and MX». Las cargas estándar usan US. Otros mercados requieren que OpenAI confirme la integración y los países y monedas permitidos.
  - Search activado por defecto; Ads desactivado; checkout desactivado salvo integración aparte.
  - Las URL de producto e imagen deben ser públicas, preferiblemente HTTPS, y la de producto debe mostrar la variante seleccionada cuando se pueda.
  - La especificación **no menciona** Schema.org, JSON-LD ni JavaScript.
  - [OpenAI, Product Feed Spec](https://developers.openai.com/commerce/specs/feed)
- **[oficial, llms-full.txt de developers.openai.com/commerce, leído el 28-10-2026]**
  - «Product feeds give ChatGPT the catalog data it needs to index your products».
  - Entrega: «Push feeds to OpenAI via SFTP». Recomiendan «uploading a full snapshot at least once a day».
  - «Onboarding product feeds in ChatGPT is currently available to approved partners».
  - Ejemplos de `API-Version`: 2025-09-12 y 2025-09-29.
  - Stripe Shared Payment Token es la primera implementación del Delegated Payment Spec.
  - No se mencionan España, la UE ni EUR en el fragmento leído (primeros 100.000 de 148.000 caracteres).
  - [OpenAI Commerce docs (llms-full)](https://developers.openai.com/commerce/llms-full.txt)
- **[terceros] Evolución de Instant Checkout y del ACP:**
  - El 24-03-2026 OpenAI reorientó shopping hacia el descubrimiento: el pago vuelve al comerciante o se hace en apps dentro de ChatGPT, e Instant Checkout queda para algunos comerciantes elegibles. Las fuentes discrepan sobre si se retiró del todo.
  - El ACP se amplió para cubrir el descubrimiento de producto.
  - Forrester cifra en unos 30 los comerciantes de Shopify activos en Instant Checkout en febrero de 2026.
  - [Stellagent](https://stellagent.ai/insights/chatgpt-shopping-feature-deep-dive), [eesel](https://www.eesel.ai/blog/chatgpt-instant-checkout-2026), [Digital Applied](https://www.digitalapplied.com/blog/ai-agentic-commerce-discover-in-ai-buy-on-site-2026)
- **[terceros] Versiones del ACP:** de 2025-09-29 a 2026-01-30. La de abril de 2026 (2026-04-17) añade carrito, feed, pedidos, autenticación y objetos MCP. No se confirmó contra agenticcommerce.dev — [presenc.ai](https://presenc.ai/research/acp-merchant-adoption-tracker-2026), [Paz](https://www.paz.ai/glossary/chatgpt-product-feed-format)
- **[terceros, Profound, citado por Relevant Audience]** Las selecciones de producto integradas por feed pasaron del 8,26 % al 61,54 % entre el 10 de julio y principios de septiembre de 2026. Base: 1.757.723 ejecuciones de prompts de ChatGPT Shopping en julio de 2026 — [Relevant Audience](https://www.relevantaudience.com/ecommerce-marketing/chatgpt-shopping-product-feeds-profound-research/)
- **[terceros] Ads basados en feed:** lanzados el 12-05-2026 en EE. UU. — [Passionfruit](https://www.getpassionfruit.com/blog/chatgpt-product-feed-ads-what-retailers-need-to-know)
- **[terceros] Europa:**
  - Reino Unido abrió Ads el 06-06-2026. Lengow habla de autoservicio en EE. UU., Reino Unido y 31 mercados europeos desde el 24-08-2026; no confirmado por OpenAI.
  - Según Lengow, «OpenAI no ha publicado criterios de elegibilidad para el programa ChatGPT Shopping». El descubrimiento orgánico por feed está en beta limitada, mercado a mercado, sin fecha para España.
  - Carrefour (26-03-2026) usa una app a medida, no el feed.
  - [Lengow ES](https://www.lengow.com/es/conocer-mas/chatgpt-shopping-elegibilidad-calendario-y-como-preparar-su-feed), [Lengow Ads Europa](https://www.lengow.com/get-to-know-more/how-to-get-ready-for-chatgpt-ads-in-europe)

### Inferences
- Las fichas de producto llegan a ChatGPT por tres vías:
  1. **Feed o catálogo estructurado**: feed de OpenAI, Shopify Catalog o proveedores de metadatos. Es la vía de más peso en 2026 en EE. UU.
  2. **Índice propio de OAI-SearchBot y proveedores de búsqueda**, para citación y descubrimiento.
  3. **Lectura en tiempo real de la ficha**: ChatGPT-User o el lector de shopping research.
- Para una tienda española sin feed aprobado (lo probable en octubre de 2026), pesan las vías 2 y 3. Las dos consumen el HTML de la ficha.
- El papel exacto del JSON-LD Product/Offer de la página no lo documenta OpenAI. La expresión «structured metadata from … third-party providers» es compatible con que proveedores como los agregadores de Google Shopping lo extraigan, pero no está probado.

### Gaps
- No encontré documentación oficial de OpenAI que diga que lee o prioriza Schema.org/JSON-LD de las fichas.
- No hay confirmación oficial de la disponibilidad de shopping o del feed orgánico en España a octubre de 2026.
- No se pudo leer directamente el texto actual del anuncio de shopping research ni el del giro de marzo de 2026: openai.com devolvió 403.
- No se sabe si OAI-SearchBot o el lector de shopping research renderizan JS.

## 3. ChatGPT agent / cloud browser / ChatGPT Work y ChatGPT Atlas: navegador real, identificación, cookies, logins, geolocalización

### Takeaway
Los agentes de navegación de OpenAI usan un **Chromium real que renderiza**. Hay dos variantes:
- **Navegador en la nube** (ChatGPT agent, hoy «cloud browser» de ChatGPT Work): se identifica con UA de Chrome normal más **firmas Web Bot Auth** (`Signature-Agent: "https://chatgpt.com"`), sale de IPs de EE. UU. y envía `Accept-Language: en-US`.
- **Atlas** (navegador local, 21-10-2025): se presenta como Chrome de macOS sin marca propia y, según un proveedor, sin firma.

Ninguno de los dos corresponde al perfil «HTML sin JS».

### Cited Findings
- **[terceros, Simon Willison, 04-08-2025]** Petición de ChatGPT agent registrada en su servidor:
  - `User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36`, pero con `Sec-Ch-Ua-Platform: "Linux"`.
  - `Sec-Ch-Ua: "Chromium";v="138"`.
  - `Accept-Language: en-US,en;q=0.9`.
  - `Signature-Agent: "https://chatgpt.com"`, con `Signature-Input` (`tag="web-bot-auth"`, `alg="ed25519"`, que cubre `@authority`, `@method`, `@path` y `signature-agent`) y `Signature`.
  - `Cf-Ipcountry: US` (borde de Cloudflare en Seattle).
  - [Simon Willison](https://simonwillison.net/2025/Aug/4/chatgpt-agents-user-agent/)
- **[oficial, leído el 28-10-2026]** Directorio de claves de OpenAI: una clave Ed25519 con `"signature_agent":"https://chatgpt.com","purpose":"ai"`, `nbf` = 1735689600 (01-01-2025) y `exp` = 1793811370 (~nov. de 2026) — [chatgpt.com/.well-known/http-message-signatures-directory](https://chatgpt.com/.well-known/http-message-signatures-directory)
- **[oficial, art. 11845367 «ChatGPT agent allowlisting», citado por terceros; 403 en esta sesión]**
  - El navegador en la nube «uses Web Bot Auth to sign outbound HTTP requests», con `Signature-Agent` igual a https://chatgpt.com.
  - Figura como agente firmado en el directorio de Cloudflare (`chatgpt-agent`).
  - Akamai lo verifica.
  - [OpenAI Help (vía búsqueda)](https://help-lb.openai.com/en/articles/11845367-chatgpt-agent-allowlisting), [WorkOS](https://workos.com/blog/web-bot-auth-identify-ai-agents), [Castle](https://blog.castle.io/how-to-authenticate-openai-operator-requests-using-http-message-signatures/)
- **[oficial, art. 11752874, vía búsqueda] y [terceros, MacStories, ~26-08-2026]:**
  - «ChatGPT agent is no longer available». Se remite a ChatGPT Work y al «cloud browser».
  - El navegador en la nube corre en un ordenador remoto, sin acceso a pestañas, cookies ni contraseñas del dispositivo.
  - Las cookies persisten entre sesiones y se pueden borrar por sitio.
  - Desde el 25-08-2026 admite inicio de sesión mediante *takeover*: el usuario introduce las credenciales y el modelo no las ve.
  - Los CAPTCHA requieren intervención manual.
  - [OpenAI Help (vía búsqueda)](https://help.openai.com/en/articles/11752874-agent), [MacStories](https://www.macstories.net/?p=198275), [Notebookcheck](https://www.notebookcheck.net/ChatGPT-signs-in-to-your-accounts-now-and-stays-signed-in.1379126.0.html)
- **[terceros] ChatGPT Atlas** (lanzado el 21-10-2025):
  - En el lanzamiento, su UA era idéntico al de Chrome 141 de macOS, sin identificador propio — [Simon Willison](https://feeds.simonwillison.net/2025/Oct/21/introducing-chatgpt-atlas/)
  - Según HUMAN Security, usa la pila TLS/HTTP de Chrome y no tiene identidad criptográfica pública ni cadena de UA para robots.txt. Es la afirmación de un solo proveedor — [HUMAN Security](https://www.humansecurity.com/ai-agent/chatgpt-atlas/)
  - El modo agente de Atlas opera en la sesión local del usuario, con sus cookies e inicios de sesión — [Simon Willison](https://simonwillison.net/b/9060)

### Inferences
- El navegador en la nube es un Chromium real sobre Linux que ejecuta JS y renderiza. Hace clic e interactúa, y gestiona cookies, por lo que puede aceptar o rechazar banners de consentimiento.
- Por defecto se presenta como usuario de EE. UU. con `en-US`. Una tienda española con geodirección por IP o por `Accept-Language` podría servirle la versión internacional o en inglés.
- Atlas hereda la localización y el idioma reales del usuario, que en España serían IP española y `es-ES`.

### Gaps
- No hay documentación sobre cómo resuelven los agentes los banners de cookies (CMP) en las webs españolas. La interacción es posible, pero no se sabe si es una política fija.
- No se sabe si el cloud browser permite elegir país o idioma, ni si sale siempre de EE. UU. en 2026.
- No hay confirmación oficial de que Atlas no firme sus peticiones.

## 4. Localización: origen de las peticiones, Accept-Language y páginas por país

### Takeaway
Todas las evidencias sitúan el origen en EE. UU.:
- IPs de OpenAI con aspecto de Azure;
- centros de datos de Des Moines y Phoenix, según Vercel (2024);
- `Cf-Ipcountry: US` y `Accept-Language: en-US` en el agente, según Willison (2025).

OpenAI no documenta ni la región ni la cabecera de idioma de sus fetchers.

### Cited Findings
- «All AI crawlers we measured operate from U.S. data centers», y ChatGPT opera desde Des Moines y Phoenix (diciembre de 2024) — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- El agente envió `Accept-Language: en-US,en;q=0.9` desde un país detectado como US (agosto de 2025) — [Simon Willison](https://simonwillison.net/2025/Aug/4/chatgpt-agents-user-agent/)
- El feed de OpenAI fija `store_country` y las cargas estándar en US. Otros países requieren confirmación de OpenAI — [Product Feed Spec](https://developers.openai.com/commerce/specs/feed)

### Inferences
- Una auditoría que emule a OpenAI debería pedir la página desde un contexto no español (IP de EE. UU. y `Accept-Language: en-US`) para detectar geodirecciones, o al menos registrar si la ficha española depende de la IP o del idioma.
- Lo contrario, una petición española con `es-ES`, emula a Atlas o a un usuario, no a los fetchers del servidor.

### Gaps
- No hay fuente fiable sobre la `Accept-Language` de GPTBot, OAI-SearchBot y ChatGPT-User, ni sobre si OpenAI usa proxies regionales en Europa.

## 5. Recomendaciones de OpenAI a comerciantes y editores sobre legibilidad

### Takeaway
OpenAI no publica, en lo encontrado, ninguna recomendación del tipo «sirva el contenido sin JS». Sus indicaciones se limitan a tres cosas:
- permitir OAI-SearchBot en robots.txt para aparecer en búsqueda;
- usar el *allowlisting* del agente (Web Bot Auth) para no bloquear el navegador;
- enviar un feed de producto con URL públicas y estables.

La recomendación de servir el contenido en el HTML del servidor procede de terceros.

### Cited Findings
- Permitir OAI-SearchBot hace que el sitio aparezca en los resultados de búsqueda; robots.txt tarda unas 24 h en aplicarse — [OpenAI bots](https://developers.openai.com/api/docs/bots)
- URL de producto e imagen públicas, preferiblemente HTTPS, estables y que muestren la variante seleccionada; precio y disponibilidad al día — [Product Feed Spec](https://developers.openai.com/commerce/specs/feed)
- Codificar los caracteres inseguros de las URL; TLS 1.2 o superior en el puerto 443 para los endpoints del comerciante — [OpenAI Commerce llms-full](https://developers.openai.com/commerce/llms-full.txt)
- Vercel recomienda renderizar en servidor el contenido crítico porque los rastreadores de ChatGPT no ejecutan JS — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)

### Inferences
- Para una auditoría de octubre de 2026 en España, el perfil base «respuesta HTTP sin ejecutar JavaScript» es correcto para GPTBot, OAI-SearchBot y ChatGPT-User. En ChatGPT-User conviene distinguir el texto visible del HTML de los bloques `<script>` (JSON-LD), que según Resoneo no le llegan al modelo.
- Se necesita un **segundo perfil, renderizado en Chromium**, para el navegador en la nube y para Atlas. El primero emula EE. UU. y en-US con cookies nuevas; el segundo, el contexto local del usuario. La captura por CDP con Chrome real ya lo permite.
- El perfil renderizado no cubre los pasos interactivos que sí hacen estos agentes: aceptar banners, elegir variantes, iniciar sesión.
- El feed, que es el canal dominante en EE. UU., queda fuera del alcance de una auditoría de fichas.

### Gaps
- No se encontró ninguna guía oficial de OpenAI sobre JavaScript, renderizado en servidor, Schema.org o banners de consentimiento para editores o comerciantes.
- La página chatgpt.com/merchants no se pudo consultar en esta sesión.
