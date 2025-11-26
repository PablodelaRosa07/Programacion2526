#regular

matriz = []

def listas():
    numListas = int(input("¿Cuántas listas quieres tener?:"))
    for i in range (0,numListas):
        lista = []
        num = int(input("¿Cuántos números quieres meter en la lista?:"))
        for i in range(num):
            numeroMeter = int(input("Introduce un número:"))
            lista.append(numeroMeter)
        matriz.append(lista)
    return matriz

def numeroMaxFila(matriz,numFila): 
    listaFilaMax = getFila(matriz,numFila)
    numMaximo = getMaximo(listaFilaMax)
    return numMaximo

def numeroMaxColumna(matriz,numColumna):
    listaColumnaMax = getColumna(numColumna,matriz)
    numMaximo = getMaximo(listaColumnaMax)

    return numMaximo

def getMaximo(listaNumeros,num):
    numero = 0
    for elemento in listaNumeros[num]:
        if elemento > numero:
            numero = elemento

    return numero

def getFila(matriz):
    listaFilaMax = []
    for i in range (len(matriz)):
        listaFilaMax.append(matriz[i])

    return listaFilaMax

def getColumna(num,matriz):
    listaColumnaMax = []
    for i in range (len(matriz)):
        listaColumnaMax.append(matriz[i][num])

    return listaColumnaMax

def totalMatriz(matriz):
    suma = 0
    listaTodo = []
    for i in range (0,len(matriz)):
        for elemento in matriz[i]:
            suma = suma+elemento

    return suma


resultado = listas()
getFila(matriz)
numeroMaximo = numeroMaxFila(getFila(matriz),resultado)
columnaMayor = numeroMaxColumna(resultado)
totalMatrizTodo = totalMatriz(resultado)
print(f"El número máximo de esa fila es: {numeroMaximo}")
print(f"El número máximo de esa fila es: {columnaMayor}")
print(f"La suma de la matriz es: {totalMatrizTodo}")
