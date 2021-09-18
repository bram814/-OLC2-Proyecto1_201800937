from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Tipo import Tipo
from src.Interprete.Instrucciones.Funcion import Funcion
from math import sqrt

class Sqrt(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        
        simbolo = table.getTabla("Sqrt##Native12")
        if simbolo == None: return Exception("Semantico", "No se encontró el parámetro de Tan", self.fila, self.columna)

        if simbolo.get_tipo() != Tipo.INT64 and simbolo.get_tipo() != Tipo.FLOAT64:
            return Exception("Semantico", "Tipo de parametro de Tan no es un Valor.", self.fila, self.columna)

        if isinstance(sqrt(simbolo.get_valor()), int): simbolo.set_tipo(Tipo.INT64)
        if isinstance(sqrt(simbolo.get_valor()), float): simbolo.set_tipo(Tipo.FLOAT64)
        self.tipo = simbolo.get_tipo()
        return sqrt(simbolo.get_valor())
