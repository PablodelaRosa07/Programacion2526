#def sirve para definir una función

#Definición función recibe un numero y devuelve un booleano (True o False)
def comprobarPar(numero):
    return numero %2==0

num = int(input("Dame un número:"))
esPar= comprobarPar(num)
esPar= comprobarPar(32)
print(32,esPar)


cadena = "fuera"
#Dentro del método veo lo que recibe como argumento o lo que defino dentro
profesion = "torero"
def saludar (nomb,ed,prof):
    print("Hola ",nomb, ed, prof)
    cadena1 = "dentro"
    return cadena1 #Hace que se convierta en el que está fuera

cadena2 = saludar ("A",20,profesion)
print(cadena2[0])
print(cadena2[0])