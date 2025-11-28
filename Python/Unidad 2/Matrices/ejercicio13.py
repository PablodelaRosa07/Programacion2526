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

def sumaPorFilasIgual():
    listaSuma = []
    for i in range (len(matriz)):
        suma = 0
        for elemento in matriz[i]:
            suma = suma+elemento
        listaSuma.append(suma)
    for i in range (0,len(listaSuma)-1):
        if listaSuma[i] == listaSuma[i+1]:
            comprobacion = True
        elif listaSuma[i] != listaSuma[i+1]:
            comprobacion = False

    return comprobacion,listaSuma
    




resultadoListas = listas()
resultadoSumas = sumaPorFilasIgual()
print(resultadoListas)
print(resultadoSumas)