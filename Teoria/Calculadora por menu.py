
"""""
PRÁCTICA 0 - Estructura de Datos y Algoritmos IM. Curso 24/25
- AUTOR: Javier Fernandez Meroño
- EJERCICIO: 3
- EXPLICACIONES:


Calculadora simple: Crea una función que simule una calculadora básica. La
función debe aceptar dos números y un operador (suma, resta, multiplicación
o división) y devolver el resultado.

"""
import os

#definimos las funciones de cada operacion disponible

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

if __name__ == "__main__":

    exit=0 #Variable de control para salir de la calculadora
    while exit != 1:

        os.system('cls')
        print("1)Suma \n2)Resta \n3)Multiplicacion \n4)Division \n5)Salir")
        opcion= int(input("Selecciona que operacion quieres realizar:"))

        if opcion == 1:
            num1=float(input("Dame un numero:"))
            num2=float(input("Dame otro numero:"))
            resultado=suma(num1,num2)
            print(f"El resultado de sumar {num1} + {num2}= {resultado}")

        elif opcion == 2:
            num1=float(input("Dame un numero:"))
            num2=float(input("Dame otro numero:"))
            resultado=resta(num1,num2)
            print(f"El resultado de restar {num1} - {num2}= {resultado}")

        elif opcion == 3:
            num1=float(input("Dame un multiplicando:"))
            num2=float(input("Dame su multiplicador:"))
            resultado=multiplicacion(num1,num2)
            print(f"El resultado de multiplicar {num1} * {num2}= {resultado}")

        elif opcion == 4:
            num1=int(input("Dame un dividendo:"))
            num2=int(input("Dame su divisor:"))
            resultado=division(num1,num2)
            print(f"El resultado de dividir {num1} / {num2}= {resultado}")
        
        else:
            print("Selecione una opcion posbile")

        print("\n¿Quieres salir de programa?")
        salida= int(input("1)Si \n2)No \nSelecione una opcion:"))
        if salida == 1:
            exit = 1

        
        