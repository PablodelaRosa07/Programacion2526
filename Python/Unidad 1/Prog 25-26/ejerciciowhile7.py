import random
num1 = random.randint(1,10)
num2 = int(input("Intenta adivinar un número del 1 al 10:"))
while num1 != num2:
    print("No has adivinado el número")
    num2 = int(input("Intentalo otra vez:"))
if num1 == num2:
    print("Has acertado, era el",num2)