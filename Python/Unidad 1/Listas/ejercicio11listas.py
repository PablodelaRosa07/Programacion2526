import random
lista=[]
pop = 0
for i in range (0,20):
    num = random.randint(0,100)
    if num % 2 == 0:
        lista.append(num)
        lista.pop(pop)
        lista.insert(0, num)
    else:
        lista.append(num)
    pop=pop+1
print(lista)