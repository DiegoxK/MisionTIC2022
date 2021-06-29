# Ejercicios

# 15. Se cuenta con la siguiente información:
# Las edades de 5 estudiantes del turno mañana.
# Las edades de 6 estudiantes del turno tarde.
# Las edades de 11 estudiantes del turno noche.
# Las edades de cada estudiante deben ingresarse por teclado.
# a) Obtener el promedio de las edades de cada turno (tres promedios)
# b) Imprimir dichos promedios (promedio de cada turno)
# c) Mostrar por pantalla un mensaje que indique cuál de los tres turnos tiene un promedio 
# de edades mayor.
 
#Algoritmo:
"""
Ingresar las edades de los estudiantes
aplicar el promedio
    mostrar en pantalla los 3 promedios y un mensaje indicando cual tiene un promedio de edades mayor

"""
#Resultado esperado:
"""
---------------------------------------------------------------

Input = 
Output = 

---------------------------------------------------------------



---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:
from functools import reduce

def mean():

    m = input('Enter the five students age from the morning turn (Separated by spacing): ').split()
    m_list = [int(x) for x in m]
    m_mean = reduce(lambda accumulator, x: accumulator + int(x), m_list)/len(m_list)
    eve = input('Enter the five students age from the afternoon turn (Separated by spacing): ').split()
    eve_list =[int(x) for x in eve]
    eve_mean = reduce(lambda accumulator, x: accumulator + int(x), eve_list)/len(eve_list)
    night = input('Enter the five students age from the night turn (Separated by spacing): ').split()
    night_list = [int(x) for x in night]
    night_mean = reduce(lambda accumulator, x: accumulator + int(x), night_list)/len(night_list)

    print('The mean of the stundents from the morning turn is: ({})\nThe mean of the stundents from the afternoon turn is: ({})\nThe mean of the stundents from the night turn is: ({})'.format(m_mean,eve_mean,night_mean))

    if m_mean > eve_mean and m_mean > night_mean:
        print('The higher mean is from the morning turn')
    elif eve_mean > m_mean and eve_mean > night_mean:
        print('The higher mean is from the afternoon turn')
    elif night_mean > m_mean and night_mean > eve_mean:
        print('The higher mean is from the night turn')
    elif len(set([m_mean,eve_mean,night_mean])) == 1:
        print("The three means are the same")
    elif len(set([m_mean,eve_mean,night_mean])) == 2:
        print("Two means are the higher")


mean()