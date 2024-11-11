

"""
PRÁCTICA 0 - Estructura de Datos y Algoritmos IM. Curso 24/25
- AUTOR: Javier Fernandez Meroño
- EJERCICIO: 3           
- ACLARACIONES:Supongo que el enunciado se refiere con "aceptar" a que la función reciba los dos números y el operador,
                y esta le devuelva el resultado.

                He  echo una función por cada operación mas que nada para poder usar este mismo código en adelante.
                En el caso de que el enunciado se refiriera a que dentro de la función se pidiera al usuario tanto el operador como
                los números simplemente habría que introducir lo anterior a la función "calculadora" dentro de dicha función y dejarla asi
                calculadora().

- EXPLICACIONES:Como tal el programa en primer lugar pide al usuario un operador, proporcionándole cuales admite la calculadora, si el usuario
                introduce un operador diferente o bien no solamente dicho operador, por ejemplo "k+" o "-afsaf", le pide al usuario que lo 
                introduzca nuevamente. Continua pidiéndole al usuario los dos números a operar. Dando paso a la función 
                "calculadora", esta recibe los datos pedidos al usuario y dependiendo cual sea la variable operador, realizará una operación u
                otra. En cada caso se llamara a la función que realice dicha operación. la cual retornará el resultado. Por último se imprime
                la operación completa y su resultado en pantalla.

"""
from os import system   #biblioteca para usar la función os.system("cls")
#definimos las funciones de cada operación disponible

def suma(num1, num2):
    resultado= num1+num2
    return resultado

def resta(num1, num2):
    resultado=num1 - num2
    return resultado

def multiplicacion(num1, num2):
    resultado=num1 * num2
    return resultado

def division(num1, num2):
    resultado=num1 / num2
    return resultado

#función pedida en el enunciado
def calculadora(num1,num2,operador):

    if operador == "+" :
        resultado=suma(num1,num2)
        return resultado

    elif operador == "-":
        resultado=resta(num1,num2)
        return resultado

    elif operador == "*":
        resultado=multiplicacion(num1,num2)
        return resultado

    elif operador == "/":
        resultado=division(num1,num2)
        return resultado
    
if __name__ == "__main__":

    system('cls')#función para borrar las ejecuciones anteriores del terminal
    exit=0
    #el usuario debe introducir correctamente el operador
    while exit == 0:
        operador=input("Dame un operador (+,-,*,/):")
        if (operador !="+") and (operador !="-") and (operador !="*" ) and (operador !="/" ):
            print("Selecciona un operador disponible")
        else:
            exit=1

    num1=float(input("Dame un numero:"))
    num2=float(input("Dame otro numero:"))

    resultado=calculadora(num1,num2,operador)

    print(f"El resultado de {num1} {operador} {num2} = {resultado} ")
