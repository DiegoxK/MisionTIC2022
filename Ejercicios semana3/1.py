# Ejercicios

#1. Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos
#tienen notas mayores o iguales a 7 y cuántos menores.
 
#Algoritmo:
"""
-Ingresar la cantidad de notas
    para cada nota
        si las notas son > 7
            imprimir(() estudiantes sacaron 7 o mas )
    

"""
#Resultado esperado:
"""
---------------------------------------------------------------


---------------------------------------------------------------


---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def notes():

    list_of_notes1 = []
    list_of_notes2 = []
    for x in range(10):
        notes = int(input("Enter a note: "))
        if notes >= 7:
            list_of_notes1.append(notes)
        elif notes < 7:
            list_of_notes2.append(notes)

    print("{} stundents got 7 or more note".format(len(list_of_notes1)),list_of_notes1)
    print("{} stundents got 6 or lesss note".format(len(list_of_notes2)),list_of_notes2)

notes()