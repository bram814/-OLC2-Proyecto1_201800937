from Interprete.Instrucciones.Funcion import Funcion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo

class Float(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("Float##Native16")
        if simbolo == None: 
            return Exception("Semantico", "No se encontró el parámetro de Float.", self.fila, self.columna)
        
        if simbolo.get_tipo() != Tipo.FLOAT64 and simbolo.get_tipo() != Tipo.INT64:
            return Exception("Semantico", "Tipo de parámetro de Float incorrecto.", self.fila, self.columna)

        simbolo.set_tipo(Tipo.FLOAT64)
        self.tipo = simbolo.get_tipo()
        return float(simbolo.get_valor())