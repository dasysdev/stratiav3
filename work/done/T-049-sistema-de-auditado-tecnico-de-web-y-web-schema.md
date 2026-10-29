---
id: T-049
title: Sistema de auditado técnico de Web y Web Schema.org
status: hecha
depends: T-078
milestone:
created: 2026-10-27
closed: 2026-10-29
---

## Objetivo

Construir en web-audit el auditor técnico: extracción del marcado (primera carga y renderizado, con el motor de captura), comprobaciones de los requisitos técnicos y expediente técnico, cuando el canon tenga el sistema cuantitativo

## Criterios de aceptación

- [x] Decidida con el usuario la forma de compartir el motor de captura de demand-engine
- [x] Sistema cuantitativo técnico fijado en el canon (OQ-30)
- [x] Auditor que produce el expediente técnico de una URL con los estados de cada requisito

## Resultado

Auditor técnico web-audit/bin/audit + skill /web-audit: 356 comprobaciones, expediente con tasa D-166; probado en 5 sitios reales

## Notas

- 2026-10-27 De T-047, decisiones de método comunes a los niveles: HTML servido o DOM renderizado (serialización usa el servido; el consumidor contempla el renderizado; JSON-LD inyectado deja serialización en NA), NE por bloque JSON-LD roto (ws-serialization/001), asimetría de términos no definidos (Microdata los exige, JSON-LD y Schema.org no), alcance en RDFa (Open Graph). Detalle: web-audit/reference/reports/2026-10-27-primera-pasada.md.
- 2026-10-28 2026-10-28 Forma de compartir el motor decidida con el usuario (T-063, alternativa B): sistema de primer nivel capture/ con el motor y el almacén de fichas congeladas comunes; se implanta en T-066 y T-067.
- 2026-10-28 De T-077: tasa de cumplimiento técnico fijada (D-166: una sola tasa satisfechos/evaluados, sin pesos ni umbrales, desglose por naturaleza, cobertura evaluados/pertinentes; vista particular por tipo de página con casos requisito × página, por requisito y por página; vista general una vez por sitio). Páginas de una auditoría (D-167) las congela T-078. Mínimo de Web (D-168): w-document/008–014 y w-consumer/015–017. Al empezar: capture ya guarda los bytes originales con audit-es (response.html.gz, T-069): revisar con /web-reference el punto 2 del método común de Web y el NE de w-document/001 y 004, que aún dicen «hasta T-069».
- 2026-10-28 Matiz del usuario (2026-10-28): la auditoría de una tienda parte del sitemap; las fichas del encargo salen de él. En capture.audit, in_sitemaps por URL dará siempre «yes»; lo que informa es la canónica de cada ficha (campo canonical).
- 2026-10-28 Arquitectura decidida con el usuario: híbrido (C). Código para la extracción común (grafo del marcado, OG, robots, sitemaps, HTTP) y comprobaciones deterministas con primitivas genéricas enlazadas a cada id en un registro de web-audit validado contra la referencia; lo que no tenga enlace o pida juicio, a un agente sobre los hechos extraídos; el código valida y calcula la tasa (D-166). Los requisitos que descargan imágenes, NE hasta que capture las congele (tarea aparte).
- 2026-10-28 Referencia revisada con /web-reference: método común de Web (puntos 2, 3 y 5) y métodos y NE de w-document/001 y 004, robots.txt (w-consumer/009, 011–013) y sitemaps (w-protocol/004–012, w-consumer/014) ya sin «hasta T-069/T-078»; w-consumer/003 precisado: sin indicio de error en el título ni en el h1, satisfecho sin más examen. reqs check correcto (356 requisitos).
- 2026-10-29 Probado con 5 auditorías reales (burritoblanco-t078, kiwoko, guaw, todoplano, eci; ECI parada a petición del usuario tras su primera evaluación). Burrito, flujo completo con /web-audit: 761 casos, 5 juicios del agente (NA), expediente escrito. Rendimiento: ECI (50 sitemaps, 465.000 URL) en 9 s y 300 MB tras leer los sitemaps en streaming. Abierto: I-49 (cobertura y NA). A decidir: el punto 5 del método común descarta las URL de sitemaps hijos en subdirectorios (Magento: /sitemaps/421/), y w-consumer/014 sale no satisfecho en todas las páginas de Todoplano y ECI.
- 2026-10-29 2026-10-29 Decisión del usuario: lectura flexible de la ubicación de los sitemaps, como Google (google-search-sitemaps-build#q05): un sitemap enviado (declarado en robots.txt, por índice o /sitemap.xml) vale para todo su host. Cambiados el punto 5 del método común de Web, w-consumer/014 (cita q05) y el código; w-protocol/009 sigue con la ubicación estricta del protocolo. Todoplano: ficha y categoría pasan a satisfecho.
