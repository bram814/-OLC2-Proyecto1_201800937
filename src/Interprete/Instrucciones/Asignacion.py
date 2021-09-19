from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.Simbolo import Simbolo


class Asignacion(Instruccion):

    def __init__(self, identificador, expresion, tipo, fila, columna):
        self.identificador = identificador
        self.expresion = expresion
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = self.expresion.interpretar(tree, table)
        if isinstance(value, Exception): return value

        if(self.tipo != None and self.tipo  != self.expresion.tipo): # Aca verifica si el tipo es el mismo.
            return Exception("Semantico", "Error de tipo, no se puede convertir de " + str(self.expresion.tipo) + " a " + str(self.tipo), self.fila, self.columna)
        self.tipo = self.expresion.tipo

        simbolo = table.getTabla(self.identificador) # Va a buscar el ID a la tabla de simbolo.
        if simbolo == None: # Si no Existe lo declara, lo agrega a la tabla de simbolo.
            simbolo = Simbolo(str(self.identificador), self.expresion.tipo, self.fila, self.columna, value)
            result = table.setTabla(simbolo)
        else: # Si ya Existe el simbolo, lo actualiza en la tabla de simbolos.
            simbolo = Simbolo(str(self.identificador), self.expresion.tipo, self.fila, self.columna, value)
            result = table.actualizarTabla(simbolo)
           
        if table.getLocal(str(self.identificador))==1:
            ambit = "Global"    
        else:
            ambit = "Local"
        dic = {"id":str(self.identificador), "tipo":self.expresion.tipo, "ambito":ambit, "fila":self.fila, "columna":self.columna}
        tree.Table.append(dic)
        if isinstance(result, Exception): return result
        return None

    
    def AST(self):
        pass