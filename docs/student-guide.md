# Guia Del Estudiante

Status: draft  
Purpose: iniciar practica PAA desde el CLI o con un agente AI.

## Primer Dia

1. Clona el repositorio.
2. Revisa las fuentes oficiales enlazadas en `docs/official-sources.md`.
3. Genera el prompt para tu agente:

```bash
python3 cli/tutorpaa/main.py session-prompt --student sample
```

4. Pegalo en Codex, opencode u otro agente dentro del repo.
5. Al terminar, revisa tu reporte:

```bash
python3 cli/tutorpaa/main.py report --student sample
```

Tambien puedes iniciar manualmente con:

```text
Lee AGENTS.md y actua como mi tutor PAA.
Usa prompts/agents/tutor.md.
Mi estudiante es sample.
Hazme preguntas una por una y actualiza mi progreso despues de corregir.
```

## Como Responder

Cuando el tutor haga una pregunta:

- Responde con la opcion elegida.
- Agrega una frase de razonamiento.
- Si no sabes, explica que intentaste.

Ejemplo:

```text
Elijo B. Primero simplifique la ecuacion y me dio x = 4.
```

## Como Practicar Mejor

- Practica en bloques cortos de 20 a 30 minutos.
- Revisa errores el mismo dia.
- No busques solo acertar: busca entender por que una opcion incorrecta parecia atractiva.
- Alterna matematica y verbal.
- Usa la prueba practica oficial como simulacro externo bajo tiempo, no como banco para memorizar respuestas.
