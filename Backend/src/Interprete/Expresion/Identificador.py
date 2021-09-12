from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception

class Identificador(Instruccion):
    
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna
        self.tipo = None

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.identificador.lower())
        if simbolo == None:
            return Exception("Semantico", "Variable " + self.identificador + " no encontrada.", self.fila, self.columna)

        self.tipo = simbolo.get_tipo()
        if simbolo.get_valor() == None:
            return Exception("Semantico", "Variable " + self.identificador + " vacia.", self.fila, self.columna)
        
        return simbolo.get_valor()


    def AST(self):
        pass