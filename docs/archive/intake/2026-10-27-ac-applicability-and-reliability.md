# Aplicación de los criterios, pertinencia de las derivaciones y Fiabilidad

Fecha: 2026-10-27. Update descrito por el usuario en la sesión de diseño del sistema de reglas que rige la valoración de los criterios de aceptación. Recoge las decisiones del usuario sobre las propuestas de Claude. Ortografía de las citas normalizada.

Encargo de partida: «Vamos a empezar en el sistema de reglas que rigen cómo se valoran los criterios de aceptación. Se me ocurre que hay un marco general y luego cada requisito fija algún matiz para orientar la evaluación.» Antes de construir, el usuario pidió resolver cuatro problemas y confirmar si un criterio puede ser NA o NE: «Los criterios siempre se evalúan y aplican. Confirmémoslo. Quizás en la práctica es así salvo algunas excepciones.»

## 1. Aplicación de los criterios: NA y NE

Palabras del usuario: «No hay NA, NE es una incidencia. NA de comparabilidad aún no podemos decidir (depende de esta sesión).»

- Los seis criterios se aplican y se evalúan siempre que la disponibilidad efectiva es 1. No hay NA de criterio.
- Excepción pendiente: el NA de **Comparabilidad**, que se decide con las reglas de AC por requisito (punto 5).
- **NE es una incidencia de la auditoría**, en cualquiera de los seis criterios: queda fuera de la escala (NE ≠ 0) y se registra qué comprobación falló (p. ej., no se pudo inspeccionar un recurso, o un registro externo no respondió). Deja de ser el estado que absorbe «nada confirma ni refuta el dato» en Fiabilidad (ver punto 3).
- El **NA del requisito** se mantiene: es otra cosa (un requisito condicionado que no se activa, o un RI que no corresponde a un ámbito, FUND §3.5). Claude lo dio por hecho y el usuario no lo objetó.
- Los ejemplos del canon que registran «Fiabilidad NE» por falta de corroboración dejan de valer y se corrigen.

### Comparabilidad en un RI de una sola oferta

Aceptado («es como propones»): el contraste se exige cuando la respuesta es una **dimensión por la que se comparan las ofertas de la clase** (gramaje, composición, precio…). Entonces Comparabilidad evalúa si se expresa sobre bases contrastables (unidad, denominación normalizada, escala oficial), aunque el RI trate de una sola oferta. Las preguntas comparativas de PAA son evidencia de que una dimensión es de comparación (D-104).

## 2. Prestación derivada de un atributo (D-090): se decide en la pertinencia

Palabras del usuario: «A. El recomendado.»

- Un atributo (tejido, material, composición) **por sí solo** no es información pertinente para un requisito sobre una prestación: solo aporta una tendencia, no un vínculo fundado (PF-03). Sin nada más, la disponibilidad efectiva es 0, el IR es 0 y no se valoran los AC. La recomendación es declarar la prestación.
- Con el matiz «por sí solo»: si la ficha declara la prestación («percal, fresca para verano»), el atributo puede acompañarla como contexto.
- Se enmienda D-090: lo dictamina la **pertinencia** en la auditoría, no la valoración de los AC. Sigue en pie que no lo dictamina el modelo de demanda y que el requisito de la prestación tiene que existir en el modelo.
- Lectura adoptada de las palabras originales del usuario en D-090 («eso ya es tarea de la valoración de criterios de aceptación»): «es tarea de la auditoría, no del modelo de demanda».
- Motivos: es lo que el canon ya hace con «producto muy vendido» frente a la disponibilidad (PF-07, GSC0 §6.5); encaja con la regla 6 de la información resolutiva y con CT-08; evita que cualquier atributo próximo al tema abra la puerta de la disponibilidad (invariante 10). Lo pertinente pero insuficiente es el mismo hecho con menos detalle o con otro alcance; lo no pertinente es otro hecho que solo se correlaciona.

## 3. Prueba de derivación (frontera de OQ-56)

Palabras del usuario: «sí» a la propuesta de Claude, tras descartar una condición previa («interpreta o combina, no aporta»).

> Una derivación se admite si su conclusión **no puede ser falsa cuando lo publicado es verdad**, aplicando reglas:
> - **generales:** valen para cualquier oferta (definiciones, lógica, aritmética, hechos generales del mundo). Un hecho particular del producto tomado de fuera (un registro, la web del fabricante, lo que el auditor sepa del modelo) no es una regla y solo sirve para contrastar.
> - **descriptivas:** dicen qué son las cosas. Una norma solo cuenta para fijar el significado de un término («seda», qué exige GOTS), no para dar por hecho que la oferta cumple lo que obliga: la ley dice lo que debe ser, no lo que la oferta es.
> - **citadas con su fuente y sin contrafuente:** si una fuente admisible o la realidad documentada del mercado la contradice, la regla no es necesaria.
>
> Si la información trata la misma cuestión, aunque sea con menos detalle, en general o con otro alcance, no hay derivación: es pertinente y la juzgan los AC.

- La prueba no cuenta pasos: respeta la regla 7 de los AC y la invariante 9.
- Por qué se descartó «interpreta o combina, no aporta»: excluía un «no» fundado sobre otra cuestión («100 % lana» → «¿apto para veganos?» → «no»), contra la neutralidad de respuesta (invariante 13), y obligaba a juzgar si la publicación «trata» la cuestión, que es un juicio de proximidad temática (invariante 10).

Casos (hipotéticos):

| Publicado | Pregunta | Resultado | Por qué |
|---|---|---|---|
| `InStock` | ¿Disponible? | Admitida | Significado del término |
| Talla 42 → SKU-420 → `InStock` | ¿Está la 42? | Admitida | Combina lo publicado |
| Envío gratis desde 50 €; precio 60 € | ¿Envío gratis? | Admitida | Aritmética |
| «Fabricado en Portugal» | ¿Origen UE? | Admitida | Hecho general del mundo |
| «100 % lana» | ¿Apto para veganos? | Admitida: «no» | Definición |
| «Percal» | ¿Ligamento? | Admitida: tafetán | Definición |
| «Percal» | ¿Composición? | No admitida | Contrafuente: la RAE dice algodón, pero se vende percal de poliéster y algodón |
| «Percal 100 % algodón» | ¿Es fresca? | No admitida | No es necesaria (D-090) |
| «Muy vendido» | ¿Hay stock? | No admitida | No es necesaria (PF-07) |
| «Producto nuevo», venta en España | ¿Garantía legal? | No admitida | Regla normativa; además, `gen/12` existe porque la ley obliga a informar (art. 97.1.n) |
| GTIN | ¿Marca? | No admitida | Hecho particular tomado de fuera: solo contrasta |
| «Modelo disponible» | ¿Está la 42? | Pertinente, sin derivación | Misma cuestión con otro alcance; lo juzga Aplicabilidad |

## 4. Fiabilidad

Palabras del usuario: «Para la propiedad de corrección: hay que establecer cómo se evalúa (conocimiento del modelo, estructura del dato, hay que profundizar). Actualidad (quita esta propiedad, no hay forma de evaluarla). Consistencia (se puede evaluar para cada ámbito y a nivel transversal adquiere una nueva dimensión de análisis).» Sobre las propuestas: «1. sí, G1. 2. sí. 3. elige tú. 4. sí. 5. sí.»

### Definición

> La información supera las comprobaciones de corrección y consistencia proporcionadas a su naturaleza: no se acreditan errores ni contradicciones materiales.

Sustituye a «La corrección, actualidad y consistencia de la información están suficientemente sustentadas mediante comprobaciones y evidencias pertinentes».

### Lectura refutadora (G1)

- **2:** supera las comprobaciones que tocan a ese tipo de dato.
- **1:** hay un defecto no material, o uno que afecta solo a parte de lo examinado.
- **0:** hay un defecto material.
- El registro enumera las comprobaciones hechas y el resultado dice «sin defectos detectados en…», nunca «exacto». Respeta la invariante 12: no presenta la ausencia de contradicción como exactitud, dice qué se comprobó.
- Un dato que nada refuta ni confirma recibe el grado que corresponda a las comprobaciones superadas, no NE.
- Se descartó la lectura corroboradora (2 solo con corroboración positiva): trataba la ausencia de corroboración como limitación (invariante 12), funcionaba como un tope (invariante 7) y castigaba al ecommerce por que no exista registro para un tipo de dato.
- Consecuencia asumida: Fiabilidad discrimina cuando hay defectos; la mayoría de los datos estables sin defectos obtendrán 2.

### Tres familias de comprobación

| Familia | Qué comprueba | Ejemplos (hipotéticos) | Qué puede concluir |
|---|---|---|---|
| **Estructura del dato** | Las reglas que el propio dato lleva consigo | Dígito de control del GTIN; composición que suma 100 %; precio final = base − descuento; unidad coherente con la magnitud; valor dentro de una enumeración cerrada (clase energética A–G); fecha de validez ya vencida en la captura | Refutar, con certeza |
| **Conocimiento del dominio** | Reglas generales: definiciones, denominaciones legales, normas que fijan el significado de un término | «Certificado GOTS» en una sábana 100 % poliéster (GOTS exige al menos un 70 % de fibra natural ecológica); «satén de seda» con composición 100 % poliéster (el Reglamento (UE) 1007/2011 reserva «seda» a esa fibra) | Solo refutar |
| **Fuente independiente** | Hechos particulares en registros públicos | Número de certificado en el Label Check de OEKO-TEX; EPREL; GS1 | Refutar o corroborar, solo en algunos tipos de dato |

Límites del conocimiento del dominio («conocimiento del modelo» se lee como el del modelo de IA que audita):

- **Solo refuta.** No puede confirmar un hecho de la oferta.
- **Misma prueba que las derivaciones (punto 3), en su parte de necesidad:** un dato es defecto solo si **no puede** ser verdad según una regla general y descriptiva, citada con su fuente y sin contrafuente. Si solo es improbable, es una sospecha: se anota y no gradúa. Ejemplo: «percal 100 % poliéster» no se refuta, porque existe percal de poliéster. Así, una inferencia por tendencia no puede crear un hecho (D-090) ni destruirlo (Fiabilidad).
- **Regla citada con su fuente** (M10). Si el auditor no puede enunciar la regla y de dónde sale, es una sospecha.
- Las reglas generales son el conocimiento del dominio; los hechos particulares son la fuente independiente. La misma distinción que separa derivación de contraste en el punto 3.

Cuando existe una fuente independiente para un tipo de dato (certificaciones, clase energética, GTIN), consultarla forma parte de las comprobaciones que le tocan.

### Identificador ausente

Decidido por Claude por delegación del usuario («elige tú»): si el ecommerce no da el identificador que permitiría la comprobación externa (p. ej., el número de certificado), **cuenta en Justificación (P18, verificabilidad), no en Fiabilidad**. Motivo: con G1, Fiabilidad gradúa los defectos que encuentran las comprobaciones; la falta del identificador no es un error de corrección, sino la falta de una base para verificar. Así no se cuenta dos veces (EV-13).

### Frontera con la evaluación técnica (invariante 8)

Una propiedad mal escrita o una sintaxis inválida es técnica y solo cuenta por su efecto en la disponibilidad. Una sintaxis válida con un valor imposible (GTIN con dígito de control erróneo) es Fiabilidad.

### Consistencia por ámbito

Dentro de las representaciones de cada ámbito, y cuenta en su GSC de Fiabilidad:

- **Web:** texto, tabla, variantes, y HTML frente a Schema.org.
- **Web Schema.org:** dentro del marcado.
- **Catálogos distribuidos:** dentro del ítem y entre las variantes de un grupo.

## 5. Propiedades: se retira P15 · Actualidad

- **P15 · Actualidad** se retira del catálogo de propiedades. El ID no se reutiliza (como los retirados en D-007).
- Motivo (usuario): «no hay forma de evaluarla».
- Lo detectable sigue cubierto por otras vías: fecha de validez vencida en la captura (estructura del dato); feed desfasado frente a la web (consistencia transversal); «Agotado» visible con `InStock` en el marcado (consistencia dentro de Web). Lo que se pierde es juzgar si un dato sin fecha está al día, que ya no era evaluable (EV-10).
- Asociaciones orientativas de **Fiabilidad**: **P14 y P16**. P18 sale de Fiabilidad y queda en Justificación (consecuencia del identificador ausente).

## 6. Nueva dimensión de análisis: consistencia transversal

Palabras del usuario: «a nivel transversal adquiere una nueva dimensión de análisis»; «5. sí» a la forma T1.

- **Unidad:** RI × par de ámbitos. Es una dimensión de análisis propia, distinta de la valoración RI × ámbito.
- **Forma (T1): hallazgos sin escala.** Por RI y par de ámbitos: hecho, valores, momento, materialidad, y si la diferencia es legítima (p. ej., un precio propio de un canal, declarado). Una diferencia legítima y declarada no es incoherencia.
- **No modifica el GSC de ningún ámbito ni se agrega:** no se puede saber cuál de los dos lados está mal, y mezclarlos rompería la invariante 2 y el caso H (FUND §10.4).
- **Lo que aporta:** lo que el juicio por ámbito no puede expresar. Ejemplo (hipotético): un marcado coherente consigo mismo a 89 € en una página que dice 79 €; quien solo lee el marcado no puede saberlo. Lo mismo, un feed desfasado.
- **Pares:** Catálogos distribuidos ↔ Web; Catálogos distribuidos ↔ Web Schema.org; HTML ↔ Web Schema.org (el mismo hallazgo que ya ve Web, reutilizado, EV-13); entre perfiles de Catálogos distribuidos (Google, Meta).
- **Condiciones de operación:** captura de los ámbitos en un momento comparable; identidad de la entidad entre ámbitos (GTIN, SKU o `item_group_id` frente a URL y variante); acceso al feed.
- Un estado cualitativo por RI (T2: coherente / discrepancia no material / discrepancia material) queda para más adelante; se puede construir sobre T1 sin rehacer nada.

## 7. Pendiente

Palabras del usuario sobre las reglas de AC por requisito: «No sé. Luego vemos.» y «los matices de AC por requisito no solo dependen de PAA. Taxo también puede calibrarlos.»

- **Alcance de las reglas de AC de un requisito (D-115, OQ-61):** si son solo de pertinencia o también orientan la evaluación («si es muy comparable, verificable, etc.», palabras del usuario en D-104). Con el punto 1, unas reglas solo de pertinencia se reducirían al NA de Comparabilidad.
- **Escritores:** taxo (referencias, normativa, fichas reales) además de PAA, frente a la regla «un solo escritor por requisito» de D-115.
- **NA de Comparabilidad.**
- **Qué comprobaciones de corrección tocan a cada tipo de dato** (rasgo × entidad) y qué reglas del dominio, con su fuente, guarda el modelo de demanda.
- **T2** de la consistencia transversal.
