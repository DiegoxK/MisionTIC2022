# Ejercicios

#.9 Leer un número entero de tres dígitos y determinar en qué posición está el mayor dígito
 
#Algoritmo:
"""
-Ingresar el numero
-Hallar el indice de los digitos en cada numero
-comparar los indices
    si el primer digito es el mayor
        imprimir(el primer digito es el mayor)
    sinosi el segundo es el mayor
        imprimir(el segundo digito es el mayor)
    sino
        imprimir(el tercer digito es el mayor)
 
"""
#Resultado esperado:
"""
Input = 123
Output = el tercer digito es el mayor
---------------------------------------------------------------
Input = 231
Output = el segundo digito es el mayor
---------------------------------------------------------------
Input = 321
Output = el primer digito es el mayor

"""
#Transcripcion y verificacion del resultado:

input_number = input("Number1: ")

if input_number[0] > input_number[1] and input_number[0] > input_number[2]:
    print("El primer digito ({}) es mayor que el segundo ({}) y el tercer ({}) digito".format(input_number[0],input_number[1],input_number[2]))
elif input_number[1] > input_number[0] and input_number[1] > input_number[2]:
    print("El segundo digito ({}) es mayor que el primer ({}) y el tercer ({}) digito".format(input_number[1],input_number[0],input_number[2]))
elif input_number[2] > input_number[0] and input_number[2] > input_number[1]:
    print("El tercer digito ({}) es mayor que el segundo ({}) y el primer ({}) digito".format(input_number[2],input_number[1],input_number[0]))
