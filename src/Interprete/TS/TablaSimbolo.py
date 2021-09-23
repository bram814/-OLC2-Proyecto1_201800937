'''
    AMBITOEs un entorno, es la parte del codigo donde pueden acceder las variables.
    AMBITO -> Determina en qué partes del programa una entidad puede ser usada.

    En la tabla de simbolos nos facilita usar un diccionario para poder ir encontrando las datos.

    ATRIBUTO keys() --> {id:"varaibleId", tipo:"tipoId"} obtiene la posicion id, tipo, etc..
'''

from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Tipo import *

class TablaSimbolo:
    def __init__(self, anterior = None):
        self.tabla = {} # Diccionario Vacio
        self.anterior = anterior
        self.funciones = []
        self.struct = {}

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
        cont = 1
        tablaActual = self
        while tablaActual.tabla != None:
            if id in tablaActual.tabla :
                return cont
            else:
                tablaActual = tablaActual.anterior
                if tablaActual is None:
                    return 1
                cont += 1
        return 1

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
        
    def addStruct(self, id, atributos, fila, columna):
        if id in self.struct.keys():
            Exception("Semantico", "Variable repetida en Struc.", fila, columna)
        else:
            self.struct[id] = atributos

    def getStruct(self, id):
        tablaActual = self
        while tablaActual.struct != None:
            if id in tablaActual.struct.keys():
                return tablaActual.struct[id]
            else:
                tablaActual = tablaActual.anterior
                if tablaActual is None:
                    return None
        return None

    # def actualizarStruct(self, idVar, attrs, type):
    #     env = self
    #     newSymbol = Symbol(None, idVar, Type.STRUCT, type)
    #     newSymbol.attributes = attrs
    #     while env != None:
    #         if idVar in env.variables.keys():
    #             env.variables[idVar] = newSymbol
    #             return
    #         env = env.prev
    #     self.variables[idVar] = newSymbol

    #     tablaActual = self
    #     simbolo = Simbolo()