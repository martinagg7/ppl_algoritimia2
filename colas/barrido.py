from colas import *
def barrido(cola):
    i=1
    while i<=cola.tamanio:
       dato=cola.mover_al_final()
       print(dato)
       i+=1


       
def barrido(cola):
    cola_aux=Cola()
    while cola.cola_vacia() is False:
        dato=cola.atencion()
        print(dato)
        cola_aux.arribo(dato)
        
    while cola_aux.cola_vacia() is False:
        dato=cola_aux.atencion()
        cola.arribo(dato)

mi_cola = Cola()

mi_cola.arribo(1)
mi_cola.arribo(2)
mi_cola.arribo(3)
mi_cola.arribo(4)

print("Elementos en la cola:")
print(mi_cola.lista_cola())

print("Barrido de la cola:")
barrido(mi_cola)

print("Elementos en la cola después del barrido:")
print(mi_cola.lista_cola())