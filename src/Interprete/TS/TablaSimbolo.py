'''
    AMBITOEs un entorno, es la parte del codigo donde pueden acceder las variables.
    AMBITO -> Determina en qué partes del programa una entidad puede ser usada.

    En la tabla de simbolos nos facilita usar un diccionario para poder ir encontrando las datos.

'''

from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Tipo import *

class TablaSimbolo:
    def __init__(self, anterior = None):
        self.tabla = {} # Diccionario Vacio
        self.anterior = anterior
        self.funciones = []

    def setTabla(self, simbolo):      # Agregar una variable
        if simbolo.id in self.tabla :
            return Exception("Semantico", "Variable " + simbolo.id + " ya existe", simbolo.fila, simbolo.columna)
        else:
            self.tabla[simbolo.id] = simbolo
            return None

    def getTabla(self, id):            # obtener una variable
        tablaActual = self
        while tablaActual.tabla != None:
            if id in tablaActual.tabla :
                return tablaActual.tabla[id]
            else:
                tablaActual = tablaActual.anterior
                if tablaActual is None:
                    return None
        return None
        
    #local sin while
    def getLocal(self, id):
        tablaActual = self
        if id in tablaActual.tabla :
            return tablaActual.tabla[id]
        else:
            tablaActual = tablaActual.anterior
            if tablaActual is None:
                return None

    def actualizarTabla(self, simbolo):
        tablaActual = self
        
        while tablaActual != None:
            if simbolo.id in tablaActual.tabla :
                if tablaActual.tabla[simbolo.id].get_tipo() == simbolo.get_tipo() or tablaActual.tabla[simbolo.id].get_tipo() != simbolo.get_tipo() :
                    tablaActual.tabla[simbolo.id].set_valor(simbolo.get_valor())
                    tablaActual.tabla[simbolo.id].set_tipo(simbolo.get_tipo())
                    return None
                return Exception("Semantico", "Tipo de dato Diferente en Asignacion", simbolo.get_fila(), simbolo.get_columna()) 
            else:
                tablaActual = tablaActual.anterior
                if tablaActual is None:
                    return None
        return Exception("Semantico", "Variable No encontrada en Asignacion", simbolo.get_fila(), simbolo.get_columna())
        
        
    
