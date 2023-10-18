lista=[1,3,2,4]
for i in range(len(lista)-1):
    if lista[i]>lista[i+1]:
        lista[i],lista[i+1]=lista[i+1],lista[i]