
'''
PRÁCTICA 0 - Estructura de Datos y Algoritmos IM. Curso 24/25
- AUTOR: Javier Fernandez Merono
- EJERCICIO: 4
- EXPLICACIONES: Comenzamos el programa importando la función sqrt para realizar la raíz cuadrada.
                A continuación creamos las funciones que manejan las excepciones correspondientes. Cuando 
                el usuario introduce un valor que genera un error, el programa salta al except, una vez dentro se abre un archivo.txt, de
                nombre"errores" en modo append "a" , es decir, añade al archivo la cadena que le digamos, en cada
                función se imprimirá el tipo de error que salga, una vez escrito, se le dirá al usuario que ha echo mal. 

'''
from math import sqrt #importamos solamente la función raíz cuadrada

def Division():
    try:
        dividendo= float(input("Dame el dividendo:"))
        divisor = float(input("Dame el divisor:"))
        cociente=dividendo / divisor
        return cociente
    except ZeroDivisionError:
        with open('errores.txt','a') as archivo:
            archivo.write('ZeroDivisionError:\n')
        return "El divisor tiene que ser distinto de 0"

def Raiz():
    try:
        num=float(input("Dame el radicando:"))
        resultado= sqrt(num)
        return resultado
    except ValueError:
        with open('errores.txt','a') as archivo:
            archivo.write('ValueError:\n')
        return "El radicando debe ser >=0"
        

def Conversion_cadena_entero():
    cadena=input("Dame un numero:")
    try:
        cadena=int(cadena)
        return cadena
    
    except ValueError:
        with open('errores.txt','a') as archivo:
            archivo.write('ValueError:\n')
        return "El numero no puede incluir letras"



if __name__ == "__main__":
    print(Raiz())
    print(Division())
    print(Conversion_cadena_entero())
    