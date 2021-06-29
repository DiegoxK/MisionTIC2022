# Ejercicios

# 12.  Leer un número entero menor que 50 y positivo y determinar si es un número primo.
 
#Algoritmo:
"""
-Ingresar el numero entero
-Comparar el numero en una lista de primos
    si el numero ensta en la lsita
        imprimir("El numero es un primo positivo")
    sino
        imprimir("El numero no es un primo")


"""
#Resultado esperado:
"""
Input = 17

Output = "El numero es un primo positivo"

---------------------------------------------------------------
Input = 18

Output = "El numero no es un primo positivo"
---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def prime():
    number = int(input("Enter a number minor than fifty: "))
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    
    if number > 50:
        prime()
    elif number in primes:
        print("The number is a positive prime!")
    else:
        print("The number is not a positive prime")

prime()