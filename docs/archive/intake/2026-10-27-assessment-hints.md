# Pistas de valoración

Fecha: 2026-10-27. Update descrito por el usuario en la sesión de diseño del sistema de reglas que rige la valoración de los criterios de aceptación. Continúa `INTAKE 2026-10-27-ac-applicability-and-reliability` y resuelve lo que su §7 dejaba pendiente (alcance y escritores de las reglas de AC de un requisito, NA de Comparabilidad). Ortografía de las citas normalizada.

Encargo de partida: «hay un marco general y luego cada requisito fija algún matiz para orientar la evaluación».

## 1. Nombre

Palabras del usuario: «a esto le vamos a llamar "pistas de valoración"».

Las **pistas de valoración** son lo que cada requisito fija para orientar la valoración de sus criterios de aceptación. Sustituyen a lo que D-115 llamaba «reglas de AC de un requisito».

## 2. Prueba con requisitos reales y reparto por niveles

Claude probó la hipótesis de tres niveles (marco general, tipo de requisito, requisito) con nueve requisitos del catálogo que aplican a unas sábanas: composición (`cat.ropa-de-casa/01`), gramaje (`cat.ropa-de-casa/05`), número de hilos (`cat.sabanas/03`), tamaño de cama (`cat.ropa-de-cama/01`), certificación de sustancias nocivas (`cat.ropa-de-casa/03`), precio (`gen/04`), variantes disponibles (`gen.variantes/02`), garantía legal (`gen/12`) e identificadores (`gen/03`). Para cada uno y cada AC anotó qué tendría que mirar el auditor que no diga ya el marco general, y de dónde saldría.

Resultado (usuario: «todo es OK»):

| AC | Dónde se concreta | Ejemplos de la prueba |
|---|---|---|
| **Concreción** | Ya está en el catálogo: componentes de la información resolutiva | Fibras y porcentajes, composición de cada parte; hilo simple o de varios cabos; estado de cada variante |
| **Justificación** | Marco general | La base es la declaración del vendedor o una derivación reconstruible. En certificaciones, el número de certificado sale del tipo |
| **Aplicabilidad** | Tipo (entidad) | Variante: estado y GTIN de cada talla. Juego de piezas: composición de cada pieza. Oferta: precio de cada variante |
| **Fiabilidad** | Tipo (rasgo × entidad) | Identidad: dígito de control y GS1. Certificación: registro y clases válidas. Material: la composición suma 100 % y usa las denominaciones legales. Oferta: aritmética del precio. Tamaño de cama coherente con las medidas de la pieza |
| **Precisión** | Requisito (las unidades de las magnitudes, por tipo) | Qué términos son ambiguos y qué los fija: «microfibra» no es una fibra; «144 hilos» sin superficie ni cabos; «Queen» o «full»; «OEKO-TEX» sin decir qué norma; «garantía de 3 años» sin decir si es legal o comercial |
| **Comparabilidad** | Requisito | Si es una dimensión de comparación y sobre qué base: composición (fibra y % en peso), hilos (misma superficie, hilo simple), gramaje (g/m²), precio (total) |

Decisiones:

- **Tres niveles.** Marco general para todos los AC; **tipo de requisito** (rasgo × entidad) para Aplicabilidad y Fiabilidad; **requisito** para Precisión y Comparabilidad. Concreción y Justificación no necesitan pistas nuevas.
- **Alcance:** las pistas dicen **qué mirar**, no cuánto pesa cada criterio. El peso de cada criterio en un requisito es de la síntesis del IR (OQ-28).
- La prueba mostró además una comprobación de **consistencia entre requisitos del mismo ámbito** (una bajera de 90 × 190 en una ficha que dice «cama de 150»). Es consistencia por ámbito (P16) y sale del tipo.

## 3. NA de Comparabilidad

Usuario: «sí» a «marcamos "no se compara" en los requisitos que no se usan para comparar».

- El requisito lleva una **marca de dimensión de comparación** (sí / no) en el modelo de demanda. Si no lo es, **Comparabilidad es NA** en ese requisito. Lo decide el modelo, no el auditor.
- Ejemplos de la prueba que no son dimensiones de comparación: tamaño de cama (es un filtro: primero se elige el tamaño y luego se compara), variantes disponibles, garantía legal (es la misma para todos), identificadores (sirven para emparejar ofertas, no para compararlas).
- Motivo: valorar Comparabilidad en esos requisitos daría un 2 automático o repetiría lo que ya mira Precisión.

## 4. Quién escribe las pistas

Usuario: «sí» a «taxo y PAA escriben las pistas».

- **Pistas por tipo:** una tabla de reglas por rasgo × entidad, como la de importancia, que compila el entrenamiento.
- **Pistas por requisito:** las escriben **taxo** (desde las referencias, la normativa que es fuente del requisito y la justificación del requisito) y **PAA** (desde sus preguntas).
- Cada pista lleva su **origen**. Las pistas **se suman y nunca se quitan**.
- No choca con «un solo escritor por requisito» (D-115): esa regla protege la estructura del requisito (separar, partir, sacar). La información resolutiva ya admite aportaciones de varios orígenes y PAA ya añade aportaciones aditivas.

## 5. Las pistas son criterios, no listas

Palabras del usuario: «aunque sean matices por requisito debemos intentar siempre trabajar con reglas y/o criterios, no deben ser comparaciones deterministas. Esto no sería una práctica correcta: "una lista de vocabulario admitido"». Sobre el planteamiento de Claude: «Sí, lo único es evitar ser demasiado verboso. Las pistas deben ser breves pero suficientemente claras.»

- Una pista es un **criterio que el auditor aplica razonando**, no una lista contra la que se compara palabra por palabra. Ejemplo: no «términos ambiguos: microfibra, 144 hilos, Queen», sino «un recuento de hilos solo es claro si dice sobre qué superficie se cuenta y si cuenta hilos simples o de varios cabos», que sirve también para «300 TC» o para cualquier forma nueva.
- Cada pista es **breve pero suficientemente clara**, y dice su porqué.
- Los **ejemplos solo ilustran, nunca cierran**: el auditor juzga también lo que no aparece en ellos.
- Las **fuentes justifican la pista**, no son lo que se busca. Si una norma fija una lista cerrada (los nombres de fibras del Reglamento (UE) 1007/2011), la pista es «usa la denominación legal» y la norma se cita como fuente; no se copia la lista.
- El entrenamiento **rechaza las pistas que sean una lista o una frase exacta** y las reformula como criterio.
- Las comprobaciones de estructura del dato (dígito de control, suma de porcentajes) son cálculos exactos, pero son reglas generales que valen para cualquier dato, no listas de vocabulario: encajan.

## 6. Las pistas se apoyan en las propiedades

Usuario: «¿Estás teniendo en cuenta que para valorar los AC lo que se estudia son las propiedades de calidad, verdad?». Claude propuso que cada pista nombre la propiedad que observa y los AC a los que afecta. Usuario: «sí».

- Cada pista dice **qué propiedad hay que observar** y **a qué AC afecta**. Respeta la cadena del canon: lo observado → la propiedad afectada → la consecuencia para el AC → el GSC.
- Una sola pista puede servir a varios AC sin repetirse.
- Las pistas **orientan qué observar; nunca puntúan propiedades** (invariante 5).

Ejemplos (hipotéticos):

| Pista | Propiedad | AC afectados |
|---|---|---|
| El recuento de hilos dice sobre qué superficie se cuenta y si cuenta cabos. | P13 Normalización | Precisión, Comparabilidad |
| La composición se da con nombres de fibra, no de tejido ni de acabado. | P09 Claridad | Precisión |
| El estado se da por cada variante. | P11 Identificabilidad | Aplicabilidad |
| El tamaño de cama encaja con las medidas de la pieza. | P16 Coherencia | Fiabilidad |

## 7. Pendiente

- Formato de las pistas en el catálogo y de la tabla por tipo; cómo las usa la auditoría (perfil del RI).
- Cómo se fija la marca de dimensión de comparación: valor por defecto y qué prueba la establece.
- Contenido de la tabla por tipo (sigue en OQ-66 para las comprobaciones de corrección).
