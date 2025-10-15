''' 
Permite agregar tareas, verlas y marcar como completadas
'''
def agregar_tareas(tareas):
    while True:
        nombre = input("Escribe la nueva tarea: ")
        if nombre == "":
            print("No se puede agregar")
        else:
            tareas.append({"nombre": nombre, "estado": "Pendiente"})
            print("Tarea agregada.")
        otra = input("¿Deseas agregar otra tarea? Escribe 'si' o 'no': ")
        if otra != "si":
            break
    return tareas
'''
Caso de prueba:
Entrada: "tarea de programación", "si", "tarea de artes", "si", "practicar ejercicios mate", "no"
Salida: Escribe la nueva tarea: tarea de programación
Tarea agregada.
¿Deseas agregar otra tarea? Escribe 'si' o 'no': si
Escribe la nueva tarea: tarea de artes
Tarea agregada. 
¿Deseas agregar otra tarea? Escribe 'si' o 'no': si
Escribe la nueva tarea: practicar ejercicios mate
Tarea agregada. 
¿Deseas agregar otra tarea? Escribe 'si' o 'no': no
--- MENÚ ---
'''

def mostrar_tareas(tareas):
    if len(tareas) == 0:
        print("No tienes tareas.")
        return
    print("-- Lista de tareas --")
    i = 0
    while i < len(tareas):
        nombre = tareas[i]["nombre"]
        estado = tareas[i]["estado"]
        print(str(i + 1) + ". " + nombre + " - " + estado)
        i += 1
'''
Caso de prueba:
Entrada: "tarea de programación", "si", "tarea de artes", "practicar ejercicios mate, "no"
Salida: -- Lista de tareas --
1. tarea de programación - Pendiente
2. tarea de artes - Pendiente
3. practicar ejercicios mate - Pendiente

Por ejemplo si ya completaste una tarea, seleccionando el numero 2 que en este caso es tarea de artes, 
y vuelves a seleccionar la opción 2, te mostrara lo siguiente:
-- Lista de tareas --
1. tarea de programación - Pendiente
2. tarea de artes - Completada
3. practicar ejercicios mate - Pendiente
'''

def completar_tarea(tareas):
    if len(tareas) == 0:
        print("No hay tareas para completar.")
        return
    mostrar_tareas(tareas)
    numero = input("Número de la tarea a completar: ")
    numero = int(numero)  
    if numero < 1 or numero > len(tareas):
        print("Número inválido.")
    else:
        tareas[numero-1]["estado"] = "Completada"
        print("Tarea completada.")
'''
Caso de prueba:
Entrada: "Número de la tarea a completar:" 2 
Salida: Tarea completada.
'''




