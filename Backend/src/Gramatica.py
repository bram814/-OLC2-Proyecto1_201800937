import re
import os
from Interprete.TS.Exception import Exception
errores = []
reservadas = {
    'print'    : 'RPRINT',
    'println'  : 'RPRINTLN',
    'true'     : 'RTRUE',
    'false'    : 'RFALSE',
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
t_DOBLEPUNTO    = r'\:'
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
     t.type = reservadas.get(t.value.lower(),'ID')
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
t_ignore = " \t"

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
import Interprete.ply.lex as lex
lexer = lex.lex()
# Asociacion
# precedence = (
#     ('left','OR'),
#     ('left','AND'),
#     ('right','UNOT'),
#     ('left','IGUALACION','DIFERENCIA','MENORQUE','MENORIGUAL','MAYORQUE','MAYORIGUAL'),
#     ('left','MAS','MENOS'),
#     ('left','DIV','POR','MODULO'),
#     ('nonassoc', 'POTE'),
#     ('right','UMENOS'),
#     )
precedence = (
    ('right','IGUAL'),
    ('left', 'OR'),
    ('left', 'AND'),
    ('left', 'UNOT'),
    ('nonassoc', 'MAYORQUE', 'MENORQUE', 'MAYORIGUAL', 'MENORIGUAL', 'IGUALACION', 'DIFERENCIA'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'POR', 'DIV', 'MODULO'),
    ('right', 'UMENOS'),
    ('right', 'POTE'),
    )

# Definición de la Gramatica 
#   Clases Abstractas.
from Interprete.Instrucciones.Println import Println
from Interprete.Instrucciones.Print import Print

from Interprete.Expresion.Aritmetica import Aritmetica
from Interprete.Expresion.Relacional import Relacional
from Interprete.Expresion.Primitivo import Primitivo
from Interprete.Expresion.Logica import Logica
from Interprete.TS.Tipo import *

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
    '''instruccion  : ins_print fin_instruccion
                    | ins_println fin_instruccion
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
    '''fin_instruccion  : PUNTOCOMA'''
    t[0] = None

# --------------------------------------------- IMPRIMIR ---------------------------------------------
def p_imprimir_print(t): # Sin salto de linea
    'ins_print   : RPRINT PARA expresion PARC'
    t[0] = Print(t[3], t.lineno(1), find_column(input, t.slice[1]))

def p_imprimir_println(t): # Sin salto de linea
    'ins_println   : RPRINTLN PARA expresion PARC'
    t[0] = Println(t[3], t.lineno(1), find_column(input, t.slice[1]))

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
    # elif t[1] == '+':
    #     t[0] = Aritmetica(t[2], Operador_Aritmetico.UMAS, None, t.lineno(1), find_column(input, t.slice[1]))
    elif t[1] == '!':
         t[0] = Logica(t[2], Operador_Logico.NOT, None, t.lineno(1), find_column(input, t.slice[1]))

def p_expresion_agrupacion(t):
    ''' expresion :   PARA expresion PARC '''
    t[0] = t[2]

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


import Interprete.ply.yacc as yacc
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


from Interprete.TS.Arbol import Arbol
from Interprete.TS.TablaSimbolo import TablaSimbolo

f = open("Backend/src/entrada.txt", "r")
entrada = f.read()
f.close()

instrucciones = parse(str(entrada)+"\n")
ast = Arbol(instrucciones)
TSGlobal = TablaSimbolo()
ast.set_tabla_ts_global(TSGlobal)

# Busca errores Lexicos y Sintacticos.
for error in errores:
    ast.get_excepcion().append(error) # Lo guarda
    ast.update_consola(error.__str__()) # Lo actualiza en consola (lo muestra)

for instruccion in ast.get_instruccion():
    value = instruccion.interpretar(ast, TSGlobal)
    if isinstance(value, Exception):
        ast.get_excepcion().append(value)
        ast.update_consola(value.__str__())


print(ast.get_consola())