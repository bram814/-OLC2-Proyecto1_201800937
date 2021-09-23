from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.TS.Simbolo import Simbolo

class DeclaracionStruct(Instruccion):

    def __init__(self, id, tipo, atributos, fila, columna):
        self.id = id
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        self.atributos = atributos
    
    # def execute(self, environment):
    #     struct = environment.getStruct(self.type)
    #     if struct == None:
    #         print("No existe el type")
    #         return
    #     attrs = {}
    #     for att in struct:
    #         attrs.update({
    #             att: 0
    #         });
    #     environment.saveVarStruct(self.id, attrs, self.type)

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.id)
        struct = table.getStruct(self.id)

        temp_atributo = {}
        for atributo in struct:
            print(atributo)

        # if simbolo == None: # Si no Existe lo declara, lo agrega a la tabla de simbolo.
        #     simbolo = Simbolo(str(self.identificador), self.expresion.tipo, self.fila, self.columna, None)
        #     result = table.setTabla(simbolo)
        # else: # Si ya Existe el simbolo, lo actualiza en la tabla de simbolos.
        #     simbolo = Simbolo(str(self.identificador), self.expresion.tipo, self.fila, self.columna, None)
        #     result = table.actualizarTabla(simbolo)

        # if isinstance(result, Exception): return result
        # print(simbolo.atributos)
