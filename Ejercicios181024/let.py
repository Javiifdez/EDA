class Pila:
    def __init__(self):
        self.pila = []

    def esVacia(self):
        return len(self.pila) == 0

    def apilar(self, elemento):
        self.pila.append(elemento)

    def desapilar(self):
        if not self.esVacia():
            return self.pila.pop()
        else:
            print("ERROR: No se puede desapilar porque la pila estaba vacía.")

    def cima(self):
        if not self.esVacia():
            return self.pila[-1]
        else:
            print("ERROR: No se puede consultar la cima porque la pila estaba vacía.")

    def tamanio(self):
        return len(self.pila)


from collections import deque


class Cola:
    def __init__(self) -> None:
        self.cola = deque([])

    def encolar(self, elemento) -> None:
        self.cola.append(elemento)

    def desencolar(self):  # devuelve el primer valor de la cola
        return self.cola.popleft() if not self.esVacia() else None

    def esVacia(self) -> bool:
        return len(self.cola) == 0

    def esPrimero(self):  # devuelve el valor que hay en primer lugar
        return self.cola[0] if not self.esVacia() else None

    def tamanio(self):  # Método para obtener el tamaño de la cola
        return len(self.cola)


def num_students_unable_to_eat(sandwiches, alumnos):
    pila_sandwiches = Pila()
    cola_estudiantes = Cola()

    # Apilamos los sándwiches en la pila
    for sandwich in sandwiches:
        pila_sandwiches.apilar(sandwich)

    # Encolamos a los estudiantes en la cola
    for alumno in alumnos:
        cola_estudiantes.encolar(alumno)

    # Contamos el número de estudiantes que no pueden comer
    while not cola_estudiantes.esVacia():
        if pila_sandwiches.esVacia():  # Si ya no hay sándwiches
            break

        # Miramos el sándwich en la cima de la pila
        sandwich_cima = pila_sandwiches.cima()
        no_comer = False
        size = cola_estudiantes.tamanio()

        for _ in range(size):
            alumno = cola_estudiantes.desencolar()

            if alumno == sandwich_cima:
                # El estudiante come el sándwich
                no_comer= True
                pila_sandwiches.desapilar()  # Se sirve el sándwich
                break
            else:
                # El estudiante no puede comer y vuelve al final de la cola
                cola_estudiantes.encolar(alumno)

        if not no_comer:
            # Si nadie pudo comer el sándwich de arriba, terminamos
            break

    return cola_estudiantes.tamanio()  # Devuelve el número de estudiantes que no pudieron comer


# Ejemplo de uso
sandwiches = [1, 1, 0, 1, 0, 1]
alumnos = [0, 1, 0, 1, 0, 1]
resultado = num_students_unable_to_eat(sandwiches, alumnos)
print("Número de estudiantes que no pudieron comer:", resultado)

