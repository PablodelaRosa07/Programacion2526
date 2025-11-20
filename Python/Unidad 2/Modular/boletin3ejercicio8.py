def opciones():
    listaNum = []
    veces = int(input("¿Cuántas veces quieres añadir un número?:"))
    for i in range(veces):
        num = int(input("Introduce número:"))
        listaNum.append(num)
    print ("a. Devuelve la media")
    print ("b. Devuelve cuántos son pares")
    print ("c. Devuelve cuántos son negativos")
    print ("d. Devuelve la suma de todos los números introducidos")
    opcion = input("¿Qué desea hacer?:").lower()

    return opcion,listaNum

def quehacer(opcion1,listaNum):
    if opcion1 == "a":
        suma = 0
        for i in range (0,len(listaNum)):
            suma = suma+listaNum[i]
        resultado = suma/len(listaNum)
        print(f"La media es:{resultado}")
    elif opcion1 == "b":
        listaPares = []
        for pares in listaNum:
            if pares % 2 == 0:
                listaPares.append(pares)
        print(f"Los números pares son:{listaPares}")
    elif opcion1 == "c":
        listaNeg = []
        for negativos in listaNum:
            if negativos < 0:
                listaNeg.append(negativos)
        print(f"Los negativos son:{listaNeg}")
    elif opcion1 == "d":
        suma = 0
        for i in range (0,len(listaNum)):
            suma = suma+listaNum[i]
        print(f"La suma es:{suma}")
    
    return opcion1,listaNum

opciones1 = opciones()
quehacer(opciones1[0],opciones1[1])