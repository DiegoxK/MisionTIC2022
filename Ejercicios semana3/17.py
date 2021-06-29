# Ejercicios

# 17. Ingresar una oración que pueden tener letras tanto en mayúsculas como minúsculas. 
# Contar la cantidad de vocales. Crear un segundo string con toda la oración en minúsculas 
# para que sea más fácil disponer la condición que verifica que es una vocal.
 
#Algoritmo:
"""
Ingresar la oracion


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

def vowels():

    vocals = ['a','e','i','o','u']
    sntce = input('Enter the sentence: ').lower()
    total = 0

    for vocal in vocals:
        total += sntce.count(vocal)
    print('The total of vowels in the sentence are: '+str(total))
    
vowels()