# La araña de la auditoría captura primero las fichas y sigue la paginación

Fecha: 2026-10-29. Origen: conversación con el usuario (tarea T-088).

## Petición

Usuario: «para la araña. prioriza la captura de productos. Optimiza la estrategia para capturar productos».

## Cambio

Claude propuso alternativas y el usuario eligió:

1. **Prioridad de fichas, aprendida en el rastreo** (sin configuración por sitio). La araña confirma una ficha por las señales de su documento: `og:type` `product`, o `Product` en JSON-LD o microdatos. Da prioridad a las URL con la forma de URL de las fichas confirmadas. Después visita los listados que más fichas descubren. Sustituye la lectura «recorrido en anchura» de D-173.
2. **Paginación:** «admitir solo paginación». La araña sigue una URL cuyo único parámetro es de paginación y tiene valor numérico (`page`, `p`, `pag`, `pagina`, `pg`). Las facetas (`?q=`, filtros) siguen fuera. Enmienda D-173.

## Contexto

- Con D-173, una ficha que solo aparece en la página 2 o siguientes de su categoría quedaba fuera del rastreo. Se registraría como no rastreable, aunque el sitio la enlaza.
- burritoblanco, recorrido en anchura: tras 20 páginas, la primera ficha estaba en la posición 65 de la cola. Con la prioridad: 35 fichas en las primeras 40 URL.
- El orden solo importa si el rastreo se corta. Un rastreo completo alcanza las mismas páginas.
- Las señales de ficha de la araña sirven para ordenar. No son la clasificación del tipo de página del universo (T-083).
