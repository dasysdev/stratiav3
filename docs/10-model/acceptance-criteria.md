---
id: acceptance-criteria
title: Criterios de aceptación
layer: model
status: vigente
version: 1.9
updated: 2026-10-29
sources: [BASE §5.2, FUND §6, FUND §10.1, GSC0 §6.4, INTAKE 2026-10-26-choice-criteria-and-descriptions, INTAKE 2026-10-27-ac-applicability-and-reliability, INTAKE 2026-10-27-assessment-hints, INTAKE 2026-10-28-minimum-representation-image, INTAKE 2026-10-28-informative-audit-v1, INTAKE 2026-10-28-shipping-zones, INTAKE 2026-10-29-oq-review, INTAKE 2026-10-29-issues-review]
---

# Criterios de aceptación (AC)

## Definición

> Los **criterios de aceptación** son las condiciones evaluativas con las que se juzgan aspectos diferenciados de la capacidad de la información comercial expuesta en una interfaz para resolver un requisito informativo. — BASE §5.2

| Criterio | Condición evaluada |
|---|---|
| **Concreción** | La información cubre los componentes de la cuestión con la extensión y el detalle necesarios, directamente o mediante derivaciones justificadas. |
| **Precisión** | El significado de afirmaciones, términos, valores y relaciones puede interpretarse inequívocamente. |
| **Aplicabilidad** | La información puede atribuirse con claridad a la entidad, el alcance y las condiciones concretas que plantea el requisito. |
| **Comparabilidad** | La información permite efectuar o evaluar el contraste requerido sobre bases equivalentes o equivalencias justificadas. |
| **Fiabilidad** | La información supera las comprobaciones de corrección y consistencia proporcionadas a su naturaleza: no se acreditan errores ni contradicciones materiales. |
| **Justificación** | La información expuesta aporta una base identificable y suficiente para sostener y reconstruir la respuesta mediante afirmaciones y relaciones de soporte justificadas. |

La definición de **Fiabilidad** está enmendada por [D-121](../30-governance/decisions.md#d-121) — INTAKE 2026-10-27-ac-applicability-and-reliability. Ya no incluye la actualidad ([D-123](../30-governance/decisions.md#d-123)).

Cada criterio se valora con el **GSC** (0/1/2). No hay NA de criterio, salvo el de Comparabilidad en los requisitos que no son dimensión de comparación; NE solo registra una incidencia de la auditoría (regla 9). Ver [scoring-systems](scoring-systems.md#grado-de-satisfacción-de-criterio-gsc).

## Reglas e invariantes

1. **Solo se valoran si la [disponibilidad efectiva](effective-availability.md) = 1.** La disponibilidad no forma parte de este catálogo.
2. **No son indicadores de resolución.** Valoran condiciones específicas y preceden a la síntesis por requisito (IR).
3. **Su formulación se refiere siempre a la información pertinente efectivamente utilizable «en una interfaz»** y a la cuestión y el alcance examinados (FUND §6.1).
4. **Proporcionan juicios diferenciados y complementarios** (BASE §5.2). La regla operativa de no compensación encubierta entre AC es una propuesta V1 (M09, [audit-gsc](../20-methods/audit-gsc/README.md)). La síntesis del IR sigue pendiente.
5. **El impacto relativo de cada criterio depende del RI y del ámbito**; su aplicación no, porque los seis se aplican siempre, salvo el NA de Comparabilidad (reglas 6 y 9, enmienda de [D-117](../30-governance/decisions.md#d-117)). Qué mira cada criterio en un requisito lo orientan sus [pistas de valoración](assessment-hints.md) ([D-125](../30-governance/decisions.md#d-125)). Algunas condiciones pueden ser indispensables: su insuficiencia condiciona el resultado aunque los demás criterios estén satisfechos. **No se trasladan al modelo vigente los antiguos pesos y topes numéricos.**
6. **Comparabilidad es contextual:** se evalúa cuando la cuestión requiere contraste.
   - **Hay contraste cuando la respuesta es una dimensión por la que se comparan las ofertas de la clase** (gramaje, composición, precio…), aunque el RI trate de una sola oferta. Entonces evalúa si se expresa sobre bases contrastables: unidad, denominación normalizada, escala oficial. Las preguntas comparativas de PAA son evidencia de que una dimensión es de comparación ([D-104](../30-governance/decisions.md#d-104), [D-118](../30-governance/decisions.md#d-118)).
   - Puede apoyarse en conversiones o equivalencias justificadas, **sin imponer formatos idénticos** (FUND §6.2).
   - Si la respuesta no es una dimensión de comparación, **Comparabilidad es NA**. Lo decide la marca de dimensión de comparación del requisito en el modelo de demanda, no el auditor ([D-126](../30-governance/decisions.md#d-126), [assessment-hints](assessment-hints.md#reglas-e-invariantes)). Es la única excepción a la regla 9.
7. **Derivaciones admitidas.** Una respuesta puede estar **expresada directamente** o ser **derivable mediante relaciones y operaciones justificadas** por la evidencia publicada.
   - Ninguna derivación válida se penaliza por requerir varios pasos.
   - El número de pasos no es una escala auxiliar del GSC.
   - No se presentan como datos publicados los estados, identidades, condiciones o relaciones que el agente complete con conjeturas o con conocimiento externo no acreditado.
   - Qué derivaciones se admiten lo fija la [prueba de derivación](effective-availability.md#pertinencia-de-lo-derivado) ([D-120](../30-governance/decisions.md#d-120)).
8. **El GSC expresa la satisfacción de la condición**, no la capacidad compensatoria ni el esfuerzo computacional de un modelo. Una valoración baja no demuestra que ninguna IA pueda resolver la cuestión; una alta no garantiza el éxito de cualquier sistema.
9. **Los seis criterios se aplican siempre** que la disponibilidad efectiva es 1 ([D-117](../30-governance/decisions.md#d-117)).
   - No hay NA de criterio. La única excepción es el NA de Comparabilidad en los requisitos que no son dimensión de comparación (regla 6).
   - **NE es una incidencia de la auditoría:** una comprobación que no se pudo hacer (un recurso que no se pudo inspeccionar). Queda fuera de la escala (NE ≠ 0) y se registra qué comprobación falló. No es falta de evidencia sobre lo publicado.
   - El NA del requisito es otro estado y se mantiene: un requisito condicionado que no se activa, o un RI que no corresponde a un ámbito (FUND §3.5).

### Fiabilidad: lectura refutadora y comprobaciones

> **Lectura refutadora:** **2**, supera las comprobaciones que tocan a ese tipo de dato; **1**, hay un defecto no material, o uno que afecta solo a parte de lo examinado; **0**, hay un defecto material. El registro enumera las comprobaciones hechas y el resultado dice «sin defectos detectados en…», nunca «exacto». — INTAKE 2026-10-27-ac-applicability-and-reliability

- Un dato que nada refuta ni confirma recibe el grado que corresponda a las comprobaciones superadas, no NE ([D-121](../30-governance/decisions.md#d-121)).
- El 2 afirma que se superaron las comprobaciones, no que el dato sea verdadero: la ausencia de contradicción sigue sin demostrar exactitud.
- Consecuencia asumida: Fiabilidad discrimina cuando hay defectos; la mayoría de los datos estables sin defectos obtendrán 2.

**Sin fuentes externas** ([D-154](../30-governance/decisions.md#d-154), que enmienda [D-122](../30-governance/decisions.md#d-122)): la auditoría no consulta nada externo a lo que publica el ecommerce. Usa la representación del ámbito y reglas generales citadas (definiciones, normas que fijan el significado de un término, especificaciones de formato). Ningún hecho particular del producto tomado de fuera (un registro, la web del fabricante) entra, ni siquiera para contrastar. Lo que el auditor sepa de un producto concreto no es regla ni evidencia: solo puede frenar una refutación o quedar como sospecha (regla asimétrica, abajo).

**Tres familias de comprobación** ([D-154](../30-governance/decisions.md#d-154)):

| Familia | Qué comprueba | Ejemplos (hipotéticos) | Qué puede concluir |
|---|---|---|---|
| **Estructura del dato** | Las reglas que el propio dato lleva consigo | Dígito de control y longitud del GTIN; composición que suma 100 %; precio final = base − descuento; unidad coherente con la magnitud; valor dentro de una enumeración cerrada (clase energética A–G); fecha de validez publicada y ya vencida en la captura | Refutar, con certeza |
| **Conocimiento del dominio** | Reglas generales: definiciones, denominaciones legales, normas que fijan el significado de un término; imposibilidades físicas o lógicas | «Certificado GOTS» en una sábana 100 % poliéster (GOTS exige al menos un 70 % de fibra natural ecológica); «satén de seda» con composición 100 % poliéster (el Reglamento (UE) 1007/2011 reserva «seda» a esa fibra); un plaid de 130 × 170 cm que pesa 40 kg | Solo refutar |
| **Consistencia dentro del ámbito** | Que lo publicado en el ámbito no se contradiga | Web: texto, tabla, variantes, y HTML frente a Schema.org. Web Schema.org: dentro del marcado. Entre requisitos del mismo ámbito: una bajera de 90 × 190 en una ficha que dice «cama de 150» | Refutar: la contradicción material es el defecto |

- **Conocimiento del dominio** (el del modelo de IA que audita):
  - solo refuta: no puede confirmar un hecho de la oferta;
  - un dato es defecto solo si **no puede** ser verdad según una regla general y descriptiva, citada con su fuente y sin contrafuente (la parte de necesidad de la [prueba de derivación](effective-availability.md#pertinencia-de-lo-derivado)), o por una imposibilidad física o lógica;
  - si solo es improbable, es una sospecha: se anota y no gradúa. «Percal 100 % poliéster» no se refuta, porque existe percal de poliéster. Así, una inferencia por tendencia no puede crear un hecho ([D-119](../30-governance/decisions.md#d-119)) ni destruirlo (Fiabilidad);
  - si el auditor no puede enunciar la regla y de dónde sale, es una sospecha (reexaminabilidad).
- **Conocimiento del modelo, regla asimétrica:**

  > El conocimiento del modelo puede **frenar** una refutación libremente, pero solo puede **producirla** con una regla general citada o con una imposibilidad física o lógica. Lo que el modelo sepa de un producto, una marca o un modelo concretos es una **sospecha**: se anota con su motivo, no gradúa y pasa al informe como «a verificar por el ecommerce». — INTAKE 2026-10-28-informative-audit-v1

  Lo que el modelo sabe de un caso concreto no es reexaminable, puede estar desfasado o confundir variantes, haría depender el resultado del auditor y trataría distinto a marcas conocidas y desconocidas. Usarlo como contrafuente solo evita penalizar ([D-154](../30-governance/decisions.md#d-154)).
- **Comprobaciones por tipo de dato:** son el contenido de las pistas dirigidas a un tipo ([D-127](../30-governance/decisions.md#d-127)), que redacta Claude ([D-137](../30-governance/decisions.md#d-137)). Cada pista dirigida a un tipo se revisa contra la lista de requisitos a los que llega, que da el código. Si la pista no vale en todos, se reescribe más general o pasa a ser una pista dirigida a una fuente o a un requisito ([D-200](../30-governance/decisions.md#d-200), [assessment-hints](assessment-hints.md)).
- **Registro:** dice qué familias se aplicaron: «sin defectos detectados en estructura, dominio y consistencia del ámbito; sin contraste externo». Si a un dato solo le toca la consistencia, también es 2, y el registro lo dice.
- **NE** queda casi limitado a no poder leer una representación que pide la comprobación de consistencia.
- **Certificaciones:** se juzgan por lo publicado, no se validan. En Fiabilidad, solo estructura, dominio y consistencia (una fecha de validez vencida, un sello incompatible con la composición). Los demás AC miran lo suyo: Justificación, que se publiquen el número y el organismo; Precisión, «OEKO-TEX» sin decir qué norma; Aplicabilidad, que la certificación se atribuya al producto que se vende y no a una materia prima.
- **Imágenes:** lo que una foto muestra no sirve para refutar un dato; solo cuenta la información explícita que lleve ([effective-availability](effective-availability.md#imágenes-lo-que-muestran-y-lo-que-expresan), [D-144](../30-governance/decisions.md#d-144)).
- **Identificador ausente:** si el ecommerce no da el identificador que permitiría verificar un dato (p. ej., el número de certificado), cuenta en **Justificación** (P18), no en Fiabilidad. La auditoría no lo verifica, pero es la base que permite a cualquiera verificarlo ([D-154](../30-governance/decisions.md#d-154)).
- **Frontera con la evaluación técnica:** una propiedad mal escrita o una sintaxis inválida es técnica y solo cuenta por su efecto en la disponibilidad; una sintaxis válida con un valor imposible (GTIN con dígito de control erróneo) es Fiabilidad. La sintaxis es la del marcado (serialización y vocabulario); las reglas internas de un valor, como el dígito de control, son estructura del dato. Si un perfil exige un valor válido, ese requisito técnico se evalúa también en el expediente técnico: los dos expedientes son independientes y en ninguno se cuenta dos veces ([D-206](../30-governance/decisions.md#d-206)).
- **Consistencia por ámbito:** cuenta en el GSC de Fiabilidad de su ámbito. En Catálogos distribuidos se comprueba dentro del ítem y entre las variantes de un grupo. La consistencia entre ámbitos es otra dimensión de análisis, que no modifica este GSC ([consistencia transversal](evaluation-scopes.md#consistencia-transversal)).
- **Límite:** Fiabilidad mide la corrección y la coherencia interna de lo publicado, no su veracidad frente al mundo. Un 2 no acredita que una certificación, una clase energética o un GTIN sean válidos ([scope](../00-context/scope.md#límite-de-interpretación)).

### Unidades de un conjunto

> Las unidades de un conjunto (destinos, modalidades de entrega, variantes, momentos del pedido) no son partes de la cuestión y no se divide por ellas. Las cubre la **Concreción** (cobertura de las unidades), la **Aplicabilidad** (atribución de cada valor a su unidad) y la **Precisión** (significado de lo expresado: «nacional», «24/48 h»). — INTAKE 2026-10-28-shipping-zones

- El requisito declara su conjunto, en la pregunta o en la descripción ([D-164](../30-governance/decisions.md#d-164)). Es el tratamiento de las variantes del [ejemplo mínimo](#ejemplo-mínimo-hipotético).
- El silencio sobre una unidad es cobertura parcial (Concreción), no disponibilidad 0 del requisito, y no equivale a un «no»: una ausencia exige prueba de cobertura.
- **Frontera 0/1:** si al menos una unidad del conjunto está cubierta, la Concreción es 1 como mínimo. El 0 queda para cuando lo presente no cubre ninguna unidad (solo información general o auxiliar) ([D-197](../30-governance/decisions.md#d-197)).
- **Ejemplos abiertos:** una lista con «p. ej.» o «…» orienta y no forma componentes. Solo un conjunto declarado cuenta para la Concreción ([D-197](../30-governance/decisions.md#d-197), que ratifica la [RI-07](../20-methods/audit-gsc/ri-profile.md#procedimiento-de-elaboración-ri-01-a-ri-09)).
- Ejemplos (hipotéticos) en el envío, cuyo conjunto son las zonas de España ([D-165](../30-governance/decisions.md#d-165)): solo «envío a Península 4,95 €» afecta a la Concreción; «envío 4,95 €» sin zona, a la Aplicabilidad; «envío nacional», a la Precisión si admite dos lecturas materiales; «envíos a toda España 4,95 €» da Concreción 2 en el coste, porque cubre las zonas por derivación; «no enviamos a Canarias, Ceuta ni Melilla», con las tarifas de la Península y Baleares, da Concreción 2, porque el «no» resuelve; una ficha que dice «gratis a toda España» con una página de envíos que excluye Canarias, a la Fiabilidad (contradicción dentro del ámbito).

### Fundamento de un beneficio reclamado

- El fundamento de un beneficio que el producto reclama («favorece la higiene dental», [D-025](../30-governance/decisions.md#d-025)) se valora en la **Justificación** del requisito de esa prestación, si el modelo lo tiene ([D-183](../30-governance/decisions.md#d-183)).
- Si el modelo no tiene ese requisito, el fundamento no se audita.
- No hay un requisito propio para el fundamento de un beneficio.

## Distinciones

| Par | Diferencia |
|---|---|
| Disponibilidad frente a **Concreción** | La disponibilidad dice si existe información utilizable. La concreción dice si cubre la cuestión con la extensión y el detalle necesarios. |
| **Concreción** frente a **Precisión** | La primera comprueba si la cuestión queda cubierta; la segunda, si el significado de lo expresado es inequívoco. |
| **Precisión** frente a **Aplicabilidad** | Comprender «disponible» no determina **qué variante** está disponible. |
| **Aplicabilidad** frente a **Fiabilidad** | Atribuir bien una afirmación no garantiza su exactitud ni su consistencia. |
| **Fiabilidad** frente a **Justificación** | La fiabilidad depende de que la información supere las comprobaciones de corrección y consistencia. La justificación exige un soporte identificable para reconstruir la respuesta; la falta del identificador que permitiría verificar un dato cuenta en ella ([D-122](../30-governance/decisions.md#d-122), [D-154](../30-governance/decisions.md#d-154)). Citar una fuente no demuestra su verdad, y la ausencia de contradicciones no demuestra exactitud. |
| **Evidencia compartida** | Un hallazgo puede afectar a varios criterios, pero hay que explicar la consecuencia específica para cada uno, sin tratarlo como varios defectos independientes. |

**Resumen:** la disponibilidad trata del acceso; la concreción, de la cobertura; la precisión, del significado; la aplicabilidad, de la atribución; la fiabilidad, de la confianza en lo afirmado; la justificación, del fundamento. La comparabilidad interviene cuando hay contraste.

## Interpretación

La interpretación semántica legítima y el razonamiento sustentado se distinguen de la **invención de hechos faltantes**. Por ejemplo (GSC0 PF-06, propuesta V1), el significado general de `InStock` puede reconocerse por conocimiento del dominio. En cambio, la identidad de la variante a la que se refiere, la oferta y el momento requieren sustento en las fuentes admitidas.

Del mismo modo, que una ficha declare el tejido o la composición («percal», «100 % algodón») no resuelve un requisito sobre la prestación («¿qué sensación térmica ofrece?»): deducir la prestación del atributo completa con conocimiento del dominio un hecho que la oferta no declara, y no se descarta por su número de pasos. Lo dictamina la **pertinencia**, en la auditoría: el atributo por sí solo no es pertinente para la prestación, de modo que no se llega a valorar los AC ([D-090](../30-governance/decisions.md#d-090), enmendada por [D-119](../30-governance/decisions.md#d-119); [choice-criteria](choice-criteria.md#prestación-derivada-de-un-atributo)). La frontera con el reconocimiento semántico legítimo y con las derivaciones admitidas la fija la [prueba de derivación](effective-availability.md#pertinencia-de-lo-derivado) ([D-120](../30-governance/decisions.md#d-120)).

La relación orientativa entre criterios y propiedades que sustentan su análisis está en [quality-properties](quality-properties.md#asociaciones-orientativas-con-los-criterios).

## Ejemplo mínimo (hipotético)

**RI:** disponibilidad comercial de cada variante. **Ámbito:** Web. Ficha con tallas 41, 42 y 43 y la afirmación «Disponible para compra online» en la cabecera del modelo, sin estado por talla.

| AC | Valor ilustrativo | Motivo |
|---|---|---|
| Concreción | 1 | Hay información sobre el modelo, pero falta el desglose por variante. |
| Precisión | 2 | La expresión es interpretable; el problema está en la atribución. |
| Aplicabilidad | 1 | El estado se atribuye al modelo, no inequívocamente a la talla 42. |
| Comparabilidad | NA | La disponibilidad por variante no es una dimensión de comparación (marca del requisito). |
| Fiabilidad | 2, si supera las comprobaciones de estructura del dato y de consistencia dentro del ámbito (hipótesis) | Sin defectos detectados; no afirma que el estado sea exacto. |
| Justificación | 1 | Soporte parcial; no fundamenta una conclusión para la talla 42. |

Los valores son ilustrativos, no una auditoría real.

## Pendiente

- Guías por criterio con pruebas, evidencias, reglas interpretativas y anclajes 0/1/2. Hay propuesta V1 en [ac-guides](../20-methods/audit-gsc/ac-guides.md), pendiente de calibración. Ver [open-questions](../30-governance/open-questions.md).

## Relacionado

- [quality-properties](quality-properties.md)
- [scoring-systems](scoring-systems.md)
- [assessment-hints](assessment-hints.md): pistas de valoración de cada requisito.
- [gsc-decision](../20-methods/audit-gsc/gsc-decision.md): procedimiento de decisión (propuesta V1).
