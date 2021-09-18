from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Simbolo import Simbolo

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

        simbolo = table.getTabla(self.identificador)
        if simbolo == None:
            simbolo = Simbolo(str(self.identificador), self.tipo, self.fila, self.columna, value)
            result = table.setTabla(simbolo)
            if isinstance(result, Exception): return result
        else: # Si ya Existe el simbolo, lo actualiza en la tabla de simbolos.
            simbolo = Simbolo(str(self.identificador), self.expresion.tipo, self.fila, self.columna, value)
            result = table.actualizarTabla(simbolo)


        return None
    
    def AST(self):
        pass