from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Simbolo import Simbolo

class Declaracion(Instruccion):

    def __init__(self, identificador, fila, columna, expresion=None):
        self.identificador = identificador
        self.tipo = None
        self.fila = fila
        self.columna = columna
        self.expresion = expresion

    def interpretar(self, tree, table):
        if self.expresion != None:
            value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
            if isinstance(value, Exception): return value
            self.tipo = self.expresion.tipo
        else:
            value = None

        simbolo = Simbolo(str(self.identificador).lower(), self.tipo, self.fila, self.columna, value)
        
        result = table.setTabla(simbolo)
        if isinstance(result, Exception): return result
        
        return None
    
    def AST(self):
        pass