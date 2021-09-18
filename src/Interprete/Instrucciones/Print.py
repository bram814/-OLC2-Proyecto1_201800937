from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.TS.Exception import Exception

class Print(Instruccion):

    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    
    def interpretar(self, tree, table):
        for instruccion in self.expresion:
            value = instruccion.interpretar(tree, table)

            if isinstance(value, Exception): return value

            tree.update_consola_(value)

    def AST(self):
        pass