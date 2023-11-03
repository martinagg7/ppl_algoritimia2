"Clase polinomio"

class Nodo:
    def __init__(self, valor, termino):
        self.valor = valor
        self.termino = termino
        self.sig = None

class Polinomio:
    def __init__(self):
        self.cima = None
        self.terminos = 0

    def apilar_OLD(self, valor, termino):
        nuevo_nodo = Nodo(valor, termino)
        nuevo_nodo.sig = self.cima
        self.cima = nuevo_nodo
        self.terminos += 1

    def desapilar(self):
        if self.cima is not None:
            valor = self.cima.valor
            termino=self.cima.termino
            self.cima = self.cima.sig
            self.terminos -= 1
            return valor,termino
        else:
            return None
        
    def agregar_termino(self, valor, termino):
        nodo = Nodo(valor, termino)
        puntero=self.cima
        anterior=None 
        insertado =False

        while puntero.sig is not None or not insertado:
            if anterior is not None and anterior.termino>nodo.termino>puntero.termino:
                    anterior.sig=nodo
                    nodo.sig=puntero
                    insertado=True
            elif nodo.termino>puntero.termino:
                    self.cima=nodo
                    nodo.sig=puntero
                    insertado = True
            if not insertado:
                anterior=puntero
                puntero=puntero.sig



    def agregar_termino_BAD(self, valor, termino):
        nodo = Nodo(valor, termino)
        polinomio_aux = Polinomio()

        if self.cima is None:
            self.cima = nodo
        else:
            if nodo.termino >= self.cima.termino:

                nodo.sig = self.cima
                self.cima = nodo

            else:
                while self.cima.termino>nodo.termino:
                    polinomio_aux.apilar(self.desapilar())
                self.apilar(nodo.valor,nodo.termino)
                while polinomio_aux.cima is not None:
                    self.apilar(polinomio_aux.desapilar())

    def obtener_valor_BAD(self,termino):
        aux=self.cima
        while aux.termino>termino:
            aux=aux.sig
        if aux.termino==termino:
            return aux.valor
        else:
            return None


    def obtener_valor(self, termino):
        puntero=self.cima
        encontrado=False
        valor=None
        while puntero is not None and not encontrado:
            if puntero.termino==termino:
                valor=puntero.valor   
                encontrado = True                                    
            else:
                puntero=puntero.sig
        return valor
    
    def imprimir_polinimio(self):
        l=[]
        aux=self.cima
        while aux is not None:
            l.append(aux.valor + "X^" + aux.termino)
            aux=aux.sig
        polinomio_str="+".join(l)
        return polinomio_str
        

                



  





