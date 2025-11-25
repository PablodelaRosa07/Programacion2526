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

def numeroMax(matriz): 
    numero = 0
    num = int(input("Introduce la fila:"))
    for elemento in matriz[num]:
        if elemento > numero:
            numero = elemento
    
    return numero

def numeroMaxColumna(matriz):
    numero = 0
    listaColumnaMax = []
    num = int(input("Introduce la columna:"))
    for i in range (len(matriz)):
        listaColumnaMax.append(matriz[i][num])
    for elemento in listaColumnaMax:
        if elemento > numero:
            numero = elemento

    return numero

def totalMatriz(matriz):
    suma = 0
    listaTodo = []
    for i in range (0,len(matriz)):
        for elemento in matriz[i]:
            suma = suma+elemento

    return suma


resultado = listas()
numeroMaximo = numeroMax(resultado)
columnaMayor = numeroMaxColumna(resultado)
totalMatrizTodo = totalMatriz(resultado)
print(numeroMaximo)
print(columnaMayor)
print(totalMatrizTodo)