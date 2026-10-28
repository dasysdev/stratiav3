# Cómo cumple la captura el perfil de consumo: sin JavaScript y con un contexto nuevo por ficha

Decisión del usuario del 2026-10-28, tomada en la sesión de la tarea T-069 (perfiles de captura en capture), que cierra OQ-80 y precisa D-157. Recogida por Claude el mismo día.

## OQ-80 · Cómo cumple el motor «navegador real que no ejecuta JavaScript»

Alternativas que propuso Claude:

| Vía | Qué hace | Coste |
|---|---|---|
| A | Desactivar JavaScript en Chrome, por ventana. Se lee lo que recibe un navegador real que no ejecuta JavaScript; `<noscript>` es marcado. | No se pasa un desafío que exige JavaScript: queda como incidencia. |
| B | Cargar con JavaScript y leer la respuesta HTTP (`response.html`). | Pasa desafíos, pero una navegación, una recarga o las cookies hechas por JavaScript cambian sin rastro el documento leído: deja de ser un navegador que no ejecuta JavaScript. |
| C | Híbrido: A y, solo ante un desafío, otro intento con JavaScript únicamente para que se resuelva solo, y recarga sin JavaScript; la ficha lo registra. | Más código; el estado deja de ser del todo limpio (cookie del desafío). |

Recomendación de Claude: A; medir la tasa de desafíos en un lote de prueba; añadir C solo si los datos lo piden.

Respuesta del usuario: «A, y C si hace falta».

Datos medidos (lote de 22 portadas de tiendas españolas, una visita por perfil, 2026-10-28): con el perfil de auditoría, 1 desafío de 22 (Fnac: DataDome, 403 con CAPTCHA en la primera respuesta, antes de que pudiera ejecutarse JavaScript; C no lo resolvería); con el perfil de lectura del motor (Chrome persistente con JavaScript), 0 de 22. Con estos datos, C no se adopta.

## Estado limpio por ficha

D-157 dice «antes de cada captura se borran las cookies y el almacenamiento del dominio». Claude propuso cumplirlo con un **contexto de navegador nuevo por ficha**, desechado al terminar: sin cookies, almacenamiento ni caché de ningún sitio y sin ningún consentimiento heredado. Es más estricto que borrar un dominio y no toca el perfil persistente que usan otras capturas. Riesgo: algún antibot detecta contextos de tipo incógnito; se ve en la tasa de desafíos.

Respuesta del usuario: contexto desechable.

## IP de origen

Claude preguntó qué hacer si la IP de origen no es española o no se puede comprobar. Respuesta del usuario: «ignora lo de la ip. no hace falta que lo tengas en cuenta».

## Fuera de docs/ (hecho en T-069)

capture tiene perfiles de captura con nombre, que elige quien captura: el de siempre, por defecto, y el del perfil de consumo de la auditoría (D-156, D-157). La ficha congelada registra el perfil usado; el de auditoría registra también `Accept-Language`, la IP de origen con su país y su ASN, robots.txt por bot, los bytes originales del cuerpo y las cabeceras de cada salto de redirección (D-159). Detalle en `capture/README.md`.
