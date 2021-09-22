'''
    AST   -> Abstract Syntax Tree, almacena nodos.
    Nodos -> Los nodos del AST siven para realizar todas las instrucciones, funciones, operaciones, entre otros, por medio del interprete.
    Instruccion -> Sera una clase abstracta
'''
import graphviz
class Arbol():

    def __init__(self, instruccion):
        self.instruccion = instruccion
        self.funciones = []
        self.excepcion = []
        self.consola = ""
        self.tabla_ts_global = None
        self.Table = []
        self.dot = ""
        self.cont = 0


    def get_instruccion(self):
        return self.instruccion
    
    def set_instruccion(self, instruccion):
        self.instruccion = instruccion
    
    def get_excepcion(self):
        return self.excepcion
    
    def set_excepcion(self, excepcion):
        self.excepcion = excepcion

    def get_consola(self):
        return self.consola
    
    def set_consola(self, consola):
        self.consola = consola;

    def update_consola_(self, cadena): # Sin salto de linea
        self.consola += str(cadena)

    def update_consola(self, cadena):   # Para el println
        self.consola += str(cadena) + '\n'

    def get_tabla_ts_global(self):
        return self.tabla_ts_global

    def set_tabla_ts_global(self, ts_global):
        self.tabla_ts_global = ts_global

    def get_funciones(self):
        return self.funciones

    def getFuncion(self, nombre):
        for funcion in self.funciones:
            if funcion.nombre == nombre:
                return funcion
        return None
    
    def addFuncion(self, funcion):
        self.funciones.append(funcion)
    
    # GENERATE AST SIN HEROKU
    def generate_ast(self, root):
        self.dot = ""
        self.dot += "digraph {\n"
        self.dot += "n0[label=\"" + root.get_value().replace("\"", "\\\"") + "\"];\n"
        self.cont = 1
        self.search_graph("n0", root)
        self.dot += "}"
        return self.dot
    
    def search_graph(self, id, nodo_padre):
        for hijo in nodo_padre.getNodos():
            id_hijo = "n" + str(self.cont)
            self.dot += id_hijo + "[label=\"" + hijo.get_value().replace("\"", "\\\"") + "\"];\n"
            self.dot += id + "->" + id_hijo + ";\n"
            self.cont += 1
            self.search_graph(id_hijo, hijo)

    # GENERATE AST CON HEROKU
    def GENERATE_AST(self, root):
        dot = graphviz.Digraph(name="grafo", format="svg")
        print("h")
        print(root)
        dot.node('n0', root.get_value().replace("\"", "\\\""))
        self.cont = 1
        self.SEARCH_GRAPH(dot, 'n0', root)
        # dot.view()
        return dot

    def SEARCH_GRAPH(self, dot, id, nodo_padre):
        for hijo in nodo_padre.getNodos():
            id_hijo = "n" + str(self.cont)
            dot.node(id_hijo, hijo.get_value().replace("\"", "\\\""))
            dot.edge(id, id_hijo)
            self.cont +=1
            self.SEARCH_GRAPH(dot, id_hijo, hijo)