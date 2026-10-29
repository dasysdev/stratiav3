# T-090 · Pasada de control de la inducción de las especializaciones

Fecha: 2026-10-29. Pasada de control de [D-216](../../../docs/30-governance/decisions.md#d-216): las especializaciones son bloques del catálogo que induce el entrenamiento, y el clasificador (reglamento v4) las usa por su id.

**Ejecuciones:**

- `var/runs/2026-10-29-v7-a` y `-b`: los 14 casos de control y los 5 casos de ECI con especializaciones. Reglas 7. A se clasificó entera antes que B, para que B encontrara las especializaciones que A registró.
- Comparadas con `var/runs/2026-10-26-v6-a` y `-b` (control, reglamento v3) y `var/runs/2026-10-25-eci-a` y `-b` (los 5 casos de ECI, reglamento v3).

**Ciclos:**

- [Reglas 7](2026-10-29-v7-report.md) (v6 y eci): se compila `esp.juego`. Las propuestas de ECI quedan fuera del marco porque no tienen información resolutiva (D-063). La familia de importancia también se acepta: la coherencia por requisito pasa de 52 a 11.
- [Reglas 8](2026-10-29-v8-report.md) (v7 y eci): se compilan `esp.a-bateria` (con `esp.bateria` como sinónimo), `esp.luces` y `esp.equitacion`. La importancia se descarta porque la coherencia de los modelos empeora de 0 a 1. `esp.compartimento-portatil` queda fuera del marco: solo existe en las ejecuciones v3, y el clasificador v4 lo recoge en el bloque de categoría.

**Consumo:** 51,6 M de tokens en 38 casos: 24,8 M en A y 26,8 M en B. El 92 % es lectura de caché.

## Resultado

| Medida | v6 / eci | v7 |
|---|---|---|
| Clave, 5 casos de ECI | 3/5 | **5/5** |
| Clave, control | 14/14 | 13/14 |
| Especializaciones (por id), control | 14/14 | 13/14 |
| Composición, control | 13/14 | 11/14 |
| Aplicación de la oferta, control | 8/14 | 8/14 |
| Importancia en los requisitos comunes, control | 359/359 | 376/379 |
| Hechos declarados sin pregunta, control (A / B) | 32 / 34 | **19 / 19** |
| Cobertura del control: especializaciones esperadas (A / B) | 6 / 6 | 6 / 7 |
| Cobertura del control: cuestiones clave (A / B) | 27 / 26 | 26 / 27 |

**La clave inestable por el nombre desaparece.** Las dos lijadoras toman `esp.a-bateria@0` en A y en B; en eci, la misma lijadora salía como `esp.a-bateria` y como `esp.bateria`, y la otra salía sin especialización en A. También son estables `esp.luces` (deportiva) y `esp.juego` (los cinco juegos, del catálogo).

**Lo que empeora en el control, y por qué:**

- **Clave, `bota-polo-e`:** B registró `esp.equitacion` y A no la propuso. La inestabilidad es de existencia, no de nombre: ya ocurrió en v4. En la pasada no estaba en el catálogo; con las reglas 8 está compilada y el clasificador la verá en la clase.
- **Composición, 3 casos:** las dos fundas nórdicas añaden en B el alias «Juegos de cama» (hg-15-1-11), y la manta cambia de nivel (Mantas decorativas en A, Mantas en B). Las 3 diferencias de importancia salen de ese cambio de la manta. La composición no se induce (OQ-49) y no depende de T-090.

## Causas y corrección

Las tres discrepancias se repasaron con el usuario caso a caso, con lo esperado en los casos de control como resultado deseado. En los tres casos el clasificador se aparta de una regla que ya existe. El reglamento v4 se precisa sin decisiones nuevas:

| Caso | Causa | Corrección del reglamento |
|---|---|---|
| `bota-polo-e` | A buscó el atributo «equestrian-discipline», que es de una categoría afín (`sg-4-5`), y concluyó que no había apoyo. B registró la especialización con ese mismo apoyo afín. Ninguno vio que Botas (`aa-8-3`) tiene `boot-style` = Equitación. | P4: el valor de un atributo de un componente es apoyo; el apoyo afín es evidencia complementaria y no basta solo (D-024). El bloque compilado ya citaba `boot-style=Equitación` y el valor del PTD `BOOT`. |
| Fundas nórdicas | El paso 2.3 («no entra si traería requisitos que no aplican») admitía dos lecturas. A: no entra. B: como alias no trae requisitos, así que entra. Los dos vieron `warmth-level` («del edredón o la colcha») con `bin/taxo category`. La divergencia ya estaba en v2, v4 y v6. | Paso 2.3: la prueba vale también para un alias; los atributos se miran con `bin/taxo category` aunque la categoría no tenga bloque. Ejemplo: Juegos de cama en un juego de fundas sin relleno (D-032). |
| `manta-nacarina-046` | A eligió la hoja Mantas decorativas porque la tienda llama «plaid» a las tres medidas. | Paso 2.3: ejemplo de una manta que se vende en medidas de cama y en una de sofá: es Mantas (D-028). |

## Verificación

`var/runs/2026-10-29-v7r-a` y `-b`: los 4 casos, con las reglas 8 y el reglamento corregido. Consumo: 19,5 M de tokens.

| Caso | Clave A = B | Composición A = B | Composición = esperada | Especialización |
|---|---|---|---|---|
| `bota-polo-e` | sí | sí | sí | `esp.equitacion@1` en las dos |
| `funda-nordica-bordada-401` | sí | sí (sin alias) | sí | `esp.juego@1` |
| `funda-nordica-salvia-642` | sí | sí (sin alias) | sí | `esp.juego@1` |
| `manta-nacarina-046` | sí | sí (Mantas) | sí | — |

El control, con v7 en los otros 10 casos y v7r en estos 4, ya no empeora frente a v6:

| Medida | v6 | v7 + v7r |
|---|---|---|
| Clave | 14/14 | 14/14 |
| Especializaciones (por id) | 14/14 | 14/14 |
| Composición | 13/14 | 14/14 |
| Aplicación de la oferta | 8/14 | 9/14 |
| Importancia en los requisitos comunes | 359/359 | 382/382 |

## Hallazgos para otras tareas

- **Juegos y medidas (D-086):** `esp.juego/02` repite las medidas de cada pieza que ya preguntan los bloques de las piezas. Varios agentes lo votan principal, crítico o «no relevante». El relevo natural es el filtro de relevancia de su requisito en esas clases.
- **Nivel de las especializaciones:** los agentes anclan `esp.a-bateria` y `esp.luces` en la hoja, aunque dicen que valen para toda la rama. Ahora sube solo con dos hijas que la compartan.
- **Dudas repetidas del clasificador:** el plazo de devolución contradictorio de Burrito Blanco (14 y 45 días), «Envío a España» frente a «a toda España» (D-165) y pestañas vacías en la ficha congelada (seguridad y devoluciones de ECI).
