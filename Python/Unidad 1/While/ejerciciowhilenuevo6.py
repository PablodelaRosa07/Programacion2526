num = int(input("Introduce un número:"))
num2 = 1
while num2 <= num:
    if num2 % 2 != 0:
        print("*"+"#"*(num-2)+"*")
    else:
        print("*"+"@*"*(num-3))
    num2 = num2+1