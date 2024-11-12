
class Nodo:
    #contructor
    def __init__(self,valor):#le pasamos un valor al nombre
        self.valor = valor
        self.sig = None

class Lista_Enlazada():
    #contructor
    def __init__(self) -> None:#crear lista vacia
        self.primero = None
        self.ultimo = None
        self.tamanio = 0

    #método para imprimir
    def __str__(self):
        string = ""
        aux = self.primero  # variable aux para ir recorriendo los nodos
        while aux is not None:
            string += str(aux.valor) + " -> "
            aux = aux.sig
        string += "None"
        return string

    #insertar
    def insertar_principio(self,valor) -> None:
        nuevo = Nodo(valor)
        if self.tamanio == 0:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            #es importante el orden para no hacer leaks de memoria
            nuevo.sig = self.primero
            #si lo hacemos al reves el que estaba primero pierde su puntero
            self.primero = nuevo
        self.tamanio +=1

    #insertar por la derecha
    def insertar_final(self,valor) -> None:
        nuevo = Nodo(valor)
        if self.tamanio == 0:
            self.primero = nuevo
            self.ultimo = nuevo
     
        else:
            #el siguiente al que antes era el ultimo es ahora el nuevo
            #es importante el orden para no perder el puntero del que antes era el ultimo 
            # de otra forma no podemos referirnos al siguiente de ese nodo
            self.ultimo.sig = nuevo
            self.ultimo = nuevo
        self.tamanio +=1

    #insertar en una posicion en particular
    def insertar_en_posicion(self,valor,indice):

        if self.tamanio < indice:
            print("Indice fuera de rango")
            print(f"El tamaño de la lista es {self.tamanio}")
            return

        if (self.esVacia() or indice <= 0):#si la lista es vacia se inserta igualmente
            #aprovechamos el if para insetar al principio
            self.insertar_principio(valor)

        #si el indice es el del tamaño se inserta a la derecha
        elif (self.tamanio == indice):
            self.insertar_final(valor)

        else:
            aux = self.primero
            contador = 0
            nuevo = Nodo(valor)
            #se para en el nodo del indice
            while contador < indice - 1:
                aux = aux.sig
                contador += 1
            nuevo.sig = aux.sig
            aux.sig = nuevo
            self.tamanio += 1

    #borrar el valor (indice) empezando a contar por la izquierda
    def eliminar_izq(self,indice):
        
        aux = self.primero
        contador = 1
        #lista vacia
        if self.primero == None:
            print("La lista es vacia")
            return
        
        if self.tamanio < indice:
            print("Indice fuera de rango")
            print(f"El tamaño de la lista es {self.tamanio}")
            return

        if indice == 1:
            self.primero = aux.sig
        
        else:
            #se para en el anterior al que queremos eliminar
            while aux is not None and contador < indice - 1:
                aux = aux.sig
                contador += 1
        
        # Si aux es None o aux.sig es None, índice es mayor que la longitud de la lista
        if aux is None or aux.sig is None :
            print("Indice fuera de rango")
            return  # índice fuera de rango

        #en el caso en que se quiera eliminar el ultimo elmento , el siguiente tomara como None su siguiente
        aux.sig = aux.sig.sig
        self.tamanio-=1

    #borrar el valor (indice) empezando a contar por la derecha
    def eliminar_dcha(self,indice):
        #comprobamos si esta dentro del rango
        if self.tamanio < indice:
            print("Indice fuera de rango")
            print(f"El tamaño de la lista es {self.tamanio}")
            return
        indice_izq =self.tamanio - indice +1
        self.eliminar_izq(indice_izq)

    #consultar valor en la posicion........
    def consultar_por_indice(self,indice):
        aux = self.primero
        if indice >= self.tamanio:
            return self.ultimo.valor

        elif indice <=0:
            return self.primero.valor

        else:
            aux = self.primero
            contador = 0
            #se para en el nodo del indice
            while contador < indice:
                aux = aux.sig
                contador += 1

            return aux.valor

    #es vacia?
    def esVacia(self) -> bool:
        return self.tamanio == 0

    #tamaño de la lista
    def cantidad(self) -> int:
        return self.tamanio

#TO-DO
#CONSULTAR, IZQ, DCHA, VALOR DE POSICION...
#pensar la parte de while not... de eliminar izq
    
if __name__ == '__main__':
    lista = Lista_Enlazada()
    lista.insertar_principio(2)
    lista.insertar_final(3)
    lista.insertar_final(8)
    print(lista)
    lista.insertar_en_posicion(1,1)
    print(lista)
    print(lista.consultar_por_indice(4))
