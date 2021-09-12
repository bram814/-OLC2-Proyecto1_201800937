from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception

class Return(Instruccion):

    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna
        self.tipo = None
        self.result = None

    def interpretar(self, tree, table):
        result = self.expresion.interpretar(tree, table)
        if isinstance(result, Exception): return result

        self.tipo = self.expresion.tipo 
        self.result = result            # Devuelve el Resultado.

        return self


    def AST(self):
        pass