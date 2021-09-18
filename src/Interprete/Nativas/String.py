from src.Interprete.Instrucciones.Funcion import Funcion
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Tipo import Tipo

class String(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("String##Native13")
        if simbolo == None : return Exception("Semantico", "No se encontró el parámetro de String.", self.fila, self.columna)

        if simbolo.get_tipo() == Tipo.NULO:
            return Exception("Semantico", "Tipo de parametro de String no se puede convertir a Nulo.", self.fila, self.columna)
        simbolo.set_tipo(Tipo.STRING)
        self.tipo = simbolo.get_tipo()
        return str(simbolo.get_valor())