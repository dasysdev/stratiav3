---
name: docs-update
description: Incorpora un update a la documentación de stratia.cic, depositado en docs/intake/ o descrito por el usuario. El intake prevalece sobre el contenido existente y lo sobrescribe. Claude decide y aplica sin pedir aprobación: análisis de impacto, decisiones, módulos, glosario, registros y changelog. Después archiva el artefacto como fuente trazable, valida e informa al terminar. Úsala cuando el usuario pida procesar el intake, actualizar o modificar la documentación o incorporar un cambio metodológico.
---

# docs-update — incorporar un update a la documentación

Convierte un **update** en cambios trazables de `docs/`. Un update puede ser uno o varios artefactos de `docs/intake/`, o un cambio que el usuario describe.

Reglas de fondo: `docs/CLAUDE.md` (capas, frontmatter, plantilla, redacción) y el `CLAUDE.md` raíz. Esta skill las aplica, con una excepción: **el intake prevalece sobre ellas** cuando las contradice.

**Entrada:** `$ARGUMENTS`, que puede ser:
- una o varias rutas de `docs/intake/`;
- una descripción del cambio;
- nada: se procesan **todos** los artefactos pendientes de `docs/intake/` (excepto `README.md` y `.gitkeep`).

Si un artefacto está vacío o es ilegible, dilo, déjalo en el intake y continúa con los demás.

## Principios

1. **El intake prevalece.** El contenido del update sobrescribe lo existente, incluidas las invariantes del `CLAUDE.md` raíz y las decisiones `aceptadas`. Ante un conflicto, gana el intake. Se registra una decisión que sustituye la anterior y el conflicto se menciona en el informe final.
2. **Claude decide; el propietario no gestiona el proceso.** No se pide aprobación previa ni se plantean preguntas. Las ambigüedades del artefacto se resuelven con la interpretación más fiel a su texto y más coherente con el resto del canon. Cada interpretación queda escrita en la decisión correspondiente para que pueda revisarse después. Solo se pregunta si el artefacto es ininteligible o si la acción afectaría a algo fuera de `docs/`, `CLAUDE.md` o la propia skill.
3. **No se añade nada que el artefacto no diga.** Decidir una ambigüedad no autoriza a ampliar el contenido con criterio metodológico propio. Lo no resuelto por el artefacto se registra como cuestión abierta.
4. **Se respeta el estado declarado por el artefacto.** Si se presenta como provisional o propuesta, se incorpora con `status: propuesta` (o `> **Estado: propuesta**`). Lo que afirma como vigente se incorpora como vigente.
5. **Una sola fuente de verdad.** Lo sobrescrito se sustituye en todas sus apariciones. Nunca conviven la versión antigua y la nueva.
6. **Precedencia por capas.** Si el artefacto introduce conceptos, criterios, propiedades, escalas, pesos o indicadores, van a `10-model`, aunque el artefacto sea metodológico.
7. **Todo lo procesado va al archivo.** Un artefacto procesado sale de `docs/intake/` y pasa a `docs/archive/intake/`. Solo permanece en el intake si el usuario pide **aplazarlo** o si es ilegible.

## Procedimiento

### 1. Leer y delimitar

- Lee **completo** cada artefacto. Si no es `.md`, usa la herramienta adecuada (PDF por páginas, por ejemplo).
- Varios artefactos del mismo update se procesan juntos. Si se contradicen entre sí, prevalece el más reciente (fecha del fichero o la que declare el artefacto); regístralo.
- Extrae las **afirmaciones de cambio** (definición, regla, concepto, escala, indicador, procedimiento, pendiente…), con cita literal o localizador.

### 2. Orientarse en el canon (lectura mínima)

- Localiza los términos en `docs/glossary.md` y lee solo los módulos canónicos implicados.
- Haz `grep` en `docs/` (sin `archive/`) para encontrar **todas** las menciones afectadas, incluidas las invariantes del `CLAUDE.md` raíz y la skill.
- Revisa:
  - `30-governance/decisions.md`, en especial D-006 y las decisiones relacionadas;
  - `open-questions.md`, por si el artefacto cierra alguna OQ;
  - `issues.md`.
- No leas enteros `decisions.md`, `issues.md`, `open-questions.md` ni `changelog.md`. Localiza con `grep` la entrada, la fila de la tabla o el último ID, y lee solo ese tramo con `sed -n`.

### 3. Analizar el impacto y decidir

| Relación | Tratamiento |
|---|---|
| **confirma** | Sin cambio, o solo añadir a `sources`. |
| **precisa** | Editorial. |
| **amplía** | Añadir en la capa que corresponda. |
| **enmienda** | Sobrescribir la definición, regla, escala o indicador. Decisión de canon (D-NNN). |
| **contradice** (invariante, decisión aceptada, D-006) | **Prevalece el intake.** Sobrescribir, registrar una decisión que sustituye la anterior y actualizar la invariante si procede. |
| **nuevo concepto** | Módulo canónico (existente o nuevo), entrada de glosario y decisión. |
| **cierra pendiente** | Decisión y marcar `cerrada → D-NNN` en la OQ o `resuelta → D-NNN` en la incidencia. |
| **abre pendiente** | Nueva OQ. |
| **fuera de alcance** | Prevalece el intake: se amplía el alcance (`scope.md`) con una decisión. |

Decide también la capa destino, el tipo de changelog (`canon`, `método`, `editorial`, `estructura`, `gobernanza`) y si hace falta un módulo nuevo (plantilla de `docs/CLAUDE.md`, 80–250 líneas).

Guarda internamente el plan con esta forma; se resume en el informe final:

| # | Afirmación | Relación | Destino | Tipo | Acción | Interpretación adoptada |
|---|---|---|---|---|---|---|

### 4. Aplicar (en este orden)

1. **Numeración:** obtén los siguientes IDs libres con `grep` (`D-`, `OQ-`, `I-`) y la fecha con `date +%F`.
2. **Archivar el artefacto:**
   ```bash
   mkdir -p docs/archive/intake
   mv docs/intake/<f> docs/archive/intake/<AAAA-MM-DD>-<slug>.<ext>
   chmod a-w docs/archive/intake/<AAAA-MM-DD>-<slug>.<ext>
   ```
   - Su clave de fuente es `INTAKE <AAAA-MM-DD>-<slug>`.
   - Si el slug ya existe, añade el sufijo `-2`, `-3`…
3. **`decisions.md`:** una entrada por decisión (contexto, decisión, interpretación adoptada si la hubo, consecuencias), añadida también a la tabla. Si sustituye otra, marca la anterior como `sustituida por D-NNN`.
4. **Módulos:**
   - El texto normativo del artefacto va **literal**, con `— INTAKE <stem>` o con «enmendada por D-NNN» si reemplaza una cita anterior.
   - Añade `INTAKE <stem>` a `sources`.
   - `version`: +0.1 por cambio; +1.0 si el módulo se reestructura o se redefine. Actualiza `updated`.
5. **Propagación:** sustituye todas las menciones del paso 2. Si cambia una invariante, actualiza el `CLAUDE.md` raíz.
6. **`glossary.md`:** entradas nuevas o modificadas.
7. **`open-questions.md` / `issues.md`:** cierra las entradas resueltas y abre las nuevas.
8. **`changelog.md`:** una entrada al principio, con la fecha, los tipos, las decisiones enlazadas y el resultado (`aplicado` o `aplicado parcialmente (motivo)`).
9. **Índice:** si hay un módulo nuevo, añádelo a `docs/README.md`.

### 5. Validar

- Ejecuta `python3 tools/check_docs.py` hasta llegar a **0 errores**.
- Haz un `grep` de comprobación: no debe quedar la versión sobrescrita fuera de `archive/` y de las citas históricas de `30-governance/`.
- **Si cambió `00-context/` o `10-model/`**, lanza un revisor independiente (`Agent`, `docs-reviewer`):
  - pásale el artefacto archivado y la lista de ficheros y secciones modificados (no los módulos enteros), sin tus conclusiones;
  - pídele que compruebe si el canon refleja fielmente el intake: omisiones, alteraciones de sentido, añadidos no sustentados, versiones antiguas que sigan vigentes y contradicciones internas;
  - corrige lo que proceda y vuelve a validar.

### 6. Informar

Informe breve al usuario:

- **qué cambió**: decisiones, módulos y versiones;
- **qué se sobrescribió**, en especial las invariantes y decisiones sustituidas;
- **interpretaciones adoptadas** ante ambigüedades;
- **nuevas cuestiones abiertas**;
- **artefacto archivado** (ruta) y **contenido restante** de `docs/intake/`;
- **resultado** de la validación y de la revisión.

## Qué no hacer

- Pedir aprobación o plantear preguntas al propietario, salvo en los casos del principio 2.
- Dejar coexistir la versión sobrescrita con la nueva.
- Inventar contenido, fórmulas, pesos o escalas que el artefacto no proponga.
- Editar `docs/archive/`, salvo para añadir un artefacto archivado.
- Dejar en el intake un artefacto ya procesado, o borrarlo sin archivarlo.
