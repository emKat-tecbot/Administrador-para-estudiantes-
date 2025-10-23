from calculadora_de_calificaciones import codigo_calculadorDeNotas
from Organizador_de_estudio import Organizador_de_estudio
from organizador_de_horario import codigo_horario
from administrador_de_tareas import codigoTareas
from Seguimiento_Alimenticio import Seguimiento_Alimenticio
from datetime import datetime

def menu():
  print("==BIENVENIDO AL ADMINISTRADOR PARA ESTUDIANTES==")
  print( f'''
  1. Calculadora de calificaciones
  2. Organizador de comida
  3. Organizador de estudio
  4. Organizador de horario
  5. Organizador de tareas
  6. Salir''')
  return str(input("Selecciona una opcion (1-5): "))

def main():
  while True:
    opcion = menu()
    if opcion in ["1","2","3","4","5", "6","7"]:
      opcion = int(opcion)
      break
    else:
      print("La opcion no esta en el menu intenta de nuevo por favor.")
  if opcion == 1:
    while True:
      optCal = codigo_calculadorDeNotas.menu()
      if optCal == 1:
        final = codigo_calculadorDeNotas.calPorClase()
        print(final)
      elif optCal == 2: 
        qNNPP = codigo_calculadorDeNotas.qNNPP(final[0])
        print(qNNPP[0])
      elif optCal == 3:
        codigo_calculadorDeNotas.porgresoDeNota ()
      elif optCal == 4:
        nmaterias = int(input("Por curiosidad, cuantas materias quisieras poner en tu base de Datos? "))
        i = 0
        j = 0
        dificultad = " "
        prioridad = []
        clase = []
        nota = []
        meta = []
        while i < nmaterias:
          final = codigo_calculadorDeNotas.calPorClase()
          while j < nmaterias:
            clase.append( final [1])
            nota.append(final[0])
            meta.append(codigo_calculadorDeNotas.qNNPP(final[0]))
            while type(dificultad) == str:
              dificultad = int(input("En la escala del 1 al 10, que tan dificil es tu clase? "))
              if type(dificultad) == str and dificultad < 1 or dificultad > 10:
                print("ERROR: respuesta no valida")
              if type(dificultad) == int and dificultad in [1,2,3,4,5,6,7,8,9,10]:
                prioridad.append(dificultad)
                break
            if type(dificultad) != str:
               print("Error!!!")
               break
            j += 1
          if j >= nmaterias:
            break
          i += 1
          if i >= nmaterias :
            baseDeNotas = codigo_calculadorDeNotas.baseDeDatosdeNotas(clase,nota,meta,prioridad)
            break
      if optCal == 5:
         ntemas = int(input("cuantos temas quisiera registrar? "))
         temas = []
         dificultad = []
         for i in range (ntemas):
            tema = input("agregue un tema: ")
            dificil = int(input("en la escala del 1 al 10, que tan dificil es el tema " + tema ": "))
            dificultad.append(dificil)
            temas.append(tema)
         horasLibres = int(input("en promedio cuanto tiempo libre tienes a la semana? "))
         hoy = int(input("que dia del mes estamos hoy? "))
         fechaExamen = int(input("que dia del mes es el examen? "))
         calendario = codigo_calculadorDeNotas.calendario(temas,horasLibres,dificultad,hoy,fechaExamen)
      if optCal == 6:
        #base de notas
        nmaterias = int(input("Por curiosidad, cuantas materias quisieras poner en tu base de Datos? "))
        i = 0
        j = 0
        dificultad = " "
        prioridad = []
        clase = []
        nota = []
        meta = []
        while i < nmaterias:
          final = codigo_calculadorDeNotas.calPorClase()
          while j < nmaterias:
            clase.append( final [1])
            nota.append(final[0])
            meta.append(codigo_calculadorDeNotas.qNNPP(final[0]))
            while type(dificultad) == str:
              dificultad = int(input("En la escala del 1 al 10, que tan dificil es tu clase? "))
              if type(dificultad) == str and dificultad < 1 or dificultad > 10:
                print("ERROR: respuesta no valida")
              if type(dificultad) == int and dificultad in [1,2,3,4,5,6,7,8,9,10]:
                prioridad.append(dificultad)
                break
            if type(dificultad) != str:
               print("Error!!!")
               break
            j += 1
          if j >= nmaterias:
            break
          i += 1
          if i >= nmaterias :
            baseDeNotas = codigo_calculadorDeNotas.baseDeDatosdeNotas(clase,nota,meta,prioridad)
        #calendario
        ntemas = int(input("cuantos temas quisiera registrar? "))
        temas = []
        dificultad = []
        for i in range (ntemas):
          tema = input("agregue un tema: ")
          dificil = int(input("en la escala del 1 al 10, que tan dificil es el tema " + tema ": "))
          dificultad.append(dificil)
          temas.append(tema)
        horasLibres = int(input("en promedio cuanto tiempo libre tienes a la semana? "))
        hoy = int(input("que dia del mes estamos hoy? "))
        fechaExamen = int(input("que dia del mes es el examen? "))
        calendario = codigo_calculadorDeNotas.calendario(temas,horasLibres,dificultad,hoy,fechaExamen)
        archivo = codigo_calculadorDeNotas.Archivo(baseDeNotas,calendario)
      elif optCal == 7:
         print("adios :D")
         break
            
  elif opcion == 2:
    Seguimiento_Alimenticio. asegurar_archivos()

    while True:
        print("\n--- MENÚ SEGUIMIENTO ALIMENTICIO ---")
        print("1. Registrar o editar meta de macronutrientes")
        print("2. Registrar nueva comida")
        print("3. Ver resumen del día (elige lo que comiste)")
        print("4. Sugerir menú aleatorio del día")
        print("5. Ver comidas guardadas")
        print("6. Guardar comida como favorita")
        print("7. Eliminar comida")
        print("8. Ver comidas favoritas")
        print("9. Ver cumplimiento total")
        print("10. Regresar al menú principal")

        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            Seguimiento_Alimenticio.guardar_meta()
        elif opcion == "2":
            Seguimiento_Alimenticio .registrar_comida()
        elif opcion == "3":
            Seguimiento_Alimenticio .resumen_dia()
        elif opcion == "4":
            Seguimiento_Alimenticio.sugerir_menu()
        elif opcion == "5":
            Seguimiento_Alimenticio .mostrar_comidas()
        elif opcion == "6":
            Seguimiento_Alimenticio .guardar_favoritas()
        elif opcion == "7":
            Seguimiento_Alimenticio .eliminar_comida()
        elif opcion == "8":
            Seguimiento_Alimenticio .mostrar_favoritas()
        elif opcion == "9":
            Seguimiento_Alimenticio .cumplimiento_total()
        elif opcion == "10":
            print("\nRegresando al menú principal...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
  elif opcion == 3:
    print("\n=== ORGANIZADOR DE ESTUDIO ===")
    usar_guardado = input("¿Cargar plan guardado? (s/n): ").strip().lower()

    plan = None
    if usar_guardado == "s":
        plan = cargar_plan()
        if plan is None:
            print("No se encontró archivo o está vacío. Vamos a crear uno nuevo.")
            usar_guardado = "n"

    if usar_guardado != "s":
        materia = input("Materia: ").strip()
        tipo = input("Tipo de curso (Calculo/Programacion/otro): ").strip()
        dificultad = int(input("Dificultad (1-5): ").strip())
        dias = int(input("Días restantes: ").strip())
        carga = int(input("Carga diaria (minutos): ").strip())

        plan = crear_plan(materia, tipo, dificultad, dias, carga)

        g = input("¿Guardar este plan? (s/n): ").strip().lower()
        if g == "s":
            guardar_plan(plan)
            print("Plan guardado en", "plan_estudio.txt")

    resultado = generar_horario(plan)
    indicadores = calcular_indicadores(plan, resultado["min_hechos"])

    print("\n--- Resumen del plan (minutos por sección) ---")
    print("Teoría:", plan["min_plan"][0], "| Práctica:", plan["min_plan"][1], "| Simulacro:", plan["min_plan"][2])

    print("\n--- Plan diario sugerido ---")
    for linea in resultado["lineas"]:
        print(linea)

    print("\n--- Matriz de bloques (por día) ---")
    indice = 0
    while indice < len(resultado["matriz"]):
        print("Día", (indice + 1), "->", resultado["matriz"][indice])
        indice = indice + 1

    print("\n=== INDICADORES ===")
    print("Materia:", indicadores["materia"])
    print("Tipo de curso:", indicadores["tipo_curso"])
    print("Días:", indicadores["dias_restantes"], "| Carga (min/día):", indicadores["carga_diaria_min"])
    print("Min plan (T/P/S):", indicadores["min_plan"])
    print("Min hechos (T/P/S):", indicadores["min_hechos"])
    print("Cumplimiento %:", indicadores["cumplimiento_pct"])
    print("Horas efectivas:", indicadores["horas_efectivas"])
    print("Estado:", indicadores["estado"])
    
  elif opcion == 4:
    while True:
      opcion_horario = menu()
      if opcion_horario == "1":
        materias = registrar_clases([
            {"nombre": "Cálculo", "horas_semanales": 3},
            {"nombre": "Física", "horas_semanales": 3},
            {"nombre": "Programación", "horas_semanales": 4}
        ])
        print(mostrar_clases(materias, as_text=True))

      elif opcion_horario == "2":
        matriz_clases = acomodo_automatico_matriz(materias)
        print(imprimir_matriz(matriz_clases, as_text=True))

      elif opcion_horario == "3":
        tareas = [
            registrar_tarea_calendario(
                "Hoja de Derivadas", "Cálculo", 3, datetime(2025, 10, 18, 23, 59),
                tipo="TAREA", prioridad=4, dificultad=2, energia="MEDIA"
            ),
            registrar_tarea_calendario(
                "Estudiar Newton", "Física", 2, datetime(2025, 10, 17, 20, 0),
                tipo="ESTUDIO", prioridad=5, dificultad=2, energia="ALTA"
            ),
            registrar_tarea_calendario(
                "Práctica listas", "Programación", 2, datetime(2025, 10, 19, 21, 0),
                tipo="PROYECTO", prioridad=3, dificultad=3, energia="MEDIA"
            )
        ]

      elif opcion_horario == "4":
        calendario = generar_calendario_tareas(
            matriz_clases, ordenar_tareas_por_deadline(tareas)
        )
        print(imprimir_matriz(calendario, "Calendario combinado", as_text=True))

      elif opcion_horario == "5":
        print(imprimir_reporte_carga(calendario, as_text=True))
        guardar_estado("estado.json", materias, calendario, tareas)
        print("Estado guardado en 'estado.json'.")

      elif opcion_horario == "6":
        materias, matriz_clases, tareas = cargar_estado("estado.json")
        print("Estado cargado.")

      elif opcion_horario == "7":
        
        exportar_txt("matriz.txt", matriz_clases)
        print("Matriz exportada a 'matriz.txt'.")

      elif opcion_horario == "0":
        print("Saliendo del programa...")
        break

      else:
        print("Opción inválida. Intenta nuevamente.")
    Codigo.main()
  elif opcion == 5:
    print("\n=== ADMINISTRADOR DE TAREAS ===")
    matriz_tareas = [[], [], []]
    opcion_tarea = ""
    while opcion_tarea != "5":
      print("MENÚ DE TAREAS")
      print("1. Agregar tareas")
      print("2. Ver tareas")
      print("3. Completar tarea")
      print("4. Eliminar tarea")
      print("5. Salir al menú principal")
      opcion_tarea = input("Elige una opción: ")
      if opcion_tarea == "1":
        matriz_tareas = agregar_tareas(matriz_tareas)
      elif opcion_tarea == "2":
        mostrar_tareas(matriz_tareas)
      elif opcion_tarea == "3":
        completar_tarea(matriz_tareas)
      elif opcion_tarea == "4":
        eliminar_tarea(matriz_tareas)
      elif opcion_tarea == "5":
        print("Saliendo del administrador de tareas...")
      else:
        print("Opción no válida, intenta de nuevo.")
        
  elif opcion == 6:
        print("Gracias, adios :D")


main()
