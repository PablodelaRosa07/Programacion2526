print("Introduce palabras, escribe ""stop"" si no deseas guardar más palabras")
listaPalabras = []
palabra = input("Introduce una palabra:").lower()
listaPalabras = []
while palabra != "stop":
    listaPalabras.append(palabra)
    palabra = input("Introduce otra palabra:").lower()
letra = input("Introduce una letra:").lower()
print(f"La letra introducida es {letra} y hay {len(listaPalabras)} en la lista: {listaPalabras}")
print("Introduzca ""E"" si desea devolver la lista de palabras que comienzan por la letra")
print("Introduzca ""C"" si desea devolver la lista de palabras que contienen  la letra")
print("Introduzca ""S"" para terminar el programa")
opcion = input("¿Qué desea hacer?:").upper()
while opcion != "S":
    if opcion == "E":
        a = 0
        for palabra in listaPalabras:
            if palabra[0] == letra:
                print(listaPalabras[a])
            a = a+1
    if opcion == "C":
        for palabra in listaPalabras:
            for letras in palabra:
                if letras == letra:
                    print(palabra)
    opcion = input("¿Qué desea hacer?:").upper()
print("Saliendo del programa...")