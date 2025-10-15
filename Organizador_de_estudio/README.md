El organizador de estudios es un asistente por consola, de uso guiado y sencillo, que convierte en minutos un par de datos del alumno (tipo de curso, dificultad, días y carga diaria) para generar un plan mínimo viable dividido en secciones de teoría, práctica y simulacro. La herramienta reparte bloques de 30 minutos de forma razonable, prioriza práctica en cursos exigentes y al cierre entrega indicadores de cumplimiento, horas efectivas y un estado “listo/no listo” para decidir rápido el siguiente movimiento. Está pensada como punto de entrada para estudiantes nuevos y como base ampliable para futuras interacciones del proyecto. Autor: Luis Iniestra

Algoritmo

Entradas:

Nombre de la materia.

Tipo de curso (Cálculo, Programación u otro).

Nivel de dificultad (1 a 5).

Número de días restantes para estudiar.

Carga diaria de estudio (en minutos).

Proceso:

Inicialización de listas:

pesos = [0.35, 0.45, 0.20] → proporciones para teoría, práctica y simulacro.

min_plan = [0, 0, 0] y min_hechos = [0, 0, 0] para registrar minutos planeados y realizados.

Captura de datos:

Se piden al usuario los valores de materia, tipo, dificultad, días y carga diaria.

Se valida que los valores sean correctos.

Ajuste de pesos:

Según el tipo de curso se modifican los valores de pesos.

Se normalizan los pesos para que la suma total sea igual a 1.

Cálculo del plan de estudio:

Se calcula el total de minutos disponibles (días * carga diaria).

Se distribuyen los minutos entre teoría, práctica y simulacro, ajustando la práctica según la dificultad.

Los resultados se guardan en min_plan.

Generación del plan diario:

Se crean bloques de 30 minutos por día.

Se asignan los bloques priorizando práctica, luego teoría y finalmente simulacro.

Se van sumando los minutos realizados en min_hechos.

Cálculo de indicadores:

Se calcula el porcentaje de cumplimiento (min_hechos / min_plan * 100).

Se calculan las horas efectivas (min_hechos_total / 60).

Se determina el estado (“listo” si el cumplimiento es ≥ 80%, de lo contrario “no_listo”).

Presentación de resultados:

Se muestran los minutos planificados y realizados por sección.

Se muestran los indicadores finales de desempeño.

Salidas

Minutos planificados por sección: Teoría, Práctica y Simulacro.

Distribución diaria del estudio en bloques de 30 minutos.

Porcentaje total de cumplimiento.

Horas efectivas de estudio.

Estado final del plan (“listo” o “no_listo”).
