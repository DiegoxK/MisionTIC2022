# Ejercicios

# Problema #1:
# Utilizar la función incorporada map() para crear una función que retorne una lista con la 
# longitud de cada palabra (separadas por espacios) de una frase. La función recibe una cadena 
# de texto y retornará una lista

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

sntnce = input('Enter a sentence: ')

lista = list(map(len, sntnce.split()))

print(lista)

def longitud_palabras(frase): # Función

    palabra_len = list(map(len, frase.split())) # Longitud de cada palabra
    return palabra_len # Retornar resultado

print(longitud_palabras('Hola Luis, como estas?')) # Prueba de la función