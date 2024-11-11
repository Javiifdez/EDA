class Pila:
     def __init__(self):#funcion constructura
         self.contenido=[]
         self.contador=0#es un atributo de la clase

     def tamanio(self):#es un metodo de la clase Pila
          return len(self.contenido)
        
     def apilar(self,valor):
          self.contenido.append(valor)
          self.contador+=1

     def desapilar(self):
         self.contador -=1
         return self.contenido.pop()

     def cima(self):
          return self.contenido[-1]
     
if __name__ == "__main__":
     pila = Pila()
     
     pila.apilar(9)
     pila.apilar(8)
     print(pila.cima())
     print(pila.desapilar())

