# Ejercicios
"""
Problema #5:
Realizar una función que tome una lista y retorne un diccionario que contenga los valores de 
la lista como clave y el índice como el valor. Utilizar la función enumerate.

"""
#Algoritmo:
"""

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

L = ['a','b','c','d','e']
A = {key:value for value,key in enumerate(L)}
print(A)

def d_list(L):
    return {key:value for value,key in enumerate(L)}
print(d_list(['a','b','c','d','e']))