class Tree:
    def __init__(self):
        self.raiz = None
        self.size = 0
    
    def setRaiz(self, raiz):
        if (self.raiz == None):
            self.raiz = raiz
            self.size = 1
        else:
            return "Raiz já definida"


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
    
    def setProximo(self, proximo):
        self.proximo = proximo