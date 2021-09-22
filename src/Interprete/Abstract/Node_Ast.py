class Node_Ast():
    
    def __init__(self, value):
        self.value = value
        self.hojas = []

    def getNodos(self):
        return self.hojas
        
    def setNodos(self, hojas):
        self.hojas = hojas
    
    def crearHoja(self, valueHijo):
        self.hojas.append(Node_Ast(valueHijo))

    def crearNodo(self, hijo):
        self.hojas.append(hijo)

    def get_value(self):
        return str(self.value)
    
    def set_value(self, value):
        self.value = value
