"""
Programa que permite agregar tareas, verlas, completarlas, 
eliminarlas y ver estadísticas usando listas (matrices).
"""

"""
Casos de prueba:
Categorías disponibles:
1. Escuela
2. Casa
3. Personal
Selecciona una categoría: 1
Escribe la tarea: estudiar matemáticas
Tarea agregada
¿Quieres agregar otra tarea? (si/no): si
Selecciona una categoría: 2
Escribe la tarea: lavar ropa
Tarea agregada
¿Quieres agregar otra tarea? (si/no): no

"""
def agregar_tareas(matriz_tareas):
    print("Categorías disponibles:")
    print("1. Escuela")
    print("2. Casa")
    print("3. Personal")

    repetir = "si"
    while repetir == "si":
        opcion = input("Selecciona una categoría: ")
        if opcion == "1" or opcion == "2" or opcion == "3":
            categoria = int(opcion) - 1
            nombre = input("Escribe la tarea: ")
            if nombre != "":
                tarea = [nombre, "Pendiente"]   
                matriz_tareas[categoria].append(tarea)
                print("Tarea agregada")
            else:
                print("No se puede agregar una tarea vacía")
        else:
            print("Opción no válida.")
        repetir = input("¿Quieres agregar otra tarea? (si/no): ")
    return matriz_tareas


"""
Casos de prueba: 
LISTA DE TAREAS
Categoría: Escuela
1. estudiar matemáticas - Pendiente
Categoría: Casa
1. lavar ropa - Pendiente

Categoría: Escuela
1. biologia - Completada
Categoría: Casa
1. lavar - Pendiente

LISTA DE TAREAS
Categoría: Casa
1. lavar - Pendiente
"""
def mostrar_tareas(matriz_tareas):
    categorias = ["Escuela", "Casa", "Personal"]
    print("LISTA DE TAREAS")
    hay_tareas = False
    for i in range(len(matriz_tareas)): 
        if len(matriz_tareas[i]) > 0:
            print("Categoría:", categorias[i])
            for j in range(len(matriz_tareas[i])):  
                tarea = matriz_tareas[i][j]
                print(str(j + 1) + ". " + tarea[0] + " - " + tarea[1])
            hay_tareas = True

    if hay_tareas == False:
        print("No hay tareas registradas")
    print()

"""
Casos de prueba:
LISTA DE TAREAS
Categoría: Escuela
1. biologia - Pendiente
Categoría: Casa
1. lavar - Pendiente

Selecciona la categoría: 1
Número de la tarea a completar: 1
Tarea completada
"""
def completar_tarea(matriz_tareas):
    mostrar_tareas(matriz_tareas)
    cat = input("Selecciona la categoría: ")
    num = input("Número de la tarea a completar: ")
    cat = int(cat)
    num = int(num)
    if cat >= 1 and cat <= 3:
        if num >= 1 and num <= len(matriz_tareas[cat - 1]):
            matriz_tareas[cat - 1][num - 1][1] = "Completada"
            print("Tarea completada")
        else:
            print("Número de tarea no válido")
    else:
        print("Categoría no válida")


"""
Casos de prueba
LISTA DE TAREAS
Categoría: Escuela
1. biologia - Completada
Categoría: Casa
1. lavar - Pendiente

Selecciona la categoría: 1
Número de la tarea a eliminar: 1
Tarea eliminada

"""
def eliminar_tarea(matriz_tareas):
    mostrar_tareas(matriz_tareas)
    cat = input("Selecciona la categoría: ")
    num = input("Número de la tarea a eliminar: ")
    cat = int(cat)
    num = int(num)

    if cat >= 1 and cat <= 3:
        if num >= 1 and num <= len(matriz_tareas[cat - 1]):
            nueva_lista = []
            i = 0
            while i < len(matriz_tareas[cat - 1]):
                if i != num - 1:
                    nueva_lista.append(matriz_tareas[cat - 1][i])
                i = i + 1
            matriz_tareas[cat - 1] = nueva_lista
            print("Tarea eliminada")
        else:
            print("Número de tarea no válido")
    else:
        print("Categoría no válida")
        

def menuTarea():
    matriz_tareas = [[], [], []]
    opcion = ""
    while opcion != "5":
        print("MENÚ")
        print("1. Agregar tareas")
        print("2. Ver tareas")
        print("3. Completar tarea")
        print("4. Eliminar tarea")
        print("5. Salir")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            matriz_tareas = agregar_tareas(matriz_tareas)
        elif opcion == "2":
            mostrar_tareas(matriz_tareas)
        elif opcion == "3":
            completar_tarea(matriz_tareas)
        elif opcion == "4":
            eliminar_tarea(matriz_tareas)
        elif opcion == "5":
            print("Saliendo del programa")
        else:
            print("Opción no válida")

