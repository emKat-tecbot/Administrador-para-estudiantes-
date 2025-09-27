# ------------------------------------------------------------
# Organizador de Comidas – Avance
# Cumple: variables, funciones, if/elif/else, for, while, listas y pruebas.
# Incluye objetivos diarios de macros y descripción de cada función.
# ------------------------------------------------------------

# Algoritmo:
# 1. Mostrar nombre de comida.
# 2. Pedir qué equivale una porción.
# 3. Pedir alimento y macros de proteínas.
# 4. Pedir alimento y macros de carbohidratos.
# 5. Pedir alimento y macros de grasas.
# 6. Guardar la información y regresarla.
def registrar_comida(nombre_comida):
    print(f"\n--- {nombre_comida} ---")
    porcion = input("¿Qué equivale una porción? (ej. 100g, 1 taza): ")

    desc_prot = input("¿Qué alimento aporta proteínas y en qué cantidad? ")
    prote = float(input("Proteínas por porción (g): "))

    desc_carb = input("¿Qué alimento aporta carbohidratos y en qué cantidad? ")
    carb = float(input("Carbohidratos por porción (g): "))

    desc_gras = input("¿Qué alimento aporta grasas y en qué cantidad? ")
    gras = float(input("Grasas por porción (g): "))

    return {
        "nombre": nombre_comida,
        "porcion": porcion,
        "desc_prot": desc_prot, "proteinas": prote,
        "desc_carb": desc_carb, "carbohidratos": carb,
        "desc_gras": desc_gras, "grasas": gras
    }


# Algoritmo:
# 1. Iniciar acumuladores de macros en cero.
# 2. Recorrer la lista de comidas con un ciclo for.
# 3. Mostrar información de la porción y los alimentos.
# 4. Preguntar cuántas porciones se consumieron.
# 5. Multiplicar macros por número de porciones.
# 6. Sumar los resultados a los acumuladores.
# 7. Regresar totales de proteínas, carbohidratos y grasas.
def calcular_totales(comidas):
    total_p = total_c = total_g = 0
    for comida in comidas:
        print(f"\nPara {comida['nombre']} (1 porción = {comida['porcion']})")
        print("Proteínas de:", comida['desc_prot'])
        print("Carbohidratos de:", comida['desc_carb'])
        print("Grasas de:", comida['desc_gras'])
        porciones = int(input("¿Cuántas porciones consumiste?: "))
        total_p += comida["proteinas"] * porciones
        total_c += comida["carbohidratos"] * porciones
        total_g += comida["grasas"] * porciones
    return total_p, total_c, total_g


# Algoritmo:
# 1. Mostrar objetivos diarios de macros.
# 2. Comparar consumo con objetivos usando if/elif/else.
# 3. Indicar si está por debajo, por encima o justo en el objetivo.
# 4. Determinar macro dominante (proteínas, carbohidratos, grasas).
# 5. Si no hay un dominante claro, devolver "Balance aproximado".
def evaluar_dieta(p, c, g, obj_p, obj_c, obj_g):
    print("\n--- Comparación con objetivos ---")
    print("Objetivo de proteínas:", obj_p, "g")
    print("Objetivo de carbohidratos:", obj_c, "g")
    print("Objetivo de grasas:", obj_g, "g")

    if p < obj_p:
        print("Proteínas: por debajo del objetivo.")
    elif p > obj_p:
        print("Proteínas: por encima del objetivo.")
    else:
        print("Proteínas: justo en el objetivo.")

    if c < obj_c:
        print("Carbohidratos: por debajo del objetivo.")
    elif c > obj_c:
        print("Carbohidratos: por encima del objetivo.")
    else:
        print("Carbohidratos: justo en el objetivo.")

    if g < obj_g:
        print("Grasas: por debajo del objetivo.")
    elif g > obj_g:
        print("Grasas: por encima del objetivo.")
    else:
        print("Grasas: justo en el objetivo.")

    if p == c == g == 0:
        return "No hay datos."
    if p > c and p > g:
        return "Alta en proteínas."
    elif c > p and c > g:
        return "Alta en carbohidratos."
    elif g > p and g > c:
        return "Alta en grasas."
    else:
        return "Balance aproximado."


# Algoritmo:
# 1. Crear una comida de ejemplo con macros definidos.
# 2. Probar caso límite sin datos (totales en 0).
# 3. Probar caso con proteínas dominantes.
# 4. Mostrar los resultados obtenidos.
def pruebas():
    demo = {
        "nombre": "Pollo",
        "porcion": "100 g",
        "desc_prot": "100 g de pollo", "proteinas": 20,
        "desc_carb": "N/A", "carbohidratos": 0,
        "desc_gras": "5 g de aceite", "grasas": 5
    }
    print("Prueba 1 (sin datos):", evaluar_dieta(0, 0, 0, 50, 200, 60))
    print("Prueba 2 (proteínas altas):", evaluar_dieta(60, 10, 5, 50, 200, 60))


# Algoritmo:
# 1. Iniciar ciclo while para mostrar menú.
# 2. Opción 1 → pedir objetivos diarios, registrar comidas, calcular totales y evaluar.
# 3. Opción 2 → ejecutar pruebas.
# 4. Opción 0 → salir del programa.
# 5. Si se elige otra cosa, mostrar "opción inválida".
def main():
    opcion = ""
    while opcion != "0":
        print("\n--- Menú ---")
        print("1) Registrar comidas y calcular macros")
        print("2) Ejecutar pruebas")
        print("0) Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\n--- Objetivos diarios ---")
            obj_p = float(input("Proteínas necesarias (g): "))
            obj_c = float(input("Carbohidratos necesarios (g): "))
            obj_g = float(input("Grasas necesarias (g): "))

            comidas = []
            etiquetas = ["Comida principal 1", "Comida principal 2", "Snack / Batido"]
            for nombre in etiquetas:
                comidas.append(registrar_comida(nombre))

            p, c, g = calcular_totales(comidas)

            print("\n--- Resumen del día ---")
            print("Proteínas consumidas:", p, "g")
            print("Carbohidratos consumidos:", c, "g")
            print("Grasas consumidas:", g, "g")

            resultado = evaluar_dieta(p, c, g, obj_p, obj_c, obj_g)
            print("Evaluación general:", resultado)

        elif opcion == "2":
            pruebas()
        elif opcion == "0":
            print("Programa terminado.")
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()