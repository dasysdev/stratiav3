# Perfil de consumo de Google para fichas de producto (AI Overviews, Modo IA, Gemini, compra agéntica) — estado a 28-10-2026

Nota de investigación. Fuentes oficiales: developers.google.com, ai.google.dev, blog.google. Las fuentes secundarias se marcan como **[secundaria]**. Las fechas «Last updated» son las del pie de cada página oficial, consultada el 28-10-2026.

## 1. Googlebot: renderizado de JavaScript, límites y user agents

### Takeaway
Googlebot sigue un proceso documentado de tres fases (rastreo → renderizado → indexación). **Todas las páginas que devuelven 200 entran en la cola de renderizado** de un Chromium headless evergreen, y lo que se indexa es el HTML renderizado. El renderizado es diferido y sin estado (cookies y almacenamiento se borran entre cargas, los permisos se deniegan, no hay WebSockets) y se limita a 2 MB por recurso. La indexación es mobile-first: casi todo el rastreo usa Googlebot Smartphone.

### Cited Findings
- Tres fases: «Google processes JavaScript web apps in three main phases» (crawling, rendering, indexing). — [JavaScript SEO basics, act. 2026-03-04](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- «Googlebot queues all pages with a `200` HTTP status code for rendering». La espera en cola «may stay on this queue for a few seconds, but it can take longer than that». — [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- Si el estado no es 200, «rendering might be skipped». Con `noindex`, «it may skip rendering and JavaScript execution». — [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- Motor: «Google Search runs JavaScript with an evergreen version of Chromium». En el renderizado, «a headless Chromium renders the page and executes the JavaScript». Del HTML renderizado se vuelven a extraer los enlaces, y es lo que se indexa. — [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- En los sitios app shell, «the initial HTML does not contain the actual content»: Google los indexa ejecutando el JS. — [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- Shadow DOM: Google «flattens the shadow DOM and light DOM»; solo se indexa lo que es visible en el HTML renderizado. — [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- Caché: «Googlebot caches aggressively in order to reduce network requests and resource usage». WRS puede ignorar las cabeceras de caché y usar JS/CSS desactualizados. — [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics); [Fix Search-related JavaScript problems, act. 2025-12-18](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript)
- Sin estado: WRS no conserva estado entre cargas. Local Storage, Session Storage y las cookies HTTP «are cleared across page loads». — [Fix Search-related JavaScript problems](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript)
- Se espera que Googlebot rechace las peticiones de permiso («Features that require user permission don't make sense for Googlebot»). Solo usa HTTP y «does not support other types of connections» (WebSockets, WebRTC). No admite WebGL. Sigue las redirecciones de servidor y de cliente. Puede omitir recursos que juzga no esenciales para el contenido. — [Fix Search-related JavaScript problems](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript)
- Enlaces: solo se descubren los `<a href>`. Se desaconseja el enrutado por fragmentos (#). — [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- Límite de tamaño de Googlebot: «Googlebot crawls the first 2MB of a supported file type, and the first 64MB of a PDF file». Se mide sin comprimir, y solo la parte descargada pasa a indexación. «each resource referenced in the HTML (such as CSS and JavaScript) is fetched separately», cada uno con el mismo límite. — [Googlebot, act. 2026-02-03](https://developers.google.com/search/docs/crawling-indexing/googlebot)
- El límite genérico de la infraestructura de rastreo es de 15 MB («only crawl the first 15MB of a file»), y cada rastreador puede fijar el suyo (por ejemplo, 2 MB para Googlebot). HTTP/1.1 por defecto, con HTTP/2 admitido. gzip, deflate y br. ETag/If-None-Match y Last-Modified. — [Overview of Google crawlers, act. 2026-06-12](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers)
- Mobile-first: «For most sites Google Search primarily indexes the mobile version of the content». Googlebot Smartphone y Googlebot Desktop comparten el token `Googlebot` en robots.txt. — [Googlebot](https://developers.google.com/search/docs/crawling-indexing/googlebot)
- User agents (abreviados en la fuente): Smartphone `Mozilla/5.0 (Linux; Android 6.0.1; …) … (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`; Desktop `Mozilla/5.0 AppleWebKit/537.36 (…; compatible; Googlebot/2.1; …) Chrome/W.X.Y.Z Safari/537.36` (W.X.Y.Z es la versión de Chrome). — [Google's common crawlers, act. 2026-10-15](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)

### Inferences
- El índice que alimenta a Search es **el DOM renderizado**, no la respuesta HTTP. En una ficha de producto cuyo precio, variantes o JSON-LD se inyectan con JS, Google ve ese contenido una vez renderizada la página (con retraso y sin garantía).
- Un perfil base «respuesta HTTP sin JS» es **más estricto** que Googlebot. Detecta lo que está en el HTML inicial, que es la vía más fiable y la que Google recomienda para datos de producto (ver §4). Pero declararía ausente información que Google sí consume tras renderizar.
- Lo que un DOM renderizado por Google **no** incluye: contenido tras clics o interacción, contenido tras conceder permisos, estado de cookies previas, WebSockets. Eso encaja con la restricción del proyecto de no navegar interactivamente.

### Gaps
- Google no publica en las páginas consultadas un **timeout de renderizado**, un presupuesto de renderizado ni un límite de CPU. Se cita a menudo una cifra de «~5 s», pero no la encontré en documentación oficial vigente.
- La «indexación en dos oleadas» (two waves) es un marco de Google I/O 2018. La documentación vigente habla de una cola de renderizado. No verifiqué en esta sesión si Google la ha descrito como superada.
- El anuncio de Googlebot evergreen (blog de Search Central, mayo de 2019) no se consultó en esta sesión.
- No hay cifra oficial del **viewport** del renderizador (ver §6).

## 2. AI Overviews, Modo IA y Gemini: ¿índice renderizado o captura en vivo? Fetchers separados

### Takeaway
AI Overviews y el Modo IA se nutren del **índice de Google Search**. Para aparecer, la página debe estar indexada y ser elegible para fragmento, sin más requisitos técnicos. El grounding de Gemini (Apps y Vertex AI) se define oficialmente como «providing content from the Google Search index to the model at prompt time». Las capturas bajo demanda («URL context» de la API de Gemini, Gemini Notebook, Google-Agent) son otro canal: consultan primero el índice o caché y, si falta, hacen una captura en vivo. Los fetchers activados por el usuario en general **no respetan robots.txt**.

### Cited Findings
- Requisito de AI Overviews y Modo IA: «a page must be indexed and eligible to be shown in Google Search with a snippet». «There are no additional technical requirements». — [AI features and your website, act. 2025-12-10](https://developers.google.com/search/docs/appearance/ai-features)
- Ambas funciones «may use a 'query fan-out' technique — issuing multiple related searches across subtopics and data sources». «While responses are being generated, our advanced models identify more supporting web pages». — [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- Controles: nosnippet, data-nosnippet, max-snippet y noindex. Si el contenido sigue apareciendo, conviene comprobar que el control es «correct and visible to Googlebot». Esto indica que la lectura es la de Googlebot. — [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- Google-Extended no tiene user agent propio: es un token de robots.txt. Controla si el contenido «may be used for training future generations of Gemini models» (Gemini Apps, Vertex AI API) y el grounding, definido como «providing content from the Google Search index to the model at prompt time». «does not impact a site's inclusion in Google Search» y no es señal de ranking. La página no menciona los AI Overviews. — [Google's common crawlers, act. 2026-10-15](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
- Según la página de funciones IA, Google-Extended es el control para «AI training and grounding in some of Google's other systems», y el rastreo de Search lo gobiernan las reglas de Googlebot. — [AI features and your website](https://developers.google.com/search/docs/appearance/ai-features)
- GoogleOther (`…(compatible; GoogleOther)`, en móvil y escritorio) es un rastreador genérico para equipos de producto, sin producto específico. Google-CloudVertexBot rastrea, a petición del propietario del sitio, para Vertex AI Agents, y «no effect on Search». Google-InspectionTool solo da servicio a Rich Results Test e Inspección de URLs. — [Google's common crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
- Los fetchers activados por el usuario «generally ignore robots.txt rules». Lista vigente: Google-Agent; Gemini Notebook (`Google-GeminiNotebook`, que sustituye a `Google-NotebookLM`, admitido hasta agosto de 2026); Google-Read-Aloud; Google Messages; Google-Pinpoint; FeedFetcher; GoogleProducer; Google-Site-Verification; Google-CWS. La página no dice si renderizan. — [Google's user-triggered fetchers, act. 2026-08-19](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers)
- «URL context» de la API de Gemini: primero un índice interno en caché. «If a URL is not available in the index (for example, if it's a very new page), the tool automatically falls back to do a live fetch». Hasta 20 URL por petición y 34 MB por URL. Admite HTML, JSON, XML, PDF e imágenes. No admite contenido de pago ni tras login. La página no indica user agent ni si ejecuta JS. — [URL context, ai.google.dev, act. 2026-10-13](https://ai.google.dev/gemini-api/docs/url-context)

### Inferences
- En AI Overviews y el Modo IA, el «perfil de consumo» es el de Googlebot Smartphone más el renderizado WRS: lo que lee la IA es lo que hay en el índice, es decir, el DOM renderizado (§1).
- Cuando un usuario de Gemini pega una URL de producto, lo más probable es la ruta «índice o caché primero, captura en vivo si falta». Así lo documenta la herramienta URL context de la API, y la app de Gemini usa probablemente un mecanismo análogo, aunque esto no está documentado para la app. El UA de esa captura en vivo no consta oficialmente.
- Para una auditoría de fichas en España, el canal dominante (índice) se emula mejor con un **DOM renderizado sin interacción** desde un móvil. La respuesta HTTP sin JS emula el peor caso: una captura en vivo que no renderiza, sin confirmar.

### Gaps
- No hay documentación oficial sobre qué fetcher (UA) usa la **app de Gemini** cuando el usuario pide leer una URL, ni sobre si renderiza JS.
- No encontré documentación oficial que confirme si el Modo IA hace capturas en vivo fuera del índice durante el fan-out.
- La página de user-triggered fetchers no aclara si Google-Agent, Read Aloud o Gemini Notebook ejecutan JS.

## 3. Funciones agénticas: checkout agéntico, Let Google Call, UCP, auto browse en Chrome y Google-Agent

### Takeaway
Hay dos familias. (a) **Compra en superficies de Google** (checkout agéntico, checkout nativo con UCP en el Modo IA y la app de Gemini): funciona sobre **Merchant Center (feed de productos) y el Shopping Graph**, con APIs de UCP y Google Pay, no navegando la web. Solo está disponible en EE. UU. (b) **Agentes que navegan** (auto browse de Gemini en Chrome, Project Mariner o agentes alojados en Google con el UA `Google-Agent`): usan un **navegador real**, con clics y formularios. Solo se ofrecen en EE. UU. o con suscripción. Ninguno de los dos opera hoy para comercios en España.

### Cited Findings
- I/O 2025 (mayo de 2025): el Modo IA para compras combina Gemini con el Shopping Graph. Se citan unos 50 000 millones de listados, más de 2000 millones actualizados cada hora. Se anunció el checkout agéntico para EE. UU. — **[secundaria]** [Retail TouchPoints](https://www.retailtouchpoints.com/topics/digital-commerce/google-brings-advanced-ai-capabilities-to-search-including-virtual-try-on-agentic-checkout); [Digital Commerce 360, 20-05-2025](https://www.digitalcommerce360.com/2025/05/20/google-ai-shopping-experiences/)
- 13-11-2025: el checkout agéntico empieza a desplegarse en Search y el Modo IA «from eligible merchants in the U.S. like Wayfair, Chewy, Quince and select Shopify merchants». Parte del seguimiento de precio («Track price»). Google prevé ampliarlo a medida que más comercios admitan guest checkout y Google Pay. «Let Google Call» llama a tiendas locales para consultar stock. — [blog.google, «Let AI do the hard parts of your holiday shopping»](https://blog.google/products/shopping/agentic-checkout-holiday-ai-shopping/); **[secundaria]** [9to5Google, 13-11-2025](https://9to5google.com/2025/11/13/google-agentic-shopping/); [TechCrunch, 13-11-2025](https://techcrunch.com/2025/11/13/google-expands-ai-shopping-with-conversational-search-agentic-checkout-and-an-ai-that-calls-stores-for-you)
- UCP (Universal Commerce Protocol): estándar abierto anunciado en la NRF (enero de 2026), codesarrollado con Shopify, Etsy, Wayfair, Target y Walmart. Une descubrimiento, checkout y posventa. Se declara compatible con MCP y AP2. — **[secundaria]** [TechCrunch, 11-01-2026](https://www.techcrunch.com/2026/01/11/google-announces-a-new-protocol-to-facilitate-commerce-using-ai-agents/); [InfoQ, 01-2026](https://infoq.com/news/2026/01/google-agentic-commerce-ucp)
- Guía oficial de UCP en Merchant Center: el hub permite configurar la cuenta, probar las integraciones de API y declarar que se está listo. Solo los productos con el atributo de feed `native_commerce(checkout_eligibility)` muestran el botón **Buy now**. Las operaciones son de carrito (por ejemplo, «transferring to a merchant's cart») y de checkout («creating a checkout, updating shipping settings, or completing a transaction»). Disponibilidad: «gradually rolling out in the United States, with Australia and Canada to follow early next year». «this applies only to products sold within the United States». Acceso anticipado con formulario de interés. — [Merchant UCP guides, act. 2026-10-19](https://developers.google.com/merchant/ucp/guides)
- Los requisitos de preparación (cuenta de Merchant Center, envíos, devoluciones, feed de productos, gestor de pagos de Google Pay para el checkout nativo) aparecen en el fragmento de búsqueda de la guía oficial. Se cita además un sandbox (octubre de 2026). — [Merchant UCP guides (fragmento)](https://developers.google.com/merchant/ucp/guides); **[secundaria]** [Relevant Audience](https://www.relevantaudience.com/ecommerce-marketing/google-merchant-center-ucp-integration-hub/)
- Auto browse en Chrome (Gemini 3): lanzado en vista previa el 28-01-2026 para suscriptores de AI Pro y Ultra en EE. UU. (Windows, macOS, Chromebook Plus). Navega, sigue enlaces y rellena formularios con teclado y ratón simulados, y pide confirmación para acciones sensibles. Llegó a Android en EE. UU. hacia el 19-08-2026. — [blog.google, «The new era of browsing: Putting Gemini to work in Chrome»](https://blog.google/products-and-platforms/products/chrome/gemini-3-auto-browse/); **[secundaria]** [9to5Google, 28-01-2026](https://9to5google.com/2026/01/28/chrome-gemini-auto-browse/); [ProPakistani, 19-08-2026](https://propakistani.pk/2026/08/19/google-chrome-on-android-gets-agentic-browsing-image-generation-and-more/amp/)
- Google-Agent: lo usan los agentes alojados en infraestructura de Google que «navigate the web and perform actions upon user request». Tiene UA móvil y de escritorio con «compatible; Google-Agent» y la versión de Chrome W.X.Y.Z, e ignora robots.txt como fetcher activado por el usuario. Experimenta con Web Bot Auth con la identidad `https://agent.bot.goog`. — [Google's user-triggered fetchers, act. 2026-08-19](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers)
- Fuentes secundarias citan Project Mariner como ejemplo de Google-Agent en la documentación. — **[secundaria]** [seo-kreativ.de](https://www.seo-kreativ.de/en/blog/google-user-agent-for-ai-agents-explained/); [suganthan.com](https://suganthan.com/notes/google-agent-crawler/)

### Inferences
- La compra agéntica de Google **no lee la ficha HTML**: la decisión y el pago se apoyan en el feed de Merchant Center, el Shopping Graph y las APIs de UCP. Para una auditoría que solo captura páginas, esto queda fuera del ámbito Web y cae en el de catálogos distribuidos (feed de Merchant Center).
- Los agentes que navegan (auto browse, Google-Agent) ven el DOM completamente renderizado de un Chrome real, con estado de sesión y capacidad de interacción. Es un perfil **más rico** que Googlebot. Como el proyecto excluye la navegación interactiva, ese perfil solo se puede emular hasta el DOM renderizado de la primera carga.
- España: nada de esto está disponible para comercios españoles a 28-10-2026, según las fuentes. UCP solo cubre EE. UU., con Australia y Canadá anunciados después, y auto browse solo EE. UU. Es plausible que llegue durante el perímetro (oct. 2026 – T1 2027), pero no hay anuncio.

### Gaps
- No encontré documentación oficial sobre si el checkout agéntico o UCP consultan la ficha web para validar precio o stock en el momento de la compra.
- No hay calendario oficial de UCP ni del checkout agéntico para la UE o España.
- La relación exacta entre Project Mariner y el UA Google-Agent no consta con certeza en la página oficial consultada (solo en secundarias).

## 4. Datos estructurados: JSON-LD inyectado por JS, Product/Offer y su papel frente a los feeds de Merchant Center

### Takeaway
Google **sí lee JSON-LD generado con JavaScript**, pero para fichas de producto advierte que eso hace los rastreos de Shopping «less frequent and less reliable» y recomienda el marcado Product en el HTML inicial. Para AI Overviews y el Modo IA no hace falta marcado Schema.org especial, aunque debe coincidir con el texto visible. Google no documenta cómo se combinan el marcado y los feeds de Merchant Center.

### Cited Findings
- «JavaScript can generate JSON-LD and inject it into the page», con la recomendación de probar la implementación. — [JavaScript SEO basics, act. 2026-03-04](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- Merchant listings: «dynamically-generated markup can make Shopping crawls less frequent and less reliable». «we recommend putting Product structured data in the initial HTML for best results». — [Merchant listing structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)
- Requisitos de Product: `name`, `image` y `offers`. «merchant listings require an Offer as the merchant has to be the seller of the product». «merchant listing experiences require a price greater than zero». `priceCurrency` es obligatorio si hay `price`. Recomendados en Offer: `availability`, `itemCondition`, `priceValidUntil`, `shippingDetails` y `hasMerchantReturnPolicy`. Para devoluciones se recomienda una política global en Organization. Algunos códigos de precio unitario «are only supported by Merchant Center feeds». — [Merchant listing structured data](https://developers.google.com/search/docs/appearance/structured-data/merchant-listing)
- Funciones IA: «There's also no special schema.org structured data that you need to add». Hay que asegurar que «your structured data matches the visible text on the page». — [AI features and your website, act. 2025-12-10](https://developers.google.com/search/docs/appearance/ai-features)
- Storebot-Google (`Storebot-Google/1.0`, en escritorio y móvil) es el rastreador de «All Google Shopping surfaces». — [Google's common crawlers, act. 2026-10-15](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
- La elegibilidad del botón Buy now en el Modo IA y Gemini depende de un atributo del **feed** (`native_commerce(checkout_eligibility)`), no del marcado. — [Merchant UCP guides, act. 2026-10-19](https://developers.google.com/merchant/ucp/guides)

### Inferences
- La advertencia sobre el marcado dinámico implica que el canal de Shopping (Storebot-Google o el procesado de Shopping) **no renderiza siempre**, o lo hace con menos frecuencia. Para Product/Offer, el HTML inicial es el perfil de lectura «seguro» que Google pide.
- Para la auditoría, conviene distinguir dos perfiles por ámbito: **Web Schema.org** con el marcado del HTML inicial como lectura fiable, y el marcado inyectado por JS como lectura posible pero degradada. En el ámbito **Web**, el contenido visible del DOM renderizado.

### Gaps
- Google no documenta oficialmente cómo pondera o combina el Shopping Graph el marcado Product de la página y el feed de Merchant Center (prioridad o resolución de conflictos).
- No consta oficialmente si Storebot-Google renderiza JS.
- No se leyó el tramo final de la página de merchant listings (propiedades de OfferShippingDetails ni fecha de actualización).

## 5. robots.txt, cookies y muros de consentimiento, locale (IP de EE. UU., Accept-Language) y relevancia para España

### Takeaway
Los rastreadores comunes respetan siempre robots.txt, y los recursos bloqueados no se renderizan. Los fetchers activados por el usuario en general lo ignoran. Googlebot es sin estado (no conserva cookies) y deniega permisos. Sale **sobre todo desde IP de EE. UU.** y **no envía Accept-Language**. Por tanto, las páginas que adaptan el idioma o el país pueden indexarse en su variante por defecto o estadounidense, salvo que haya URL por locale con hreflang.

### Cited Findings
- Googlebot comprueba robots.txt antes de capturar. «Google Search won't render JavaScript from blocked files or on blocked pages». — [JavaScript SEO basics](https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics)
- Los rastreadores comunes respetan siempre robots.txt en los rastreos automáticos. Los especiales (AdsBot) pueden ignorar `*` con permiso. — [Overview of Google crawlers, act. 2026-06-12](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers)
- Los fetchers activados por el usuario «generally ignore robots.txt rules». — [Google's user-triggered fetchers](https://developers.google.com/crawling/docs/crawlers-fetchers/google-user-triggered-fetchers)
- Cookies: «HTTP cookies are cleared across page loads», igual que Local Storage y Session Storage. — [Fix Search-related JavaScript problems, act. 2025-12-18](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript)
- IP: «Google egresses primarily from IP addresses in the United States». Si detecta bloqueo de EE. UU., puede rastrear desde otros países. — [Overview of Google crawlers](https://developers.google.com/crawling/docs/crawlers-fetchers/overview-google-crawlers)
- Locale: «the crawler sends HTTP requests without setting `Accept-Language` in the request header». Googlebot también rastrea desde IP fuera de EE. UU. Usa el mismo UA en todas las configuraciones. Google recomienda URL separadas por locale con hreflang, y advierte que puede no rastrear, indexar ni posicionar todo el contenido de cada locale. — [Locale-adaptive pages, act. 2025-12-10](https://developers.google.com/search/docs/specialty/international/locale-adaptive-pages)
- El Modo IA está disponible en español desde el 23-09-2025 y en España desde el 08-10-2025, dentro de una expansión a unos 50 países y 36 idiomas. — **[secundaria]** [TechCrunch, 23-09-2025](https://techcrunch.com/2025/09/23/googles-ai-mode-arrives-in-spanish-globally/); [Última Hora, 08-10-2025](https://www.ultimahora.es/noticias/tecnologia-videojuegos/2025/10/08/2486443/modo-busqueda-google-llega-espana.html); [Marketing4Ecommerce](https://marketing4ecommerce.net/modo-ia-google-espana/)

### Inferences
- **Banners de consentimiento (RGPD/LSSI):** como Googlebot no hace clic ni guarda cookies, cada carga equivale a la de un **visitante nuevo que no ha consentido**. Lo que lee es el DOM con el banner presente y sin los scripts condicionados al consentimiento. Si el contenido comercial está superpuesto pero en el DOM, se indexa. Si el sitio lo retiene hasta el consentimiento (un muro), no. Esto es una inferencia a partir de la ausencia de estado y de interacción, no una declaración oficial.
- **España:** una ficha .es que redirige o adapta el contenido según la IP (por ejemplo, de EE. UU. a una versión internacional o en inglés) o según Accept-Language puede indexarse en una variante distinta de la española. La captura de la auditoría debería fijarse **sin Accept-Language** (o hacer constar ambas variantes) y registrar la IP de salida (española). Así se detectan divergencias que Google vería desde EE. UU.
- Una ficha bloqueada a Googlebot en robots.txt no entra en AI Overviews ni en el Modo IA, pero un fetcher activado por el usuario (Gemini Notebook, Google-Agent) puede leerla igualmente.

### Gaps
- No encontré declaración oficial de Google sobre el tratamiento de los muros de consentimiento de cookies (ni de Martin Splitt; la búsqueda no dio resultados citables).
- No consta si los fetchers de Gemini o Google-Agent salen desde IP europeas o envían Accept-Language.

## 6. Viewport y emulación móvil del renderizador

### Takeaway
Oficialmente solo consta que Googlebot Smartphone «simulates a mobile user», que su UA es Android con Chrome evergreen y que la indexación es mobile-first. Google no publica en las páginas consultadas las dimensiones del viewport del WRS.

### Cited Findings
- Googlebot Smartphone simula un usuario móvil y Googlebot Desktop uno de escritorio. La mayoría de las peticiones usan el rastreador móvil. — [Googlebot, act. 2026-02-03](https://developers.google.com/search/docs/crawling-indexing/googlebot)
- UA Smartphone: `Mozilla/5.0 (Linux; Android 6.0.1; …) … (compatible; Googlebot/2.1; …)`, con la versión de Chrome evergreen W.X.Y.Z. — [Google's common crawlers, act. 2026-10-15](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers)
- La página de problemas de JS no trata el viewport ni el lazy loading. Remite a una guía aparte de lazy loading. — [Fix Search-related JavaScript problems](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript)

### Inferences
- La emulación razonable para la auditoría es un **perfil móvil** (UA de Android con Chrome, viewport de móvil). El contenido que solo aparece en escritorio, o con lazy loading que depende del scroll, no debe darse por disponible en el perfil base.

### Gaps
- No hay cifra oficial del viewport del WRS. Hay cifras de la comunidad (un viewport móvil estrecho y una página «alargada» para disparar el lazy loading), pero no las verifiqué contra fuentes oficiales en esta sesión.
- Tampoco consta oficialmente cómo se tratan `IntersectionObserver` ni el scroll en el renderizado.

---
**Nota para la decisión del perfil base (síntesis de las inferencias anteriores, no de una fuente):** el canal de Google que llega a AI Overviews, al Modo IA y al grounding de Gemini es el **índice de Search**, construido con el **DOM renderizado** por un Chromium headless móvil, sin estado ni interacción. Por eso el DOM renderizado sin interacción (perfil móvil, sin cookies, sin Accept-Language) es la emulación más fiel de Google. La respuesta HTTP sin JS representa el canal «fiable» que Google recomienda para Product/Offer (Shopping) y el peor caso de las capturas en vivo no documentadas. Una opción coherente con las fuentes es tomar el DOM renderizado como base de Google y registrar la diferencia con la respuesta HTTP como hallazgo de robustez.
