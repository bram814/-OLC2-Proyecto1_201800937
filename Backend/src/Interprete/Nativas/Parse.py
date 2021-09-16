from Interprete.Instrucciones.Funcion import Funcion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import Tipo
import re

class Parse(Funcion):

    def __init__(self, nombre, parametros, instrucciones, fila, columna):
        self.nombre = nombre
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO
    
    def interpretar(self, tree, table):
        simbolo_tipo = table.getTabla("Parse##Native14")
        simbolo_valor = table.getTabla("Parse##Native15")

        if simbolo_valor == None and simbolo_tipo == None: 
            return Exception("Semantico", "No se encontró el parámetro de Parse.", self.fila, self.columna)

        if simbolo_valor.get_tipo() != Tipo.STRING:
            return Exception("Semantico", "Tipo de parametro de Parse no es String.", self.fila, self.columna)

        # --------------------- INT ---------------------
        is_int = False
        tk_entero = r'\d+$' # Expresion para entero.
        if (re.match(tk_entero, simbolo_valor.get_valor()) is not None): # Verifica si el valor es un entero, si lo es devuelve true.
            is_int = True # Si la variable bool es True, quiere decir que es Int...
        
        # --------------------- FLOAT ---------------------
        is_double = False
        tk_double = r'\d+\.\d+' 
        if re.match(tk_double, simbolo_valor.get_valor()) is not None: # Verifica si el valor es un decimal, si lo es devuelve true.
            is_double = True # Si la variable bool es True, quiere decir que es Float...

        if is_double == True and is_int == False: # Validadcion para cuando sea Float...
            simbolo_valor.set_tipo(Tipo.FLOAT64)
        
        if is_int == True and is_double == False: # Validadcion para cuando sea Int...
            simbolo_valor.set_tipo(Tipo.INT64)
        
        if simbolo_valor.get_tipo() == Tipo.STRING: 
            return Exception("Semantico", "Tipo de parametro de Parse no se puede convertir.", self.fila, self.columna)

        if simbolo_tipo.get_valor() == "Float64":
            simbolo_valor.set_tipo(Tipo.FLOAT64)
            self.tipo = simbolo_valor.get_tipo()
            return float(simbolo_valor.get_valor())

        elif simbolo_tipo.get_valor() == "Int64":
            self.tipo = simbolo_valor.get_tipo()
            if simbolo_valor.get_tipo() == Tipo.FLOAT64:
                return Exception("Semantico", "Tipo de parametro de Parse no se puede convertir Float64 a Int64.", self.fila, self.columna)
            else:
                return int(simbolo_valor.get_valor())
        
        return None

