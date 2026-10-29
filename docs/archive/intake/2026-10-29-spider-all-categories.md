# La auditoría busca todas las categorías; la araña va categoría a categoría

Fecha: 2026-10-29. Origen: conversación con el usuario (tarea T-093).

## Petición

- Usuario: «la prioridad son las fichas de producto, pero las categorías y las otras páginas de contenido que hemos definido como relevantes para la audit tb deben encontrarse».
- Después: «hay un cambio de canon que debe aplicar un cambio en la araña. Buscamos todas las categorías no solo las inmediatas de cada producto».
- Claude propuso alternar fichas y categorías. Usuario: «no hace falta que hagas esa alternancia. ve por categoría obteniendo las urls de las fichas de forma paginada y luego saltando a otra categoría y así sucesivamente».
- Claude preguntó cuándo capturar las fichas reunidas. Usuario: «al terminar cada categoría».

## Cambio

1. **Categorías de la auditoría:** todas las categorías del sitio, no solo la inmediata de cada ficha. Enmienda D-167 (ítem «Categoría o listado»).
2. **Orden de la araña:** primero las políticas de D-167, localizadas desde la portada. Después, categoría a categoría: la categoría, toda su paginación y las fichas que listan sus páginas; luego, la siguiente categoría. Enmienda D-204.

## Lecturas de Claude al construir la araña (capture, T-093)

- Una categoría es un enlace de las migas de una ficha, a cualquier nivel, y cualquier URL con la forma de URL de esas categorías.
- La paginación de una categoría sigue mientras la página lista fichas.
- Una categoría capturada antes de saberse que lo era se recorre igual, sin volver a pedirla.
- Después de las categorías: las fichas halladas en otras páginas, las formas de URL aún no capturadas y el resto.

## Contexto

- Medida en burritoblanco, 60 URL: la portada, 3 políticas, la categoría «lo más nuevo» con sus 5 páginas y 49 fichas.
- `pages audit` (capture) sigue con la categoría inmediata hasta T-083.
