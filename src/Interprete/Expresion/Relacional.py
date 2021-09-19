from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Tipo import *

class Relacional(Instruccion):

    def __init__(self, exp_left, operador, exp_rigth, fila, columna):
        self.exp_left = exp_left
        self.operador = operador
        self.exp_rigth = exp_rigth
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.BOOLEANO


    def interpretar(self, tree, table):
        left = self.exp_left.interpretar(tree, table)
        if isinstance(left, Exception): return left
        rigth = self.exp_rigth.interpretar(tree, table)
        if isinstance(rigth, Exception): return rigth

        if self.operador == Operador_Relacional.MAYORQUE: # expresion > expresion
            # INT
            if self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.INT64:                          # INT > INT     = BOOL
                return self.casteo(self.exp_left.tipo, left) > self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                      # INT > FLOAT   = BOOL
                return self.casteo(self.exp_left.tipo, left) > self.casteo(self.exp_rigth.tipo, rigth)
            # DOUBLE
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.INT64:                      # FLOAT > INT   = BOOL
                return self.casteo(self.exp_left.tipo, left) > self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                    # FLOAT > FLOAT = BOOL
                return self.casteo(self.exp_left.tipo, left) > self.casteo(self.exp_rigth.tipo, rigth)
            # STRING
            elif self.exp_left.tipo == Tipo.STRING and self.exp_rigth.tipo == Tipo.STRING:                      # STRIN > STRIN = BOOL
                return self.casteo(self.exp_left.tipo, left) > self.casteo(self.exp_rigth.tipo, rigth)
            # CHAR
            elif self.exp_left.tipo == Tipo.CHAR and self.exp_rigth.tipo == Tipo.CHAR:                          # CHAR > CHAR   = BOOL
                return self.casteo(self.exp_left.tipo, left) > self.casteo(self.exp_rigth.tipo, rigth)
            # BOOLEANO PENDIENTE
            elif self.exp_left.tipo == Tipo.BOOLEANO and self.exp_rigth.tipo == Tipo.BOOLEANO:           # BOOL > BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) > self.casteo(self.exp_rigth.tipo, rigth)
            return Exception("Semantico", "Tipo Erroneo de operacion para >.", self.fila, self.columna)

        elif self.operador == Operador_Relacional.MENORQUE: # expresion > expresion
            # INT
            if self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.INT64:                          # INT < INT     = BOOL
                return self.casteo(self.exp_left.tipo, left) < self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                      # INT < FLOAT   = BOOL
                return self.casteo(self.exp_left.tipo, left) < self.casteo(self.exp_rigth.tipo, rigth)
            # DOUBLE
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.INT64:                      # FLOAT < INT   = BOOL
                return self.casteo(self.exp_left.tipo, left) < self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                    # FLOAT < FLOAT = BOOL
                return self.casteo(self.exp_left.tipo, left) < self.casteo(self.exp_rigth.tipo, rigth)
            # STRING
            elif self.exp_left.tipo == Tipo.STRING and self.exp_rigth.tipo == Tipo.STRING:                      # STRIN < STRIN = BOOL
                return self.casteo(self.exp_left.tipo, left) < self.casteo(self.exp_rigth.tipo, rigth)
            # CHAR
            elif self.exp_left.tipo == Tipo.CHAR and self.exp_rigth.tipo == Tipo.CHAR:                          # CHAR < CHAR   = BOOL
                return self.casteo(self.exp_left.tipo, left) < self.casteo(self.exp_rigth.tipo, rigth)
            # BOOLEANO PENDIENTE
            elif self.exp_left.tipo == Tipo.BOOLEANO and self.exp_rigth.tipo == Tipo.BOOLEANO:           # BOOL > BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) < self.casteo(self.exp_rigth.tipo, rigth)
            return Exception("Semantico", "Tipo Erroneo de operacion para <.", self.fila, self.columna)
        
        elif self.operador == Operador_Relacional.MAYORIGUAL: # expresion > expresion
            # INT
            if self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.INT64:                          # INT >= INT     = BOOL
                return self.casteo(self.exp_left.tipo, left) >= self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                      # INT >= FLOAT   = BOOL
                return self.casteo(self.exp_left.tipo, left) >= self.casteo(self.exp_rigth.tipo, rigth)
            # DOUBLE
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.INT64:                      # FLOAT >= INT   = BOOL
                return self.casteo(self.exp_left.tipo, left) >= self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                    # FLOAT >= FLOAT = BOOL
                return self.casteo(self.exp_left.tipo, left) >= self.casteo(self.exp_rigth.tipo, rigth)
            # STRING
            elif self.exp_left.tipo == Tipo.STRING and self.exp_rigth.tipo == Tipo.STRING:                      # STRIN >= STRIN = BOOL
                return self.casteo(self.exp_left.tipo, left) >= self.casteo(self.exp_rigth.tipo, rigth)
            # CHAR
            elif self.exp_left.tipo == Tipo.CHAR and self.exp_rigth.tipo == Tipo.CHAR:                          # CHAR >= CHAR   = BOOL
                return self.casteo(self.exp_left.tipo, left) >= self.casteo(self.exp_rigth.tipo, rigth)
            # BOOLEANO PENDIENTE
            elif self.exp_left.tipo == Tipo.BOOLEANO and self.exp_rigth.tipo == Tipo.BOOLEANO:           # BOOL >= BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) >= self.casteo(self.exp_rigth.tipo, rigth)
            return Exception("Semantico", "Tipo Erroneo de operacion para >=.", self.fila, self.columna)
        
        elif self.operador == Operador_Relacional.MENORIGUAL: # expresion > expresion
            # INT
            if self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.INT64:                          # INT <= INT     = BOOL
                return self.casteo(self.exp_left.tipo, left) <= self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                      # INT <= FLOAT   = BOOL
                return self.casteo(self.exp_left.tipo, left) <= self.casteo(self.exp_rigth.tipo, rigth)
            # DOUBLE
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.INT64:                      # FLOAT <= INT   = BOOL
                return self.casteo(self.exp_left.tipo, left) <= self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                    # FLOAT <= FLOAT = BOOL
                return self.casteo(self.exp_left.tipo, left) <= self.casteo(self.exp_rigth.tipo, rigth)
            # STRING
            elif self.exp_left.tipo == Tipo.STRING and self.exp_rigth.tipo == Tipo.STRING:                      # STRIN <= STRIN = BOOL
                return self.casteo(self.exp_left.tipo, left) <= self.casteo(self.exp_rigth.tipo, rigth)
            # CHAR
            elif self.exp_left.tipo == Tipo.CHAR and self.exp_rigth.tipo == Tipo.CHAR:                          # CHAR <= CHAR   = BOOL
                return self.casteo(self.exp_left.tipo, left) <= self.casteo(self.exp_rigth.tipo, rigth)
            # BOOLEANO PENDIENTE
            elif self.exp_left.tipo == Tipo.BOOLEANO and self.exp_rigth.tipo == Tipo.BOOLEANO:           # BOOL <= BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) <= self.casteo(self.exp_rigth.tipo, rigth)
            return Exception("Semantico", "Tipo Erroneo de operacion para <=.", self.fila, self.columna)

        elif self.operador == Operador_Relacional.IGUALACION: # expresion > expresion
            # INT
            if self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.INT64:                          # INT == INT     = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                      # INT == FLOAT   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.NULO:                      # INT == FLOAT   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            # DOUBLE
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.INT64:                      # FLOAT == INT   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                    # FLOAT == FLOAT = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.NULO:                    # FLOAT == FLOAT = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            # STRING
            elif self.exp_left.tipo == Tipo.STRING and self.exp_rigth.tipo == Tipo.STRING:                      # STRIN == STRIN = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.STRING and self.exp_rigth.tipo == Tipo.NULO:                      # STRIN == STRIN = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            # PENDIENTE STRING CON INT Y FLOAT.
            # elif self.exp_left.tipo == Tipo.STRING and self.exp_rigth.tipo == Tipo.INT64:                       # STRIN == INT = BOOL
            #     return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            # elif self.exp_left.tipo == Tipo.STRING and self.exp_rigth.tipo == Tipo.FLOAT64:                     # STRIN == FLOAT = BOOL
            #     return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)        
            # CHAR
            elif self.exp_left.tipo == Tipo.CHAR and self.exp_rigth.tipo == Tipo.CHAR:                          # CHAR == CHAR   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.CHAR and self.exp_rigth.tipo == Tipo.NULO:                          # CHAR == CHAR   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            # BOOLEANO PENDIENTE
            elif self.exp_left.tipo == Tipo.BOOLEANO and self.exp_rigth.tipo == Tipo.BOOLEANO:                  # BOOL == BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.BOOLEANO and self.exp_rigth.tipo == Tipo.NULO:                  # BOOL == BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            #   NULO
            elif self.exp_left.tipo == Tipo.NULO and self.exp_rigth.tipo == Tipo.NULO:                          # BOOL == BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.NULO and self.exp_rigth.tipo == Tipo.INT64:                          # BOOL == BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.NULO and self.exp_rigth.tipo == Tipo.FLOAT64:                          # BOOL == BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.NULO and self.exp_rigth.tipo == Tipo.STRING:                          # BOOL == BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.NULO and self.exp_rigth.tipo == Tipo.CHAR:                          # BOOL == BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.NULO and self.exp_rigth.tipo == Tipo.BOOLEANO:                          # BOOL == BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) == self.casteo(self.exp_rigth.tipo, rigth)
            
            return Exception("Semantico", "Tipo Erroneo de operacion para ==.", self.fila, self.columna)

        elif self.operador == Operador_Relacional.DIFERENCIA: # expresion > expresion
            # INT
            if self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.INT64:                          # INT != INT     = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                      # INT != FLOAT   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.INT64 and self.exp_rigth.tipo == Tipo.NULO:                      # INT != FLOAT   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            # DOUBLE
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.INT64:                      # FLOAT != INT   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.FLOAT64:                    # FLOAT != FLOAT = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.FLOAT64 and self.exp_rigth.tipo == Tipo.NULO:                    # FLOAT != FLOAT = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            # STRING
            elif self.exp_left.tipo == Tipo.STRING and self.exp_rigth.tipo == Tipo.STRING:                      # STRIN != STRIN = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.STRING and self.exp_rigth.tipo == Tipo.NULO:                      # STRIN != STRIN = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            # CHAR
            elif self.exp_left.tipo == Tipo.CHAR and self.exp_rigth.tipo == Tipo.CHAR:                          # CHAR != CHAR   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.CHAR and self.exp_rigth.tipo == Tipo.NULO:                          # CHAR != CHAR   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            # BOOLEANO PENDIENTE
            elif self.exp_left.tipo == Tipo.BOOLEANO and self.exp_rigth.tipo == Tipo.BOOLEANO:           # BOOL != BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.BOOLEANO and self.exp_rigth.tipo == Tipo.NULO:           # BOOL != BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            # NULO
            elif self.exp_left.tipo == Tipo.NULO and self.exp_rigth.tipo == Tipo.NULO:           # BOOL != BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.NULO and self.exp_rigth.tipo == Tipo.INT64:           # BOOL != BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.NULO and self.exp_rigth.tipo == Tipo.FLOAT64:           # BOOL != BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.NULO and self.exp_rigth.tipo == Tipo.STRING:           # BOOL != BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.NULO and self.exp_rigth.tipo == Tipo.CHAR:           # BOOL != BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            elif self.exp_left.tipo == Tipo.NULO and self.exp_rigth.tipo == Tipo.BOOLEANO:           # BOOL != BOOL   = BOOL
                return self.casteo(self.exp_left.tipo, left) != self.casteo(self.exp_rigth.tipo, rigth)
            
            
            return Exception("Semantico", "Tipo Erroneo de operacion para !=.", self.fila, self.columna)   

        return Exception("Semantico", "Tipo de Operacion no Especificado.", self.fila, self.columna)

    def AST(self):
        pass

    def casteo(self,tipo, valor):
        if tipo == Tipo.INT64:
            return int(valor)
        elif tipo == Tipo.FLOAT64:
            return float(valor)
        elif tipo == Tipo.BOOLEANO:
            return bool(valor)
        return str(valor)
        