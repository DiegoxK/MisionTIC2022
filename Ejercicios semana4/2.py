# Ejercicios

# Problema #2:
# Crear una función que tome una lista de dígitos y devuelva al número al que corresponden. 
# Por ejemplo [1,2,3] corresponde a el número ciento veintitrés (123). Utilizar la función 
# reduce.

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

numbers = [1,2,3]
number = reduce(lambda x,y: str(x)+str(y), numbers)
print(int(number))


def digitos_a_numero(digitos):
    return reduce(lambda x,y:x*10 + y,digitos)
print(digitos_a_numero([1,2,3]))