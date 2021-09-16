from Interprete.Instrucciones.Funcion import Funcion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo

class Trunc(Funcion):
    
    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("Trunc##Native8")
        if simbolo == None : return Exception("Semantico", "No se encontró el parámetro de Truncate", self.fila, self.columna)

        if simbolo.get_tipo() != Tipo.INT64:
            return Exception("Semantico", "Tipo de parametro de Truncate no es un valor.", self.fila, self.columna)
       
        simbolo.set_tipo(Tipo.INT64)
        self.tipo = simbolo.get_tipo()
        return int(simbolo.get_valor())