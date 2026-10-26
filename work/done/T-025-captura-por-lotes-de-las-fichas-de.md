---
id: T-025
title: Captura por lotes de las fichas de entrenamiento con el motor
status: hecha
depends: T-024
milestone: codigo
created: 2026-10-25
closed: 2026-10-25
---

## Objetivo

Capturar las 30 fichas del piloto de T-024 (las otras 270, en T-029) con crawl/SiteRun, a ritmo B y con tope diario de 300 para ECI, sin desplazamiento, y congelarlas en el formato que lee el clasificador

## Criterios de aceptación

- [x] Orden de captura por lotes del entrenamiento sobre crawl/SiteRun, con ritmo B (pausa 10–30 s; pausa larga 1–3 min cada 20–30), tope diario de 300 para ECI y sin desplazamiento: se guarda el HTML de la primera carga; pruebas en verde
- [x] Arranque escalonado: primeras 5 fichas, revisión del HTML de primera carga y continuación
- [x] Cada ficha capturada queda en var/pages/ID.html (el formato de taxo page fetch) con su instantánea; las que no existen se sustituyen por reservas de su categoría
- [x] Resumen por resultado (captured, blocked, gone, failed, disallowed) y por categoría; ante un bloqueo el lote para con la evidencia
- [x] T-020 criterio 1 marcado: el entrenamiento usa el motor de captura común

## Resultado

Captura por lotes del catálogo de entrenamiento (bin/train capture, ritmo B, primera carga sin scroll, reservas, registro reanudable): piloto ECI 30/30 sin bloqueos

## Notas

- 2026-10-25 Decisión del usuario (2026-10-25): ritmo B y sin la técnica del scroll; se entra y se guarda el HTML de la primera carga (DOM tras la carga, sin desplazamiento ni permanencia; response.html.gz se conserva igual). El desplazamiento está fijo en capture/visit.py (_visit → scroll_through): hace falta una opción de visita (p. ej. scroll: false en el ritmo) que por defecto siga desplazando para el MPIR y taxo page fetch. Estimación: ~25 s por ficha, unas 2–2,5 h para 300.
- 2026-10-25 bin/train capture SELECTION [--pilot] [--max N] [--ignore-hours] [--status] (src/demand_engine/demand/collect.py sobre crawl/SiteRun; registro reanudable var/training/eci/capture-*.jsonl; reservas ante gone/disallowed/reserved). Pacing con scroll (por defecto true; false = primera carga, acción first_load). pages.freeze compartido con taxo page fetch. Ritmo B en eci.spec.json. 67 pruebas en verde (e2e con Chrome: primera carga y reserva).
- 2026-10-25 Arranque escalonado (el usuario eligió saltar el horario: 22:50): 5/5 capturadas sin bloqueo. La primera carga trae precio, descripción, características, ingredientes y alérgenos, operador, EAN y envíos (mermelada Tiptree); material, aptitudes, piezas (sopera Rosenthal). JSON-LD pobre (nombre, marca, color): lo útil está en el HTML.
- 2026-10-25 Piloto 30/30 capturado (22:50–23:15, fuera de horario por decisión del usuario), sin bloqueos ni reservas usadas; ~25 s por ficha. Todas las fichas traen precio y su bloque de características (en moda, «Composición»: material exterior e interior, suela). Registro: demand-engine/var/training/eci/capture-eci-2026-10-25.jsonl.
