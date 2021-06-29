# Ejercicios

# 6.Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.
 
#Algoritmo:
"""
-Ingresar el numero en forma de string
-leer y comparar el indice de cada caracter
    si los caracteres son iguales
        imprimir(Los digitos de ambso numeros son el mismo)
    sino
        imprimir(los digitos son distintos)

"""
#Resultado esperado:
"""
Input = 44
Ambos numeros son iguales
---------------------------------------------------------------

Input = 45
Ambos numeros son los mismos

"""
#Transcripcion y verificacion del resultado:

input_number = input("Number: ")

if input_number[1] == input_number[0]:
    print("Both digits are the same")
else:
    print("Both digits are diferent")
