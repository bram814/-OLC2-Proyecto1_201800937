from enum import Enum

class Tipo(Enum):

    NULO     = 1 # Nulo
    INT64    = 2 # Enteros
    FLOAT64  = 3 # Decimal
    BOOLEANO = 4 # Booleano
    CHAR     = 5 # Caracter 'a'
    STRING   = 6 # Cadena "texto"
    ARRAY    = 7 # Arrelo []
    STRUCT   = 8 

class Operador_Aritmetico(Enum):

    SUMA        = 1  # suma (+)
    RESTA       = 2  # resta (-)
    POR         = 3  # multiplicacion (*)
    DIV         = 4  # division (/)
    POTE        = 5  # potencia (^)
    MODU        = 6  # modulo (%)

class Operador_Relacional(Enum):
    
    MAYORQUE   = 1  # (>)
    MENORQUE   = 2  # (<)
    MAYORIGUAL = 3  # (>=)
    MENORIGUAL = 4  # (<=)
    IGUALACION = 5  # (==)
    DIFERENCIA = 6  # (!=)


class Operador_Logico(Enum):
    
    OR  = 1  # (||)
    AND = 2  # (&&)
    NOT = 3  # (!)
