numero = input("Dime un número:")
digito = input("Dime un dígito:")
lista = list(numero)
lista.append(numero)
i = 0
while lista[i] != digito:
    i = i+1
print("Está en la posición:",i)