
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
        

from collections import deque


class Cola:
    def __init__(self) -> None:
        self.cola = deque([])
        self.ultimo = 0
        self.tamanio = 0
    def encolar(self,elemento) -> None:
        self.ultimo +=1
        self.cola.insert(self.ultimo,elemento)
        self.tamanio += 1
    def desencolar(self):#devuelve el primer valor de la cola
        return self.cola.popleft()   
    def esVacia(self) -> bool:
        if len(self.cola) == 0:
            return True
        else:
            return False
    def esPrimero(self):#devuelve el valor que hay en primer lugar
        return self.cola[0]

#La cima de la comida != primero alumnos
def no_es_nesquik(alumnos,comida):
    alumnos.desencolar()
    if comida.cima() == 1:
        alumnos.encolar(0)

    else:
        alumnos.encolar(1)

#Funcion principal
def siguiente(alumnos,comida):
    #comida = alumno
    if alumnos.esPrimero() == comida.cima():
        alumnos.desencolar()
        comida.desapilar()
    #comida != alumno
    else:
        no_es_nesquik(alumnos,comida)

def bucle(alumnos, comida):
    while not alumnos.esVacia() and comida.tamanio() != 0 and contiene(alumnos, comida.cima()):
        siguiente(alumnos, comida)

    if alumnos.esVacia() and comida.tamanio() != 0:
        print("Todos los alumnos tienen su comida")
    else:
        print("Hay alumnos sin comida")


def contiene(alumnos, elemento):
    # Guardamos los elementos que desencolamos para volver a encolarlos después
    elementos_temporales = []
    encontrado = False
    
    while not alumnos.esVacia():
        # Desencolamos el elemento
        actual = alumnos.desencolar()
        elementos_temporales.append(actual)  # Almacenamos el elemento temporalmente
        
        # Comparamos con el elemento que buscamos
        if actual == elemento:
            encontrado = True
    
    # Volvemos a encolar los elementos originales
    for elem in elementos_temporales:
        alumnos.encolar(elem)
    
    return encontrado


if __name__ == "__main__":
     
    alumnos = Cola()
    comida = Pila()
    
    alumnos.encolar(1)
    alumnos.encolar(0)
    alumnos.encolar(0)
    alumnos.encolar(1)

 # Insertar elementos en la pila 'comida'
    comida.apilar(1)
    comida.apilar(1)
    comida.apilar(0)
    comida.apilar(1)

    bucle(alumnos,comida)



