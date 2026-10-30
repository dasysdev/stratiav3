# Triaje de los requisitos técnicos de Web

> **Nombres** ([D-220](../../../docs/30-governance/decisions.md#d-220)): este informe conserva los nombres de su fecha. Web es hoy el ámbito Contenido, y Web Schema.org, el ámbito Marcado.

Fecha: 2026-10-28. Tarea T-073. El usuario pidió revisar los 22 requisitos del [perfil de Web](2026-10-28-perfil-web.md) «teniendo en cuenta el scope de esta auditoría». Claude propuso un criterio y cinco bloques, y el usuario aceptó retirar los bloques 3, 4 y 5 y mantener el 2.

## Criterio

Un requisito de Web se queda si su incumplimiento puede impedir **obtener o leer la información de la página** con el perfil de consumo, o **el acceso de los sistemas que la consumen**. Se apoya en el canon:
- se audita «la información publicada, sus representaciones y las condiciones técnicas de su exposición», sin la infraestructura completa ([scope](../../../docs/00-context/scope.md));
- la política de acceso de los sistemas automatizados se revisa de forma auxiliar, sin que sea «una auditoría integral del rastreo» ([evaluation-scopes](../../../docs/10-model/evaluation-scopes.md#perfil-de-consumo-no-interactivo)).

La unidad es la ficha de producto, que llega por su URL.

## Resultado

| Decisión | Requisitos |
|---|---|
| Se quedan | 12 (10 obligatorios, 2 recomendados) |
| No se auditan | 10 |
| **Total** | **22** |

Los 10 están en [retired.json](../retired.json) con el motivo `no se audita` y la decisión `triaje Web 2026-10-28`. Sus citas se conservan y sus ids no se reutilizan.

## Se quedan

| Bloque | Requisitos |
|---|---|
| 1 · Acceso y lectura de la página | `w-consumer/001` (sin inicio de sesión), `002` (200), `003` (no es página de error), `004` (tipo de texto), `005` (contenido textual), `006` (marcado presente); `w-document/001` (codificación declarada), `004` (UTF-8 real, NE hasta T-069) |
| 2 · Política de acceso de los bots | `w-consumer/009` (Googlebot), `010` (`noindex`), `011` (OAI-SearchBot), `012` (PerplexityBot) |

## No se auditan

| Bloque | Por qué | Ids |
|---|---|---|
| 3 · Conformidad formal sin efecto en la lectura (4) | Los decodificadores aceptan también la etiqueta `utf8`. La posición de la declaración solo importa sin `charset` ni BOM. El DOCTYPE cambia el modo de renderizado, no el contenido. | `w-document/002`, `003`, `006`, `007` |
| 4 · Rastreo del sitio (3) | Sirven para descubrir otras páginas, no para leer la que se audita. | `w-document/005`, `w-consumer/007`, `008` |
| 5 · Redundantes o que no pueden fallar con nuestra evidencia (3) | Sin `Location` la redirección no se sigue y ya falla `w-consumer/002`. Sin `Content-Type` Chrome deduce el tipo, y el tipo lo mira `w-consumer/004`. `Content-Encoding` nunca sale incumplido con lo que guarda capture. | `w-protocol/001`, `002`, `003` |

**Efecto en el perfil:** el nivel protocolo se queda sin requisitos. RFC 9110 y RFC 9309 siguen con su ficha: el RFC 9309 sirve al método de robots.txt, y el RFC 9110 al de la respuesta. El perfil de D-159 no cambia: el triaje decide qué se audita de él, como el de Web Schema.org.

**Para las pasadas siguientes:** los candidatos sin escribir del [informe del perfil](2026-10-28-perfil-web.md#pendiente) se juzgan con este criterio. Por eso quedan fuera la forma de `Location`, la unicidad de `Content-Type` y de la declaración `meta`, y la forma del propio robots.txt.
