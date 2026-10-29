---
id: T-080
title: Descubrimiento de las páginas de una auditoría y reserva TDM en el canon
status: hecha
depends:
milestone:
created: 2026-10-29
closed: 2026-10-29
---

## Objetivo

Registrar en el canon con /docs-update dos decisiones. 1) Las páginas de una auditoría se descubren por la unión del rastreo y los sitemaps. El rastreo sigue los enlaces <a href> del documento sin JavaScript y solo sirve para descubrir. Lo que queda fuera se considera no rastreable. El único requisito que se valora es el del sitemap (D-162), en cada página auditada. Enmienda D-167: las fichas auditadas salen del universo descubierto. 2) En la auditoría, la reserva TDM se comprueba antes de capturar; si la hay, el proceso para y avisa. Enmienda D-042 solo para la auditoría.

## Criterios de aceptación

- [x] decisions.md registra las dos decisiones con las palabras del usuario y enmienda D-167 y D-042
- [x] evaluation-scopes y los demás módulos afectados recogen el descubrimiento y la parada por reserva; D-162 se mantiene: los enlaces no se auditan
- [x] Glosario y changelog actualizados; python3 tools/check_docs.py sin errores

## Resultado

D-170 (universo de la auditoría: rastreo ∪ sitemaps; los enlaces solo descubren) y D-171 (reserva TDM en la auditoría: comprobar, parar y avisar); evaluation-scopes 2.5

## Notas

- 2026-10-29 Palabras del usuario (2026-10-29): «Realmente no busco auditar rastreo profundamente. Solo un motor de descubrimiento de URLS», «en la auditoria no valoramos cuestiones de los enlaces y su rastreabilidad. Simplemente los usamos como medio de descubrimiento», «Esto me sirve para detectar urls que no estan en el sitemaps», «el universo es la union sitemaps con rastreo. lo que queda fuera se considera irrastreable», «el objetivo es descubrir el recurso de un modo u otro. El unico requisito que valoramos es el del sitemaps». Reserva TDM: «analizar si hay reserva antes de empezar cualquier proceso de captura. si lo hay, paramos y el sistema notifica», y después «solo audit». Aceptado: araña propia en capture (no Screaming Frog como motor); enlace = <a href> del documento sin JS, nofollow se sigue y se registra; requisito del sitemap en cada página auditada y fichas auditadas tomadas del universo; ~1 página/s, tope 50.000 URL, sin horario. Una ausencia exige cobertura (invariante 11): in_sitemaps sigue con undetermined.
- 2026-10-29 Revisión independiente (docs-reviewer) aplicada: Decisión de D-170 literal («Fichas auditadas: salen del universo descubierto») y lecturas de Claude marcadas (el encargo elige entre las del universo; instantánea de la visita del rastreo; páginas de D-167 sobre lo capturado); D-150 y D-042 anotadas como enmendadas por D-171 en la auditoría; OQ-85 anotada; triaje completo (w-document/005, w-consumer/007 y 008). Pendiente editorial sin abrir: evaluation-scopes supera las 250 líneas (~272; ya tenía 257).
