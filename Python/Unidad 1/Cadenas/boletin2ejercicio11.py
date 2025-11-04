num = input("Introduce un número:")
lista = list(num)
lista2 = len(lista)
i = -3
while i >= -lista2:
    lista.insert(i,".")
    i = i-4
print(lista)
salida = ""
a = 0
for valor in lista:
    salida = salida+valor
print(salida)