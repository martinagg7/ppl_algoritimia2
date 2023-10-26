
class Cola:
    class Nodo:
        def __init__(self,valor):
            self.valor=valor
            self.siguiente=None

    def __init__(self):
        self.frente=None
        self.final=None
        self.tamanio=0
        
    def arribo(self,value):#añadir al final cola
        nodo=self.Nodo(value)
        if self.tamanio==0:
            self.frente=nodo
        else:
            self.final.siguiente=nodo
        self.final=nodo
        self.tamanio+=1

    def atencion(self):
        if self.tamanio==0:
            return None
        else:
            valor=self.frente.valor
            self.frente=self.frente.siguiente
            self.tamanio-=1
            return valor
    def cola_vacia(self):
        "Devulve true si esta vacia"
        return self.frente is None
    
    def en_frente(self):
        return self.frente.valor
    
    def tamanio(self):
        return self.tamanio
    
    def mover_al_final(self):
        if self.tamanio==0:
            return None
        else:
            "Mueve un elemento del inicio de la cola al final"
        dato=self.atencion()
        self.arribo(dato)
        return dato
    
    def lista_cola(self):
        lista=[]
        puntero=self.frente
        while puntero is not None:
            lista.append(puntero.valor)
            puntero=puntero.siguiente
        return lista





 






        

