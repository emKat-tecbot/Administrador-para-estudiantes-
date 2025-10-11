from calculadora_de_callificaciones import calculadorDeNotas
from Organizador_de_estudio import OrganizadorDeEstudio
from organizador_de_horario import Codigo
from organizador_de_comida import CodigoAvanceMacroComidas
from administrador_de_tareas import menu
from calculadora_de_callificaciones import calificacionMenu
from organizador_de_horario import horario-menu
from administrador_de_tareas import codigoTareas
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
      print(type(opcion))
      break
    else:
      print("La opcion no esta en el menu intenta de nuevo por favor.")
  if opcion == 1:
    while True:
      optCal = calificacionMenu.menu
      if optCal == 1:
        final = calculadora_de_callificaciones.calPorClase()
      elif optCal == 2: 
        qNNPP = calculadora_de_callificaciones.qNNPP(final)
      elif optCal == 3:
        calculadora_de_callificaciones.porgresoDeNota ()
      elif optCal == 4:
        calculadora_de_callificaciones.tiempoDeEstudio(final,qNNPP)
      else:
        break
  elif opcion == 2:
    CodigoAvanceMacroComidas.main()
    print()
  elif opcion == 3:
    OrganizadorDeEstudio.main()
  elif opcion == 4:
    while True:
      horario-menu.menu()
      if op == 1:
        funcion_registrar_clases.registrar_clases()
      elif op== 2:
        funcion_mostrar_clases.mostrar_clases(materias)
      elif op== 3:
        funcion_acomodo_automatico.acomodo_acomodo_automatico_dias(materias)
      elif op== 4:
        funcion_acomodo_manual.acomodo_manual_dias(materias)
      elif op== 5:
        funcion_mostrar_acomodo_dias.mostrar_acomodo(dias_ultimo)
      elif op== 6:
        funcion_acomodo_automatico_MATRIZ.acomodo_acomodo_automatico_matriz(materias)
      elif op== 7:
        funcion_acomodo_manual_MATRIZ.acomodo_manual_matriz(materias)
      elif op== 8:
        funcion:registrar_tarea.registrar_tarea_calendario()
      elif op== 9:
        funcion:mostrar_tareas.mostrar_tareas(tareas)
      elif op== 10:
        funcion:generar_calendario.generar_calendario_tareas(matriz_clases,tareas)
      elif op== 11:
        funcion:mostrar_calendario.mostrar_matriz_clases(matriz_clases)
      elif op== 12:
        break
      else
      print("Opcion no valida intenta de nuevo")
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
