# Informe del entrenamiento · reglas 6 · tanda de control T-032 · 2026-10-26

Ejecuciones: var/runs/2026-10-26-v6-a, var/runs/2026-10-26-v6-b.

## Métricas

### Cobertura en el conjunto de control

| Ejecución | Casos | Composición | Especializaciones | Cuestiones clave | Aplicación | Inferida esperada |
|---|---|---|---|---|---|---|
| 2026-10-26-v6-a | 14 | 13/14 | 6/14 | 27/40 (68 %) | 5/6 | 0/2 |
| 2026-10-26-v6-b | 14 | 14/14 | 6/14 | 26/40 (65 %) | 6/6 | 0/2 |

### Cobertura por hechos declarados

| Ejecución | Hechos que cuentan | Sin pregunta en el modelo |
|---|---|---|
| 2026-10-26-v6-a | 653 | 32 |
| 2026-10-26-v6-b | 684 | 34 |

### Estabilidad entre ejecuciones

| Medida | Resultado |
|---|---|
| Composición (categorías y alias) | 13/14 |
| Clave del modelo | 14/14 |
| Especializaciones | 14/14 |
| Aplicación de la oferta | 8/14 |
| Importancia en los requisitos de categoría comunes | 359/359 |

### Coherencia

Requisitos con el mismo rasgo y la misma clase e importancia distinta (lo que deciden las reglas por rasgo; una excepción por requisito no cuenta): 0 en el catálogo (440 requisitos) y 2 en los modelos.

Coherencia por requisito: 46 de 358 pares de requisito de categoría y clase tienen una mayoría clara de votos contra su importancia.

## Reglas de importancia

272 reglas: 133 generales, 36 específicas, 103 excepciones por requisito y clase. Etiquetas del catálogo: 440; votos: 2025.
Aceptada porque mejora: coherencia por requisito: 18 → 17; requisitos del catálogo sin regla: 7 → 0.

### Por rasgo

| Regla | Rasgo | Clase | Importancia | Tipo | Requisitos del catálogo que decide |
|---|---|---|---|---|---|
| `imp:certificacion-origen@fb` | certificacion-origen | Alimentación, bebida y tabaco (fb) | complementario | general | 2 |
| `imp:certificacion-origen@hg` | certificacion-origen | Casa y jardín (hg) | complementario | general | 2 |
| `imp:certificacion-origen@aa-8` | certificacion-origen | Calzado (aa-8) | complementario | general | 1 |
| `imp:certificacion-origen@bt-3-3` | certificacion-origen | Clips y fundas para chupetes (bt-3-3) | complementario | general | 1 |
| `imp:certificacion-origen@vp-1-5-5-8` | certificacion-origen | Aceite para motores de vehículos (vp-1-5-5-8) | principal | general | 1 |
| `imp:construccion@lb` | construccion | Maletas y bolsos de viaje (lb) | complementario | general | 10 |
| `imp:construccion@aa-8` | construccion | Calzado (aa-8) | complementario | general | 2 |
| `imp:construccion@fr-22` | construccion | Sofás (fr-22) | complementario | general | 5 |
| `imp:construccion@ha-15` | construccion | Herramientas (ha-15) | principal | general (sube desde las hijas) | 2 |
| `imp:construccion@me-3` | construccion | Música y grabaciones (me-3) | complementario | general (sube desde las hijas) | 4 |
| `imp:construccion@aa-6-2` | construccion | Joyas para piercings (aa-6-2) | principal | general | 1 |
| `imp:construccion@aa-8-3` | construccion | Botas (aa-8-3) | principal | específica | 1 |
| `imp:construccion@ap-2-9` | construccion | Camas para mascotas (ap-2-9) | complementario | general | 2 |
| `imp:construccion@bt-3-3` | construccion | Clips y fundas para chupetes (bt-3-3) | principal | general | 1 |
| `imp:construccion@fb-2-7` | construccion | Salsas y cremas para untar (fb-2-7) | complementario | general | 2 |
| `imp:construccion@hg-11-3` | construccion | Objetos para llevar comida y bebida (hg-11-3) | principal | general | 2 |
| `imp:construccion@hg-15-4` | construccion | Toallas (hg-15-4) | principal | general | 2 |
| `imp:construccion@hg-3-64` | construccion | Cojines (hg-3-64) | principal | general | 1 |
| `imp:construccion@aa-8-11-5` | construccion | Zapatillas para bebés y niños (aa-8-11-5) | principal | específica | 1 |
| `imp:construccion@ap-2-3-7` | construccion | Juguetes para perros (ap-2-3-7) | complementario | general | 1 |
| `imp:construccion@ap-2-9-4` | construccion | Camas de enfriamiento (ap-2-9-4) | principal | específica | 1 |
| `imp:construccion@hg-11-3-11` | construccion | Botellas de agua (hg-11-3-11) | complementario | específica | 1 |
| `imp:construccion@hg-15-1-2` | construccion | Sábanas (hg-15-1-2) | principal | general | 3 |
| `imp:construccion@hg-15-1-4` | construccion | Mantas (hg-15-1-4) | principal | general | 1 |
| `imp:construccion@hg-15-1-5` | construccion | Fundas de nórdico (hg-15-1-5) | principal | general | 2 |
| `imp:construccion@hg-15-1-6` | construccion | Protectores para colchones (hg-15-1-6) | principal | general | 2 |
| `imp:construccion@hg-15-1-8` | construccion | Fundas de almohada y de cojines (hg-15-1-8) | complementario | general | 2 |
| `imp:construccion@hg-11-10-7-11` | construccion | Soperas (hg-11-10-7-11) | complementario | general | 1 |
| `imp:construccion@hg-15-1-6-2` | construccion | Cubrecolchones (hg-15-1-6-2) | complementario | específica | 2 |
| `imp:contenido@fr-22` | contenido | Sofás (fr-22) | principal | general | 2 |
| `imp:contenido@me-3` | contenido | Música y grabaciones (me-3) | principal | general (sube desde las hijas) | 4 |
| `imp:contenido@bt-3-3` | contenido | Clips y fundas para chupetes (bt-3-3) | principal | general | 0 |
| `imp:contenido@lb-1-12` | contenido | Mochilas escolares (lb-1-12) | principal | general | 0 |
| `imp:contenido@ap-2-3-3` | contenido | Comida para perros (ap-2-3-3) | complementario | general | 1 |
| `imp:contenido@hg-15-1-2` | contenido | Sábanas (hg-15-1-2) | principal | general (sube desde las hijas) | 0 |
| `imp:contenido@hg-15-1-5` | contenido | Fundas de nórdico (hg-15-1-5) | principal | general | 0 |
| `imp:contenido@hg-15-4-5` | contenido | Toallas de mano (hg-15-4-5) | principal | general | 0 |
| `imp:contenido@hg-15-1-8-2` | contenido | Fundas de almohada (hg-15-1-8-2) | principal | general | 1 |
| `imp:contenido@hg-15-4-1-1` | contenido | Toallas de baño (hg-15-4-1-1) | principal | general | 0 |
| `imp:cuidado@aa` | cuidado | Ropa y accesorios (aa) | complementario | general (sube desde las hijas) | 2 |
| `imp:cuidado@fr` | cuidado | Mobiliario (fr) | complementario | general | 2 |
| `imp:cuidado@lb` | cuidado | Maletas y bolsos de viaje (lb) | complementario | general | 1 |
| `imp:cuidado@fb-2` | cuidado | Alimentos (fb-2) | complementario | general | 2 |
| `imp:cuidado@hg-11` | cuidado | Cocina y comedor (hg-11) | principal | general | 1 |
| `imp:cuidado@hg-15` | cuidado | Ropa de casa (hg-15) | complementario | general | 2 |
| `imp:cuidado@hg-3` | cuidado | Decoración (hg-3) | complementario | general | 1 |
| `imp:cuidado@aa-8-7` | cuidado | Pantuflas (aa-8-7) | principal | específica | 0 |
| `imp:cuidado@ap-2-3` | cuidado | Productos para perros (ap-2-3) | complementario | general (sube desde las hijas) | 3 |
| `imp:cuidado@ap-2-9` | cuidado | Camas para mascotas (ap-2-9) | principal | general | 1 |
| `imp:cuidado@bt-3-3` | cuidado | Clips y fundas para chupetes (bt-3-3) | principal | general | 1 |
| `imp:cuidado@hg-3-64` | cuidado | Cojines (hg-3-64) | principal | específica | 0 |
| `imp:cuidado@hg-15-1-4` | cuidado | Mantas (hg-15-1-4) | principal | específica | 0 |
| `imp:estetica@aa` | estetica | Ropa y accesorios (aa) | principal | general | 2 |
| `imp:estetica@fr` | estetica | Mobiliario (fr) | principal | general | 2 |
| `imp:estetica@ha` | estetica | Bricolaje (ha) | complementario | general | 2 |
| `imp:estetica@hg` | estetica | Casa y jardín (hg) | principal | general | 2 |
| `imp:estetica@lb` | estetica | Maletas y bolsos de viaje (lb) | complementario | general | 2 |
| `imp:estetica@aa-8` | estetica | Calzado (aa-8) | complementario | específica | 1 |
| `imp:estetica@ap-2` | estetica | Productos para mascotas (ap-2) | complementario | general | 2 |
| `imp:estetica@fr-22` | estetica | Sofás (fr-22) | complementario | específica | 4 |
| `imp:estetica@bt-3-3` | estetica | Clips y fundas para chupetes (bt-3-3) | complementario | general | 2 |
| `imp:estetica@lb-1-12` | estetica | Mochilas escolares (lb-1-12) | principal | específica | 0 |
| `imp:estetica@me-3-4` | estetica | Álbumes y LP (me-3-4) | complementario | general | 1 |
| `imp:estetica@vp-1-5` | estetica | Mantenimiento, cuidado y decoración de vehículos (vp-1-5) | complementario | general | 2 |
| `imp:estetica@hg-11-3-11` | estetica | Botellas de agua (hg-11-3-11) | complementario | específica | 1 |
| `imp:estetica@hg-15-1-6-2` | estetica | Cubrecolchones (hg-15-1-6-2) | complementario | específica | 0 |
| `imp:identidad@aa-6` | identidad | Joyería (aa-6) | principal | general | 1 |
| `imp:identidad@ap-2` | identidad | Productos para mascotas (ap-2) | principal | general (sube desde las hijas) | 6 |
| `imp:identidad@fb-2` | identidad | Alimentos (fb-2) | principal | general | 2 |
| `imp:identidad@fr-22` | identidad | Sofás (fr-22) | principal | general | 1 |
| `imp:identidad@ha-15` | identidad | Herramientas (ha-15) | principal | general (sube desde las hijas) | 4 |
| `imp:identidad@me-3` | identidad | Música y grabaciones (me-3) | principal | general | 9 |
| `imp:identidad@vp-1` | identidad | Piezas y accesorios para vehículos (vp-1) | complementario | general | 1 |
| `imp:identidad@aa-8-3` | identidad | Botas (aa-8-3) | principal | general | 1 |
| `imp:identidad@aa-8-7` | identidad | Pantuflas (aa-8-7) | principal | general | 1 |
| `imp:identidad@hg-15-4` | identidad | Toallas (hg-15-4) | principal | general | 1 |
| `imp:identidad@hg-3-64` | identidad | Cojines (hg-3-64) | principal | general | 1 |
| `imp:identidad@aa-8-11-5` | identidad | Zapatillas para bebés y niños (aa-8-11-5) | principal | general | 1 |
| `imp:identidad@hg-11-10-7` | identidad | Utensilios de servir (hg-11-10-7) | principal | general | 1 |
| `imp:identidad@hg-15-1-4` | identidad | Mantas (hg-15-1-4) | principal | general | 1 |
| `imp:identidad@hg-11-10-7-11` | identidad | Soperas (hg-11-10-7-11) | complementario | específica | 0 |
| `imp:magnitud@lb` | magnitud | Maletas y bolsos de viaje (lb) | principal | general (sube desde las hijas) | 2 |
| `imp:magnitud@aa-8` | magnitud | Calzado (aa-8) | complementario | general | 1 |
| `imp:magnitud@ha-15` | magnitud | Herramientas (ha-15) | complementario | general (sube desde las hijas) | 2 |
| `imp:magnitud@hg-15` | magnitud | Ropa de casa (hg-15) | principal | general | 1 |
| `imp:magnitud@aa-6-2` | magnitud | Joyas para piercings (aa-6-2) | complementario | general | 2 |
| `imp:magnitud@ap-2-9` | magnitud | Camas para mascotas (ap-2-9) | complementario | general | 1 |
| `imp:magnitud@fr-22-7` | magnitud | Sofás cama (fr-22-7) | principal | general | 1 |
| `imp:magnitud@me-3-4` | magnitud | Álbumes y LP (me-3-4) | complementario | general | 1 |
| `imp:magnitud@ap-2-3-7` | magnitud | Juguetes para perros (ap-2-3-7) | complementario | general | 1 |
| `imp:magnitud@ha-15-59-3` | magnitud | Lijadoras orbitales (ha-15-59-3) | principal | específica | 0 |
| `imp:magnitud@hg-11-3-11` | magnitud | Botellas de agua (hg-11-3-11) | complementario | general | 1 |
| `imp:magnitud@hg-15-1-5` | magnitud | Fundas de nórdico (hg-15-1-5) | complementario | específica | 0 |
| `imp:magnitud@hg-11-10-7-11` | magnitud | Soperas (hg-11-10-7-11) | complementario | general | 1 |
| `imp:magnitud@hg-15-1-2-1` | magnitud | Sábanas ajustables (hg-15-1-2-1) | complementario | específica | 0 |
| `imp:magnitud@hg-15-1-4-2` | magnitud | Mantas decorativas (hg-15-1-4-2) | complementario | específica | 0 |
| `imp:magnitud@hg-15-1-6-2` | magnitud | Cubrecolchones (hg-15-1-6-2) | complementario | específica | 1 |
| `imp:magnitud@hg-15-1-8-2` | magnitud | Fundas de almohada (hg-15-1-8-2) | complementario | específica | 0 |
| `imp:material@hg` | material | Casa y jardín (hg) | principal | general (sube desde las hijas) | 5 |
| `imp:material@aa-6` | material | Joyería (aa-6) | principal | general | 6 |
| `imp:material@aa-8` | material | Calzado (aa-8) | complementario | general | 9 |
| `imp:material@ap-2` | material | Productos para mascotas (ap-2) | principal | general (sube desde las hijas) | 10 |
| `imp:material@fb-2` | material | Alimentos (fb-2) | principal | general | 6 |
| `imp:material@fr-22` | material | Sofás (fr-22) | principal | general | 5 |
| `imp:material@lb-1` | material | Mochilas (lb-1) | complementario | general | 4 |
| `imp:material@lb-6` | material | Bolsas de deporte (lb-6) | principal | general | 1 |
| `imp:material@vp-1` | material | Piezas y accesorios para vehículos (vp-1) | complementario | general | 1 |
| `imp:material@aa-8-3` | material | Botas (aa-8-3) | principal | específica | 2 |
| `imp:material@bt-3-3` | material | Clips y fundas para chupetes (bt-3-3) | principal | general | 1 |
| `imp:material@ha-15-59` | material | Lijadoras (ha-15-59) | complementario | general | 1 |
| `imp:material@ha-15-60` | material | Bloques de lija (ha-15-60) | principal | general | 1 |
| `imp:material@hg-11-3` | material | Objetos para llevar comida y bebida (hg-11-3) | complementario | específica | 1 |
| `imp:material@hg-15-1-4` | material | Mantas (hg-15-1-4) | complementario | específica | 1 |
| `imp:material@ap-2-3-3-1` | material | Comida para perros sin prescripción médica (ap-2-3-3-1) | complementario | específica | 0 |
| `imp:material@hg-15-1-4-2` | material | Mantas decorativas (hg-15-1-4-2) | principal | específica | 0 |
| `imp:material@vp-1-5-5-8` | material | Aceite para motores de vehículos (vp-1-5-5-8) | principal | específica | 0 |
| `imp:material@vp-1-5-5-8-4` | material | Aceite de motor sintético (vp-1-5-5-8-4) | complementario | específica | 1 |
| `imp:prestacion@lb` | prestacion | Maletas y bolsos de viaje (lb) | complementario | general (sube desde las hijas) | 10 |
| `imp:prestacion@aa-8` | prestacion | Calzado (aa-8) | complementario | general | 13 |
| `imp:prestacion@fr-22` | prestacion | Sofás (fr-22) | complementario | general | 5 |
| `imp:prestacion@ha-15` | prestacion | Herramientas (ha-15) | principal | general (sube desde las hijas) | 6 |
| `imp:prestacion@vp-1` | prestacion | Piezas y accesorios para vehículos (vp-1) | complementario | general | 3 |
| `imp:prestacion@ap-2-9` | prestacion | Camas para mascotas (ap-2-9) | principal | general | 5 |
| `imp:prestacion@hg-15-4` | prestacion | Toallas (hg-15-4) | complementario | general | 4 |
| `imp:prestacion@hg-3-64` | prestacion | Cojines (hg-3-64) | complementario | general | 4 |
| `imp:prestacion@ap-2-3-7` | prestacion | Juguetes para perros (ap-2-3-7) | complementario | general | 2 |
| `imp:prestacion@hg-11-3-11` | prestacion | Botellas de agua (hg-11-3-11) | principal | general | 2 |
| `imp:prestacion@hg-15-1-2` | prestacion | Sábanas (hg-15-1-2) | principal | general (sube desde las hijas) | 0 |
| `imp:prestacion@hg-15-1-4` | prestacion | Mantas (hg-15-1-4) | complementario | general | 2 |
| `imp:prestacion@hg-15-1-6` | prestacion | Protectores para colchones (hg-15-1-6) | principal | general | 5 |
| `imp:prestacion@hg-11-10-7-11` | prestacion | Soperas (hg-11-10-7-11) | complementario | general | 2 |
| `imp:prestacion@hg-15-1-8-2` | prestacion | Fundas de almohada (hg-15-1-8-2) | complementario | general | 3 |
| `imp:seguridad@me` | seguridad | Multimedia (me) | complementario | general | 1 |
| `imp:seguridad@fb-2` | seguridad | Alimentos (fb-2) | principal | general | 2 |
| `imp:seguridad@fr-22` | seguridad | Sofás (fr-22) | complementario | general | 2 |
| `imp:seguridad@hg-15` | seguridad | Ropa de casa (hg-15) | complementario | general | 2 |
| `imp:seguridad@aa-6-2` | seguridad | Joyas para piercings (aa-6-2) | principal | general | 1 |
| `imp:seguridad@bt-3-3` | seguridad | Clips y fundas para chupetes (bt-3-3) | principal | general | 1 |
| `imp:seguridad@ha-15-59` | seguridad | Lijadoras (ha-15-59) | complementario | general | 1 |
| `imp:seguridad@hg-11-3` | seguridad | Objetos para llevar comida y bebida (hg-11-3) | principal | general | 1 |
| `imp:seguridad@hg-3-64` | seguridad | Cojines (hg-3-64) | complementario | general | 1 |
| `imp:seguridad@ap-2-3-7` | seguridad | Juguetes para perros (ap-2-3-7) | principal | general | 1 |
| `imp:seguridad@ap-2-9-4` | seguridad | Camas de enfriamiento (ap-2-9-4) | principal | general | 1 |
| `imp:seguridad@hg-11-10-7-11` | seguridad | Soperas (hg-11-10-7-11) | principal | general | 1 |
| `imp:uso@aa` | uso | Ropa y accesorios (aa) | principal | general | 9 |
| `imp:uso@lb` | uso | Maletas y bolsos de viaje (lb) | principal | general | 4 |
| `imp:uso@aa-6` | uso | Joyería (aa-6) | complementario | específica | 1 |
| `imp:uso@ap-2` | uso | Productos para mascotas (ap-2) | principal | general | 8 |
| `imp:uso@bt-3` | uso | Salud del bebé (bt-3) | principal | general | 2 |
| `imp:uso@fb-2` | uso | Alimentos (fb-2) | principal | general | 1 |
| `imp:uso@fr-22` | uso | Sofás (fr-22) | complementario | general | 2 |
| `imp:uso@ha-15` | uso | Herramientas (ha-15) | principal | general (sube desde las hijas) | 6 |
| `imp:uso@vp-1` | uso | Piezas y accesorios para vehículos (vp-1) | principal | general | 3 |
| `imp:uso@fr-22-7` | uso | Sofás cama (fr-22-7) | principal | específica | 1 |
| `imp:uso@hg-11-10` | uso | Utensilios de mesa (hg-11-10) | principal | general | 1 |
| `imp:uso@hg-3-64` | uso | Cojines (hg-3-64) | complementario | general | 1 |
| `imp:uso@lb-1-12` | uso | Mochilas escolares (lb-1-12) | complementario | específica | 1 |
| `imp:uso@lb-1-16` | uso | Mochilas para computadora portátil (lb-1-16) | complementario | específica | 2 |
| `imp:uso@me-3-3` | uso | CD de música (me-3-3) | complementario | general | 2 |
| `imp:uso@me-3-4` | uso | Álbumes y LP (me-3-4) | principal | general | 1 |
| `imp:uso@aa-8-11-5` | uso | Zapatillas para bebés y niños (aa-8-11-5) | complementario | específica | 3 |
| `imp:uso@ap-2-3-7` | uso | Juguetes para perros (ap-2-3-7) | complementario | específica | 3 |
| `imp:uso@fb-2-7-6` | uso | Confituras y gelatinas (fb-2-7-6) | complementario | específica | 1 |
| `imp:uso@hg-11-3-11` | uso | Botellas de agua (hg-11-3-11) | complementario | general | 3 |
| `imp:uso@hg-15-1-4` | uso | Mantas (hg-15-1-4) | complementario | general | 2 |
| `imp:uso@hg-15-1-6` | uso | Protectores para colchones (hg-15-1-6) | principal | general | 1 |
| `imp:uso@hg-11-10-7-11` | uso | Soperas (hg-11-10-7-11) | complementario | específica | 3 |
| `imp:uso@hg-15-1-2-1` | uso | Sábanas ajustables (hg-15-1-2-1) | principal | general | 1 |
| `imp:uso@hg-15-1-6-2` | uso | Cubrecolchones (hg-15-1-6-2) | complementario | específica | 1 |

Reglas del marco: `marco:D-043.1/medida-descriptiva` (29), `marco:D-043.1/medida-que-fija` (11), `marco:D-043.6/composicion-textil` (3) · requisitos sin regla: 0.

### Excepciones por requisito y clase

103 excepciones, 10 de crítico. Votos de la clase, con el del catálogo como voto de partida.

| Regla | Requisito | Rasgo | Clase | Importancia | Votos |
|---|---|---|---|---|---|
| `imp:cat.aceite-para-motores-de-vehiculos/01@vp-1-5-5-8` | cat.aceite-para-motores-de-vehiculos/01 | prestacion | Aceite para motores de vehículos (vp-1-5-5-8) | crítico | crítico 3, principal 2 |
| `imp:cat.alimentos/06@fb-2-7-6` | cat.alimentos/06 | material | Confituras y gelatinas (fb-2-7-6) | crítico | crítico 6, principal 1 |
| `imp:cat.alimentos/07@fb-2-7-6` | cat.alimentos/07 | identidad | Confituras y gelatinas (fb-2-7-6) | complementario | complementario 6, principal 1 |
| `imp:cat.alimentos/09@fb-2-7-6` | cat.alimentos/09 | material | Confituras y gelatinas (fb-2-7-6) | complementario | complementario 4, principal 3 |
| `imp:cat.alimentos/10@fb-2-7-6` | cat.alimentos/10 | material | Confituras y gelatinas (fb-2-7-6) | complementario | complementario 6, principal 1 |
| `imp:cat.alimentos/13@fb-2-7-6` | cat.alimentos/13 | seguridad | Confituras y gelatinas (fb-2-7-6) | complementario | complementario 7 |
| `imp:cat.bloques-de-lija/08@ha-15-60` | cat.bloques-de-lija/08 | uso | Bloques de lija (ha-15-60) | complementario | complementario 2, principal 1 |
| `imp:cat.bolsas-de-viaje-y-deporte/07@lb-6` | cat.bolsas-de-viaje-y-deporte/07 | construccion | Bolsas de deporte (lb-6) | principal | principal 6, complementario 1 |
| `imp:cat.bolsas-de-viaje-y-deporte/08@lb-6` | cat.bolsas-de-viaje-y-deporte/08 | construccion | Bolsas de deporte (lb-6) | principal | principal 7 |
| `imp:cat.bolsas-de-viaje-y-deporte/14@lb-6` | cat.bolsas-de-viaje-y-deporte/14 | uso | Bolsas de deporte (lb-6) | complementario | complementario 7 |
| `imp:cat.botas/05@aa-8-3` | cat.botas/05 | construccion | Botas (aa-8-3) | complementario | complementario 3 |
| `imp:cat.botas/06@aa-8-3` | cat.botas/06 | material | Botas (aa-8-3) | complementario | complementario 3 |
| `imp:cat.botellas-de-agua/02@hg-11-3-11` | cat.botellas-de-agua/02 | construccion | Botellas de agua (hg-11-3-11) | principal | principal 7 |
| `imp:cat.botellas-de-agua/04@hg-11-3-11` | cat.botellas-de-agua/04 | construccion | Botellas de agua (hg-11-3-11) | principal | principal 7 |
| `imp:cat.botellas-de-agua/11@hg-11-3-11` | cat.botellas-de-agua/11 | prestacion | Botellas de agua (hg-11-3-11) | complementario | complementario 7 |
| `imp:cat.calzado/02@aa-8-7` | cat.calzado/02 | uso | Pantuflas (aa-8-7) | complementario | complementario 2, principal 1 |
| `imp:cat.calzado/03@aa-8-11-5` | cat.calzado/03 | uso | Zapatillas para bebés y niños (aa-8-11-5) | principal | principal 7 |
| `imp:cat.calzado/04@aa-8-7` | cat.calzado/04 | material | Pantuflas (aa-8-7) | principal | principal 3 |
| `imp:cat.calzado/04@aa-8-11-5` | cat.calzado/04 | material | Zapatillas para bebés y niños (aa-8-11-5) | principal | principal 7 |
| `imp:cat.calzado/07@aa-8-3` | cat.calzado/07 | material | Botas (aa-8-3) | complementario | complementario 3 |
| `imp:cat.calzado/08@aa-8-7` | cat.calzado/08 | material | Pantuflas (aa-8-7) | principal | principal 2, complementario 1 |
| `imp:cat.calzado/11@aa-8-11-5` | cat.calzado/11 | construccion | Zapatillas para bebés y niños (aa-8-11-5) | complementario | complementario 7 |
| `imp:cat.calzado/12@aa-8-3` | cat.calzado/12 | uso | Botas (aa-8-3) | complementario | complementario 3 |
| `imp:cat.calzado/15@aa-8-7` | cat.calzado/15 | prestacion | Pantuflas (aa-8-7) | principal | principal 2, complementario 1 |
| `imp:cat.calzado/16@aa-8-7` | cat.calzado/16 | prestacion | Pantuflas (aa-8-7) | principal | principal 2, complementario 1 |
| `imp:cat.calzado/19@aa-8-3` | cat.calzado/19 | material | Botas (aa-8-3) | complementario | complementario 3 |
| `imp:cat.calzado/24@aa-8-11-5` | cat.calzado/24 | uso | Zapatillas para bebés y niños (aa-8-11-5) | principal | principal 7 |
| `imp:cat.casa-y-jardin/02@hg-15-1-4` | cat.casa-y-jardin/02 | estetica | Mantas (hg-15-1-4) | complementario | complementario 2, principal 1 |
| `imp:cat.casa-y-jardin/02@hg-15-1-4-2` | cat.casa-y-jardin/02 | estetica | Mantas decorativas (hg-15-1-4-2) | principal | principal 3 |
| `imp:cat.cd-de-musica/01@me-3-3` | cat.cd-de-musica/01 | identidad | CD de música (me-3-3) | crítico | crítico 3 |
| `imp:cat.cd-de-musica/04@me-3-3` | cat.cd-de-musica/04 | identidad | CD de música (me-3-3) | complementario | complementario 3 |
| `imp:cat.cd-de-musica/07@me-3-3` | cat.cd-de-musica/07 | uso | CD de música (me-3-3) | principal | principal 3 |
| `imp:cat.cd-de-musica/09@me-3-3` | cat.cd-de-musica/09 | contenido | CD de música (me-3-3) | complementario | complementario 3 |
| `imp:cat.cocina-y-comedor/01@hg-11-3-11` | cat.cocina-y-comedor/01 | material | Botellas de agua (hg-11-3-11) | principal | principal 7 |
| `imp:cat.cojines-decorativos/01@hg-3-64` | cat.cojines-decorativos/01 | medida | Cojines (hg-3-64) | crítico | crítico 2, principal 1 |
| `imp:cat.cojines-decorativos/07@hg-3-64` | cat.cojines-decorativos/07 | estetica | Cojines (hg-3-64) | complementario | complementario 3 |
| `imp:cat.cojines-decorativos/11@hg-3-64` | cat.cojines-decorativos/11 | material | Cojines (hg-3-64) | complementario | complementario 3 |
| `imp:cat.comida-para-perros/03@ap-2-3-3-1` | cat.comida-para-perros/03 | material | Comida para perros sin prescripción médica (ap-2-3-3-1) | principal | principal 3 |
| `imp:cat.comida-para-perros/08@ap-2-3-3-1` | cat.comida-para-perros/08 | material | Comida para perros sin prescripción médica (ap-2-3-3-1) | principal | principal 3 |
| `imp:cat.comida-para-perros/15@ap-2-3-3-1` | cat.comida-para-perros/15 | material | Comida para perros sin prescripción médica (ap-2-3-3-1) | principal | principal 3 |
| `imp:cat.decoracion/02@hg-3-64` | cat.decoracion/02 | material | Cojines (hg-3-64) | complementario | complementario 3 |
| `imp:cat.discos-y-lp/01@me-3-4` | cat.discos-y-lp/01 | identidad | Álbumes y LP (me-3-4) | crítico | crítico 5 |
| `imp:cat.discos-y-lp/04@me-3-4` | cat.discos-y-lp/04 | identidad | Álbumes y LP (me-3-4) | complementario | complementario 3, principal 2 |
| `imp:cat.discos-y-lp/11@me-3-4` | cat.discos-y-lp/11 | contenido | Álbumes y LP (me-3-4) | complementario | complementario 5 |
| `imp:cat.discos-y-lp/12@me-3-4` | cat.discos-y-lp/12 | uso | Álbumes y LP (me-3-4) | complementario | complementario 5 |
| `imp:cat.fundas-de-almohada/03@hg-15-1-8-2` | cat.fundas-de-almohada/03 | construccion | Fundas de almohada (hg-15-1-8-2) | principal | principal 5, complementario 2 |
| `imp:cat.fundas-de-almohada/08@hg-15-1-8-2` | cat.fundas-de-almohada/08 | construccion | Fundas de almohada (hg-15-1-8-2) | principal | principal 7 |
| `imp:cat.fundas-de-nordico/05@hg-15-1-5` | cat.fundas-de-nordico/05 | construccion | Fundas de nórdico (hg-15-1-5) | complementario | complementario 3, principal 2 |
| `imp:cat.joyas-para-piercings/01@aa-6-2` | cat.joyas-para-piercings/01 | identidad | Joyas para piercings (aa-6-2) | crítico | crítico 4, principal 3 |
| `imp:cat.joyas-para-piercings/07@aa-6-2` | cat.joyas-para-piercings/07 | construccion | Joyas para piercings (aa-6-2) | complementario | complementario 7 |
| `imp:cat.joyeria/03@aa-6-2` | cat.joyeria/03 | material | Joyas para piercings (aa-6-2) | complementario | complementario 4, principal 3 |
| `imp:cat.juguetes-para-perros/02@ap-2-3-7` | cat.juguetes-para-perros/02 | uso | Juguetes para perros (ap-2-3-7) | principal | principal 3 |
| `imp:cat.juguetes-para-perros/04@ap-2-3-7` | cat.juguetes-para-perros/04 | prestacion | Juguetes para perros (ap-2-3-7) | principal | principal 3 |
| `imp:cat.juguetes-para-perros/08@ap-2-3-7` | cat.juguetes-para-perros/08 | material | Juguetes para perros (ap-2-3-7) | complementario | complementario 2, principal 1 |
| `imp:cat.lijadoras/04@ha-15-59-3` | cat.lijadoras/04 | uso | Lijadoras orbitales (ha-15-59-3) | complementario | complementario 5 |
| `imp:cat.maletas-y-bolsos-de-viaje/01@lb-1-16` | cat.maletas-y-bolsos-de-viaje/01 | uso | Mochilas para computadora portátil (lb-1-16) | principal | principal 2, complementario 1 |
| `imp:cat.mantas/01@hg-15-1-4` | cat.mantas/01 | prestacion | Mantas (hg-15-1-4) | principal | principal 3 |
| `imp:cat.mantas/05@hg-15-1-4` | cat.mantas/05 | magnitud | Mantas (hg-15-1-4) | complementario | complementario 2, principal 1 |
| `imp:cat.mantas/06@hg-15-1-4-2` | cat.mantas/06 | material | Mantas decorativas (hg-15-1-4-2) | complementario | complementario 3 |
| `imp:cat.mantas/08@hg-15-1-4` | cat.mantas/08 | prestacion | Mantas (hg-15-1-4) | principal | principal 2, complementario 1 |
| `imp:cat.mantas/08@hg-15-1-4-2` | cat.mantas/08 | prestacion | Mantas decorativas (hg-15-1-4-2) | complementario | complementario 2, principal 1 |
| `imp:cat.mantas/11@hg-15-1-4` | cat.mantas/11 | construccion | Mantas (hg-15-1-4) | complementario | complementario 3 |
| `imp:cat.mobiliario/01@fr-22` | cat.mobiliario/01 | estetica | Sofás (fr-22) | principal | principal 3 |
| `imp:cat.mochilas-escolares/03@lb-1-12` | cat.mochilas-escolares/03 | construccion | Mochilas escolares (lb-1-12) | principal | principal 5 |
| `imp:cat.mochilas-para-portatil/03@lb-1-16` | cat.mochilas-para-portatil/03 | construccion | Mochilas para computadora portátil (lb-1-16) | principal | principal 3 |
| `imp:cat.mochilas/01@lb-1-12` | cat.mochilas/01 | uso | Mochilas escolares (lb-1-12) | principal | principal 5 |
| `imp:cat.mochilas/03@lb-1` | cat.mochilas/03 | material | Mochilas (lb-1) | principal | de las hijas |
| `imp:cat.mochilas/04@lb-1` | cat.mochilas/04 | prestacion | Mochilas (lb-1) | principal | de las hijas |
| `imp:cat.mochilas/05@lb-1-16` | cat.mochilas/05 | prestacion | Mochilas para computadora portátil (lb-1-16) | principal | principal 2, complementario 1 |
| `imp:cat.mochilas/12@lb-1` | cat.mochilas/12 | construccion | Mochilas (lb-1) | principal | de las hijas |
| `imp:cat.mochilas/13@lb-1-12` | cat.mochilas/13 | uso | Mochilas escolares (lb-1-12) | principal | principal 3, complementario 2 |
| `imp:cat.mochilas/13@lb-1-16` | cat.mochilas/13 | uso | Mochilas para computadora portátil (lb-1-16) | principal | principal 2, crítico 1 |
| `imp:cat.mochilas/15@lb-1` | cat.mochilas/15 | uso | Mochilas (lb-1) | complementario | de las hijas |
| `imp:cat.musica-y-grabaciones/01@me-3` | cat.musica-y-grabaciones/01 | identidad | Música y grabaciones (me-3) | crítico | de las hijas |
| `imp:cat.pantuflas/03@aa-8-7` | cat.pantuflas/03 | prestacion | Pantuflas (aa-8-7) | principal | principal 3 |
| `imp:cat.productos-para-mascotas/01@ap-2-3-7` | cat.productos-para-mascotas/01 | uso | Juguetes para perros (ap-2-3-7) | principal | principal 2, complementario 1 |
| `imp:cat.productos-para-mascotas/01@ap-2-3-3-1` | cat.productos-para-mascotas/01 | uso | Comida para perros sin prescripción médica (ap-2-3-3-1) | crítico | crítico 2, principal 1 |
| `imp:cat.protectores-de-colchon/04@hg-15-1-6-2` | cat.protectores-de-colchon/04 | construccion | Cubrecolchones (hg-15-1-6-2) | principal | principal 3 |
| `imp:cat.protectores-de-colchon/05@hg-15-1-6-2` | cat.protectores-de-colchon/05 | uso | Cubrecolchones (hg-15-1-6-2) | principal | principal 3 |
| `imp:cat.protectores-de-colchon/06@hg-15-1-6-2` | cat.protectores-de-colchon/06 | prestacion | Cubrecolchones (hg-15-1-6-2) | complementario | complementario 3 |
| `imp:cat.ropa-de-cama/02@hg-15-1-4` | cat.ropa-de-cama/02 | medida | Mantas (hg-15-1-4) | crítico | crítico 2, principal 1 |
| `imp:cat.ropa-de-casa/02@hg-15-1-4` | cat.ropa-de-casa/02 | cuidado | Mantas (hg-15-1-4) | complementario | complementario 2, principal 1 |
| `imp:cat.ropa-de-casa/05@hg-15-1-2-1` | cat.ropa-de-casa/05 | magnitud | Sábanas ajustables (hg-15-1-2-1) | principal | principal 1.67, complementario 1.33 |
| `imp:cat.ropa-de-casa/05@hg-15-1-4-2` | cat.ropa-de-casa/05 | magnitud | Mantas decorativas (hg-15-1-4-2) | principal | principal 2, complementario 1 |
| `imp:cat.ropa-de-casa/05@hg-15-1-8-2` | cat.ropa-de-casa/05 | magnitud | Fundas de almohada (hg-15-1-8-2) | principal | principal 1.67, complementario 1.33 |
| `imp:cat.ropa-y-accesorios/01@aa-8-3` | cat.ropa-y-accesorios/01 | estetica | Botas (aa-8-3) | principal | principal 3 |
| `imp:cat.ropa-y-accesorios/01@aa-8-7` | cat.ropa-y-accesorios/01 | estetica | Pantuflas (aa-8-7) | principal | principal 3 |
| `imp:cat.ropa-y-accesorios/01@aa-8-11-5` | cat.ropa-y-accesorios/01 | estetica | Zapatillas para bebés y niños (aa-8-11-5) | principal | principal 7 |
| `imp:cat.ropa-y-accesorios/02@aa-6-2` | cat.ropa-y-accesorios/02 | estetica | Joyas para piercings (aa-6-2) | complementario | complementario 4, principal 3 |
| `imp:cat.salsas-y-cremas-para-untar/01@fb-2-7-6` | cat.salsas-y-cremas-para-untar/01 | construccion | Confituras y gelatinas (fb-2-7-6) | principal | principal 6, complementario 1 |
| `imp:cat.sofas-cama/03@fr-22-7` | cat.sofas-cama/03 | construccion | Sofás cama (fr-22-7) | principal | principal 3 |
| `imp:cat.sofas/01@fr-22` | cat.sofas/01 | identidad | Sofás (fr-22) | crítico | crítico 2, principal 1 |
| `imp:cat.sofas/01@fr-22-7` | cat.sofas/01 | identidad | Sofás cama (fr-22-7) | principal | principal 3 |
| `imp:cat.sofas/08@fr-22-7` | cat.sofas/08 | prestacion | Sofás cama (fr-22-7) | principal | principal 2, complementario 1 |
| `imp:cat.sofas/12@fr-22` | cat.sofas/12 | prestacion | Sofás (fr-22) | principal | principal 3 |
| `imp:cat.sofas/16@fr-22` | cat.sofas/16 | construccion | Sofás (fr-22) | principal | principal 3 |
| `imp:cat.sofas/16@fr-22-7` | cat.sofas/16 | construccion | Sofás cama (fr-22-7) | complementario | complementario 2, principal 1 |
| `imp:cat.sofas/21@fr-22-7` | cat.sofas/21 | uso | Sofás cama (fr-22-7) | complementario | complementario 3 |
| `imp:cat.sofas/24@fr-22` | cat.sofas/24 | material | Sofás (fr-22) | complementario | complementario 3 |
| `imp:cat.toallas/04@hg-15-4-5` | cat.toallas/04 | prestacion | Toallas de mano (hg-15-4-5) | principal | principal 2 |
| `imp:cat.toallas/04@hg-15-4-1-1` | cat.toallas/04 | prestacion | Toallas de baño (hg-15-4-1-1) | principal | principal 2 |
| `imp:cat.toallas/08@hg-15-4-5` | cat.toallas/08 | construccion | Toallas de mano (hg-15-4-5) | complementario | complementario 2 |
| `imp:cat.toallas/08@hg-15-4-1-1` | cat.toallas/08 | construccion | Toallas de baño (hg-15-4-1-1) | complementario | complementario 2 |

### Votos que contradicen el marco

5 votos (no cuentan para bajar lo que fija el marco):
- cat.ropa-de-cama/01 (medida-que-fija): 1 votos «principal»
- cat.ropa-de-cama/01 (medida-que-fija): 1 votos «complementario»
- cat.sofas/31 (medida): 1 votos «complementario»
- cat.calzado/05 (medida): 1 votos «complementario»
- cat.pantuflas/17 (medida): 1 votos «complementario»

## Rasgos

Requisitos del catálogo con votos de rasgo en estas ejecuciones: 203 · con rasgo elegido por los votos en el índice: 0 · rasgos propuestos sin ganar: 0 · aprobados: 0.

## Información resolutiva

485 requisitos (mínimo de aceptación: 2 tiendas distintas). Aportaciones de las listas observadas: 0 · nunca observadas: 1398. Propuestas desde las fichas: 0 aceptadas, 0 pendientes (una tienda), 0 rechazadas.

Nunca observadas: cat.aceite-de-motor-sintetico/01: tipo o grupo del aceite base; cat.aceite-de-motor-sintetico/01: declaración de formulación total o parcialmente sintética; cat.aceite-de-motor-sintetico/01: ficha de datos de seguridad con la composición del aceite base; cat.aceite-para-motores-de-vehiculos/01: grado de viscosidad SAE J300; cat.aceite-para-motores-de-vehiculos/01: viscosidad cinemática a las temperaturas de referencia; cat.aceite-para-motores-de-vehiculos/02: volumen neto de aceite del envase; cat.aceite-para-motores-de-vehiculos/03: tipo de motor o combustible al que se destina; cat.aceite-para-motores-de-vehiculos/03: marcas, modelos o motorizaciones compatibles; cat.aceite-para-motores-de-vehiculos/03: código de vehículo en un estándar de montaje; cat.aceite-para-motores-de-vehiculos/03: indicación de ajuste universal o específico; cat.aceite-para-motores-de-vehiculos/04: categoría ACEA que cumple; cat.aceite-para-motores-de-vehiculos/04: categoría API que cumple; cat.aceite-para-motores-de-vehiculos/04: homologaciones de fabricantes de vehículos o motores; cat.aceite-para-motores-de-vehiculos/05: declaración de protección contra el desgaste; cat.aceite-para-motores-de-vehiculos/05: declaración de protección a altas o bajas temperaturas; cat.aceite-para-motores-de-vehiculos/05: declaración de protección contra la corrosión; cat.aceite-para-motores-de-vehiculos/05: resultado de ensayos de protección del motor; cat.aceite-para-motores-de-vehiculos/06: declaración de ahorro de combustible o energía; cat.aceite-para-motores-de-vehiculos/06: declaración de alto flujo o baja caída de presión; cat.aceite-para-motores-de-vehiculos/06: declaración de eficiencia de filtración; cat.aceite-para-motores-de-vehiculos/06: resultado de ensayo de ahorro de combustible; cat.alimentacion-bebida-y-tabaco/01: certificación ecológica que acredita; cat.alimentacion-bebida-y-tabaco/01: certificación de comercio justo; cat.alimentacion-bebida-y-tabaco/01: otra certificación de sostenibilidad y su entidad certificadora; cat.alimentacion-bebida-y-tabaco/01: código del organismo de control o número de certificado; cat.alimentos/01: cantidad neta del alimento en peso o volumen; cat.alimentos/01: peso del artículo sin envase, con su unidad; cat.alimentos/01: peso neto escurrido; cat.alimentos/01: número de unidades del envase y cantidad neta de cada una; cat.alimentos/02: enumeración de los ingredientes; cat.alimentos/02: materia prima principal; cat.alimentos/02: categoría funcional y denominación de los aditivos; cat.alimentos/02: ficha técnica o de especificaciones del producto; cat.alimentos/03: sustancias o productos que causan alergias o intolerancias presentes en el alimento; cat.alimentos/03: advertencia de posible presencia de alérgenos por contaminación cruzada; cat.alimentos/03: declaración de ausencia de un alérgeno; cat.alimentos/03: alérgenos identificados dentro de la lista de ingredientes; cat.alimentos/04: valor energético; cat.alimentos/04: cantidad de grasas y de ácidos grasos saturados; cat.alimentos/04: cantidad de hidratos de carbono.

## Relevancia

Reglas de exclusión: 12 · requisitos excluidos en los modelos: 12 · con relevancia dudosa (votados «no relevante» sin regla): 0 · coherencia de relevancia: 0 · hechos declarados sin pregunta con estas reglas: 66.

| Regla | Requisito | Clase | Decisión |
|---|---|---|---|
| `rel:cat.bricolaje/02@ha-15-60` | cat.bricolaje/02 | Bloques de lija (ha-15-60) | excluido |
| `rel:cat.bricolaje/02@ha-15-59-3` | cat.bricolaje/02 | Lijadoras orbitales (ha-15-59-3) | excluido |
| `rel:cat.calzado/06@aa-8-7` | cat.calzado/06 | Pantuflas (aa-8-7) | excluido |
| `rel:cat.calzado/06@aa-8-11-5` | cat.calzado/06 | Zapatillas para bebés y niños (aa-8-11-5) | excluido |
| `rel:cat.calzado/12@aa-8-7` | cat.calzado/12 | Pantuflas (aa-8-7) | excluido |
| `rel:cat.casa-y-jardin/02@hg-15-1-6-2` | cat.casa-y-jardin/02 | Cubrecolchones (hg-15-1-6-2) | excluido |
| `rel:cat.mantenimiento-cuidado-y-decoracion-de-vehiculos/01@vp-1-5-5-8` | cat.mantenimiento-cuidado-y-decoracion-de-vehiculos/01 | Aceite para motores de vehículos (vp-1-5-5-8) | excluido |
| `rel:cat.mantenimiento-cuidado-y-decoracion-de-vehiculos/02@vp-1-5-5-8` | cat.mantenimiento-cuidado-y-decoracion-de-vehiculos/02 | Aceite para motores de vehículos (vp-1-5-5-8) | excluido |
| `rel:cat.piezas-y-accesorios-para-vehiculos/04@vp-1-5-5-8` | cat.piezas-y-accesorios-para-vehiculos/04 | Aceite para motores de vehículos (vp-1-5-5-8) | excluido |
| `rel:cat.productos-para-mascotas/02@ap-2-3-3-1` | cat.productos-para-mascotas/02 | Comida para perros sin prescripción médica (ap-2-3-3-1) | excluido |
| `rel:cat.productos-para-mascotas/03@ap-2-3-3-1` | cat.productos-para-mascotas/03 | Comida para perros sin prescripción médica (ap-2-3-3-1) | excluido |
| `rel:cat.productos-para-perros/01@ap-2-3-3-1` | cat.productos-para-perros/01 | Comida para perros sin prescripción médica (ap-2-3-3-1) | excluido |

Candidata 6 (2025 votos), validada por familias frente a la versión 6:

- importancia: sin cambios.
- relevancia: **descartada**.

Votos de los agentes que coinciden con la regla: 606/751. Reglas con más votos en contra:

- `imp:prestacion@fr-22`: 7 votos «principal»
- `imp:contenido@hg-15-1-8-2`: 6 votos «crítico»
- `imp:construccion@hg-15-1-2`: 6 votos «complementario»
- `imp:construccion@fr-22`: 6 votos «principal»
- `marco:D-043.1/medida-descriptiva`: 5 votos «crítico»
- `imp:material@aa-8`: 5 votos «principal»
- `imp:identidad@ap-2`: 4 votos «crítico»
- `imp:contenido@hg-15-1-5`: 4 votos «crítico»

## Usado sin compilar

| Ejecución | Caso | Bloques | Sin regla | Inferidas | Categorías sin bloque |
|---|---|---|---|---|---|
| 2026-10-26-v6-a | bota-polo-e | — | 0 | 1 | — |
| 2026-10-26-v6-a | cojin-018 | — | 0 | 0 | — |
| 2026-10-26-v6-a | cuerda-tootoy | — | 0 | 0 | — |
| 2026-10-26-v6-a | funda-nordica-bordada-401 | esp.juego | 0 | 2 | — |
| 2026-10-26-v6-a | funda-nordica-salvia-642 | esp.juego | 0 | 2 | — |
| 2026-10-26-v6-a | manta-nacarina-046 | — | 0 | 1 | — |
| 2026-10-26-v6-a | pienso-josera-sea-fish | — | 0 | 1 | — |
| 2026-10-26-v6-a | plaid-punto-101 | — | 0 | 1 | — |
| 2026-10-26-v6-a | protector-basic-010 | — | 0 | 0 | — |
| 2026-10-26-v6-a | sabanas-coralina-999 | esp.juego | 0 | 3 | — |
| 2026-10-26-v6-a | sofa-cama-luna | — | 0 | 1 | — |
| 2026-10-26-v6-a | stressless-wave-outlet | — | 0 | 0 | — |
| 2026-10-26-v6-a | toallas-azul-080 | esp.juego | 0 | 0 | — |
| 2026-10-26-v6-a | zapatillas-bano-50 | — | 0 | 1 | — |
| 2026-10-26-v6-b | bota-polo-e | — | 0 | 0 | — |
| 2026-10-26-v6-b | cojin-018 | — | 0 | 0 | — |
| 2026-10-26-v6-b | cuerda-tootoy | — | 0 | 0 | — |
| 2026-10-26-v6-b | funda-nordica-bordada-401 | esp.juego | 0 | 1 | — |
| 2026-10-26-v6-b | funda-nordica-salvia-642 | esp.juego | 0 | 1 | — |
| 2026-10-26-v6-b | manta-nacarina-046 | — | 0 | 0 | — |
| 2026-10-26-v6-b | pienso-josera-sea-fish | — | 0 | 1 | — |
| 2026-10-26-v6-b | plaid-punto-101 | — | 0 | 2 | — |
| 2026-10-26-v6-b | protector-basic-010 | — | 0 | 0 | — |
| 2026-10-26-v6-b | sabanas-coralina-999 | esp.juego | 0 | 2 | — |
| 2026-10-26-v6-b | sofa-cama-luna | — | 0 | 1 | — |
| 2026-10-26-v6-b | stressless-wave-outlet | — | 0 | 0 | — |
| 2026-10-26-v6-b | toallas-azul-080 | esp.juego | 0 | 0 | — |
| 2026-10-26-v6-b | zapatillas-bano-50 | — | 0 | 1 | — |

## Divergencias de las decisiones no inducidas

- **2026-10-26-v6-a · bota-polo-e:** especializaciones uso de equitación ↔ — · faltan compatibilidad con el estribo
- **2026-10-26-v6-a · cojin-018:** especializaciones material reciclado ↔ — · faltan qué proporción, en qué parte
- **2026-10-26-v6-a · cuerda-tootoy:** especializaciones cuerda ↔ — · faltan deshilachado, ingestión de fibras
- **2026-10-26-v6-a · funda-nordica-bordada-401:** falta la inferida esperada
- **2026-10-26-v6-a · funda-nordica-salvia-642:** composición ['hg-15-1-2-1', 'hg-15-1-5', 'hg-15-1-8-2'] alias ['hg-15-1-11']
- **2026-10-26-v6-a · manta-nacarina-046:** especializaciones tejido polar ↔ — · faltan bolitas
- **2026-10-26-v6-a · pienso-josera-sea-fish:** especializaciones pienso seco ↔ —
- **2026-10-26-v6-a · plaid-punto-101:** especializaciones tejido de punto ↔ — · faltan enganchones, deformación, bolitas
- **2026-10-26-v6-a · sabanas-coralina-999:** especializaciones juego ↔ juego juego de sábana encimera, sábana bajera ajustable y funda(s) de almohada, piezas de categorías distintas (Sábanas planas, Sábanas ajustables y Fundas de almohada) esp juego; uso invernal ↔ —; tejido polar ↔ — · faltan temporada, pérdida de pelo
- **2026-10-26-v6-a · sofa-cama-luna:** faltan antimanchas · falta la inferida esperada
- **2026-10-26-v6-a · stressless-wave-outlet:** especializaciones tapicería de piel ↔ — · aplicación incompleta
- **2026-10-26-v6-a · zapatillas-bano-50:** faltan agarre sobre suelo mojado
- **2026-10-26-v6-b · bota-polo-e:** especializaciones uso de equitación ↔ — · faltan compatibilidad con el estribo
- **2026-10-26-v6-b · cojin-018:** especializaciones material reciclado ↔ — · faltan qué proporción, en qué parte
- **2026-10-26-v6-b · cuerda-tootoy:** especializaciones cuerda ↔ — · faltan deshilachado, ingestión de fibras
- **2026-10-26-v6-b · funda-nordica-bordada-401:** faltan ¿qué preparación tiene el algodón? · falta la inferida esperada
- **2026-10-26-v6-b · manta-nacarina-046:** especializaciones tejido polar ↔ — · faltan bolitas
- **2026-10-26-v6-b · pienso-josera-sea-fish:** especializaciones pienso seco ↔ —
- **2026-10-26-v6-b · plaid-punto-101:** especializaciones tejido de punto ↔ — · faltan enganchones, deformación, bolitas
- **2026-10-26-v6-b · sabanas-coralina-999:** especializaciones juego ↔ juego Juego de piezas de categorías distintas: sábana encimera, sábana bajera y funda(s) de almohada («Qué incluye: Sábana encimera, bajera y funda(s) de almohada, 1 o 2 según medida») esp juego; uso invernal ↔ —; tejido polar ↔ — · faltan temporada, pérdida de pelo
- **2026-10-26-v6-b · sofa-cama-luna:** faltan antimanchas · falta la inferida esperada
- **2026-10-26-v6-b · stressless-wave-outlet:** especializaciones tapicería de piel ↔ —
- **2026-10-26-v6-b · zapatillas-bano-50:** faltan agarre sobre suelo mojado
- **Oferta inestable · cojin-018:** estándar | con descuento
- **Oferta inestable · manta-nacarina-046:** con descuento, con opiniones publicadas, con variantes | con opiniones publicadas, con variantes
- **Oferta inestable · protector-basic-010:** con descuento | con descuento, con opiniones publicadas
- **Oferta inestable · sabanas-coralina-999:** con variantes | con descuento, con variantes
- **Oferta inestable · stressless-wave-outlet:** cantidad limitada, con descuento | cantidad limitada, con descuento, unidad no nueva
- **Oferta inestable · toallas-azul-080:** con descuento, con garantía comercial, con opiniones publicadas | con descuento, con garantía comercial, con opiniones publicadas, con variantes

Hechos declarados sin pregunta más repetidos: Control de calidad: Burrito Blanco, S.L.U. (5); Diseño en España por Burrito Blanco, S.L.U. (4); Cambio en los 14 días naturales posteriores a la recepción (3); Cambio en 14 días naturales (3); Cambios en los 14 días naturales siguientes a la recepción (2); Diseño en España por Burrito Blanco (2); Cambios: 14 días naturales desde la recepción (2); diseño en España y control de calidad por Burrito Blanco, S.L.U. (2); Cambios en los 14 días naturales posteriores a la recepción (2); La tienda no muestra el stock disponible de cada producto (1); Garantía de calidad: Burrito Blanco, S.L.U. (sin contenido ni condiciones) (1); Imágenes generadas en parte con IA, aproximadas (1).
