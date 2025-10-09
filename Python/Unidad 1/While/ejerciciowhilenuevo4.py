num = int(input("Introduce un número:"))
num2 = 1
while num2 <= num:
    if num2 == 1 or num2 == num:
        print("*"*num)
    else:
        cadena = "*"+" "*(num-2)+"*"
        print(cadena)
    num2 = num2+1
