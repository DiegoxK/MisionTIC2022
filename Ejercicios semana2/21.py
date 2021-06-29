# Ejercicios

#21. Hacer un programa que pida al usuario las tres notas de un alumno (deben estar entre 0 y 
#5 y pueden tener decimales) y calcule el promedio e indique mediante un mensaje si aprobó 
#o no (aprueba con nota mayor a 3). Se debe validar que las notas introducidas estén dentro 
#del rango permitido
 
#Algoritmo:
"""
-ingresar la cantidad de notas
-Calcular el promedio de notas
    si el promedio es >=3
        imprimir (El estudiante aprobó)
    si el promedio es <3
        imprimir (Ek estudiante no aproó)

"""
#Resultado esperado:
"""
Input1 = 2.1
Input2 = 3.2
Input3 = 4.7

Output = 3.3

---------------------------------------------------------------
Input = 
---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def average():
    note1=float(input("Enter the first student note: "))
    note2=float(input("Enter the second student note: "))
    note3=float(input("Enter the thrid student note: "))

    average = (note1+note2+note3)/3
    print(average)

average()