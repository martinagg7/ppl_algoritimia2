
from colas import *
class Colas_prioridad():
    def __init__(self):
        self.colas_prioridad=[Cola(),Cola(),Cola(),Cola(),Cola()]
        self.tamaño=0
    def queue(self,paciente,prioridad):
        self.colas_prioridad[prioridad].arribo(paciente)
        self.tamaño+=1
    def dequeue(self):
        for cola in self.colas_prioridad:
            while cola.tamanio!=0:
                cola.atencion()
                self.tamaño-=1

