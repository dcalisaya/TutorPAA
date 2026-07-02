# TutorPAA

Status: draft  
Purpose: preparar estudiantes para la PAA de admision USFQ mediante practica guiada con agentes AI y herramientas CLI locales.

TutorPAA es un repositorio educativo abierto, pensado para uso local con agentes AI de CLI como Codex, opencode, Claude Code o herramientas similares. La interfaz principal es el agente: el estudiante conversa como en un chat, pero el agente trabaja solo sobre practica PAA, usa el contenido del repo y registra progreso.

## Enfoque

- Agent-first: el tutor AI es la interfaz principal.
- CLI como herramienta del agente, no como experiencia principal.
- Contenido abierto en archivos `jsonl`, revisable por Git.
- Progreso local por estudiante en `sessions/`.
- Agentes versionados en `prompts/agents/`.
- Sin app web por ahora: el foco es fortalecer la experiencia con CLI, Codex, opencode y agentes similares.
- Sin dependencias pesadas: el CLI inicial usa Python estandar.

## Inicio Rapido

Requisitos iniciales:

- Python 3.10 o superior.
- Un agente AI de CLI opcional, por ejemplo Codex u opencode.

Genera un prompt listo para iniciar con un agente:

```bash
python3 cli/tutorpaa/main.py session-prompt --student sample
```

Uso recomendado: ejecuta ese comando, pega el prompt en Codex/opencode dentro del repo y responde las preguntas que el tutor te presente una por una.

O copia el prompt de:

```text
prompts/start-student-session.md
```

El agente puede usar estas herramientas mientras conversa:

```bash
python3 cli/tutorpaa/main.py pick --section math --count 1 --random --format text
python3 cli/tutorpaa/main.py record --student sample --question-id math-algebra-001 --answer "5" --confidence 4 --error-type none
python3 cli/tutorpaa/main.py report --student sample
```

El banco inicial incluye 56 preguntas revisadas. Si una habilidad aun necesita mas practica que la disponible, el agente puede continuar con preguntas originales marcadas como `draft` en la conversacion. No debe detener la sesion ni convertirla en un inventario del repositorio.

## Banco Inicial

| Seccion | Tema | Preguntas revisadas |
|---|---|---:|
| Matematica | algebra | 8 |
| Matematica | arithmetic | 7 |
| Matematica | data_analysis | 8 |
| Matematica | geometry | 7 |
| Verbal | inference | 7 |
| Verbal | reading | 7 |
| Verbal | vocabulary | 6 |
| Verbal | writing | 6 |
| Total |  | 56 |

## Mapa del Repositorio

| Ruta | Proposito |
|---|---|
| `AGENTS.md` | Instrucciones para agentes AI que trabajan como tutores o mantenedores. |
| `index.json` | Indice simple para que agentes descubran archivos clave. |
| `content/paa/` | Banco abierto de preguntas PAA en JSONL. |
| `prompts/agents/` | Roles de tutor, evaluador, planificador, generador y simulador. |
| `cli/tutorpaa/` | CLI liviano sin dependencias externas. |
| `sessions/students/` | Perfiles, intentos y planes locales de estudiantes. |
| `docs/` | Modelo PAA, guias de estudiante, contenido y roadmap. |
| `packages/` | Modulos futuros para scoring, validacion de contenido y utilidades compartidas. |

## Alcance Inicial

El alcance inicial cubre:

- Practica por seccion: matematica y verbal.
- Preguntas revisadas en formato estructurado.
- Registro local de intentos.
- Reporte basico de progreso.
- Prompts para que un agente AI actue como tutor PAA.
- Flujo agent-first para practica conversacional enfocada.
- Documentacion de contribucion para agregar preguntas.
- Referencias oficiales enlazadas, sin copiar contenido propietario al banco abierto.

Fuera de alcance por ahora:

- Login, cuentas remotas o sincronizacion.
- Pagos, becas o gestion oficial de admision.
- Reemplazar la informacion oficial de la USFQ.
- Generar preguntas automaticamente sin revision humana antes de agregarlas al banco revisado.

## Proximas Mejoras

El proyecto debe crecer sin perder su enfoque local y agent-first:

- Mas preguntas revisadas por habilidad y dificultad.
- Diagnostico inicial guiado por agente.
- Mejor reporte de errores por habilidad.
- Plan semanal generado desde el historial del estudiante.
- Simulacros cortos y completos desde CLI.
- Validador de contenido JSONL.

## Nota Sobre la PAA USFQ

Este repo modela la preparacion inicial sobre dos areas principales usadas por la USFQ en su PAA de College Board para admision: aptitud verbal y aptitud matematica. La guia de College Board tambien cubre Redaccion e Ingles; esas areas quedan como preparacion complementaria y ruta futura. Los puntajes, requisitos y fechas oficiales pueden cambiar; verifica siempre la informacion vigente en los canales oficiales de la USFQ.

Fuentes iniciales:

- `docs/official-sources.md`
