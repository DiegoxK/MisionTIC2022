# Ejercicios

# 5. Leer un número entero de dos dígitos y determinar si es primo y además si es negativo. 
 
#Algoritmo:
"""
-Ingresar el numero en forma de string
-
       
"""
#Resultado esperado:
"""
Input = 2,3,5,7,11,13,17 o 19
Este numero es primo
---------------------------------------------------------------

Input = 21
ingrese numeros menores a 20

"""
#Transcripcion y verificacion del resultado:
input_number = input("Number: ")
number = int(input_number)
positive_list = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
negative_list = [-2,-3,-5,-7,-11,-13,-17,-19,-23,-29,-31,-37,-41,-43,-47,-53,-59,-61,-67,-71,-73,-79,-83,-89,-97]
if number > 0:
    print("The number is positive")
    if number in positive_list:
        print("and prime")
elif number <0:
    print("The number is negative" )
    if number in negative_list:
        print("and prime")