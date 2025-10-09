num = int(input("Introduce un número:"))
num2 = 1
while num2 <= num:
    if num2 == 1 or num2 == num:
        print("*"+"#"*(num-2)+"*")
    else:
        print("*"*num)
    num2 = num2+1