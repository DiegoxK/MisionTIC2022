# Ejercicios

# 14. Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
# a) La cantidad de valores ingresados negativos.
# b) La cantidad de valores ingresados positivos.
# c) La cantidad de múltiplos de 15.
# d) El valor acumulado de los números ingresados que son pares.

 
#Algoritmo:
"""
Ingresar los 10 valores
Crear un diccionario con nuestros datos

"""
#Resultado esperado:
"""
---------------------------------------------------------------


Output = Se han ingresado (1) Elementos en el primer cuadrante, (1) En el segundo, (1) en el tercero y (1) en el cuarto

---------------------------------------------------------------



---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

from functools import reduce
import pandas as pd

def comparatives():

    data = {'negatives':0,'positives':0,'multiples':0}
    numbers = []
    for x in range(1,10+1):

        number = int(input("Enter a integer number : "))
        numbers.append(number)

        if number < 0:
            data['negatives'] +=1
            if number%15 == 0:
                data['multiples'] +=1

        elif number > 0:
            data['positives'] +=1
            if number%15 == 0:
                data['multiples'] +=1
        else:
            print('revise the digit')

    awasinpanela = filter(lambda x: x%2==0, numbers)
    data['acumulated_value'] = reduce(lambda acummulator, awaconpanela: acummulator + awaconpanela, awasinpanela)

    
    return data
    

print(comparatives())
