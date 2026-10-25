# Marco humano y reglas inducidas en el entrenamiento

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad (tarea T-016). Lo forman dos mensajes del usuario y el diagrama de flujo «Flujo del motor de demanda» (https://claude.ai/artifact/74invDRN6mqd28sU6fgKtN), que el usuario aprobó con «documenta». La ortografía de los mensajes está normalizada.*

## Mensaje 1 del usuario

«No voy a revisarlo manualmente. Debe haber un sistema de reglas para determinar la categoría de importancia relativa. A lo sumo reviso esas reglas. El sistema debe basarse en reglas o en configuraciones específicas. La parametrización específica puede formar parte del sistema, pero como un resultado compilado, no como un diseño específico. El entrenamiento es para definir los parámetros sobre los patrones usados en el entrenamiento. Pueden salir reglas generales y reglas específicas.»

## Mensaje 2 del usuario

«Tampoco quiero revisar cada regla. Lo que defino es el marco general, objetivos, características del resultado, etc. Las reglas concretas deben ser producto del entrenamiento también.»

## Diagrama aprobado

### Marco que define el usuario (única intervención humana)

- **Propósito:** establecer los requisitos informativos de una oferta.
- **Objetivos y características del resultado:** identidad por bloques, especificidad necesaria, críticos pocos, nada de conjeturas.
- **Criterios de éxito:** cobertura de cuestiones, estabilidad entre ejecuciones, coherencia de la importancia.
- **Invariantes del canon** (D-020 a D-043): lo que ninguna regla puede violar.

El usuario no revisa requisitos, bloques ni reglas sueltas: lee el informe agregado del entrenamiento y, si hace falta, ajusta el marco.

### Entrenamiento (periódico)

1. **Reunir los casos:** el conjunto de entrenamiento más lo acumulado en la cola de pendientes.
2. **Aplicar las reglas vigentes:** dos veces por caso.
3. **Medir contra el marco.**
4. **Detectar patrones:** agrupar divergencias e inestabilidades por rasgos comunes.
5. **Inducir reglas:** reglas generales, y específicas donde la general falla, para cada decisión del procedimiento:
   - composición;
   - especializaciones;
   - relevancia de las propiedades de Amazon;
   - cuestiones inferidas;
   - importancia: rasgos del requisito → crítico, principal o complementario.
6. **Compilar el catálogo:** generador determinista de bloques y, encima, las reglas inducidas. Cada requisito guarda la regla que lo decidió.
7. **Validar automáticamente:** se aceptan si mejoran las métricas y no violan el marco; si no, se descartan.
8. **Publicar versión e informe agregado:** métricas, reglas añadidas o retiradas y sus efectos. El usuario lee el informe, no las reglas.

### Ejecución (por producto, automática)

1. Congelar la ficha.
2. Leer lo declarado.
3. Componer la clase.
4. **Seleccionar los bloques:**
   - categoría compilada → se usan sus bloques;
   - categoría nueva → se genera y compila al vuelo, marcada «no revisada», y se encola.
5. Especializaciones.
6. **Cuestiones inferidas:** añadido provisional fuera de la clave, encolado.
7. **Importancia:** la traen los bloques compilados; lo nuevo la recibe de las reglas de importancia.
8. Aplicación.
9. Denominación.
10. **Modelo de demanda:** incluye la lista de lo usado sin compilar.

### Conexiones

- El entrenamiento publica reglas y catálogo compilados, que la ejecución solo lee.
- La ejecución deja en la cola todo lo que usó sin compilar, y el entrenamiento lo convierte en casos y reglas.
- El marco fija qué cuenta como buen resultado, y el entrenamiento solo acepta reglas que lo cumplen.

### Principios

- **Identidad por bloques.**
- **Reglas inducidas, no escritas:** las reglas concretas, generales y específicas, salen del entrenamiento; el humano define el marco.
- **Catálogo como resultado:** ningún bloque ni importancia se diseña a mano; se compila desde referencias y reglas, y se regenera.
- **Ejecución sin esperas.**
- **Trazabilidad:** cada requisito dice de dónde sale y qué regla decidió su importancia.
- **Referencias fijadas.**

## Nota de Claude

Esto obliga a reformular D-041, que decía que en entrenamiento el usuario revisa bloques, inferidas e importancias, y D-036, que decía que el usuario valida siempre las críticas. El usuario define el marco, y las reglas se inducen y se validan solas contra él.
