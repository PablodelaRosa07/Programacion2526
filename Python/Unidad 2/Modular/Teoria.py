#Definición función recibe un numero y devuelve un booleano (True o False)
def comprobarPar(numero):
    return numero %2==0

num = int(input("Dame un número:"))
esPar= comprobarPar(num)
esPar= comprobarPar(32)
print(32,esPar)