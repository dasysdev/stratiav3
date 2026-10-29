# La auditoría se elige sobre el resultado del rastreo; sin lista, todas las fichas del universo

Fecha: 2026-10-29. Origen: conversación con el usuario (tarea T-083).

## Petición

- Claude preguntó cómo se relaciona `pages audit` con el rastreo de la araña. Propuso tres opciones: sobre el rastreo, la selección en un fichero aparte del manifiesto, o dos modos.
- Usuario: «opcion 1, sobre el rastreo. eso de "solo pide aparte lo no rastreado" no tiene sentido. la auditoria solo se hace sobre el resultado del rastreo».
- Claude preguntó qué fichas audita `pages audit` sin lista de fichas del encargo. Usuario: «Todas las del universo».

## Cambio

1. **Sobre el rastreo:** las páginas de una auditoría (D-167) se eligen sobre el resultado del rastreo, con la instantánea de su visita. La auditoría no pide nada al sitio. Una página de D-167 que el rastreo no capturó se registra y no se audita.
2. **Fichas sin lista del encargo:** si el encargo no da la lista de fichas, se auditan todas las fichas del universo. Enmienda D-167 (ítem «Fichas de producto»).

## Lecturas de Claude al construirlo (capture, T-083)

- El rastreo lee los sitemaps una vez, después de la portada. Cuando no queda nada que rastrear, captura una vez cada URL de los sitemaps que no alcanzó, aunque lleve parámetros. Registra sus enlaces y no los sigue.
- Una URL de los sitemaps que es la URL, la URL final o la URL canónica de una página del rastreo es esa página.
- El universo lista cada URL una vez, con:
  - alcanzada: sí; no, solo si el rastreo terminó completo; si no, indeterminada;
  - en los sitemaps: sí, por su URL, su URL final o su URL canónica; no, solo si la lectura de los sitemaps fue completa; si no, indeterminada;
  - tipo de página, por varias señales, no solo el marcado: portada (la URL de inicio); política (localizada en la portada); ficha (señales de ficha en el documento y forma de URL de ficha); categoría (en las migas de una ficha o con su forma, también su paginación; lista URL con forma de ficha y no tiene señales de ficha); otra (ninguna de esas señales). Lo dudoso queda sin tipo, y también lo no capturado, lo que no es HTML y lo de otro host.
- Las categorías auditadas son todas las del universo, sin su paginación, y la inmediata de cada ficha.
- Una ficha del encargo fuera del universo no se audita. Se registra como no alcanzada solo si el rastreo terminó completo.
- Un rastreo parado por una reserva TDM no se audita (D-171).

## Contexto

- Medida en burritoblanco, 40 URL: 6 sitemaps leídos completos, 791 URL; universo de 957 URL; 1 portada, 3 políticas, 29 fichas, 6 categorías (una y su paginación) y 1 otra; `pages audit` eligió 34 páginas.
- Fuera de `docs/`: capture (`crawl.json` con el universo; `audit.json` con las páginas elegidas) y T-084 (web-audit sobre esa auditoría).
