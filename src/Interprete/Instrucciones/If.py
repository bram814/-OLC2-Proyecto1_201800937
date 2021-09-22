from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.Abstract.Node_Ast import Node_Ast
from src.Interprete.TS.TablaSimbolo import TablaSimbolo
from src.Interprete.Instrucciones.Break import Break
from src.Interprete.Instrucciones.Return import Return 
from src.Interprete.Instrucciones.Continue import Continue
from src.Interprete.TS.Tipo import Tipo

class If(Instruccion):

    def __init__(self, condicion, ins_if, ins_else, ins_elseif, fila, columna):
        self.condicion = condicion
        self.ins_if = ins_if
        self.ins_elseif = ins_elseif
        self.ins_else = ins_else
        self.fila = fila
        self.columna = columna

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
                if self.ins_else != None:
                    new_table = TablaSimbolo(table)
                    for instruccion in self.ins_else:
                        result = instruccion.interpretar(tree, new_table)
                        if isinstance(result, Exception):
                            tree.get_excepcion().append(result)
                            tree.update_consola(result.__str__())       
                        if isinstance(result, Break): return result
                        if isinstance(result, Return): return result
                        if isinstance(result, Continue): return result

                elif self.ins_elseif != None:
                    result = self.ins_elseif.interpretar(tree, table)
                    if isinstance(result, Exception): return result
                    if isinstance(result, Break): return result    
                    if isinstance(result, Return): return result
                    if isinstance(result, Continue): return result
                        
                
        else:
            return Exception("Semantico", "Tipo de Dato no Booleano en If.", self.fila, self.columna)

    def AST(self):
        nodo = Node_Ast("IF")
        nodo.crearHoja("if")
        nodo.crearNodo(self.condicion.AST())
        instrucciones_if = Node_Ast("INSTRUCCIONES - IF")
        for instruccion_if in self.ins_if:
            instrucciones_if.crearNodo(instruccion_if.AST())
        nodo.crearNodo(instrucciones_if)

        if self.ins_else != None:
            instrucciones_else = Node_Ast("INSTRUCCIONES - ELSE")
            for instruccion_else in self.ins_else:
                instrucciones_else.crearNodo(instruccion_else.AST())
            nodo.crearNodo(instrucciones_else)

        elif self.ins_elseif != None:
            instrucciones_elseif = Node_Ast("INSTRUCCIONES - ELSEIF")
            instrucciones_elseif.crearNodo(self.ins_elseif.AST())
            nodo.crearNodo(instrucciones_elseif)

        return nodo
