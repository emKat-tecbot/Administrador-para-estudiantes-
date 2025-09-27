
# -----------------------------
# Generador de planes de estudio
# -----------------------------
materia = ""
tipo_curso = ""
dificultad = 3               # 1..5
dias_restantes = 0           # entero 
carga_diaria_min = 0         # minutos por día

# Pesos por sección (suman ≈ 1.0)
peso_teoria = 0.35
peso_practica = 0.45
peso_simulacro = 0.20

# Minutos planificados por sección
min_plan_teoria = 0
min_plan_practica = 0
min_plan_simulacro = 0

# Minutos realizados simulados (se actualizan con el "plan" impreso)
min_hechos_teoria = 0
min_hechos_practica = 0
min_hechos_simulacro = 0

# Indicadores de resultado
indicador_cumplimiento_pct = 0.0
indicador_horas_efectivas = 0.0
indicador_estado = "no_listo"


# -----------------------------
# Funciones de apoyo
# -----------------------------
def seleccionar_plantilla_simple(tipo):
    """
    Ajusta pesos por tipo de curso.
    Tipos conocidos: Calculo/Programacion. Si no, usa valores por defecto.
    """
    global peso_teoria, peso_practica, peso_simulacro
    t = tipo.strip().lower()

    if t == "calculo" or t == "cálculo":
        peso_teoria = 0.35
        peso_practica = 0.50
        peso_simulacro = 0.15
    elif t == "programacion" or t == "programación":
        peso_teoria = 0.25
        peso_practica = 0.55
        peso_simulacro = 0.20
    else:
        peso_teoria = 0.35
        peso_practica = 0.45
        peso_simulacro = 0.20

    # Normalización suave
    s = peso_teoria + peso_practica + peso_simulacro
    if s != 0.0:
        peso_teoria = peso_teoria / s
        peso_practica = peso_practica / s
        peso_simulacro = peso_simulacro / s


def crear_plan_basico():
    """
    Pide datos al usuario (wizard) y valida que sean razonables.
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
            if d_val >= 1 and d_val <= 5:
                dificultad = d_val
                dif_ok = True
        if not dif_ok:
            print("-> Valor inválido. Intenta de nuevo.")

    # días restantes (entero > 0)
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

    # carga diaria (minutos por día, entero > 0)
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
    Calcula los minutos plan por sección, ajustando práctica por dificultad.
    """
    global min_plan_teoria, min_plan_practica, min_plan_simulacro

    min_totales = dias_restantes * carga_diaria_min

    # Ajuste por dificultad: práctica sube/baja 15% por nivel desde 3.
    dt = dificultad - 3            # -2..+2
    ajuste = 0.15 * dt             # -0.30..+0.30
    p_pr = peso_practica * (1 + ajuste)
    if p_pr < 0.10:
        p_pr = 0.10
    if p_pr > 0.70:
        p_pr = 0.70

    rem = 1.0 - p_pr
    base_ts = peso_teoria + peso_simulacro
    if base_ts <= 0.0:
        p_te = 0.50
        p_si = 0.50
    else:
        p_te = (peso_teoria / base_ts) * rem
        p_si = (peso_simulacro / base_ts) * rem

    min_plan_teoria = int(min_totales * p_te)
    min_plan_practica = int(min_totales * p_pr)
    min_plan_simulacro = int(min_totales * p_si)


def imprimir_plan_diario_basico():
    """
    Genera un plan orientativo por día sin fechas reales.
    Usa bloques de 30 minutos y reparte de forma proporcional.
    No guarda estructuras: solo imprime y actualiza acumulados.
    """
    global min_hechos_teoria, min_hechos_practica, min_hechos_simulacro

    BLOQUE = 30
    dia = 1
    while dia <= dias_restantes:
        print("\nDía", dia)
        asignado = 0

        # Capacidad diaria en minutos
        cap_dia = carga_diaria_min

        # Metas restantes
        falt_te = min_plan_teoria - min_hechos_teoria
        falt_pr = min_plan_practica - min_hechos_practica
        falt_si = min_plan_simulacro - min_hechos_simulacro

        # Mientras haya capacidad y algo por hacer, asignar bloques
        intentos = 0
        while intentos < 12:  # límite defensivo de bloques/día
            if asignado + BLOQUE > cap_dia:
                break

            # Recalcular faltantes
            falt_te = min_plan_teoria - min_hechos_teoria
            falt_pr = min_plan_practica - min_hechos_practica
            falt_si = min_plan_simulacro - min_hechos_simulacro

            if falt_te <= 0 and falt_pr <= 0 and falt_si <= 0:
                break

            # Prioridad simple: práctica > teoría > simulacro si hay mucho por hacer
            elegir = "ninguna"
            if falt_pr > 0:
                elegir = "practica"
            elif falt_te > 0:
                elegir = "teoria"
            elif falt_si > 0:
                elegir = "simulacro"

            if elegir == "practica":
                min_hechos_practica += BLOQUE
                if min_hechos_practica > min_plan_practica:
                    min_hechos_practica = min_plan_practica
                asignado += BLOQUE
                print("  30 min -> Sección PRÁCTICA (", min_hechos_practica, "/", min_plan_practica, ")")

            elif elegir == "teoria":
                min_hechos_teoria += BLOQUE
                if min_hechos_teoria > min_plan_teoria:
                    min_hechos_teoria = min_plan_teoria
                asignado += BLOQUE
                print("  30 min -> Sección TEORÍA (", min_hechos_teoria, "/", min_plan_teoria, ")")

            elif elegir == "simulacro":
                min_hechos_simulacro += BLOQUE
                if min_hechos_simulacro > min_plan_simulacro:
                    min_hechos_simulacro = min_plan_simulacro
                asignado += BLOQUE
                print("  30 min -> Sección SIMULACRO (", min_hechos_simulacro, "/", min_plan_simulacro, ")")

            else:
                break

            intentos = intentos + 1

        dia = dia + 1


def calcular_indicadores_basico():
    """
    Calcula indicadores de cumplimiento y horas, y define estado (listo/no_listo).
    """
    global indicador_cumplimiento_pct, indicador_horas_efectivas, indicador_estado

    min_plan_total = (min_plan_teoria + min_plan_practica + min_plan_simulacro)
    min_hechos_total = (min_hechos_teoria + min_hechos_practica + min_hechos_simulacro)

    if min_plan_total == 0:
        indicador_cumplimiento_pct = 0.0
    else:
        indicador_cumplimiento_pct = (min_hechos_total * 100.0) / float(min_plan_total)

    indicador_horas_efectivas = min_hechos_total / 60.0

    if indicador_cumplimiento_pct >= 80.0:
        indicador_estado = "listo"
    else:
        indicador_estado = "no_listo"

    print("\n=== INDICADORES ===")
    print("Materia:", materia)
    print("Tipo:", tipo_curso)
    print("Días considerados:", dias_restantes, "| Carga diaria (min):", carga_diaria_min)
    print("Min plan (T/P/S):", min_plan_teoria, "/", min_plan_practica, "/", min_plan_simulacro)
    print("Min hechos (T/P/S):", min_hechos_teoria, "/", min_hechos_practica, "/", min_hechos_simulacro)
    print("Cumplimiento %:", round(indicador_cumplimiento_pct, 2))
    print("Horas efectivas:", round(indicador_horas_efectivas, 2))
    print("Estado:", indicador_estado)


def reset_basico():
    """
    Reinicia variables clave para poder correr otro escenario sin cerrar el programa.
    """
    global min_hechos_teoria, min_hechos_practica, min_hechos_simulacro
    global min_plan_teoria, min_plan_practica, min_plan_simulacro
    global indicador_cumplimiento_pct, indicador_horas_efectivas, indicador_estado

    min_hechos_teoria = 0
    min_hechos_practica = 0
    min_hechos_simulacro = 0

    min_plan_teoria = 0
    min_plan_practica = 0
    min_plan_simulacro = 0

    indicador_cumplimiento_pct = 0.0
    indicador_horas_efectivas = 0.0
    indicador_estado = "no_listo"


# -----------------------------
# main
# -----------------------------
def main():
    print("=== Asistente de Plan de Estudio (Básico) ===")
    continuar = "s"

    while continuar.lower() == "s":
        reset_basico()
        crear_plan_basico()
        generar_secciones_basico()

        print("\n--- Resumen del plan (minutos por sección) ---")
        print("Teoría:", min_plan_teoria, " | Práctica:", min_plan_practica, " | Simulacro:", min_plan_simulacro)

        print("\n--- Plan diario sugerido (sin fechas reales) ---")
        imprimir_plan_diario_basico()

        calcular_indicadores_basico()

        continuar = input("\n¿Quieres generar otro plan? (s/n): ").strip()
        if continuar == "":
            continuar = "n"

    print("\nGracias. Fin del asistente.")

# main()
