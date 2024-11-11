
''' ---------------------------- Ejercicio 6 Implementacion Pilas ------------------------------------------

Verificar palíndromo con pilas: Escribe un programa que determine si una palabra
ingresada por el usuario es un palíndromo. Usa una lista como pila para almacenar
los caracteres de la palabra y compáralos al desapilar.
Motivación: Utilizar listas como pilas es una forma sencilla y práctica de abordar el
problema, y ayuda a los estudiantes a entender el concepto de comparación de
elementos usando una estructura de datos.

FUNCIONA PARA PALABRAS, PARA FRASES HAY QUE HACER ALGUNOS CAMBIO QUE NO ENTIENDO

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
    
def es_palindromo(palabra) -> bool:

    palabra = palabra.lower()
    pila1 = Pila()
    invertida = ""

    for letra in palabra:
        pila1.apilar(letra)

    for i in range(pila1.tamanio()):

        invertida += pila1.cima()
        pila1.desapilar()

    if invertida == palabra :
        return True
    
    else:
        return False
    


if __name__ == "__main__":

    print(es_palindromo("Reconocer"))