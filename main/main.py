from calculadora_de_callificaciones import calculadorDeNotas
from Organizador_de_estudio import OrganizadorDeEstudio
from organizador_de_horario import Codigo
from organizador_de_comida import CodigoAvanceMacroComidas
from administrador de tareas import menu

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
    calculadorDeNotas.main()
  elif opcion == 2:
    CodigoAvanceMacroComidas.main()
    print()
  elif opcion == 3:
    OrganizadorDeEstudio.main()
  elif opcion == 4:
    Codigo.main()
  elif opcion == 5:

    
def mainTarea():
    tareas = []
    while True:
        menuTarea()
        opcion = input("Selecciona una opción: ")
        if opcion == "1":
            agregar_tareas(tareas)
        elif opcion == "2":
            mostrar_tareas(tareas)
        elif opcion == "3":
            completar_tarea(tareas)
        elif opcion == "4":
            print("Adiós")
            break
        else:
            print("Opción no válida.")

mainTarea()


    elif opcion == 6:
    print("Gracias, adios :D")

main()
