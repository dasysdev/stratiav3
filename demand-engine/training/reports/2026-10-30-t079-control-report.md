# T-079 · Control del reglamento v5

Fecha: 2026-10-30. Control de la reescritura de `classifier/rulebook.md` con las reglas de estilo (v4 → v5, sin cambiar ninguna regla).

**Ejecuciones:**

- `var/runs/2026-10-30-v5-a`: los 14 casos de control con el reglamento v5, las reglas 8 y el catálogo vigente (pistas 0.4).
- Comparadas con las salidas v4 de `var/runs/2026-10-29-v7-a` y `-b`, ensambladas de nuevo con el mismo catálogo y las mismas reglas. Así, la única diferencia es el reglamento. El reensamblado se hizo en memoria, fuera de `var/runs/` y sin tocar la cola.
- Pareja v4–v4 (a, b): la variación propia del clasificador. Parejas v4–v5 (a y b frente a v5): el efecto del reglamento.

**Consumo:** 38,5 M de tokens en 14 casos: 2,75 M por caso y 41 k de salida. Con el v4, los mismos casos gastaron 1,26 M (a) y 1,49 M (b) por caso, con 21 k de salida. El v5 tiene un 13 % más de palabras y la mitad de frases por línea. Causa probable del aumento: el agente cuenta más hechos declarados (756 frente a 664 y 682) y escribe más texto libre.

## Resultado

| Medida | v4 (a / b) | v5 |
|---|---|---|
| Composición frente a lo esperado | 13/14 · 12/14 | **14/14** |
| Especializaciones esperadas | 6/14 · 7/14 | 7/14 |
| Cuestiones clave | 27/40 · 27/40 | 27/40 |
| Inferidas esperadas | 0/2 · 0/2 | 0/2 |
| Hechos declarados sin pregunta | 19 · 19 | **16** |

| Estabilidad de la pareja | v4–v4 | v4b–v5 | v4a–v5 |
|---|---|---|---|
| Composición | 11/14 | 12/14 | 13/14 |
| Clave del modelo | 13/14 | 14/14 | 13/14 |
| Especializaciones por id | 13/14 | 14/14 | 13/14 |
| Aplicación de la oferta | 8/14 | 11/14 | 11/14 |
| Importancia en los requisitos comunes | 380/383 | 383/383 | 380/383 |

**El v5 no empeora ninguna medida.** Mejora la composición frente a lo esperado y los hechos sin pregunta. Entre una ejecución v4 y una v5 hay la misma estabilidad, o más, que entre dos ejecuciones v4.

**Lo que falta frente a lo esperado ya faltaba con el v4:** las especializaciones esperadas (7/14), las cuestiones clave (27/40) y las dos inferidas esperadas. No sale del cambio de redacción.

## Dudas que se repiten

- Los dos plazos de devolución de Burrito Blanco (14 días en la ficha, «hasta 45 días» en el mensaje común): todos los casos de la tienda los asignan a `gen/11`.
- `esp.juego/02` repite las medidas por pieza que ya pregunta el bloque de la pieza (D-086): fundas nórdicas, sábanas y toallas.
- Un selector de color cuyas muestras enlazan con otras fichas: unos agentes activan `gen.variantes` (D-082) y otros tratan el color como valor del producto.
- Mensajes comunes sin cifra que fijan algo comprobable (cuidados, pago a plazos): el paso 1 solo nombra importe, porcentaje, plazo o coste (D-074).
- Montaje y retirada gratuitos en los sofás: unos agentes activan `gen.posventa` y otros no (D-066).
