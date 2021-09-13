from Interprete.Abstract.Instruccion import Instruccion
from Interprete.Instrucciones.Continue import Continue
from Interprete.Instrucciones.Return import Return
from Interprete.Instrucciones.Break import Break
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo

class While(Instruccion):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        while True:
            condicion = self.condicion.interpretar(tree, table)
            if isinstance(condicion, Exception): return condicion
            
            if self.condicion.tipo == Tipo.BOOLEANO:
                if bool(condicion) == True:

                    nuevaTabla = TablaSimbolo(table)
                    for instruccion in self.instrucciones: 
                        result = instruccion.interpretar(tree, nuevaTabla) 
                        if isinstance(result, Exception):
                            tree.get_excepcion().append(result)
                            tree.update_consola(result.__str__())
                        if isinstance(result, Break): return None
                        if isinstance(result, Return): return result
                        if isinstance(result, Continue): break
                else:
                    break
            else:
                return Exception("Semantico", "Tipo de Dato no Booleano en While.", self.fila, self.columna)

    def AST(self):
        pass