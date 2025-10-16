import random
def calendario ( temas, horasLibres, dificultad, hoy, fechaExamen):
    dias = fechaExamen - hoy
    temasRep = []
    calendario = [["Dia","Horas a estudiar","Temas a estudiar","Topico de enfoque"]]
    for i in range (len(temas)):
        temasRep.extend(temas * dificultad[i])
                        
    temasDeHoy = []
    for a in range (len(temasRep)):
        for b in range (min(3,len(temasRep))):
            tema = random.choice(temasRep) 
            temasDeHoy[b].append(tema)
        for i in range (1, dias + 1):
            for j in range (len(horasLibres)):
                calendario.append([j + 1,horasLibres[j],temasDeHoy[j]])
    print(calendario)
calendario(["Algebra","Trigonometria","Calculo"],[3,2,4],[3,2,5],1,7)
