num1 = float(input("Introduce un número:"))
num2 = float(input("Introduce otro número:"))
while (num1 != 0 or num2 != 0):
    num3 = num1+num2
    print("El resultado de la suma es:",num3)
    num1 = float(input("Introduce un número:"))
    num2 = float(input("Introduce otro número:"))
    if (num1 == 0 and num2 == 0):
        print("Fin")   
    