import random

carton_bingo = [
    [5,  21, 38,   50, 63],
    [12, 17, 44,   47, 74],
    [1,  29, "--", 55, 69],
    [9,  25, 32,   59, 61],
    [14, 19, 41,   52, 66]]

fila = int(input("¿Qué fila desea comprobar?:"))
bolas = []

def bolasSalen(carton_bingo):
    veces = 0
    llamarComprueba = False
    while llamarComprueba == False:
        numero = random.randint(1,75)
        llamarComprueba = compruebaSiHayLineaEnFila(carton_bingo,bolas)
        bolas.append(numero)
        veces = veces+1
    return llamarComprueba,bolas,veces
        

def  buscaNumeroEnLista(lista, numero):
    i = 0
    encontrado = False
    posicion = -1
    while i < len(carton_bingo) and not encontrado:
        if lista[i] == numero:
            encontrado = True
            posicion = i
        else:
            i += 1

    return posicion

def compruebaSiHayLineaEnFila(carton_bingo,bolas):
    comprobar = True
    for i in range (0,len(bolas)):
        if bolas[i] in carton_bingo:
            comprobar = True
        elif bolas[i] not in carton_bingo:
            comprobar = False
        
    return comprobar


def generaAleatorio(carton_bingo,bolas,fila):
    listaNoEstan = []
    for i in range (0,len(bolas)):
        if bolas[i] not in carton_bingo[fila]:
            listaNoEstan.append(bolas[i])
        
    return listaNoEstan

def imprimirSalida(veces,fila,bolas):
    print("Se ha conseguido línea en el cartón.")
    print(f"Números que han salido antes de completar la fila: {veces}")
    print(f"Fila acertante: {fila}")
    print(f"Lista de números que han salido: {bolas}")




comprueba = bolasSalen(carton_bingo)

noEstan = generaAleatorio(carton_bingo,fila,comprueba)
print(f"Los números que no están en la fila son: {noEstan}")

salida = imprimirSalida(bolas,fila,bolas)
print(salida)