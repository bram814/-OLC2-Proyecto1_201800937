from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.TS.Tipo import Tipo
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.TablaSimbolo import TablaSimbolo
from src.Interprete.Instrucciones.Break import Break
from src.Interprete.Instrucciones.Return import Return
from src.Interprete.Instrucciones.Continue import Continue

class Funcion(Instruccion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        new_table = TablaSimbolo(table) 

        for instruccion in self.instrucciones:     
            value = instruccion.interpretar(tree, new_table)
            if isinstance(value, Exception):
                tree.get_excepcion().append(value)
                tree.update_consola(value.__str__())
            if isinstance(value, Break): 
                err = Exception("Semantico", "Break fuera de Bucle", instruccion.fila, instruccion.columna)
                tree.get_excepcion().append(err)
                tree.update_consola(err.__str__())
            if isinstance(value, Continue): 
                err = Exception("Semantico", "Continue fuera de Bucle", instruccion.fila, instruccion.columna)
                tree.get_excepcion().append(err)
                tree.update_consola(err.__str__())
            if isinstance(value, Return): # Retorna el resultado
                self.tipo = value.tipo
                return value.result

        return None

    def AST(self):
        pass