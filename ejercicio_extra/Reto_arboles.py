class Nodo:
    def __init__(self, valor=None):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
 
    def agregar(self, valor):
        if self.valor is None:
            self.valor = valor
        else:
            if valor < self.valor:
                if self.izquierda is None:
                    self.izquierda = Nodo(valor)
                else:
                    self.izquierda.agregar(valor)
            else:
                if self.derecha is None:
                    self.derecha = Nodo(valor)
                else:
                    self.derecha.agregar(valor)
                    
    def _inorden(self):
        valores = []
        if self.valor is not None:
            if self.izquierda is not None:
                valores += self.izquierda._inorden()
            valores.append(self.valor)
            if self.derecha is not None:
                valores += self.derecha._inorden()
        return valores
 
    def __repr__(self):
        return " ".join(str(valor) for valor in self._inorden())



            