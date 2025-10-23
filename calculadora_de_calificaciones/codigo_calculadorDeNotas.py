import random
def calPorClase(): # calificacion promedio por clase
    n = ""
    calProm = 0
    pesoProm = 0
    nombreDeClass = input("Cuales es el nombre de la materia? ")
    while n != "no":
        nota = float(input("Ingresa una nota de tu clase de este periodo/semestre: "))
        peso = float(input("How much is it worth? "))
        calProm += nota * peso
        pesoProm += peso
        n = input("Quieres agregar otra calificacion de su materia (y si si, n si no)?")
        if n == "no":
            final = calProm/pesoProm # formula de calificacion final 
            break
    print("su nota promedio de la clase" + nombreDeClass + " es: ", final)
    return [final,nombreDeClass ,pesoProm]
'''  
CASOS DE PRUEBA:

Caso 1: 
Entrada: 
    Nota 1: 88   Peso: 20
    Nota 2: 85   Peso: 20
    Nota 3: 90   Peso: 30
    Nota 4: 75   Peso: 30
Salida:  84.1

Caso 2: 
Entrada:
    Nota 1: 65,15
    Nota 2: 75, 10
    Nota 3: 90, 15
    Nota 4: 53, 60
Salida = 62.6
'''
def qNNPP (final): # que nota necesitare para pasar 
    final = final
    objetivo = float(input("Que nota quieres lograr este periodo/semestre "))
    peso = float(input("Que porcentaje vale el examen final? "))
    minimo = (objetivo - final * (100 -peso))/ peso # formula para la nota minima para alcanzar meta
    if minimo < 0:
        print ("Disculpa pero es imposible alcanzar la nota que deseas :/")
    else:
        print("La calificaion que necesitas para alcanzar %d es %d" %(objetivo,minimo))
    return minimo
'''
Casos de prueba:

Caso 1:
Entrada:
    Nota: 84.1
    Target: 90
    Peso: 60
Salida: 99.8 

Caso 2:
Entrada:
    Nota: 62.6
    Target: 70
    Peso: 80
Salida: 79.3

'''
def porgresoDeNota (): #enseña si estas mejorandpo tus notas o no
    notas = []
    progreso = 0
    while True: #creacion de lista de notas de una materia
        miNota = input("Quisieras agregar una calificacion de una materia (y si si, n si no)? ")
        miNota = miNota.lower()
        if miNota == "y":
            notas.append(int(input("Ingresa su nota: ")))
        if miNota == "n":
            break
    for i in range (len(notas) - 1): #analisis de si estas mejorando tus notas o no
       if notas[i] < notas[i + 1]: 
           progreso +=1
       elif notas[i] > notas[i + 1]:
           progreso -= 1
    if progreso > 0:
        print("Estas mejorando tus calificaciones, sigue asi!")
    elif progreso < 0:
        print("Tus notas estan empeorando, a trabajar se ha dicho!")
    else:
        print("Tus notas son iguales")
'''
CASOS DE PRUEBA

Caso 1:
Entrada: 90, 80, 70, 60
Salida: Tus notas estan empeorando, a trabajar se ha dicho!

Caso 2:
Entrada: 60, 59, 75, 89, 90, 50
Salida: Estas mejorando tus calificaciones, sigue asi!
'''

def baseDeDatosdeNotas(clase, nota, meta, prioridad):
    baseDeDatos = [["Clase","Nota", "Meta", "Prioridad"]]
    for i in range (len(clase)): #clasificacion de prioridades
        if prioridad[i]in [1,2,3]:
         prioridad[i]= "Baja"
        elif prioridad[i] in [4,5,6,7]:
         prioridad[i] = "Media"
        elif prioridad[i] in [8,9,10]:
         prioridad[i] = "Alta"
        baseDeDatos.append([clase[i],nota[i],meta[i],prioridad[i]]) #cfreacion de primer renglon de base de datos
    
    for columnas in range(len(baseDeDatos)):
        for filas in range (len(baseDeDatos[columnas])):
           print(baseDeDatos[columnas][filas], end = "-------") # usando las notas del usuario va creando renglones por cada clase registrada
        print("\n")
    return baseDeDatosdeNotas

# study planner calendar (day (goes untill the day of the exam), hours available, topics to study, priority of topic (based on dificulty of topic))
def calendario ( temas, horasLibres, dificultad, hoy, fechaExamen):
    dias = fechaExamen - hoy #dias para el examen
    temasRep = [] # repeticion de temas (mientras mas dificil mas se repite y por ende mas aparecen enel calendario)
    calendario = [["Dia","Horas a estudiar","Temas a estudiar"]] # primer renglon de calendario
    for i in range (len(temas)):
        temasRep.extend(temas * dificultad[i])   
    for a in range (dias): # ceacion del calendario
        temasDeHoy = [] # temas del dia
        for b in range (min(3,len(temasRep))): # el estudiante debe estudiar un maximo de 3 temas al dia
            tema = random.choice(temasRep) 
            temasDeHoy.append(tema)
        calendario.append([a + 1,horasLibres]) # se le agrega el dia y las horas libres promedio que tiene
        for l in range (3):
            calendario[a+1].append(temasDeHoy[l]) # se le agregan los temas del dia
    for columnas in range (len(calendario)):
        for filas in range (len(calendario[columnas])):
           print(calendario[columnas][filas], end = "-------") # formateando el calendario
    return calendario

def Archivo (baseDeDatosdeNotas,calendario): # usa baseDeDatos y calendario para crear un archivo de expediente
    baseDeDatos = open("ArchivoDeTexto.txt","+w")
    baseDeDatos.write("Tabla 1. Base de Notas")
    baseDeDatos.write(baseDeDatosdeNotas)
    baseDeDatos.write("\n")
    baseDeDatos.write("Tabla 2. Calendario de estudio")
    baseDeDatos.write("\n")
    baseDeDatos.write(calendario)
    baseDeDatos.seek(0)
    baseDeDatos.read()

def menu ():
  print(f'''
  1. Caificaion por clase
  2. ¿Qué nota necesito para pasar?
  3. ¿Qué tanto he progresado con esta nota?
  4. Base de Notas
  5. Calendario
  6. Expediente
  7. Salir
  ''')
  calcOpt = int(input("Que quisieras hacer? "))
  return calcOpt
  