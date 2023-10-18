def suma(n):
    if n==0:
        resultado=0
    else:
        resultado=n+suma(n-1)
    return resultado

print(suma(3))