CONTEXTO
Mi participación en el proyecto consistirá en el desarrollo de un organizador de horarios para estudiantes de nivel universitario, con el propósito de ofrecer una herramienta práctica que ayude a mejorar la administración del tiempo y la productividad académica. Este sistema permitirá registrar, visualizar y gestionar tanto el horario de clases como el horario de tareas de cada estudiante.
El organizador funcionará en dos apartados principales:
1.	Horario de clases
•	El estudiante podrá ingresar las materias que desea cursar, junto con la cantidad de horas semanales correspondientes a cada una.
•	Existirá la opción de acomodo manual, en donde el alumno organizará sus materias de acuerdo con sus preferencias y disponibilidad.
•	Además, se implementará un acomodo automático, que distribuirá las materias de forma eficiente, garantizando que el estudiante no sobrepase un límite de 5 horas de clases por día. También se considerará la inclusión de pausas y descansos entre clases para evitar la sobrecarga académica.
•	Con esto se busca ofrecer un horario flexible, pero al mismo tiempo equilibrado y funcional.
2.	Horario de tareas
•	Este apartado permitirá registrar todas las tareas asignadas en cada materia.
•	Cada tarea estará acompañada de información relevante como: la materia a la que pertenece, la cantidad de horas estimadas para su realización, así como la fecha y hora límite de entrega.
•	El sistema generará un calendario que facilitará al estudiante llevar un control detallado de sus pendientes y organizar su tiempo de manera eficiente para cumplir con todas sus obligaciones académicas.
Algoritmos del Código del Proyecto
1. Estructuras y constantes
  1.1. DIAS = ['Lunes','Martes','Miércoles','Jueves','Viernes']
  1.2. SLOTS_POR_DIA = 8
  1.3. MAX_CLASES_POR_DIA = 5
  1.4. Celdas especiales: LIBRE, DESCANSO
  1.5. Materias: lista de diccionarios → {'nombre': str, 'horas_semanales': int}
  1.6. Tareas: lista de diccionarios → {'titulo': str, 'materia': str, 'horas_estimadas': int, 'deadline': datetime}
2. Funciones ayudantes
  2.1. normaliza_dia(entrada):
    2.1.1. Si entrada está vacía → 'Lunes'.
    2.1.2. Capitalizar.
    2.1.3. Si comienza con 'Mier' → 'Miércoles'.
    2.1.4. Si no pertenece a DIAS → 'Lunes'.
    2.1.5. Devolver día normalizado.
  2.2. indice_dia(dia):
    2.2.1. Buscar índice del día en DIAS.
    2.2.2. Devolver posición correspondiente.
    2.2.3. Vista original por DÍAS
  3.1. registrar_clases():
    3.1.1. Pedir número de materias.
    3.1.2. Por cada materia, pedir nombre y horas.
    3.1.3. Guardar como diccionario.
    3.1.4. Devolver lista.
  3.2. mostrar_clases(materias):
    3.2.1. Si lista vacía → mensaje.
    3.2.2. Mostrar nombre y horas de cada materia.
  3.3. materias_a_tuplas(materias):
    3.3.1. Convertir cada dict a tupla (nombre, horas).
  3.4. acomodo_automatico_dias(materias):
    3.4.1. Crear diccionario con días vacíos.
    3.4.2. Asignar materias respetando 5h/día.
    3.4.3. Insertar 'DESCANSO' tras 2 clases seguidas.
    3.4.4. Devolver diccionario final.
  3.5. acomodo_manual_dias(materias):
    3.5.1. Pedir día al usuario.
    3.5.2. Si hay espacio (<5h) agregar.
    3.5.3. Si no, pedir otro día.
  3.6. mostrar_acomodo(dias):
    3.6.1. Mostrar lista de clases de cada día.
  4. Vista nueva con MATRIZ (clases + tareas)
    4.1. construir_matriz_vacia(): Crear matriz 5xSLOTS con 'LIBRE'.
    4.2. consecutivos_clases_al_final(fila): Contar clases seguidas al final de fila.
    4.3. contar_clases_en_dia(fila): Contar clases que no son LIBRE, DESCANSO o TAREA.
    4.4. imprimir_matriz(matriz, titulo): Imprimir encabezado y contenido tabular.
    4.5. acomodo_automatico_matriz(materias): Distribuir materias automáticas (máx. 5h/día).
    4.6. acomodo_manual_matriz(materias): Pedir días manualmente y llenar matriz.
    4.7. registrar_tarea_calendario(): Registrar tarea con título, materia, horas y fecha límite.
    4.8. mostrar_tareas(tareas): Mostrar tareas ordenadas por fecha límite.
    4.9. generar_calendario_tareas(): Insertar tareas en celdas LIBRE antes del deadline.
    4.10. mostrar_matriz_clases() / mostrar_matriz_combinada(): Mostrar matriz tabulada.
  5. Menú principal y flujo
    5.1. menu(): Mostrar lista de opciones (clases, tareas, horarios, salir).
    5.2. main(): Ejecutar funciones según opción seleccionada.
CASOS DE PRUEBA
Caso 1 — Acomodo automático por DÍAS (básico)
Entradas:
1. Opción 1 (Registrar materias)
   - 3 materias
   - Cálculo → 5 horas
   - Física → 4 horas
   - Programación → 6 horas
2. Opción 3 (Acomodo automático por DÍAS)
Salida esperada:
--- Horario por día (vista original) ---
Lunes: ['Cálculo', 'Cálculo', 'DESCANSO', 'Cálculo', 'Cálculo', 'Cálculo']
Martes: ['Física', 'Física', 'DESCANSO', 'Física', 'Física']
Miércoles: ['Programación', 'Programación', 'DESCANSO', 'Programación', 'Programación']
Jueves: ['Programación']
Viernes: []
Caso 2 — Intento de exceder 5 clases al acomodar MANUAL por DÍAS
Entradas:
1. Opción 1 (Registrar materias)
   - 2 materias
   - Redacción → 3 horas
   - Química → 4 horas
2. Opción 4 (Acomodo manual por DÍAS)
   - Redacción → Lunes
   - Química → Lunes (se llena) y Martes (restante)
Salida esperada:
Acomodo manual para Química (4 h/semana)
Día (Lunes/Martes/Miércoles/Jueves/Viernes): Lunes
Lunes ya tiene 5 horas. Elige otro día.
Día alterno: Martes
--- Horario por día (vista original) ---
Lunes: ['Redacción', 'Redacción', 'Redacción', 'Química', 'Química']
Martes: ['Química', 'Química']
Caso 3 — Tareas sobre MATRIZ + aviso por falta de espacio
Entradas:
1. Opción 1 (Registrar materias)
   - 2 materias
   - Cálculo → 5 horas
   - Física → 5 horas
2. Opción 6 (Acomodo AUTOMÁTICO MATRIZ)
3. Opción 8 (Registrar tarea)
   - Lista ejercicios (Cálculo, 3h, 2025-10-13 12:00)
4. Opción 8 (Registrar tarea)
   - Reporte (Física, 4h, 2025-10-14 12:00)
5. Opción 10 (Generar CALENDARIO sobre MATRIZ)
Salida esperada:
--- Calendario COMBINADO (clases + tareas) ---
Lun | ... TAREA: Lista ejer (Cálculo) ...
Mar | ... TAREA: Reporte (Física) ...
Aviso: horas de 'Reporte' pendientes por falta de espacio: 1
