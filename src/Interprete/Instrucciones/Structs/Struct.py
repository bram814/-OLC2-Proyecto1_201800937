from src.Interprete.Abstract.Instruccion import Instruccion

class Struct(Instruccion):

    def __init__(self, id, atributos, fila, columna):
        self.id = id
        self.atributos = atributos
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        table.addStruct(self.id, self.atributos, self.fila, self.columna)

    def AST(self):
        pass