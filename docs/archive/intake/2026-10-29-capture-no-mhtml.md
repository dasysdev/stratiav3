# El motor de captura deja de guardar el MHTML

Fecha: 2026-10-29. Origen: conversación con el usuario (tareas T-082 y T-085).

## Cambio

El motor de captura deja de guardar el MHTML (`page.mhtml.gz`) en todos los perfiles.

## Contexto

- Usuario: «quita MHTML no hace falta para el perfil de audit-es». Después: «para los demás perfiles, con html solo no basta?».
- Claude comprobó que ningún proceso lee el MHTML del motor: el entrenamiento y `/demand-model` leen `dom.html`; PAA, el DOM; web-audit, `response.html`; el MPIR, aparcado por D-095, no lo lee. `mpir ingest` acepta `.mhtml` guardados a mano, que no salen del motor.
- Claude recomendó quitarlo de todos los perfiles y enmendar el método del MPIR (`sampling-capture`: «el motor de captura guarda en una sola visita el HTML de la respuesta, el DOM renderizado y el MHTML»). Usuario: «hazlo».
- Medida: burritoblanco, 10 páginas con audit-es: 1,0 MB sin MHTML frente a 6,8 MB con él. El MHTML de la portada lleva 38 imágenes y 15 CSS.
- Argumento: el MHTML solo aporta el aspecto (imágenes y CSS). D-042 ya descartó las capturas de pantalla para no juzgar por la prominencia.

## Consecuencias

- Si se retoma el MPIR y necesita el aspecto de la página, se reintroduce con una decisión nueva.
- Las instantáneas existentes no se tocan.
- Fuera de `docs/`: capture retira el MHTML del motor.
