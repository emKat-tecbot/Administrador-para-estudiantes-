def calPorClase(): # calificacion promedio por clase
    print("Entra a funci[on 1]")
    n = ""
    calProm = 0
    pesoProm = 0
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
    return final
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
def qNNPP (entrada): # que nota necesitare para pasar 
    final = entrada
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
# calculo de plan de estudio
    print("Hagamos un plan de estudio ")
    dias = int(input("Cuantos dias faltan para el examen? "))
    for dia in range (1, dias + 1):
        horas = gap / dias
        if horas < 1: # si tienes menos de una hora para estudiar
            min = horas * 60 
            print("Dia %d: %d minutos" %(dia,min))
        if horas >= 1 and type(horas) == float: # si el tiempo esta en horas y minutos
            # separar horas y minutos
            h = gap // dias 
            min = (horas - h) * 60
            print("Dia %d: %d horas y %d minutos" %(dia,h, min))
        if horas >= 1 and type(horas) == int: # si el tiempo esta en solo horas
            print("Dia %d: %d horas" %(dia,horas))
        if horas == 0: # si no necesitas estudiar
            print("Exito! no necesitas estudiar para el examen")
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

def menu():
    print("==BIENVENIDO AL ADMINISTRADOR DE NOTAS==")
    print("1. Calificacion pormedio por clase")
    print("2. Que nota necesito para pasar?")
    print("3. Progreso de mis notas")
    print("4. Tiempo de estudio para el examen final")
    print("5. Salir ")

def main():
    menu()
    opcion = 0
    while opcion != 5:
        opcion = int(input("Selecciona una opcion (1-5): "))
        if opcion == 1:
            final = calPorClase()
            print("Tu calificacion final es: ", final)
            break
        elif opcion == 2:
            minimo = qNNPP(final)
            print("La calificacion minima que necesitas es: ", minimo)
        elif opcion == 3:
            porgresoDeNota()
        elif opcion == 4:
            tiempoDeEstudio(final,minimo)
        elif opcion == 5:
            print("Gracias, adios :D")
            break
        else:
            print("Opcion no valida, intenta de nuevo")
            menu()

# main()    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      