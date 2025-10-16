from calculadora_de_calificaciones import codigo_calculadorDeNotas
from Organizador_de_estudio import Organizador_de_Estudio
from organizador_de_horario import Codigo
from administrador_de_tareas import menu
from calculadora_de_calificaciones import calificacionMenu
from organizador_de_horario import horario_menu
from administrador_de_tareas import codigoTareas
from Seguimiento_Alimenticio import Seguimiento_Alimenticio
from Seguimiento_Alimenticio import Seguimiento_Alimenticio_Menu
from datetime import datetime
from organizador_horario_universitario import *

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
    if opcion in ["1","2","3","4","5"]:
      opcion = int(opcion)
      break
    else:
      print("La opcion no esta en el menu intenta de nuevo por favor.")
  if opcion == 1:
    while True:
      codigo_calculadorDeNotas.menu()
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
        lista = []
        cont = 0
        dificultad = " "
        prioridad = []
        clase = []
        nota = []
        meta = []
        while i < len(final[0]):
          while j < len (final[0]):
            clase.append( final [i])
            nota.append(final[i + 1])
            meta.append(qNNPP[1])
            while type(dificultad) == str:
              dificultad = int(input("En la escala del 1 al 10, que tan dificil es tu clase? "))
              if type(dificultad) == str and dificultad < 1 or dificultad > 10:
                print("ERROR: respuesta no valida")
              if type(dificultad) == int and dificultad in [1,2,3,4,5,6,7,8,9,10]:
                prioridad.append(dificultad)
                break
            j += 1
          i += 1
          lista.append([clase,nota,meta,dificultad])
        print(lista)   
  elif opcion == 2:
     print("\n=== SEGUIMIENTO ALIMENTICIO ===")
     Seguimiento_Alimenticio_Menu.menu()  
     Seguimiento_Alimenticio.main()      
  elif opcion == 3:
    OrganizadorDeEstudio.iniciar()
  elif opcion == 4:
    while True:
    opcion = menu()
    if opcion == "1":
        materias = registrar_clases([
            {"nombre": "Cálculo", "horas_semanales": 3},
            {"nombre": "Física", "horas_semanales": 3},
            {"nombre": "Programación", "horas_semanales": 4}
        ])
        print(mostrar_clases(materias, as_text=True))

    elif opcion == "2":
        matriz_clases = acomodo_automatico_matriz(materias)
        print(imprimir_matriz(matriz_clases, as_text=True))

    elif opcion == "3":
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

    elif opcion == "4":
        calendario = generar_calendario_tareas(
            matriz_clases, ordenar_tareas_por_deadline(tareas)
        )
        print(imprimir_matriz(calendario, "Calendario combinado", as_text=True))

    elif opcion == "5":
        print(imprimir_reporte_carga(calendario, as_text=True))
        guardar_estado("estado.json", materias, calendario, tareas)
        print("Estado guardado en 'estado.json'.")

    elif opcion == "6":
        materias, matriz_clases, tareas = cargar_estado("estado.json")
        print("Estado cargado.")

    elif opcion == "7":
        exportar_txt("matriz.txt", matriz_clases)
        print("Matriz exportada a 'matriz.txt'.")

    elif opcion == "0":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Intenta nuevamente.")
    Codigo.main()
  elif opcion == 5:
    tareas = []
    while True:
      menuTarea()
      opcion = input("Selecciona una opción: ")
      if opcion == "1":
        codigoTareas.agregar_tareas(tareas)
      elif opcion == "2":
          codigoTareas.mostrar_tareas(tareas)
      elif opcion == "3":
          codigoTareas.completar_tarea(tareas)
      elif opcion == "4":
          print("Adiós")
          break
      else:
          print("Opción no válida.")
  elif opcion == 6:
    print("Gracias, adios :D")

main()
