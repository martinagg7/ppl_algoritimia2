class Pila:
    class Nodo:
        def __init__(self, value):
            self.value = value
            self.next_node = None

    def __init__(self):
        self.cima = None
        self.tamanio = 0

    def create_node(self, value):
        return self.Nodo(value)

    def apilar(self, value):
        node = self.create_node(value)
        node.next_node = self.cima
        self.cima = node
        self.tamanio += 1

    def desapilar(self):
        value = None
        if self.cima is not None:
            value = self.cima.value
            self.cima = self.cima.next_node
            self.tamanio -= 1
        return value

    def pila_vacia(self):
        "Devuelve true si la pila vacia"
        return self.cima is None

    def size(self):
        return self.tamanio

    def top(self):
        if self.cima is not None:
            return self.cima.value
        else:
            return None

    def lista_pila(self):
        values = []
        pointer = self.cima
        while pointer is not None:
            values.append(pointer.value)
            pointer = pointer.next_node
        return values




