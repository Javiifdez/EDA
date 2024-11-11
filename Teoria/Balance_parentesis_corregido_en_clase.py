''' ---------------------------- SESIÓN PRÁCTICA 14/10/2024 ------------------------------------------
Vamos a programar la función para comprobar el balance de parentesis usando TAD Pila
Ver Tema 2.1 Pilas.pdf para más detalles
    Ejercicios pilas del T2.
-------------------------------------------------------------------------------------------------- '''

class Pila:
    # El constructor de la clase. Inicializa las nuevas instancias de la clase: Objetos
    def __init__(self):
        self.pila = [] # Esta lista va a almacenar el contenido de la pila

    def esVacia(self):
       return (len(self.pila)==0) # Se podría cambiar por un if...

    def apilar(self, elemento):
        self.pila.append(elemento)

    def desapilar(self):
        if (not self.esVacia()):
            self.pila.pop() # Nuestro método desalipa sin devolver la cima
            #return self.pila.pop() # desapila y devuelve la cima
        else:
            print("ERROR: No se puede desapilar porque la pila estaba vacía.")

    def cima(self):
        if (not self.esVacia()):
            #return self.pila[len(self.pila)-1] # asi lo hacemos en C, pero...
            return self.pila[-1] # es equivalente a lo anterior, para acceder al último de la lista
        else:
            print("ERROR: No se puede consultar la cimar porque la pila estaba vacía.")


## Resolucion ejercicio
def esBalanceada(expresion): ## balanceada se refiere a los parentesis bien ordenados 
    pila = Pila()

    # Recorremos expresion caracter a caracter
    for caracter in expresion:
        if (caracter=='(' or caracter =='{'  or caracter == '[') :
            pila.apilar(caracter)
        elif (caracter==')'): # Para no hacer 3 elif, cambiar por uso de diccionario
            # En la cima debiera haber un '('
            if (pila.cima() == '('):
                pila.desapilar()
            else:
                return False
        elif (caracter=='}'):
            # En la cima debiera haber un '{'
            if (pila.cima() == '{'):
                pila.desapilar()
            else:
                return False
        elif (caracter==']'):
            # En la cima debiera haber un '['
            if (pila.cima() == '['):
                pila.desapilar()
            else:
                return False
                    
    return pila.esVacia()


# Programa principal. Podriamos hacerlo con una lista de expresiones / pidiendo al usuario por consola ...
exp1 = ""
exp2 = "( a+b ) * 3 ("
exp3 = "( a+b ] * 3"
exp4 = ") a+b ( * 3"
exp5 = "[ ( ) ] + { 3}"

print(f"{exp1} : {esBalanceada(exp1)}")
print(f"{exp2} : {esBalanceada(exp2)}")
print(f"{exp3} : {esBalanceada(exp3)}")