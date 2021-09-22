from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.Abstract.Node_Ast import Node_Ast
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Tipo import *

class Aritmetica(Instruccion):

    def __init__(self, exp_left, operador, exp_rigth, fila, columna):
        self.exp_left = exp_left
        self.operador = operador
        self.exp_rigth = exp_rigth
        self.fila = fila
        self.columna = columna
        self.tipo = None

    def interpretar(self, tree, table):
        left = self.exp_left.interpretar(tree, table)
        if isinstance(left, Exception): return left
        if self.exp_rigth != None: 
            rigth = self.exp_rigth.interpretar(tree, table)
            if isinstance(rigth, Exception): return rigth

        if self.operador == Operador_Aritmetico.SUMA: # expression + expresion
            # ENTERO
            if self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.INT64:                          # INT + INT = INT
                self.tipo = Tipo.INT64
                return self.casteo(self.exp_left.tipo, left) + self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                      # INT + DOUBLE = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) + self.casteo(self.exp_rigth.tipo, rigth) 
            # DECIMAL
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.INT64:                      # DOUBLE + INT = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) + self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                    # DOUBLE + DOUBLE = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) + self.casteo(self.exp_rigth.tipo, rigth) 
            return Exception("Semantico", "Tipo Erroneo de operacion para +.", self.fila, self.columna)

        elif self.operador == Operador_Aritmetico.RESTA: # expression - expresion
            # ENTERO
            if self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.INT64:                          # INT - INT = INT
                self.tipo = Tipo.INT64
                return self.casteo(self.exp_left.tipo, left) - self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                      # INT - DOUBLE = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) - self.casteo(self.exp_rigth.tipo, rigth) 
            # DECIMAL
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.INT64:                      # DOUBLE - INT = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) - self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                    # DOUBLE - DOUBLE = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) - self.casteo(self.exp_rigth.tipo, rigth) 
            return Exception("Semantico", "Tipo Erroneo de operacion para -.", self.fila, self.columna)
        
        elif self.operador == Operador_Aritmetico.POR: # expression * expresion
            # ENTERO
            if self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.INT64:                          # INT * INT = INT
                self.tipo = Tipo.INT64
                return self.casteo(self.exp_left.tipo, left) * self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                      # INT * DOUBLE = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) * self.casteo(self.exp_rigth.tipo, rigth) 
            # DECIMAL
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.INT64:                      # DOUBLE * INT = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) * self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                    # DOUBLE * DOUBLE = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) * self.casteo(self.exp_rigth.tipo, rigth) 
            # CADENA
            elif self.exp_left.tipo == Tipo.STRING and self.exp_rigth.tipo == Tipo.STRING:                      # STRING * STRING = STRING
                self.tipo = Tipo.STRING
                return self.casteo(self.exp_left.tipo, left) + self.casteo(self.exp_rigth.tipo, rigth)
            # CHAR
            elif self.exp_left.tipo == Tipo.CHAR and self.exp_rigth.tipo == Tipo.CHAR:                          # CHAR * CHAR = CHAR
                self.tipo = Tipo.CHAR
                return self.casteo(self.exp_left.tipo, left) + self.casteo(self.exp_rigth.tipo, rigth)
             
            return Exception("Semantico", "Tipo Erroneo de operacion para *.", self.fila, self.columna)

        elif self.operador == Operador_Aritmetico.DIV: # expression / expresion
            # ENTERO
            if self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.INT64:                          # INT / INT = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) / self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                      # INT / DOUBLE = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) / self.casteo(self.exp_rigth.tipo, rigth) 
            # DECIMAL
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.INT64:                      # DOUBLE / INT = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) / self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                    # DOUBLE / DOUBLE = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) / self.casteo(self.exp_rigth.tipo, rigth) 
            return Exception("Semantico", "Tipo Erroneo de operacion para /.", self.fila, self.columna)

        elif self.operador == Operador_Aritmetico.POTE: # expression ^ expresion
            # ENTERO
            if self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.INT64:                          # INT ^ INT = INT
                self.tipo = Tipo.INT64
                return self.casteo(self.exp_left.tipo, left) ** self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                      # INT ^ DOUBLE = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) ** self.casteo(self.exp_rigth.tipo, rigth) 
            # DECIMAL
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.INT64:                      # DOUBLE / INT = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) ** self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                    # DOUBLE / DOUBLE = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) ** self.casteo(self.exp_rigth.tipo, rigth)
            # CADENA
            elif self.exp_left.tipo == Tipo.STRING and self.exp_rigth.tipo == Tipo.INT64:                      # STRING * STRING = STRING
                self.tipo = Tipo.STRING
                return self.casteo(self.exp_left.tipo, left) * self.casteo(self.exp_rigth.tipo, rigth)
            # CHAR
            elif self.exp_left.tipo == Tipo.CHAR and self.exp_rigth.tipo == Tipo.INT64:                          # CHAR * CHAR = CHAR
                self.tipo = Tipo.CHAR
                return self.casteo(self.exp_left.tipo, left) * self.casteo(self.exp_rigth.tipo, rigth) 

            return Exception("Semantico", "Tipo Erroneo de operacion para ^.", self.fila, self.columna)

        elif self.operador == Operador_Aritmetico.MODU: # expression % expresion
            # ENTERO
            if self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.INT64:                          # INT % INT = DOUBLE
                self.tipo = Tipo.INT64
                return self.casteo(self.exp_left.tipo, left) % self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                      # INT % DOUBLE = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) % self.casteo(self.exp_rigth.tipo, rigth) 
            # DECIMAL
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.INT64:                      # DOUBLE % INT = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) % self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                    # DOUBLE % DOUBLE = DOUBLE
                self.tipo = Tipo.FLOAT64
                return self.casteo(self.exp_left.tipo, left) % self.casteo(self.exp_rigth.tipo, rigth) 
            return Exception("Semantico", "Tipo Erroneo de operacion para %.", self.fila, self.columna)

        elif self.operador == Operador_Aritmetico.UMENOS: #NEGACION UNARIA
            if self.exp_left.tipo == Tipo.INT64:
                self.tipo = Tipo.INT64
                return - self.casteo(self.exp_left.tipo, left)
            elif self.exp_left.tipo == Tipo.FLOAT64:
                self.tipo = Tipo.FLOAT64
                return - self.casteo(self.exp_left.tipo, left)
            return Exception("Semantico", "Tipo Erroneo de operacion para - unario.", self.fila, self.columna)

        return Exception("Semantico", "Tipo de Operacion Aritmética no Especificado.", self.fila, self.columna)    

    def AST(self):
        nodo = Node_Ast("ARITMÉTICA")
        if self.exp_rigth != None:
            nodo.crearNodo(self.exp_left.AST())
            nodo.crearHoja(self.operator())
            nodo.crearNodo(self.exp_rigth.AST())
        else:
            nodo.crearHoja(self.operator())
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
        
    def operator(self):
        if self.operador == Operador_Aritmetico.SUMA:
            return "+"
        elif self.operador == Operador_Aritmetico.RESTA:
            return "-"
        elif self.operador == Operador_Aritmetico.POR:
            return "*"
        elif self.operador == Operador_Aritmetico.DIV:
            return "/"
        elif self.operador == Operador_Aritmetico.POTE:
            return "^"
        elif self.operador == Operador_Aritmetico.MODU:
            return "&"
        elif self.operador == Operador_Aritmetico.UMENOS:
            return "-"
    