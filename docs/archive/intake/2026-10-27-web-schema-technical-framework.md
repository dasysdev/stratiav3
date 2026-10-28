# Marco de la evaluación técnica de Web Schema.org

Fecha: 2026-10-27. Update descrito por el usuario en la sesión de planificación del sistema web-audit (tarea T-044). Parte del estudio del inventario de fuentes para la auditoría de Schema.org (`tmp/inventario_fuentes_auditoria_schema_org.md`) y del canon de la evaluación técnica (BASE §3.1 y §6.2; FUND §4.2, §7.3, §8.5 y §12; OQ-30). Claude propuso un plan con cuatro decisiones y el usuario respondió punto por punto.

Encargo de partida: «vamos a crear un nuevo sistema web-audit. crearemos una skill de creación y mantenimiento de documentación de referencia con los criterios de evaluación. más adelante crearemos el sistema de auditado».

## 1. Alcance de web-audit

Usuario: «solo técnico».

- **web-audit** es el sistema de la **evaluación técnica** de los ámbitos **Web** y **Web Schema.org** (unidad: requisito técnico × ámbito). Empieza por Web Schema.org.
- No hace la evaluación informativa (disponibilidad efectiva, AC, GSC): la auditoría GSC es otro sistema. Esa auditoría puede consultar la referencia técnica para interpretar el marcado, sin que los requisitos técnicos se conviertan en criterios informativos.
- Primera pieza: la documentación de referencia con los criterios de la evaluación técnica y una skill para crearla y mantenerla. El sistema de auditado viene después.

## 2. Perfil de implementación

Usuario: «sí. versión más reciente 30.1 (ahora)».

Lo que motivó la propuesta: el canon usa «perfil de implementación» en la tasa de cumplimiento técnico (BASE §6.2) sin definirlo. Schema.org es permisivo por diseño: los rangos son tipos esperados, admite texto donde espera una entidad y no tiene propiedades obligatorias. Las condiciones con fuerza normativa de sintaxis salen de la serialización (JSON-LD 1.1); las propiedades exigidas y recomendadas, de los consumidores (Google Search).

- El **perfil de implementación** es el conjunto de especificaciones aplicables respecto del cual se determinan los requisitos técnicos pertinentes de un ámbito y su naturaleza obligatoria o recomendada.
- La naturaleza **obligatoria o recomendada** de un requisito técnico es **relativa al perfil** que la establece. La fija la especificación, nunca el auditor.
- En **Web Schema.org**, el perfil tiene tres niveles:

| Nivel | Especificaciones | Qué fijan |
|---|---|---|
| **Serialización** | JSON-LD 1.1 (con su procesado), Microdata y RDFa 1.1 | Sintaxis y estructura del marcado |
| **Vocabulario** | Schema.org, versión fijada **30.1** | Tipos, propiedades, dominios, rangos y enumeraciones |
| **Consumidor** | Google Search: fichas de comerciante (Merchant listing), variantes de producto, políticas de devolución y de envío, organización y fragmentos de producto (Product snippet) | Propiedades exigidas y recomendadas por ese consumidor |

- La versión del vocabulario se fija y queda registrada con cada resultado. Cambiarla obliga a revisar los requisitos que dependen de ella.
- **Google Merchant Center** pertenece a Catálogos distribuidos. En Web Schema.org solo sirve para la consistencia transversal ([D-124]).
- Lectura de Claude, registrada en T-044: el «sí» aprueba la recomendación sin añadir otros consumidores (Bing u otros). Pueden añadirse después con la skill, como perfil nuevo.

## 3. Estados del requisito técnico

Usuario: «sí».

- **Satisfacción:** **satisfecho** o **no satisfecho**, según la comprobación de su método.
- **Aplicabilidad:** **no aplicable (NA)** cuando el requisito no corresponde al perfil o al recurso examinado. Se justifica y se separa de los requisitos pertinentes.
- **Evaluación:** **no evaluable (NE)** es una **incidencia de la auditoría** (una comprobación que no se pudo hacer), no una puntuación. No equivale a «no satisfecho». Es el mismo tratamiento que en la evaluación informativa.
- El **sistema cuantitativo** sigue abierto: cómo entran las obligatorias y las recomendadas en la tasa de cumplimiento técnico, umbrales y cobertura. No se fijan pesos.

## 4. Función de las fuentes

Aprobado con el plan (función de cada clase de fuente del inventario).

- Solo una **especificación aplicable** (de serialización, de vocabulario o de un consumidor) fundamenta un requisito técnico.
- Las demás fuentes tienen otra función:

| Clase | Ejemplos del inventario | Función |
|---|---|---|
| Instrumento del sistema | SHACL, PROV-O | Sirven para construir el auditor (perfiles como restricciones, procedencia de las evidencias); no son condiciones que deba cumplir el ecommerce |
| Principios generales | W3C Data on the Web Best Practices | Orientan; no dan requisitos comprobables de una ficha |
| Método de comprobación | Schema Markup Validator, Rich Results Test | Sirven para comprobar y calibrar; no son fuente de criterios ni equivalen a calidad informativa |
| Práctica de terceros | Skills de auditoría SEO | Listas de errores frecuentes, sin autoridad |
| Antecedente histórico | GS1 SmartSearch (2015) | Solo contexto |
| Datos comerciales distribuidos | Merchant Center | Catálogos distribuidos y consistencia transversal |

- Un requisito técnico expresa **una sola condición comprobable**.
- Cada requisito técnico cita literalmente su especificación: fuente, sección y versión congelada.

## 5. Referencia técnica

Usuario: «sí, A».

- La documentación de referencia vive en `web-audit/reference/`, como datos y fichas gobernados por el canon, igual que el catálogo de bloques de demand-engine:
  - las fuentes, congeladas por versión (fuera de git y desechables);
  - una ficha por fuente, con citas literales;
  - los requisitos técnicos, con los siete campos del canon, su perfil y su cita.
- Los requisitos técnicos los deciden los agentes, siempre con cita. El usuario los revisa si lo pide.
- Una skill los crea y los mantiene: añadir una fuente, actualizar ante una versión nueva y validar. No crea conceptos, estados, pesos ni fórmulas; si le falta algo, va al intake.

## 6. Pendiente

- **Frontera del GTIN.** Un GTIN con el dígito de control inválido, ¿es sintaxis (técnica) o valor (Fiabilidad, D-122)? El perfil de Merchant listing lo trata como condición propia. Propuesta de Claude: la «sintaxis» de D-122 es la del marcado (serialización y vocabulario); las reglas internas de un valor, como el dígito de control, son estructura del dato y cuentan en Fiabilidad. Si un perfil de consumidor exige un GTIN válido, ese requisito técnico se evalúa también en el expediente técnico, porque los dos expedientes son independientes y en ninguno se cuenta dos veces.
- **OQ-30**, lo que queda: los requisitos técnicos concretos (en web-audit), el método y la cobertura de cada uno, el sistema cuantitativo técnico y los perfiles de Web (sin marcado) y de Catálogos distribuidos.
