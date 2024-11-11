"""
Invertir una cadena: Dada una cadena de texto ingresada por el usuario, utiliza una 
lista como pila para invertir el orden de los caracteres. Muestra la cadena invertida 
al final. 
Motivación: En Python, las listas son una forma natural de implementar pilas 
debido a su flexibilidad y las operaciones de apilado y desapilado. 
"""
class Pila:
    def __init__(self):
        self.pila = []
    def esVacia(self):
       return (len(self.pila)==0)
    def apilar(self, elemento):
        self.pila.append(elemento)
    def desapilar(self):
        if (not self.esVacia()):
            self.pila.pop()
        else:
            print("ERROR: No se puede desapilar porque la pila estaba vacía.")
    def cima(self):
        if (not self.esVacia()):
            return self.pila[-1]
        else:
            print("ERROR: No se puede consultar la cimar porque la pila estaba vacía.")
    
    def tamanio(self):#es un metodo de la clase Pila
        return len(self.pila)


def invertir_cadena(cadena) ->str:
    
    cadena_invertida=""
    pila1= Pila()

#apilamos la cadena en una nueva pila
    for letra in cadena:
        pila1.apilar(letra)
#desapilamos la cadena en un string para que este invertida    
    while not pila1.esVacia():
#es necesario ver la cima porque el metodo desapilar no retorna ningún valor
        cadena_invertida = cadena_invertida + pila1.cima()
        pila1.desapilar()

    return cadena_invertida


if __name__ == "__main__":
    cadena = input("Dame una cadena:")
    cadena_invertida = invertir_cadena(cadena)
    print(cadena_invertida)