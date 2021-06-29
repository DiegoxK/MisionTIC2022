# Ejercicios

# 7. Leer dos números enteros y determinar cuál es el mayor
 
#Algoritmo:
"""
-Ingresar dos numeros en forma de string
-Comparar ambos numeros

    si el primer numero es mayor que el segundo
        imprimir(El primer numero es mayor que el segundo)
    sinosi el segundo numero es el mayor
        imprimir(El segundo numero es mayor que el primero)
    sino
        imprimir(Ambos numeros son el mismo)

 
"""
#Resultado esperado:
"""
Input = 32
El primer numero es mayor que el segundo
---------------------------------------------------------------
Input = 23
El segundo numero es mayor que el primero
---------------------------------------------------------------
Input = 33
Ambos numeros son el mismo

"""
#Transcripcion y verificacion del resultado:
input_number1 = input("Number: ")
input_number2 = input("Number: ")

if int(input_number1) > int(input_number2):
    print("The first number ({}) is greater than the second ({})".format(input_number1, input_number2))
elif int(input_number1) < int(input_number2):
    print("The second number ({}) is greater than the first ({})".format(input_number1, input_number2))
else:
    print("Both numbers are the same")
