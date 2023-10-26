class Nodo():
    def __init__(self,valor):
        self.valor=valor#aqui porque no pones none
        self.siguiente=None

class Pila():
    def __init__(self):
        self.cima=None
        self.tamaño=0
    def apilar(self,valor):
        nodo=Nodo(valor)
        nodo.siguiente=self.cima
        self.cima=nodo
        self.tamaño+=1
    def desapilar(self):
        valor=self.cima.valor
        self.cima=self.cima.siguiente
        self.tamaño-=1
        return valor
    def vacia(self):
        if Pila.tamaño==0:
            return "la pila esta vacia"
    def tamaño(self):
        return self.tamaño
