nom = input("Introduce Nombre y Apellidos:")
palabras = nom.split()
for palabra in palabras:
    print(palabra[0].upper(),palabra[1:-1],palabra[-1].upper())