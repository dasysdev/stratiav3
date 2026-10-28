# Un solo perfil de consumo: sin JavaScript y con todo el documento

Decisión del usuario del 2026-10-28, tomada en sesión tras la investigación «Perfil de consumo de agentes IA» (informe en `reports/Perfil de consumo de agentes IA.md`, notas en `research_notes/Perfil de consumo de agentes IA/`), y recogida por Claude el mismo día.

## Lo que planteaba la investigación (resumen de Claude)

- Las IA leen una ficha por dos vías. La **lectura en vivo** (ChatGPT-User, Claude-User, Perplexity-User, lectura de Meta AI, Copilot, lectura de URL de Gemini) pide solo el HTML de la respuesta, sin ejecutar JavaScript, y casi siempre lo reduce a texto visible antes de dárselo al modelo, de modo que el JSON-LD casi nunca llega. La **vía de índice** puede renderizar: Google siempre (Chromium móvil sin estado; de ese índice salen AI Overviews, el Modo IA y Gemini), Bing a veces, OpenAI quizá (un solo indicio). Los navegadores agénticos renderizan, pero interactúan.
- Propuesta del informe: perfil A (respuesta HTTP sin JS, con una capa que anota si cada hecho está en texto visible o solo en marcado), perfil B (DOM tras la carga, Chrome Android, como segundo perfil), sondas G (IP de EE. UU.) y L (`Accept-Language: en-US`), y endurecer el contexto de la petición: contexto de navegador nuevo por ficha frente al perfil persistente de Chrome de capture, que puede arrastrar el consentimiento; sin `Accept-Language`, que Chrome envía siempre; IP de origen registrada; user agent de Chrome con un token propio declarado; matriz de robots.txt por bot.
- Tensión señalada: el canon define Web como HTML + Schema.org, pero la lectura en vivo entrega al modelo solo el texto visible.

## Decisión del usuario

> vamos dejar solo un perfil que no ejecuta js y utiliza todo el DOM

> Nos basamos en que es más compatible y preferible generalmente que la información no dependa de ejecución de javascript (aunque algunos sistemas sí puedan leerla). Es una condición que decidimos adoptar ahora.

(Texto del usuario con las erratas corregidas: «vamos dejar solo un perfil que no ejecuta js y utiliza todo el DOM» y «Nos basamso en que es mas compatible y preferible geenralemnte que la ifnromación no dependa de ejecuciónd e javascripr. (anque algunos sistemas si peudan leerla) Es una condición que decimiso adoptar ahora.»)

El usuario no se pronunció sobre el contexto de la petición (estado, `Accept-Language`, IP, user agent, robots.txt, sondas).
