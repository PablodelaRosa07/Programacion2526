matriz = [[22, 20, 19, 21],[18, 25, 23, 22],[19, 21, 20, 24],[17, 23, 22, 19],[24, 23, 27, 26]]

def tempMedia(matriz):
    listaNumero = []
    for i in range (0,len(matriz)):
        fila = matriz[i]
        media = tempMediaHotelporFila(fila)
        listaNumero.append(media)

    return listaNumero

def tempMediaHotelporFila(listaNum):
    suma = 0
    for elemento in listaNum:
        suma = suma+elemento
    suma = suma/len(listaNum)

    return suma

def tempHab(matriz):
    suma = 0
    for i in range (0,len(matriz)):
        for a in range (0,len(matriz[i])):
            if a == i:
                suma = suma+matriz[i][a]
    suma = suma/len(matriz)
    return suma

def tempHabDet(matriz):
    columna = int(input("Introduce el número de columna:"))
    suma = 0
    for elemento in matriz:
        suma = suma+elemento[columna]
    suma = suma/len(matriz)

    return suma

def todasColumnas(matriz):
    listaNumero = []
    for i in range (0,len(matriz)):
        fila = matriz[i]
        media = resultadoHab1(fila)
        listaNumero.append(media)

    return listaNumero



resultadoPlanta = tempMedia(matriz)
resultadoHotel = tempMediaHotelporFila(resultadoPlanta)
resultadoHab1 = tempHab(matriz)
print(f"La media por habitación es: {resultadoPlanta}")
print(f"La media del hotel es: {resultadoHotel}")
print(f"La media de la habitación 1 es: {resultadoHab1}")
resultadoHabDet = tempHabDet(matriz)
print(f"La media de la hanitación dicha es: {resultadoHabDet}")
resultadoColumnas = todasColumnas(matriz)
print(f"La media de las columnas es: {resultadoColumnas}")