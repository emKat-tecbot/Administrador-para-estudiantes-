#modo estudiante
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
        if n == "n":
            final = calProm/pesoProm # formula de calificacion final 
            break
    print("su nota promedio es: ", final)
    return [final,,nombreDeClass,peso]
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

def tiempoDeEstudio(entrada, entrada2): #nos cuenta que tanto debes estudiar para pasar el examen final
    nota = entrada # la calificacion final promedio
    calParaFinal = entrada2 # calificacion necesaria para pasar la final
    gap = calParaFinal - nota # diferencia entre la nota necesaria y la que tienees
    if gap < 5 : 
        print("Ok, sabes mucho del tema no te preocupes")
    elif gap < 10:
        print("Deberias ponerle un buen tiempo a estudiar para el examen final")
    elif gap < 15: 
        print("Ok alerta roja, la hora de estudiar es ahora")


#  grade spreadsheet (class, grade, goal grade, priority) 
def baseDeDatosdeNotas(clase, nota, meta, prioridad):
    baseDeDatos = [["Clase","Nota","Promedio", "Meta", "Prioridad"]]
    for i in range (1,4):
         if prioridad in [1,2,3]:
            prioridad = "Baja"
         elif prioridad in [4,5,6,7]:
             prioridad = "Media"
         elif prioridad in [8,9,10]:
             prioridad = "Alta"
         for j in range (len(clase)):
            baseDeDatos[i].append(clase[j],nota[j],meta[j],prioridad[j])
    return baseDeDatos
baseDeDatosdeNotas(["Matematica","Quimica","Sociales"],[85,90,78],[90,95,100],[9,7,5])
#GPA converter

# study planner calendar (day (goes untill the day of the exam), hours available, topics to study, priority of topic (based on dificulty of topic))
'''
CASOS DE PRUEBA:

Caso 1:
Entrada:
    Nota promedio: 84.1\
    Calificacion necesaria para pasar la final:99.8
Salida: "", "15 h  y 42 min"

Caso 2:
    Nota promedio: 62.6
    Calificacion necesaria para pasar la final: 79.3
Salida: "", "16h y 42min"

'''
#modo profesor

#funcion 1. crear matriz de nota estudiantil

#funcion 2 matriz por rubrica

#fubcion 3 estadistica en general (max, min)

#funcion 4 progreso de nota por estudiante (si esta mejorandom, en que competencias)
def menu ():
  print(f'''
  1. Caificaion por clase
  2. ¿Qué nota necesito para pasar?
  3. ¿Qué tanto he progresado con esta nota?
  4. Plan de estudio
  ''')
  calcOpt = int(imput("Que quisieras hacer? "))
  return calcOpt
  