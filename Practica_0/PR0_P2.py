

'''
PRÁCTICA 0 - Estructura de Datos y Algoritmos IM. Curso 24/25
- AUTOR: Javier Fernandez Merono
- EJERCICIO: 2
- EXPLICACIONES: El programa comienza definiendo las funciones de cada funcionalidad pedida.
En la primera función se  pasa la frase pedida al usuario a minusculas para que no sea sensible a mayus o minus, 
y va recorriendo la frase en busca de las vocales, si la encuentra el  contador se incrementa.

La siguiente función utiliza las funciones max() y min() para buscar el máximo y mínimo y los devuelve

La siguiente funcionalidad convierte la lista en un grupo, para que se borren los número repetidos, porque
en un grupo no pueden haber números repetidos, y vuelva a pasarla a lista, esta vez sin duplicados.

En la función para invertir el orden de la lista, se crea una nueva lista vacia. Se recorre la lista
empezando por el final: por ejemplo para len(lista)=3 ,si i=1, se añadirá lista[3-1-1], es decir, lista[2], que es el ultimo elem. de la lista
se irá incrementando la resta segun se itere el bucle for. Por cada iteración se añadirá la letra a la lista inicializada anteriormente.

La última funcion convierta la lista a tupla usando la  funcion (tuple). Esta nueva tupla tendrá sus valores inmutables, como
ocurre con todas las tuplas.
'''

#5
def contar_vocales(frase):

    vocales = ['a', 'e', 'i', 'o', 'u']
    contador=0
    frase=frase.lower() #pasamos la frase a minusculas para que no sea sensible a mayus o minus

    #recorremos la frase buscando las vocales
    for i in range(len(frase)):
        if frase[i] in vocales:
            contador+=1

    print(f" Las vocales de la frase son:{contador}")

#13
def max_y_min(nums):
    maximo= max(nums)#funciones que buscan el maximo y el minimo respectivamente
    minimo= min(nums)

    return maximo, minimo

#14
def numeros_duplicados(lista):
    conjunto=set(lista)#al transformar la lista en conjunto se eliminan los duplicados, por las
    #propiedades de los conjuntos
    return list(conjunto)
    
#15 
def invertir_lista(lista):
    longitud=len(lista)
    lista_inverta=[]#iniamos una lista vacia
    for i in range(longitud):
        lista_inverta.append(lista[longitud-(i+1)]) 

    return lista_inverta
    
#20
def convertir_lista_a_tupla(lista):
    tupla= tuple(lista)
    return tupla

if __name__ =="__main__":

    frase = input("Dame una frase: ")
    contar_vocales(frase)

    #El usuario debe introducir la logitud de la lista de numeros
    lista_numeros=[]
    i=int(input("De cuantos numeros quieres que sea la lista:"))
    #llenamos la lista con tantos numeros como haya introducido el usuario
    for num in range(i):
        nums= float(input("Dame un numero:"))
        lista_numeros.append(nums)


    resultado = max_y_min(lista_numeros)
    print(f"El maximo es {resultado[0]}, y el minimo el {resultado[1]}")

    sin_duplicados= numeros_duplicados(lista_numeros)
    print(f"La lista sin duplicados es: {sin_duplicados}")

    lista_invertida= invertir_lista(lista_numeros)
    print(f"La lista invertida es: {lista_invertida}")

    nueva_tupla= convertir_lista_a_tupla(lista_numeros)
    print(f"La lista ahora es de tipo {type(nueva_tupla)}")
