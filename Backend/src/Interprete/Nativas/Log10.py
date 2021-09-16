from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.Instrucciones.Funcion import Funcion
from math import log # log(valor, base)

class Log10(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("Log10##Native5")
        if simbolo == None : return Exception("Semantico", "No se encontró el parámetro de Log10", self.fila, self.columna)

        if simbolo.get_tipo() != Tipo.INT64 and simbolo.get_tipo() != Tipo.FLOAT64:
            return Exception("Semantico", "Tipo de parametro de Log no es un Valor.", self.fila, self.columna)


        simbolo.set_tipo(Tipo.FLOAT64)
        self.tipo = simbolo.get_tipo()
        return float(log(simbolo.get_valor(),10))
