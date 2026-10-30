---
name: web-audit
description: Auditado técnico de Contenido y Marcado de un sitio (T-049, D-166, D-167). Sobre las páginas que capture congeló con audit-es (capture/var/audits/AUDIT), aplica los requisitos técnicos de la referencia de web-audit, deja a un agente los casos que piden juicio o el contenido visible de la página y escribe el expediente técnico con la tasa de cumplimiento técnico. Úsala cuando el usuario pida el expediente técnico, la evaluación técnica o la tasa de cumplimiento técnico de un sitio, o auditar técnicamente unas fichas.
---

# web-audit: expediente técnico de un sitio

El código aplica cada requisito técnico de `web-audit/reference/requirements/` a sus casos (D-161): uno por sitio en la vista general y uno por página de la auditoría, según su tipo, en la particular. Cada caso sale con su estado (satisfecho, no satisfecho, NA o NE, D-131) y su evidencia. Lo que el método pide juzgar o leer en el contenido visible (un soft 404, si la página muestra variantes o un precio tachado, si un nombre es de una persona) queda `pendiente`, y lo decide **un** agente. Después el código valida sus juicios y escribe el expediente con la tasa de D-166. Se ejecuta en el host, sin contenedor (la captura sí lo usa).

**Entrada:** `AUDIT` (una auditoría de capture) o las URL de las fichas del encargo.

- Si dan URL y no hay auditoría: primero, `capture/bin/pages crawl AUDIT PORTADA` (unos 3 s por página; un ID ocupado se rechaza); después, `capture/bin/pages audit AUDIT URL…` (sin URL, todas las fichas del universo). Elige un `AUDIT` corto: `tienda-AAAAMMDD`.
- `ls capture/var/audits/` lista las que hay.

## Procedimiento

0. **Imágenes:** `web-audit/bin/audit images AUDIT`. Pasa a capture las URL de imagen del marcado; capture pide cada una con GET, sin el cuerpo, una por segundo a cada host como máximo. Una URL ya registrada no se repite. Si termina con el código 3 (reserva TDM), para e informa.
1. **Evaluar:** `web-audit/bin/audit run AUDIT`. Escribe `web-audit/var/audits/AUDIT/` (`cases.json`, `pending.json`, `run.json`). Si no hay pendientes, escribe también el expediente: salta al paso 4.
2. **Juzgar:** lanza **un** agente (`Agent`, `general-purpose`) con el encargo de abajo y espera a que termine.
3. **Comprobar:** `web-audit/bin/audit check AUDIT`. Si no dice «correcto», continúa el mismo agente (`SendMessage`) con los problemas; si a la segunda sigue mal, para e informa.
4. **Expediente:** `web-audit/bin/audit finish AUDIT`. Escribe `dossier.json` (cada caso con su estado final, quién lo decidió y su evidencia, y las tasas) y `report.md`.
5. **Informar** al usuario, breve:
   - la tasa y la cobertura de cada ámbito, vista y tipo de página, con su desglose por naturaleza (Contenido y Marcado por separado, nunca sumados);
   - los no satisfechos que importan, agrupados (obligatorios primero);
   - las incidencias (NE) por causa;
   - lo que decidió el agente;
   - las páginas no localizadas (`run.json`): no son incumplimientos (D-167).

   Si la ejecución pertenece a una tarea de `bin/pm`, deja los hallazgos con `bin/pm note`.

## Encargo del agente

- Eres el auditor técnico de los casos que el código no puede decidir.
- Trabaja en `/home/gonwsl/projects/stratiav3`. Los casos están en `web-audit/var/audits/AUDIT/pending.json`: cada uno trae el requisito (`condition`, `method`, `applicability`), la pregunta concreta (`question`) y lo que el código ya extrajo (`evidence`).
- Para leer una página: `web-audit/bin/audit text AUDIT PÁGINA` (el texto visible del documento de la respuesta, sin JavaScript, que es el perfil de consumo, D-156). Si hace falta el HTML: `zcat` del `response.html.gz` de la instantánea (su ruta está en `capture/var/audits/AUDIT/audit.json`, campo `snapshot`); búscalo con `grep`, no lo leas entero.
- Responde a la pregunta de cada caso con lo que muestra la página, y nada más:
  - **NA** si no se da la aplicabilidad (la página no muestra lo que la pregunta plantea), con su motivo;
  - **satisfecho** o **no satisfecho** según la condición, con la evidencia literal de la página (un fragmento citado);
  - **NE** solo si la comprobación no se puede hacer con lo que hay, con la causa. NE no es «no satisfecho».
- No uses lo que sepas de la tienda o del producto: solo lo publicado en la página.
- Escribe `web-audit/var/audits/AUDIT/judgments.json`: una lista con un objeto por caso pendiente, `{"req", "page", "state", "evidence", "reason"}` (`reason` es obligatorio en NA y NE). `state` es `satisfecho`, `no satisfecho`, `NA` o `NE`.
- Comprueba con `web-audit/bin/audit check AUDIT` hasta que diga «correcto».
- No leas `cases.json`, `dossier.json` ni `report.md`.
- Escribe `evidence` y `reason` con frases cortas y en voz activa. La evidencia es una cita literal: no la reescribas.
- Devuelve en pocas líneas: cuántos casos de cada estado y tus dudas.

## Qué no hacer

- No corregir a mano los estados que decidió el código ni los juicios del agente: si un estado está mal, el fallo es del método (`/web-reference`) o de la comprobación (`web-audit/src/web_audit/checks/`).
- No sumar ni promediar Contenido y Marcado, ni combinar la tasa de un tipo de página con la de otro o con la general; no añadir umbrales ni estados derivados de la tasa (D-166).
- No descargar nada fuera de capture. El acceso a las imágenes es de capture (paso 0); sus dimensiones, su relación de aspecto y su formato son NE: fuera de V1.
