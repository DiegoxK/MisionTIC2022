# Ejercicios

# 4. leer un número entero de dos dígitos menor que 20 y determinar si es primo. 
 
#Algoritmo:
"""
-Ingresar el numero en forma de string

-¿El numero es menor que 20?
    Si
        -Determinar si el numero coincide con uno en una lista de primos

        Si el numero esta en = [2,3,5,7,11,13,17,19]
        imprimir(el numero el primo!)

        Sino
        imprimir(el numero no es primo)

    No
        imprimir(ingrese numeros menores a 20)   
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

def prime_finder():
    input_number = input("Enter a number less than twenty: ")
    number = int(input_number)
    list_of_primes = [2,3,5,7,11,13,17,19]
    if number > 20:
        prime_finder()
    elif number in list_of_primes:
        print("This is a prime number")
    else:
        print("This number is not a prime")
prime_finder()