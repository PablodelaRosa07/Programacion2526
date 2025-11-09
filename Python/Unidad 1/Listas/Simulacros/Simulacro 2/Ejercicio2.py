impares=[]
contaimpar=0
num1=int(input("Introduce un número:"))
num2=int(input("Introduce otro número:"))
if num1 !=0 and num2!=0:
    while num1>=num2:
        num1=int(input("Introduce un número:"))
        num2=int(input("Introduce otro número:"))
    rango=input("¿El rango es abierto(A) o es cerrado(C)?").lower()
    while num1 !=0 or num2!=0:
        
        if rango =="c":
            for i in range(num1,num2+1):
                if i%2==1:
                    impares.append(i)
                    contaimpar = contaimpar+1                  
            print("=========================================================")
            print(f"Impares que existen entre {num1} y el {num2}:{impares} ")
            print(f"En total existen {contaimpar} números impares en el rango.")
            print("=========================================================")
            contaimpar = 0
            impares = []
        elif rango =="a":
            for i in range(num1+1,num2):
                if i%2==1:
                    impares.append(i)
                    contaimpar = contaimpar+1           
            print("=========================================================")
            print(f"Impares que existen entre {num1} y el {num2}:{impares} ")
            print(f"En total existen {contaimpar} números impares en el rango.")
            print("=========================================================")
            contaimpar = 0  
            impares = [] 
        num1=int(input("Introduce un número:"))
        num2=int(input("Introduce otro número:"))
        while num1>=num2:
            num1=int(input("Introduce un número:"))
            num2=int(input("Introduce otro número:"))
            if num1 !=0 or num2!=0:
                rango=input("¿El rango es abierto(A) o es cerrado(C)?").lower()