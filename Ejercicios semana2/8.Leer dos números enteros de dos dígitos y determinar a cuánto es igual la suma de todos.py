# Ejercicios

#8. Leer dos números enteros de dos dígitos y determinar a cuánto es igual la suma de todos los dígitos
 
#Algoritmo:
"""
-Ingresar los numeros
-Hallar el indice de los digitos en cada numero
-Sumar los indices
 
"""
#Resultado esperado:
"""
Input = 32 + 12
Output = 8
---------------------------------------------------------------
Input = 23 + 45
Output = 14
---------------------------------------------------------------
Input = 33 + 10
Output =7

"""
#Transcripcion y verificacion del resultado:
def index_sum():
    input_number1 = input("Number1: ")
    input_number2 = input("Number2: ")

    print(int(input_number1[0])+int(input_number1[1])+int(input_number2[0])+int(input_number2[1]))

index_sum()