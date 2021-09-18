from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Tipo import Tipo
from src.Interprete.Instrucciones.Funcion import Funcion
from math import cos 

class Coseno(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        
        simbolo = table.getTabla("Cos##Native10")
        if simbolo == None: return Exception("Semantico", "No se encontró el parámetro de Coseno", self.fila, self.columna)

        if simbolo.get_tipo() != Tipo.INT64 and simbolo.get_tipo() != Tipo.FLOAT64:
            return Exception("Semantico", "Tipo de parametro de Coseno no es un Valor.", self.fila, self.columna)

        if isinstance(cos(simbolo.get_valor()), int): simbolo.set_tipo(Tipo.INT64)
        if isinstance(cos(simbolo.get_valor()), float): simbolo.set_tipo(Tipo.FLOAT64)
        self.tipo = simbolo.get_tipo()
        return cos(simbolo.get_valor())
