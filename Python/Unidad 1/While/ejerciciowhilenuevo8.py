num = int(input("Introduce un número:"))
ultimodigito = 0
while num != 0:
    resto = num % 10
    print(resto)
    num = num//10
    ultimodigito = ultimodigito + resto
print("La suma de todos los números es:",ultimodigito)