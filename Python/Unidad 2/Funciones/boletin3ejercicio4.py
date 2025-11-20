def estaOrdenadaAscendemente():
    listaNum=[]
    ordenada = True
    num = int(input("Introduce cuántos números quieres meter:"))
    orden = input("¿Ascendente (A) o Descendente (D)?:").upper()
    for i in range (num):
        meterNum = int(input("Introduce un número:"))
        listaNum.append(meterNum)
    i = 0
    if orden == "A":
        while i < len(listaNum)-1 and ordenada:
            if listaNum[i] > listaNum[i+1]:
                ordenada = False
            i = i+1
    if orden == "D":
        while i < len(listaNum)-1 and ordenada:
            if listaNum[i] < listaNum[i+1]:
                ordenada = False
            i = i+1
    print(ordenada)
    return listaNum

resultado=estaOrdenadaAscendemente()
