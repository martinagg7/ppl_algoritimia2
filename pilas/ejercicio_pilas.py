"Pila de números enteros y queremos separala en dos pilas de pares y impares"
from pilas import *
pila_datos=Pila()
pila_datos.apilar(1)
pila_datos.apilar(2)
pila_datos.apilar(3)
pila_datos.apilar(4)
pila_datos.apilar(5)
pila_par=Pila()
pila_impar=Pila()

while pila_datos.pila_vacia() is False:
    dato=pila_datos.desapilar()
    if dato%2==0:
        pila_par.apilar(dato)
    else:
        pila_impar.apilar(dato)

print(pila_par.lista_pila())
print(pila_impar.lista_pila())
