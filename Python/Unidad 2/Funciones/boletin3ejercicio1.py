def calcularLista():
    listaNum=[]
    cantidadNum = int(input("¿Cuántos números quieres añadir?:"))
    for i in range (cantidadNum):
        num = input("Introduce un número:")
        listaNum.append(num)
    return listaNum,cantidadNum

def listaReves(cantidad):
    listaReversa=[]
    for i in range(cantidad,0,-1):
        listaReversa.append(i)
    return listaReversa

lista=calcularLista()
calcularLista(lista[1])
inversa=listaReves(lista)

print(inversa)