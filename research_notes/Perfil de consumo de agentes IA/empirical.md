# Evidencia empírica: cómo obtienen y leen las páginas los crawlers y agentes de IA (estado a 28-10-2026)

Notas para decidir el perfil de consumo de la auditoría de fichas de producto de ecommerce españoles «sin navegación interactiva». Recordatorio de contexto: hoy la captura usa Chrome real por CDP y guarda la respuesta HTTP en bruto y el DOM tras la carga; el perfil base es «respuesta HTTP sin ejecutar JavaScript».

Convenciones: cada hecho lleva la fecha de su fuente. **[Medido]** significa que hay experimento o datos de logs; **[Opinión/doc]** significa recomendación, documentación del proveedor o interpretación. Muchas fuentes de 2026 son blogs de proveedores con interés comercial (detección de bots, herramientas GEO). Lo indico cuando es relevante.

## 1. Ejecución de JavaScript: ¿qué crawlers y fetchers renderizan? ¿Se comportan distinto los fetchers que lanza el usuario y los crawlers de entrenamiento?

### Takeaway
La evidencia sigue indicando que los fetchers que lanza el usuario (ChatGPT-User, Claude-User, Perplexity-User) y los crawlers de entrenamiento de OpenAI, Anthropic, Perplexity, Meta y ByteDance leen solo el HTML inicial. Hay excepciones medidas:
- Googlebot (y con él Gemini, AI Overviews y AI Mode), Applebot y Bing renderizan, Bing solo en parte.
- Mistral y los asistentes chinos renderizan en el fetch en vivo (test de junio de 2026).
- Hay indicios de octubre de 2026, de un solo sitio, de que OAI-SearchBot hace un renderizado diferido con Chrome headless unos 30 minutos después de pedir el HTML.

Por tanto, el perfil «HTML sin JS» representa bien la lectura en vivo de los grandes asistentes de EE. UU. Pero los índices que alimentan sus respuestas pueden contener contenido renderizado.

### Cited Findings

**Vercel/MERJ, 17-12-2024 [Medido]**
- Método: monitorización de nextjs.org y de la red de Vercel durante varios meses, validada en dos bolsas de empleo (Resume Library, en Next.js, y CV Library, monolítica). Microsoft Copilot quedó excluido por no tener user-agent propio. Autores: Zecchini, Moore, Ubl y Siddle. — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- Volumen en un mes en la red de Vercel: Googlebot 4.500 M de fetches, GPTBot 569 M, Claude 370 M, AppleBot 314 M, PerplexityBot 24,4 M. GPTBot, Claude, AppleBot y PerplexityBot suman unos 1.300 M (≈28 % de Googlebot). — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- Ninguno de los crawlers de OpenAI (OAI-SearchBot, ChatGPT-User, GPTBot), Anthropic (ClaudeBot), Meta (Meta-ExternalAgent), ByteDance (Bytespider) ni Perplexity (PerplexityBot) renderiza JS. CCBot tampoco. Gemini sí renderiza, sobre la infraestructura de Google, y AppleBot también, con un crawler basado en navegador. — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- Descargan ficheros JS pero no los ejecutan: son el 11,50 % de las peticiones de ChatGPT y el 23,84 % de las de Claude. — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- Tipos de contenido:
  - ChatGPT: 57,70 % de sus fetches son HTML.
  - Claude: 35,17 % son imágenes.
  - Googlebot: HTML 31,00 %, JSON 29,34 %, texto 20,77 %, JS 15,25 %.
  - — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- Errores y redirecciones:
  - ChatGPT: 34,82 % de sus fetches dan 404 y 14,36 % siguen redirecciones.
  - Claude: 34,16 % dan 404.
  - Googlebot: 8,22 % dan 404 y 1,49 % siguen redirecciones.
  - — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)

**Glenn Gabe (GSQi), 11-08-2025, actualizado 19-10-2026 [Medido, anecdótico]**
- Método: prompts sobre URLs de un sitio cliente totalmente CSR y de «varios» sitios JS sin nombre, con páginas sin JS como control. Sin tamaño de muestra.
- Resultados:
  - ChatGPT dijo que no podía leer el contenido.
  - Perplexity falló en todas las URLs, a veces con «Access Denied».
  - Claude dijo que la URL «was returned without any visible content».
  - Las páginas de control se leyeron bien.
- La actualización del 19-10-2026 («434 Days Later») dice que ChatGPT y Claude «still cannot render JS-based content».
- — [GSQi](https://www.gsqi.com/marketing-blog/ai-search-javascript-rendering)

**Andre Alpar (Search Engine World), 09-06-2026, actualizado 02-07-2026 [Medido, una pasada]**
- Método: 12 asistentes, una URL secreta por asistente y el prompt «Summarize this page and report the internal reference number». El HTML mostraba un número señuelo; un JS externo lo sustituía por el real, servido desde un segundo endpoint. Se registraron página, JS y endpoint.
- No ejecutaron JS (devolvieron el señuelo): ChatGPT, Claude, Gemini, Perplexity, Meta AI y Copilot. Copilot descargó el script vía Diffbot, pero no lo ejecutó.
- Grok ejecutó el JS en un nodo proxy, pero la respuesta lo ignoró.
- Sí ejecutaron JS: DeepSeek, ERNIE, Qwen, Kimi y Mistral (Europa).
- La mayoría de los asistentes de EE. UU. pidieron solo el HTML.
- — [Search Engine World](https://www.searchengineworld.com/do-ai-assistants-actually-render-your-javascript-when-grounding-we-put-it-to-the-test)

**Bogdan Ripa, 22-10-2026 [Medido, un sitio pequeño]**
- Método: sitio estático de unas pocas decenas de páginas en Cloudflare, con un Worker que registra todas las peticiones, del 8 al 22 de octubre de 2026. 560 peticiones de IPs verificadas contra las listas publicadas por OpenAI, más una trampa `/api/js`.
- **OAI-SearchBot** funciona como un pipeline de al menos tres partes:
  - un comprobador de robots.txt (flota de Dulles, `OAI-SearchBot/1.0`);
  - un fetcher rápido de HTML (Atlanta; 325 de 359 peticiones consecutivas cambiaron de IP);
  - un renderizador Chrome headless que vuelve una mediana de **32 minutos** después del HTML (26 páginas, casi todas entre 29 y 39 minutos). Ejecutó JS: llamó a `get-session`, siguió una redirección de cliente, pidió 14 ficheros de prefetch de Next.js y llamó a la trampa `/api/js`. Un renderizado de una página de listado hizo 66 peticiones desde 52 IPs.
  - Su user-agent es Chrome 131 Mac con `OAI-SearchBot/1.4`.
  - — [Ripa](https://bogdanripa.substack.com/p/an-analysis-of-openais-bots)
- **ChatGPT-User:**
  - pide solo HTML, sin CSS, imágenes ni JS;
  - nunca pidió robots.txt;
  - no envía Referer;
  - envía siempre `Accept-Language: en-US`;
  - trabaja en ráfagas de menos de 15 s;
  - 93 IPs en 18 ciudades.
  - — [Ripa](https://bogdanripa.substack.com/p/an-analysis-of-openais-bots)
- **GPTBot:** 28 peticiones desde 3 IPs (Atlanta). El 11-10 cargó CSS y JS 2–4 s después del HTML. No está probado que ejecute JS. — [Ripa](https://bogdanripa.substack.com/p/an-analysis-of-openais-bots)
- Contradicción: una auditoría de 342 sitios de lanzamiento (2026) concluye que no hay renderizado, pero usa un único GET por sitio, así que no puede detectar un renderizado diferido. — [aat.ee](https://www.aat.ee/blog/ai-crawlers-javascript-rendering-audit). No hay anuncio de OpenAI sobre renderizado; fuentes secundarias discrepan sobre qué dice su documentación. — [búsqueda agregada; ver aat.ee y searchoptimo.com](https://searchoptimo.com/blog/do-ai-crawlers-render-javascript)

**searchVIU [Medido, muestra pequeña]**
- Test de octubre de 2025: ChatGPT, Claude y Perplexity no capturaron contenido JS en el fetch en vivo. La tabla del propio artículo es incoherente: marca a ChatGPT como único sistema que encontró un precio cargado por JS. — [searchVIU](https://www.searchviu.com/en/schema-markup-and-ai-in-2025-what-chatgpt-claude-perplexity-gemini-really-see/)
- Su página sobre renderizado (12–17-11-2025) es una recopilación sin método propio, que repite las cifras de Vercel. Cuidado con citarla como estudio. — [searchVIU](https://www.searchviu.com/en/ai-crawlers-javascript-rendering/)

**Documentación de Google [Opinión/doc]**
- AI Overviews y AI Mode se alimentan del rastreo estándar de Googlebot, que renderiza con Chromium headless. — [Google AI features](https://developers.google.com/search/docs/appearance/ai-features); [Google JS SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)

### Inferences
- **Dos caminos de consumo distintos.**
  - **Lectura en vivo** (fetchers que lanza el usuario, como ChatGPT-User y Claude-User): HTML inicial sin JS, solo el documento, sin subrecursos.
  - **Indexación de búsqueda** (OAI-SearchBot según un único estudio; Googlebot/Gemini; Applebot; Bing en parte): puede renderizar, de forma diferida.
  - El perfil base «respuesta HTTP sin JS» equivale al denominador común del primer camino y al peor caso del segundo. El DOM tras la carga equivale al techo del segundo camino.
- La diferencia entre fetchers de usuario y crawlers de entrenamiento no está en el JS (ninguno de los dos ejecuta, salvo OAI-SearchBot y los de Google y Apple), sino en:
  - **robots.txt:** ChatGPT-User no lo pidió (Ripa); Perplexity-User lo ignora en general, según secundarias.
  - **Subrecursos:** ChatGPT-User no pide subrecursos.
  - **Origen IP:** ver §5.
- Las tasas de 404 de más del 34 % (Vercel, 2024) indican que los crawlers de IA trabajan con listas de URLs desfasadas. En fichas de producto con rotación de catálogo, esto importa.

### Gaps
- No hay estudio a gran escala posterior a Vercel/MERJ (2024) con logs multi-sitio que mida el renderizado por bot en 2025–2026. Las réplicas son de un sitio o anecdóticas.
- No encontré medición independiente de Claude-User, Claude-SearchBot, Perplexity-User, Meta-ExternalFetcher, Amazonbot ni Bytespider en 2026 sobre JS.
- El renderizado diferido de OAI-SearchBot procede de un solo sitio durante dos semanas. Nadie lo ha replicado.
- Copilot y Bing: no hay medición pública de cuánto JS ejecutan.

## 2. Datos estructurados: ¿leen los asistentes el JSON-LD/Schema.org? ¿Importa si se inyecta por JS o va en el HTML del servidor?

### Takeaway
En el fetch en vivo, el JSON-LD casi nunca llega al modelo:
- Pilot Digital (agosto de 2026): **0 de 25** bloques JSON-LD sobrevivieron en ChatGPT, Gemini, Claude, Firecrawl y Chrome reader.
- searchVIU (octubre de 2025): ningún sistema extrajo un precio que solo estaba en JSON-LD.

Pero un test de febrero de 2026 mostró que ChatGPT y Perplexity sí devolvieron un dato que solo estaba en un JSON-LD inválido, probablemente leído como texto o vía índice, no como esquema.

Conclusión: el marcado llega por la vía de los índices y feeds (Google, Bing, feeds de comercio), no por la lectura en vivo. No hay test publicado que compare JSON-LD inyectado por JS con JSON-LD en el HTML del servidor.

### Cited Findings
- **Pilot Digital** (test del 06-08-2026, publicado el 06-10-2026) [Medido, una página]
  - Método: una página estática con 14 canarios ocultos y 5 herramientas (ChatGPT, Gemini y Claude con su fetch integrado, más Firecrawl y Chrome reader).
  - JSON-LD: 0/5 en cada herramienta; la posición (head, body, final del body) no cambió nada.
  - Meta description: solo la vieron Claude y Firecrawl; Gemini elimina el `<head>`.
  - JSON en un `<div>` oculto: lo vieron 4 de 5; en `<script>`, 0 de 5; en `<template>`, 1 de 5.
  - Microdata: ✗ en ChatGPT y Claude, parcial en Gemini.
  - RDFa: ✗ en los tres asistentes.
  - Texto visible (control): ✓ en todas.
  - Perplexity no se probó, y la página era noindex.
  - — [Pilot Digital](https://pilotdigital.com/blog/research-finding-json-schema-doesnt-help-optimize-for-ai-search/)
- **searchVIU, octubre de 2025** [Medido, muestra pequeña]: precio solo en JSON-LD. Claude, ChatGPT y los demás lo pasaron por alto; concluyen que los chatbots leen solo el HTML visible en la recuperación directa. La propia tabla es incoherente en Gemini. — [searchVIU](https://www.searchviu.com/en/schema-markup-and-ai-in-2025-what-chatgpt-claude-perplexity-gemini-really-see/)
- **searchVIU, análisis de código filtrado de Claude Code** [Opinión, no verificable]: el paso HTML→Markdown (Turndown) elimina `<head>`, `<script>` y atributos, y con ellos el JSON-LD. — [searchVIU](https://www.searchviu.com/en/claude-leak-ai-grounding/)
- **Mark Williams-Cook, «DUCKYEA», 06-02-2026** [Medido, un caso]: dirección ficticia solo dentro de un JSON-LD inválido e inventado. ChatGPT y Perplexity la devolvieron. Su conclusión: «the LLM agent is simply picking up whatever you are listing in the HTML». El mismo artículo recuerda que OpenAI obtiene datos de shopping de feeds estructurados y que Microsoft ha dicho que el schema ayuda a Copilot. — [Search Engine Roundtable](https://www.seroundtable.com/chatgpt-perplexity-structured-data-text-40862.html); [post original](https://www.linkedin.com/posts/markseo_seo-share-7424067359088455680-vNFv/)
- **Contradicción explícita:** DUCKYEA (sí se lee) frente a Pilot Digital y searchVIU (se elimina en el fetch). La diferencia de vía (índice o caché frente a fetch en vivo) es la explicación más plausible, pero nadie la ha demostrado. — [SER](https://www.seroundtable.com/chatgpt-perplexity-structured-data-text-40862.html); [Pilot Digital](https://pilotdigital.com/blog/research-finding-json-schema-doesnt-help-optimize-for-ai-search/)
- **Writesonic 2026, vía Trusted Shops** [secundaria, no verificada]: «0 de 6 LLMs leyeron JSON-LD en modo conversación»; la microdata en el body se leería mejor que el JSON-LD del head. — [Trusted Shops AI Trust Audit](https://ai-trust-audit.trustedshops.com/pt/blog/o-que-os-ai-crawlers-veem-e-o-que-nao-veem)
- **Schema App** [Opinión/doc]: Perplexity y quizá ChatGPT no pueden ver el JSON-LD inyectado en cliente cuando rastrean, pero pueden usar índices de terceros que sí renderizan. — [Schema App](https://support.schemaapp.com/support/solutions/articles/33000296861-large-language-models-and-javascript-consumption)
- **Correlación, no causalidad:** en agentes inmobiliarios alemanes, el 6,2 % de los visibles en ChatGPT tenía FAQPage frente al 0,8 % de los no visibles (p = 0,002). — [ResearchGate](https://www.researchgate.net/publication/400228790_THE_IMPACT_OF_JSON-LD_METADATA_ON_CHATGPT_VISIBILITY)
- **Ecommerce:** OpenAI invita a los comerciantes a enviar un feed de producto directo «to ensure ChatGPT always reflects the most up-to-date information», mediante su especificación de Product Feed. No pude abrir la página: la cita procede del snippet. — [OpenAI Help (403 al abrirla)](https://help.openai.com/en/articles/11128490). Guías de terceros dicen que el programa de comerciantes era solo para EE. UU. a julio de 2026 [no verificado]. — [stellagent](https://stellagent.ai/insights/chatgpt-product-recommendation)

### Inferences
- Para el ámbito **Web Schema.org**, el consumidor relevante no es el fetcher en vivo del asistente, sino:
  - los sistemas de indexación (Google, que sí parsea Schema.org; Bing y Copilot);
  - las canalizaciones de feeds de comercio.
- Esto separa el consumo del marcado del consumo del HTML visible y es coherente con interpretar los ámbitos Web y Web Schema.org por separado.
- Para el ámbito **Web** visto por un fetcher en vivo, solo cuenta el texto visible del HTML inicial: lo que esté solo en JSON-LD o en atributos no llega.
- El JSON-LD inyectado por JS, sin prueba directa, se deduce que es invisible para cualquier consumidor que no renderice. Es la combinación de §1 y §2, no una medición.

### Gaps
- No hay experimento publicado que compare JSON-LD en el HTML del servidor con JSON-LD inyectado por JS frente a asistentes o crawlers de IA.
- No hay evidencia medida de que el JSON-LD de una ficha cambie los listados de producto de ChatGPT Shopping, Perplexity Shopping o Gemini.
- No pude leer la especificación del Product Feed de OpenAI ni su cobertura geográfica (España).

## 3. Navegadores agénticos (ChatGPT agent/Atlas, Comet, Gemini/Chrome, Claude for Chrome, Browser Use): cuota de tráfico, renderizado e identificación

### Takeaway
Los navegadores agénticos son navegadores reales: renderizan todo y ejecutan JS. Por user-agent son indistinguibles de Chrome:
- Atlas tiene el mismo UA que Chrome 141 macOS.
- Comet no lleva ningún token propio.

La identificación fiable depende de Web Bot Auth (firmas HTTP, RFC 9421) y de los «signed agents» de Cloudflare (agosto de 2025), que sigue en borrador IETF. Su cuota de tráfico es pequeña pero crece rápido:
- La categoría «user action» de Cloudflare creció más de 15 veces en 2025.
- Era el 2,7 % del tráfico de bots de IA en julio de 2026, según fuente secundaria.

### Cited Findings
- **Cloudflare, «signed agents» (28-08-2025)** [Opinión/doc]
  - Nueva clase de bot: agentes dirigidos por el usuario que firman sus peticiones con Web Bot Auth.
  - Cohorte inicial: ChatGPT agent, Goose (Block), Browserbase y Anchor Browser; también Cloudflare Browser Rendering.
  - Sin cifras de tráfico.
  - — [Cloudflare](https://blog.cloudflare.com/signed-agents/)
- **Web Bot Auth** se basa en HTTP Message Signatures (RFC 9421). Sigue siendo un borrador, no un estándar IETF; una fuente dice que el grupo de trabajo no tenía documentos adoptados a 12-08-2026. — [nerdleveltech](https://nerdleveltech.com/web-bot-auth-ietf-standard-agent-verification)
- **Lista de 2026 [secundaria, no verificada en fuente primaria]:** un blog afirma que una actualización de Cloudflare de junio de 2026 listaba 19 agentes de IA verificados (ChatGPT Atlas, Claude in Chrome, Perplexity Browser, Gemini Agent Mode…) y que en julio de 2026 la categoría «signed agent» se fusionó con Verified Bots mediante un campo de metadatos. Hay que confirmarlo en developers.cloudflare.com. — [pravinkumar.co](https://www.pravinkumar.co/blog/cloudflare-june-2026-bot-management-webflow-protection-2026)
- **Atlas** (21-10-2025): UA `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) … Chrome/141.0.0.0 Safari/537.36`, «identical to … the latest Google Chrome on macOS». — [Simon Willison](https://simonwillison.net/2025/Oct/21/introducing-chatgpt-atlas/)
- **Comet:** UA esencialmente igual al de Chrome. Su bloqueador de anuncios por defecto impide cargar GTM/GA4, así que esas sesiones no aparecen en la analítica. — [Taggrs](https://taggrs.io/ai-browsers-tracking-attribution/)
- **HUMAN Security** [proveedor]: los filtros por UA y robots.txt no identifican de forma fiable las sesiones de Atlas. — [HUMAN](https://www.humansecurity.com/ai-agent/chatgpt-atlas/)
- **Cloudflare Radar Year in Review 2025** [Medido]:
  - El rastreo de «user action» creció más de 15 veces en 2025 (más de 21 veces de enero a principios de diciembre).
  - Los bots de IA distintos de Googlebot generaron el 4,2 % de las peticiones HTML; Googlebot solo, el 4,5 %.
  - A 2-12-2025, los humanos generaban el 47 % de las peticiones HTML y los bots no IA el 44 %.
  - — [Cloudflare](https://blog.cloudflare.com/radar-2025-year-in-review/)
- **Reparto por propósito en Radar, julio de 2026** [secundaria]: ≈44,5 % entrenamiento, 40 % mixto, 11,6 % búsqueda, 2,7 % acción de usuario (≈2,2 % en marzo). — [softwareseni](https://www.softwareseni.com/the-numbers-behind-ai-crawling-what-cloudflare-radar-reveals-about-who-takes-and-who-gives-back)
- **Junio de 2026:** Matthew Prince (Cloudflare) compartió datos de Radar con el tráfico automatizado en ≈57,5 % de las peticiones HTML frente a 42,5 % humano, atribuido sobre todo a agentes. Él mismo dijo que los datos eran «a bit messy». — [TechTimes](https://www.techtimes.com/articles/317877/20260605/bot-traffic-passes-humans-online-cloudflare-says-agentic-ai-drove-575-share.htm)
- **WebMall** (Universidad de Mannheim, arXiv 2508.13024, aceptado en SIGIR 2026) [Medido, benchmark simulado]:
  - Montaje: 4 tiendas simuladas con productos extraídos de Common Crawl.
  - Los agentes con árbol de accesibilidad superan claramente a los de solo captura de pantalla.
  - GPT-4.1 y Claude Sonnet 4 lograron un 62–75 % en tareas básicas y un 19–41 % en avanzadas (v1/v2).
  - — [arXiv](https://arxiv.org/html/2508.13024v2)
- **Perplexity**, Cloudflare (04-08-2025) [Medido, disputado]:
  - Ante bloqueos, Perplexity usó crawlers no declarados con UA genérico de Chrome macOS: 3–6 M de peticiones diarias, frente a 20–25 M del crawler declarado.
  - También rotó ASN y a veces ignoró robots.txt.
  - Perplexity lo negó y alegó que las peticiones lanzadas por el usuario no son rastreo.
  - — [Cloudflare](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/); [TechRepublic](https://www.techrepublic.com/article/news-cloudflare-accuses-perplexity-stealth-crawling-violations/)

### Inferences
- Los navegadores agénticos consumen la página como un humano con Chrome: DOM renderizado, banners de consentimiento, interacción. Pero eso es navegación interactiva y queda fuera del perímetro «sin navegación interactiva».
- El «DOM tras la carga» guardado por la captura se aproxima a lo que ve un agente en su primera vista, sin clics.
- La lectura de agentes por árbol de accesibilidad (WebMall) sugiere que, en un DOM renderizado, la semántica accesible pesa más que el aspecto visual.

### Gaps
- No hay cifra primaria de cuota de tráfico por navegador agéntico (Atlas, Comet, Claude for Chrome, Gemini en Chrome) ni para ecommerce.
- No pude confirmar en fuente primaria la lista de junio de 2026 ni la fusión de julio de 2026.
- No se sabe qué agentes firman con Web Bot Auth en modo navegador local, frente al modo de navegador remoto en la nube.

## 4. Muros de consentimiento y gestión de bots: CMP, bloqueos, desafíos y páginas inalcanzables

### Takeaway
No hay medición empírica del efecto de los banners CMP en los crawlers de IA: todo procede de guías de proveedores.

El mecanismo es claro:
- Un CMP inyectado por JS no existe para un fetcher sin JS, que recibe el contenido íntegro del HTML.
- El riesgo está en los muros servidos desde el servidor (respuesta sin contenido sin cookie de consentimiento) y en el texto legal al principio del DOM.

En bloqueo, Cloudflare:
- bloquea por defecto los crawlers de IA desde el 01-07-2025;
- desde el 15-09-2026 configura por defecto «Agent: Block on pages with ads» en dominios nuevos con anuncios;
- dice que el 17 % de sus sitios activa algún bloqueo del entrenamiento y menos del 1 % bloquea la búsqueda.

No encontré una cifra de páginas de ecommerce inalcanzables para los fetchers de IA.

### Cited Findings
- **Cloudflare, 01-07-2025** («Content Independence Day»): pasó a bloquear por defecto los crawlers de IA en los sitios que aloja y anunció «pay per crawl». — [MIT Technology Review](https://www.technologyreview.com/2025/07/01/1119498/cloudflare-will-now-by-default-block-ai-bots-from-crawling-its-clients-websites/); [Cloudflare](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)
- **Mismo post del 01-07-2025** (relación rastreo/referencias): «750 times harder» obtener tráfico de OpenAI y «30,000 times harder» de Anthropic que de Google «antiguo». — [Cloudflare](https://blog.cloudflare.com/content-independence-day-no-ai-crawl-without-compensation/)
- **Cloudflare, 15-09-2026** («accountable mixed-use crawlers»):
  - Nuevos controles Search / Training / Agent. «Agent» = «user-directed agents visiting a page on behalf of a human», como los fetchers de chat y los agentes de navegador.
  - Los agentes no tienen opción Disallow: solo Allow, Block on pages with ads o Block.
  - Valores por defecto en dominios nuevos:
    - sitio sin anuncios: Search Allow, Training Allow, Agent Allow;
    - sitio con anuncios: Search Allow, Training «Disallow AI Training», Agent «Block on pages with ads».
  - «Block» y «Block on pages with ads» pasan a afectar también a los crawlers mixtos (Googlebot, Bingbot, Applebot).
  - «less than 1% of Cloudflare sites choose to block Search bots»; «17% of sites choose to enable some mechanism to block training».
  - — [Cloudflare](https://blog.cloudflare.com/accountable-mixed-use-ai-crawlers)
- **Cloudflare Radar, mayo de 2024–mayo de 2025** (top 10.000 dominios): ≈14 % tienen directivas para bots de IA en robots.txt (546 dominios), y GPTBot es el más bloqueado. — [Cloudflare](https://blog.cloudflare.com/from-googlebot-to-gptbot-whos-crawling-your-site-in-2025/)
- **Desafíos:** según Cloudflare, el tráfico oculto de Perplexity no pudo superar los «managed challenges» (agosto de 2025). Implica que un fetcher sin navegador real se queda en la página de desafío. — [Cloudflare](https://blog.cloudflare.com/perplexity-is-using-stealth-undeclared-crawlers-to-evade-website-no-crawl-directives/)
- **GSQi** (agosto de 2025): Perplexity devolvió «Access Denied» en parte de las URLs probadas, sin bloqueo en robots.txt. — [GSQi](https://www.gsqi.com/marketing-blog/ai-search-javascript-rendering)
- **CMP** [Opinión, guías de proveedores, sin medición]:
  - Un CMP inicializado por JS no se ejecuta en los crawlers de IA, que no hacen clic en «aceptar».
  - Un overlay servido desde el servidor deja el contenido en el DOM, aunque el extractor puede degradarlo.
  - El peor caso es la respuesta que solo contiene el banner sin cookie de consentimiento.
  - Las guías distinguen entre banner (superpuesto) y muro (bloquea).
  - — [usestanding](https://usestanding.com/guides/cookie-consent-banners-ai-crawlers); [CookieFirst](https://cookiefirst.com/can-cookie-banners-block-ai-agents-and-ai-traffic/); [Contextractor](https://www.contextractor.com/cookie-consent-handling/)

### Inferences
- **El banner de consentimiento depende del perfil de captura.**
  - Para un perfil «HTTP sin JS», casi siempre es irrelevante; solo afectan los muros de servidor.
  - Para el DOM tras la carga en Chrome real, el banner sí aparece (overlay) y sí puede alterar el DOM.
  - El perfil base sin JS es, por tanto, más fiel a cómo consumen los fetchers de IA que el DOM renderizado.
- **Tres resultados que la auditoría debería distinguir y registrar.** Con Chrome real por CDP desde una IP residencial o española, la captura puede superar desafíos que un fetcher de IA no superaría, y al revés: puede no recibir un bloqueo específico por UA de IA. De ahí la distinción entre:
  - «alcanzable por un navegador»;
  - «alcanzable por el UA del fetcher de IA X»;
  - «servido con desafío».
- Los defaults de Cloudflare de septiembre de 2026 afectan sobre todo a sitios con anuncios. Las fichas de ecommerce rara vez llevan anuncios de terceros, así que el default «Agent: Allow» les aplicaría en principio. Es una inferencia sin medir.

### Gaps
- No hay medición del porcentaje de fichas de producto (ni de ecommerces españoles) que devuelven 403 o un desafío a GPTBot, ChatGPT-User, ClaudeBot o PerplexityBot.
- No hay medición del efecto de CMPs concretos (OneTrust, Cookiebot, Didomi) sobre lo que extraen los asistentes.
- No encontré el estado actual (octubre de 2026) de pay per crawl / «Pay Per Use» ni cifras de adopción. Las fuentes secundarias lo dan en beta privada.
- No hay datos públicos de Akamai, DataDome ni Fastly de 2026 que pudiera verificar en esta sesión.

## 5. Geografía y locale: origen IP y Accept-Language

### Takeaway
Casi todos los crawlers de IA salen solo de EE. UU.:
- GPTBot, OAI-SearchBot y PerplexityBot/Perplexity-User: solo EE. UU.
- ChatGPT-User es la excepción: ≈48 % de sus subredes están fuera de EE. UU., incluido Madrid.

Ninguno adapta Accept-Language al usuario: casi todos lo omiten, y ChatGPT-User envía `en-US`. Una tienda española que redirige o adapta contenido por IP o por idioma del navegador puede estar sirviendo otra versión, o una redirección, a casi todos los consumidores de IA.

### Cited Findings
- **Vercel** (diciembre de 2024): centros de datos de ChatGPT en Des Moines y Phoenix; de Claude en Columbus (Ohio); todos en EE. UU. — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- **EdgeComet** (22-02-2026) [Medido sobre rangos IP publicados, geolocalizados con MaxMind]:
  - GPTBot: 20 subredes en Phoenix, Atlanta y Des Moines, «zero international presence».
  - Crawler de ChatGPT Search: 35 subredes en ≈5 ciudades de EE. UU.
  - **ChatGPT-User: 224 subredes en 15 países, ≈48 % fuera de EE. UU.** (Dublín, Londres, Fráncfort, Varsovia, Milán, **Madrid**).
  - PerplexityBot y Perplexity-User: solo Ashburn (AWS us-east-1).
  - ClaudeBot: no analizado; Anthropic no publica rangos.
  - Googlebot: 165 subredes en 22 países, aunque la mayoría de sus peticiones siguen saliendo de rangos de EE. UU.
  - — [EdgeComet](https://edgecomet.com/blog/where-do-search-bots-and-ai-crawlers-actually-live-an-analysis-of-484-ip-subnets/)
- **Ripa** (octubre de 2026): ChatGPT-User usó 93 IPs en 18 ciudades y 22 redes; OAI-SearchBot salió de Atlanta, Des Moines, Phoenix y Dulles. — [Ripa](https://bogdanripa.substack.com/p/an-analysis-of-openais-bots)
- **MERJ** (03-03-2026, actualizado 29-09-2026, datos de febrero de 2026) [Medido, 29 agentes, sin recuento de peticiones]:
  - Accept-Language ausente en GPTBot, OAI-SearchBot, ClaudeBot, Claude-User, Claude-SearchBot, PerplexityBot, Perplexity-User, meta-externalagent, Amazonbot y DuckAssistBot.
  - ChatGPT-User: ausente o `en-US,en;q=0.9`.
  - MistralAI: ausente o `en-US,en;q=0.9`.
  - Bytespider: ausente, `en-US,en;q=0.5` o `zh,zh-CN;q=0.9`.
  - Applebot: lo ajusta al ccTLD (`de-DE` en .de).
  - Googlebot: ausente, salvo `en-US` al seguir redirecciones JS durante el renderizado.
  - Algunos crawlers de IA dejaron de enviar Accept-Language tras detectarse el problema.
  - — [MERJ](https://merj.com/blog/your-accept-language-redirects-could-be-blocking-search-engines-and-ai-crawlers)
- **Ripa** (octubre de 2026): ChatGPT-User envía siempre `Accept-Language: en-US`. — [Ripa](https://bogdanripa.substack.com/p/an-analysis-of-openais-bots)
- **Google, páginas adaptadas al locale** [doc]: las IPs por defecto de Googlebot parecen de EE. UU. y no envía Accept-Language, así que el contenido adaptado puede no rastrearse para otros locales. — [Google](https://support.google.com/webmasters/answer/6144055?hl=en)
- **Documentación de los proveedores:** a agosto de 2026, las páginas de crawlers de OpenAI, Anthropic y Perplexity no dicen nada de idioma ni de región. — [lantad.co](https://lantad.co/blog/googlebot-sets-no-accept-language)

### Inferences
- **El perfil de captura debería fijar y registrar IP de origen y Accept-Language**, porque cambian la respuesta. Un perfil representativo de los consumidores de IA sería: sin Accept-Language, o `en-US`, desde una IP de EE. UU.
- **Una captura desde España con `es-ES` es el mejor caso**, no el representativo: equivale a ChatGPT-User desde Madrid, y aun así con `en-US`.
- **Las redirecciones por IP o idioma son un riesgo de disponibilidad efectiva** que debería registrarse como hecho técnico. Sin embargo, el canon no permite que descuente el GSC más allá de su efecto sobre la disponibilidad.

### Gaps
- No hay medición del comportamiento de ecommerces españoles concretos ante IPs de EE. UU. sin Accept-Language: redirecciones a /en/, bloqueos geográficos, precios en USD.
- No hay datos de origen IP de ClaudeBot/Claude-User, Applebot, Amazonbot ni Meta.

## 6. Recomendaciones prácticas del SEO técnico y de la literatura «GEO»

### Takeaway
El consenso, con evidencia medida detrás, es servir el contenido crítico de la ficha en el HTML inicial (SSR/SSG). El CSR solo es aceptable para lo no esencial. El dato comercial clave también debe estar en el texto visible y no solo en JSON-LD ni en atributos. Hay que evitar las redirecciones por Accept-Language o IP y usar URLs por locale con hreflang. El JSON-LD en el HTML inicial se recomienda para buscadores y feeds, no porque lo lean los fetchers de IA.

### Cited Findings
- **Vercel** (diciembre de 2024): renderizar en servidor el contenido crítico (contenido principal, metadatos, navegación), dejar el CSR para lo no esencial, y mantener redirecciones, sitemaps y URLs consistentes por las altas tasas de 404. — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- **MERJ** (2026): no redirigir a bots por Accept-Language; usar URLs explícitas por locale con hreflang; tratar Accept-Language como preferencia; registrar las cabeceras en los logs. — [MERJ](https://merj.com/blog/your-accept-language-redirects-could-be-blocking-search-engines-and-ai-crawlers)
- **Pilot Digital** (octubre de 2026): poner los hechos en texto visible; el contenido en `<div>` sobrevive y el de `<script>` no. — [Pilot Digital](https://pilotdigital.com/blog/research-finding-json-schema-doesnt-help-optimize-for-ai-search/)
- **Williams-Cook** (febrero de 2026): el schema sigue valiendo la pena, pero reetiquetar el SEO básico como «GEO» no aporta. — [SER](https://www.seroundtable.com/chatgpt-perplexity-structured-data-text-40862.html)
- **GSQi** (2025–2026): los sitios CSR son invisibles para ChatGPT, Perplexity y Claude; recomienda SSR o prerenderizado. — [GSQi](https://www.gsqi.com/marketing-blog/ai-search-javascript-rendering)
- **Ripa** (octubre de 2026) [Opinión basada en un caso]: si OAI-SearchBot renderiza con retraso, el índice de ChatGPT Search podría ver contenido JS, pero ChatGPT-User en vivo no. — [Ripa](https://bogdanripa.substack.com/p/an-analysis-of-openais-bots)

### Inferences
- **Perfil base y perfil secundario:** las recomendaciones coinciden con el perfil base «respuesta HTTP sin JS». El DOM tras la carga sirve como perfil secundario, para detectar contenido que solo existe con JS y representar a los consumidores que renderizan: Google/Gemini, Applebot, OAI-SearchBot (indicio), Mistral y los agentes de navegador.
- **Propuesta para el contraste de perfiles** (sin fórmula ni peso): «presente en HTML inicial» frente a «solo en DOM renderizado» frente a «solo en JSON-LD» frente a «ausente».

### Gaps
- Casi toda la literatura GEO de 2026 son blogs de proveedores que repiten Vercel 2024. Las mediciones nuevas e independientes son pocas y de un sitio: GSQi, Search Engine World, Pilot Digital, Ripa, MERJ, EdgeComet.
- No hay estudios específicos de fichas de producto ni de ecommerce europeo.
