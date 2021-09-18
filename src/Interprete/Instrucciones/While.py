from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.Instrucciones.Continue import Continue
from src.Interprete.Instrucciones.Return import Return
from src.Interprete.Instrucciones.Break import Break
from src.Interprete.TS.TablaSimbolo import TablaSimbolo
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Tipo import Tipo

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