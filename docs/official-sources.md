# Fuentes Oficiales

Status: active  
Purpose: registrar fuentes oficiales usadas para calibrar TutorPAA sin copiar contenido propietario.

## Fuentes USFQ / College Board

1. Prueba practica PAA
   - URL: https://www.usfq.edu.ec/sites/default/files/2023-11/prueba-practica-paa.pdf
   - Tipo: PDF oficial enlazado por USFQ.
   - Uso permitido en este repo: referencia externa para simulacros, familiarizacion con formato y calibracion de dificultad.
   - No copiar al banco abierto: preguntas completas, lecturas, claves o secciones extensas.

2. Guia de estudios PAA
   - URL: https://www.usfq.edu.ec/sites/default/files/2023-11/guia-estudios-paa.pdf
   - Tipo: PDF oficial enlazado por USFQ.
   - Uso permitido en este repo: referencia de estructura, categorias de ejercicios, sugerencias de estudio y habilidades evaluadas.
   - No copiar al banco abierto: ejercicios completos, explicaciones extensas o lecturas completas.

## Observaciones Confirmadas

- La guia de estudios PAA describe una prueba con Lectura, Redaccion, Matematicas e Ingles.
- La estructura general incluye seleccion multiple de cuatro opciones y algunos ejercicios de Matematicas donde el estudiante suple la respuesta.
- Matematicas se organiza en Aritmetica, Algebra, Geometria, y Analisis de datos y Probabilidad.
- Lectura incluye vocabulario en contexto, ideas explicitas e implicitas, analisis, interpretacion e inferencias, analisis de informacion cuantitativa o graficos, y analisis literario.

## Uso Por Agentes

Los agentes pueden:

- Recomendar al estudiante hacer una seccion del PDF oficial bajo tiempo.
- Pedir que el estudiante reporte respuestas o dudas desde el PDF.
- Explicar habilidades y estrategias usando lenguaje propio.
- Generar ejercicios originales inspirados en las categorias oficiales.
- Enriquecer `content/` con preguntas originales calibradas por los temas de las fuentes.

Los agentes no deben:

- Transcribir preguntas oficiales completas dentro de `content/`.
- Crear un archivo derivado que reproduzca la prueba practica.
- Presentar contenido del PDF como si fuera autoria del repo.

## Nota Operativa

Si el estudiante esta usando este repo con Codex u opencode, el flujo recomendado es:

```text
Lee docs/official-sources.md.
Ayudame a usar la prueba practica oficial como simulacro.
No copies las preguntas al repo; yo te dire el numero de pregunta y mi razonamiento.
Corrige mi razonamiento y registra el tipo de error.
```
