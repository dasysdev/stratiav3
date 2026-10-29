# Descubrimiento de las páginas de una auditoría y reserva TDM en la auditoría

Decisiones del usuario del 2026-10-29 (tarea T-080), sobre la propuesta de Claude de un motor de rastreo para la auditoría. El usuario eligió y precisó en tres respuestas sucesivas.

## 1. Descubrimiento de las páginas de una auditoría

Punto de partida del usuario: «para la auditoria necesitamos descubrir todas las urls de productos (y de otras paginas de contenido especificas). No me quiero basar en el sitemaps porque eso me impide poder valorar el requisito de que el recurso este presente en el sitemaps».

Claude propuso dos alternativas: Screaming Frog SEO Spider como motor (A) o una araña propia en capture, con Screaming Frog como modelo (B). Usuario: «ok a B».

Palabras del usuario sobre el alcance:

- «Realmente no busco auditar rastreo profundamente. Solo un motor de descubrimiento de URLS.»
- «en la auditoria no valoramos cuestiones de los enlaces y su rastreabilidad. Simplemente los usamos como medio de descubrimiento.»
- «Esto me sirve para detectar urls que no estan en el sitemaps. Si es acertado lo que dices que el universo es la union sitemaps con rastreo. lo que queda fuera se considera irrastreable.»
- «el objetivo es descubrir el recurso de un modo u otro. El unico requisito que valoramos es el del sitemaps.»
- «si el rastreo usa el mismo perfil de captura. Aprovecha el mismo proceso para ambas cosas. descubrir + capturar»

Decisiones:

- **Universo de la auditoría:** las páginas de una auditoría se descubren por la unión del rastreo del sitio y de sus sitemaps.
- **Rastreo:** parte de la portada y sigue los enlaces `<a href>` del documento de la respuesta HTTP sin ejecutar JavaScript. Los enlaces `nofollow` se siguen y se registran. (Propuesta de Claude; usuario: «OK».)
- **Los enlaces solo descubren:** no se valoran ni se auditan los enlaces ni la rastreabilidad.
- **Fuera del universo:** lo que no se descubre se considera no rastreable.
- **Único requisito que se valora:** que la página esté en los sitemaps (D-162), en cada página auditada. (Lectura de Claude; usuario: «ok».)
- **Fichas auditadas:** salen del universo descubierto. (Lectura de Claude; usuario: «ok».)
- **Un solo proceso:** el rastreo usa el perfil de auditoría y captura cada página en la misma visita que la descubre.

## 2. Reserva TDM en la auditoría

Claude explicó la reserva de minería de textos y datos (art. 67.3 TRLPI; `tdmrep.json`, cabecera y meta `tdm-reservation`) y que hoy el motor, ante una reserva, no conserva el contenido de esa página (D-042).

Usuario: «analizar si hay reserva antes de empezar cualquier proceso de captura. si lo hay, paramos y el sistema notifica.» Claude preguntó si vale para todos los procesos o solo para la auditoría. Usuario: «solo audit».

Decisiones:

- Antes de capturar ninguna página de una auditoría, se comprueba si el sitio tiene reserva de minería de textos y datos.
- Si la hay, no se captura nada: el proceso para y avisa.
- Solo en la auditoría. Los demás procesos de captura siguen como fija D-042.

## Fuera de `docs/` (operación, para las tareas T-081 a T-085)

- Motor: araña propia en capture. Screaming Frog (versión gratuita) solo como contraste en el piloto.
- Ritmo: 1 página/s como máximo, o el `Crawl-delay` si es mayor. Tope de 50.000 URL. Sin horario. Usuario: «ok a lo que propones».
- Perfil `audit-es`: consulta el origen (RIPEstat) una vez por ejecución (usuario: «ok»). El resto del perfil no cambia de momento (usuario: «dejalo asi de momento»).
