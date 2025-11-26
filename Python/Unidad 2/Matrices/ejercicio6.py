matriz = []

def lista(matriz):
    numListas = int(input("¿Cuántas listas quieres tener?:"))
    for i in range (0,numListas):
        lista = []
        num = int(input("¿Cuántos números quieres meter en la lista?:"))
        for i in range(num):
            numeroMeter = int(input("Introduce un número:"))
            lista.append(numeroMeter)
        matriz.append(lista)
    return matriz

def columna(matriz):
    columnas = int(input("¿Qué columna quieres sumar?(0,1,2):"))
    while columnas > 2:
        columnas = int(input("¿Qué columna quieres sumar?(0,1,2):"))
    suma = 0
    for elemento in matriz:
        suma = suma + elemento[columnas]
    return suma

listas = lista(matriz)
suma = columna(listas)
print(f"La suma de las columnas es: {suma}")
