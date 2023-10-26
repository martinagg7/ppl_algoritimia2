from pilas import *

def barrido(pila):
    paux=Pila()
    
    while pila.pila_vacia() is not True:
        dato=pila.desapilar()
        print(dato)
        paux.apilar(dato)

    while paux.pila_vacia() is not True:
        dato=paux.desapilar()
        pila.apilar(dato)

mi_pila=Pila()
mi_pila.apilar(4)
mi_pila.apilar(2)
print(mi_pila.lista_pila())

barrido(mi_pila)