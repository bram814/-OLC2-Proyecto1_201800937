from Interprete.Abstract.Instruccion import Instruccion
from Interprete.TS.Exception import Exception
from Interprete.TS.Tipo import *

class Logica(Instruccion):
    
    def __init__(self, exp_left, operador, exp_rigth, fila, columna):
        self.exp_left = exp_left
        self.operador = operador
        self.exp_rigth = exp_rigth
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.BOOLEANO