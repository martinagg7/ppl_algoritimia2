"Dada una lista de letras nos queremos quedar solo con las vocales"
from colas import *
#pedimos al usuario la lista de las letras
cola_datos=Cola()
cola_vocales=Cola()
letra=input("Ingrese una letra:")
while letra!="":
    cola_datos.arribo(letra)
    letra=input("Ingrese una letra:")

def obtener_vocales(cola):
    vocales=["A","E","I","O","U"]
    while cola_datos.cola_vacia() is False:
        dato=cola_datos.atencion()
        if dato.upper() in vocales:
            cola_vocales.arribo(dato)
    return cola_vocales.lista_cola()

print(obtener_vocales(cola_datos))