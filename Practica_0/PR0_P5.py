

'''
PRÁCTICA 0 - Estructura de Datos y Algoritmos IM. Curso 24/25
- AUTOR: Javier Fernandez Merono
- EJERCICIO: 5
- EXPLICACIONES: Comenzamos defieniendo las funciones pedidas.
                La funcion "leer" habre el archivo en modo leer y va recorriendo e imprimiendo cada linea
                por eso (linea,end=""), que hace que cada letra en vez de imprimirla en un salto de linea lo haga 
                seguido.

                Respecto a la segunda funcionalidad, el programa inicia pidiendo la cadena a buscar al usuario.
                Después abre el archivo en modo lectura y almacena cada linea del archivo en la variable "lineas",
                gracias a la funcion readlines() que devuelve una lista con cada line.El siguiente bucle for va incrementado
                dos valores por cada iteración, la linea y el numero de linea, que empieza en 1.
                Continua diviediendo cada linea en palabras,
                con la funcion split() y almacena una lista con cada palabra. Si la palabra se encuentra en esta
                ultima lista, imprimira la linea donde aparece y el numero de la linea, y seguira 
                recorriendo el archivo buscando mas veces la palabra hasta el fin del archivo.
'''

def leer(nombre_archivo):
    try:
        with open(nombre_archivo,'r') as archivo:
            for letra in archivo:
                print(letra,end='')
        print("\n--------FIN--------")
    except FileNotFoundError:
        print("Archivo no encontrado")


def buscar(archivo):

    palabra_buscada= input("¿Qué palabra quieres buscar?:")
    try:
    # Función para buscar una palabra en un archivo y mostrar en qué líneas aparece

        with open(archivo, 'r') as f:
            lineas = f.readlines()
        
        # Recorrer cada línea y buscar la palabra
        for numero_linea, linea in enumerate(lineas, start=1):
            # Dividir la línea en palabras
            palabras = linea.split()
            
            # Verificar si la palabra buscada está en la lista de palabras de la línea
            if palabra_buscada in palabras:
                print(f"La palabra '{palabra_buscada}' se encuentra en la línea {numero_linea}: {linea.strip()}")
                    

    except FileNotFoundError:
        print("Archivo no encontrado")

if __name__ == "__main__":
    archivo="archivo.txt"
    leer(archivo)
    buscar(archivo)

