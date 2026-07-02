# Guia De Contenido

Status: draft  
Purpose: reglas para crear y revisar preguntas abiertas de TutorPAA.

## Formato

El contenido vive en archivos JSONL: una pregunta por linea.

Campos requeridos:

- `id`
- `status`
- `section`
- `topic`
- `difficulty`
- `question`
- `choices`
- `answer`
- `explanation`
- `skills`
- `estimated_time_seconds`

## Estados

- `draft`: generado o escrito, aun sin revision.
- `curated`: revisado y apto para practica.
- `deprecated`: retirado, se conserva por historial.

## Dificultad

Usar escala 1 a 5:

- 1: fundamento.
- 2: basico con un paso.
- 3: intermedio.
- 4: avanzado.
- 5: simulacro dificil.

## Derechos

No copiar preguntas propietarias, examenes reales cerrados ni material de pago. Se permiten preguntas originales inspiradas en habilidades generales.

Los PDFs oficiales enlazados en `docs/official-sources.md` se usan para calibrar estructura, temas, dificultad y estrategia. No deben importarse literalmente al banco abierto.

## Calidad

Cada pregunta debe:

- Tener una unica respuesta correcta.
- Incluir distractores razonables.
- Explicar el procedimiento.
- Declarar habilidades evaluadas.
- Usar lenguaje claro y sin ambiguedad.

## Enriquecimiento Desde Fuentes

Al enriquecer el banco:

- Usa los PDFs oficiales para identificar habilidades, formato y niveles de dificultad.
- Escribe preguntas originales; no reproduzcas lecturas, ejercicios ni claves de los PDFs.
- Distribuye nuevas preguntas entre temas faciles, intermedios y avanzados.
- Prefiere textos cortos originales para lectura e inferencia.
- Mantiene IDs estables con el patron `{section}-{topic}-{number}`.
