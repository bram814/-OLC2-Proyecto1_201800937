from Interprete.Abstract.Instruccion import Instruccion

class Primitivo(Instruccion):
    
    def __init__(self, tipo, valor, fila, columna):
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table):
        return self.valor

    def AST(self):
        pass