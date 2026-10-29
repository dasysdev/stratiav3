---
id: T-081
title: Reserva TDM previa en la auditoría de capture: parar y avisar
status: hecha
depends: T-080
milestone:
created: 2026-10-29
closed: 2026-10-29
---

## Objetivo

Que la auditoría de capture (pages audit y la araña) compruebe la reserva TDM antes de capturar: tdmrep.json y la cabecera y la meta tdm-reservation de la portada. Si hay reserva, no captura nada, para y avisa. Una reserva que aparece a mitad del proceso también lo para. Solo la auditoría: los demás procesos no cambian.

## Criterios de aceptación

- [x] Con reserva en tdmrep.json o en la portada, pages audit no captura ninguna página, sale con error y un mensaje claro, y el manifiesto registra la parada con su evidencia
- [x] Una reserva en la cabecera o la meta de una página interior para el proceso y queda registrada
- [x] El entrenamiento, el MPIR, PAA y la captura suelta no cambian; pruebas de capture en verde

## Resultado

La auditoría de capture comprueba la reserva TDM antes de capturar y para ante cualquier reserva (D-171)

## Notas

- 2026-10-29 Canon: D-171 (lecturas de Claude: la petición de la portada para comprobar sigue D-042; una reserva a mitad para el proceso, la página con reserva no se conserva y lo anterior sí; «avisa» = la orden sale con error y mensaje, y el manifiesto registra la parada con evidencia). Al terminar, actualizar capture/README (Legitimidad, Páginas de una auditoría) y la fila de capture del CLAUDE.md raíz.
- 2026-10-29 Hecho: audit.run comprueba tdmrep.json antes de nada; la portada es la primera visita (antes de los sitemaps) y completa la comprobación; un resultado reserved (página, o tdmrep.json de otro origen, también el de un sitemap) para la auditoría; manifiesto con reservation (where, url, source, evidencia); pages audit sale con código 3 y mensaje en stderr. Lectura de Claude: cualquier entrada de tdmrep.json que reserva una ruta es reserva del sitio (coherente con «una reserva a mitad para el proceso»). Para T-082: reutilizar tdm.reserving/tdm.signals y el patrón stop_reserved de audit.run.
