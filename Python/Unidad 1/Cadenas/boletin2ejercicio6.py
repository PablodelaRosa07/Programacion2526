texto = "La inyección de SQL es un tipo de ciberataque encubierto en el cual un hacker inserta código propio en un sitio web con el fin de quebrantar las medidas de seguridad y acceder a datos protegidos. Una vez dentro, puede controlar la base de datos del sitio web y secuestrar la información de los usuarios. Le explicamos cómo funcionan los ataques de inyección de SQL, cómo combatirlos y cómo una herramienta antivirus potente lo puede proteger contra las consecuencias"
cadena = texto.split(".")
cadena2 = texto.split()
print(cadena)
print("Hay",len(cadena),"frases y",len(cadena2),"palabras en total")
frase1 = "La inyección de SQL es un tipo de ciberataque encubierto en el cual un hacker inserta código propio en un sitio web con el fin de quebrantar las medidas de seguridad y acceder a datos protegidos"
frase2 = "Una vez dentro, puede controlar la base de datos del sitio web y secuestrar la información de los usuarios"
frase3 = "Le explicamos cómo funcionan los ataques de inyección de SQL, cómo combatirlos y cómo una herramienta antivirus potente lo puede proteger contra las consecuencias"
cadenafrase1 = frase1.split()
cadenafrase2 = frase2.split()
cadenafrase3 = frase3.split()
print("Hay",len(cadenafrase1),"en la primera frase",len(cadenafrase2),"en la segunda y",len(cadenafrase3),"en la tercera")