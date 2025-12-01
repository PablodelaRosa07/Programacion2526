import random
matriz = []

def datosLluvia(matriz):
    for i in range (0,20):
        lista = []
        for a in range (0,7):
            lluvias = random.randint(1,100)
            lista.append(lluvias)
        matriz.append(lista)

    return matriz

def calcularAguaMax():
    listaSuma = []
    numeroMax = 0
    posicionLista = 0

    for i in range(0,len(matriz)):
        suma = 0
        for elemento in matriz[i]:
            suma = elemento+suma
        suma = suma/len(matriz[i])
        listaSuma.append(suma)

    for i in range(0,len(listaSuma)-1):
        if listaSuma[i] > listaSuma[i+1]:
            numeroMax = listaSuma[i]
    
    for i in range(0,len(listaSuma)):
        if numeroMax == listaSuma[i]:
            posicionLista = i


        



resultado = datosLluvia(matriz)


