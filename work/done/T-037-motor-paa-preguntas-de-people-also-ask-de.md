---
id: T-037
title: Motor PAA: preguntas de People Also Ask de google.es con navegador real
status: hecha
depends:
milestone: codigo
created: 2026-10-26
closed: 2026-10-27
---

## Objetivo

Recoger de forma sistemática, reanudable y a ritmo de persona las preguntas PAA de un conjunto de semillas de una clase, con la estrategia optimizada por las sondas de sábanas (2026-10-26)

## Criterios de aceptación

- [x] demand-engine/bin/paa ejecuta un conjunto de semillas, reanudable, y para ante un desafío sin eludirlo
- [x] Preguntas consolidadas por conjunto con su procedencia (semilla, posición, pregunta que la desplegó, fecha)
- [x] Pruebas con Chrome contra un servidor local: despliegue, consentimiento, eco de la consulta y bloqueo
- [x] Conjunto optimizado de sábanas ejecutado en menos de 15 minutos y comparado con la sonda de 25 semillas
- [x] README con la estrategia de semillas y la excepción de legitimidad (robots.txt de Google) pendiente de registrar en el canon

## Resultado

Motor PAA: bin/paa, estrategia núcleo+material con 8 clics, respuestas de IA bloqueadas; conjunto sabanas en ~5 min (200 preguntas, todos los tipos y criterios)

## Notas

- 2026-10-26 Ejecución real 2026-10-26 22:48: 2–4 min por búsqueda (DOM 12–16 MB con 6–8 respuestas de Modo IA abiertas, Chrome sin GPU); el motor ahora cierra cada respuesta. Desde ~23:10, Chrome limpio con el hilo principal de la página de Google al 100 % desde el arranque, sin /sorry/ ni CAPTCHA: posible desafío encubierto tras ~60 búsquedas en la tarde. Motor parado tras dos bloqueos (var/paa/engine.json). Sesiones del perfil revisadas: no se restauraron pestañas antiguas. AC 4 pendiente.
- 2026-10-27 2026-10-27: causa real de la saturación: bucle requestAnimationFrame de las respuestas de IA, pintado por software (Chrome sin GPU); no era bloqueo de Google. Solución: serp.Answers aprende y bloquea las llamadas async/callback sin preguntas (6761; respeta 10041). Pausa 5 s y sin pausa larga (decisión del usuario; endurecer al primer bloqueo, README). Conjunto sabanas completo: 10 semillas, 200 preguntas únicas, 7 búsquedas en 3 min 40 s; todos los tipos útiles y los 7 criterios de la sonda de 25.
