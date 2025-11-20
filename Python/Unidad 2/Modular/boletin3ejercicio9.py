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
    for numero in lista1:
        if lista1[numero] > lista1[numero-1]:
            lista1.insert(-1,numero)

opciones1 = num()
opciones(opciones1[0],opciones1[1])