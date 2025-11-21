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

def suma(suma):
    suma = 0
    for i in range (0,len(matriz)):
        if matriz[i] % 2 == 0:
            for elemento in matriz[i]:
                suma = suma+elemento
    return suma

lista = listas()
suma(lista)
print(suma(lista))