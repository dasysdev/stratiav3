# Casos de control de PAA

Lo esperado de la clasificación PAA de cada conjunto de semillas. Es el conjunto de control del entrenamiento propio de PAA (D-114): una pasada se compara con estos ficheros, y no se acepta un cambio que empeore la concordancia.

- **Un fichero por conjunto:** `<conjunto>.json`, con el mismo nombre que `demand-engine/paa/<conjunto>.json`.
- PAA trabaja por clase y los casos de `cases/` son por ficha. Por eso cada fichero lista en `cases` las fichas de control que cubre.
- **Revisión:** la hizo el usuario el 2026-10-27 (T-042). Marcó cada elemento de la clasificación con el reglamento PAA v3 como esperado o no, y resolvió los dudosos en cinco pasos:
  1. productos vecinos fuera del perímetro (D-141);
  2. la moda nunca genera (D-142);
  3. la popularidad no genera (D-142);
  4. «el mejor» es un criterio intermedio (D-142);
  5. el encogimiento en mantas es una aportación.

  El detalle está en T-042.
- **Enmiendas:** el 2026-10-28 (T-053), D-146 corrigió el paso 1 en pantuflas, botas y sofás cama: la pregunta sobre la categoría madre va dentro cuando trata de algo que la clase hereda, y la del material, si la clase lo tiene o lo hereda. El 2026-10-29 (T-058), D-218 llevó las preguntas de montaña de botas a una especialización nueva que propone PAA. Cada fichero afectado lo registra en `amended`.

## Formato

| Campo | Contenido |
|---|---|
| `set` · `label` · `cases` | Conjunto, nombre y fichas de control de `cases/` que cubre |
| `catalog` | Clave del modelo con que se clasificó: lo esperado vale para esa versión del catálogo |
| `questions` | Preguntas únicas del conjunto revisado |
| `reviewed` | Cuándo, quién, contra qué reglamento, en qué tarea y con qué decisiones vigentes |
| `amended[]` | Correcciones posteriores a la revisión: cuándo, quién, tarea, decisiones y resumen |
| `perimeter.out` | Preguntas que deben quedar fuera del perímetro. `added`: las que añadieron las decisiones de la revisión o de una enmienda; `why`, el motivo de cada una cuando lo hay |
| `criteria[]` | `name`, `verdict` esperado (`genera`, `cubierto`, `no-genera`), `intermediate` si procede, `questions`; `proposed_verdict` cuando la revisión cambió el del agente |
| `candidates[]` | `question`, `blocks`, `trait` y las `questions` que lo apoyan |
| `revisions[]` | `target`, `action` y `summary` |
| `contributions[]` | `target`, `contribution` y `kind` (precisión o sustento) |
| `specializations[]` | Especializaciones nuevas que propone PAA (D-218): `name` y las `questions` que van a ella; se emparejan por las preguntas |

En los cinco últimos, cada elemento lleva `expected`:

- `true`: debe aparecer.
- `false`: no debe aparecer. Sirve para que el control detecte que vuelve un error ya corregido.

Cuando la revisión cambia lo que propuso el agente, el elemento lleva `why` con el motivo.

Los ids (`N1`, `R2`, los ids de criterio) cambian de una ejecución a otra, así que la comparación se hace por **contenido**: qué se pregunta, sobre qué requisito y con qué acción. Igual que `bin/compare` con los casos del modelo de demanda.

**Comparador:** `bin/paa control [CONJUNTO…]` ([manual](../../src/demand_engine/paa/README.md#control-contra-los-casos-de-paa)). Las reglas de la revisión están en el canon (D-141, D-142, D-146) y en el reglamento PAA v6. Las métricas con que se acepta un ajuste siguen abiertas (OQ-64).
