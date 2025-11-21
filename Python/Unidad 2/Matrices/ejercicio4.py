def lista():
    listaNormal = []
    veces = int(input("¿Cuántos números quieres meter?:"))
    for i in range (veces):
        num = int(input("Introduce un número:"))
        listaNormal.append(num)

    return listaNormal

def suma(listaNormal):
    suma = 0
    for i in range (0,len(listaNormal)):
        suma = suma+listaNormal[i]

    return suma

resultado = lista()
suma(resultado)
print(suma(resultado))