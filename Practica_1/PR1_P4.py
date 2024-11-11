'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 1 – TAD (Clases) Conjunto, Pila, Cola y Lista
AUTORES:
- Javier Fernandez Meroño
- David Sanz Fuertes
EJERCICIO: 4
EXPLICACIONES:

'''

from PR1_P1 import Nodo, Lista_Enlazada

def  mitad(lista):
    #declaramos dos variables que recorreran la lista
    aux = lista.primero
    aux2= lista.primero
    #recorremos la lista hasta que una llegue al final
    while aux != lista.ultimo and aux.sig != lista.ultimo : #si no verificamos que aux.sig es el ultimo, da error si esta en la penultima pos
        aux = aux.sig.sig
        aux2 = aux2.sig
    #si la auxiliar esta en el penultimo aumentamos en uno el otro puntero
    if aux.sig == lista.ultimo:
        aux2 = aux2.sig
    #el nodo donde este la variable que no esta en el final sera la que este en la mitad
    return aux2.valor#tambien se podria llamar al metodo de consultar en esa pos, abria q añadir un contador


if __name__ == '__main__':
    lista = Lista_Enlazada()
    lista.insertar_principio(2)
    lista.insertar_final(3)
    lista.insertar_final(4)
    lista.insertar_final(8)
    lista.insertar_final(0)
    lista.insertar_final(1)
    print(lista)
    print(mitad(lista))





