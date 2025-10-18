import matplotlib.pyplot as plt
import random

def guardar_meta():
    print("\n--- Establecer o editar meta diaria ---")
    prote = input("Gramos de proteína: ")
    carb = input("Gramos de carbohidratos: ")
    grasa = input("Gramos de grasa: ")

    archivo = open("meta.txt", "w")
    archivo.write(prote + "," + carb + "," + grasa)
    archivo.close()
    print("Meta guardada correctamente.\n")

def leer_meta():
    archivo = open("meta.txt", "r")
    linea = archivo.readline().strip()
    archivo.close()
    datos = linea.split(",")
    prote = float(datos[0])
    carb = float(datos[1])
    grasa = float(datos[2])
    return prote, carb, grasa

def registrar_comida():
    print("\n--- Registrar nueva comida ---")
    nombre = input("Nombre de la comida: ")
    tipo = input("Tipo (batido/almuerzo/cena): ").lower()
    prote = input("Proteína (g): ")
    carb = input("Carbohidratos (g): ")
    grasa = input("Grasas (g): ")
    ingredientes = input("Ingredientes (separados por coma): ")

    archivo = open("comidas.txt", "a")
    linea = nombre + "," + tipo + "," + prote + "," + carb + "," + grasa + "," + ingredientes + "\n"
    archivo.write(linea)
    archivo.close()
    print("Comida registrada correctamente.\n")

def mostrar_comidas():
    print("\n--- Comidas registradas ---")
    archivo = open("comidas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    tipo = input("¿Qué tipo deseas ver? (batido/almuerzo/cena/todas): ").lower()

    contador = 1
    for linea in lineas:
        datos = linea.strip().split(",")
        if tipo == "todas" or tipo == datos[1]:
            print(str(contador) + ") " + datos[0] + " (" + datos[1] + ") → P:" + datos[2] + " C:" + datos[3] + " G:" + datos[4])
            contador += 1
    print()

def resumen_dia():
    print("\n--- Resumen del Día ---")
    meta_p, meta_c, meta_g = leer_meta()
    archivo = open("comidas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    total_p = 0
    total_c = 0
    total_g = 0

    for linea in lineas:
        datos = linea.strip().split(",")
        total_p += float(datos[2])
        total_c += float(datos[3])
        total_g += float(datos[4])

    print("Consumido: P:", total_p, " C:", total_c, " G:", total_g)
    print("Falta: P:", meta_p - total_p, " C:", meta_c - total_c, " G:", meta_g - total_g, "\n")

def sugerir_menu():
    print("\n--- Sugerencia del Día ---")
    archivo = open("comidas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    tipos = ["batido", "almuerzo", "cena"]

    for tipo in tipos:
        opciones = []
        for linea in lineas:
            datos = linea.strip().split(",")
            if datos[1] == tipo:
                opciones.append(datos)
        if len(opciones) > 0:
            elegido = random.choice(opciones)
            print(tipo.title() + ": " + elegido[0] + " → P:" + elegido[2] + " C:" + elegido[3] + " G:" + elegido[4])
    print()

def eliminar_comida():
    print("\n--- Eliminar comida ---")
    mostrar_comidas()
    numero = int(input("Número de comida a eliminar: "))

    archivo = open("comidas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    nuevo = []
    contador = 1
    for linea in lineas:
        if contador != numero:
            nuevo.append(linea)
        contador += 1

    archivo = open("comidas.txt", "w")
    for linea in nuevo:
        archivo.write(linea)
    archivo.close()
    print("Comida eliminada correctamente.\n")

def guardar_favoritas():
    print("\n--- Guardar comida favorita ---")
    mostrar_comidas()
    numero = int(input("Número de comida favorita: "))

    archivo = open("comidas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    archivo_fav = open("favoritas.txt", "a")
    archivo_fav.write(lineas[numero - 1])
    archivo_fav.close()
    print("Comida añadida a favoritas.\n")

def verificar_cumplimiento():
    print("\n--- Verificación de cumplimiento semanal ---")
    dia = input("Introduce el día actual (lunes, martes, miercoles, jueves, viernes, sabado, domingo): ").lower()

    meta_p, meta_c, meta_g = leer_meta()
    archivo = open("comidas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    total_p = 0
    total_c = 0
    total_g = 0
    for linea in lineas:
        datos = linea.strip().split(",")
        total_p += float(datos[2])
        total_c += float(datos[3])
        total_g += float(datos[4])

 
    if total_p >= meta_p and total_c >= meta_c and total_g >= meta_g:
        resultado = "cumplida"
        print("Meta diaria cumplida.")
    else:
        resultado = "no cumplida"
        print("Meta diaria no cumplida.")

 
    archivo = open("historial.txt", "a")
    archivo.write(dia + "," + resultado + "\n")
    archivo.close()


    archivo = open("historial.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    print("\n--- Resumen semanal ---")
    matriz = []
    for linea in lineas:
        datos = linea.strip().split(",")
        matriz.append(datos)

    for fila in matriz:
        print(f"{fila[0].capitalize()}: {fila[1].capitalize()}")
    print()

def graficar_progreso():
    print("\n--- Gráfico de Progreso ---")
    meta_p, meta_c, meta_g = leer_meta()
    archivo = open("comidas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()

    total_p = 0
    total_c = 0
    total_g = 0
    for linea in lineas:
        datos = linea.strip().split(",")
        total_p += float(datos[2])
        total_c += float(datos[3])
        total_g += float(datos[4])

    etiquetas = ['Proteína', 'Carbohidratos', 'Grasa']
    consumido = [total_p, total_c, total_g]
    meta = [meta_p, meta_c, meta_g]

    plt.bar(etiquetas, meta, color='gray', label='Meta')
    plt.bar(etiquetas, consumido, color='green', label='Consumido')
    plt.legend()
    plt.title("Comparación Meta vs Consumido")
    plt.show()

