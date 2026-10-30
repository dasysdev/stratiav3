---
id: T-103
title: info-audit: filtro de lectura Alfa (alfa/1)
status: hecha
depends: T-097
milestone: piloto-gsc-bb
created: 2026-10-30
closed: 2026-10-30
---

## Objetivo

Implementar en info-audit el filtro Alfa según docs/20-methods/audit-gsc/filter-alfa.md: de response.html (audit-es) al contenido del ámbito Contenido, en JSON con sus fragmentos y anotaciones.

## Criterios de aceptación

- [x] info-audit tiene un comando que aplica alfa/1 a una ficha congelada de capture (page-ID) y escribe el JSON de filter-alfa.md (filter, version, ficha, title, text, fragments)
- [x] Sobre la ficha de canarios (research_notes/text-reading-canaries/site/index.html), la salida contiene exactamente los códigos de las reglas Entra y ninguno de No entra; prueba automática
- [x] Cada fragmento lleva posicion y ruta, y las anotaciones oculto, region, control, alt y enlace según la especificación; pruebas por anotación
- [x] Sobre la ficha del edredón de BB, la composición, el envío y las devoluciones salen con la anotación oculto
- [x] info-audit/README describe el filtro y su versión

## Resultado

Filtro Alfa alfa/1 en info-audit: canarios exactos y anotaciones; el edredón saca composición, envío y devoluciones como ocultos

## Notas

- 2026-10-30 Entrada (T-097): bin/audit validate lee la salida de alfa/1 por filter, version, ficha, title y text; posicion es [inicio, fin) en text. Mantén esos nombres.
- 2026-10-30 Saneamiento: el piloto no tiene auditoría de capture (decisión del usuario, T-094). El comando recibe el page-ID de la ficha audit-es.
- 2026-10-30 Hecho (agente): info-audit/bin/audit alfa PAGE-ID → info-audit/var/representations/PAGE-ID.alfa-1.json (filter, version, ficha, source, title, text, fragments). Lee los bytes originales de audit-es (sha256 y perfil comprobados); árbol HTML propio sobre html.parser y codificación por el Encoding Standard; desde el host delega en el contenedor (Python 3.13). 100 pruebas de info-audit en verde.
- 2026-10-30 Canarios: los 36 códigos de Entra y ninguno de los 22 de No entra. Edredón: composición (9.650), envío (10.178) y devoluciones (10.720) con oculto [aria-hidden, inert] y region aside. Edredón 14.208 caracteres y 509 fragmentos (262 ocultos); Barbie 12.229 y 472 (245). Igual al filtro sobre el DOM de Chrome en 54 fichas audit-es de 5 sitios.
- 2026-10-30 Discrepancias: los fragmentos usan start/end como dice el formato de filter-alfa.md (posicion = [start, end)); dos botones seguidos salen pegados («DescripciónEnvíos»), candidato a alfa/2; reading-filters.md dice que la composición del edredón empieza en el carácter 10.035 (texto de T-101) y con alfa/1 empieza en 9.638: pasa al /docs-update del saneamiento. Propuesta sin tarea: capture.pages.info(ID) y response_bytes(ID).
