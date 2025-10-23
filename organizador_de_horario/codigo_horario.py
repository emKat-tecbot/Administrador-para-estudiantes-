# Organizador de Horarios Universitarios 
from __future__ import annotations
from datetime import datetime
from copy import deepcopy
from typing import Optional
import json

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
SLOTS_POR_DIA = 8
MAX_CLASES_POR_DIA = 5
MAX_TAREAS_POR_DIA = 6
LIBRE = "LIBRE"
DESCANSO = "DESCANSO"
TIPOS_TAREA = {"TAREA", "ESTUDIO", "PROYECTO", "EXAMEN"}
ENERGIAS = {"BAJA", "MEDIA", "ALTA"}

"""
Función: normaliza_dia
Descripción:
Convierte una entrada textual a uno de los días válidos del sistema (Lunes–Viernes),
aceptando variantes comunes (e.g., “mie”, “mié”, “mier”) y manejando espacios/casos.

Algoritmo:
1) Si la entrada es nula o vacía, devolver "Lunes".
2) Limpiar espacios y pasar a minúsculas para comparar prefijos (lun, mar, mie/mié/mier, jue, vie).
3) Si coincide con algún prefijo, devolver el nombre canónico del día.
4) Si no coincide, pero es exactamente uno de los elementos en DIAS, devolverlo.
5) En cualquier otro caso, devolver "Lunes".
"""
def normaliza_dia(entrada: str) -> str:
    if not entrada:
        return "Lunes"
    e = entrada.strip()
    if not e:
        return "Lunes"
    base = e.lower()
    if base.startswith("lun"):
        return "Lunes"
    if base.startswith("mar"):
        return "Martes"
    if base.startswith("mie") or base.startswith("mié") or base.startswith("mier"):
        return "Miércoles"
    if base.startswith("jue"):
        return "Jueves"
    if base.startswith("vie"):
        return "Viernes"
    if e in DIAS:
        return e
    return "Lunes"
"""
Función: registrar_clases
Descripción:
Construye y valida el catálogo de materias a partir de una lista de diccionarios
con campos 'nombre' y 'horas_semanales'. Asegura nombres únicos y horas no negativas.

Algoritmo:
1) Verificar que 'entradas' no sea None; si lo es, lanzar error.
2) Iterar sobre cada entrada, normalizar nombre y convertir horas a entero ≥ 0.
3) Resolver duplicados de nombre agregando sufijos incrementales.
4) Acumular y devolver la lista de materias {nombre, horas_semanales}.
"""
def registrar_clases(entradas: Optional[list[dict]] = None) -> list[dict]:
    if entradas is None:
        raise ValueError("registrar_clases requiere 'entradas'.")
    out = []
    usados = set()
    for i, m in enumerate(entradas, 1):
        nombre_raw = m.get("nombre")
        nombre = (nombre_raw if isinstance(nombre_raw, str) else f"Materia_{i}").strip()
        if not nombre:
            nombre = f"Materia_{i}"
        horas_raw = m.get("horas_semanales", 0)
        try:
            horas = int(horas_raw)
        except Exception:
            horas = 0
        if horas < 0:
            horas = 0
        if nombre.lower() in usados:
            k = 2
            base = nombre
            while f"{base}_{k}".lower() in usados:
                k += 1
            nombre = f"{base}_{k}"
        usados.add(nombre.lower())
        out.append({"nombre": nombre, "horas_semanales": horas})
    return out

"""
Función: mostrar_clases
Descripción:
Genera una representación de texto (o lista de líneas) con el resumen de materias
y sus horas semanales.

Algoritmo:
1) Preparar encabezado si hay materias; si no, indicar ausencia.
2) Recorrer materias y agregar “nombre: X horas/semana”.
3) Devolver texto unificado si as_text es True; de lo contrario, lista.
"""
def mostrar_clases(materias: list[dict], as_text: bool = False):
    lines = ["--- Horario de Clases ---"] if materias else ["No hay materias registradas."]
    for m in materias:
        nom = str(m.get("nombre", "")).strip()
        hrs = int(m.get("horas_semanales", 0))
        lines.append(f"{nom}: {hrs} horas/semana")
    return "\n".join(lines) if as_text else lines

"""
Función: materias_a_tuplas
Descripción:
Convierte una lista de materias en una lista de tuplas (nombre, horas).

Algoritmo:
1) Iterar materias; tomar nombre y convertir horas a entero.
2) Agregar (nombre, horas) al resultado y devolverlo.
"""
def materias_a_tuplas(materias: list[dict]) -> list[tuple[str, int]]:
    r = []
    for m in materias:
        nom = str(m.get("nombre", "")).strip()
        try:
            hrs = int(m.get("horas_semanales", 0))
        except Exception:
            hrs = 0
        r.append((nom, hrs))
    return r

"""
Función: total_horas_materias
Descripción:
Suma las horas semanales de todas las materias registradas.

Algoritmo:
1) Inicializar acumulador en 0.
2) Para cada materia, sumar int(horas_semanales) manejando errores.
3) Devolver el total.
"""
def total_horas_materias(materias: list[dict]) -> int:
    total = 0
    for m in materias:
        try:
            total += int(m.get("horas_semanales", 0))
        except Exception:
            total += 0
    return total


"""
Función: construir_matriz_vacia
Descripción:
Genera la matriz semanal (5 x SLOTS_POR_DIA) inicializada con LIBRE.

Algoritmo:
1) Crear 5 filas.
2) En cada fila, colocar SLOTS_POR_DIA celdas con LIBRE.
3) Devolver la matriz.
"""
def construir_matriz_vacia() -> list[list[str]]:
    return [[LIBRE for _ in range(SLOTS_POR_DIA)] for _ in range(len(DIAS))]

"""
Función: consecutivos_clases_al_final
Descripción:
Cuenta cuántas clases consecutivas hay al final de una fila, deteniéndose
ante LIBRE, DESCANSO o una celda de TAREA.

Algoritmo:
1) Recorrer la fila en reversa.
2) Incrementar contador mientras no se encuentre LIBRE/DESCANSO/TAREA.
3) Devolver el contador.
"""
def consecutivos_clases_al_final(fila: list[str]) -> int:
    count = 0
    for celda in reversed(fila):
        if celda in (LIBRE, DESCANSO) or str(celda).startswith("TAREA:"):
            break
        count += 1
    return count

"""
Función: contar_clases_en_dia
Descripción:
Cuenta cuántas celdas de una fila son clases (excluye LIBRE, DESCANSO y TAREAS).

Algoritmo:
1) Recorrer la fila y sumar cuando la celda no sea LIBRE/DESCANSO ni comience con "TAREA:".
2) Devolver el total.
"""
def contar_clases_en_dia(fila: list[str]) -> int:
    c = 0
    for x in fila:
        if x not in (LIBRE, DESCANSO) and not str(x).startswith("TAREA:"):
            c += 1
    return c

"""
Función: imprimir_matriz
Descripción:
Formatea la matriz semanal en una tabla legible (texto o lista de líneas),
truncando contenidos de celdas para mantener ancho consistente.

Algoritmo:
1) Construir encabezado de slots.
2) Para cada día, generar la fila con celdas truncadas a 10 caracteres.
3) Devolver texto unido si as_text es True; si no, lista.
"""
def imprimir_matriz(matriz: list[list[str]], titulo: str = "Matriz semanal", as_text: bool = False):
    header = "Slot | " + " | ".join([f"{i:02d}" for i in range(SLOTS_POR_DIA)])
    lines = [f"--- {titulo} ---", header, "-" * len(header)]
    for d_idx, dia in enumerate(DIAS):
        fila = matriz[d_idx]
        contenido = " | ".join(f"{str(c)[:10]:10}" for c in fila)
        lines.append(f"{dia[:3]}  | {contenido}")
    return "\n".join(lines) if as_text else lines

"""
Función: repartir_descansos_matriz
Descripción:
Inserta un descanso en la primera celda libre de cada fila que tenga
al menos dos clases programadas.

Algoritmo:
1) Recorrer filas; calcular número de clases.
2) Si hay ≥ 2 y existe LIBRE, colocar DESCANSO en el primer LIBRE.
"""
def repartir_descansos_matriz(matriz: list[list[str]]) -> None:
    for fila in matriz:
        if contar_clases_en_dia(fila) >= 2 and LIBRE in fila:
            fila[fila.index(LIBRE)] = DESCANSO

"""
Función: validar_matriz
Descripción:
Verifica que la matriz tenga 5 filas y SLOTS_POR_DIA columnas por fila.

Algoritmo:
1) Validar tipo y tamaño de la lista principal.
2) Validar tipo y largo de cada fila.
3) Devolver True/False.
"""
def validar_matriz(matriz: list[list[str]]) -> bool:
    if not isinstance(matriz, list) or len(matriz) != 5:
        return False
    for fila in matriz:
        if not isinstance(fila, list) or len(fila) != SLOTS_POR_DIA:
            return False
    return True

"""
Función: acomodo_automatico_matriz
Descripción:
Distribuye las horas de materias en la matriz semanal, rotando entre días,
insertando descansos cuando hay rachas largas y respetando un máximo diario.

Algoritmo:
1) Construir matriz vacía y calcular horas totales a colocar.
2) Iterar materias y, por cada hora, ubicar en el día actual si hay espacio.
3) Tras dos clases seguidas, insertar DESCANSO cuando sea posible.
4) Avanzar al siguiente día circularmente.
5) Al final, repartir descansos globales y devolver la matriz.
"""
def acomodo_automatico_matriz(materias: list[dict]) -> list[list[str]]:
    matriz = construir_matriz_vacia()
    dia_idx = 0
    total_colocar = total_horas_materias(materias)
    if total_colocar <= 0:
        return matriz
    safety = total_colocar * 20 + 200
    for m in materias:
        nombre = str(m.get("nombre", "")).strip()
        try:
            horas = int(m.get("horas_semanales", 0))
        except Exception:
            horas = 0
        while horas > 0 and safety > 0:
            fila = matriz[dia_idx]
            if contar_clases_en_dia(fila) < MAX_CLASES_POR_DIA:
                if consecutivos_clases_al_final(fila) >= 2 and LIBRE in fila and contar_clases_en_dia(fila) <= MAX_CLASES_POR_DIA - 2:
                    fila[fila.index(LIBRE)] = DESCANSO
                if LIBRE in fila and contar_clases_en_dia(fila) < MAX_CLASES_POR_DIA:
                    fila[fila.index(LIBRE)] = nombre
                    horas -= 1
            dia_idx = (dia_idx + 1) % len(DIAS)
            safety -= 1
    repartir_descansos_matriz(matriz)
    return matriz

__task_seq = 0

"""
Función: _gen_tarea_id
Descripción:
Genera un identificador único para tareas combinando timestamp y un contador
secuencial interno.

Algoritmo:
1) Incrementar el contador global.
2) Concatenar con el timestamp actual en segundos.
3) Devolver la cadena resultante.
"""
def _gen_tarea_id() -> str:
    global __task_seq
    __task_seq += 1
    return f"T{int(datetime.now().timestamp())}{__task_seq}"

"""
Función: registrar_tarea_calendario
Descripción:
Crea un diccionario de tarea con campos normalizados (tipo, energía, horas,
prioridad, dificultad, bloque, dependencias y recurrencia) y un id único.

Algoritmo:
1) Validar/normalizar tipo y energía contra catálogos.
2) Convertir horas/prioridad/dificultad/bloque a enteros válidos (mínimos).
3) Normalizar días de recurrencia con normaliza_dia.
4) Generar id con _gen_tarea_id y devolver la estructura de tarea.
"""
def registrar_tarea_calendario(
    titulo: str, materia: str, horas_estimadas: int, deadline: datetime,
    tipo: str = "TAREA", prioridad: int = 3, dificultad: int = 2,
    energia: str = "MEDIA", deps: Optional[list[str]] = None,
    recurrente: Optional[list[str]] = None, bloque_slots: int = 1
) -> dict:
    t = (tipo or "TAREA").upper()
    if t not in TIPOS_TAREA:
        t = "TAREA"
    e = (energia or "MEDIA").upper()
    if e not in ENERGIAS:
        e = "MEDIA"
    dlist = deps if isinstance(deps, list) else []
    rlist = []
    if isinstance(recurrente, list):
        for d in recurrente:
            nd = normaliza_dia(str(d))
            if nd in DIAS:
                rlist.append(nd)
    try:
        h = int(horas_estimadas)
    except Exception:
        h = 1
    if h < 1:
        h = 1
    try:
        pr = int(prioridad)
    except Exception:
        pr = 3
    try:
        dif = int(dificultad)
    except Exception:
        dif = 2
    try:
        bs = int(bloque_slots)
    except Exception:
        bs = 1
    if bs < 1:
        bs = 1
    return {
        "id": _gen_tarea_id(),
        "titulo": (titulo or "").strip(),
        "materia": (materia or "").strip(),
        "horas_estimadas": h,
        "deadline": deadline,
        "tipo": t,
        "prioridad": pr,
        "dificultad": dif,
        "energia": e,
        "deps": dlist,
        "recurrente": rlist,
        "bloque_slots": bs,
    }

"""
Función: contar_tareas_en_dia
Descripción:
Cuenta cuántas celdas de una fila representan tareas.

Algoritmo:
1) Recorrer la fila y sumar las celdas que comiencen con "TAREA:".
2) Devolver el total.
"""
def contar_tareas_en_dia(fila: list[str]) -> int:
    s = 0
    for c in fila:
        if isinstance(c, str) and c.startswith("TAREA:"):
            s += 1
    return s

"""
Función: encontrar_slot_para_tarea
Descripción:
Selecciona un índice libre en la fila según la energía preferida:
ALTA (inicio), MEDIA (medio) o BAJA (final).

Algoritmo:
1) Recolectar todos los índices con LIBRE.
2) Si no hay libres, devolver None.
3) Elegir min, central o max según energía.
"""
def encontrar_slot_para_tarea(fila: list[str], energia: str) -> Optional[int]:
    indices_libres = []
    for i, c in enumerate(fila):
        if c == LIBRE:
            indices_libres.append(i)
    if not indices_libres:
        return None
    e = energia.upper() if isinstance(energia, str) else "MEDIA"
    if e == "ALTA":
        return indices_libres[0]
    if e == "BAJA":
        return indices_libres[-1]
    return indices_libres[len(indices_libres) // 2]

"""
Función: bloques_necesarios
Descripción:
Calcula el número de bloques que se requieren para cubrir las horas estimadas,
dado el tamaño del bloque en slots.

Algoritmo:
1) Asegurar bloque_slots ≥ 1.
2) Usar división entera redondeando hacia arriba: (horas + bloque - 1) // bloque.
3) Devolver al menos 1.
"""
def bloques_necesarios(horas_estimadas: int, bloque_slots: int) -> int:
    if bloque_slots <= 0:
        bloque_slots = 1
    total_slots = int(horas_estimadas) if horas_estimadas else 1
    n_bloques = (total_slots + bloque_slots - 1) // bloque_slots
    if n_bloques < 1:
        n_bloques = 1
    return n_bloques

"""
Función: ordenar_tareas_por_deadline
Descripción:
Ordena y devuelve una copia de la lista de tareas por fecha de entrega ascendente,
usando el algoritmo de burbuja.

Algoritmo:
1) Copiar la lista original.
2) Aplicar bubble sort comparando el campo 'deadline'.
3) Retornar la copia ordenada.
"""
def ordenar_tareas_por_deadline(tareas: list[dict]) -> list[dict]:
    copia = tareas[:]
    n = len(copia)
    for i in range(n):
        cambio = False
        for j in range(0, n - i - 1):
            if copia[j]["deadline"] > copia[j + 1]["deadline"]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
                cambio = True
        if not cambio:
            break
    return copia

"""
Función: generar_calendario_tareas
Descripción:
Inserta bloques de tareas dentro de una matriz de clases siguiendo prioridad
por fecha (deadline) y la estrategia de energía, respetando límites por día
y continuidad de bloques.

Algoritmo:
1) Clonar la matriz de clases y validarla; si no válida, usar una vacía.
2) Ordenar tareas por deadline ascendente.
3) Por cada tarea, calcular número de bloques a colocar y tamaño de bloque.
4) Para cada bloque, antes del deadline (ajustado a días hábiles), elegir fila
   y buscar posición libre acorde a energía; verificar contigüidad y capacidad.
5) Colocar etiquetas “TAREA: título (materia)” en los slots del bloque.
6) Devolver la matriz combinada.
"""
def generar_calendario_tareas(
    matriz_clases: list[list[str]], tareas: list[dict], politica: str = "mixta"
) -> list[list[str]]:
    combinado = deepcopy(matriz_clases)
    if not validar_matriz(combinado):
        combinado = construir_matriz_vacia()
    orden = ordenar_tareas_por_deadline(tareas) if isinstance(tareas, list) else []
    for t in orden:
        try:
            horas = int(t.get("horas_estimadas", 1))
        except Exception:
            horas = 1
        if horas < 1:
            horas = 1
        bloque = int(t.get("bloque_slots", 1)) if isinstance(t.get("bloque_slots", 1), int) else 1
        if bloque < 1:
            bloque = 1
        n_bloques = bloques_necesarios(horas, bloque)
        energia = (t.get("energia", "MEDIA") or "MEDIA").upper()
        limite_dia = t.get("deadline", datetime.now()).weekday()
        if limite_dia > 4:
            limite_dia = 4
        bloques_colocados = 0
        intentos = 0
        while bloques_colocados < n_bloques and intentos < (n_bloques * 20 + 50):
            for d in range(limite_dia + 1):
                fila = combinado[d]
                if contar_tareas_en_dia(fila) >= MAX_TAREAS_POR_DIA:
                    continue
                pos = encontrar_slot_para_tarea(fila, energia)
                if pos is None:
                    continue
                if pos + bloque > SLOTS_POR_DIA:
                    continue
                k = 0
                libre_contiguo = True
                while k < bloque:
                    if fila[pos + k] != LIBRE:
                        libre_contiguo = False
                        break
                    k += 1
                if not libre_contiguo:
                    continue
                etiqueta = f"TAREA: {t.get('titulo','')} ({t.get('materia','')})"
                k2 = 0
                while k2 < bloque:
                    fila[pos + k2] = etiqueta
                    k2 += 1
                bloques_colocados += 1
                if bloques_colocados >= n_bloques:
                    break
            intentos += 1
    return combinado

"""
Función: reporte_carga
Descripción:
Calcula, por cada día, el número de clases, tareas y espacios libres en la matriz.

Algoritmo:
1) Recorrer las 5 filas (Lunes–Viernes).
2) Contar clases, tareas y LIBRE en cada fila.
3) Construir dict por día con estos totales y devolverlo.
"""
def reporte_carga(matriz: list[list[str]]) -> dict:
    resumen = {}
    for d_idx, dia in enumerate(DIAS):
        fila = matriz[d_idx]
        clases = contar_clases_en_dia(fila)
        tareas = contar_tareas_en_dia(fila)
        libres = 0
        for c in fila:
            if c == LIBRE:
                libres += 1
        resumen[dia] = {"clases": clases, "tareas": tareas, "libres": libres}
    return resumen

"""
Función: imprimir_reporte_carga
Descripción:
Construye una tabla de texto (o lista de líneas) con el resumen de carga
por día, mostrando clases, tareas y libres.

Algoritmo:
1) Obtener el dict de reporte_carga.
2) Formatear líneas por cada día.
3) Si as_text es True, unir con saltos de línea.
"""
def imprimir_reporte_carga(matriz: list[list[str]], as_text: bool = False):
    r = reporte_carga(matriz)
    lines = ["--- Carga semanal ---"]
    for dia in DIAS:
        data = r[dia]
        lines.append(f"{dia:10s}  clases: {data['clases']:2d} | tareas: {data['tareas']:2d} | libres: {data['libres']:2d}")
    return "\n".join(lines) if as_text else lines

"""
Función: porcentaje_ocupacion
Descripción:
Calcula el porcentaje de ocupación de la matriz (slots no LIBRE).

Algoritmo:
1) Si la matriz está vacía, devolver 0.0.
2) Contar el total de celdas y cuántas no son LIBRE.
3) Devolver (ocupadas / total) * 100.0.
"""
def porcentaje_ocupacion(matriz: list[list[str]]) -> float:
    if not matriz or not matriz[0]:
        return 0.0
    total = len(matriz) * len(matriz[0])
    ocupadas = 0
    for fila in matriz:
        for c in fila:
            if c != LIBRE:
                ocupadas += 1
    return (ocupadas / total) * 100.0

"""
Función: guardar_estado
Descripción:
Persiste en un archivo JSON las materias, la matriz y la lista de tareas,
serializando el campo 'deadline' como cadena con formato "%Y-%m-%d %H:%M".

Algoritmo:
1) Construir estructura serializable; para cada tarea convertir 'deadline' a str.
2) Abrir el archivo en modo escritura con UTF-8.
3) Volcar JSON con indentación para legibilidad.
"""
def guardar_estado(path: str, materias: list[dict], matriz: list[list[str]], tareas: list[dict]) -> None:
    serial_tareas = []
    for t in tareas:
        d = {}
        for k, v in t.items():
            d[k] = v
        if isinstance(d.get("deadline"), datetime):
            d["deadline"] = d["deadline"].strftime("%Y-%m-%d %H:%M")
        serial_tareas.append(d)
    serial = {
        "materias": materias,
        "matriz": matriz,
        "tareas": serial_tareas,
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(serial, f, ensure_ascii=False, indent=2)

"""
Función: cargar_estado
Descripción:
Carga el estado desde un archivo JSON, reconstruyendo la matriz, el catálogo
de materias y las tareas, convirtiendo 'deadline' de texto a datetime.

Algoritmo:
1) Abrir el archivo y cargar el JSON.
2) Extraer 'materias', 'matriz' y 'tareas' (con valores por defecto).
3) Parsear cada 'deadline' con strptime; si falla, usar datetime.now().
4) Validar la matriz; si no es válida, reemplazar por una vacía.
5) Devolver (materias, matriz, tareas).
"""
def cargar_estado(path: str) -> tuple[list[dict], list[list[str]], list[dict]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    materias = data.get("materias", [])
    matriz = data.get("matriz", construir_matriz_vacia())
    tareas = data.get("tareas", [])
    for t in tareas:
        val = t.get("deadline")
        if isinstance(val, str) and val:
            try:
                t["deadline"] = datetime.strptime(val, "%Y-%m-%d %H:%M")
            except Exception:
                t["deadline"] = datetime.now()
        elif not isinstance(val, datetime):
            t["deadline"] = datetime.now()
    if not validar_matriz(matriz):
        matriz = construir_matriz_vacia()
    return materias, matriz, tareas

"""
Función: exportar_txt
Descripción:
Exporta a un archivo .txt una versión de texto de la matriz semanal generada
por imprimir_matriz.

Algoritmo:
1) Abrir el archivo en modo escritura con UTF-8.
2) Obtener la representación textual con imprimir_matriz(..., as_text=True).
3) Escribir línea por línea en el archivo y cerrar.
"""
def exportar_txt(path: str, matriz: list[list[str]]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        texto = imprimir_matriz(matriz, as_text=True)
        if isinstance(texto, str):
            for line in texto.split("\n"):
                f.write(line + "\n")
        else:
            for line in texto:
                f.write(str(line) + "\n")
"""
Funcion Menu
"""
def menu() -> str:
    print("===== ORGANIZADOR DE HORARIOS =====")
    print("1) Registrar materias ")
    print("2) Generar matriz de clases automática")
    print("3) Registrar tareas ")
    print("4) Generar calendario combinado")
    print("5) Reporte y guardar estado")
    print("6) Cargar estado desde archivo")
    print("7) Exportar matriz a TXT")
    print("0) Salir")
    return input("Selecciona una opción: ").strip()
