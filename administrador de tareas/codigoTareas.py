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
Entrada: "Leer libro", "si", "Estudiar biología", "no"
Salida: Escribe la nueva tarea: leer libro
Tarea agregada.
¿Deseas agregar otra tarea? Escribe 'si' o 'no': si
Escribe la nueva tarea: estudiar biologia
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
Entrada: "Leer libro", "si", "Estudiar biología", "no"
Salida: -- Lista de tareas --
1. leer libro - Pendiente
2. estudiar biologia - Pendiente

Si ya completaste una tarea, y vuelves a seleccionar la opción 2, te mostrara lo siguiente:
-- Lista de tareas --
1. leer libro - Pendiente
2. estudiar biologia - Completada
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



