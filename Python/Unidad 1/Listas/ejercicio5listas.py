import random
listanum=[]
listacuadrados=[]
listacubos=[]
for i in range (1,21):
    num = random.randint(0,100)
    listanum.append(num)
    listacuadrados.append(num**2)
    listacubos.append(num**3)
    print(num,"",num**2,"",num**3)