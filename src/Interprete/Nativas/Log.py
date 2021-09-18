from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Tipo import Tipo
from src.Interprete.Instrucciones.Funcion import Funcion
from math import log # log(valor, base)

class Log(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        
        simbolo_base = table.getTabla("Log##Native6")
        simbolo_valor = table.getTabla("Log##Native7")
        if simbolo_base == None or simbolo_valor == None : return Exception("Semantico", "No se encontró el parámetro de Log", self.fila, self.columna)

        if simbolo_base.get_tipo() != Tipo.INT64 and simbolo_base.get_tipo() != Tipo.FLOAT64 and simbolo_valor.get_tipo() != Tipo.INT64 and simbolo_valor.get_tipo() != Tipo.FLOAT64:
            return Exception("Semantico", "Tipo de parametro de Log no es un Valor.", self.fila, self.columna)

        simbolo_base.set_tipo(Tipo.FLOAT64)
        simbolo_valor.set_tipo(Tipo.FLOAT64)
        self.tipo = simbolo_base.get_tipo()
        return float(log(simbolo_valor.get_valor(),simbolo_base.get_valor()))
