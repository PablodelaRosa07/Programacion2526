lista = []  #Crea una lista vacía
lista = [0]  #La posición 0 es la primera de la lista
lista = [-1]  #La posición -1 es la última de la lista
import random  #Importamos algo, en este caso "random"
algo = 0  #Crea una variable
otracosa = 1  #Crea otra variable
suma = algo+otracosa  #Crea una variable sumando, restando... otras variables
#Se puede hacer con listas
lista2 = []
lista3 = lista2+lista  #Así concatenas 2 listas para juntarlas en una
len(lista)  #Longitud de la lista
lista.append()  #Añade un elemento al final de la lista
lista.insert()  #Añade un elemento en la posición especificada, por ejemplo: lista.insert(0, 3), añade un 3 en la posición 0
lista.remove()  #Borra un elemento de la lista, por ejemplo: lista.remove(3), borra el 3 de la lista
lista.pop()  #Borra por defecto el útimo elemento de la lista a menos que indiques la posición
lista.reverse()  #Reversa el orden de la lista
lista.sort()  #Ordena los elementos de menor a mayor
print(lista.index(2))  #Devuelve en que posición está el primer 2

mensaje="Hola Mundo"
mensaje1=mensaje.find("Mundo") #Encontrar algo en una cadena