# Flujo Agent-First

Status: draft  
Purpose: definir como TutorPAA funciona como chat especializado de practica.

## Principio

El agente AI es la interfaz principal. El CLI no reemplaza al tutor; le da herramientas para consultar contenido, registrar intentos y producir reportes.

## Experiencia Del Estudiante

El estudiante deberia poder escribir:

```text
Actua como mi tutor PAA y empieza mi practica.
```

El agente debe:

1. Leer `AGENTS.md` y `prompts/agents/tutor.md`.
2. Revisar el perfil del estudiante.
3. Elegir una pregunta curated.
4. Presentarla sin respuesta.
5. Esperar intento.
6. Corregir y explicar.
7. Registrar el intento.
8. Elegir la siguiente pregunta segun el resultado.

El agente no debe detenerse solo porque el banco curado sea pequeno. Debe informar la limitacion brevemente y continuar con preguntas originales `draft` en la conversacion.

Tampoco debe pedir confirmacion adicional con frases como "quieres comenzar" cuando el estudiante ya pidio practicar. Debe empezar.

Si el estudiante pregunta "que recomiendas?", el agente debe recomendar una ruta y empezar la primera pregunta en el mismo mensaje.

## Herramientas Del Agente

Listar contenido:

```bash
python3 cli/tutorpaa/main.py list
```

Escoger preguntas como JSON:

```bash
python3 cli/tutorpaa/main.py pick --section math --count 1 --random
```

Escoger una pregunta ya formateada para el estudiante:

```bash
python3 cli/tutorpaa/main.py pick --section math --count 1 --random --format text
```

Registrar intento:

```bash
python3 cli/tutorpaa/main.py record \
  --student sample \
  --question-id math-algebra-001 \
  --answer "5" \
  --reasoning "Reste 5 y dividi entre 3" \
  --confidence 4 \
  --error-type none
```

Ver reporte:

```bash
python3 cli/tutorpaa/main.py report --student sample
```

Generar prompt de arranque:

```bash
python3 cli/tutorpaa/main.py session-prompt --student sample
```

## Contrato De Sesion

Cada intento debe guardar:

- estudiante
- pregunta
- respuesta
- razonamiento
- confianza
- correcto o incorrecto
- tipo de error
- habilidades relacionadas

## Formato De Pregunta

Para seleccion multiple, cada pregunta debe incluir:

- numero de pregunta;
- seccion, tema y dificultad si estan disponibles;
- enunciado;
- todas las opciones;
- instruccion de respuesta consistente con las etiquetas mostradas.

Ejemplo:

```text
Pregunta 1 [math / algebra / dificultad 1]:
Si 3x + 5 = 20, ¿cuanto vale x?

Opciones:
A. 3
B. 5
C. 7
D. 15

Responde con A, B, C o D, tu razonamiento y confianza del 1 al 5.
```

## Adaptacion

Si el estudiante falla:

- repetir una habilidad similar con menor dificultad;
- explicar el concepto;
- pedir que reconstruya el razonamiento;
- registrar error.

Si acierta con confianza alta:

- subir dificultad;
- alternar habilidad relacionada;
- avanzar hacia mini simulacro.

Si acierta con razonamiento debil:

- marcar observacion;
- pedir explicacion alternativa;
- no asumir dominio total.

## Banco Pequeno

Mientras el repositorio tenga poco contenido, el comportamiento correcto es:

- usar primero preguntas curated;
- generar preguntas originales `draft` en la conversacion cuando haga falta;
- no guardar preguntas draft como curated;
- no convertir la sesion en un reporte de limitaciones;
- mantener el foco en practicar.
