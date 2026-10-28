---
id: T-075
title: Fallo de reader en Zara: getResponseBody sin recurso
status: pendiente
depends:
milestone:
created: 2026-10-28
---

## Objetivo

Que el perfil reader capture la portada de zara.com/es: en el lote de T-069 falló con «Network.getResponseBody: No resource with given identifier found» con HTTP 200 (instantánea en capture/var/tmp/challenge-lot/www.zara.com/reader/).

## Criterios de aceptación

- [ ] Causa trazada en el motor (p. ej., el documento sustituido por una navegación de JavaScript) antes de culpar al sitio
- [ ] reader captura zara.com/es o la visita queda con un resultado que explica la causa
- [ ] Pruebas de capture en verde

## Notas
