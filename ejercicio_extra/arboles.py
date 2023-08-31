class Nodo:
    def __init__(self, valor, hijos=None):
        self.valor = valor
        self.hijos = hijos
        if hijos is not None:
            if isinstance(hijos, Nodo):
                self.agregar_hijo(hijos)
            else:
                for hijo in hijos:
                    self.agregar_hijo(hijo)
        else:
            self.hijos = []

    def __repr__(self):
        return f'{self.valor} -- {self.hijos}'

    def agregar_hijo(self, nodo_hijo):
        if not self.hijos:
            self.hijos = []
        self.hijos.append(nodo_hijo)
