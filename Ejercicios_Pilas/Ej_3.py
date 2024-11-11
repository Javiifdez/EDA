
''' ---------------------------- Ejercicio 3 Implementacion Pilas ------------------------------------------

Conversion de números de base decimal a binaria: Escribe un programa que
convierta un número entero positivo ingresado por el usuario desde la base decimal
a la base binaria. Usa una lista como pila para almacenar los restos de la división
por 2 y, luego, imprime el número binario al desapilar los elementos.
Motivación: La lista permite una implementación sencilla de la pila sin necesidad
de crear una clase adicional

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



def conversion_bin(numero) -> str:
    restos= Pila()
    resultado = ""
 #conversion a base entera, cada resto es una cifra del numero
    cociente =1
    while cociente != 0:

        cociente = numero // 2
        resto = (numero % 2) #tambien podrias cambiar a string aqui
        restos.apilar(resto)
        numero=cociente 

#desapilamos y guardamos los restos en la variable resultado
    while not restos.esVacia():
        resultado += str(restos.cima()) #solo se puede concatenar strings
        restos.desapilar()

    return resultado


numero=13
print(conversion_bin(numero))