from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.TablaSimbolo import TablaSimbolo
from src.Interprete.Instrucciones.Break import Break
from src.Interprete.TS.Simbolo import Simbolo
from src.Interprete.Instrucciones.Funcion import Funcion

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
                
                elif result.parametros[contador]["identificador"] == "TypeOf##Native3":
                    result.parametros[contador]['tipoDato'] = expresion.tipo
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), expresion.tipo, self.fila, self.columna, result_expression)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla
                
                elif result.parametros[contador]["identificador"] == "Log10##Native5":
                    result.parametros[contador]['tipoDato'] = expresion.tipo
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), expresion.tipo, self.fila, self.columna, result_expression)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla

        
                elif result.parametros[contador]["identificador"] == "Log##Native6" or result.parametros[contador]["identificador"] == "Log##Native7":
                    result.parametros[contador]['tipoDato'] = expresion.tipo
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), expresion.tipo, self.fila, self.columna, result_expression)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla

                elif result.parametros[contador]["identificador"] == "Trunc##Native8":
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), result.parametros[contador]['tipoDato'], self.fila, self.columna, result_expression)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla

                elif result.parametros[contador]["identificador"] == "Sin##Native9":
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), result.parametros[contador]['tipoDato'], self.fila, self.columna, result_expression)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla

                elif result.parametros[contador]["identificador"] == "Cos##Native10":
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), result.parametros[contador]['tipoDato'], self.fila, self.columna, result_expression)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla

                elif result.parametros[contador]["identificador"] == "Tan##Native11":
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), result.parametros[contador]['tipoDato'], self.fila, self.columna, result_expression)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla

                elif result.parametros[contador]["identificador"] == "Sqrt##Native12":
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), result.parametros[contador]['tipoDato'], self.fila, self.columna, result_expression)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla
                
                elif result.parametros[contador]["identificador"] == "String##Native13":
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), result.parametros[contador]['tipoDato'], self.fila, self.columna, result_expression)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla
                
                elif result.parametros[contador]["identificador"] == "Parse##Native14" or result.parametros[contador]["identificador"] == "Parse##Native15":
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), result.parametros[contador]['tipoDato'], self.fila, self.columna, result_expression)
                    resultTabla = nuevaTabla.setTabla(simbolo)
                    if isinstance(resultTabla, Exception): return resultTabla

                elif result.parametros[contador]["identificador"] == "Float##Native16":
                    result.parametros[contador]['tipoDato'] = expresion.tipo
                    simbolo = Simbolo(str(result.parametros[contador]['identificador']), expresion.tipo, self.fila, self.columna, result_expression)
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