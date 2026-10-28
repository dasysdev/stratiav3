---
id: T-069
title: Perfiles de captura en capture y perfil de auditoría de D-157
status: hecha
depends:
milestone:
created: 2026-10-28
closed: 2026-10-28
---

## Objetivo

Que capture admita varios perfiles de captura con nombre, que quien captura elige al pedir la captura, y que uno de ellos sea el perfil de auditoría informativa de Web y Web Schema.org (D-156, D-157): un navegador real que no ejecuta JavaScript, con estado limpio por ficha, `Accept-Language` es-ES, IP española registrada, user agent real y robots.txt registrado por bot. El perfil actual (Chrome persistente, el que usan PAA, el entrenamiento y el MPIR) sigue igual y es el perfil por defecto. Con el usuario se resuelve cómo cumple el perfil de auditoría «no ejecuta JavaScript» (OQ-80).

## Criterios de aceptación

- [x] Diseño de los perfiles de captura acordado con el usuario: qué fija un perfil, cómo se elige y qué perfil queda registrado en la ficha congelada
- [x] El perfil actual sigue siendo el de por defecto y no cambia: PAA, el entrenamiento y el MPIR capturan igual que antes (pruebas existentes en verde)
- [x] Propuesta para OQ-80 (desactivar JavaScript en Chrome frente a leer response.html de una carga con JavaScript) acordada con el usuario y llevada al canon con /docs-update
- [x] Perfil de auditoría: antes de cada captura borra las cookies y el almacenamiento del dominio y nunca acepta un banner; probado con una ficha de un dominio ya capturado con el perfil actual
- [x] Perfil de auditoría: la ficha congelada registra el perfil usado, `Accept-Language`, IP de origen, país y ASN
- [x] Perfil de auditoría: la ficha congelada registra qué permite robots.txt a GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-User, PerplexityBot, Googlebot, Google-Extended, Bingbot y los bots de Meta y Amazon
- [x] Tasa de desafíos del perfil de auditoría medida en un lote de prueba frente a la del perfil actual

## Resultado

Perfiles de captura en capture: reader (por defecto, sin cambios) y audit-es (D-157/D-163: sin JS, contexto desechable por ficha, respuesta HTTP con bytes originales, cabeceras de cada salto, Accept-Language, origen IP/país/ASN y robots.txt por bot); OQ-80 cerrada por D-163; tasa de desafíos 1/22 frente a 0/22

## Notas

- 2026-10-28 Usuario: «T-069 no debe modificar todos los perfiles. Es un perfil específico identificado que lo usaremos cuando consideremos. El perfil para capturar PAA sigue igual. De alguna forma estoy planteando que capture tenga múltiples perfiles.»
- 2026-10-28 T-072 (perfil de Web, D-159): los requisitos técnicos de Web necesitan del perfil de auditoría, además de robots.txt por bot (ya en los criterios), los bytes originales del cuerpo de la respuesta (hoy response.html es el cuerpo decodificado por Chrome y pasado a UTF-8, sin BOM): sin ellos, la codificación real y la posición en bytes de la declaración son NE, y las cabeceras de cada salto de redirección (hoy solo url, status y to).
- 2026-10-28 Diseño acordado con el usuario: perfiles con nombre en capture/profiles.py; reader (por defecto, el actual) y audit-es (D-157): contexto de navegador desechable por ficha (más estricto que borrar el dominio; no toca el perfil persistente de PAA), JavaScript desactivado (Emulation.setScriptExecutionDisabled), primera carga sin desplazar, ID.html = documento de la respuesta en UTF-8, bytes originales (Fetch, con BOM) y cabeceras de cada salto, robots.txt por bot. Elección: pages fetch --profile, pages.fetch(profile=), crawl. La ficha registra profile. OQ-80: A (JS desactivado), medir tasa de desafíos y C (JS solo para pasar el desafío y recarga sin JS) solo si los datos lo piden. IP: el usuario «ignora lo de la ip»: sin comprobación ni rechazo; solo se registra IP/país/ASN (RIPEstat).
- 2026-10-28 Lote de desafíos (22 portadas de tiendas españolas, una visita por perfil, 2026-10-28; capture/var/tmp/challenge-lot/): audit-es 21 capturadas, 1 desafío (Fnac, DataDome 403 con CAPTCHA en la primera respuesta, antes de cualquier JS: atribuible al contexto nuevo, no a la falta de JS; C no lo resolvería); reader 21 capturadas, 0 desafíos, 1 error (Zara: Network.getResponseBody sin recurso). Tasa de desafíos 4,5 % frente a 0 %. Pruebas reales con audit-es: audit-cojin-018, audit-cuerda-tootoy, audit-eci-aceite-010695 (dominios ya capturados con reader): 200, bytes originales, ES/AS3352.
- 2026-10-28 T-074 (D-161, D-162): la auditoría técnica necesitará además congelar los sitemaps del sitio (declarados en robots.txt o /sitemap.xml, con índices y gzip; buscar la URL de la página en los grandes) y páginas de otros tipos (categoría, políticas y contenido, portada); qué páginas, en OQ-85.
