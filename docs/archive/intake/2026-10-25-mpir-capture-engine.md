# Motor de captura del MPIR: divergencia de renderizado, capturas de pantalla y pendientes

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad (tareas T-002 y T-013).*

## Contexto

El usuario pidió empezar a trabajar en el MPIR por la infraestructura («C. Infraestructura primero»), con ropa de cama como clase del piloto. Sobre la captura pidió: «Plantea una estrategia óptima para evitar bloqueos y a su vez suficientemente eficiente para que no tardemos una eternidad. Puedes simular ser un humano, quizás rpa, estamos desde una IP doméstica, eso puede ayudar. Si usas headless o curl ojo con el user agent». Sobre la identificación del rastreador: «lo que consideres según respuesta anterior. Esta parte es muy importante por lo que probablemente merece la atención de construir un motor de captura para MPIR».

Claude propuso un motor que usa un Chrome real, con ventana, por CDP directo, a ritmo de lector y desde la IP doméstica. Sin curl ni headless para las páginas, porque la incoherencia entre capas es lo que más bloqueos provoca. Respetando robots.txt y las reservas de minería de textos y datos. Y parando ante cualquier desafío, sin resolver CAPTCHAs, rotar IP ni aplicar parches antidetección. El usuario respondió: «no hace falta captura de pantalla. Implementa el motor». El motor se implementó en `mpir/` (T-013).

## Hechos que registrar

1. **Divergencia (registrar, no resolver).** `20-methods/mpir/sampling-capture.md` («Contenido dinámico e interacción selectiva») dice que el renderizado con navegador automatizado «se empleará selectivamente para evitar coste y complejidad innecesarios». El motor, con la aprobación del usuario, renderiza siempre con Chrome real por CDP, por dos motivos:
   - la incoherencia entre capas (curl con user-agent de navegador, headless) es lo que más bloqueos provoca;
   - con el volumen del piloto, el coste es despreciable.

   En una sola visita guarda el HTML de la respuesta, el DOM renderizado y el MHTML. **Propuesta:** actualizar `sampling-capture` para que el renderizado sea el procedimiento por defecto, con esa justificación, y mantener que la presencia de JavaScript no es una limitación metodológica.
2. **Decisión del usuario (2026-10-25): no se hacen capturas de pantalla.** El método no las exige, y evitan la tentación de juzgar por la prominencia (cautela 4: «prominencia editorial ≠ importancia relativa»).
3. **OQ-14 y OQ-15.**
   - OQ-14 (campos y almacenamiento físico): el motor fija de forma provisional ficheros JSON y gzip por instantánea en `mpir/var`, sin base de datos.
   - OQ-15 (herramientas, navegador y configuración): fija Chrome estable con ventana sobre Xvfb.
   - La configuración definitiva la decide la sonda T-014: Chrome del contenedor o del host, porque sin GPU el contenedor bloquea WebGL.
   - Se anotan ambas sin cerrarlas.
4. **Legitimidad.** El motor aplica robots.txt (RFC 9309) y las reservas de minería de textos y datos (art. 67.3 TRLPI; TDMRep, cabecera y meta), en coherencia con «respetará las políticas aplicables». No hace falta cambio. Se menciona solo si el módulo lo admite sin crear conceptos. No se toca el canon `10-model`.
