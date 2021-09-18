from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Tipo import Tipo
from src.Interprete.Instrucciones.Funcion import Funcion

class UpperCase(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre.lower()
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("UpperCase##Native1")
        if simbolo == None : return Exception("Semantico", "No se encontró el parámetro de UpperCase", self.fila, self.columna)

        if simbolo.get_tipo() != Tipo.STRING:
            return Exception("Semantico", "Tipo de parametro de ToUpper no es cadena.", self.fila, self.columna)

        self.tipo = simbolo.get_tipo()
        return simbolo.get_valor().upper()