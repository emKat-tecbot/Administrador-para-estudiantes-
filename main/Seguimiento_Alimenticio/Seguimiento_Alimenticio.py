# ------------------------------------------------------------
# Proyecto: Seguimiento Alimenticio
# Autor: David García Zamora
# ------------------------------------------------------------
# Este programa permite registrar comidas y calcular el total
# de proteínas, carbohidratos y grasas del día. También compara
# los resultados con los objetivos del usuario.
# ------------------------------------------------------------


def registrarComida(nombre):
    print(f"\n--- {nombre} ---")
    porcion = input("¿Qué equivale una porción? (ej. 100g, 1 taza): ")
    prote = float(input("Proteínas por porción (g): "))
    carb  = float(input("Carbohidratos por porción (g): "))
    gras  = float(input("Grasas por porción (g): "))
    porciones = float(input("¿Cuántas porciones consumiste hoy?: "))

    consP = prote * porciones
    consC = carb  * porciones
    consG = gras  * porciones

    comida = [nombre, porcion, consP, consC, consG]
    return comida



def mostrarComidas(lista):
    if len(lista) == 0:
        print("No hay comidas registradas.")
    else:
        print("\n--- Comidas Registradas ---")
        for i in range(len(lista)):
            print(f"{i+1}. {lista[i][0]} ({lista[i][1]}) - P:{lista[i][2]}g C:{lista[i][3]}g G:{lista[i][4]}g")



def calcularTotales(lista):
    totalP = totalC = totalG = 0
    for i in range(len(lista)):
        totalP += lista[i][2]
        totalC += lista[i][3]
        totalG += lista[i][4]
    return [totalP, totalC, totalG]



def promedioMacros(lista):
    if len(lista) == 0:
        return [0, 0, 0]
    total = calcularTotales(lista)
    divisor = len(lista)
    promP = total[0] / divisor
    promC = total[1] / divisor
    promG = total[2] / divisor
    return [promP, promC, promG]



def evaluarDieta(totales, objetivos):
    print("\n--- Comparación con objetivos ---")
    etiquetas = ["Proteínas", "Carbohidratos", "Grasas"]
    for i in range(3):
        if totales[i] < objetivos[i]:
            print(f"{etiquetas[i]}: por debajo del objetivo ({totales[i]} / {objetivos[i]} g)")
        elif totales[i] > objetivos[i]:
            print(f"{etiquetas[i]}: por encima del objetivo ({totales[i]} / {objetivos[i]} g)")
        else:
            print(f"{etiquetas[i]}: justo en el objetivo ({totales[i]} g)")

    if totales[0] > totales[1] and totales[0] > totales[2]:
        print("Dieta alta en proteínas.")
    elif totales[1] > totales[0] and totales[1] > totales[2]:
        print("Dieta alta en carbohidratos.")
    elif totales[2] > totales[0] and totales[2] > totales[1]:
        print("Dieta alta en grasas.")
    else:
        print("Dieta balanceada.")



def pruebas():
    comidas = [
        ["Pollo", "100g", 25, 0, 3],
        ["Arroz", "1 taza", 5, 45, 1],
        ["Aguacate", "50g", 2, 3, 8]
    ]
    print("\nPrueba: comidas registradas de ejemplo")
    mostrarComidas(comidas)
    totales = calcularTotales(comidas)
    print("\nTotales de prueba:", totales)
    prom = promedioMacros(comidas)
    print("Promedios de prueba:", prom)
    objetivos = [60, 120, 50]
    evaluarDieta(totales, objetivos)
    
def main():
    comidas = []
    
    print("\n--- Objetivos diarios ---")
    objP = float(input("Proteínas necesarias (g): "))
    objC = float(input("Carbohidratos necesarios (g): "))
    objG = float(input("Grasas necesarias (g): "))
    objetivos = [objP, objC, objG]

    
    while True:
        
        opcion = input("Selecciona una opción (1-7): ")

        if opcion == "1":
            nombre = input("Nombre de la comida (ej. Desayuno, Almuerzo, Cena): ")
            nueva = registrarComida(nombre)
            comidas.append(nueva)
            print("Comida registrada correctamente.")
        elif opcion == "2":
            mostrarComidas(comidas)
        elif opcion == "3":
            if len(comidas) == 0:
                print("No hay comidas registradas.")
            else:
                totales = calcularTotales(comidas)
                print(f"\nTotales del día: Proteínas={totales[0]}g, Carbohidratos={totales[1]}g, Grasas={totales[2]}g")
        elif opcion == "4":
            prom = promedioMacros(comidas)
            print(f"\nPromedio por comida: Proteínas={prom[0]:.2f}g, Carbohidratos={prom[1]:.2f}g, Grasas={prom[2]:.2f}g")
        elif opcion == "5":
            totales = calcularTotales(comidas)
            evaluarDieta(totales, objetivos)
        elif opcion == "6":
            pruebas()
        elif opcion == "7":
            print("Saliendo del seguimiento alimenticio...")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
