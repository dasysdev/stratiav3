# Perfil de Web: fuentes y requisitos técnicos

> **Nombres** ([D-220](../../../docs/30-governance/decisions.md#d-220)): este informe conserva los nombres de su fecha. Web es hoy el ámbito Contenido, y Web Schema.org, el ámbito Marcado.

Fecha: 2026-10-28. Tarea T-072. Construido sobre el documento base del usuario, con 19 requisitos técnicos del HTML (anexo A de `docs/archive/intake/2026-10-28-web-implementation-profile.md`). Aplica el perfil de implementación de Web ([D-159](../../../docs/30-governance/decisions.md#d-159)) y su frontera técnica/informativa ([D-160](../../../docs/30-governance/decisions.md#d-160)). Las fichas y los requisitos los escribieron cuatro autores, uno por nivel y uno para los operadores de IA, y se validaron juntos.

## Resultado

| Nivel | Fichas | Citas | Requisitos (obligatorios / recomendados) |
|---|---|---|---|
| Protocolo | 2 | 32 | 3 (1 / 2) |
| Documento | 5 | 27 | 7 (7 / 0) |
| Consumidor | 12 nuevas, más `google-search-sd-policies` | 82 (sin las de sd-policies) | 12 (8 / 4) |
| **Web** | **19 nuevas** | **141** | **22 (16 / 6)** |

`web-audit/bin/reqs check`: correcto. En total hay 50 fichas y 345 requisitos: 323 de Web Schema.org y 22 de Web.

**Triaje posterior** ([triaje Web](2026-10-28-triaje-web.md), T-073): se quedan 12 (10 obligatorios, 2 recomendados). No se auditan la conformidad formal sin efecto en la lectura, el rastreo del sitio ni lo redundante: `w-protocol/001`–`003`, `w-document/002`, `003`, `005`–`007` y `w-consumer/007`, `008`. Las tablas de abajo describen la pasada antes del triaje.

Fuentes nuevas: las 19 son especificaciones aplicables del perfil de Web, registradas en `references/sources.json` y congeladas el 2026-10-28.
- **Protocolo:** RFC 9110 y RFC 9309.
- **Documento:** HTML (syntax, parsing, semantics y links) y Encoding.
- **Consumidor:**
  - Google Search: Search Essentials, enlaces, robots.txt, meta robots, `noindex`, códigos de estado, redirecciones, tipos indexables y JavaScript;
  - operadores de IA: OpenAI, Anthropic y Perplexity.

## Reparto de los 19 RT del documento base

| RT | Requisitos | Nota |
|---|---|---|
| 01 · Direccionabilidad | — | Google solo dice «Don't use fragments», sin must ni should. |
| 02 · Accesibilidad automatizada | `w-consumer/001` | Un desafío a nuestro navegador es NE. |
| 03 · Respuesta HTTP satisfactoria | `w-consumer/002` | |
| 04 · Redirecciones | `w-protocol/001` | El «SHOULD» de los bucles es del cliente; la página de redirecciones de Google no fija nada sobre la cadena. |
| 05 · Correspondencia de la respuesta | `w-consumer/003` | Soft 404. |
| 06 · Condiciones de solicitud | — | Es el perfil de consumo (D-157). |
| 07 · Tipo de contenido | `w-protocol/002`, `w-consumer/004` | |
| 08 · Integridad y decodificación | `w-protocol/003` | Que se transmita «íntegramente» no lo fija ninguna fuente del perfil. |
| 09 · Codificación de caracteres | `w-document/001`–`004` | El 004 (codificación real) no estaba en el reparto. Sale del «declara y utiliza» del RT y de un must distinto. |
| 10 · Interpretabilidad estructural | — | Condición previa: un analizador conforme siempre da un DOM. |
| 11 · Representación recuperable | `w-consumer/005` | Contenido textual. Que sea la información comercial es informativo (D-160). |
| 12, 13, 14 · JavaScript, recursos dependientes, interacción | — | Se siguen del perfil sin JavaScript (D-156). |
| 15 · Marcado Schema.org | `w-consumer/006` | Es la misma condición que `ws-consumer/177`, sobre `response.html`. |
| 16 · Enlaces | `w-document/005`, `w-consumer/007`, `008` | El 008 (sin `href` `javascript:`) no estaba en el reparto. Lo fija el «Not recommended» de la guía de enlaces. |
| 17 · robots.txt | `w-consumer/009` (Googlebot), `011` (OAI-SearchBot), `012` (PerplexityBot) | Anthropic no fija requisito. |
| 18 · Directivas de indexación | `w-consumer/010` | `nofollow` no bloquea la indexación: ninguna fuente lo prohíbe. |
| 19 · Conformidad ampliada | `w-document/006`, `007` | DOCTYPE en su sitio y con su forma. **«Sin errores de análisis» no da requisito**: los must de los errores de análisis son de los validadores y del analizador («Conformance checkers must report…»), no del documento. |

**Diferencias con el reparto aprobado:**
- Del RT-19 se quedó fuera la mitad sin errores de análisis.
- Del RT-09 salen cuatro requisitos en lugar de tres.
- Se añaden el `w-document/007` y el `w-consumer/008`.

Todos se apoyan en texto con must, should o recommend, y los decidieron los agentes con cita (D-133).

## Formato y validador

- **Ámbito `Web`:** tres ficheros (`web-protocol.json`, `web-document.json`, `web-consumer.json`) e ids `w-<nivel>/NNN` (`FILES` en `reqs.py`).
- **`scopes` en las fichas:** cada ficha de especificación aplicable dice de qué perfiles es, porque «consumidor» es nivel de los dos. Las 23 fichas de Web Schema.org llevan `["Web Schema.org"]`, y `google-search-sd-policies` lleva los dos ámbitos.
- **«requirement(s)»** cuenta como término de lo obligatorio, por Search Essentials («minimum technical requirements»).
- **Preámbulo:** la sección `#` es el texto antes del primer encabezado (`references.read`). Sin ella no se podía citar la recomendación de OpenAI y Perplexity, cuya página no tiene encabezados en la raíz del contenido.
- **Método común de Web** (README): la respuesta HTTP sin JavaScript, los límites de los bytes del cuerpo y robots.txt según RFC 9309.

## Qué es NE hoy

Depende de lo que guarda capture (nota en T-069):

- **Bytes originales:** `response.html` es el cuerpo ya decodificado por Chrome y pasado a UTF-8.
  - `w-document/004` (codificación real) es siempre NE.
  - `w-protocol/003` nunca sale no satisfecho: un cuerpo ilegible es NE.
  - `w-document/003` mide la posición en el cuerpo guardado, con un margen: entre los bytes 1022 y 1024 es NE.
- **robots.txt** (`w-consumer/009`, `011` y `012`): solo lo conservan las capturas sueltas, con `robots.txt` y `legitimacy` en `meta.json`. Las fichas del entrenamiento no lo tienen. El registro por bot es de T-069.
- **Cabeceras de los saltos:** capture guarda de cada salto la URL, el estado y el destino. `w-protocol/001` deduce `Location` de que Chrome siguió el salto, y `002` solo mira la respuesta final.
- **Googlebot:** nuestro navegador no es Googlebot (D-157), así que un bloqueo del WAF a Googlebot no se puede comprobar.

## Pendiente

- **Candidatos con must o should que no estaban en el reparto** (sin escribir):
  - **Protocolo:** que `Location` sea una referencia URI válida; una sola línea de `Content-Type` y de `Location`; `identity` en `Content-Encoding` (SHOULD NOT).
  - **Documento:** una sola declaración `meta` de codificación; no combinar `charset` con `http-equiv`; sin referencias de carácter en la declaración.
  - **Consumidor:** la forma del propio robots.txt (ubicación, UTF-8, ruta con `/`), la fecha de `unavailable_after` y el HTML válido con `data-nosnippet`.
- **Errores de análisis:** si se quieren, habría que escribir reglas sueltas de la sintaxis (13.1) que un validador detecta, como atributos duplicados o contenido tras `</html>`. Un requisito agregado no se puede escribir: el must sería el del validador.
- **Criterios operativos para revisar:**
  - `w-consumer/001`: qué es una página de inicio de sesión (contenido principal con un formulario de contraseña).
  - `w-consumer/005`: que un «activa JavaScript» o un «Cargando…» no cuenta como contenido.
- **URL válida** (`w-document/005`): el URL Standard no está registrado. El método aproxima «valid URL string» como «el analizador de URL no da errores de validación».
- **Límite de 2 MB de Googlebot:** la página de Googlebot lo da como hecho, sin must ni should. No está registrada.
- **Mínimo de representación de Web:** [OQ-84](../../../docs/30-governance/open-questions.md#f-evaluación-técnica).
