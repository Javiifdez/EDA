#iniciamos las funcionalidades de la clase pila

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
     cadena_bien = "[()]"
     cadena_mal = "[(]])"
     pila= Pila()
     brackets={"}":"{", "]":"[", ")":"("}

     #1. Aplilar los parentesis en una pila siempre que sean de apertura
     for caracter in cadena_mal:
        if caracter in brackets.values():
             pila.apilar(caracter)

        if caracter in brackets.keys():
            if brackets[caracter] == pila.cima(): 
                pila.desapilar()
            else:
                break
                
     if pila.tamanio() == 0:
        print("La cadena está balanceada")
     else:
        print("La cadena no está balanceada")