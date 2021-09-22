from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.Abstract.Node_Ast import Node_Ast
from src.Interprete.TS.Exception import Exception

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
        nodo = Node_Ast("RETURN")
        nodo.crearHoja("return")
        nodo.crearHoja(str(self.result))
        nodo.crearHoja(";")
        return nodo
        