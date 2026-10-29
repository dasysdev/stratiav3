---
id: T-086
title: Acceso a recursos de una auditoría por lista de URL en capture
status: hecha
depends:
milestone:
created: 2026-10-29
closed: 2026-10-29
---

## Objetivo

capture pide con GET una lista de URL de recurso de una auditoría (las imágenes del marcado, que extrae web-audit) y guarda el estado y las cabeceras de cada respuesta, sin el cuerpo. También congela el robots.txt de cada host de esas URL que no tenga ya en la auditoría (CDN). Aplica la legitimidad del motor, el ritmo y la parada por reserva TDM. capture no interpreta el marcado: la lista se la da quien la pide.

## Criterios de aceptación

- [x] Un comando de capture recibe una auditoría y una lista de URL y registra en capture/var/audits/AUDIT/, por cada URL, el estado final, las redirecciones y las cabeceras de la respuesta a GET
- [x] capture corta cada respuesta tras las cabeceras y no guarda ningún byte del cuerpo
- [x] El robots.txt de cada host de la lista que no esté ya en la auditoría queda congelado en ella
- [x] Si robots.txt prohíbe una URL a nuestro bot, capture no la pide y la registra como no pedida, con la regla
- [x] Una URL ya registrada en la auditoría no se vuelve a pedir
- [x] Pruebas con un sitio local (200, 404, 403, redirección, X-Robots-Tag noindex, host de CDN con robots.txt propio) y pruebas de capture en verde
- [x] capture/README y la fila de capture del CLAUDE.md raíz lo describen

## Resultado

pages resources: GET por lista de URL sin cuerpo, robots.txt de cada host nuevo, reservas TDM y 429 (resources.json)

## Notas

- 2026-10-29 Decisión del usuario (2026-10-29): para V1, acceso a las imágenes con GET (no HEAD: algunos CDN responden 405 o con otras cabeceras, y Google usa GET); sin guardar bytes de la imagen. Dimensiones, relación de aspecto y formato (ws-consumer/007–010, 333, 336) quedan fuera de V1. Medido en los expedientes: 8–26 URL de imagen por ficha; hosts de CDN en ECI (dam.elcorteingles.es) y todoplano (images.logicommerce.cloud).
- 2026-10-29 Mecanismo: Page.heads (Fetch en la fase de respuesta para todo recurso; sigue los 3xx con Location y aborta la última con Fetch.failRequest). Probado con images.logicommerce.cloud (todoplano-t049): 200, cabeceras HTTP/2 en minúsculas, robots.txt 404 del CDN en resources/sites/. Para T-087: la navegación envía el Accept de un documento, no el de una imagen; 429 = blocked, para y se repite; auditorías anteriores a la araña: el robots.txt conocido sale de audit.json.
