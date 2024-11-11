'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 1 – TAD (Clases) Conjunto, Pila, Cola y Lista
AUTORES:
- Javier Fernandez Meroño
- David Sanz Fuertes
EJERCICIO: 5
EXPLICACIONES:

'''
from PR1_P1 import Nodo, Lista_Enlazada

#definimos la funcion
def consultar_por_indice_dcha(lista: Lista_Enlazada,indice):
#comprobamos que el indice esta dentro del rango
    if lista.tamanio < indice:
        print("Indice fuera de rango")
        print(f"El tamaño de la lista es {lista.cantidad}")
        return
#ajustamos el indice para poder usar el metodo consultar en posicion
    indice_nuevo= lista.tamanio - indice 
#usamos este metodo para retornar el valor
    return lista.consultar_por_indice(indice_nuevo)

#pruebas
if __name__ == '__main__':
    
    lista = Lista_Enlazada()
    lista.insertar_principio(1)
    lista.insertar_final(2)
    lista.insertar_final(3)
    lista.insertar_final(4)
    lista.insertar_final(5)
    #lista.insertar_final(6)
    print(lista)
    #print(consultar_por_indice_dcha(lista,4))