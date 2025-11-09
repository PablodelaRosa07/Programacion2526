vecesganadashumano = 0
vecesganadasmaquina = 0
partidasjugadas = 0
apuestapar = 0
apuestanone = 0
numhumano = int(input("Introduce un número del 0 al 5:"))
while numhumano < 0 or numhumano >= 6:
    numhumano = int(input("Introduce un número del 0 al 5:"))
apuesta = input("¿Apuestas pares (P) o nones (N)?:").upper
import random
nummaquina = random.randint(0,5)
resultado = numhumano+nummaquina
while numhumano != 0 or nummaquina != 0:
    if resultado % 2 == 0:
        print("El resultado es",resultado,", por lo tanto es par")
        if (resultado%2) == 0 and apuesta == "P":
            print("Ha ganado el humano")
            apuestapar = apuestapar+1
            vecesganadashumano = vecesganadashumano+1
        elif (resultado%2) != 0 and apuesta == "P":
            print("Ha ganado la máquina")
            vecesganadasmaquina = vecesganadasmaquina+1
            apuestanone = apuestanone+1
    elif resultado % 2 != 0:
        print("El resultado es",resultado,", por lo tanto es none")
        if (resultado%2) != 0 and apuesta == "N":
            print("Ha ganado el humano")
            apuestapar = apuestapar+1
            vecesganadashumano = vecesganadashumano+1
        elif (resultado%2) == 0 and apuesta == "N":
            print("Ha ganado la máquina")
            vecesganadasmaquina = vecesganadasmaquina+1
            apuestanone = apuestanone+1
    partidasjugadas = partidasjugadas+1
    numhumano = int(input("Introduce un número del 0 al 5:"))
    apuesta = input("¿Apuestas pares (P) o nones (N)?:").upper
    nummaquina = random.randint(0,5)
print("Mismo número de piedras: Fin")
print("El humano ha ganado",vecesganadashumano,"veces")
print("La máquina ha ganado",vecesganadasmaquina,"veces")
print("Se han jugado",partidasjugadas,"partidas")
if apuestapar < apuestanone:
    print("La apuesta humana más frecuente es nones")
elif apuestapar > apuestanone:
    print("La apuesta humana más frecuente es la par")
elif apuestapar == apuestanone:
    print("El humano ha apostado las mismas veces Pares que Nones")
