---
name: web-reference
description: Crea y mantiene la referencia técnica de web-audit (D-133). Añade una fuente (registro, congelación, ficha con citas literales y requisitos técnicos), la actualiza ante una versión nueva (refs diff, pin, revisión de citas y requisitos) y valida con web-audit/bin/reqs check. El canon prevalece; no crea estados, pesos, fórmulas, clases, niveles ni perfiles. Úsala cuando el usuario pida añadir o actualizar fuentes de la evaluación técnica, escribir o revisar requisitos técnicos de Marcado o de Contenido o validar la referencia.
---

# web-reference: referencia técnica de web-audit

Fichas de fuente con citas literales y requisitos técnicos de Marcado y de Contenido, en `web-audit/reference/`. El formato está en `web-audit/reference/README.md`. Las fuentes las custodia `references/` (D-149): registro, versiones congeladas y versión fijada, comunes a todos los sistemas (`references/README.md`; lo propio de web-audit, en `web-audit/README.md`). Los comandos (`references/bin/refs` y `web-audit/bin/reqs`) se ejecutan en el host, desde la raíz del proyecto.

**Entrada:** `añadir FUENTE|URL…`, `actualizar [FUENTE…]` o `validar` (lo que se haga si no se indica nada).

**Antes de empezar**, lee `web-audit/reference/README.md` y, de `docs/10-model/evaluation-scopes.md`, solo las secciones «Perfil de implementación», «Estados del requisito técnico» y «Fuentes de los requisitos técnicos».

## Añadir una fuente

1. **Registro.**
   - Si no está en `references/sources.json`, añade su entrada: `id` en kebab-case, `kind`, `title`, `publisher`, `url` y `uses` con `web-audit`; si viene del inventario de partida, también `inventory`.
   - Si ya está registrada para otro sistema, añade `web-audit` a su `uses`.
   - Los validadores y las skills de terceros no se registran (D-132).
   - Añade la fuente a `web-audit/reference/inventory.md`, con su función y su estado.
2. **Congelar:** `references/bin/refs fetch ID`. La primera versión queda fijada sola.
3. **Clase, nivel y ámbitos**, según las tablas del canon: la de clases de fuente (D-132) y, si es una especificación aplicable, la de niveles del perfil de cada ámbito (Marcado, D-130; Contenido, D-159), con los ámbitos de cuyo perfil es (`scopes`).
   - Si la fuente no encaja en ellas (un consumidor que el perfil no recoge, una clase que no está), no la trates como especificación aplicable.
   - Regístralo en `docs/30-governance/issues.md` con una propuesta, o prepara un intake para `/docs-update`, y dilo en el informe.
4. **Ficha** (`web-audit/reference/cards/ID.json`).
   - `reqs section ID` lista las secciones y `reqs section ID SECCIÓN` muestra su texto. Copia las citas de ahí, nunca de memoria ni de la web en vivo.
   - Cita solo lo que fundamenta un requisito o la función de la fuente.
   - En una especificación aplicable, cita también el texto que fija cada naturaleza: «MUST» y «SHOULD», o las cabeceras «Required properties» y «Recommended properties».
5. **Requisitos** (solo de una especificación aplicable), en el fichero de su ámbito y nivel (Marcado: `requirements/serialization.json`, `vocabulary.json` o `consumer.json`; Contenido: `web-protocol.json`, `web-document.json` o `web-consumer.json`):
   - **Una sola condición comprobable** por requisito (D-132). Si una frase de la especificación exige dos cosas (`name` y `offers`), salen dos requisitos.
   - La **naturaleza** la fija la especificación, nunca tú. Si no dice must, required, shall, should ni recommend, no hay requisito: un «may» es opcional.
   - **Solo lo técnico** (D-145, D-147, D-148; «Qué se escribe» en el README): la presencia de lo exigido, la forma de lo que se publica y la formación estructural (partes exigidas, partes para interpretar un valor, coherencia entre partes), más los recomendados del mínimo de representación. La presencia de un recomendado que solo añade otro hecho no se escribe: es de la evaluación informativa. Si una pasada anterior lo escribió, va a `retired.json` con `reason` `modelo de demanda`.
   - Rellena `method`, `evidence`, `applicability` y `not_evaluable` para que otro pueda comprobar el requisito sin preguntarte.
   - **Vista** (D-161): `view` `general` (una vez por sitio) o `particular`, con los `page_types` a los que se aplica.
   - **Condición del proyecto** (D-162): lleva `decision` en lugar de `spec`. Solo la crea el canon, nunca la skill.
   - Ids: el siguiente número libre del fichero, contando los de `retired.json`, que no se reutilizan.
6. **Validar:** `web-audit/bin/reqs check`, hasta que diga «correcto».

## Actualizar ante una versión nueva

1. `references/bin/refs check [FUENTE…]`: qué ha cambiado en origen.
2. `references/bin/refs fetch FUENTE` y `references/bin/refs diff FUENTE`: los cambios respecto a la versión fijada.
3. **Fijar** la versión nueva con `references/bin/refs pin FUENTE VERSIÓN`: la referencia sigue la versión vigente de cada documento.
   - La versión fijada es una para todos los sistemas. Si `uses` nombra otro, `refs pin` dice cómo revisa él lo suyo: dilo en el informe.
   - La excepción es `schemaorg`. Su versión la fija el canon (D-130): otra release va al intake y no se fija desde aquí.
4. `web-audit/bin/reqs check` muestra las fichas que citan la versión anterior y las citas que ya no están. Por cada ficha de la fuente:
   - vuelve a copiar las citas que cambiaron;
   - revisa los requisitos que las usan: condición, naturaleza, método;
   - añade los requisitos que fije el texto nuevo y retira los que ya no fije (a `retired.json`, con su motivo; «ya no lo fija» todavía no es un motivo del formato: añadirlo es un cambio del README y del validador, que se dice en el informe);
   - pon `version` a la fijada.
5. `web-audit/bin/reqs check`, hasta que diga «correcto».

## Validar

`web-audit/bin/reqs check`. Corrige la referencia, nunca el canon ni el validador para que pase. Si el problema está en el formato o en el canon, dilo en el informe.

## Por lotes

Con varias fuentes, usa agentes en paralelo (`Agent`, `general-purpose`) sin que dos escriban en el mismo fichero:

1. **Fichas:** un agente por fuente; cada uno escribe solo su `cards/ID.json`.
2. **Requisitos:** un agente por nivel; cada uno escribe su fichero de `requirements/` y solo puede añadir citas a las fichas de su nivel.

**Encargo de cada agente:**
- La fuente o el nivel que le toca y los ficheros en los que puede escribir.
- Que lea el README de la referencia y las tres secciones del canon de arriba.
- Que siga los pasos 4 y 5 de «Añadir una fuente».
- Que valide con `reqs check` (los errores de ficheros ajenos no son suyos).
- Que devuelva en pocas líneas lo que ha hecho y sus dudas.

Al final, valida tú el conjunto.

## Reglas

- **El canon prevalece.** La skill no crea conceptos, estados, pesos, fórmulas, umbrales, puntuaciones, clases, niveles, perfiles ni ámbitos (D-133). Si algo falta, va al intake (`docs/intake/`, `/docs-update`) o a `issues.md`.
- **Solo una especificación aplicable fundamenta un requisito técnico** (D-132). Las demás fuentes tienen ficha, pero no requisitos.
- **Los requisitos son técnicos.** No valoran la información comercial (disponibilidad efectiva, criterios de aceptación, GSC; D-129).
- **Los requisitos los deciden los agentes**, siempre con cita. No pidas aprobación: el usuario los revisa si lo pide.

## Informe

Breve:
- fuentes añadidas o actualizadas y su clase;
- citas y requisitos por nivel y naturaleza (el resumen de `reqs check`);
- lo que no encaja en el canon, con la incidencia o el intake abiertos;
- las fuentes que siguen sin ficha.

En una pasada por lotes, el informe queda también en `web-audit/reference/reports/AAAA-MM-DD-tema.md`, con lo que queda pendiente.

Si el trabajo pertenece a una tarea de `bin/pm`, deja los hallazgos con `bin/pm note`.
