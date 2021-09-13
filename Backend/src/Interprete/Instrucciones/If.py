from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break
from Interprete.Instrucciones.Return import Return 
from Interprete.Instrucciones.Continue import Continue
from Interprete.TS.Tipo import Tipo

class If(Instruccion):

    def __init__(self, condicion, ins_if, ins_elseif, ins_else, fila, columna):
        self.condicion = condicion
        self.ins_if = ins_if
        self.ins_elseif = ins_elseif
        self.ins_else = ins_else
        self.fila = fila
        self.columna = columna
        self.flag = False;

    def interpretar(self, tree, table):
        cond = self.condicion.interpretar(tree, table)
        if isinstance(cond, Exception): return cond

        if self.condicion.tipo == Tipo.BOOLEANO:

            if bool(cond) == True:
                new_table = TablaSimbolo(table)
                for instruccion in self.ins_if:
                    result = instruccion.interpretar(tree, new_table)
                    if isinstance(result, Exception):
                        tree.get_excepcion().append(result)
                        tree.update_consola(result.__str__())
                    if isinstance(result, Break): return result
                    if isinstance(result, Return): return result
                    if isinstance(result, Continue): return result
            else:
                if self.ins_elseif != None:
                    new_table = TablaSimbolo(table)
                    for instruccion in self.ins_elseif:
                        result = instruccion.interpretar(tree, new_table)
                        if(self.flag == False):
                            self.flag = instruccion.condicion.interpretar(tree, new_table)
                        if isinstance(result, Exception):
                            tree.get_excepcion().append(result)
                            tree.update_consola(result.__str__()) 
                        if isinstance(result, Break): return result    
                        if isinstance(result, Return): return result
                        if isinstance(result, Continue): return result
                        if(self.flag == True): break

                if self.ins_else != None and self.flag != True:
                    new_table = TablaSimbolo(table)
                    for instruccion in self.ins_else:
                        result = instruccion.interpretar(tree, new_table)
                        if isinstance(result, Exception):
                            tree.get_excepcion().append(result)
                            tree.update_consola(result.__str__())       
                        if isinstance(result, Break): return result
                        if isinstance(result, Return): return result
                        if isinstance(result, Continue): return result

        else:
            return Exception("Semantico", "Tipo de Dato no Booleano en If.", self.fila, self.columna)

    def AST(self):
        pass

