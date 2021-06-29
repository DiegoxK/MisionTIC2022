# Ejercicios

# 16. Cargar una oración por teclado. Mostrar luego cuantos espacios en blanco se ingresaron. 
# Tener en cuenta que un espacio en blanco es igual a
# " ", en cambio una cadena vacía es ""

 
#Algoritmo:
"""
Ingresar el string
contar la cantidad de espacios

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

def sentence_string():

    sntce = input('Enter a sentence: ')
    spacings = sntce.count(' ')
    print('There are '+str(spacings)+' spacings')

sentence_string()