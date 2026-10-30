# Vistas de la evaluación técnica y sitemaps

> **Nombres** ([D-220](../../../docs/30-governance/decisions.md#d-220)): este informe conserva los nombres de su fecha. Web es hoy el ámbito Contenido, y Web Schema.org, el ámbito Marcado.

Fecha: 2026-10-28. Tarea T-074. Aplica [D-161](../../../docs/30-governance/decisions.md#d-161) (vista general y vista particular; tipos de página) y [D-162](../../../docs/30-governance/decisions.md#d-162) (toda página auditada está en los sitemaps, condición del proyecto).

## Resultado

| | Web Schema.org | Web | Total |
|---|---|---|---|
| Vista general | 84 | 10 | 94 |
| Vista particular | 239 | 13 | 252 |
| **Requisitos** | **323** | **23** | **346** |

`web-audit/bin/reqs check`: correcto. Web pasa de 12 a 23 requisitos (21 obligatorios, 2 recomendados).

## Vista y tipos de página de los requisitos que había

Se asignan por especificación:

| Requisitos | Vista | Tipos de página |
|---|---|---|
| Organization, política de devoluciones y política de envío de Google (Web Schema.org) | general | — |
| Fichas de comerciante, fragmentos de producto, variantes y reseñas de Google (Web Schema.org) | particular | ficha de producto |
| Presencia del marcado (`ws-consumer/177`, `w-consumer/006`) | particular | ficha de producto |
| Serialización, vocabulario y el resto de las directrices generales de datos estructurados (Web Schema.org) | particular | todos |
| Acceso y lectura, robots.txt y `noindex` (Web) | particular | todos |

Son lecturas de Claude, revisables. Las más discutibles:
- que la presencia del marcado solo se exija en la ficha de producto;
- que la política de devoluciones y la de envío de nivel de organización sean generales, aunque la Offer también lleve las suyas, que son particulares (fichas de comerciante).

## Sitemaps

**Fuentes nuevas:**
- `sitemaps-org-protocol` (protocolo, 17 citas);
- `google-search-sitemaps-build` (consumidor, 4 citas; repite el protocolo y no da requisitos propios);
- `google-search-sitemaps-overview` (consumidor, 2 citas; no exige ni recomienda tener un sitemap).

**Requisitos de la vista general,** sobre los sitemaps que publica el sitio (método común de Web, punto 5):

| Id | Condición |
|---|---|
| `w-protocol/004` | Elemento raíz `urlset` o `sitemapindex` |
| `005` | UTF-8 |
| `006` | Cada entrada `url` o `sitemap` tiene `loc` |
| `007` | Cada `loc` es una URL absoluta |
| `008` | Cada `loc` tiene menos de 2048 caracteres |
| `009` | Cada URL es válida para la ubicación del sitemap (protocolo, host, directorio o declaración en robots.txt) |
| `010` | Como mucho 50.000 entradas |
| `011` | Como mucho 50 MB sin comprimir |
| `012` | Sin `&` ni `<` sin escapar |
| `w-consumer/013` | Cada línea `sitemap:` de robots.txt lleva una URL absoluta |

Todos son obligatorios y todos son de forma. Con el criterio del triaje de Web quedan fuera:
- el escape de `'`, `"` y `>`, que no impide leer el XML;
- `lastmod` y `changefreq`;
- la ubicación en la raíz y el índice cuando hay varios sitemaps, que no impiden el descubrimiento;
- los mismos límites repetidos por Google, por redundantes.

**Condición del proyecto:**
- `w-consumer/014`: la URL de la página está en un sitemap del sitio.
- Vista particular, todos los tipos de página, obligatorio.
- Lleva `decision: D-162` en lugar de `spec`.
- Sin sitemap no se satisface.

## Formato y validador

- **`view`** (`general` o `particular`) en todos los requisitos y **`page_types`** en los particulares, con los tipos del canon.
- **`decision`** en lugar de `spec` para una condición del proyecto. La decisión ha de existir en `decisions.md`, y la naturaleza no se comprueba en las citas.
- **Resumen** de `reqs check`: requisitos por vista.
- **Método común de Web:** puntos 5 (sitemaps) y 6 (vistas).

## Qué es NE hoy

- **Sitemaps:** capture no congela robots.txt ni los sitemaps de una auditoría, así que los requisitos de sitemap y `w-consumer/014` son NE. Los sitemaps grandes (El Corte Inglés tiene millones de URL, repartidas en índices) exigen buscar la URL leyendo todos los ficheros o muchos de ellos. Va con [OQ-85](../../../docs/30-governance/open-questions.md#f-evaluación-técnica), que decide también qué páginas de cada tipo se auditan.
- **Páginas de otros tipos:** hoy solo hay fichas de producto congeladas. Los requisitos particulares de categoría, políticas y portada esperan a OQ-85.
