num = float(input("Introduce un número:"))
while num:
    num2 = float(input("Introduce otro número:"))
    num = num+num2
    if num2 == 0:
        print("El resultado de la suma de los números anteriores es:",num)