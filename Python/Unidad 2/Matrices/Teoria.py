matriz = [[0,2,4],[1,3,5],[6,8,10]]
#print(matriz[1]) #Pinta fila 1 (1,3,5)
#print(matriz[1][1]) #Pinta fila 1 columna 1 (3)

def sumafila(matriz,numFila):
    suma = 0
    fila = matriz[numFila]
    for elemento in fila:
        suma = suma+elemento
    return suma


def sumaMatriz(listaSuma):
    suma = 0
    for i in range (0,len(listaSuma)):
        suma = suma+sumafila(matriz, i)
    return suma


resultado = sumafila(matriz, 0)
listaSuma = sumafila(matriz, 1)
sumaRes = sumaMatriz(matriz)
print(sumaRes)
