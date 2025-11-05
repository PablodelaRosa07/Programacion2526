import random
lista = ["Cutaneo del cuello", "Esternocleidomastoideo","Pectoral mayor", "Escaleno", "Deltoides", "Biceps braquial", "Braquial" ,"Serrato", "Recto del abdomen", "Oblicuo", "Transverso", "Supinador" ,"Iliaco" ,"Cubital", "Supinador corto", "Flexor del pulgar", "Pectineo", "Sartorio", "Vasto externo", "Vasto interno", "Recto anterior", "Tibial", "Gemelo" ,"Sóleo" ,"Extensor de los dedos del pie", "Pedio", "Lumbricales","Occipital","Esplenio","Trapecio","Deltoides","Redondo menor","Redondo mayor","Supinador","Cubital posterior","Infraespinoso","Romboide","Triceps braquial","Dorsal ancho","Anconeo","Extensor del meñique","Gluteo mayor","Semitendinoso","Aductor mayor","Biceps crural","Semimembranoso","Plantar","Gemelos","Plexor largo de los dedos","Tendón"]

for i in range(51):
    ran = random.choice(lista)
    match ran:
        case "Cutaneo del cuello": #1
            respuesta = input("¿Dónde está Cutaneo del cuello?:").lower
            if respuesta == "cuello":
                print("Has acertado")
            else:
                print("Has fallado, está en el cuello")
            lista.pop(lista.index("Cutaneo del cuello"))
        case "Esternocleidomastoideo": #2
            respuesta = input("¿Dónde está Esternocleidomastoideo?:").lower
            if respuesta == "cuello":
                print("Has acertado")
            else:
                print("Has fallado, está en el cuello")
            lista.pop(lista.index("Esternocleidomastoideo"))
        case "Pectoral mayor": #3
            respuesta = input("¿Dónde está Pectoral mayor?:").lower
            if respuesta == "pecho":
                print("Has acertado")
            else:
                print("Has fallado, está en el pecho")
            lista.pop(lista.index("Pectoral mayor"))
        case "Escaleno": #4
            respuesta = input("¿Dónde está Escaleno?:").lower
            if respuesta == "cuello":
                print("Has acertado")
            else:
                print("Has fallado, está en el cuello")
            lista.pop(lista.index("Escaleno"))
        case "Escaleno": #5
            respuesta = input("¿Dónde está Deltoides?:").lower
            if respuesta == "hombro":
                print("Has acertado")
            else:
                print("Has fallado, está en el hombro")
            lista.pop(lista.index("Deltoides"))
        case "Escaleno": #6
            respuesta = input("¿Dónde está Biceps braquial?:").lower
            if respuesta == "brazo":
                print("Has acertado")
            else:
                print("Has fallado, está en el brazo")
            lista.pop(lista.index("Biceps braquial"))
        case "Escaleno": #7
            respuesta = input("¿Dónde está Braquial?:").lower
            if respuesta == "brazo":
                print("Has acertado")
            else:
                print("Has fallado, está en el brazo")
            lista.pop(lista.index("Braquial"))
        case "Escaleno": #8
            respuesta = input("¿Dónde está Serrato?:").lower
            if respuesta == "torax":
                print("Has acertado")
            else:
                print("Has fallado, está en el torax")
            lista.pop(lista.index("Serrato"))
        case "Escaleno": #9
            respuesta = input("¿Dónde está Recto del abdomen?:").lower
            if respuesta == "abdomen":
                print("Has acertado")
            else:
                print("Has fallado, está en el abdomen")
            lista.pop(lista.index("Recto del abdomen"))
        case "Escaleno": #10
            respuesta = input("¿Dónde está Oblicuo?:").lower
            if respuesta == "abdomen":
                print("Has acertado")
            else:
                print("Has fallado, está en el abdomen")
            lista.pop(lista.index("Oblicuo"))
        case "Escaleno": #11
            respuesta = input("¿Dónde está Transverso?:").lower
            if respuesta == "abdomen":
                print("Has acertado")
            else:
                print("Has fallado, está en el abdomen")
            lista.pop(lista.index("Transverso"))
        case "Escaleno": #12
            respuesta = input("¿Dónde está Supinador?:").lower
            if respuesta == "brazo":
                print("Has acertado")
            else:
                print("Has fallado, está en el brazo")
            lista.pop(lista.index("Supinador"))
        case "Escaleno": #13
            respuesta = input("¿Dónde está Iliaco?:").lower
            if respuesta == "abdomen":
                print("Has acertado")
            else:
                print("Has fallado, está en el abdomen")
            lista.pop(lista.index("Iliaco"))
        case "Escaleno": #14
            respuesta = input("¿Dónde está Cubital?:").lower
            if respuesta == "brazo":
                print("Has acertado")
            else:
                print("Has fallado, está en el brazo")
            lista.pop(lista.index("Cubital"))
        case "Escaleno": #15
            respuesta = input("¿Dónde está Supinador corto?:").lower
            if respuesta == "muñeca":
                print("Has acertado")
            else:
                print("Has fallado, está en la muñeca")
            lista.pop(lista.index("Supinador corto"))
        case "Escaleno": #16
            respuesta = input("¿Dónde está Flexor del pulgar?:").lower
            if respuesta == "brazo":
                print("Has acertado")
            else:
                print("Has fallado, está en el brazo")
            lista.pop(lista.index("Flexor del pulgar"))
        case "Escaleno": #17
            respuesta = input("¿Dónde está Pectineo?:").lower
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna")
            lista.pop(lista.index("Pectineo"))
        case "Sartorio":
            respuesta = input("¿Dónde está el Sartorio?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna")
            lista.pop(lista.index("Sartorio"))
        case "Vasto externo":
            respuesta = input("¿Dónde está el Vasto externo?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna")
            lista.pop(lista.index("Vasto externo"))

        case "Vasto interno":
            respuesta = input("¿Dónde está el Vasto interno?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna")
            lista.pop(lista.index("Vasto interno"))

        case "Recto anterior":
            respuesta = input("¿Dónde está el Recto anterior?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna")
            lista.pop(lista.index("Recto anterior"))

        case "Tibial":
            respuesta = input("¿Dónde está el Tibial?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna")
            lista.pop(lista.index("Tibial"))

        case "Gemelo":
            respuesta = input("¿Dónde está el Gemelo?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna")
            lista.pop(lista.index("Gemelo"))

        case "Sóleo":
            respuesta = input("¿Dónde está el Sóleo?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna")
            lista.pop(lista.index("Sóleo"))

        case "Extensor de los dedos del pie":
            respuesta = input("¿Dónde está el Extensor de los dedos del pie?: ").lower()
            if respuesta == "pie":
                print("Has acertado")
            else:
                print("Has fallado, está en el pie")
            lista.pop(lista.index("Extensor de los dedos del pie"))

        case "Pedio":
            respuesta = input("¿Dónde está el Pedio?: ").lower()
            if respuesta == "pie":
                print("Has acertado")
            else:
                print("Has fallado, está en el pie")
            lista.pop(lista.index("Pedio"))

        case "Lumbricales":
            respuesta = input("¿Dónde están los Lumbricales?: ").lower()
            if respuesta == "mano" or respuesta == "pie":
                print("Has acertado")
            else:
                print("Has fallado, están en la mano o en el pie")
            lista.pop(lista.index("Lumbricales"))

        case "Occipital":
            respuesta = input("¿Dónde está el Occipital?: ").lower()
            if respuesta == "cabeza":
                print("Has acertado")
            else:
                print("Has fallado, está en la cabeza")
            lista.pop(lista.index("Occipital"))

        case "Esplenio":
            respuesta = input("¿Dónde está el Esplenio?: ").lower()
            if respuesta == "cuello":
                print("Has acertado")
            else:
                print("Has fallado, está en el cuello")
            lista.pop(lista.index("Esplenio"))

        case "Trapecio":
            respuesta = input("¿Dónde está el Trapecio?: ").lower()
            if respuesta == "espalda":
                print("Has acertado")
            else:
                print("Has fallado, está en la espalda")
            lista.pop(lista.index("Trapecio"))

        case "Deltoides":
            respuesta = input("¿Dónde está el Deltoides?: ").lower()
            if respuesta == "hombro":
                print("Has acertado")
            else:
                print("Has fallado, está en el hombro")
            lista.pop(lista.index("Deltoides"))

        case "Redondo menor":
            respuesta = input("¿Dónde está el Redondo menor?: ").lower()
            if respuesta == "hombro":
                print("Has acertado")
            else:
                print("Has fallado, está en el hombro")
            lista.pop(lista.index("Redondo menor"))

        case "Redondo mayor":
            respuesta = input("¿Dónde está el Redondo mayor?: ").lower()
            if respuesta == "hombro":
                print("Has acertado")
            else:
                print("Has fallado, está en el hombro")
            lista.pop(lista.index("Redondo mayor"))

        case "Supinador":
            respuesta = input("¿Dónde está el Supinador?: ").lower()
            if respuesta == "brazo":
                print("Has acertado")
            else:
                print("Has fallado, está en el brazo")
            lista.pop(lista.index("Supinador"))

        case "Cubital posterior":
            respuesta = input("¿Dónde está el Cubital posterior?: ").lower()
            if respuesta == "brazobrazo":
                print("Has acertado")
            else:
                print("Has fallado, está en el brazo")
            lista.pop(lista.index("Cubital posterior"))

        case "Infraespinoso":
            respuesta = input("¿Dónde está el Infraespinoso?: ").lower()
            if respuesta == "espalda":
                print("Has acertado")
            else:
                print("Has fallado, está en la espalda")
            lista.pop(lista.index("Infraespinoso"))

        case "Romboide":
            respuesta = input("¿Dónde está el Romboide?: ").lower()
            if respuesta == "espalda":
                print("Has acertado")
            else:
                print("Has fallado, está en la espalda")
            lista.pop(lista.index("Romboide"))

        case "Triceps braquial":
            respuesta = input("¿Dónde está el Triceps braquial?: ").lower()
            if respuesta == "brazo":
                print("Has acertado")
            else:
                print("Has fallado, está en el brazo")
            lista.pop(lista.index("Triceps braquial"))

        case "Dorsal ancho":
            respuesta = input("¿Dónde está el Dorsal ancho?: ").lower()
            if respuesta == "espalda":
                print("Has acertado")
            else:
                print("Has fallado, está en la espalda")
            lista.pop(lista.index("Dorsal ancho"))

        case "Anconeo":
            respuesta = input("¿Dónde está el Anconeo?: ").lower()
            if respuesta == "brazo":
                print("Has acertado")
            else:
                print("Has fallado, está en el brazo")
            lista.pop(lista.index("Anconeo"))

        case "Extensor del meñique":
            respuesta = input("¿Dónde está el Extensor del meñique?: ").lower()
            if respuesta == "brazo":
                print("Has acertado")
            else:
                print("Has fallado, está en el brazo")
            lista.pop(lista.index("Extensor del meñique"))

        case "Gluteo mayor":
            respuesta = input("¿Dónde está el Gluteo mayor?: ").lower()
            if respuesta == "gluteo":
                print("Has acertado")
            else:
                print("Has fallado, está en los glúteos")
            lista.pop(lista.index("Gluteo mayor"))

        case "Semitendinoso":
            respuesta = input("¿Dónde está el Semitendinoso?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna")
            lista.pop(lista.index("Semitendinoso"))

        case "Aductor mayor":
            respuesta = input("¿Dónde está el Aductor mayor?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna")
            lista.pop(lista.index("Aductor mayor"))

        case "Biceps crural":
            respuesta = input("¿Dónde está el Biceps crural?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en pierna")
            lista.pop(lista.index("Biceps crural"))

        case "Semimembranoso":
            respuesta = input("¿Dónde está el Semimembranoso?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna")
            lista.pop(lista.index("Semimembranoso"))

        case "Plantar":
            respuesta = input("¿Dónde está el Plantar?: ").lower()
            if respuesta == "pierna" or respuesta == "pie":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna o el pie")
            lista.pop(lista.index("Plantar"))

        case "Gemelos":
            respuesta = input("¿Dónde están los Gemelos?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, están en la pierna")
            lista.pop(lista.index("Gemelos"))

        case "Plexor largo de los dedos":
            respuesta = input("¿Dónde está el Plexor largo de los dedos?: ").lower()
            if respuesta == "brazo":
                print("Has acertado")
            else:
                print("Has fallado, está en el brazo")
            lista.pop(lista.index("Plexor largo de los dedos"))

        case "Tendón":
            respuesta = input("¿Dónde está el Tendón?: ").lower()
            if respuesta == "pierna":
                print("Has acertado")
            else:
                print("Has fallado, está en la pierna")
            lista.pop(lista.index("Tendón"))