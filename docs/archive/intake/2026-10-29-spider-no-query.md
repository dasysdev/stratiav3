# La araña de la auditoría no rastrea URL con parámetros

Fecha: 2026-10-29. Origen: conversación con el usuario (tarea T-082).

## Cambio

- **Rastreo:** la araña solo rastrea URL sin parámetros (query). Los enlaces con parámetros no se siguen; se cuentan.
- Enmienda D-170 («sigue los enlaces `<a href>` del documento»), que no filtraba los enlaces.

## Contexto

- Prueba con un prototipo en burritoblanco.com (2026-10-29; `audit-es`, una página por segundo, tope de 50 visitas): ~280 enlaces por página; 1341 URL descubiertas desde 50 páginas, el 71 % con parámetros (facetas `?q=`, `?page=`). El tope de 50.000 URL se agotaría en facetas.
- Usuario: «sin facetas; la araña solo rastrea URL sin parámetros (query)».
- Segunda prueba, sin parámetros: 1298 enlaces con parámetros descartados; 392 URL descubiertas desde 50 páginas.

## Lecturas de Claude al construir la araña (capture, T-082)

- Solo sigue enlaces `http` y `https` del host de la URL de inicio y del host final de la portada (`x.es` → `www.x.es`).
- No sigue los enlaces a recursos que no son páginas, por su extensión (PDF, imágenes, vídeo, ficheros, CSS, JS).
- Recorre el sitio en anchura, en el orden de descubrimiento.
- Un bloqueo para el rastreo (política del motor, D-042).
- La cobertura del rastreo queda incompleta por el tope, un bloqueo, una reserva TDM, una interrupción o páginas con error cuyos enlaces no se leyeron. Una página excluida por robots.txt o un 404 no la dejan incompleta.

## Consecuencias

- Una URL con parámetros no entra en el universo por el rastreo. Puede entrar por los sitemaps.
