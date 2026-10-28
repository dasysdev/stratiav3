# Campos de una pista de valoración

Fecha: 2026-10-27. Update descrito por el usuario en la sesión de diseño del sistema de pistas de valoración. Resuelve OQ-68 (campos exactos de una pista, quién escribe las dirigidas a una fuente y su lugar en el perfil del RI). Ortografía de las citas normalizada.

## 1. Campos

Claude propuso seis campos. Usuario: «OK», con una duda sobre el id y las claves para buscar. Sobre el id: «ok al id, pero sin 0s delante». Sobre un índice generado de pistas por requisito: «olvida lo de los índices por ahora».

| Campo | Para qué sirve |
|---|---|
| `id` | Número que pone el sistema, **sin ceros delante**: `PV-1`, `PV-2`… Nadie elige nombres y el número no cambia aunque se reescriba el texto. |
| `pista` | El criterio y su porqué, en una o dos frases. |
| `propiedad` | Qué propiedades hay que observar. |
| `ac` | A qué criterios afecta. |
| `para` | A quién va dirigida: un tipo (rasgo, entidad o ambos), una fuente o un requisito. |
| `origen` | Quién la escribió y en qué se apoya (ley, referencia, preguntas de PAA), como en la información resolutiva. |

Ejemplo (hipotético):

```json
{
  "id": "PV-3",
  "pista": "La composición usa el nombre legal de cada fibra, con su % en peso: es lo que permite entenderla y compararla.",
  "propiedad": ["P09", "P13"],
  "ac": ["Precisión", "Comparabilidad"],
  "para": {"fuente": "ley:UE-1007/2011"},
  "origen": {"tipo": "normativa", "apoyo": ["ley:UE-1007/2011-16.1"]}
}
```

## 2. Quién escribe cada destino

Usuario: «OK».

| Dirigida a… | La escribe |
|---|---|
| Un tipo | El entrenamiento |
| Una fuente | Taxo |
| Un requisito | Taxo o PAA |

## 3. Cómo le llegan al auditor

Usuario: «OK».

- Al montar el modelo de una ficha, el código busca las pistas de cada requisito y las guarda ya resueltas en el modelo.
- El perfil del RI gana un campo, `pistas_valoracion`, que se rellena solo desde el modelo. El auditor no lo escribe; solo lo usa.

## 4. Aplazado

- Un índice generado de pistas por requisito (para no recorrer todas las pistas y para revisar huecos): «olvida lo de los índices por ahora».
