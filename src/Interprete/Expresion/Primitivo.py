from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.Abstract.Node_Ast import Node_Ast

class Primitivo(Instruccion):
    
    def __init__(self, tipo, valor, fila, columna):
        self.tipo = tipo
        self.valor = valor
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table):
        return self.valor

    def AST(self):
        nodo = Node_Ast("PRIMITIVO")
        nodo.crearHoja(str(self.valor))
        return nodo