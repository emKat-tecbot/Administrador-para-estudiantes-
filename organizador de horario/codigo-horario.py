# Organizador de Horarios Universitarios 
from __future__ import annotations
from datetime import datetime
from copy import deepcopy
from typing import Optional
import json

# ------------------------------ CONSTANTES ---------------------------------

DIAS = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]
SLOTS_POR_DIA = 8
MAX_CLASES_POR_DIA = 5
MAX_TAREAS_POR_DIA = 6  # para análisis/sugerencias
LIBRE = "LIBRE"
DESCANSO = "DESCANSO"
TIPOS_TAREA = {"TAREA", "ESTUDIO", "PROYECTO", "EXAMEN"}
ENERGIAS = {"BAJA", "MEDIA", "ALTA"}

# ------------------------------ UTILIDADES BÁSICAS --------------------------

"""
Descripción:
Normaliza un nombre de día a la convención interna (Lunes..Viernes).

Algoritmo:
1) Si la entrada está vacía -> "Lunes".
2) strip()+capitalize(); si empieza con "Mier" -> "Miércoles".
3) Si no pertenece a DIAS -> "Lunes"; si sí, devolver tal cual.
"""
def normaliza_dia(entrada: str) -> str:
    if not entrada:
        return "Lunes"
    e = entrada.strip().capitalize()
    if e.startswith("Mier"):
        return "Miércoles"
    if e not in DIAS:
        return "Lunes"
    return e

"""
Descripción:
Devuelve el índice [0..4] de un día dentro de DIAS.

Algoritmo:
1) Usar DIAS.index(dia) y regresar el entero.
"""
def indice_dia(dia: str) -> int:
    return DIAS.index(dia)

"""
Descripción:
Limita un entero al rango [lo, hi].

Algoritmo:
1) Si n<lo -> lo; si n>hi -> hi; en otro caso n.
"""
def clamp(n: int, lo: int, hi: int) -> int:
    if n < lo:
        return lo
    if n > hi:
        return hi
    return n

"""
Descripción:
Indica si una celda es LIBRE.

Algoritmo:
1) Comparar celda == LIBRE y regresar bool.
"""
def es_libre(celda: str) -> bool:
    return celda == LIBRE

"""
Descripción:
Indica si una celda es de TAREA.

Algoritmo:
1) Verificar isinstance(str) y prefijo "TAREA:".
"""
def es_tarea(celda: str) -> bool:
    return isinstance(celda, str) and celda.startswith("TAREA:")

"""
Descripción:
Indica si una celda es un DESCANSO.

Algoritmo:
1) Comparar celda == DESCANSO.
"""
def es_descanso(celda: str) -> bool:
    return celda == DESCANSO

# ------------------------------ MATERIAS -----------------------------------

"""
Descripción:
Construye y valida una lista de materias a partir de dicts de entrada.

Algoritmo:
1) Verificar entradas!=None; si no, error.
2) Para cada registro: normalizar nombre y horas>=0.
3) Acumular y regresar.
"""
def registrar_clases(entradas: Optional[list[dict]] = None) -> list[dict]:
    if entradas is None:
        raise ValueError("registrar_clases requiere 'entradas'.")
    out = []
    for i, m in enumerate(entradas, 1):
        nombre = (m.get("nombre") or f"Materia_{i}").strip()
        horas = int(m.get("horas_semanales", 0))
        if horas < 0:
            horas = 0
        out.append({"nombre": nombre, "horas_semanales": horas})
    return out

"""
Descripción:
Genera una vista (lista o texto) del catálogo de materias.

Algoritmo:
1) Encabezado según haya materias.
2) Para cada materia, formatear "nombre: horas/semana".
3) Unir con "\n" si as_text.
"""
def mostrar_clases(materias: list[dict], as_text: bool = False):
    lines = ["--- Horario de Clases ---"] if materias else ["No hay materias registradas."]
    for m in materias:
        lines.append(f"{m['nombre']}: {m['horas_semanales']} horas/semana")
    return "\n".join(lines) if as_text else lines

"""
Descripción:
Convierte materias [{nombre, horas}] a [(nombre, horas)].

Algoritmo:
1) Recorrer materias y armar tupla (nombre, int(horas)).
"""
def materias_a_tuplas(materias: list[dict]) -> list[tuple[str, int]]:
    return [(m["nombre"], int(m["horas_semanales"])) for m in materias]

"""
Descripción:
Suma las horas_semanales de todas las materias.

Algoritmo:
1) Acumular int(horas) y regresar total.
"""
def total_horas_materias(materias: list[dict]) -> int:
    total = 0
    for m in materias:
        total += int(m.get("horas_semanales", 0))
    return total

"""
Descripción:
Busca una materia por nombre y regresa índice o -1 (case-insensitive).

Algoritmo:
1) Recorrer enumerate(materias) y comparar lower(); si coincide, devolver índice.
"""
def buscar_materia(materias: list[dict], nombre: str) -> int:
    for idx, m in enumerate(materias):
        if m["nombre"].lower() == nombre.lower():
            return idx
    return -1

"""
Descripción:
Elimina una materia por nombre si existe.

Algoritmo:
1) Obtener índice con buscar_materia; si >=0, pop y True; si no, False.
"""
def eliminar_materia(materias: list[dict], nombre: str) -> bool:
    idx = buscar_materia(materias, nombre)
    if idx >= 0:
        materias.pop(idx)
        return True
    return False

"""
Descripción:
Actualiza horas_semanales de una materia existente.

Algoritmo:
1) Buscar índice; si existe, setear horas>=0 y True; si no, False.
"""
def actualizar_materia_horas(materias: list[dict], nombre: str, horas: int) -> bool:
    idx = buscar_materia(materias, nombre)
    if idx >= 0:
        materias[idx]["horas_semanales"] = max(0, int(horas))
        return True
    return False

"""
Descripción:
Ordena (burbuja) copia de materias por horas (desc por defecto).

Algoritmo:
1) Copiar lista y aplicar bubble sort comparando horas.
"""
def ordenar_materias_por_horas(materias: list[dict], descendente: bool = True) -> list[dict]:
    copia = materias[:]
    n = len(copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            a = int(copia[j]["horas_semanales"])
            b = int(copia[j + 1]["horas_semanales"])
            if (descendente and a < b) or ((not descendente) and a > b):
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
    return copia

# ------------------------------ ACOMODO POR DÍAS ---------------------------

"""
Descripción:
Distribuye horas de materias por día con descansos y límites.

Algoritmo:
1) Inicializar dict días y contadores.
2) Para cada (materia, horas): repartir cíclicamente sin exceder MAX_CLASES_POR_DIA.
3) Insertar DESCANSO tras rachas >=2 cuando haya hueco.
"""
def acomodo_automatico_dias(materias: list[dict]) -> dict:
    dias = {d: [] for d in DIAS}
    horas_dia = {d: 0 for d in dias}
    i = 0
    tuplas = materias_a_tuplas(materias)
    total_horas = sum(h for _, h in tuplas)

    for materia, horas in tuplas:
        while horas > 0:
            dia = list(dias.keys())[i % 5]
            if horas_dia[dia] < MAX_CLASES_POR_DIA:
                if (len(dias[dia]) >= 2 and
                    dias[dia][-1] != DESCANSO and
                    dias[dia][-2] != DESCANSO and
                    horas_dia[dia] <= 3 and
                    total_horas > 0):
                    dias[dia].append(DESCANSO)
                else:
                    dias[dia].append(materia)
                    horas_dia[dia] += 1
                    horas -= 1
                    total_horas -= 1
            else:
                i += 1
        i += 1
    return dias

"""
Descripción:
Coloca materias manualmente respetando horas y límites diarios.

Algoritmo:
1) Mapear horas por materia.
2) Para cada asignación (materia, día): normalizar día y colocar horas hasta agotar o límite.
"""
def acomodo_manual_dias(materias: list[dict], asignaciones: list[tuple[str, str]]) -> dict:
    dias = {d: [] for d in DIAS}
    horas_dia = {d: 0 for d in dias}
    horas_map = {m["nombre"]: int(m["horas_semanales"]) for m in materias}

    for materia, dia_in in asignaciones:
        dia = normaliza_dia(dia_in)
        horas = horas_map.get(materia, 0)
        while horas > 0 and horas_dia[dia] < MAX_CLASES_POR_DIA:
            dias[dia].append(materia)
            horas_dia[dia] += 1
            horas -= 1
    return dias

"""
Descripción:
Devuelve una representación textual del acomodo por día.

Algoritmo:
1) Construir líneas por cada día y su lista de items.
"""
def mostrar_acomodo(dias: dict, as_text: bool = False):
    lines = ["--- Horario por día ---"]
    for d in DIAS:
        lines.append(f"{d}: {dias.get(d, [])}")
    return "\n".join(lines) if as_text else lines

# ------------------------------ MATRIZ SEMANAL ------------------------------

"""
Descripción:
Crea una matriz 5xSLOTS_POR_DIA llena de LIBRE.

Algoritmo:
1) Para cada día crear una fila de longitud SLOTS_POR_DIA con LIBRE.
"""
def construir_matriz_vacia() -> list[list[str]]:
    return [[LIBRE for _ in range(SLOTS_POR_DIA)] for _ in range(len(DIAS))]

"""
Descripción:
Cuenta racha de clases al final de una fila.

Algoritmo:
1) Recorrer en reversa hasta encontrar LIBRE/DESCANSO/TAREA y contar.
"""
def consecutivos_clases_al_final(fila: list[str]) -> int:
    count = 0
    for celda in reversed(fila):
        if celda in (LIBRE, DESCANSO) or str(celda).startswith("TAREA:"):
            break
        count += 1
    return count

"""
Descripción:
Cuenta celdas de clase (excluye LIBRE/DESCANSO/TAREA).

Algoritmo:
1) Recorrer fila y sumar si no es LIBRE/DESCANSO ni empieza con "TAREA:".
"""
def contar_clases_en_dia(fila: list[str]) -> int:
    return sum(1 for c in fila if c not in (LIBRE, DESCANSO) and not str(c).startswith("TAREA:"))

"""
Descripción:
Formatea la matriz semanal en tabla legible (lista o texto).

Algoritmo:
1) Construir encabezado y por cada día truncar celdas y formatear.
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
Descripción:
Inserta un DESCANSO por fila si hay >=2 clases y existe LIBRE.

Algoritmo:
1) Para cada fila, si contar_clases_en_dia>=2 y hay LIBRE, poner un DESCANSO en el primer LIBRE.
"""
def repartir_descansos_matriz(matriz: list[list[str]]) -> None:
    for fila in matriz:
        if contar_clases_en_dia(fila) >= 2 and LIBRE in fila:
            fila[fila.index(LIBRE)] = DESCANSO

"""
Descripción:
Verifica que la matriz sea 5 x SLOTS_POR_DIA.

Algoritmo:
1) Validar número de filas y longitud de cada fila; True/False.
"""
def validar_matriz(matriz: list[list[str]]) -> bool:
    if len(matriz) != 5:
        return False
    for fila in matriz:
        if len(fila) != SLOTS_POR_DIA:
            return False
    return True

"""
Descripción:
Coloca clases en matriz rotando días e intercalando descansos.

Algoritmo:
1) Construir matriz vacía.
2) Para cada materia: mientras haya horas, si hay cupo y LIBRE, colocar; tras racha>=2, intercalar DESCANSO.
3) Repartir descansos globales y regresar matriz.
"""
def acomodo_automatico_matriz(materias: list[dict]) -> list[list[str]]:
    matriz = construir_matriz_vacia()
    dia_idx = 0
    for m in materias:
        nombre, horas = m["nombre"], int(m["horas_semanales"])
        while horas > 0:
            if contar_clases_en_dia(matriz[dia_idx]) < MAX_CLASES_POR_DIA:
                fila = matriz[dia_idx]
                if consecutivos_clases_al_final(fila) >= 2 and LIBRE in fila:
                    fila[fila.index(LIBRE)] = DESCANSO
                if LIBRE in fila:
                    fila[fila.index(LIBRE)] = nombre
                    horas -= 1
            dia_idx = (dia_idx + 1) % len(DIAS)
    repartir_descansos_matriz(matriz)
    return matriz

# ------------------------------ TAREAS -------------------------------------

__task_seq = 0

"""
Descripción:
Genera un id único de tarea con timestamp y secuencia.

Algoritmo:
1) Incrementar contador global y concatenar a timestamp.
"""
def _gen_tarea_id() -> str:
    global __task_seq
    __task_seq += 1
    return f"T{int(datetime.now().timestamp())}{__task_seq}"

"""
Descripción:
Crea un dict de tarea con metadatos normalizados.

Algoritmo:
1) Validar tipo/energía contra catálogos; normalizar listas y bloque>=1.
2) Devolver dict con id y campos.
"""
def registrar_tarea_calendario(
    titulo: str, materia: str, horas_estimadas: int, deadline: datetime,
    tipo: str = "TAREA", prioridad: int = 3, dificultad: int = 2,
    energia: str = "MEDIA", deps: Optional[list[str]] = None,
    recurrente: Optional[list[str]] = None, bloque_slots: int = 1
) -> dict:
    tipo = (tipo or "TAREA").upper()
    if tipo not in TIPOS_TAREA:
        tipo = "TAREA"
    energia = (energia or "MEDIA").upper()
    if energia not in ENERGIAS:
        energia = "MEDIA"
    deps = deps or []
    recurrente = [d for d in (recurrente or []) if d in DIAS]
    return {
        "id": _gen_tarea_id(),
        "titulo": titulo.strip(),
        "materia": materia.strip(),
        "horas_estimadas": int(horas_estimadas),
        "deadline": deadline,
        "tipo": tipo,
        "prioridad": int(prioridad),
        "dificultad": int(dificultad),
        "energia": energia,
        "deps": deps,
        "recurrente": recurrente,
        "bloque_slots": max(1, int(bloque_slots)),
    }

"""
Descripción:
Cuenta cuántas celdas son TAREA en una fila.

Algoritmo:
1) Recorrer y sumar si str y empieza con "TAREA:".
"""
def contar_tareas_en_dia(fila: list[str]) -> int:
    return sum(1 for c in fila if isinstance(c, str) and c.startswith("TAREA:"))

"""
Descripción:
Selecciona un índice LIBRE según energía (ALTA temprano, BAJA tarde, MEDIA medio).

Algoritmo:
1) Recolectar índices LIBRE y elegir min/max/medio según energía.
"""
def encontrar_slot_para_tarea(fila: list[str], energia: str) -> Optional[int]:
    indices_libres = [i for i, c in enumerate(fila) if c == LIBRE]
    if not indices_libres:
        return None
    energia = energia.upper() if energia else "MEDIA"
    if energia == "ALTA":
        return min(indices_libres)
    if energia == "BAJA":
        return max(indices_libres)
    return indices_libres[len(indices_libres) // 2]

"""
Descripción:
Calcula bloques requeridos dado horas y tamaño de bloque.

Algoritmo:
1) Ajustar bloque>=1.
2) Usar división entera redondeando hacia arriba.
"""
def bloques_necesarios(horas_estimadas: int, bloque_slots: int) -> int:
    if bloque_slots <= 0:
        bloque_slots = 1
    total_slots = horas_estimadas
    n_bloques = (total_slots + bloque_slots - 1) // bloque_slots
    return max(1, n_bloques)

"""
Descripción:
Ordena (burbuja) tareas por fecha de entrega ascendente.

Algoritmo:
1) Bubble sort comparando t["deadline"].
"""
def ordenar_tareas_por_deadline(tareas: list[dict]) -> list[dict]:
    copia = tareas[:]
    n = len(copia)
    for i in range(n):
        for j in range(0, n - i - 1):
            if copia[j]["deadline"] > copia[j + 1]["deadline"]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
    return copia

"""
Descripción:
Inserta bloques de tareas en matriz de clases respetando deadline y energía.

Algoritmo:
1) Copiar matriz.
2) Para cada tarea: calcular n_bloques, límite de día y buscar slots contiguos LIBRE.
3) Colocar etiqueta por bloque hasta completar.
"""
def generar_calendario_tareas(
    matriz_clases: list[list[str]], tareas: list[dict], politica: str = "mixta"
) -> list[list[str]]:
    combinado = deepcopy(matriz_clases)
    for t in tareas:
        horas = int(t["horas_estimadas"])
        bloque = int(t.get("bloque_slots", 1))
        n_bloques = bloques_necesarios(horas, bloque)
        energia = t.get("energia", "MEDIA").upper()
        limite_dia = min(4, t["deadline"].weekday())
        bloques_colocados = 0
        for _ in range(3):
            for d in range(limite_dia + 1):
                if bloques_colocados >= n_bloques:
                    break
                fila = combinado[d]
                pos = encontrar_slot_para_tarea(fila, energia)
                if pos is None or pos + bloque > SLOTS_POR_DIA:
                    continue
                if any(fila[pos + k] != LIBRE for k in range(bloque)):
                    continue
                etiqueta = f"TAREA: {t['titulo']} ({t['materia']})"
                for k in range(bloque):
                    fila[pos + k] = etiqueta
                bloques_colocados += 1
            if bloques_colocados >= n_bloques:
                break
    return combinado

# ------------------------------ REPORTES -----------------------------------

"""
Descripción:
Resume por día: #clases, #tareas, #libres.

Algoritmo:
1) Para cada fila: contar con utilidades y armar dict por día.
"""
def reporte_carga(matriz: list[list[str]]) -> dict:
    resumen = {}
    for d_idx, dia in enumerate(DIAS):
        fila = matriz[d_idx]
        clases = contar_clases_en_dia(fila)
        tareas = contar_tareas_en_dia(fila)
        libres = sum(1 for c in fila if c == LIBRE)
        resumen[dia] = {"clases": clases, "tareas": tareas, "libres": libres}
    return resumen

"""
Descripción:
Imprime/retorna tabla de carga semanal en texto.

Algoritmo:
1) Llamar reporte_carga y formatear líneas.
"""
def imprimir_reporte_carga(matriz: list[list[str]], as_text: bool = False):
    r = reporte_carga(matriz)
    lines = ["--- Carga semanal ---"]
    for dia in DIAS:
        data = r[dia]
        lines.append(f"{dia:10s}  clases: {data['clases']:2d} | tareas: {data['tareas']:2d} | libres: {data['libres']:2d}")
    return "\n".join(lines) if as_text else lines

"""
Descripción:
Porcentaje de ocupación (slots != LIBRE).

Algoritmo:
1) Contar celdas no LIBRE y dividir entre total.
"""
def porcentaje_ocupacion(matriz: list[list[str]]) -> float:
    total = len(matriz) * len(matriz[0]) if matriz else 0
    if total == 0:
        return 0.0
    ocupadas = 0
    for fila in matriz:
        for c in fila:
            if c != LIBRE:
                ocupadas += 1
    return (ocupadas / total) * 100.0

# ------------------------------ PERSISTENCIA / ARCHIVOS --------------------

"""
Descripción:
Persiste materias/matriz/tareas a JSON serializando deadlines.

Algoritmo:
1) Construir objeto y json.dump con indent (deadline -> "%Y-%m-%d %H:%M").
"""
def guardar_estado(path: str, materias: list[dict], matriz: list[list[str]], tareas: list[dict]) -> None:
    serial = {
        "materias": materias,
        "matriz": matriz,
        "tareas": [{**t, "deadline": t["deadline"].strftime("%Y-%m-%d %H:%M")} for t in tareas],
    }
    with open(path, "w", encoding="utf-8") as f:
        json.dump(serial, f, ensure_ascii=False, indent=2)

"""
Descripción:
Carga JSON y reconstituye tipos (datetime en deadline).

Algoritmo:
1) json.load; defaults; parsear cada deadline con strptime.
"""
def cargar_estado(path: str) -> tuple[list[dict], list[list[str]], list[dict]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    materias = data.get("materias", [])
    matriz = data.get("matriz", construir_matriz_vacia())
    tareas = data.get("tareas", [])
    for t in tareas:
        t["deadline"] = datetime.strptime(t["deadline"], "%Y-%m-%d %H:%M")
    return materias, matriz, tareas

"""
Descripción:
Exporta la matriz formateada a un .txt.

Algoritmo:
1) Abrir archivo y escribir cada línea de imprimir_matriz(..., as_text=True).
"""
def exportar_txt(path: str, matriz: list[list[str]]) -> None:
    with open(path, "w", encoding="utf-8") as f:
        texto = imprimir_matriz(matriz, as_text=True)
        for line in texto.split("\n"):
            f.write(line + "\n")


