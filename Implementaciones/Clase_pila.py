class Pila:
    # El constructor de la clase. Inicializa las nuevas instancias de la clase: Objetos
    def __init__(self):
        self.pila = [] # Esta lista va a almacenar el contenido de la pila
        self.tamanio = 0

    def apilar(self, elemento):
        self.pila.append(elemento)
        self.tamanio +=1

    def desapilar(self):
        if (not self.esVacia()):
            self.pila.pop() # Nuestro método desalipa sin devolver la cima
            #return self.pila.pop() # desapila y devuelve la cima
        else:
            print("ERROR: No se puede desapilar porque la pila estaba vacía.")
        self.tamanio -= 1
    def cima(self):
        if (not self.esVacia()):
            #return self.pila[len(self.pila)-1] # asi lo hacemos en C, pero...
            return self.pila[-1] # es equivalente a lo anterior, para acceder al último de la lista
        else:
            print("ERROR: No se puede consultar la cimar porque la pila estaba vacía.")
    
    def tamanio(self):#es un metodo de la clase Pila
        return self.tamanio