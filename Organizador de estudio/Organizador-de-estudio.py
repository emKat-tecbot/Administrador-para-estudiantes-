# -----------------------------
# Generador de planes de estudio
# -----------------------------

# 0=teoría, 1=práctica, 2=simulacro
etiquetas = ["TEORÍA", "PRÁCTICA", "SIMULACRO"]

materia = ""
tipo_curso = ""
dificultad = 3               # 1..5
dias_restantes = 0           # entero
carga_diaria_min = 0         # minutos por día

# Pesos por sección en una lista [T, P, S] (suman ~1.0)
pesos = [0.35, 0.45, 0.20]

# Minutos planificados y realizados [T, P, S]
min_plan = [0, 0, 0]
min_hechos = [0, 0, 0]

# Indicadores
indicador_cumplimiento_pct = 0.0
indicador_horas_efectivas = 0.0
indicador_estado = "no_listo"


# -----------------------------
# Funciones de apoyo (listas)
# -----------------------------
def normalizar_pesos():
    s = pesos[0] + pesos[1] + pesos[2]
    if s != 0:
        pesos[0] /= s
        pesos[1] /= s
        pesos[2] /= s

def seleccionar_plantilla_simple(tipo):
    """
    Ajusta pesos por tipo de curso usando la lista [T,P,S].
    """
    t = tipo.strip().lower()
    if t == "calculo" or t == "cálculo":
        pesos[0], pesos[1], pesos[2] = 0.35, 0.50, 0.15
    elif t == "programacion" or t == "programación":
        pesos[0], pesos[1], pesos[2] = 0.25, 0.55, 0.20
    else:
        pesos[0], pesos[1], pesos[2] = 0.35, 0.45, 0.20
    normalizar_pesos()


def crear_plan_basico():
    """
    Pide datos al usuario (igual que antes).
    """
    global materia, tipo_curso, dificultad, dias_restantes, carga_diaria_min

    materia = input("Materia: ").strip()
    tipo_curso = input("Tipo de curso (Calculo/Programacion/otro): ").strip()

    # dificultad (1..5)
    dif_ok = False
    while not dif_ok:
        d_str = input("Dificultad (1-5): ").strip()
        if d_str.isdigit():
            d_val = int(d_str)
            if 1 <= d_val <= 5:
                dificultad = d_val
                dif_ok = True
        if not dif_ok:
            print("-> Valor inválido. Intenta de nuevo.")

    # días restantes
    dias_ok = False
    while not dias_ok:
        dr = input("Días restantes (entero, ej. 7): ").strip()
        if dr.isdigit():
            d_val = int(dr)
            if d_val > 0:
                dias_restantes = d_val
                dias_ok = True
        if not dias_ok:
            print("-> Valor inválido. Intenta de nuevo.")

    # carga diaria (min)
    carga_ok = False
    while not carga_ok:
        cd = input("Carga diaria (minutos, ej. 120): ").strip()
        if cd.isdigit():
            c_val = int(cd)
            if c_val > 0:
                carga_diaria_min = c_val
                carga_ok = True
        if not carga_ok:
            print("-> Valor inválido. Intenta de nuevo.")

    seleccionar_plantilla_simple(tipo_curso)


def generar_secciones_basico():
    """
    Calcula min_plan [T, P, S]. Ajuste por dificultad SOLO en práctica.
    """
    min_totales = dias_restantes * carga_diaria_min

    # práctica sube/baja 15% por nivel desde 3
    dt = dificultad - 3            # -2..+2
    p_pr = pesos[1] * (1 + 0.15 * dt)
    if p_pr < 0.10: p_pr = 0.10
    if p_pr > 0.70: p_pr = 0.70

    rem = 1.0 - p_pr
    base_ts = pesos[0] + pesos[2]
    if base_ts <= 0:
        p_te, p_si = 0.50, 0.50
    else:
        p_te = (pesos[0] / base_ts) * rem
        p_si = (pesos[2] / base_ts) * rem

    min_plan[0] = int(min_totales * p_te)
    min_plan[1] = int(min_totales * p_pr)
    min_plan[2] = int(min_totales * p_si)


def imprimir_plan_diario_basico():
    """
    Genera plan por día con bloques de 30 min.
    Prioridad simple: PRÁCTICA > TEORÍA > SIMULACRO.
    Actualiza min_hechos [T, P, S].
    """
    BLOQUE = 30
    min_hechos[0] = min_hechos[1] = min_hechos[2] = 0

    for dia in range(1, dias_restantes + 1):
        print("\nDía", dia)
        asignado = 0
        cap_dia = carga_diaria_min

        intentos = 0    # límite defensivo de bloques/día
        while intentos < 12:
            if asignado + BLOQUE > cap_dia:
                break

            falt_T = min_plan[0] - min_hechos[0]
            falt_P = min_plan[1] - min_hechos[1]
            falt_S = min_plan[2] - min_hechos[2]

            if falt_T <= 0 and falt_P <= 0 and falt_S <= 0:
                break

            # elegir sección (índice): 1>0>2 (P>T>S)
            elegido = -1
            if falt_P > 0:
                elegido = 1
            elif falt_T > 0:
                elegido = 0
            elif falt_S > 0:
                elegido = 2

            if elegido == -1:
                break

            # asignar bloque
            min_hechos[elegido] += BLOQUE
            if min_hechos[elegido] > min_plan[elegido]:
                min_hechos[elegido] = min_plan[elegido]
            asignado += BLOQUE

            print(f"  30 min -> {etiquetas[elegido]} ( {min_hechos[elegido]} / {min_plan[elegido]} )")

            intentos += 1


def calcular_indicadores_basico():
    """
    KPIs con sumas directas de listas.
    """
    global indicador_cumplimiento_pct, indicador_horas_efectivas, indicador_estado

    min_plan_total = sum(min_plan)
    min_hechos_total = sum(min_hechos)

    if min_plan_total == 0:
        indicador_cumplimiento_pct = 0.0
    else:
        indicador_cumplimiento_pct = (min_hechos_total * 100.0) / float(min_plan_total)

    indicador_horas_efectivas = min_hechos_total / 60.0
    indicador_estado = "listo" if indicador_cumplimiento_pct >= 80.0 else "no_listo"

    print("\n=== INDICADORES ===")
    print("Materia:", materia)
    print("Tipo:", tipo_curso)
    print("Días considerados:", dias_restantes, "| Carga diaria (min):", carga_diaria_min)
    print("Min plan (T/P/S):", min_plan[0], "/", min_plan[1], "/", min_plan[2])
    print("Min hechos (T/P/S):", min_hechos[0], "/", min_hechos[1], "/", min_hechos[2])
    print("Cumplimiento %:", round(indicador_cumplimiento_pct, 2))
    print("Horas efectivas:", round(indicador_horas_efectivas, 2))
    print("Estado:", indicador_estado)


def reset_basico():
    """
    Reset con listas (más corto).
    """
    global indicador_cumplimiento_pct, indicador_horas_efectivas, indicador_estado
    min_plan[0] = min_plan[1] = min_plan[2] = 0
    min_hechos[0] = min_hechos[1] = min_hechos[2] = 0
    indicador_cumplimiento_pct = 0.0
    indicador_horas_efectivas = 0.0
    indicador_estado = "no_listo"
