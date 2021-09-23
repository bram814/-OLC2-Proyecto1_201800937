from src.Interprete.TS.Exception import Exception
from src.Interprete.Nativas.UpperCase import UpperCase
from src.Interprete.Nativas.LowerCase import LowerCase
from src.Interprete.Abstract.Node_Ast import Node_Ast
from src.Interprete.Nativas.Tangente import Tangente
from src.Interprete.Nativas.String import String
from src.Interprete.Nativas.TypeOf import TypeOf
from src.Interprete.Nativas.Length import Length
from src.Interprete.Nativas.Coseno import Coseno
from src.Interprete.Nativas.Log10 import Log10
from src.Interprete.Nativas.Trunc import Trunc
from src.Interprete.Nativas.Parse import Parse
from src.Interprete.Nativas.Float import Float
from src.Interprete.Nativas.Sqrt import Sqrt
from src.Interprete.Nativas.Seno import Seno
from src.Interprete.Nativas.Log import Log
import re
import os
errores = []
reservadas = {
    'print'    : 'RPRINT',
    'println'  : 'RPRINTLN',
    'true'     : 'RTRUE',
    'false'    : 'RFALSE',
    'Int64'    : 'RINT64',
    'Float64'  : 'RFLOAT64',
    'Bool'     : 'RBOOL',
    'Char'     : 'RCHAR',
    'String'   : 'RSTRING',
    'global'   : 'RGLOBAL',
    'local'    : 'RLOCAL',
    'if'       : 'RIF',
    'elseif'   : 'RELSEIF',
    'else'     : 'RELSE',
    'end'      : 'REND',
    'break'    : 'RBREAK',
    'continue' : 'RCONTINUE',
    'return'   : 'RRETURN',
    'while'    : 'RWHILE',
    'for'      : 'RFOR',
    'in'       : 'RIN',
    'function' : 'RFUNCTION',
    'nothing'  : 'RNOTHING',
    'parse'    : 'RPARSE',
    'struct'   : 'RSTRUCT',
    'mutable'  : 'RMUTABLE',
}

tokens = [
    'MAS',
    'MENOS',
    'POR',
    'DIV',
    'POTE',
    'MODULO',
    'MAYORQUE',
    'MENORQUE',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUALACION',
    'DIFERENCIA',
    'AND',
    'OR',
    'NOT',
    'PUNTOCOMA',
    'PUNTO',
    'DOSPUNTOS',
    'DOBLEPUNTO',
    'COMA',
    'PARA',
    'PARC',
    'LLAVEA',
    'LLAVEC',
    'IGUAL',
    'DECIMAL',
    'ENTERO',
    'CADENA',
    'CHAR',
    'ID',
    'COMENTARIO_SIMPLE',
    'COMENTARIO_VARIAS_LINEAS',
] + list(reservadas.values())

# tokens
t_MAS           = r'\+'
t_MENOS         = r'\-'
t_POR           = r'\*'
t_DIV           = r'\/'
t_POTE           = r'\^'
t_MODULO        = r'\%'
t_MAYORQUE      = r'\>'
t_MENORQUE      = r'\<'
t_MAYORIGUAL    = r'\>\='
t_MENORIGUAL    = r'\<\='
t_IGUALACION    = r'\=\='
t_DIFERENCIA    = r'\!\='
t_AND           = r'\&\&'
t_OR            = r'\|\|'
t_NOT           = r'\!'
t_PUNTOCOMA     = r'\;'
t_PUNTO         = r'\.'
t_DOSPUNTOS     = r'\:'
t_DOBLEPUNTO    = r'\:\:'
t_COMA          = r'\,'
t_PARA          = r'\('
t_PARC          = r'\)'
t_LLAVEA        = r'\{'
t_LLAVEC        = r'\}'
t_IGUAL         = r'\='

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t):
    r'[a-zA-Z][a-zA-Z_0-9]*'
    t.type = reservadas.get(t.value,'ID')
    return t

def t_CADENA(t):
    r'\"(\\"|.)*?\"'
    t.value = t.value[1:-1]  # remover comillas
    t.value = t.value.replace('\\\\', '\\')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace("\\'", '\'')
    return t


def t_CHAR(t):
    r"""\' (\\'| \\\\ | \\n | \\t | \\r | \\" | .)? \'"""
    t.value = t.value[1:-1]  # remover comillas
    t.value = t.value.replace('\\\\', '\\')
    t.value = t.value.replace('\\n', '\n')
    t.value = t.value.replace('\\t', '\t')
    t.value = t.value.replace('\\r', '\r')
    t.value = t.value.replace('\\"', '\"')
    t.value = t.value.replace("\\'", '\'')
    return t

# comentario de varias lineas //...
def t_COMENTARIO_VARIAS_LINEAS(t):
    r'\#\=(.|\n)*?\=\#'
    t.lexer.lineno += t.value.count("\n") 

# Comentario simple //...
def t_COMENTARIO_SIMPLE(t):
    r'\#.*\n'
    t.lexer.lineno += 1

# Caracteres ignorados
t_ignore = " \t\r"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    errores.append(Exception("Lexico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    t.lexer.skip(1)

# Compute column.
#     input is the input text string
#     token is a token instance
def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# Construyendo el analizador léxico
import src.Interprete.ply.lex as lex
lexer = lex.lex()
# Asociacion
precedence = (
    ('left','OR'),
    ('left','AND'),
    ('right','UNOT'),
    ('left','IGUALACION','DIFERENCIA','MENORQUE','MENORIGUAL','MAYORQUE','MAYORIGUAL'),
    ('left','MAS','MENOS'),
    ('left','DIV','POR','MODULO'),
    ('nonassoc', 'POTE'),
    ('right','UMENOS'),
    )

# Definición de la Gramatica 
#   Clases Abstractas.
from src.Interprete.Instrucciones.Structs.DeclaracionStruct import DeclaracionStruct
from src.Interprete.Instrucciones.Declaracion import Declaracion
from src.Interprete.Instrucciones.Asignacion import Asignacion
from src.Interprete.Instrucciones.Structs.Struct import Struct
from src.Interprete.Instrucciones.Structs.Acceso import Acceso
from src.Interprete.Instrucciones.Continue import Continue
from src.Interprete.Instrucciones.Println import Println
from src.Interprete.Instrucciones.Llamada import Llamada
from src.Interprete.Instrucciones.Funcion import Funcion
from src.Interprete.Instrucciones.Return import Return
from src.Interprete.Instrucciones.While import While
from src.Interprete.Instrucciones.Print import Print
from src.Interprete.Instrucciones.Break import Break
from src.Interprete.Instrucciones.For import For
from src.Interprete.Instrucciones.If import If

from src.Interprete.Expresion.Identificador import Identificador
from src.Interprete.Expresion.Aritmetica import Aritmetica
from src.Interprete.Expresion.Relacional import Relacional
from src.Interprete.Expresion.Primitivo import Primitivo
from src.Interprete.Expresion.Logica import Logica
from src.Interprete.TS.Tipo import *

def p_init(t) :
    'init            : instrucciones'
    t[0] = t[1]

def p_instrucciones_instrucciones_instruccion(t) :
    'instrucciones    : instrucciones instruccion'
    if t[2] != "":
        t[1].append(t[2])
    t[0] = t[1]
    
# --------------------------------------------- INSTRUCCIONES ---------------------------------------------

def p_instrucciones_instruccion(t) :
    'instrucciones    : instruccion'
    if t[1] == "":
        t[0] = []
    else:    
        t[0] = [t[1]]

# --------------------------------------------- INSTRUCCION ---------------------------------------------

def p_instruccion(t):
    '''instruccion  : ins_print
                    | ins_println
                    | ins_asignacion
                    | ins_declaracion
                    | ins_if
                    | ins_break
                    | ins_continue
                    | ins_return
                    | ins_while
                    | ins_for
                    | ins_funcion
                    | ins_llamada fin_instruccion
                    | ins_struct
                    | ins_struct_declaracion
                    | COMENTARIO_VARIAS_LINEAS
                    | COMENTARIO_SIMPLE
    '''
    t[0] = t[1]


# ---------------------------------------- ERROR EN PUNTO COMA -------------------------------------------
def p_instruccion_error(t):
    'instruccion        : error PUNTOCOMA'
    errores.append(Exception("Sintáctico","Error Sintáctico. " + str(t[1].value) , t.lineno(1), find_column(input, t.slice[1])))
    t[0] = ""

def p_fin_instruccion(t) :
    '''fin_instruccion  : PUNTOCOMA
                        | '''
    if len(t) == 2:
        t[0] = ";"
    elif len(t) == 1:
        t[0] = None

# --------------------------------------------- IMPRIMIR ---------------------------------------------
def p_imprimir_print(t): # Sin salto de linea
    'ins_print   : RPRINT PARA listExp PARC fin_instruccion'
    if t[5] == None:
        errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
    t[0] = Print(t[3], t.lineno(1), find_column(input, t.slice[1]))
    
def p_imprimir_println(t): # Sin salto de linea
    'ins_println   : RPRINTLN PARA listExp PARC fin_instruccion'
    if t[5] == None:
        errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
    t[0] = Println(t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_list_coma_exp(t) :
    'listExp    : listExp  COMA sal_exp'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_list_list_coma_exp(t) :
    'listExp    : sal_exp'
    t[0] = [t[1]]

def p_list_ex(t):
    'sal_exp    : expresion'
    t[0] = t[1]
    
# --------------------------------------------- ASIGNACIÓN ---------------------------------------------
def p_instruccion_asignacion(t): # Lista de Asignacion.
    '''ins_asignacion   : asignacion_tipo 
                        | asignacion
    '''
    t[0] = t[1]

def p_asignacion_(t): # Asignacion -> ID = Expresión;
    '''asignacion       : ID IGUAL expresion fin_instruccion'''
    if t[4] == None:
        errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
    t[0] = Asignacion(t[1], t[3], None, t.lineno(1), find_column(input, t.slice[1]))

def p_asignacion_tipo(t): # Asignacion -> ID = Expresión :: TIPO
    '''asignacion_tipo  : ID IGUAL expresion DOBLEPUNTO TIPO fin_instruccion'''
    if t[6] == None:
        errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
    t[0] = Asignacion(t[1], t[3], t[5], t.lineno(1), find_column(input, t.slice[1]))

    # identificador, expresion, fila, columna):


# --------------------------------------------- ASIGNACIÓN [DECLARACION] ---------------------------------------------
def p_instruccion_declaracion(t):
    '''ins_declaracion  : declaracion_global
                        | declaracion_local 
    '''
    t[0] = t[1]

def p_declaracion_global(t):
    '''declaracion_global   : RGLOBAL ID fin_instruccion
                            | RGLOBAL ID IGUAL expresion fin_instruccion
    '''
    if len(t) == 4:
        if t[3] == None:
            errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
        t[0] = Declaracion(t[2], t.lineno(1), find_column(input, t.slice[1]), None)
    elif len(t) == 6:
        if t[5] == None:
            errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
        t[0] = Declaracion(t[2], t.lineno(1), find_column(input, t.slice[1]), t[4])


def p_declaracion_local(t):
    '''declaracion_local    : RLOCAL ID fin_instruccion'''
    if t[3] == None:
            errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
    t[0] = Declaracion(t[2], t.lineno(1), find_column(input, t.slice[1]), None)


# --------------------------------------------- CONDICIONAL [IF] ---------------------------------------------
def p_instruccion_if(t):
    '''ins_if   : RIF expresion instrucciones REND fin_instruccion
                | RIF expresion instrucciones RELSE instrucciones REND fin_instruccion
                | RIF expresion instrucciones list_elseif REND fin_instruccion
    '''
    if len(t) == 6: # [if]
        if t[5] == None:
            errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
        t[0] = If(t[2], t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    
    elif len(t) == 8: # [if][else]
        if t[7] == None:
            errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
        t[0] = If(t[2], t[3], t[5], None, t.lineno(1), find_column(input, t.slice[1]))
    
    elif len(t) == 7: # [if][elseif] | [IF][ELSEIF][ELSE]
        if t[6] == None:
            errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
        t[0] = If(t[2], t[3], None, t[4], t.lineno(1), find_column(input, t.slice[1]))
    
def p_list_elseif_instruccion(t):
    '''list_elseif  : RELSEIF expresion instrucciones
                    | RELSEIF expresion instrucciones list_elseif
                    | RELSEIF expresion instrucciones RELSE instrucciones
    '''
    if len(t) == 4:
        t[0] = If(t[2], t[3], None, None, t.lineno(1), find_column(input, t.slice[1]))
    elif len(t) == 5:
        t[0] = If(t[2], t[3], None, t[4], t.lineno(1), find_column(input, t.slice[1]))
    elif len(t) == 6:
        t[0] = If(t[2], t[3], t[5], None, t.lineno(1), find_column(input, t.slice[1]))
    
# --------------------------------------------- SENTENCIAS DE TRANSFERENCIAS [BREAK] -----------------------------------------------
def p_instruccion_break(t) :
    'ins_break      : RBREAK fin_instruccion'
    t[0] = Break(t.lineno(1), find_column(input, t.slice[1]))

# --------------------------------------------- SENTENCIAS DE TRANSFERENCIAS [CONTINUE] --------------------------------------------
def p_instruccion_return(t) :
    'ins_return     : RRETURN expresion fin_instruccion'
    t[0] = Return(t[2], t.lineno(1), find_column(input, t.slice[1]))

# --------------------------------------------- SENTENCIAS DE TRANSFERENCIAS [RETURN] ----------------------------------------------
def p_instruccion_continue(t) :
    'ins_continue   : RCONTINUE fin_instruccion'
    t[0] = Continue(t.lineno(1), find_column(input, t.slice[1]))

# --------------------------------------------- lOOPS [WHILE] ---------------------------------------------
def p_instruccion_while(t):
    '''ins_while    : RWHILE expresion instrucciones REND fin_instruccion'''
    if t[5] == None:
        errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
    t[0] = While(t[2], t[3], t.lineno(1), find_column(input, t.slice[1]))

# --------------------------------------------- LOOPS [FOR] ----------------------------------------------
def p_instruccion_for(t):
    '''ins_for      : RFOR ID RIN expresion DOSPUNTOS expresion instrucciones REND fin_instruccion 
                    | RFOR ID RIN expresion instrucciones REND fin_instruccion
    '''
    if len(t) == 10:
        if t[8] == None:
            errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
        t[0] = For(t[2], t[4], t[6], t[7], t.lineno(1), find_column(input, t.slice[1]))
    elif len(t) == 8:
        if t[7] == None:
            errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
        t[0] = For(t[2], t[4], None, t[5], t.lineno(1), find_column(input, t.slice[1]))

 
# --------------------------------------------- FUNCIONES [CREATE FUNCTION] ----------------------------------------------
def p_instruccion_funcion(t):
    '''ins_funcion  : RFUNCTION ID PARA PARC instrucciones REND fin_instruccion
                    | RFUNCTION ID PARA parametros PARC instrucciones REND fin_instruccion
    '''
    if len(t) == 8:
        if t[7] == None:
            errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
        t[0] = Funcion(t[2], [], t[5], t.lineno(1), find_column(input, t.slice[1]))
    
    elif len(t) == 9:
        if t[8] == None:
            errores.append(Exception("Sintáctico","Error Sintáctico, falta \";\". ", t.lineno(1), find_column(input, t.slice[1])))
        t[0] = Funcion(t[2], t[4], t[6], t.lineno(1), find_column(input, t.slice[1]))

def p_parametros_parametros(t) :
    'parametros     : parametros COMA parametro'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_parametros_parametro(t) :
    'parametros    : parametro'
    t[0] = [t[1]]

def p_parametro(t) :
    'parametro     : ID DOBLEPUNTO TIPO'
    t[0] = {'tipoDato':t[3],'identificador':t[1]} # Create Dicctionary.

# --------------------------------------------- FUNCIONES [CALL FUNCTION] ----------------------------------------------
def p_instruccion_llamada(t) :
    'ins_llamada     : ID PARA PARC'
    t[0] = Llamada(t[1], [], t.lineno(1), find_column(input, t.slice[1]))


def p_instruccion_llamada_params(t) :
    'ins_llamada     : ID PARA listParams PARC'
    t[0] = Llamada(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_instruccion_llamada_parse(t):
    'ins_llamada     : RPARSE PARA listParse PARC'
    t[0] = Llamada(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_list_parse(t):
    '''listParse    :   listParse COMA expresion'''
    t[1].append(t[3])
    t[0] = t[1]

def p_list_parse_(t):
    '''listParse    : parseFloat'''
    t[0] = [t[1]]

def p_list_float_parse(t):
    '''parseFloat   : RFLOAT64
                    | RINT64
    '''
    if t[1] == 'Float64':
        t[0] = Primitivo(Tipo.STRING, str(t[1]), t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == 'Int64':
        t[0] = Primitivo(Tipo.STRING, str(t[1]), t.lineno(1), find_column(input, t.slice[1]))
        
        
def p_list_params_params(t) :
    'listParams    : listParams COMA listParam'
    t[1].append(t[3])
    t[0] = t[1]
    
def p_list_params_param(t) :
    'listParams    : listParam'
    t[0] = [t[1]]

def p_list_param(t):
    'listParam    : expresion'
    t[0] = t[1]

# --------------------------------------------- [STRUCT] [CREAR] ----------------------------------------------
def p_instruccion_struct(t):
    '''ins_struct   :   RSTRUCT ID listStructs REND fin_instruccion'''
    t[0] = Struct(t[2], t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_list_list_struct(t) :
    'listStructs    : listStructs listStruct'
    t[1].append(t[2])
    t[0] = t[1]

def p_list_struct(t) :
    'listStructs    : listStruct'
    t[0] = [t[1]]

def p_expresion_struct(t):
    'listStruct    :    ID PUNTOCOMA'
    t[0] = {'tipoDato':None,'identificador':t[1], t[1]: None}

def p_expresion_struct_tipo(t):
    'listStruct    :    ID DOBLEPUNTO TIPO PUNTOCOMA '
    t[0] = {'tipoDato':t[3],'identificador':t[1], t[1]: None}

# --------------------------------------------- [STRUCT] [DECLARACION] ----------------------------------------------
def p_instruccion_struct_declaracion(t):
    '''ins_struct_declaracion   : ID PARA listParams PARC'''
    t[0] = DeclaracionStruct(t[1], Tipo.STRUCT, t[3], t.lineno(1), find_column(input, t.slice[1]))

# --------------------------------------------- [STRUCT] [CALL] ----------------------------------------------
def p_instruccion_struct_call(t):
    '''ins_struct_call  : ID PUNTO ID'''
    t[0] = Acceso(t[1], t[3], t.lineno(1), find_column(input, t.slice[1]))

# --------------------------------------------- TIPO DE DATO ---------------------------------------------
def p_tipo(t):
    ''' TIPO            : RINT64
                        | RFLOAT64
                        | RBOOL
                        | RCHAR
                        | RSTRING'''

    if t[1] == 'Int64':
        t[0] = Tipo.INT64
    elif t[1] == 'Float64':
        t[0] = Tipo.FLOAT64
    elif t[1] == 'Bool':
        t[0] = Tipo.BOOLEANO
    elif t[1] == 'Char':
        t[0] = Tipo.CHAR
    elif t[1] == 'String':
        t[0] = Tipo.STRING
    elif t[1] == 'nothing':
        t[0] = Tipo.NULO
# --------------------------------------------- EXPRESION ---------------------------------------------

def p_expresion_binaria(t):
    '''
    expresion : expresion MAS expresion
            | expresion MENOS expresion
            | expresion POR expresion
            | expresion DIV expresion
            | expresion POTE expresion
            | expresion MODULO expresion
            | expresion MAYORQUE expresion
            | expresion MENORQUE expresion
            | expresion MAYORIGUAL expresion
            | expresion MENORIGUAL expresion
            | expresion IGUALACION expresion
            | expresion DIFERENCIA expresion
            | expresion AND expresion
            | expresion OR expresion
    '''
    # Aritmética
    if t[2] == '+':
        t[0] = Aritmetica(t[1], Operador_Aritmetico.SUMA,   t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '-':
        t[0] = Aritmetica(t[1], Operador_Aritmetico.RESTA,  t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '*':
        t[0] = Aritmetica(t[1], Operador_Aritmetico.POR,    t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '/':
        t[0] = Aritmetica(t[1], Operador_Aritmetico.DIV,    t[3], t.lineno(2), find_column(input, t.slice[2]))   
    elif t[2] == '^':
        t[0] = Aritmetica(t[1], Operador_Aritmetico.POTE,   t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '%':
        t[0] = Aritmetica(t[1], Operador_Aritmetico.MODU,   t[3], t.lineno(2), find_column(input, t.slice[2]))  
    # Relacional
    elif t[2] == '>':
        t[0] = Relacional(t[1], Operador_Relacional.MAYORQUE,   t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '<':
        t[0] = Relacional(t[1], Operador_Relacional.MENORQUE,   t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '>=':
        t[0] = Relacional(t[1], Operador_Relacional.MAYORIGUAL, t[3], t.lineno(2), find_column(input, t.slice[2])) 
    elif t[2] == '<=':
        t[0] = Relacional(t[1], Operador_Relacional.MENORIGUAL, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '==':
        t[0] = Relacional(t[1], Operador_Relacional.IGUALACION, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '!=':
        t[0] = Relacional(t[1], Operador_Relacional.DIFERENCIA, t[3], t.lineno(2), find_column(input, t.slice[2]))
    # Lógica.
    elif t[2] == '&&':
        t[0] = Logica(t[1], Operador_Logico.AND, t[3], t.lineno(2), find_column(input, t.slice[2]))
    elif t[2] == '||':
        t[0] = Logica(t[1], Operador_Logico.OR, t[3], t.lineno(2), find_column(input, t.slice[2]))

def p_expresion_unaria(t):
    '''expresion : MENOS expresion %prec UMENOS
                | NOT expresion %prec UNOT'''
    
    if t[1] == '-':
        t[0] = Aritmetica(t[2], Operador_Aritmetico.UMENOS, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
        t[0] = Logica(t[2], Operador_Logico.NOT, None, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_agrupacion(t):
    ''' expresion :   PARA expresion PARC '''
    t[0] = t[2]

def p_expresion_identificador(t):
    '''expresion : ID'''
    t[0] = Identificador(t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_entero(t):
    '''expresion : ENTERO'''
    t[0] = Primitivo(Tipo.INT64,t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_decimal(t):
    '''expresion : DECIMAL'''
    t[0] = Primitivo(Tipo.FLOAT64, t[1], t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_cadena(t):
    '''expresion : CADENA'''
    t[0] = Primitivo(Tipo.STRING,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_char(t):
    '''expresion : CHAR'''
    t[0] = Primitivo(Tipo.CHAR,str(t[1]).replace('\\n', '\n'), t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_true(t):
    '''expresion : RTRUE'''
    t[0] = Primitivo(Tipo.BOOLEANO, True, t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_false(t):
    '''expresion : RFALSE'''
    t[0] = Primitivo(Tipo.BOOLEANO, False, t.lineno(1), find_column(input, t.slice[1]))

def p_primitivo_None(t):
    '''expresion : RNOTHING'''
    t[0] = Primitivo(Tipo.NULO, None, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_llamada(t):
    '''expresion : ins_llamada'''
    t[0] = t[1]

def p_expresion_struct_atributo(t):
    '''expresion : ins_struct_call'''
    t[0] = t[1]

import src.Interprete.ply.yacc as yacc
parser = yacc.yacc()

input = ''

def getErrores():
    return errores

def parse(inp) :
    global errores
    global lexer
    global parser
    errores = []
    lexer = lex.lex()
    parser = yacc.yacc()
    global input
    input = inp
    return parser.parse(inp)

def create_native(ast):

    name = "uppercase" # CONVIERTE A MAYUSCULA.
    params = [{'tipoDato':Tipo.STRING,'identificador':'UpperCase##Native1'}]
    instrucciones = []
    uppercase = UpperCase(name, params, instrucciones, -1, -1)
    ast.addFuncion(uppercase)
 
    name = "lowercase" # CONVIERTE A MINUSCULA.
    params = [{'tipoDato':Tipo.STRING,'identificador':'LowerCase##Native2'}]
    instrucciones = []
    lowercase = LowerCase(name, params, instrucciones, -1, -1)
    ast.addFuncion(lowercase)

    name = "typeof"
    params = [{'tipoDato':Tipo.NULO,'identificador':'TypeOf##Native3'}]
    instrucciones = []
    typeof = TypeOf(name, params, instrucciones, -1, -1)
    ast.addFuncion(typeof)    

    name = "length"
    params = [{'tipoDato':Tipo.STRING,'identificador':'Length##Native4'}]
    instrucciones = []
    length = Length(name, params, instrucciones, -1, -1)
    ast.addFuncion(length)   

    name = "log10"
    params = [{'tipoDato':Tipo.INT64,'identificador':'Log10##Native5'}]
    instrucciones = []
    log10 = Log10(name, params, instrucciones, -1, -1)
    ast.addFuncion(log10)  

    name = "log"
    params = [{'tipoDato':Tipo.INT64,'identificador':'Log##Native6'}, {'tipoDato':Tipo.INT64,'identificador':'Log##Native7'}]
    instrucciones = []
    log = Log(name, params, instrucciones, -1, -1)
    ast.addFuncion(log)  

    name = "trunc"
    params = [{'tipoDato':Tipo.INT64,'identificador':'Trunc##Native8'}]
    instrucciones = []
    truncate = Trunc(name, params, instrucciones, -1, -1)
    ast.addFuncion(truncate)    
    
    name = "sin"
    params = [{'tipoDato':Tipo.INT64,'identificador':'Sin##Native9'}]
    instrucciones = []
    sin = Seno(name, params, instrucciones, -1, -1)
    ast.addFuncion(sin)
    
    name = "cos"
    params = [{'tipoDato':Tipo.INT64,'identificador':'Cos##Native10'}]
    instrucciones = []
    cos = Coseno(name, params, instrucciones, -1, -1)
    ast.addFuncion(cos)

    name = "tan"
    params = [{'tipoDato':Tipo.INT64,'identificador':'Tan##Native11'}]
    instrucciones = []
    tan = Tangente(name, params, instrucciones, -1, -1)
    ast.addFuncion(tan)

    name = "sqrt"
    params = [{'tipoDato':Tipo.INT64,'identificador':'Sqrt##Native12'}]
    instrucciones = []
    sqrt = Sqrt(name, params, instrucciones, -1, -1)
    ast.addFuncion(sqrt)

    name = "string"
    params = [{'tipoDato':Tipo.STRING,'identificador':'String##Native13'}]
    instrucciones = []
    string = String(name, params, instrucciones, -1, -1)
    ast.addFuncion(string)

    name = "parse"
    params = [{'tipoDato':Tipo.STRING,'identificador':'Parse##Native14'},{'tipoDato':Tipo.STRING,'identificador':'Parse##Native15'}]
    instrucciones = []
    parse = Parse(name, params, instrucciones, -1, -1)
    ast.addFuncion(parse)

    name = "float"
    params = [{'tipoDato':Tipo.FLOAT64,'identificador':'Float##Native16'}]
    instrucciones = []
    float = Float(name, params, instrucciones, -1, -1)
    ast.addFuncion(float)



from src.Interprete.TS.Arbol import Arbol
from src.Interprete.TS.TablaSimbolo import TablaSimbolo

def execute_grammar(entrada):
    # f = open("Backend/src/entrada.txt", "r")
    # entrada = f.read()
    # f.close()

    instrucciones = parse(str(entrada)+"\n")
    ast = Arbol(instrucciones)
    TSGlobal = TablaSimbolo()
    ast.set_tabla_ts_global(TSGlobal)
    create_native(ast)
    # Busca errores Lexicos y Sintacticos.
    for error in errores:
        ast.get_excepcion().append(error) # Lo guarda
        ast.update_consola(error.__str__()) # Lo actualiza en consola (lo muestra)

    for instruccion in ast.get_instruccion():
        if isinstance(instruccion, Funcion): 
            ast.addFuncion(instruccion)
        else:
            value = instruccion.interpretar(ast, TSGlobal)
            if isinstance(value, Exception):
                ast.get_excepcion().append(value)
                ast.update_consola(value.__str__())
            if isinstance(value, Break): 
                mistake = Exception("Semantico", "Break fuera de Bucle", instruccion.fila, instruccion.columna)
                ast.get_excepcion().append(mistake)
                ast.update_consola(mistake.__str__())
            if isinstance(value, Continue): 
                mistake = Exception("Semantico", "Continue fuera de Bucle", instruccion.fila, instruccion.columna)
                ast.get_excepcion().append(mistake)
                ast.update_consola(mistake.__str__())
            if isinstance(value, Return): 
                mistake = Exception("Semantico", "Return fuera de Bucle", instruccion.fila, instruccion.columna)
                ast.get_excepcion().append(mistake)
                ast.update_consola(mistake.__str__())


    return ast