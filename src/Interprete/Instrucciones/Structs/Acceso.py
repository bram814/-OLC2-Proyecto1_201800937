from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.TS.Exception import Exception

class Acceso(Instruccion):

    def __init__(self, id, atributo, fila, columna):
        self.id = id
        self.tipo = None
        self.fila = fila
        self.columna = columna
        self.atributo = atributo
    

    def interpretar(self, tree, table):

        simbolo = table.getTabla(self.id)
        struct =  table.getStruct(self.id)
        self.tipo = simbolo.tipo
        if simbolo != None:
            if simbolo.valor != None:
                if simbolo.valor.atributos != None:
                    for i in simbolo.valor.atributos:
                        if i == self.atributo:
                            return simbolo.valor.atributos[i]

    def AST(self):
        pass