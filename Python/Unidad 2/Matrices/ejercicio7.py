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
        for a in range (0,len(matriz[i])):
            if i % 2 == 0:
                suma = suma+matriz[i][a]
    return suma

lista = listas()
lista2 = suma(lista)
print(f"La suma de las filas pares es: {lista2}")