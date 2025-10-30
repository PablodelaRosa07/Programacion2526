numero = input("Dime un número:")
digito = int(input("Dime la posición del dígito:"))
for i in range (len(numero)):
    if i == digito:
        print("Es el número:",numero[i])
