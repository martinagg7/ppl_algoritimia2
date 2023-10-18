def sumar(lista, n=0,suma=0):
    if n==len(lista):
        return suma
    else:
        suma+=lista[n]
        n=n+1
        sumar(lista,n,suma)