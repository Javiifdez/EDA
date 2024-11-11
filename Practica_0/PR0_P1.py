'''
PRÁCTICA 0 - Estructura de Datos y Algoritmos IM. Curso 24/25
- AUTOR: Javier Fernandez Meroño
- EJERCICIO: 1
- EXPLICACIONES: Comenzamos definiendo las funciones pedida por el enunciado. 
En primer lugar se le pide al usuario la contraseña, mientras el usuario la introduzca mal , la función
retornara el booleano False, por lo tanto se volverá a repetir el bucle while.

A continuación se da paso a la primera funcionalidad donde se le pide al usuario su edad, se le pide por teclado y se 
convierte la entrada a entero, para poder operar con esta variable. Si la edad es mayor o igual a 18 sera mayor de edad de lo contrario entrara
en el if y se le imprimirá que es menor de edad.

La siguiente funcionalidad pide al usuario su altura y convierte la variable a flotante, s esto no es posible, salta al except y se le vuelve a 
pedir su altura. Si la altura es valida y es mayor a 1.7 , se imprimirá por pantalla que el usuario es alto de lo contrario, se 
imprimirá que es promedio

La última función pide al usuario su año de nacimiento y calcula teniendo en cuanta que estamos
 en 2024 su edad. Si esta es menor de 30 años se imprimirá que es menor a 30 años de lo contrario 
 se imprimirá que es mayor.

'''


def contrasena():
    contrasena=input("Escriba la contraseña por favor:")
    if contrasena== 'python123':
        print('Contraseña correcta')
        return True
    else:
        print('Contraseña incorrecta:')
        return False

def mayor_edad():
     edad= int(input("Dime tu edad:"))
     if edad< 18:
          print("Eres menor de edad")
     else:
          print("Eres mayor de edad")


def ingresar_altura():
    exit=0

    while exit ==0:
        try:
            altura=float(input("Ingrese su altura:"))


        except ValueError:
            print("Introduzca una altura posible:")
            exit= 0

        if altura<=1.7:
                print("Eres de estatura promedio")
        else:
                print("Eres alto") 
        exit= 1

def calcular_edad():
     anio= int(input("Dime tu año de nacimiento:"))
     edad= 2024- anio
     if edad < 30:
         print("Es menor a 30 años")
     else:
         print("Es mayor a 30 años")

if __name__ == '__main__':
   
    validado =False
    while validado == False:
        validado = contrasena()

    mayor_edad()
    ingresar_altura()
    calcular_edad()

     



