from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.Abstract.Node_Ast import Node_Ast
from src.Interprete.Instrucciones.Continue import Continue
from src.Interprete.Instrucciones.Return import Return
from src.Interprete.Instrucciones.Break import Break
from src.Interprete.TS.TablaSimbolo import TablaSimbolo
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Simbolo import Simbolo
from src.Interprete.TS.Tipo import Tipo

class For(Instruccion):
    def __init__(self, variable, cond1, cond2, instrucciones,  fila, columna):
        self.variable = variable
        self.cond1 = cond1
        self.cond2 = cond2
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        
        new_table = TablaSimbolo(table) 
        left = self.cond1.interpretar(tree, new_table)
        if isinstance(left, Exception): return left
        if self.cond2 != None:
            right = self.cond2.interpretar(tree, new_table)
            if isinstance(right, Exception): return right

        if self.cond1.tipo == Tipo.INT64 and self.cond2.tipo == Tipo.INT64:

            simbolo = new_table.getTabla(self.variable)
            if simbolo == None: # Si no Existe lo declara, lo agrega a la tabla de simbolo.
                simbolo = Simbolo(str(self.variable), self.cond1.tipo, self.fila, self.columna, left)
                result = new_table.setTabla(simbolo)

            temp = left;
            while(left <= right):

                new_ambit = TablaSimbolo(new_table) # Inicia el segundo ambito.
                simbolo = Simbolo(str(self.variable), self.cond1.tipo, self.fila, self.columna, left)
                result = new_table.actualizarTabla(simbolo)
                for instruccion in self.instrucciones:       # Inicia ejecutando las instrucciones adentro del For.
                    result = instruccion.interpretar(tree, new_ambit) 
                    if isinstance(result, Exception) :
                        tree.get_excepcion().append(result)
                        tree.update_consola(result.__str__())
                    if isinstance(result, Break): return None
                    if isinstance(result, Return): return result
                    if isinstance(result, Continue): break

                left+=1
                if(left>right): break
            
            simbolo = Simbolo(str(self.variable), self.cond1.tipo, self.fila, self.columna, temp)
            result = new_table.actualizarTabla(simbolo)

        elif self.cond1.tipo == Tipo.STRING and self.cond2 == None:

            simbolo = new_table.getTabla(self.variable)
            if simbolo == None: # Si no Existe lo declara, lo agrega a la tabla de simbolo.
                simbolo = Simbolo(str(self.variable), self.cond1.tipo, self.fila, self.columna, left)
                result = new_table.setTabla(simbolo)
            
            temp = left;
            i = 0;
            while(i < len(left)):

                new_ambit = TablaSimbolo(new_table) # Inicia el segundo ambito.
                simbolo = Simbolo(str(self.variable), self.cond1.tipo, self.fila, self.columna, left[i])
                result = new_table.actualizarTabla(simbolo)
                for instruccion in self.instrucciones:       # Inicia ejecutando las instrucciones adentro del For.
                    result = instruccion.interpretar(tree, new_ambit) 
                    if isinstance(result, Exception) :
                        tree.get_excepcion().append(result)
                        tree.update_consola(result.__str__())
                    if isinstance(result, Break): return None
                    if isinstance(result, Return): return result
                    if isinstance(result, Continue): break

                i += 1
            
            simbolo = Simbolo(str(self.variable), self.cond1.tipo, self.fila, self.columna, temp)
            result = new_table.actualizarTabla(simbolo)
        else:
            return Exception("Semantico", "Error de tipo rango, string o array.", self.fila, self.columna)
        
        
    def AST(self):
        nodo = Node_Ast("FOR")
        nodo.crearHoja("for")
        nodo.crearHoja(str(self.variable))
        nodo.crearHoja("in")
        nodo.crearNodo(self.cond1.AST())
        if self.cond2 != None:
            nodo.crearHoja(":")
            nodo.crearNodo(self.cond2.AST())
        instrucciones = Node_Ast("INSTRUCCIONES")
        for instruccion in self.instrucciones:
            instrucciones.crearNodo(instruccion.AST())
        nodo.crearNodo(instrucciones)
        nodo.crearHoja("end")
        nodo.crearHoja(";")
        
        return nodo