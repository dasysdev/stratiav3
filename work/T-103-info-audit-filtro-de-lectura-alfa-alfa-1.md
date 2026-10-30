---
id: T-103
title: info-audit: filtro de lectura Alfa (alfa/1)
status: pendiente
depends: T-097
milestone: piloto-gsc-bb
created: 2026-10-30
---

## Objetivo

Implementar en info-audit el filtro Alfa según docs/20-methods/audit-gsc/filter-alfa.md: de response.html (audit-es) al contenido del ámbito Contenido, en JSON con sus fragmentos y anotaciones.

## Criterios de aceptación

- [ ] info-audit tiene un comando que aplica alfa/1 a una ficha congelada de capture (page-ID) y escribe el JSON de filter-alfa.md (filter, version, ficha, title, text, fragments)
- [ ] Sobre la ficha de canarios (research_notes/text-reading-canaries/site/index.html), la salida contiene exactamente los códigos de las reglas Entra y ninguno de No entra; prueba automática
- [ ] Cada fragmento lleva posicion y ruta, y las anotaciones oculto, region, control, alt y enlace según la especificación; pruebas por anotación
- [ ] Sobre la ficha del edredón de BB, la composición, el envío y las devoluciones salen con la anotación oculto
- [ ] info-audit/README describe el filtro y su versión

## Notas

- 2026-10-30 Entrada (T-097): bin/audit validate lee la salida de alfa/1 por filter, version, ficha, title y text; posicion es [inicio, fin) en text. Mantén esos nombres.
- 2026-10-30 Saneamiento: el piloto no tiene auditoría de capture (decisión del usuario, T-094). El comando recibe el page-ID de la ficha audit-es.
