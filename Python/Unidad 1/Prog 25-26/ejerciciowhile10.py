import random
num1 = random.randint(1,10)
num2 = random.randint(1,10)
num3 = int(input("Intenta adivinar la suma:"))
while num3 != num1+num2:
    print("Has fallado")
    num3 = int(input("Intentalo otra vez:"))
print("Has acertado,",num1,"+",num2,"=",num3)