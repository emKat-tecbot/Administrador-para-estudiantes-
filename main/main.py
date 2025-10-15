from calculadora_de_callificaciones import calculadorDeNotas
from Organizador_de_estudio import Organizador_de_Estudio
from organizador_de_horario import Codigo
from administrador_de_tareas import menu
from calculadora_de_callificaciones import calificacionMenu
from organizador_de_horario import horario_menu
from administrador_de_tareas import codigoTareas
from Seguimiento_Alimenticio import Seguimiento_Alimenticio
from Seguimiento_Alimenticio import Seguimiento_Alimenticio_Menu

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
      calificacionMenu.menu()
      optCal = calificacionMenu.menu()
      if optCal == 1:
        final = calculadorDeNotas.calPorClase()
      elif optCal == 2: 
        qNNPP = calculadorDeNotas.qNNPP(final)
      elif optCal == 3:
        calculadorDeNotas.porgresoDeNota ()
      elif optCal == 4:
        calculadorDeNotas.tiempoDeEstudio(final,qNNPP)
      else:
          break
  elif opcion == 2:
     print("\n=== SEGUIMIENTO ALIMENTICIO ===")
     Seguimiento_Alimenticio_Menu.menu()  
     Seguimiento_Alimenticio.main()      
  elif opcion == 3:
    OrganizadorDeEstudio.iniciar()
  elif opcion == 4:
    from datetime import datetime
from organizador_horario_universitario import *

while True:
    opcion = menu()
    if opcion == "1":
        materias = registrar_clases([
            {"nombre": "Física", "horas_semanales": 4},
            {"nombre": "Cálculo", "horas_semanales": 3},
            {"nombre": "Programación", "horas_semanales": 5}
        ])
    elif opcion == "2":
        print(mostrar_clases(materias, as_text=True))
    elif opcion == "3":
        dias_automatico = acomodo_automatico_dias(materias)
    elif opcion == "4":
        asignaciones = [("Física", "Lunes"), ("Cálculo", "Martes")]
        dias_manual = acomodo_manual_dias(materias, asignaciones)
    elif opcion == "5":
        print(mostrar_acomodo(dias_automatico, as_text=True))
    elif opcion == "6":
        matriz, texto_matriz = acomodo_automatico_matriz(materias, as_text=True)
        print(texto_matriz)
    elif opcion == "7":
        matriz, texto_manual = acomodo_automatico_matriz(materias, as_text=True)
        print(texto_manual)
    elif opcion == "8":
        tareas = [
            registrar_tarea_calendario("Proyecto Final", "Programación", 3, datetime(2025,10,25))
        ]
    elif opcion == "9":
        if tareas:
            for t in tareas:
                print(f"{t['titulo']} ({t['materia']}) - {t['horas_estimadas']}h - {t['deadline']}")
        else:
            print("No hay tareas registradas.")
    elif opcion == "10":
        combinado = generar_calendario_tareas(matriz, tareas)
        print(imprimir_matriz(combinado, titulo="Calendario combinado", as_text=True))
    elif opcion == "11":
        print(imprimir_matriz(matriz, as_text=True))
    elif opcion == "12":
        reporte = imprimir_reporte_carga(matriz, as_text=True)
        print(reporte)
        guardar_estado("estado.json", materias, matriz, tareas)
        print("Estado guardado.")
    elif opcion == "13":
        materias, matriz, tareas = cargar_estado("estado.json")
        print("Estado cargado correctamente.")
    elif opcion == "14":
        exportar_txt("horario.txt", matriz)
        print("Matriz exportada a horario.txt")
    elif opcion == "0":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")
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
