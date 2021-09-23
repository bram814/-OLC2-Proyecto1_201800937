from src.Interprete.Expresion.Identificador import Identificador
from src.Interprete.Abstract.Node_Ast import Node_Ast
from src.Interprete.Expresion.Primitivo import Primitivo
from src.Interprete.Abstract.Instruccion import Instruccion
from src.Interprete.TS.Exception import Exception
from src.Interprete.TS.TablaSimbolo import TablaSimbolo
from src.Interprete.Instrucciones.Break import Break
from src.Interprete.TS.Simbolo import Simbolo
from src.Interprete.Instrucciones.Funcion import Funcion
from src.Interprete.TS.Tipo import Tipo

class Llamada(Instruccion):

    def __init__(self, nombre, parametros, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table):
        result = tree.getFuncion(self.nombre)
        struct = table.getStruct(self.nombre)
        if result == None and struct == None:
            return Exception("Semantico", "No existe una funcion con ese nombre: " + self.nombre, self.fila, self.columna)
        
        if result != None and struct == None:
        
            if table.getLocal(self.nombre)==1:
                ambit = "Global"    
            else:
                ambit = "Local"  
            dic = {"id":str(self.nombre), "tipo":"function", "ambito":ambit, "fila":self.fila, "columna":self.columna}
            tree.Table.append(dic)

            nuevaTabla = TablaSimbolo(tree.get_tabla_ts_global()) # Nuevo ambito.
            if len(result.parametros) == len(self.parametros): # Verifica que los parametros sean los mismo, si no lanza una Exception.
                contador=0
                for expresion in self.parametros: # SE OBTIENE EL VALOR DEL PARAMETRO EN LA LLAMADA
                    result_expression = expresion.interpretar(tree, table)
                    
                    if isinstance(expresion, Primitivo):
                        dic = {"id":result.parametros[contador]['identificador'], "tipo":f"{expresion.tipo} - Parametro", "ambito":"Local", "fila":expresion.fila, "columna":expresion.columna}
                    elif isinstance(expresion, Identificador):
                        dic = {"id":result.parametros[contador]['identificador'], "tipo":f"{expresion.tipo} - Parametro", "ambito":"Local", "fila":expresion.fila, "columna":expresion.columna}
                    else:
                        try:
                            dic = {"id":result.parametros[contador]['identificador'], "tipo":f"{expresion.tipo} - Parametro", "ambito":"Local", "fila":expresion.fila, "columna":expresion.columna}
                        except:
                            dic = {"id":result.parametros[contador]['identificador'], "tipo":f"{expresion.tipo} - Parametro", "ambito":"Local", "fila":expresion.fila, "columna":expresion.columna}
                    tree.Table.append(dic)
                

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
        
        elif struct != None and result == None:
            nuevaTabla = TablaSimbolo(table) # Nuevo ambito.
            
            if len(struct) == len(self.parametros): # Verifica que los parametros sean los mismo, si no lanza una Exception.
                contador=0
                attr = {}
                for expresion in self.parametros: # SE OBTIENE EL VALOR DEL PARAMETRO EN LA LLAMADA
                    result_expression = expresion.interpretar(tree, table)  

                    if struct[contador]['tipoDato'] == None:
                        pass
                        # struct[contador]['tipoDato'] = expresion.tipo
                    elif struct[contador]['tipoDato'] != None and (struct[contador]['tipoDato'] != expresion.tipo):
                        return Exception("Semantico", "Tipo de dato Diferente de Struct.", self.fila, self.columna)
                    attr.update({'tipoDato':expresion.tipo, 'identificador':struct[contador]['identificador'], struct[contador]['identificador']:result_expression })        
                    # struct[contador][struct[contador]['identificador']] = result_expression
                
                    if isinstance(result_expression, Exception): return result_expression
                  
                    contador += 1

                simbolo = Simbolo(self.nombre, None, self.fila, self.columna, attr)
                simbolo.atributos = attr
                resultTabla = nuevaTabla.setTabla(simbolo)
                if isinstance(resultTabla, Exception): return resultTabla
                self.tipo = Tipo.STRUCT
                return simbolo
            else:
                return Exception("Semantico", "Cantidad de Parametros incorrecta.", self.fila, self.columna)
        
        else:
            return Exception("Semantico", f"Nombre de Struct y Funcion repetido. {self.nombre}", self.fila, self.columna)
        
        return value


    def AST(self):
        nodo = Node_Ast("LLAMADA A FUNCION")
        nodo.crearHoja(str(self.nombre))
        nodo.crearHoja("(")
        parametros = Node_Ast("PARAMETROS")
        for param in self.parametros:
            parametros.crearNodo(param.AST())
        nodo.crearNodo(parametros)
        nodo.crearHoja(")")
        return nodo