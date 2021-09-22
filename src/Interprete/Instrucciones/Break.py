from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.Abstract.Node_Ast import Node_Ast

class Break(Instruccion):
    def __init__(self, fila, columna):
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return self
        
    def AST(self):
        nodo = Node_Ast("BREAK")
        nodo.crearHoja("break")
        nodo.crearHoja(";")
        return nodo