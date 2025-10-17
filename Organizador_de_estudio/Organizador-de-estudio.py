# -----------------------------
# Generador de planes de estudio
# -----------------------------
#Define el archivo 
NOMBRE_ARCHIVO = "plan_estudio.txt"

# 0=teoría, 1=práctica, 2=simulacro
ETIQUETAS = ["TEORÍA", "PRÁCTICA", "SIMULACRO"]

def crear_plan(materia, tipo_curso, dificultad, dias_restantes, carga_diaria_min):
    # Pesos base por tipo
    t = (tipo_curso or "").strip().lower()
    if t == "calculo" or t == "cálculo":
        pesos = [0.35, 0.50, 0.15]
    elif t == "programacion" or t == "programación":
        pesos = [0.25, 0.55, 0.20]
    else:
        pesos = [0.35, 0.45, 0.20]

# -----------------------------
# Funciones de apoyo (listas)
# -----------------------------

    # Normalizar pesos
    s = pesos[0] + pesos[1] + pesos[2]
    if s != 0:
        pesos[0] = pesos[0] / s
        pesos[1] = pesos[1] / s
        pesos[2] = pesos[2] / s

    # Ajuste por dificultad (±15% desde 3) SOLO práctica
    dt = int(dificultad) - 3
    p_pr = pesos[1] * (1 + 0.15 * dt)
    if p_pr < 0.10:
        p_pr = 0.10
    if p_pr > 0.70:
        p_pr = 0.70

    rem = 1.0 - p_pr
    base_ts = pesos[0] + pesos[2]
    if base_ts <= 0:
        p_te = 0.5
        p_si = 0.5
    else:
        p_te = (pesos[0] / base_ts) * rem
        p_si = (pesos[2] / base_ts) * rem

    min_totales = int(dias_restantes) * int(carga_diaria_min)
    min_plan = [int(min_totales * p_te), int(min_totales * p_pr), int(min_totales * p_si)]

    plan = {
        "materia": materia,
        "tipo_curso": tipo_curso,
        "dificultad": int(dificultad),
        "dias_restantes": int(dias_restantes),
        "carga_diaria_min": int(carga_diaria_min),
        "pesos": pesos,
        "min_plan": min_plan
    }
    return plan

def generar_horario(plan):
    # Devuelve: {"lineas": [...], "min_hechos": [T,P,S], "matriz": [[bloques_dia], ...]}
    BLOQUE = 30
    dias = plan["dias_restantes"]
    carga = plan["carga_diaria_min"]
    min_plan = [plan["min_plan"][0], plan["min_plan"][1], plan["min_plan"][2]]
    min_hechos = [0, 0, 0]
    lineas = []
    matriz = []

    dia = 1
    while dia <= dias:
        lineas.append("Día " + str(dia))
        asignado = 0
        intentos = 0
        bloques_dia = []

        while intentos < 12:
            if asignado + BLOQUE > carga:
                break

            falt_T = min_plan[0] - min_hechos[0]
            falt_P = min_plan[1] - min_hechos[1]
            falt_S = min_plan[2] - min_hechos[2]

            if falt_T <= 0 and falt_P <= 0 and falt_S <= 0:
                break

            if falt_P > 0:
                elegido = 1
            elif falt_T > 0:
                elegido = 0
            else:
                elegido = 2

            min_hechos[elegido] += BLOQUE
            if min_hechos[elegido] > min_plan[elegido]:
                min_hechos[elegido] = min_plan[elegido]

            asignado = asignado + BLOQUE
            linea = "  30 min -> " + ETIQUETAS[elegido] + " (" + str(min_hechos[elegido]) + " / " + str(min_plan[elegido]) + ")"
            lineas.append(linea)
            bloques_dia.append(ETIQUETAS[elegido])

            intentos = intentos + 1

        matriz.append(bloques_dia)
        dia = dia + 1

    return {"lineas": lineas, "min_hechos": min_hechos, "matriz": matriz}

def calcular_indicadores(plan, min_hechos):
    total_plan = plan["min_plan"][0] + plan["min_plan"][1] + plan["min_plan"][2]
    total_hecho = min_hechos[0] + min_hechos[1] + min_hechos[2]

    if total_plan == 0:
        pct = 0.0
    else:
        pct = (total_hecho * 100.0) / float(total_plan)

    horas = total_hecho / 60.0

    if pct >= 80.0:
        estado = "listo"
    else:
        estado = "no_listo"

    return {
        "cumplimiento_pct": round(pct, 2),
        "horas_efectivas": round(horas, 2),
        "estado": estado,
        "min_plan": [plan["min_plan"][0], plan["min_plan"][1], plan["min_plan"][2]],
        "min_hechos": [min_hechos[0], min_hechos[1], min_hechos[2]],
        "materia": plan["materia"],
        "tipo_curso": plan["tipo_curso"],
        "dias_restantes": plan["dias_restantes"],
        "carga_diaria_min": plan["carga_diaria_min"]
    }

def guardar_plan(plan):
    # Escribe SIEMPRE en "plan_estudio.txt" en la carpeta desde la que se ejecuta Python
    archivo = open(NOMBRE_ARCHIVO, "w", encoding="utf-8")
    archivo.write("materia:" + str(plan["materia"]) + "\n")
    archivo.write("tipo_curso:" + str(plan["tipo_curso"]) + "\n")
    archivo.write("dificultad:" + str(plan["dificultad"]) + "\n")
    archivo.write("dias_restantes:" + str(plan["dias_restantes"]) + "\n")
    archivo.write("carga_diaria_min:" + str(plan["carga_diaria_min"]) + "\n")
    archivo.write("pesos:" + str(plan["pesos"][0]) + "," + str(plan["pesos"][1]) + "," + str(plan["pesos"][2]) + "\n")
    archivo.write("min_plan:" + str(plan["min_plan"][0]) + "," + str(plan["min_plan"][1]) + "," + str(plan["min_plan"][2]) + "\n")
    archivo.close()

def cargar_plan():
    # Abre en modo a+ (crea si no existe), luego lee con readline() en while True (ThinkCS)
    plan = {}
    archivo = open(NOMBRE_ARCHIVO, "a+", encoding="utf-8")
    archivo.seek(0)  # ir al inicio para leer
    lineas_leidas = 0

    while True:
        linea = archivo.readline()
        if len(linea) == 0:
            break
        linea = linea.strip()
        if ":" not in linea:
            continue

        partes = linea.split(":", 1)
        clave = partes[0].strip()
        valor = partes[1].strip()
        lineas_leidas = lineas_leidas + 1

        if clave == "materia":
            plan["materia"] = valor
        elif clave == "tipo_curso":
            plan["tipo_curso"] = valor
        elif clave == "dificultad":
            plan["dificultad"] = int(valor)
        elif clave == "dias_restantes":
            plan["dias_restantes"] = int(valor)
        elif clave == "carga_diaria_min":
            plan["carga_diaria_min"] = int(valor)
        elif clave == "pesos":
            nums = valor.split(",")
            pesos = []
            i = 0
            while i < len(nums):
                if nums[i] != "":
                    pesos.append(float(nums[i]))
                i = i + 1
            plan["pesos"] = pesos
        elif clave == "min_plan":
            nums = valor.split(",")
            mins = []
            j = 0
            while j < len(nums):
                if nums[j] != "":
                    mins.append(int(nums[j]))
                j = j + 1
            plan["min_plan"] = mins

    archivo.close()

    # Si el archivo estaba vacío, regresar None para que el main cree uno nuevo
    if lineas_leidas == 0:
        return None

    # Completar faltantes
    if "materia" not in plan:
        plan["materia"] = "Sin nombre"
    if "tipo_curso" not in plan:
        plan["tipo_curso"] = "otro"
    if "dificultad" not in plan:
        plan["dificultad"] = 3
    if "dias_restantes" not in plan:
        plan["dias_restantes"] = 1
    if "carga_diaria_min" not in plan:
        plan["carga_diaria_min"] = 60
    if "pesos" not in plan:
        plan["pesos"] = [0.35, 0.45, 0.20]
    if "min_plan" not in plan:
        tmp = crear_plan(plan["materia"], plan["tipo_curso"], plan["dificultad"], plan["dias_restantes"], plan["carga_diaria_min"])
        plan["min_plan"] = tmp["min_plan"]

    return plan
