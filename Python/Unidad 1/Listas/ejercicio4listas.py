num = int(input("Introduce un número:"))
lista=[]
for i in range(0,num+1):
    print(i)
    lista.append(i)
if i == num:    
    for i in range (num+1,0,-1):
        print(i)
print(lista[:])