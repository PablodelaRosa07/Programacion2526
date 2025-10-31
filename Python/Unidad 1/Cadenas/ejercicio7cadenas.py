num = input("Introduce un número:")
quitar = int(input("¿Cuántos números quieres quitar?:"))
salida = ""
num = list(num)
for i in range (0,quitar):
    num.pop(0)
for valor in num:
    salida = salida+valor
print(salida)