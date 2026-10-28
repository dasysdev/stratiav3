# Perfil de implementación de Web

Decisión del usuario del 2026-10-28, tomada en sesión (T-072). La recoge Claude el mismo día.

## Contexto

El usuario pidió: «utiliza este doc como base de referencia para construir los requisitos técnicos para todo el recurso web», con el documento `tmp/requisitos_tecnicos_html.md` (anexo A, literal): 19 requisitos técnicos (RT-HTML-01…14, RT-WEB-15…19) en cinco bloques: publicación y acceso; formato y codificación; lectura y consumo automatizado; Schema.org en Web; y adicionales condicionados.

El canon no tenía perfil de implementación de Web: solo el de Web Schema.org ([D-130](../30-governance/decisions.md#d-130)); el de Web seguía en OQ-30. Según D-133, el usuario fija el perfil y los agentes escriben los requisitos. Claude comprobó en origen el texto de las fuentes candidatas y propuso un perfil de tres niveles, como el de Web Schema.org, y el reparto de los 19 RT.

## 1. Perfil de implementación de Web

| Nivel | Especificaciones | Qué fijan |
|---|---|---|
| **Protocolo** | HTTP Semantics (RFC 9110) y Robots Exclusion Protocol (RFC 9309) | La respuesta (estado, redirecciones, `Content-Type`, `Content-Encoding`) y cómo se leen las reglas de robots.txt |
| **Documento** | HTML (WHATWG Living Standard: sintaxis, codificación de caracteres, enlaces y errores de análisis) y Encoding (WHATWG) | La codificación declarada y UTF-8, la sintaxis del documento y la forma de los enlaces |
| **Consumidor** | **Google Search**: requisitos técnicos de Search Essentials, enlaces rastreables, robots.txt, meta robots y `X-Robots-Tag`, bloqueo de la indexación, códigos de estado HTTP, redirecciones, tipos de fichero indexables, JavaScript y las directrices generales de datos estructurados (presencia del marcado). **Operadores de IA**: OpenAI, Anthropic y Perplexity, cada uno con su página de bots | Lo que el consumidor exige o recomienda para rastrear, indexar o recuperar la página: que su bot no esté bloqueado, un 200, contenido indexable y marcado |

- Como en Web Schema.org, la naturaleza la fija la especificación: un operador de IA da requisito solo donde su página dice must, should o recommend (OpenAI y Perplexity recomiendan permitir en robots.txt su bot de búsqueda; la página de Anthropic describe sus bots y no fija nada).
- El marcado Schema.org se examina en Web solo por su **presencia**; su sintaxis, estructura y conformidad son de Web Schema.org.

## 2. Reparto de los 19 RT del documento base

**Dan requisito técnico** (unos 18, de 13 RT; la cifra final sale de las versiones congeladas):

| RT | Condición | Especificación | Naturaleza |
|---|---|---|---|
| 02 | No exige iniciar sesión; un desafío a nuestro navegador es NE, no un incumplimiento | Search Essentials | obligatoria |
| 03 | La respuesta final es 200 | Search Essentials | obligatoria |
| 04 | Cada redirección lleva `Location` | RFC 9110 («SHOULD») | recomendada |
| 05 | Con 200, no es una página de error | Search Essentials | obligatoria |
| 07 | Hay `Content-Type` · el tipo es uno que Google indexa | RFC 9110 · Search Essentials | recomendada · obligatoria |
| 08 | Si se comprime, se declara `Content-Encoding` | RFC 9110 («MUST») | obligatoria |
| 09 | Se declara la codificación · es UTF-8 · la declaración está en los primeros 1024 bytes | HTML | obligatoria |
| 11 | El documento de la respuesta tiene contenido textual | Search Essentials | obligatoria |
| 15 | Hay marcado en JSON-LD, Microdata o RDFa | Directrices generales de datos estructurados de Google | obligatoria |
| 16 | Los enlaces son `<a href>` · el `href` es una URL válida | Enlaces de Google · HTML | recomendada · obligatoria |
| 17 | robots.txt no impide rastrear la URL a Googlebot · a OAI-SearchBot · a PerplexityBot | Search Essentials · OpenAI · Perplexity (y RFC 9309 para leer las reglas) | obligatoria · recomendada · recomendada |
| 18 | No hay `noindex` aplicable a Googlebot | Search Essentials | obligatoria |
| 19 | Sin errores de análisis del HTML · empieza por DOCTYPE | HTML | obligatoria |

En el RT-11, que la información **comercial** esté en el HTML no es técnico: es disponibilidad efectiva. Lo técnico es que haya contenido indexable.

**No dan requisito técnico:**

| RT | Por qué |
|---|---|
| 01 · Direccionabilidad | Google solo dice «Don't use fragments», sin must ni should; y el recurso se pide por su URL. |
| 06 · Condiciones de solicitud | Son el perfil de consumo (D-157): la condición de todas las comprobaciones, no un requisito. |
| 10 · DOM utilizable | Un analizador HTML conforme siempre da un DOM: es una condición previa (si no se obtiene el documento, NE común), no un requisito. La conformidad la recoge el 19. |
| 12 · Contenido generado con JavaScript | Con el perfil único sin JavaScript (D-156) se reduce al 11: el propio documento lo dice («Si el perfil no ejecuta JavaScript, se evalúa la representación obtenida sin esa ejecución»). |
| 13 · Recursos técnicos dependientes | Sin JavaScript, ningún recurso dependiente construye la representación del perfil: nunca se aplica. |
| 14 · Independencia de interacción | El perfil no opera la página: lo que exige interactuar no está en la respuesta y su efecto es informativo (disponibilidad efectiva). |

## 3. Frontera técnica e informativa en Web

- **Técnico:** el acceso y la recuperación del recurso, la forma de la respuesta y del documento, y la presencia de lo que el consumidor exige para la página (no bloqueado, 200, contenido indexable, marcado). Las recomendaciones del consumidor sobre el acceso y la forma (permitir un bot, enlaces `<a href>`) son técnicas: no añaden un hecho comercial.
- **Informativo:** si la información comercial pertinente está en el documento y se puede leer (disponibilidad efectiva y AC).

## 4. Lo que queda abierto

- El **mínimo de representación de Web** (D-147: «se fijarán con sus perfiles»): no se decidió en esta sesión.
- El perfil de Catálogos distribuidos y el sistema cuantitativo técnico (OQ-30).

## 5. Fuera de docs

- **Referencia técnica:** el ámbito `Web`, los niveles protocolo, documento y consumidor, un fichero por nivel (`web-protocol.json`, `web-document.json`, `web-consumer.json`) e ids `w-<nivel>/NNN`. La validación de la naturaleza acepta «requirement(s)» como término de lo obligatorio: Search Essentials dice «minimum technical requirements», no «must».
- **Capture (T-069):** guarda el cuerpo decodificado por Chrome, sin los bytes originales. Hasta que los guarde, la codificación real y el BOM son NE. robots.txt por bot está pendiente de T-069. El estado, las cabeceras y las redirecciones ya se registran.

## Respuesta del usuario

- A «¿Qué consumidores entran en el nivel consumidor del perfil de Web?»: «Google Search y operadores de IA» (la otra opción era «Solo Google Search», la recomendada por Claude).
- A «¿Apruebas el perfil de tres niveles, el reparto de los 19 RT y el plan?»: «Apruebo».

## Anexo A · Documento base (`tmp/requisitos_tecnicos_html.md`, literal)

# Requisitos técnicos del HTML

## A. Publicación, acceso y recuperación

| ID | Requisito técnico | Condición de cumplimiento |
| --- | --- | --- |
| RT-HTML-01 | Direccionabilidad del recurso | La página comercial dispone de una URL resoluble que permite solicitar directamente el recurso HTML, sin depender de haber recorrido previamente una interfaz interactiva. |
| RT-HTML-02 | Accesibilidad automatizada | El recurso puede obtenerse mediante las solicitudes automatizadas previstas, sin obstáculos obligatorios como autenticación humana, CAPTCHA o una interacción previa que impida acceder al contenido. |
| RT-HTML-03 | Respuesta HTTP satisfactoria | La recuperación del recurso termina en una respuesta HTTP de éxito adecuada para entregar el documento. Para una página comercial ordinaria, se espera normalmente 200 OK. |
| RT-HTML-04 | Resolución de redirecciones | Cuando existen redirecciones, estas pueden seguirse bajo el perfil definido y conducen al recurso comercial esperado, sin bucles, destinos erróneos ni bloqueos. |
| RT-HTML-05 | Correspondencia de la respuesta con el recurso solicitado | La respuesta obtenida entrega efectivamente el documento comercial solicitado, no una página de error, desafío de seguridad o documento sustitutivo presentado como respuesta satisfactoria. |
| RT-HTML-06 | Compatibilidad con las condiciones de solicitud | El recurso puede recuperarse en las condiciones automatizadas definidas para el estudio, considerando cuando proceda el agente de usuario, mercado, idioma y demás condiciones de acceso pertinentes. |

## B. Formato, codificación e interpretación

| ID | Requisito técnico | Condición de cumplimiento |
| --- | --- | --- |
| RT-HTML-07 | Identificación del tipo de contenido | La respuesta HTTP identifica correctamente la representación HTML mediante un tipo de contenido apropiado, normalmente text/html, sin declaraciones incompatibles que comprometan su procesamiento. |
| RT-HTML-08 | Integridad y decodificación de la respuesta | El documento se transmite íntegramente y las codificaciones de contenido utilizadas, como gzip o Brotli, pueden interpretarse correctamente mediante la información HTTP correspondiente. |
| RT-HTML-09 | Codificación de caracteres | El documento declara y utiliza una codificación coherente que permite recuperar correctamente sus caracteres. Para la conformidad con HTML actual, corresponde UTF-8. |
| RT-HTML-10 | Interpretabilidad estructural del documento | El HTML recibido puede procesarse mediante un analizador conforme al estándar y generar una estructura DOM utilizable, sin errores que impidan localizar o extraer el contenido correspondiente. |

## C. Lectura y consumo automatizado

| ID | Requisito técnico | Condición de cumplimiento |
| --- | --- | --- |
| RT-HTML-11 | Recuperabilidad de la representación comercial | El mecanismo de publicación permite obtener una representación con información comercial procesable bajo el perfil de consumo establecido, y no únicamente una estructura vacía que el consumidor no puede completar. |
| RT-HTML-12 | Compatibilidad del contenido generado mediante JavaScript | Cuando la información se genera mediante JavaScript y el perfil permite ejecutarlo, su procesamiento automático produce una representación recuperable y legible. Si el perfil no ejecuta JavaScript, se evalúa la representación obtenida sin esa ejecución. |
| RT-HTML-13 | Disponibilidad de recursos técnicos dependientes | Los scripts, respuestas de datos y demás recursos necesarios para construir la representación que permite el perfil pueden recuperarse y procesarse sin fallos que impidan obtenerla. |
| RT-HTML-14 | Independencia de interacción para el consumo | La obtención de la representación comercial prevista para el consumo automatizado no requiere clics, introducción de datos, selección interactiva de opciones u otras operaciones excluidas del perfil. |

## D. Implementación de Schema.org en Web

| ID | Requisito técnico | Condición de cumplimiento |
| --- | --- | --- |
| RT-WEB-15 | Presencia y recuperabilidad del marcado Schema.org | El recurso comercial incorpora una representación Schema.org que puede localizarse y recuperarse mediante las condiciones de consumo aplicables, cuando corresponda al perfil de implementación evaluado. |

## E. Requisitos adicionales condicionados

| ID | Requisito técnico | Condición de cumplimiento |
| --- | --- | --- |
| RT-WEB-16 | Descubribilidad mediante enlaces HTML | Las páginas comerciales pueden localizarse siguiendo enlaces automatizables, por ejemplo mediante elementos a con href resoluble. |
| RT-WEB-17 | Permisos de rastreo automatizado | Las reglas aplicables de robots.txt no impiden el acceso de los rastreadores contemplados en el perfil. |
| RT-WEB-18 | Compatibilidad con directivas de indexación | Las directivas noindex, nofollow o X-Robots-Tag no contradicen los objetivos de indexación del consumidor evaluado. |
| RT-WEB-19 | Conformidad formal ampliada con HTML | Ausencia de infracciones sintácticas o estructurales relevantes conforme al estándar HTML. |
