from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.Abstract.Node_Ast import Node_Ast
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Tipo import *

class Logica(Instruccion):
    
    def __init__(self, exp_left, operador, exp_right, fila, columna):
        self.exp_left = exp_left
        self.operador = operador
        self.exp_right = exp_right
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.BOOLEANO

     
    def interpretar(self, tree, table):
        left = self.exp_left.interpretar(tree, table)
        if isinstance(left, Exception): return left
        if self.exp_right != None:
            right = self.exp_right.interpretar(tree, table)
            if isinstance(right, Exception): return right


        if self.operador == Operador_Logico.AND:
            if self.exp_left.tipo == Tipo.BOOLEANO and self.exp_right.tipo == Tipo.BOOLEANO:
                return self.casteo(self.exp_left.tipo, left) and self.casteo(self.exp_right.tipo, right)
            return Exception("Semantico", "Tipo Erroneo de operacion para &&.", self.fila, self.columna)
        
        elif self.operador == Operador_Logico.OR:
            if self.exp_left.tipo == Tipo.BOOLEANO and self.exp_right.tipo == Tipo.BOOLEANO:
                return self.casteo(self.exp_left.tipo, left) or self.casteo(self.exp_right.tipo, right)
            return Exception("Semantico", "Tipo Erroneo de operacion para ||.", self.fila, self.columna)

        elif self.operador == Operador_Logico.NOT:
            if self.exp_left.tipo == Tipo.BOOLEANO:
                return not self.casteo(self.exp_left.tipo, left)
            return Exception("Semantico", "Tipo Erroneo de operacion para !.", self.fila, self.columna)

        return Exception("Semantico", "Tipo de Operacion no Especificado.", self.fila, self.columna)

    def AST(self):
        nodo = Node_Ast("LÓGICA")
        
        if self.exp_right != None:
            nodo.crearNodo(self.exp_left.AST())
            nodo.crearHoja(self.logic())
            nodo.crearNodo(self.exp_right.AST())
        else:
            nodo.crearHoja(self.logic())
            nodo.crearNodo(self.exp_left.AST())
        
        return nodo

    def casteo(self,tipo, valor):
        if tipo == Tipo.INT64:
            return int(valor)
        elif tipo == Tipo.FLOAT64:
            return float(valor)
        elif tipo == Tipo.BOOLEANO:
            return bool(valor)
        return str(valor)
        
    def logic(self):
        if self.operador == Operador_Logico.AND:
            return str("&&")
        elif self.operador == Operador_Logico.OR:
            return str("||")
        elif self.operador == Operador_Logico.NOT:
            return str("!")
           