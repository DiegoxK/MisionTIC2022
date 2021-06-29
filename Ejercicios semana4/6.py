# Ejercicios
"""
Problema #6:
Realizar una función que retorne el recuento de la cantidad de elementos en la lista cuyo 
valor es igual a su índice. Utilizar la función enumerate.

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

L = [0,2,2,1,5,5,6,10]
A = [x for x in enumerate(L) if x[0]==x[1]]
print(len(A))

def count_match_index(L):
    return len([num for count,num in enumerate(L) if num==count])
print(count_match_index([0,2,2,1,5,5,6,10]))