# Perfil de consumo de fichas de producto: Anthropic (Claude) y Perplexity (estado a 28-10-2026)

Notas de investigación. Convención: **[OFICIAL]** = documentación o blog del propio proveedor; **[TERCERO]** = medio, proveedor de seguridad o SEO; **[OBSERVADO]** = comprobado en esta sesión (28-10-2026) con consulta directa. Las fechas entre paréntesis son las de la fuente; lo anterior a 2026 se marca como tal.

## 1. Anthropic: ClaudeBot, Claude-User, Claude-SearchBot (y los antiguos anthropic-ai / Claude-Web): propósito, user agents, robots.txt, IP

### Takeaway
Anthropic documenta hoy tres agentes con token propio de robots.txt (ClaudeBot = entrenamiento, Claude-User = lectura a petición del usuario, Claude-SearchBot = calidad de búsqueda) y afirma que todos respetan robots.txt, incluido Claude-User; publica una lista de IP (bots.json) que sale de rangos estadounidenses (bloque propio de Anthropic sobre AWS y direcciones de Google Cloud). Los tokens antiguos anthropic-ai y Claude-Web ya no aparecen en la documentación vigente.

### Cited Findings
- [OFICIAL] El artículo de soporte (fechado 7-4-2026) enumera tres bots: **ClaudeBot** («collecting web content that could potentially contribute to their training»), **Claude-User** («supports Claude AI users»; bloquearlo «prevents our system from retrieving your content in response to a user query») y **Claude-SearchBot** («improve search result quality for users»; bloquearlo puede reducir la visibilidad en resultados) — [Anthropic Support](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
- [OFICIAL] Los bots de Anthropic «respect "do not crawl" signals» y honran «industry standard directives in robots.txt»; la regla debe repetirse en cada subdominio; Anthropic admite la extensión no estándar `Crawl-delay` (ejemplo con ClaudeBot) — [Anthropic Support](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
- [OFICIAL] El artículo no da las cadenas completas de user agent, solo los tokens; remite a la lista de IP `claude.com/crawling/bots.json` y advierte que bloquear por IP puede impedir que el bot lea robots.txt — [Anthropic Support](https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler)
- [OFICIAL/OBSERVADO] `bots.json` (creationTime 2026-10-20) contiene el bloque `216.73.216.0/22` y una docena de /32 en 34.162.x, 34.152.x, 34.153.x, 34.186.x, 136.79.x y 136.83.x — [bots.json](https://claude.com/crawling/bots.json). Según el registro ARIN (RDAP), 216.73.216.0–216.73.219.255 se llama «AWS-ANTHROPIC» y está registrado a Anthropic, PBC; 34.162.230.222 y 136.79.143.251 pertenecen a Google LLC (GOOGL-2) — [ARIN RDAP 216.73.216.1](https://rdap.arin.net/registry/ip/216.73.216.1), [ARIN RDAP 34.162.230.222](https://rdap.arin.net/registry/ip/34.162.230.222)
- [TERCERO] La cadena de Claude-User se publica habitualmente como `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Claude-User/1.0; +Claude-User@anthropic.com)`; los directorios no coinciden en la dirección de contacto (`claude-user@anthropic.com`, `Claude-User@anthropic.com`, `mailto:support@anthropic.com`) — [CL SEO](https://chrisleverseo.com/user-agents/claude-user/), [Cloudflare Radar (directorio)](https://radar.cloudflare.com/bots/directory/claude-user), [Known Agents](https://knownagents.com/agents/claude-user)
- [TERCERO] Una incidencia de Claude Code informa que, desde la v2.1.83, la herramienta WebFetch de Claude Code también se identifica como `Claude-User` en el User-Agent — [claudeissues.com #38568](https://claudeissues.com/issue/38568-docs-document-that-webfetch-identifies-as-claude-user-so-site-operators-can-allo)
- [TERCERO] Como el user agent es autodeclarado, cualquier bot puede hacerse pasar por Claude-User; la coincidencia en logs no prueba identidad (de ahí la verificación por IP) — [CL SEO](https://chrisleverseo.com/user-agents/claude-user/)

### Inferences
- A diferencia de Perplexity (sección 4), Anthropic declara que **también su fetcher a petición del usuario respeta robots.txt**; la documentación de la API lo confirma: la herramienta web fetch devuelve `url_not_allowed` cuando robots.txt lo impide (sección 2). Para la auditoría, un `Disallow` para `Claude-User` equivale a disponibilidad nula en Claude para esa ficha.
- Todas las IP publicadas son de registro estadounidense (ARIN). Una ficha española que geolocaliza por IP (redirección a otro país, precio en otra moneda, «no disponible en tu región», banner de consentimiento distinto) puede servir a Claude una versión distinta de la que ve un comprador en España.

### Gaps
- No encontré documentación oficial vigente con la cadena completa de ClaudeBot ni de Claude-SearchBot; no la incluyo.
- No encontré fuente oficial actual sobre **anthropic-ai** y **Claude-Web**: el artículo de soporte vigente (7-4-2026) no los menciona. Por lo que recuerdo (no verificado en esta sesión), eran tokens antiguos (hasta 2024) que Anthropic dejó de usar; conviene tratarlos solo como compatibilidad hacia atrás en robots.txt.
- No hay documentación sobre si Claude-SearchBot renderiza JavaScript ni sobre cómo se relaciona con el índice que usa la búsqueda de Claude (sección 2).
- Anthropic no documenta firma criptográfica (Web Bot Auth) para sus bots; la verificación documentada es IP + user agent. No pude consultar la ficha de Cloudflare Radar (403).

## 2. Anthropic: ¿web fetch y web search ejecutan JavaScript o leen HTML/texto? ¿Qué índice respalda la búsqueda?

### Takeaway
Oficialmente, la herramienta web fetch de la API **no admite sitios renderizados con JavaScript** y devuelve a Claude **texto extraído** (`text/plain`), no el HTML; para JS remite a una herramienta de navegador que ejecuta el cliente. La búsqueda web no nombra proveedor en la documentación, pero la lista de subencargados de Anthropic incluye **Brave Search** (desde 19-3-2025) y **turbopuffer** (desde 6-5-2026) en «Web Search».

### Cited Findings
- [OFICIAL] «The web fetch tool currently does not support websites dynamically rendered with JavaScript. For pages that need a real browser (JavaScript rendering, clicking, or filling forms), consider the browser use tool, a client tool where your application drives the browser…» — [Claude Docs, Web fetch tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)
- [OFICIAL] Funcionamiento: «The API retrieves the full text content from the specified URL»; el resultado es un bloque `document` con `source.type: "text"`, `media_type: "text/plain"` y `data: "Full text content of the article..."`; los PDF se devuelven en base64. Tipos admitidos: «only text, HTML, and PDF» — [Claude Docs, Web fetch tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)
- [OFICIAL] El código de error `url_not_allowed` cubre URL bloqueadas por filtros de dominio «or by Anthropic-side restrictions, such as private addresses, `robots.txt`, and URLs that appear to contain a credential» — [Claude Docs, Web fetch tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)
- [OFICIAL] Hay caché del lado de Anthropic: «The content returned might not always reflect the latest version available at the URL»; desde `web_fetch_20260309` existe `use_cache: false` para forzar contenido fresco. `max_content_tokens` trunca el texto. Referencia de tamaño: página media de 10 kB ≈ 2.500 tokens — [Claude Docs, Web fetch tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)
- [OFICIAL] Versiones vigentes: `web_fetch_20250910` (básica), `20260209` (filtrado dinámico: Claude escribe y ejecuta código para filtrar el contenido obtenido antes de que entre en el contexto, «Processing structured data from webpages»), `20260309` (+ cache bypass), `20260318` (+ response inclusion). Solo puede leer URL que ya aparecieron en la conversación (mensaje del usuario, resultados de herramientas o de búsqueda) — [Claude Docs, Web fetch tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool)
- [OFICIAL] La búsqueda web devuelve por resultado `url`, `title`, `page_age` y `encrypted_content` (contenido cifrado que solo la API descifra); las citas incluyen `cited_text` de hasta 150 caracteres. No se nombra el proveedor del índice. Admite `user_location` aproximada con `city`, `region`, `country` (ISO 3166-1 alfa-2) y `timezone` (IANA). Precio: 10 USD por 1.000 búsquedas — [Claude Docs, Web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)
- [TERCERO] TechCrunch (21-3-2025) informó de que las pruebas apuntaban a Brave como motor de la búsqueda de Claude; Simon Willison encontró un parámetro «BraveSearchParams» en la función de búsqueda — [TechCrunch](https://techcrunch.com/2025/03/21/anthropic-appears-to-be-using-brave-to-power-web-searches-for-its-claude-chatbot/embed/), [Simon Willison](https://simonwillison.net/b/8583)
- [TERCERO, sobre fuente oficial] Según Xponent21 (2-7-2026, actualizado 16-7-2026), la lista de subencargados de Anthropic incluye Brave Search desde el 19-3-2025 (seguía en la lista el 2-7-2026, «scoped to all products») y **turbopuffer** desde el 6-5-2026 en la categoría «Web Search» (base de datos vectorial y de texto completo), con un papel no público: «we cannot confirm from public sources exactly how that component is used» — [Xponent21](https://xponent21.com/insights/claude-web-search-brave-turbopuffer/)
- [TERCERO] Vercel/MERJ (17-12-2024, dato antiguo): «none of the major AI crawlers currently render JavaScript», incluido ClaudeBot; Claude descarga ficheros JS (23,84 % de sus peticiones en nextjs.org) pero no los ejecuta; 370 millones de descargas de ClaudeBot en un mes en la red de Vercel; reparto en nextjs.org: imágenes 35,17 %, JS 23,84 % — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- [TERCERO] Prueba de botpresso: la lectura de Claude Pro devolvió solo texto extraído; el propio Claude advirtió que el autor o el marcado Schema «may exist in the raw HTML» pero no le llegaba — [botpresso](https://botpresso.com/ai-assistants-schema-markup-test/)

### Inferences
- El perfil base «respuesta HTTP sin ejecutar JavaScript» describe bien **qué llega al servidor** (no se ejecuta JS), pero **no lo que lee Claude**: la API convierte la respuesta en texto plano antes de pasarla al modelo. Lo que no sobrevive a esa extracción (bloques `<script type="application/ld+json">`, atributos, contenido oculto, posiblemente tablas mal estructuradas) es plausible que no llegue al modelo (corroborado indirectamente por botpresso y searchVIU, sección 7). Un perfil más fiel sería: HTML inicial sin JS → extracción de texto visible.
- [OBSERVADO, por la descripción de la propia herramienta en este entorno] La herramienta WebFetch de Claude Code «converts the page to markdown» y responde con un modelo pequeño y rápido sobre ese markdown: es otra capa más de reducción del contenido distinta de la API.
- La búsqueda web de Claude no lee la página en el momento de la consulta: Claude ve fragmentos del índice (Brave, y quizá turbopuffer) y solo lee la ficha si después usa web fetch. Lo que el índice de Brave capturó (y si renderiza JS) condiciona el descubrimiento, no la lectura.
- La caché de web fetch implica que Claude puede leer una versión antigua de un precio o de la disponibilidad.

### Gaps
- La documentación de la API no dice qué User-Agent, Accept-Language ni geolocalización usa el fetcher del servidor; no hay prueba oficial de que la API web fetch salga como `Claude-User` (sí lo dicen fuentes de terceros para Claude Code).
- No hay documentación del método exacto de extracción HTML → texto (si conserva tablas, `alt`, `<noscript>` o el contenido de `<script>`).
- No consta oficialmente si claude.ai (app de consumo) usa exactamente la misma herramienta que la API.
- No encontré información sobre si el rastreador de Brave renderiza JavaScript; Xponent21 solo indica que no usa un user agent diferenciado y que no rastrea lo que Googlebot no puede rastrear.

## 3. Anthropic: Claude in Chrome, browser use y computer use (navegador real)

### Takeaway
Las vías de agente de Anthropic usan un navegador real: Claude in Chrome actúa en el Chrome del usuario (disponibilidad general anunciada el 26-8-2026), y la herramienta browser use de la API la ejecuta el cliente en su propio navegador. En ambos casos se ejecuta JavaScript y Claude no recibe el HTML: recibe el **árbol de accesibilidad, el texto visible y capturas de pantalla**.

### Cited Findings
- [OFICIAL] Claude for Chrome se anunció como piloto el 25-8-2025 («giving Claude the ability to see what you're looking at, click buttons, and fill forms»); después se abrió a Max (24-11-2025) y a Pro, Team y Enterprise (18-12-2025). Permisos por sitio, que el usuario concede o revoca; listas permitidas y bloqueadas para administradores; Claude pide confirmación antes de «publishing, purchasing, or sharing personal data»; categorías bloqueadas: «financial services, adult content, and pirated content» — [Claude blog](https://claude.com/blog/claude-for-chrome)
- [OFICIAL] Entre los riesgos, el blog menciona «hidden malicious form fields in a webpage's Document Object Model (DOM) invisible to humans»: el agente trabaja sobre la página renderizada — [Claude blog](https://claude.com/blog/claude-for-chrome)
- [TERCERO] Según el índice del blog de Anthropic, Claude in Chrome alcanzó disponibilidad general el 26-8-2026; otras fuentes dan fechas anteriores (junio o julio de 2026) sin verificar; solo Chrome, solo planes de pago — [Gigazine](https://gigazine.net/gsc_news/en/20260827-claude-chrome-available/), [techbytes](https://techbytes.app/posts/claude-in-chrome-is-generally-available/)
- [OFICIAL] La herramienta browser use es un conjunto de herramientas de cliente: «Your application runs every call against its own browser automation; nothing runs on Anthropic's side», y por tanto «the sites Claude visits see your executor's network identity». Canales de lectura: `read_page`/`find` (árbol de accesibilidad como texto, con referencias `[ref_2]`, hasta 50.000 caracteres), `get_page_text` («the page's visible text as plain text, prioritizing the main article content»), `screenshot`/`zoom` (imagen). Recomendación a quien la implemente: «Build page reads from what the page renders (the accessibility tree or visible text), not raw DOM source, so hidden text doesn't reach Claude» — [Claude Docs, Browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool)

### Inferences
- En el modo agente, el contenido inyectado por JavaScript **sí** está disponible, pero el JSON-LD (que no se renderiza) y el texto oculto **no** llegan por diseño: Anthropic recomienda expresamente excluir el DOM oculto.
- Claude in Chrome usa el perfil, las cookies, el consentimiento ya dado, la IP y el idioma del usuario: para un comprador en España, ve la versión española de la ficha. Es el perfil más parecido a la captura de la auditoría con Chrome real por CDP, pero exige leer el árbol de accesibilidad o el texto visible, no el HTML.
- Este modo implica navegación interactiva (clics, formularios), que queda fuera del perímetro de la auditoría («sin navegación interactiva»); sí sirve como referencia de qué ve el agente en la carga inicial renderizada.

### Gaps
- No encontré documentación oficial de soporte (support.claude.com) que describa exactamente cómo Claude in Chrome lee la página (si es igual que la herramienta browser use: árbol de accesibilidad, texto y capturas). Es razonable suponerlo, pero no consta.
- No hay datos sobre el User-Agent de Claude in Chrome (es el Chrome del usuario, presumiblemente sin marca propia) ni sobre firma Web Bot Auth.

## 4. Perplexity: PerplexityBot, Perplexity-User, índice propio y ejecución de JavaScript

### Takeaway
Perplexity documenta dos agentes: PerplexityBot (rastreador del índice de búsqueda, que respeta robots.txt) y Perplexity-User (lectura a petición del usuario, que «generally ignores robots.txt»), ambos con IP de AWS en Virginia del Norte (EE. UU.). Tiene índice propio (más de 200.000 millones de URL, sept. de 2025). Las pruebas sobre si renderiza JavaScript se contradicen: Vercel (dic. de 2024) dice que no; searchVIU (oct. de 2025) observó un precio inyectado por JS en las respuestas basadas en su índice.

### Cited Findings
- [OFICIAL] **PerplexityBot**: «designed to surface and link websites in search results on Perplexity» y «not used to crawl content for AI foundation models». UA: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; PerplexityBot/1.0; +https://perplexity.ai/perplexitybot)`. IP: `perplexitybot.json` — [Perplexity Docs, Bots](https://docs.perplexity.ai/guides/bots)
- [OFICIAL] **Perplexity-User**: «supports user actions within Perplexity»; visita páginas para responder y enlazarlas; «not used for web crawling or to collect content for training». UA: `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Perplexity-User/1.0; +https://perplexity.ai/perplexity-user)`. robots.txt: «Since a user requested the fetch, this fetcher generally ignores robots.txt rules». IP: `perplexity-user.json`. Los cambios en robots.txt pueden tardar hasta 24 h en reflejarse. La guía de WAF se basa en UA + IP; no menciona Web Bot Auth. La página no tiene fecha — [Perplexity Docs, Bots](https://docs.perplexity.ai/guides/bots)
- [OFICIAL/OBSERVADO] `perplexity-user.json` (creationTime 2025-10-17) contiene 44.208.221.197/32, 34.193.163.52/32, 18.97.21.0/30 y 18.97.43.80/29; `perplexitybot.json` (creationTime 2025-02-07), ocho prefijos en 107.20.x, 3.x y 18.x — [perplexity-user.json](https://www.perplexity.com/perplexity-user.json), [perplexitybot.json](https://www.perplexity.com/perplexitybot.json). Según ARIN, 44.208.221.197 pertenece a «Amazon Data Services Northern Virginia» (AMAZON-IAD); 18.97.21.1 y 107.20.236.150, a Amazon — [ARIN RDAP 44.208.221.197](https://rdap.arin.net/registry/ip/44.208.221.197), [ARIN RDAP 107.20.236.150](https://rdap.arin.net/registry/ip/107.20.236.150)
- [OFICIAL] Índice propio: la API de búsqueda (sept. de 2025) da acceso a «an index covering hundreds of billions of webpages», el mismo del motor de respuestas; el artículo de investigación habla de más de 200.000 millones de URL únicas, flotas de rastreo e indexación de «tens of thousands of CPUs» y «tens of thousands of index update requests each second», y afirma que «PerplexityBot, our search crawler, complies with explicit limits set forth in robots.txt files» — [Perplexity Research](https://research.perplexity.ai/articles/architecting-and-evaluating-an-ai-first-search-api), [Perplexity blog](https://hub-prod.perplexity.ai/hub/blog/introducing-the-perplexity-search-api)
- [TERCERO] Vercel/MERJ (17-12-2024, dato antiguo): PerplexityBot no renderiza JavaScript — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- [TERCERO] searchVIU (pruebas de octubre de 2025, publicado el 2-12-2025): Perplexity respondió desde su índice, no con una lectura directa; antes de la indexación encontró 0/8 precios y después 1/8, **solo el precio inyectado por JavaScript (12,99 €)**, no el estático de 5,99 €; el autor lo interpreta como señal de que los rastreadores ejecutan JS al indexar (hipótesis, una sola página de prueba) — [searchVIU](https://www.searchviu.com/en/schema-markup-and-ai-in-2025-what-chatgpt-claude-perplexity-gemini-really-see/). Esto contradice a [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler) (fechas y métodos distintos).

### Inferences
- Perplexity responde a menudo **desde su índice** (contenido rastreado antes, quizá antiguo), no desde una lectura en vivo: el perfil de consumo tiene dos momentos, la indexación con PerplexityBot y la lectura en vivo, ocasional, con Perplexity-User.
- Como Perplexity-User ignora en general robots.txt, un `Disallow` no garantiza su ausencia; para la auditoría, robots.txt no es un buen indicador de la disponibilidad para Perplexity en las lecturas a petición del usuario (sí lo es para PerplexityBot).
- Todas las IP publicadas están en AWS us-east-1 (Virginia): mismo riesgo de geolocalización que con Anthropic.
- Dada la contradicción sobre JS, conviene que la auditoría capture ambos estados (HTML inicial y DOM renderizado) y registre en qué difieren los hechos comerciales, en lugar de fijar uno solo como «lo que ve Perplexity».

### Gaps
- No hay documentación oficial de Perplexity sobre si PerplexityBot o Perplexity-User ejecutan JavaScript, qué formato pasan al modelo ni qué Accept-Language usan.
- La frase «controls which sites these user requests can access» de la documentación no aclara del todo el comportamiento de Perplexity-User con robots.txt.
- No encontré si Perplexity usa además índices de terceros (por ejemplo, Bing o Google) como complemento en 2026.

## 5. Perplexity: navegador Comet y compras (Shopping, Buy with Pro, Merchant Program, Instant Buy con PayPal)

### Takeaway
Comet es un navegador Chromium con asistente lateral que lee la página abierta (gratuito en todo el mundo desde el 2-10-2025). Las compras de Perplexity se basan sobre todo en **catálogos y feeds de comercios** (Merchant Program, «store sync» de PayPal), no en leer la ficha HTML, y las funciones de pago dentro del chat (Buy with Pro, Instant Buy) son **solo para EE. UU.** según las fuentes encontradas.

### Cited Findings
- [TERCERO] Comet se lanzó el 9-7-2025 para suscriptores Max (200 USD/mes) y pasó a ser gratuito en todo el mundo el 2-10-2025 («will always be free»); el asistente lateral «see[s] what's on the web page» que tiene abierta el usuario; el plan gratuito tiene acceso limitado al agente — [TechCrunch](https://techcrunch.com/2025/07/09/perplexity-launches-comet-an-ai-powered-web-browser/), [Engadget](https://engadget.com/ai/perplexitys-comet-ai-browser-is-now-free-for-everyone-170017509.html), [Tom's Guide](https://www.tomsguide.com/ai/perplexity/perplexitys-ai-browser-comet-is-now-free-for-everyone-heres-how-to-download-it)
- [OFICIAL] Perplexity Shopping y el **Perplexity Merchant Program** se anunciaron el 18-11-2024 (dato antiguo) para usuarios de EE. UU., con «Buy with Pro» para suscriptores Pro y la intención de ampliarlo a otros mercados — [Perplexity blog, Shop like a Pro](https://hub-prod.perplexity.ai/hub/blog/shop-like-a-pro), [MediaPost](https://www.mediapost.com/publications/article/401224/perplexity-takes-on-google-intros-shopping-for-u.html)
- [OFICIAL, PayPal] Instant Buy (25-11-2025): compra dentro del chat de Perplexity para consumidores de EE. UU.; el comercio sigue siendo el vendedor; socios iniciales Abercrombie & Fitch, Fabletics, Ashley Furniture y Newegg; servicios de PayPal para comercios: «store sync» (hace descubrible el catálogo del comercio en Perplexity) y «agent ready» — [PayPal Newsroom](https://newsroom.paypal-corp.com/2025-11-PayPal-and-Perplexity-Launch-Instant-Buy), [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2025/paypal-and-perplexity-debut-instant-buy-ahead-of-black-friday-shopping)
- [TERCERO, sin verificar] Guías de proveedores dicen que el Merchant Program acepta feeds CSV con la especificación de Google Merchant Center y que las fichas de producto se alimentan de feeds vivos (Shopify, PayPal, Firmly.ai); una fuente griega cita la compra de Cymbio por PayPal (enero de 2026) y «5.000 comercios»: dato único, sin confirmar — [Alhena](https://alhena.ai/blog/perplexity-shopping-merchants-setup-guide/), [secnews.gr](https://www.secnews.gr/en/725171/paypal-perplexity-instant-buy-agentic-commerce-2026/)

### Inferences
- Para fichas españolas, la vía de compra de Perplexity (feeds y PayPal) no está disponible según las fuentes; Perplexity lee esas fichas como contenido web (índice o Perplexity-User) y, si el usuario lo usa, a través de Comet. Esto corresponde al ámbito **Catálogos distribuidos** del modelo, no a Web.
- Comet, como Claude in Chrome, es un navegador real del usuario (JS, cookies, IP y idioma de España).

### Gaps
- No encontré documentación oficial actual (2026) del Merchant Program (requisitos del feed, países) ni de ampliación de Instant Buy o Shopping a España o a la UE.
- Un resultado de búsqueda menciona una vulnerabilidad de «indirect prompt injection» en Comet descubierta por investigadores de Brave (2025), lo que indicaría que el agente procesa el contenido de la página como entrada; no leí la fuente primaria y no la cito como hecho.
- No hay fuente oficial sobre cómo lee la página el agente de Comet (DOM, árbol de accesibilidad o capturas) ni sobre su User-Agent (presumiblemente el de un Chrome normal).

## 6. La acusación de Cloudflare (agosto de 2025) por rastreo encubierto y la respuesta de Perplexity; robots.txt en lecturas a petición del usuario

### Takeaway
Cloudflare (4-8-2025) acusó a Perplexity de pasar, cuando la bloqueaban, a un user agent genérico de Chrome en macOS con IP y ASN fuera de sus rangos, y la retiró de su lista de bots verificados. Perplexity atribuyó ese tráfico a BrowserBase (un servicio de navegadores en la nube que usa ocasionalmente) y defendió que las lecturas a petición del usuario no están sujetas a robots.txt. La disputa no está resuelta por una fuente independiente.

### Cited Findings
- [TERCERO, Cloudflare] Método: dominios nuevos, nunca indexados, con robots.txt que prohibía todo y reglas WAF contra PerplexityBot y Perplexity-User; Perplexity respondió con detalle sobre su contenido. El rastreador no declarado usó un UA de «Chrome 124» sobre macOS (`Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)…`), IP fuera de los rangos publicados y rotación de ASN, observado en «decenas de miles de dominios». Volúmenes: declarado «20-25m daily requests», no declarado «3-6m daily requests». Cloudflare dice que Perplexity ignoró robots.txt o no lo descargó (RFC 9309). Medidas: retirada del estado de bot verificado y firmas en la regla gestionada de bloqueo de rastreo IA (también en planes gratuitos) — [Cloudflare blog](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)
- [TERCERO, Cloudflare] Comparación: en la misma prueba, ChatGPT-User descargó robots.txt y se detuvo ante el `Disallow`; ChatGPT Agent firma sus peticiones con Web Bot Auth — [Cloudflare blog](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)
- [OFICIAL, Perplexity] Respuesta (agosto de 2025): los agentes a petición del usuario leen solo cuando una persona pregunta algo concreto y «do not store the information or train with it»; Cloudflare confundió con su tráfico «3-6M daily requests» de BrowserBase, que Perplexity usa «only occasionally», con menos de 45.000 peticiones diarias; lo llama «a basic traffic analysis failure»; justifica no aplicar robots.txt por analogía con los «user-triggered fetchers» de Google — [Perplexity blog](https://www.perplexity.ai/hub/blog/agents-or-bots-making-sense-of-ai-on-the-open-web)
- [TERCERO] Cloudflare replicó que Perplexity intentaba desviar la atención «broadening the discussion to all AI agents» — [TechRadar](https://www.techradar.com/pro/perplexity-hits-back-after-cloudflare-slams-its-online-scraping-tools), [Search Engine Journal](https://www.searchenginejournal.com/cloudflare-delists-and-blocks-perplexity-from-crawling-websites/552899/)
- [OFICIAL] La documentación vigente de Perplexity mantiene que Perplexity-User «generally ignores robots.txt rules» — [Perplexity Docs, Bots](https://docs.perplexity.ai/guides/bots)

### Inferences
- Que Perplexity use navegadores en la nube (BrowserBase, según su propia respuesta) para «tareas especializadas» indica que **parte de sus lecturas puede hacerse con un navegador real que ejecuta JS** y con un user agent de Chrome indistinguible. El perfil de Perplexity no es uno solo.
- Para la auditoría: las fichas tras un WAF o anti-bot (Cloudflare, Akamai, DataDome), habituales en el ecommerce español grande, pueden bloquear a Perplexity desde agosto de 2025 por la regla gestionada de Cloudflare. La disponibilidad real para Perplexity depende de la configuración anti-bot del comercio, no solo de robots.txt.

### Gaps
- No encontré verificación independiente (ni de Cloudflare ni de terceros) posterior a agosto de 2025 sobre si Perplexity cambió de conducta, volvió a ser bot verificado o adoptó Web Bot Auth.
- No hay datos públicos de cuántas lecturas de Perplexity pasan por BrowserBase ni con qué configuración (JS, idioma, IP).

## 7. ¿Leen estos sistemas JSON-LD / Schema.org de la página?

### Takeaway
Ni Anthropic ni Perplexity tienen una declaración oficial sobre el uso de JSON-LD. Las pruebas empíricas de terceros (pocas y de calidad limitada) indican que **en la lectura directa, Claude no recibe el JSON-LD** (solo texto extraído) y que Perplexity responde desde su índice sin evidencia de usar Schema; un experimento informal sugiere que, cuando el JSON-LD llega al modelo, se trata como texto, no como datos estructurados.

### Cited Findings
- [OFICIAL, por omisión] La documentación de web fetch describe la salida como `text/plain` («Full text content») y no menciona datos estructurados; la de browser use recomienda leer solo lo renderizado (árbol de accesibilidad o texto visible), lo que excluye el JSON-LD — [Claude Docs, Web fetch tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-fetch-tool), [Claude Docs, Browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool)
- [TERCERO] searchVIU (octubre de 2025): «JSON-LD Schema Markup is NOT extracted by ANY system during direct fetch»; Claude, en lectura directa, encontró 0/8 precios («I couldn't find any prices displayed on the page. The pricing information may be loaded dynamically...»), ni siquiera los visibles; Perplexity (índice) solo encontró el precio inyectado por JS. Advertencias: una sola página, proveedor de servicios SEO, explicaciones hipotéticas — [searchVIU](https://www.searchviu.com/en/schema-markup-and-ai-in-2025-what-chatgpt-claude-perplexity-gemini-really-see/)
- [TERCERO] Mark Williams-Cook puso la dirección de una empresa ficticia solo dentro de un JSON-LD inválido; ChatGPT y Perplexity la extrajeron, lo que se interpreta como lectura del marcado **como texto** de la página — [Search Engine Roundtable](https://www.seroundtable.com/chatgpt-perplexity-structured-data-text-40862.html)
- [TERCERO] Otterly: al pedir a siete plataformas que leyeran el Schema de una página, Claude afirmó que no había marcado (evidencia débil: se basa en lo que dicen los propios modelos) — [Otterly](https://otterly.ai/blog/schema-markup-real-impact-ai-search/)
- [TERCERO] botpresso: la lectura de Claude devolvió solo texto extraído; el Schema «may exist in the raw HTML» pero no le llegaba — [botpresso](https://botpresso.com/ai-assistants-schema-markup-test/)
- [TERCERO] Estudio de Ahrefs (1.885 páginas que añadieron JSON-LD): cambios en las citas de AI Mode y ChatGPT indistinguibles del ruido (no midió Claude ni Perplexity por separado; agrupa tipos de Schema) — [AuthorityTech, sobre Ahrefs](https://authoritytech.io/curated/schema-markup-ai-citations-ahrefs-study-2026)

### Inferences
- Para el perfil de lectura en vivo de Claude, la evidencia apoya que **Web Schema.org no contribuye** a lo que el modelo lee (o solo como texto, si la extracción conservara los `<script>`, que no parece ser el caso). Para el índice de Perplexity o de Brave, que el JSON-LD se use al indexar es posible pero no está probado.
- Esto refuerza la separación del modelo entre los ámbitos Web y Web Schema.org: su valor de consumo difiere según el agente, y no debe suponerse que una IA «lee» un hecho porque esté en el JSON-LD.

### Gaps
- No existe declaración oficial de Anthropic ni de Perplexity sobre el uso de Schema.org o JSON-LD en el rastreo, la indexación o la lectura.
- No encontré pruebas controladas y reproducibles de 2026 que aíslen Claude-SearchBot o PerplexityBot frente al JSON-LD.

## 8. Cookies y consentimiento, geolocalización e IP, Accept-Language y fichas de un país (España)

### Takeaway
Ningún proveedor documenta cookies, consentimiento ni Accept-Language de sus fetchers de servidor. Lo verificable es que **todas las IP publicadas de Anthropic y Perplexity son estadounidenses** (Anthropic/AWS, Google Cloud, AWS Virginia), que la búsqueda de Claude admite una ubicación aproximada (`country: "ES"`) para localizar resultados, y que los agentes de navegador (Claude in Chrome, Comet, browser use) heredan la IP, el idioma y las cookies del usuario o del entorno que los ejecuta.

### Cited Findings
- [OFICIAL/OBSERVADO] IP de Anthropic: bloque AWS-ANTHROPIC (Anthropic, PBC) más direcciones de Google LLC, según ARIN — [bots.json](https://claude.com/crawling/bots.json), [ARIN RDAP 216.73.216.1](https://rdap.arin.net/registry/ip/216.73.216.1), [ARIN RDAP 136.79.143.251](https://rdap.arin.net/registry/ip/136.79.143.251)
- [OFICIAL/OBSERVADO] IP de Perplexity-User y PerplexityBot: Amazon (AMAZON-IAD, Virginia del Norte; AMAZON-EC2) — [perplexity-user.json](https://www.perplexity.com/perplexity-user.json), [ARIN RDAP 44.208.221.197](https://rdap.arin.net/registry/ip/44.208.221.197), [ARIN RDAP 18.97.21.1](https://rdap.arin.net/registry/ip/18.97.21.1)
- [OFICIAL] Búsqueda web de Claude: `user_location` con `type: "approximate"`, `city`, `region`, `country` (ISO 3166-1 alfa-2, que se rechaza con 400 si no se admite) y `timezone` (IANA) — [Claude Docs, Web search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)
- [OFICIAL] Browser use: «the sites Claude visits see your executor's network identity» — [Claude Docs, Browser use tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool)
- [OFICIAL/TERCERO] Funciones de compra de Perplexity limitadas a EE. UU. (Shopping 2024, Instant Buy 2025) — [Perplexity blog](https://hub-prod.perplexity.ai/hub/blog/shop-like-a-pro), [PayPal Newsroom](https://newsroom.paypal-corp.com/2025-11-PayPal-and-Perplexity-Launch-Instant-Buy)

### Inferences
- Un fetcher de servidor sin estado (Claude-User, web fetch de la API, Perplexity-User, PerplexityBot) llega **sin cookies y sin consentimiento**: recibe la primera respuesta, con el banner de la CMP en el HTML si se sirve desde el servidor, y sin el contenido que dependa de aceptar cookies o de JS. Un muro de consentimiento o un intersticial de país en el servidor pueden dejar la ficha sin hechos comerciales para estos agentes.
- Por la IP estadounidense, una ficha .es con geolocalización puede redirigir a una tienda de EE. UU. o internacional, mostrar otra moneda o idioma, o bloquear. La auditoría, que captura desde España, puede estar viendo una versión **mejor** que la que recibe la IA. Conviene registrar para cada ficha si la respuesta cambia según el país de origen de la IP (y el Accept-Language), y no suponer que la versión española es la que se consume.
- Los agentes de navegador sí ven la versión española (IP, idioma y cookies del usuario); es el único perfil cuyo contexto coincide con el del comprador en España.

### Gaps
- No hay documentación ni pruebas encontradas sobre el Accept-Language que envían Claude-User, el web fetch de la API, PerplexityBot o Perplexity-User.
- No encontré pruebas empíricas del comportamiento de estos agentes ante muros de consentimiento (CMP) ni ante redirecciones geográficas en ecommerce europeo.
- No consta si `user_location` de la búsqueda de Claude afecta a la lectura posterior con web fetch (por diseño parece afectar solo a la ordenación de los resultados de búsqueda).
