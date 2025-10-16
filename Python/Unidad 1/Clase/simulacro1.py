num1 = int(input("Introduce un número:"))
num2 = int(input("Introduce un segundo número:"))
num3 = int(input("Introduce un tercer número:"))
while num1 != 0 and num2 != 0 and num3 != 0:
    if num1 > num2 > num3:
        print("Sigue un orden Decreciente")
    elif num1 < num2 < num3:
        print("Sigue un orden Creciente")
    elif num1 == num2 == num3:
        print("Son Iguales")
    else:
        print("Están Desordenados")
    num1 = int(input("Introduce un número:"))
    num2 = int(input("Introduce un segundo número:"))
    num3 = int(input("Introduce un tercer número:"))
print("Son 0")

