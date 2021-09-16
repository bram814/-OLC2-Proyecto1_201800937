from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
from Interprete.Instrucciones.Funcion import Funcion
from math import sin 

class Seno(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        
        simbolo = table.getTabla("Sin##Native9")
        if simbolo == None: return Exception("Semantico", "No se encontró el parámetro de Seno", self.fila, self.columna)

        if simbolo.get_tipo() != Tipo.INT64 and simbolo.get_tipo() != Tipo.FLOAT64:
            return Exception("Semantico", "Tipo de parametro de Seno no es un Valor.", self.fila, self.columna)

        if isinstance(sin(simbolo.get_valor()), int): simbolo.set_tipo(Tipo.INT64)
        if isinstance(sin(simbolo.get_valor()), float): simbolo.set_tipo(Tipo.FLOAT64)
        self.tipo = simbolo.get_tipo()
        return sin(simbolo.get_valor())
