
class Cola:
    class Nodo:
        def __init__(self,valor):
            self.valor=valor
            self.siguiente=None

    def __init__(self):
        self.frente=None
        self.final=None
        self.tamanio=0
    def anadir_final(self,value):
        nodo=self.Nodo(value)
        if self.tamanio==0:
            self.frente=nodo
        else:
            self.final.siguiente=nodo
        self.final=nodo
        self.tamanio+=1
    def eliminar_frente(self):
        if self.tamanio==0:
            return None
        else:
            valor=self.frente.valor
            self.frente=self.frente.siguiente
            self.tamanio-=1
            return valor
    def vacia(self):
        if self.tamanio==0:
            return True
        else:
            return False
    def list(self):
        lista=[]
        puntero=self.frente
        while puntero is not None:
            lista.append(puntero.valor)
            puntero=puntero.siguiente
        return lista




 






        

