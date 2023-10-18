"Escribe una función recursiva que sume todos los números pares o impares en un rango dado"
def sumar_pares(lista,n=0,suma=0):
    if n==len(lista):
        return suma
    else:
        if lista[n]%2==0:
            suma+=lista[n]
        n+=1
        return(sumar_pares(lista,n,suma))

print(sumar_pares([1,2,3]))