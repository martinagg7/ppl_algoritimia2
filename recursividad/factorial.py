def factorial(n):
    if n== 0:
        return 1
    else:
        return n*factorial(n-1)

def hanoi(n, origen, auxiliar, destino):
    pass



def ordenarCONrecursividad(ordenada, desordenada):
    def f_minimo(lista):
        if not lista:
            return None, []
    
        minimo = min(lista)
        lista_sin_minimo = [x for x in lista if x != minimo]
        return minimo, lista_sin_minimo

    if len(desordenada)==1:
        ultimo = desordenada[0]
        ordenada.append(ultimo)
        return ordenada, []
    else:
        minimo, desordenada = f_minimo(desordenada)
        ordenada.append(minimo)
        ordenada, desordenda = ordenarCONrecursividad(ordenada, desordenada)

destino = [2]
origen = [6,4,33,4,5,6,7,87,8]
destino, origen = ordenarCONrecursividad(destino, origen)

print(destino)
