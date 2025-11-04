nom = input("Introduce Nombre y Apellidos:")
palabras = nom.split()
for palabra in palabras:
    print(palabra[0].upper())