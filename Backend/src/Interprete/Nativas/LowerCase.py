from Interprete.Instrucciones.Funcion import Funcion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo

class LowerCase(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        simbolo = table.getTabla("LowerCase##Native2")
        if simbolo == None : return Exception("Semantico", "No se encontró el parámetro de LowerCase.", self.fila, self.columna)

        if simbolo.get_tipo() != Tipo.STRING:
            return Exception("Semantico", "Tipo de parametro de uppercase no es Tipo String.", self.fila, self.columna)

        self.tipo = simbolo.get_tipo()
        return simbolo.get_valor().lower()