---
id: T-057
title: Frontera de «solo tiene sentido para otro producto» en el reglamento PAA (podólogos, pies doloridos, montaña)
status: hecha
depends:
milestone:
created: 2026-10-28
closed: 2026-10-29
---

## Objetivo

Que el agente PAA ponga fuera las preguntas sobre la madre que solo sirven a otro producto, como decidió el usuario en D-146, sin volver a sacar lo heredado

## Criterios de aceptación

- [x] Decisión del usuario sobre la vía: ejemplo hipotético más cercano en el reglamento, regla explícita (necesidad que sirve otro uso del producto) o cambio de los casos
- [x] Reglamento PAA v7 (o casos) con la decisión
- [x] bin/paa control sobre pantuflas y botas sin las regresiones de salud-pie y N1 de pantuflas, y sin perder lo recuperado en v6

## Resultado

Reglamento PAA v7 con la prueba de la respuesta natural y especializaciones desde PAA (D-218); control sin regresiones

## Notas

- 2026-10-29 Decisiones del usuario (T-058, 2026-10-29): (1) Prueba de la respuesta natural para la madre: si la pregunta pide elegir un producto de la madre para una necesidad, va dentro solo si un producto de la clase es una respuesta natural; lo que la clase comparte (cuidado, material, precio) sigue dentro. Podólogos y pies doloridos, fuera en pantuflas. (2) Botas: las preguntas de montaña («mejor calzado para andar por la montaña», «10 mejores marcas de botas de montaña») no van a esp.equitacion ni a cat.botas, sino a una especialización nueva (botas de montaña): PAA puede generar especializaciones; botas es el caso de prueba. Siguiente paso: /docs-update (precisión de D-146 y especializaciones desde PAA), reglamento PAA v7, casos de pantuflas y botas, control.
- 2026-10-29 Control v7 (var/paa/control/2026-10-29T232629/), pantuflas, botas y sofás cama frente a v6: fuera 22/36 → 33/35; criterios 11/11; candidatos 2/2 → 1/2; revisiones 3/3; aportaciones 5/9 → 9/9; especializaciones 1/1 (S1 «de montaña» en botas, con las preguntas 59, 69 y 70); regresiones 2 → 0 (salud del pie y N1 de pantuflas, fuera). Diferencia anotada: en botas, «¿Se estira el calzado de cuero?» sale como reformular de la inferida cat.calzado/24 (talla), no como candidato. Causa probable: la precisión del paso 7 («si cabe en un requisito existente al ampliar su pregunta, reformular»). Dos iteraciones del reglamento dentro de v7 (madre directa, mismo hecho, aportación frente a pista, reformular). Consumo: unos 4,0 M tokens en 7 clasificaciones. Revisión de pistas (D-211) no lanzada.
