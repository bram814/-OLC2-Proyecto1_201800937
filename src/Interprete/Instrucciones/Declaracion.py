from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.Abstract.Node_Ast import Node_Ast
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Simbolo import Simbolo

class Declaracion(Instruccion):

    def __init__(self, identificador, fila, columna, expresion=None):
        self.identificador = identificador
        self.tipo = None
        self.fila = fila
        self.columna = columna
        self.expresion = expresion

    def interpretar(self, tree, table):
        if self.expresion != None:
            value = self.expresion.interpretar(tree, table) # Valor a asignar a la variable
            if isinstance(value, Exception): return value
            self.tipo = self.expresion.tipo
        else:
            value = None

        simbolo = table.getTabla(self.identificador)
        if simbolo == None:
            simbolo = Simbolo(str(self.identificador), self.tipo, self.fila, self.columna, value)
            result = table.setTabla(simbolo)
            if isinstance(result, Exception): return result
        else: # Si ya Existe el simbolo, lo actualiza en la tabla de simbolos.
            simbolo = Simbolo(str(self.identificador), self.expresion.tipo, self.fila, self.columna, value)
            result = table.actualizarTabla(simbolo)
        
        if table.getLocal(str(self.identificador))==1:
            ambit = "Global"    
        else:
            ambit = "Local"
        dic = {"id":str(self.identificador), "tipo":self.expresion.tipo, "ambito":ambit, "fila":self.fila, "columna":self.columna}
        tree.Table.append(dic)

        return None
    
    def AST(self):
        nodo = Node_Ast("ASIGNACION")

        nodo.crearHoja(str(self.identificador))
        
        nodo.crearNodo(self.expresion.AST())
        nodo.crearHoja("::")
        nodo.crearHoja(str(self.expresion.tipo))

        return nodo