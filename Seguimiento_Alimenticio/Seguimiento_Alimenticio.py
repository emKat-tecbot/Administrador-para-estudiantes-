import random

def asegurar_archivos():
    """Crea los archivos si no existen (vacíos)."""
    open("meta.txt", "a").close()
    open("comidas.txt", "a").close()
    open("favoritas.txt", "a").close()
    open("historial.txt", "a").close()

def guardar_meta():
    asegurar_archivos()
    print("\n--- Establecer o editar meta diaria ---")
    prote = input("Gramos de proteína: ")
    carb = input("Gramos de carbohidratos: ")
    grasa = input("Gramos de grasa: ")

    archivo = open("meta.txt", "w")
    archivo.write(prote + "," + carb + "," + grasa)
    archivo.close()
    print("Meta guardada correctamente.\n")


def leer_meta():
    asegurar_archivos()
    f = open("meta.txt", "r")
    linea = f.readline().strip()
    f.close()
    if linea == "":
        return 0.0, 0.0, 0.0
    datos = linea.split(",")
    return float(datos[0]), float(datos[1]), float(datos[2])

def registrar_comida():
    asegurar_archivos()
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
    asegurar_archivos()
    print("\n--- Comidas registradas ---")
    archivo = open("comidas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    if len(lineas) == 0:
        print("No hay comidas registradas.\n")
        return

    tipo = input("¿Qué tipo deseas ver? (batido/almuerzo/cena/todas): ").lower()

    contador = 1
    i = 0
    while i < len(lineas):
        datos = lineas[i].strip().split(",")
        if tipo == "todas" or tipo == datos[1]:
            print(str(contador) + ") " + datos[0] + " (" + datos[1] + ") → P:" + datos[2] + " C:" + datos[3] + " G:" + datos[4])
            contador += 1
        i += 1
    print()


def resumen_dia():
    asegurar_archivos()

    meta_p, meta_c, meta_g = leer_meta()
    if meta_p == 0.0 and meta_c == 0.0 and meta_g == 0.0:
        print("\nPrimero registra tu meta en la opción 1 del menú.\n")
        return

    f = open("comidas.txt", "r")
    lineas = f.readlines()
    f.close()
    if len(lineas) == 0:
        print("\nNo hay comidas registradas. Usa la opción 2 para registrar alguna.\n")
        return

    print("\n--- Selecciona lo que comiste hoy ---")
    i = 1
    while i <= len(lineas):
        datos = lineas[i-1].strip().split(",")
        print(str(i) + ") " + datos[0] + " (" + datos[1] + ") → P:" + datos[2] + " C:" + datos[3] + " G:" + datos[4])
        i += 1

    sel = input("Números separados por comas (ej. 1,3,5). Enter si ninguna: ").replace(" ", "")

    total_p = 0.0
    total_c = 0.0
    total_g = 0.0

    if sel != "":
        nums = sel.split(",")
        j = 0
        while j < len(nums):
            n = nums[j]
            if n.isdigit():
                idx = int(n)
                if 1 <= idx <= len(lineas):
                    datos = lineas[idx - 1].strip().split(",")
                    total_p += float(datos[2])
                    total_c += float(datos[3])
                    total_g += float(datos[4])
            j += 1

    print("\nConsumido hoy  →  P:", total_p, " C:", total_c, " G:", total_g)
    print("Meta diaria    →  P:", meta_p, " C:", meta_c, " G:", meta_g)

    if total_p >= meta_p and total_c >= meta_c and total_g >= meta_g:
        estado = "cumplida"
        print(" Meta diaria CUMPLIDA.")
    else:
        estado = "no cumplida"
        print(" Meta diaria NO cumplida.")


    dia = input("Escribe el día (lunes, martes, miercoles, jueves, viernes, sabado, domingo): ").lower()
    h = open("historial.txt", "a")
    h.write(dia + "," + estado + "\n")
    h.close()
    print("Registro guardado en historial.\n")

def sugerir_menu():
    asegurar_archivos()
    print("\n--- Sugerencia del Día ---")
    archivo = open("comidas.txt", "r")
    lineas = archivo.readlines()
    archivo.close()
    if len(lineas) == 0:
        print("No hay comidas registradas.\n")
        return

    tipos = ["batido", "almuerzo", "cena"]
    total_p = 0.0
    total_c = 0.0
    total_g = 0.0

    t = 0
    while t < len(tipos):
        tipo = tipos[t]
        opciones = []
        i = 0
        while i < len(lineas):
            datos = lineas[i].strip().split(",")
            if len(datos) >= 5 and datos[1] == tipo:
                opciones.append(datos)
            i += 1

        if len(opciones) > 0:
            elegido = random.choice(opciones)
            print(tipo.title() + ": " + elegido[0] + " → P:" + elegido[2] + " C:" + elegido[3] + " G:" + elegido[4])
            total_p += float(elegido[2])
            total_c += float(elegido[3])
            total_g += float(elegido[4])
        t += 1

    print("\nTotales del menú sugerido → P:" + str(total_p) + " C:" + str(total_c) + " G:" + str(total_g) + "\n")

def eliminar_comida():
    asegurar_archivos()
    print("\n--- Eliminar comida ---")

    f = open("comidas.txt", "r")
    lineas = f.readlines()
    f.close()
    if len(lineas) == 0:
        print("No hay comidas registradas.\n")
        return

    i = 0
    while i < len(lineas):
        datos = lineas[i].strip().split(",")
        print(str(i + 1) + ") " + datos[0] + " (" + datos[1] + ") → P:" + datos[2] + " C:" + datos[3] + " G:" + datos[4])
        i += 1

    numero = int(input("Número de comida a eliminar: "))

    nuevo = []
    i = 0
    while i < len(lineas):
        if (i + 1) != numero:
            nuevo.append(lineas[i])
        i += 1

    f = open("comidas.txt", "w")
    j = 0
    while j < len(nuevo):
        f.write(nuevo[j])
        j += 1
    f.close()
    print("Comida eliminada correctamente.\n")


def guardar_favoritas():
    asegurar_archivos()
    print("\n--- Guardar comida favorita ---")

    f = open("comidas.txt", "r")
    lineas = f.readlines()
    f.close()
    if len(lineas) == 0:
        print("No hay comidas registradas.\n")
        return

    i = 0
    while i < len(lineas):
        datos = lineas[i].strip().split(",")
        print(str(i + 1) + ") " + datos[0] + " (" + datos[1] + ") → P:" + datos[2] + " C:" + datos[3] + " G:" + datos[4])
        i += 1

    numero = int(input("Número de comida favorita: "))

    fav = open("favoritas.txt", "a")
    fav.write(lineas[numero - 1])
    fav.close()
    print("Comida añadida a favoritas.\n")


def mostrar_favoritas():
    """Muestra el listado de favoritas."""
    asegurar_archivos()
    print("\n--- Comidas favoritas ---")
    f = open("favoritas.txt", "r")
    lineas = f.readlines()
    f.close()
    if len(lineas) == 0:
        print("No hay comidas favoritas aún.\n")
        return

    i = 0
    while i < len(lineas):
        datos = lineas[i].strip().split(",")
        print(str(i + 1) + ") " + datos[0] + " (" + datos[1] + ") → P:" + datos[2] + " C:" + datos[3] + " G:" + datos[4])
        i += 1
    print()


def cumplimiento_total():

    asegurar_archivos()
    print("\n--- Cumplimiento Total ---")

    f = open("historial.txt", "r")
    lineas = f.readlines()
    f.close()

    total_dias = len(lineas)
    cumplidos = 0
    no_cumplidos = 0

    i = 0
    while i < len(lineas):
        datos = lineas[i].strip().split(",")
        if len(datos) > 1:
            estado = datos[1].lower()
            if estado == "cumplida":
                cumplidos += 1
            elif estado == "no cumplida":
                no_cumplidos += 1
        i += 1

    if total_dias > 0:
        porcentaje_cumplidos = (cumplidos * 100.0) / total_dias
        porcentaje_no = (no_cumplidos * 100.0) / total_dias
    else:
        porcentaje_cumplidos = 0.0
        porcentaje_no = 0.0

    print("Total de días registrados:", total_dias)
    print("Días cumplidos:", cumplidos, "(", format(porcentaje_cumplidos, ".2f"), "%)")
    print("Días no cumplidos:", no_cumplidos, "(", format(porcentaje_no, ".2f"), "%)\n")
