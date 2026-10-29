---
id: T-087
title: Requisitos de acceso a las imágenes del marcado en web-audit
status: hecha
depends: T-086
milestone:
created: 2026-10-29
closed: 2026-10-29
---

## Objetivo

web-audit extrae las URL de imagen del marcado de las páginas de una auditoría, pide su acceso a capture (T-086) y evalúa con esas respuestas los requisitos de acceso: rastreable (ws-consumer/004, 185) e indexable (005, 186, 335). Los requisitos de dimensiones, relación de aspecto y formato (007–010, 333, 336) siguen en la referencia y dan NE con el motivo «fuera de V1».

## Criterios de aceptación

- [x] Un comando de web-audit pasa a capture la lista de URL de imagen del marcado de una auditoría (image, logo, thumbnailUrl y el contentUrl o url de ImageObject)
- [x] ws-consumer/004 y 185 dan satisfecho si robots.txt no bloquea a Googlebot-Image y la respuesta es de éxito; no satisfecho si bloquea o falla
- [x] ws-consumer/005, 186 y 335 se evalúan con la cabecera X-Robots-Tag de la respuesta
- [x] ws-consumer/007–010, 333 y 336 dan NE con el motivo «fuera de V1: no se descargan las imágenes»; la referencia no cambia
- [x] Una URL que capture no pidió o no registró da NE con su motivo
- [x] Pruebas de web-audit en verde y el README de web-audit lo describe

## Resultado

audit images pasa a capture las imágenes del marcado; 004/005/185/186/334/335 leen sus respuestas, 007–010/333/336 NE fuera de V1

## Notas

- 2026-10-29 Googlebot-Image sin grupo propio cae en el de Googlebot (y después en *), como dice el método; antes caía directamente en *. Una URL con outcome failed (sin respuesta) da NE, no no satisfecho: no prueba un fallo del servidor. Probado con todoplano-t049: audit images pidió 1 URL a images.logicommerce.cloud (200) y 004, 005, 185 y 186 dan satisfecho. eci-t049 tiene 10 URL en dam.elcorteingles.es aún sin pedir.
