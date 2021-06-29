# Ejercicios

# 3.Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.
 
#Algoritmo:
"""
-Ingresar el numero en forma de string

-Extraer el primer y segundo digito segun su indice

    -Si el modulo del primer y segundo digito = 0
        Imprimir(Estos numeros son par)
    -Sinosi el modulo del primer digito es = 0 pero no el segundo
        Imprimir(Solo el primer numero es par)
    sinosi el modulo del segundo digito es = 0 pero no el primero
        imprimir(Solo el segundo numero es par)
    sinosi el modulo de ambos numeros es distinto de 0
        imprimir(Ambos numeros son impares)

"""
#Resultado esperado:
"""
Input = 24
Estos numeros son par
---------------------------------------------------------------

Input = 23
Output = Solo el primer numero es par
---------------------------------------------------------------

Input = 32
Output = Solo el segundo numero es par
---------------------------------------------------------------

Input = 35
Output = Ambos numeros son impares
---------------------------------------------------------------

"""
#Transcripcion y verificacion del resultado:

def even_odd_numbers():
    number = input("Enter a two digit integer: ") 
    digits = [number[0], number[1]]
    module = [int(digits[0])%2, int(digits[1])%2]

    if module[0] == 0 and module[1] == 0:
        print("This numbers are even")
    elif module[0] == 0 and module[1] > 0:
        print("Only the first digit is even")
    elif module[0] > 0 and module[1] == 0:
        print("Only the second digit is even")
    elif module[0] > 0 and module[1] > 0:
        print("Both numbers are odd")

even_odd_numbers()