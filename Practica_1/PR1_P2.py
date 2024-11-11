'''
Estructura de Datos y Algoritmos | Ing. Matemática | Curso 24/25
PRÁCTICA 1 – TAD (Clases) Conjunto, Pila, Cola y Lista
AUTORES:
- Javier Fernandez Meroño
- David Sanz Fuertes
EJERCICIO: 2
EXPLICACIONES:

'''
def clasificacion_asignatutas(estudiante1,estudiante2):

    est1=list(estudiante1)
    est2=list(estudiante2)
    ambosAprobados = []
    soloPrimeroAprobado = []

    for asignatura in estudiante1:
        #ambos la han aprobado
        if asignatura in estudiante2:
            ambosAprobados.append(asignatura)
        #la ha aprobado el primero pero no el segundo
        else:
            soloPrimeroAprobado.append(asignatura)
    
    #asignaturas aprobadas
    alMenosUnAprobado = est1 + est2
    alMenosUnAprobado=set(alMenosUnAprobado)

    return ambosAprobados ,soloPrimeroAprobado ,alMenosUnAprobado


if __name__ == "__main__":
    #Introducimos las asignaturas que ha aprobado cada estudiante
    estudiante1 = {"Mates","Fisica","EDA","Lengua"}
    estudiante2 = {"Biologia","Ecuaciones Diferenciales","Mates","Fisica","Lengua"}
    #Vamos añadiendo las asignaturas a cada lista
    losDosAprobado, soloPrimero, AlmenosUno = clasificacion_asignatutas(estudiante1, estudiante2)
    #Imprimimos cada lista
    print(f"Ambos estudiantes han aprobado {losDosAprobado}")
    print(f"Solamente ha aprobado el primer estudiante {soloPrimero}")
    print(f"Al menos uno ha aprobado {AlmenosUno}")