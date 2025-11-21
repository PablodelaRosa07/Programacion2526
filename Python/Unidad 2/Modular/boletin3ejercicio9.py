import random

def num():
    lista = []
    for i in range (1,100):
        num = random.randint(1,1000)
        lista.append(num)
    print ("a. Conocer el mayor")
    print ("b. Conocer el menor")
    print ("c. Obtener la suma de todos los números")
    print ("d. Obtener la media")
    print ("e. Sustituir el valor de un elemento por otro número introducido por teclado")
    print ("f. Mostrar todos los números")
    opcion = input("¿Qué desea hacer?:").lower()
    return opcion,lista

def opciones(opcion1,lista1):
    while opcion1 == "a" or opcion1 == "b" or opcion1 == "c" or opcion1 == "d" or opcion1 == "e" or opcion1 == "f":
        if opcion1 == "a":
            lista_maximo = lista1[0]
            for numero in lista1[1:]:
                if numero > lista_maximo:
                    lista_maximo = numero
            print(f"El número mayor es:{lista_maximo}")
        elif opcion1 == "b":
            lista_minimo = lista1[0]
            for numero in lista1[1:]:
                if numero < lista_minimo:
                    lista_minimo = numero
            print(f"El número menor es:{lista_minimo}")
        elif opcion1 == "c":
            suma = 0
            for i in range (0,len(lista1)):
                suma = suma+lista1[i]
            print(f"La suma es:{suma}")
        elif opcion1 == "d":
            for i in range (0,len(lista1)):
                suma = suma+lista1[i]
            resultado = suma/100
            print(f"La media es:{resultado}")
        elif opcion1 == "e":
            num = int(input("Introduce qué número quieres meter:"))
            posicion = int(input("Introduce en qué posicion quieres meterlo:"))
            lista1.pop(posicion)
            lista1.insert(posicion,num)
            
        elif opcion1 == "f":
            print(lista1)

        opcion1 = input("¿Qué desea hacer?:").lower()

opciones1 = num()
opciones(opciones1[0],opciones1[1])