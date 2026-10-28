# Auditoría informativa V1: perfil de Web, ámbitos, ejecución en dos fases y Fiabilidad sin fuentes externas

Decisiones del usuario del 2026-10-28, tomadas en sesión al empezar el sistema de valoración de calidad (auditoría informativa GSC) y recogidas por Claude el mismo día. Solo documentación: no se implementa código.

## 1. Perfil de consumo de Web

Propuesta de Claude: el perfil base de Web es la respuesta HTTP sin ejecutar JavaScript (lo que capture guarda como `response.html`); el DOM tras la carga sin interacción (`dom.html`) queda como segundo perfil versionado, más adelante.

Usuario: «perfil correcto».

## 2. Ámbitos de la V1

Propuesta de Claude: Web y Web Schema.org; Catálogos distribuidos, aplazado (no hay feeds).

Usuario: «web + web schema».

## 3. Unidad de trabajo del agente auditor

Propuesta de Claude (alternativa E, ejecución en dos fases):

- **Fase 1, un agente por ficha × ámbito:** exploración, pertinencia y disponibilidad efectiva de todos los RI (OP-03…07). Mira la página entera una vez y deja la prueba de cobertura de cada ausencia. Los RI con disponibilidad 0 terminan aquí (IR = 0).
- **Fase 2, agentes por lote de RI con disponibilidad 1** (un bloque o una entidad, unos 10–15 RI): los seis AC con sus pistas (OP-08…10). Reciben las evidencias localizadas y la representación completa, para poder reabrir. En Web ven HTML y Schema.org juntos.
- **Entre fases, el código** comprueba que cada fragmento citado existe literalmente en la representación del ámbito.
- **Mitigación:** un 0 sin registro de cobertura no pasa el validador; la calibración mide sobre todo los falsos 0.
- **Motivo:** un modelo real tiene 44–72 RI (mediana ~55): unos 110 RI × ámbito y hasta 660 juicios por ficha. Un agente por ficha no cabe; un agente por RI es demasiado caro; lotes sin fase común no ven la página entera para probar una ausencia.

Descartadas: A (un agente por ficha), B (ficha × ámbito en un solo paso), C (lotes de RI sin fase común), D (un agente por RI).

Usuario: «2 ok a E».

## 4. Fiabilidad sin fuentes externas

Propuesta inicial de Claude (B): consultar fuentes independientes solo si la ficha publica el identificador, el registro es concluyente y el acceso es público. Dato: en 45 fichas congeladas no hay certificaciones con número ni clase energética; el GTIN está en 43.

Usuario: «no voy a validar certificaciones. Replantea como se evalua este AC».

Replanteo de Claude:

- La auditoría no consulta nada externo a lo que publica el ecommerce: la representación del ámbito y reglas generales citadas (definiciones, normas que fijan el significado de un término, especificaciones de formato). Ningún hecho particular del producto tomado de fuera entra, ni siquiera para contrastar.
- La definición de Fiabilidad no cambia.
- Tres familias: **estructura del dato** (refuta con certeza: dígito de control y longitud del GTIN; composición que suma 100 %; precio final = base − descuento; clase energética A–G; fecha de validez publicada y vencida en la captura), **conocimiento del dominio** (solo refuta, con una regla general citada y sin contrafuente; si solo es improbable, sospecha) y **consistencia dentro del ámbito** (Web: texto, tabla, variantes, HTML frente a JSON-LD; Web Schema.org: dentro del marcado; entre requisitos del mismo ámbito). Desaparece la fuente independiente.
- Escala sin cambios: 0 defecto material; 1 defecto no material o parcial; 2 sin defectos detectados. El registro dice qué familias se aplicaron: «sin defectos detectados en estructura, dominio y consistencia del ámbito; sin contraste externo». Si a un dato solo le toca la consistencia, también es 2, y el registro lo dice. Sin estado nuevo. NE en Fiabilidad casi desaparece: solo si no se pudo leer una representación que pide la consistencia.
- Certificaciones: se juzgan por lo publicado, no se validan. Fiabilidad: solo estructura, dominio y consistencia (fecha de validez vencida, sello incompatible con la composición). Justificación: se publican el número y el organismo (PV-4 y PV-38 se mantienen): la auditoría no los verifica, pero son la base que permite a cualquiera, IA incluida, verificarlos. Precisión: «OEKO-TEX» sin decir qué norma. Aplicabilidad: la certificación se atribuye al producto que se vende, no a una materia prima.
- Pistas: PV-5 y PV-39 (el número ha de existir en el registro) se retiran; PV-6 y PV-40 se retiran y se reescriben como pistas de Aplicabilidad, con número nuevo. Cambio de código, pendiente.
- Límite: Fiabilidad mide la corrección y la coherencia interna de lo publicado, no su veracidad frente al mundo. Un 2 no acredita que una certificación, una clase energética o un GTIN sean válidos. Se añade a los límites de interpretación.

Usuario: «para la Fiablidad. Podrias usar el conocimeinto del modelo?».

Respuesta de Claude: ya lo usa (el conocimiento del dominio es el del modelo que audita, D-122), pero solo con reglas generales. Tres tipos de conocimiento del modelo:

| Tipo | Ejemplo (hipotético) | ¿Refuta? |
|---|---|---|
| Regla general citable (ley, norma, definición, especificación) | «Seda» reservada a esa fibra (Reglamento (UE) 1007/2011); dígito de control GS1 | Sí: se enuncia, se cita y no tiene contrafuente. |
| Imposibilidad física o lógica | Un plaid de 130 × 170 cm que pesa 40 kg; una composición del 120 % | Sí: es una regla general; el dato no puede ser verdad. |
| Hecho particular que el modelo «sabe» | «El Stressless Wave lleva base de acero»; «ese GTIN es de otra marca» | No: es una sospecha y no gradúa. |

Por qué el hecho particular no refuta: no es reexaminable (M10); la memoria del modelo puede estar desfasada o confundir versiones, variantes y mercados; el resultado dependería del auditor (M12, invariante 14); trato desigual entre marcas conocidas y desconocidas; un falso 0 daña al cliente sin fundamento; mismo espíritu que la invariante 9.

Regla asimétrica propuesta:

> El conocimiento del modelo puede **frenar** una refutación libremente, pero solo puede **producirla** con una regla general citada o con una imposibilidad física o lógica. Lo que el modelo sepa de un producto, una marca o un modelo concretos es una **sospecha**: se anota con su motivo, no gradúa y pasa al informe como «a verificar por el ecommerce».

Lo general se va escribiendo como pistas por tipo de Fiabilidad, citadas (OQ-66).

Usuario: «OK».
