# Ejercicios

# Problema #3:
# Crear una función que retorne las palabras de una lista de palabras que comience con una 
# letra en específico. Utilizar la función filter

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
from functools import reduce

words = ['Perro', 'Gato', 'Pelota', 'Manzana', 'Libro', 'Python']
filt=list(filter(lambda x: x[0]=='P', words))
print(filt)

def filtro_palabras(lista_palabras, letra):
    return list(filter(lambda word:word[0]==letra,lista_palabras))
print(filtro_palabras(['Perro', 'Gato', 'Pelota', 'Manzana', 'Libro', 'Python'], 'P'))

