from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.Abstract.Node_Ast import Node_Ast
from src.Interprete.TS.Exception import Exception

class Println(Instruccion):

    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    
    def interpretar(self, tree, table):

        for instruccion in self.expresion:
            value = instruccion.interpretar(tree, table)
            if isinstance(value, Exception): return value
            tree.update_consola_(value)

        tree.update_consola("");

    def AST(self):
        nodo = Node_Ast("PRINTLN")
        nodo.crearHoja("println")
        nodo.crearHoja("(")
        cont = 0
        for ins in self.expresion:
            if cont == 0:
                nodo.crearNodo(ins.AST())
                cont = 1
            else:
                nodo.crearHoja(",")
                nodo.crearNodo(ins.AST())
        nodo.crearHoja(")")
        nodo.crearHoja(";")
        return nodo