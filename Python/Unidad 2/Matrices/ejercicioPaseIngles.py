import random
veces = 0

def todo(suma,lista,listaGanancias,numeroApuesta,resultadoApuesta,cantidadApuesta):
    print("A. Apostar")
    print("H. Historial de apuestas")
    print("R. Retirarse")
    opcion = input("¿Qué desea hacer?:").upper()
    while opcion != "A" and opcion != "H" and opcion != "R":
        print("Opción incorrecta")
        opcion = input("¿Qué desea hacer?:").upper()
    while opcion == "A" or opcion == "H":
        llamarSumaDados = sumaDados
        if opcion == "A":
            llamarApuesta = apuesta(suma)
        elif opcion == "H":
            llamarHistorial = historial(lista,numeroApuesta,suma,resultadoApuesta,cantidadApuesta)
        opcion = input("¿Qué desea hacer?:").upper()
    llamarRetirarse = retirarse(listaGanancias)
    

def sumaDados():
    num1 = random.randint(1,6)
    num2 = random.randint(1,6)
    suma = num1+num2

    return suma

def apuesta(suma):
    lista = []
    listaGanancias = []
    numeroApuesta = int(input("Introduce la suma de los números:"))
    cantidadApuesta = int(input("Introduce la cantidad que desea apostar:"))
    if suma == numeroApuesta:
        resultadoApuesta = "ganando"
        listaGanancias.append(cantidadApuesta*2)
        print(f"Has ganado {cantidadApuesta*2}")
        lista.append(cantidadApuesta*2)
    elif suma != numeroApuesta:
        resultadoApuesta = "perdiendo"
        listaGanancias.append(-cantidadApuesta)
        print(f"Has perdido {cantidadApuesta}")
        lista.append(cantidadApuesta)
        
    return lista,numeroApuesta,listaGanancias,veces

def historial(lista,numeroApuesta,suma,resultadoApuesta,cantidadApuesta):
    for i in range (0,len(lista)):
        print(f"En la jugada {i} apostó al valor {numeroApuesta} y sumó {suma}, {resultadoApuesta} {cantidadApuesta}€")

def retirarse(listaGanancias):
    suma = 0
    for elemento in listaGanancias:
        suma = suma+elemento
    print(f"Las ganancias han sido {suma}")
    
resultado = todo(apuesta,historial,retirarse,apuesta,historial,retirarse)