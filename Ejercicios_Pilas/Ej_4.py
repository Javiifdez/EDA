


''' ---------------------------- Ejercicio 4 Implementacion Pilas ------------------------------------------

Evaluación de expresiones postfijas (notación polaca inversa): Implementa un
programa que evalúe una expresión matemática en notación postfija (por ejemplo,
5 6 + 2 *). Usa una lista como pila para almacenar los operandos y aplicar las
operaciones cuando corresponda.
Motivación: Las listas permiten manipular de forma directa los elementos para
implementar la lógica de las operaciones postfijas

Ver Tema 2.1 Pilas.pdf para más detalles

Hemos consultado: https://docs.python.org/es/3/tutorial/classes.html
-------------------------------------------------------------------------------------------------- '''

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

def evaluar_postfija(expresion)-> bool:
    expresion_pila = Pila()
    operadores = "+", "-" , "*" , "/"

    #dividimos la expresion en una lista 
    expresion = expresion.split()

    for elemento in expresion:

        if elemento in operadores: 

            if expresion_pila.tamanio() < 2:
                return False

            num1 = expresion_pila.cima()
            expresion_pila.desapilar()

            num2 = expresion_pila.cima()
            expresion_pila.desapilar()

            if elemento == "+":

                num3= num1 + num2
                expresion_pila.apilar(num3)
            
            if elemento == "-":

                num3= num1 - num2
                expresion_pila.apilar(num3)

            if elemento == "*":

                num3= num1 * num2
                expresion_pila.apilar(num3)

            if elemento == "/":
                
                try:
                    num3= num1 / num2
                    expresion_pila.apilar(num3)
                
                except ZeroDivisionError:
                    print("No se puede dividir entre 0")
                    return False
            
        else:
            expresion_pila.apilar(int(elemento))
    
    if expresion_pila.tamanio() != 1:
        return False
    
    else:
        return True
    
if __name__ == "__main__" :

    expresion= "3 / 2 -"

    print(evaluar_postfija(expresion))
        