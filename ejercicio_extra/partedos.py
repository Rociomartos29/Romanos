
class Nodo:
    def __init__(self, valor,):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

    def insertar(self, valor):
        if valor < self.valor:
            if self.izquierda is None:
                self.izquierda = Nodo(valor)
            else:
                self.izquierda.insertar(valor)
        elif valor > self.valor:
            if self.derecha is None:
                self.derecha = Nodo(valor)
            else:
                self.derecha.insertar(valor)

    def __repr__(self):
        elementos = []
        self.in_order_traversal(elementos)
        return '  '.join(str(elemento)for elemento in elementos)
    
    def in_order_traversal (self, elementos):
        if self.izquierda:
            self.izquierda.inorden(elementos)
            if self.valor not in elementos:
                elementos.append(self.valor)
            if self.derecha:
                self.derecha.in_order_traversal(elementos)
