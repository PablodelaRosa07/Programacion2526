vecesganadashumano = 0
vecesganadasmaquina = 0
partidasjugadas = 0
apuestapar = 0
apuestaimpar = 0
numhumano = int(input("Introduce un número del 1 al 5:"))
while numhumano <= 0 or numhumano >= 6:
    numhumano = int(input("Introduce un número del 1 al 5:"))
apuesta = input("¿Apuestas par (P) o impar (I)?:").upper
import random
nummaquina = random.randint(1,5)
resultado = numhumano+nummaquina
while numhumano != nummaquina:
    if resultado % 2 == 0:
        print("El resultado es",resultado,", por lo tanto es par")
        if (resultado//numhumano)%2 == 0:
            print("Ha ganado el humano")
            apuestapar = apuestapar+1
            vecesganadashumano = vecesganadashumano+1
        elif (resultado//numhumano)%2 != 0:
            print("Ha ganado la máquina")
            vecesganadasmaquina = vecesganadasmaquina+1
            apuestaimpar = apuestaimpar+1
    elif resultado % 2 != 0:
        print("El resultado es",resultado,", por lo tanto es impar")
        if (resultado//numhumano)%2 != 0:
            print("Ha ganado el humano")
            apuestapar = apuestapar+1
            vecesganadashumano = vecesganadashumano+1
        elif (resultado//numhumano)%2 == 0:
            print("Ha ganado la máquina")
            vecesganadasmaquina = vecesganadasmaquina+1
            apuestaimpar = apuestaimpar+1
    partidasjugadas = partidasjugadas+1
    numhumano = int(input("Introduce un número del 1 al 5:"))
    apuesta = input("¿Apuestas par (P) o impar (I)?:").upper
    nummaquina = random.randint(1,5)
print("Mismo número de piedras: Fin")
print("El humano ha ganado",vecesganadashumano,"veces")
print("La máquina ha ganado",vecesganadasmaquina,"veces")
print("Se han jugado",partidasjugadas,"partidas")
if apuestapar < apuestaimpar:
    print("La apuesta humana más frecuente es la impar")
elif apuestapar > apuestaimpar:
    print("La apuesta humana más frecuente es la par")
elif apuestapar == apuestaimpar:
    print("El humano ha apostado las mismas veces Par que Impar")

