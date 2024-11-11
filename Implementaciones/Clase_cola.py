
from collections import deque

class Cola:
#CONSTRUCTOR DE LA CLASE COLA
    def __init__(self) -> None:
        self.cola = deque([])
        self.ultimo = 0
        self.tamanio = 0

#AÑADIR UN ELEMENTO A LA COLA
    def encolar(self,elemento) -> None:
        self.ultimo +=1
        self.cola.insert(self.ultimo,elemento)
        self.tamanio += 1

#QUITAR UN ELEMENTO A LA COLA
    def desencolar(self):#devuelve el primer valor de la cola
        return self.cola.popleft()
    
    def esVacia(self) -> bool:
        if len(self.cola) == 0:
            return True
        else:
            return False

    def esPrimero(self):#devuelve el valor que hay en primer lugar
        return self.cola[0]

"""  
                   
from sys import path
path.append(r'C:\Users\Jabvier Fernandez\OneDrive - UFV\Code\EDA\Implementaciones')
from Clase_cola import Cola

"""