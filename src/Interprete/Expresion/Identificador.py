from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.Abstract.Node_Ast import Node_Ast
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Tipo import Tipo

class Identificador(Instruccion):
    
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna
        self.tipo = None

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.identificador)
        if simbolo == None:
            return Exception("Semantico", "Variable " + self.identificador + " no encontrada.", self.fila, self.columna)

        self.tipo = simbolo.get_tipo()

        if simbolo.get_valor() == None and simbolo.get_tipo() != Tipo.NULO:
            return Exception("Semantico", "Variable " + self.identificador + " vacia.", self.fila, self.columna)
        
        return simbolo.get_valor()


    def AST(self):
        nodo = Node_Ast("IDENTIFICADOR")
        nodo.crearHoja(str(self.identificador))
        return nodo