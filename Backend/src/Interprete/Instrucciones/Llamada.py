from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.TablaSimbolo import TablaSimbolo
from Interprete.Instrucciones.Break import Break
from Interprete.TS.Simbolo import Simbolo
from Interprete.Instrucciones.Funcion import Funcion

class Llamada(Instruccion):

    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table):
        result = tree.getFuncion(self.nombre)
        if result == None:
            return Exception("Semantico", "No existe una funcion con ese nombre: " + self.nombre, self.fila, self.columna)
        nuevaTabla = TablaSimbolo(tree.get_tabla_ts_global())
        
        if len(result.parametros) == len(self.parametros): # Verifica que los parametros sean los mismo, si no lanza una Exception.
            contador=0
            for expresion in self.parametros: # SE OBTIENE EL VALOR DEL PARAMETRO EN LA LLAMADA
                result_expression = expresion.interpretar(tree, table)
                if isinstance(result_expression, Exception): return result_expression
                
                if result.parametros[contador]["tipoDato"] == expresion.tipo:  
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), result.parametros[contador]['tipoDato'], self.fila, self.columna, result_expression)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla

                else:
                    return Exception("Semantico", "Tipo de dato diferente en Parametros de la llamada.", self.fila, self.columna)
                contador += 1

            
        else: 
            return Exception("Semantico", "Cantidad de Parametros incorrecta.", self.fila, self.columna)
    
        value = result.interpretar(tree, nuevaTabla)         # INTERPRETAR EL NODO FUNCION
        if isinstance(value, Exception): return value
        self.tipo = result.tipo
        
        return value


    def AST(self):
        pass