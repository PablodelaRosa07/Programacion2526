import random
humano = float(input("Elige: Piedra(0), Papel(1), Tijeras(2):"))
maquina = random.randint(0, 2)
print("La maquina ha elegido:", maquina)
match humano:
    case 0:
        if maquina == 0:
            print("Has empatado, la máquina ha elegido Piedra, tú también")
        elif maquina == 1:
            print("Has perdido, la máquina ha elegido Papel, tú Piedra")
        elif maquina ==2:
            print("Has ganado, la máquina ha elegido Tijeras, tú Piedra")
    case 1:
        if maquina == 0:
            print("Has ganado, la máquina ha elegido Piedra y tú Papel")
        elif maquina == 1:
            print("Has empatado, la máquina ha elegido Papel, tú también")
        elif maquina ==2:
            print("Has perdido, la máquina ha elegido Tijeras, tú Papel")
    case 2:
        if maquina == 0:
            print("Has perdido, la máquina ha elegido Piedra, tú Tijeras")
        elif maquina == 1:
            print("Has ganado, la máquina ha elegido Papel, tú Tijeras")
        elif maquina ==2:
            print("Has empatado, la máquina ha elegido Tijeras, tú también")
    case _:
        print("No es un número válido")