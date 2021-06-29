# Ejercicios

# 2.Leer un número entero y determinar si tiene 3 dígitos. 
 
#Algoritmo:
"""
-Ingresar el numero en forma de string
-Determinar la cantidad de digitos del string

    -Si cantidad de digitos = 3
        Imprimir(Este numero tiene 3 digitos)
    -Sino
        Imprimir(Este numero no tiene 3 digitos)
"""
#Resultado esperado:
"""
Input = 123
Output = Este numero tiene 3 digitos!
---------------------------------------------------------------

Input = 1235
Output = Este numero no tiene 3 digitos

"""
#Transcripcion y verificacion del resultado:

def digitcount():
    
    number = input("Ingrese un valor numerico: ")
    digits = len(number)

    if digits == 3:
        print("This number have three digits!")
    else:
        print("This numbres doesn't have three digits")

digitcount()
