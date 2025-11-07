c1=0
c2=0
c3=0
c4=0
c5=0
c6=0
a=input("¿Deseas registrar un nuevo incidente? Si (S) o No (N):").upper()
while a!="N":
    if a=="S":
        c1=c1+1
        b=input("¿En  qué nivel ha ocurrido: E (para los incidentes de ESO) y P (para los incidentes de Post-Obligatoria) ?").upper()
        while b!="E" and b!="P":
            b=input("¿En  qué nivel ha ocurrido: E (para los incidentes de ESO) y P (para los incidentes de Post-Obligatoria) ?").upper()
        if b=="E":
            c2+=1
        elif b=="P":
            c3+=1
        c=input("¿Qué tipo de incidente ha ocurrido? Tipo de incidente: L(para incidentes Leves) o G(para incidentes Graves):").upper()
        while c!="L" and c!="G":
            c=input("¿Qué tipo de incidente ha ocurrido? Tipo de incidente: L(para incidentes Leves) o G(para incidentes Graves:").upper()
        if c=="L":
            c4+=1
        elif c=="G":
            c5+=1
        a=input("¿Deseas registrar un nuevo incidente? Si (S) o No (N):").upper()
    else:
        a=input("¿Deseas registrar un nuevo incidente? Si (S) o No (N):").upper()
total=c4+c5
print("Incidentes registrados")
print(f"Se han registrado {c1} incidencias, de ellas {c2} han sido en la ESO y {c3}en estudios postobligatorios, finalmente,{(c4/total)*100}% de incidentes leves y {(c5/total)*100}% de incidentes graves")