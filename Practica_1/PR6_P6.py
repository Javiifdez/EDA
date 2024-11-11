'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 1 – TAD (Clases) Conjunto, Pila, Cola y Lista
AUTORES:
- Javier Fernandez Meroño
- David Sanz Fuertes
EJERCICIO: 5
EXPLICACIONES:

Codificar una función que reciba dos listas enlazadas (TAD desarrollado
PR1_P1) ordenadas como entrada y que devuelva una nueva lista que las
fusione en una lista enlazada también ordenada

'''

from PR1_P1 import Nodo , Lista_Enlazada

#definimos la funcion
def ordenar(lista1:Lista_Enlazada, lista2:Lista_Enlazada):
    lista_resultado = Lista_Enlazada()
#recorremos ambas listas y vamos comparando
    aux1 = lista1.primero #puntero que recorrerá la lista1
    aux2 = lista2.primero #puntero que recorrerá la lista2

    cantidad1 = lista1.cantidad()
    cantidad2 = lista2.cantidad()

#vamos comparando cada element0 de la lista y añadiendolos a la lista resultado
    
    while  cantidad1 != 0 and cantidad2 != 0: #paramos cuando llegamos al final de una lista 
        if aux1.valor <= aux2.valor:
            lista_resultado.insertar_final(aux1.valor)
            aux1 = aux1.sig #avanzamos el puntero   
            cantidad1 -= 1
            #print(lista_resultado) 
        else:
            lista_resultado.insertar_final(aux2.valor)
            aux2 = aux2.sig
            cantidad2 -= 1
#una vez hemos recorrido una lista, los valores que quedan en la otra, ya estan ordenador
    if cantidad1 == 0: #hemos acabado la lista1
        while cantidad2 != 0 :
            lista_resultado.insertar_final(aux2.valor)
            aux2 = aux2.sig
            cantidad2 -= 1
    else:
        while cantidad1 != 0 :
            lista_resultado.insertar_final(aux1.valor)
            aux1 = aux1.sig
            cantidad1 -= 1

    return lista_resultado

if __name__ == "__main__":
    lista1 = Lista_Enlazada()
    lista2 = Lista_Enlazada()
    lista1.insertar_principio(2)
    lista1.insertar_final(3)
    lista1.insertar_final(8)

    lista2.insertar_final(1)
    lista2.insertar_final(4)
    lista2.insertar_final(5)

    print(ordenar(lista1,lista2))


