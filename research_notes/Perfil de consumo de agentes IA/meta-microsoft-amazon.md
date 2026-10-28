# Perfil de consumo de fichas de producto: Meta, Microsoft y Amazon (estado a 28-10-2026)

Notas de investigación para decidir el perfil base de captura de la auditoría (Chrome real por CDP, sin navegación interactiva; base actual: «respuesta HTTP sin ejecutar JavaScript»). Distingo **[oficial]** (documentación o anuncio de la empresa) de **[tercero]** (prensa, blogs de SEO, proveedores de bot management, estudios empíricos). Fechas entre paréntesis cuando el hecho es anterior a 2026 o tiene fecha propia.

## 1. Meta: crawlers, fetchers, Meta AI y Muse Spark

### Takeaway
Meta documenta cinco agentes (facebookexternalhit, meta-webindexer, meta-externalads, meta-externalagent, meta-externalfetcher) pero no dice si ejecutan JavaScript; el único estudio empírico serio (Vercel/MERJ, dic. 2024) concluye que Meta-ExternalAgent no renderiza JS. «Muse» es **Muse Spark**, el modelo de Meta Superintelligence Labs (8-4-2026) que mueve Meta AI; su harness tiene herramientas `browser.search`/`browser.open` sobre un buscador no revelado y una búsqueda propia en el catálogo de productos de Meta; el modo compras se apoya en Marketplace, contenido de marcas/creadores y «opciones de toda la web», no en checkout sobre webs de terceros, y se desplegó primero en EE. UU.

### Cited Findings
**Crawlers y fetchers [oficial, página sin fecha visible, consultada 28-10-2026]** — [Meta Web Crawlers](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers)
- `facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)`: rastrea lo que se comparte en las apps de Meta; recoge, cachea y muestra título, descripción y miniatura (vista previa de enlace). Lee **Open Graph**, que debe estar **antes del primer 1 MB** de la página o se trunca. Puede **saltarse robots.txt** en comprobaciones de seguridad o integridad. El servidor debe admitir gzip/deflate y respetar o ignorar `Range`; el contenido debe poder rastrearse «en pocos segundos». Meta recomienda listas blancas por IP (no publica rangos en esa página).
- `meta-webindexer/1.1`: «analiza contenido web para mejorar la calidad y exactitud de los resultados de búsqueda de Meta AI». Control por robots.txt.
- `meta-externalads/1.1`: rastreo para publicidad y productos de negocio. Respeta disallow.
- `meta-externalagent/1.1`: rastreo para **entrenar modelos fundacionales** o mejorar productos indexando contenido directamente. Respeta disallow.
- `meta-externalfetcher/1.1`: recupera enlaces concretos **a petición del usuario**; da soporte a funciones agénticas, «incluida ayudar a la IA a completar tareas en sitios web». **Puede saltarse robots.txt.**
- robots.txt se cachea hasta 24 h. La página **no menciona** ejecución de JS, Accept-Language, locale, cookies ni Schema.org/JSON-LD para ningún agente.

**Ejecución de JavaScript [tercero]**
- Vercel + MERJ (17-12-2024): «none of the major AI crawlers currently render JavaScript», incluido Meta-ExternalAgent; metodología: tráfico de nextjs.org y la red de Vercel durante meses, contrastado con dos webs de empleo. Copilot quedó excluido por no tener UA propio; Amazonbot y Bingbot no se estudiaron. — [Vercel, The rise of the AI crawler](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- searchVIU (12/17-11-2025) etiqueta Meta-ExternalAgent como «No JS», atribuyéndolo a Dark Visitors; sin método propio descrito. — [searchVIU](https://www.searchviu.com/en/ai-crawlers-javascript-rendering/)
- Una prueba de logs de 41 días informa de que los bots de IA de Meta nunca siguieron enlaces inyectados por script (fuente secundaria, sin autor verificable). — [searchengineoptimization.blog](https://searchengineoptimization.blog/article/41-day-log-test-finds-most-ai-crawlers-skip-javascript-links)

**Muse Spark y Meta AI**
- Muse Spark es el primer modelo de Meta Superintelligence Labs (MSL), anunciado el 8-4-2026; mueve Meta AI en la app y meta.ai, con despliegue posterior a Instagram, Facebook, WhatsApp, Messenger, Threads y gafas. Las novedades empezaron **en EE. UU.** con promesa de «más países» en semanas; API en vista previa privada para socios. [oficial] — [Meta Newsroom, Introducing Muse Spark](https://about.fb.com/news/2026/04/introducing-muse/); [TechCrunch 8-4-2026](https://techcrunch.com/2026/04/08/meta-debuts-the-muse-spark-model-in-a-ground-up-overhaul-of-its-ai/); [CNBC 8-4-2026](https://www.cnbc.com/2026/04/08/meta-debuts-first-major-ai-model-since-14-billion-deal-to-bring-in-alexandr-wang.html)
- Modo compras (actualización 12-5-2026): buscar anuncios de Facebook Marketplace cercanos «junto a opciones de toda la web», en mapa; mencionar (@) una marca o creador para ver su contenido público y sus productos en cuadrícula; escanear un producto y compararlo con alternativas; subagentes en paralelo. La página no describe checkout ni compra. [oficial] — [Meta Newsroom](https://about.fb.com/news/2026/04/introducing-muse/)
- Herramientas del harness de meta.ai: `browser.search` (buscador **no revelado**), `browser.open` (carga la página completa de un resultado), `browser.find` (búsqueda de patrones en el contenido devuelto), `meta_1p.meta_catalog_search` («Search for products in Meta's product catalog», probablemente el modo Shopping) y descarga de imágenes de catálogo. Obtenido del propio modelo por Simon Willison y confirmado como parte del harness por Jack Wu (Meta). [tercero con confirmación parcial] — [Simon Willison, 8-4-2026](https://simonwillison.net/2026/Apr/8/muse-spark/)
- Históricamente Meta AI obtenía información en tiempo real mediante acuerdos con **Bing** y después también **Google** (2024), y The Information informó de que Meta construía su propio crawler para depender menos de ellos. [tercero, 2024] — [Social Media Today](https://www.socialmediatoday.com/news/meta-is-developing-a-search-engine-to-power-its-ai-chatbot/731272/)
- Retail Brew y SmartCompany describen el recorrido de compra como cerrado dentro del ecosistema de Meta. [tercero, abr. 2026] — [Retail Brew 16-4-2026](https://www.retailbrew.com/stories/2026/04/16/meta-introduces-new-shopping-upgrades-under-ai-model-muse-spark); [SmartCompany](https://www.smartcompany.com.au/artificial-intelligence/neural-notes-meta-muse-spark-ai-reset-shopping/)
- The Information (mayo 2026, vía agregador) informa de que Meta prepara una herramienta de compra agéntica para Instagram. [tercero, no verificado] — [texxr](https://texxr.com/entity/muse-spark/launch)

### Inferences
- El fetcher que leería una ficha española a petición del usuario en Meta AI es `meta-externalfetcher` (o `browser.open` del harness, probablemente el mismo agente); el indexador para citar es `meta-webindexer`. Nada oficial indica renderizado de JS; lo prudente es suponer **HTML de la respuesta HTTP** para meta-externalagent y facebookexternalhit, y tratar meta-externalfetcher como desconocido.
- Para facebookexternalhit, lo relevante es Open Graph en el `<head>` dentro del primer MB: un perfil «HTTP sin JS» lo emula bien.
- Para productos, Meta privilegia su **catálogo propio** (Commerce/catálogos de anuncios) y Marketplace; la web abierta es complementaria. Esto encaja con el ámbito «Catálogos distribuidos» del canon más que con «Web».

### Gaps
- No encontré qué buscador alimenta `browser.search` en 2026 ni si meta-webindexer ha sustituido a los acuerdos con Bing/Google.
- No hay documentación de Meta sobre JS, JSON-LD/Schema.org, cookies/consentimiento, Accept-Language ni origen de IP de ninguno de sus agentes.
- No confirmé disponibilidad de Muse Spark ni del modo compras en España/UE a octubre de 2026 (una guía en español plantea la pregunta sin respuesta visible: [Metricool](https://metricool.com/es/meta-ai-muse-spark/)).
- No encontré fecha de alta de `meta-webindexer` ni de `meta-externalads` en la documentación.

## 2. Microsoft: Bingbot, Copilot, Copilot Checkout y Merchant Center

### Takeaway
Copilot no tiene crawler propio documentado: se alimenta del índice de Bing (Bingbot), que desde 2019 renderiza con Edge «evergreen» (Chromium), aunque las pruebas de terceros indican que renderiza de forma selectiva. Microsoft confirmó (mar. 2025) que usa Schema.org para que sus LLM entiendan las páginas y empuja IndexNow para frescura. Para compras, Copilot Checkout (desde 8-1-2026) exige feed en Microsoft Merchant Center y está limitado a comerciantes en inglés que venden a EE. UU. en USD.

### Cited Findings
**Bingbot y renderizado**
- Bing anunció en oct. 2019 que Bingbot usa Microsoft Edge (Chromium) para ejecutar JS y renderizar, comprometiéndose a actualizar el motor a «la versión estable más reciente de Microsoft Edge»; el UA «puede cambiar» para permitir el renderizado. [oficial, 2019] — [Bing Webmaster Blog, evergreen Bingbot](https://blogs.bing.com/webmaster/october-2019/The-new-evergreen-Bingbot-simplifying-SEO-by-leveraging-Microsoft-Edge)
- En 2018 Bing recomendó **dynamic rendering** (servir HTML prerenderizado a Bingbot) para webs muy dependientes de JS «para mejorar la previsibilidad del rastreo y la indexación», y no lo considera cloaking si el contenido es el mismo. [oficial, 2018] — [Bing Webmaster Blog, JavaScript, Dynamic Rendering, and Cloaking](https://blogs.bing.com/webmaster/october-2018/bingbot-Series-JavaScript,-Dynamic-Rendering,-and-Cloaking-Oh-My)
- UA clásico: `Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)`. [tercero] — [Wikipedia, Bingbot](https://en.wikipedia.org/wiki/Bingbot)
- searchVIU (nov. 2025) lo etiqueta «partial js»: puede renderizar pero limita el procesamiento de JS; la misma página afirma en otro punto «full rendering», contradicción no resuelta. [tercero] — [searchVIU](https://www.searchviu.com/en/ai-crawlers-javascript-rendering/)
- Una prueba independiente citada por un agregador encontró que Bingbot pedía scripts en ~1 de cada 800 lecturas; en el test de 41 días Bingbot no siguió enlaces inyectados por JS pero sí indexó 212 páginas cuando los enlaces pasaron a HTML plano. [tercero, verificabilidad baja] — [searchengineoptimization.blog](https://searchengineoptimization.blog/article/41-day-log-test-finds-most-ai-crawlers-skip-javascript-links)
- Un blog de SEO cita las Webmaster Guidelines con «Content that cannot be reliably rendered may not be indexed or selected for grounding results». [tercero; no pude verificar el texto oficial: la página de Bing no se pudo leer] — [eSEOspace](https://eseospace.com/blog/javascript-rendering-and-ai-crawlers/)

**Copilot**
- Vercel excluyó Copilot de su estudio porque **no tiene user agent propio** (dic. 2024). — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- Listas de terceros (oct. 2026) coinciden en que Microsoft no documenta un crawler de Copilot; bloquear Bingbot bloquea las citas de Copilot; la página oficial de crawlers de Bing, según esos resúmenes, lista bingbot, AdIdxBot, BingPreview, MicrosoftPreview y BingVideoPreview, sin entrada para Copilot. [tercero] — [Momentic, oct. 2026](https://momenticmarketing.com/blog/ai-search-crawlers-bots); [xSeek](https://www.xseek.io/docs/bing-ai-user-agents)
- Control de uso en IA por meta robots, no por token de robots.txt: **NOARCHIVE** excluye la página de las respuestas de chat (y de entrenamiento); **NOCACHE** permite usarla mostrando solo URL, título y fragmento; con ambas se aplica NOCACHE. [oficial, sept. 2023, cuando era «Bing Chat»] — [Bing Webmaster Blog, sept. 2023](https://blogs.Bing.com/webmaster/september-2023/Announcing-new-options-for-webmasters-to-control-usage-of-their-content-in-Bing-Chat). Un artículo de 2026 dice que las guías actuales aplican NOARCHIVE a «Copilot responses and grounding results». [tercero] — [ppc.land](https://ppc.land/noarchive/)

**Schema.org e IndexNow**
- Fabrice Canel (Principal PM de Bing) en SMX Munich (mar. 2025): Bing y Copilot usan schema markup para que sus LLM entiendan el contenido («When we process a page, we need to understand what this page is about»); recomendó IndexNow para empujar contenido fresco. [declaración pública de un empleado, recogida por prensa] — [Search Engine Land](https://searchengineland.com/microsoft-bing-copilot-use-schema-for-its-llms-453455)
- Un hilo de WebmasterWorld (jul. 2026) discute que el efecto medible del marcado en las respuestas de LLM no está demostrado. [tercero] — [WebmasterWorld](https://www.webmasterworld.com/gpt/5133290.htm)

**Copilot Checkout y Merchant Center**
- Copilot Checkout se lanzó el 8-1-2026 en Copilot.com (EE. UU.), con PayPal, Shopify y Stripe; el comercio sigue siendo merchant of record. [oficial, socio] — [PayPal Newsroom 8-1-2026](https://newsroom.paypal-corp.com/2026-01-08-PayPal-Powers-Microsofts-Launch-of-Copilot-Checkout)
- Página de Microsoft Advertising: requiere cuenta de **Microsoft Merchant Center** y un feed de producto «para la descubierta y el checkout»; feed «UCP-ready» (Universal Commerce Protocol) con atributos de elegibilidad de checkout nativo, advertencias de producto y Merchant Item ID; «Feeds primarily enable discovery», UCP «enables transactions» y añadirá señales de devoluciones/soporte. Copilot usa «both information found on the web and from a merchant's feed». **Solo comerciantes en inglés que venden a compradores de EE. UU. (USD)**; sin calendario de expansión; piloto para clientes seleccionados; comerciantes de Shopify inscritos automáticamente con opción de salida; sin comisión. [oficial, sin fecha] — [Microsoft Advertising, Agentic Commerce](https://about.ads.microsoft.com/en/solutions/technology/agentic-commerce)
- 21-4-2026: soporte de feeds UCP en Merchant Center disponible en EE. UU. y Checkout ampliado a móvil. [tercero que resume anuncio] — [WindowsForum](https://windowsforum.com/threads/microsoft-ucp-merchant-center-agentic-shopping-with-copilot-checkout-and-target-loyalty.419123/)

### Inferences
- Para Copilot, el perfil de consumo de una ficha es el de **Bingbot**: HTML más renderizado posible (Chromium/Edge) pero no garantizado. Emularlo con «HTTP sin JS» da el **suelo** (lo que Bing verá con seguridad); un render en Chrome da el **techo**.
- El papel de Schema.org en Bing/Copilot es el más explícito de las tres empresas (declaración pública, no documentación normativa).
- En España, Copilot Checkout y el feed UCP no aplican a octubre de 2026; Merchant Center/Shopping de Bing sí es la vía de catálogo.

### Gaps
- No pude leer las Webmaster Guidelines ni la página oficial de crawlers de Bing (devolvieron solo el título); su texto actual sobre JS, grounding y NOARCHIVE queda sin verificar de primera mano.
- No hay documentación sobre fetch en vivo de Copilot fuera del índice (p. ej., cuando el usuario pega una URL), ni sobre cookies, Accept-Language o país de las IP de Bingbot para mercados como es-ES.
- No encontré Brand Agents ni Copilot Merchant Program documentados con detalle; no hay datos de disponibilidad de Copilot Checkout en la UE.

## 3. Amazon: Amazonbot, Amzn-SearchBot, Amzn-User, Rufus/Alexa for Shopping y Buy for Me

### Takeaway
Amazon documenta tres agentes con UA tipo Chrome (Amazonbot, Amzn-SearchBot, Amzn-User; página actualizada 26-10-2026) sin decir si ejecutan JS. Buy for Me, en cambio, es un agente de navegador real (Nova Act sobre Chromium, según terceros) que ejecuta JS en la web de la marca y se presenta como navegador estándar. Rufus pasó a llamarse «Alexa for Shopping» en EE. UU. (13-5-2026); Alexa+ llegó a España en acceso anticipado el 23-4-2026.

### Cited Findings
**Agentes documentados [oficial, actualizado 26-10-2026]** — [Amazon Developer, Amazonbot](https://developer.amazon.com/amazonbot)
- `Mozilla/5.0 AppleWebKit/537.36 (KHTML, like Gecko; compatible; Amazonbot/0.1) Chrome/W.X.Y.Z Safari/537.36`: mejora productos y servicios, puede dar respuestas más exactas y **puede entrenar modelos de IA de Amazon**. Respeta robots.txt (cache hasta 30 días; si no se puede obtener, se trata como ausente); respeta `rel=nofollow` y meta `noarchive` (excluye de entrenamiento), `noindex`, `none`; no admite `crawl-delay`. IP publicadas en developer.amazon.com/amazonbot/ip-addresses/.
- `... compatible; Amzn-SearchBot/0.1 ...`: mejora la búsqueda en productos de Amazon (elegibilidad para Alexa); **no** rastrea para entrenar IA generativa; si robots.txt no lo nombra, sigue las reglas dadas a otros buscadores. IP propias publicadas.
- `... compatible; Amzn-User/0.1 ...`: acciones iniciadas por el usuario, p. ej. obtener información web en vivo para responder a Alexa; **«may not follow all robots.txt directives»**; no entrena. IP propias («live-ip-addresses»).
- La página no menciona JS, Schema.org/JSON-LD, cookies, idioma ni país de las IP. Los cambios tardan ~24 h.

**Ejecución de JS de Amazonbot [tercero]**
- No hay estudio primario; una guía lo marca «No» y el test de 41 días informa de que los bots de IA de Amazon no siguieron enlaces inyectados por JS. — [searchengineoptimization.blog](https://searchengineoptimization.blog/article/41-day-log-test-finds-most-ai-crawlers-skip-javascript-links)

**Otros agentes de Amazon catalogados por terceros** — [Known Agents, Amazon](https://knownagents.com/operators/amazon) [tercero]
- `AmazonBuyForMe` (agente IA que visita páginas de producto para el servicio Buy For Me; «uses an actual web browser»), `NovaAct` (agente de navegador), `AmazonProductDiscovery` («descubre y recoge información de productos en la web»), Amazon Bedrock AgentCore Browser (navegador en la nube para agentes), bedrockbot, amazon-QBusiness, amazon-kendra, AmazonAdBot. Sin UA ni fechas en la página.

**Buy for Me**
- Agente que visita la web externa, selecciona el producto pedido y rellena nombre, dirección y pago (cifrado; Amazon dice no ver qué se compra); beta para usuarios seleccionados de EE. UU. en la app de Amazon (lanzada abr. 2025); razonamiento con Nova y Claude, acción con Nova Act. [prensa que cita a Amazon] — [Yahoo Finance/TechCrunch](https://finance.yahoo.com/news/amazons-ai-agent-shop-third-003540471.html)
- Ene. 2026: polémica porque Buy for Me/Shop Direct mostraba productos de marcas en Amazon sin su permiso; funciona como **opt-out** (correo de baja: shopdirect@ o branddirect@amazon.com según la fuente). [tercero] — [Modern Retail 6-1-2026](https://www.modernretail.co/technology/brands-are-upset-that-buy-for-me-is-featuring-their-products-on-amazon-without-permission/); [SiliconANGLE 6-1-2026](https://siliconangle.com/2026/01/06/amazons-ai-agents-spark-backlash-retailers-listing-products-without-knowledge/)
- cside (19-6-2026, act. 20-7-2026): Buy for Me «uses a real browser», abre una sesión de Chromium, «executes JavaScript, fires pixel events, and loads resources», UA estándar de Chrome (ejemplo Chrome 124), cookie de sesión nueva y localStorage vacío, IP posiblemente residenciales/consumo o nube, **sin lista de IP publicada**; bloquear Amazonbot no lo bloquea. [tercero, proveedor de bot management] — [cside](https://cside.com/blog/how-to-block-amazon-buy-for-me)

**Rufus / Alexa for Shopping / Alexa+**
- Rufus renombrado «Alexa for Shopping» y unificado con Alexa+ (13-5-2026); varias fuentes dicen que el cambio es en EE. UU. y que Rufus mantiene el nombre en otros mercados; una lista «Buy for Me» para otros minoristas como función agéntica desde mayo de 2026. [tercero] — [GeekWire](https://www.geekwire.com/2026/amazon-unifies-alexa-and-rufus-as-ai-rivals-move-into-online-shopping/); [Perpetua](https://perpetua.io/blog-alexa-for-shopping-amazon-rufus-the-complete-guide-for-brands-and-sellers/)
- Alexa+ en España: anuncio 23-4-2026, acceso anticipado gratuito y limitado hasta al menos 15-9-2026; gratis con Prime; compras por voz con comparación de precios y resúmenes de reseñas; acceso web «pronto». [prensa española] — [WWWhatsNew 24-4-2026](https://wwwhatsnew.com/2026/04/24/alexa-plus-espana-lanzamiento-precio-prime-abril-2026/); [Geeknetic](https://www.geeknetic.es/Noticia/38384/Alexa-llega-a-Espana-con-IA-generativa-y-acceso-anticipado-gratuito.html)

### Inferences
- Amazon tiene dos perfiles distintos: **crawlers/fetchers** (Amazonbot, Amzn-SearchBot, Amzn-User: UA tipo Chrome, JS no documentado, probablemente HTML sin ejecutar) y **agente transaccional** (Buy for Me/Nova Act: navegador real con JS, sin identificación). El segundo es el único caso documentado (por terceros) de lectura con JS completo en las tres empresas, pero su función es comprar, no descubrir/comparar, y está limitado a EE. UU.
- Amzn-User es el fetcher relevante para que Alexa+ responda en España sobre una ficha externa, con perfil de JS desconocido.

### Gaps
- No hay documentación oficial de Amazon sobre cómo Nova Act/Buy for Me lee la página (DOM, árbol de accesibilidad o capturas) ni sobre JSON-LD.
- No confirmé que Rufus/Alexa for Shopping responda en amazon.es sobre productos fuera de Amazon, ni que Buy for Me esté disponible en España/UE (no encontré indicios).
- `AmazonProductDiscovery` aparece solo en un catálogo de terceros; sin UA ni documentación oficial.

## 4. Transversal: JSON-LD, cookies/consentimiento, IP/idioma, España, y el perfil base de la auditoría

### Takeaway
Ninguna de las tres empresas documenta para sus agentes la ejecución de JS, el tratamiento del consentimiento de cookies, el Accept-Language ni el país de las IP. Solo Microsoft (declaración pública) confirma el uso de Schema.org por sus LLM; Meta documenta Open Graph para vistas previas. La evidencia empírica disponible apoya «HTML de la respuesta HTTP sin JS» como perfil base para los crawlers y fetchers de IA, con un render en Chrome como perfil secundario (Bingbot, agentes de navegador).

### Cited Findings
- Vercel/MERJ (dic. 2024): ninguno de los grandes crawlers de IA estudiados (incluido Meta-ExternalAgent) renderiza JS; recomiendan servir en el servidor el contenido crítico (texto, metadatos, navegación). — [Vercel](https://vercel.com/blog/the-rise-of-the-ai-crawler)
- Bing ejecuta JS con Edge evergreen (2019) pero recomendó dynamic rendering (2018) para webs dependientes de JS. — [Bing 2019](https://blogs.bing.com/webmaster/october-2019/The-new-evergreen-Bingbot-simplifying-SEO-by-leveraging-Microsoft-Edge); [Bing 2018](https://blogs.bing.com/webmaster/october-2018/bingbot-Series-JavaScript,-Dynamic-Rendering,-and-Cloaking-Oh-My)
- Schema.org en Bing/Copilot (Canel, mar. 2025). — [Search Engine Land](https://searchengineland.com/microsoft-bing-copilot-use-schema-for-its-llms-453455)
- Open Graph en el primer MB para facebookexternalhit. — [Meta](https://developers.facebook.com/docs/sharing/webmasters/web-crawlers)
- El agente de Buy for Me llega con cookies nuevas y localStorage vacío (es decir, sin consentimiento previo almacenado). [tercero] — [cside](https://cside.com/blog/how-to-block-amazon-buy-for-me)
- Disponibilidad en España a oct. 2026: Copilot Checkout solo EE. UU./USD/inglés [oficial] ([Microsoft Advertising](https://about.ads.microsoft.com/en/solutions/technology/agentic-commerce)); Buy for Me beta EE. UU. ([Yahoo Finance](https://finance.yahoo.com/news/amazons-ai-agent-shop-third-003540471.html)); Muse Spark empezó en EE. UU. ([Meta](https://about.fb.com/news/2026/04/introducing-muse/)); Alexa+ en acceso anticipado en España desde 23-4-2026 ([WWWhatsNew](https://wwwhatsnew.com/2026/04/24/alexa-plus-espana-lanzamiento-precio-prime-abril-2026/)).

### Inferences
- Mantener **«respuesta HTTP sin ejecutar JS»** como perfil base es coherente con todos los crawlers y fetchers de IA documentados de Meta y Amazon y con el suelo de Bingbot. Añadir un **perfil secundario renderizado** (Chrome por CDP, sin interacción) cubriría Bingbot/Copilot y los agentes de navegador (Buy for Me), que son minoritarios o no disponibles en España en el periodo.
- Ningún agente documentado acepta un banner de consentimiento: el perfil sin cookies previas (estado limpio) es el realista; el contenido tapado o diferido por el CMP en el render no debería contarse como disponible para crawlers.
- Ninguna empresa documenta locale ni Accept-Language: el UA llega probablemente desde IP de EE. UU. (Amazon publica listas de IP; Meta las recomienda) y sin cabecera de idioma específica. Webs españolas con redirección por geo-IP o idioma podrían servir otra versión; conviene que la auditoría registre la variante servida y pruebe sin Accept-Language es-ES.
- En el canon, la vía principal de producto de Meta (catálogo/Commerce) y de Microsoft (Merchant Center) es el ámbito **Catálogos distribuidos**, no la Web.

### Gaps
- No hay mediciones empíricas recientes (2026) y fiables del renderizado de meta-externalfetcher, meta-webindexer, Amzn-User ni Amzn-SearchBot.
- No hay datos públicos del país de origen de las IP de los crawlers de Meta/Microsoft ni de las cabeceras Accept-Language que envían.
- No encontré datos de Cloudflare Radar de 2026 específicos de estos agentes (no se consultaron por límite de llamadas).
