# Clasificación del catálogo de entrenamiento con Claude Code

*Update descrito en la conversación del 2026-10-25 y transcrito para su trazabilidad (tareas T-020 y T-026).*

## Contexto

D-045 y `model-training` decían: «Ejecución: para probar productos reales ahora, un comando de Claude Code; para entrenar con miles de fichas no escala y hacen falta llamadas a la API por lotes (tarea aparte)». Tras capturar el piloto de 30 fichas (T-025), Claude propuso clasificarlo con la API de Anthropic por lotes (T-026) y pidió una `ANTHROPIC_API_KEY`.

## Decisión del usuario

Palabras del usuario: «para clasificar usamos claude code».

Claude lo entiende como que la clasificación del catálogo de entrenamiento se hace con agentes de Claude Code, como `/demand-model`, y no con llamadas a la API.
