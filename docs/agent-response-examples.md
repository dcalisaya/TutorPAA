# Ejemplos De Respuesta Del Agente

Status: draft  
Purpose: mostrar respuestas correctas e incorrectas para agentes TutorPAA.

## Cuando El Banco Es Pequeno

Respuesta incorrecta:

```text
El proyecto tiene solo 9 preguntas. Esto es demasiado poco para preparar un examen serio. Puedes esperar a que se agregue mas contenido.
```

Problema: es honesta, pero abandona la sesion de practica.

Otra respuesta incorrecta:

```text
Son 20 preguntas curadas en total, todas listas para practicar. ¿Quieres comenzar con un diagnostico de practica?
```

Problema: el estudiante ya pidio practicar o iniciar; el agente agrega una confirmacion innecesaria.

Otra respuesta incorrecta:

```text
Te recomiendo empezar con algebra basica. Empezamos con una?
Si 3x + 5 = 20, ¿cuanto vale x?
Escribe tu opcion (A, B, C, D).
```

Problemas: pide confirmacion innecesaria y no muestra las opciones A/B/C/D.

Respuesta correcta:

```text
Hay 20 preguntas curadas para empezar. Iniciare con diagnostico mixto.

Pregunta 1:
Si 3x + 5 = 20, ¿cuanto vale x?

Opciones:
A. 3
B. 5
C. 7
D. 15

Responde con A, B, C o D, razonamiento y confianza del 1 al 5.
```

## Cuando El Estudiante Pregunta "Que Me Recomiendas?"

Respuesta correcta:

```text
Te recomiendo empezar con algebra basica para calentar y luego pasar a datos o geometria segun tu resultado.

Pregunta 1 [math / algebra / dificultad 1]:
Si 3x + 5 = 20, ¿cuanto vale x?

Opciones:
A. 3
B. 5
C. 7
D. 15

Responde con A, B, C o D, tu razonamiento y confianza del 1 al 5.
```

## Cuando Se Agotan Preguntas Curadas

```text
Ya usamos las preguntas curadas de algebra disponibles. Sigo con una pregunta original draft para reforzar la misma habilidad.

Pregunta draft:
...
```

## Cuando El Estudiante Falla

```text
Resultado: incorrecto
Respuesta correcta: 5
Por que: al restar 5 a ambos lados queda 3x = 15; luego x = 5.
Tipo de error: calculation
Siguiente paso: resolvamos otra ecuacion lineal parecida, pero con parentesis.
```
