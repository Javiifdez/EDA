
'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 2 – Ordenación y Búsqueda. Tablas Hash. Caches LRU
AUTORES:
- David Sanz Fuertes
- Javier Fernandez Meroño
EJERCICIO: 01
EXPLICACIONES:
(id_pieza, precio, unidades, nombre_pieza).
o Crear una lista de objetos Pieza mediante un script. Deben generarse
datos aleatorios, extensos (1000 piezas) y variados.


'''

class Pieza:

    def __init__(self,pieza,precio,unidades,nombre) -> None:
        self.id_pieza = pieza
        self.precio = precio
        self.unidades = unidades
        self.nombre = nombre

def seleccion(lista:list):
    tamanio = len(lista)
    aux2 = 0
    #comparamos el primer elemento con todos los demas
    seleccionado = 0 #indice que queremos ordenar
    while seleccionado != tamanio: 
        aux1 = lista[seleccionado]      
        for i in range(seleccionado+1,tamanio):
            
            if lista[seleccionado] > lista[i]:#el pivote es mayor que el comparado
                #sustituimos el valor menor en el indice que estamos comparando
                aux1 = lista[seleccionado]
                lista[seleccionado] = lista[i]#el elemento menor ahora es el nuevo pivote    
                lista[i] = aux1 #sustituimos el antiguo pivote
                         
        seleccionado += 1
    return lista

if __name__ == "__main__":
    lista=[2,5,3,1]
    print(seleccion(lista))