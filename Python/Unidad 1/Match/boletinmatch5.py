print("Las habitaciones son:" \
" 1.Azul" \
" 2.Roja" \
" 3.Verde" \
" 4.Rosa" \
" 5.Gris")
hab = float(input("¿Qué número de habitación desea?:"))
if hab == 1:
    print("La habitación azul tiene 2 camas y está en la primera planta")
elif hab == 2:
    print("La habitación roja tiene 1 cama y está en la primera planta")
elif hab == 3:
    print("La habitación verde tiene 3 camas y está en la segunda planta")
elif hab == 4:
    print("La habitación rosa tiene 2 camas y está en la segunda planta")
elif hab == 5:
    print("La habitación gris tiene 1 camas y está en la tercera planta")
else:
    print("Ha habido un error")