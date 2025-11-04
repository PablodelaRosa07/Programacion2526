cadena = []
car = input("Introduce un caracter:")
while len(car) >= 2 or len(car) <= 0:
    car = input("Introduce un caracter:")
car2 = input("Introduce otro caracter:")
while len(car2) >= 2 or len(car2) <= 0:
    car2 = input("Introduce otro caracter:")

cadena.append(car)
cadena.insert(0,car2)
print(cadena)