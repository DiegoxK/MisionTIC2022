# Ejercicios

# 15. Leer un número entero y determinar si es múltiplo de 7. 
 
#Algoritmo:
"""
-Ingresar el numero 
-Comparar con el modulo del numero si el resultado es = 0
    si el resultado es = 0
        imprimir("El numero es multiplo de 7")
    sino
        imprimir("el numero no es multiplo de 7")


"""
#Resultado esperado:
"""
Input = 406

Output = "El numero es multiplo de 7"

---------------------------------------------------------------
Input = 408

Output = "El numero no es multiplo de 7"
---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def seven_multiple():
    number = int(input("Enter a number: "))
    if number%7 == 0:
        print("This number is multiple of seven")
    else:
        print("This number is not multiple of seven")
seven_multiple()