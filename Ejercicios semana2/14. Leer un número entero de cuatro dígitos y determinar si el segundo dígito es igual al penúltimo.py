# Ejercicios

# 14. Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo.
 
#Algoritmo:
"""
-Ingresar el numero entero de 4 digitos
-Comparar el segundo y cuarto indice 
    si el segundo digito es igual al cuarto
        imprimir("El segundo y el cuarto digito son iguales")
    sino
        imprimir("El segundo y cuarto digito no son iguales")


"""
#Resultado esperado:
"""
Input = 1717

Output = "El segundo y el cuarto digito son iguales"

---------------------------------------------------------------
Input = 4567

Output = "El segundo y cuarto digito no son iguales"
---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def dsame():
    number = input("Enter a four digits number: ")
    if number[1] == number[3]:
        print("The second and fourth digits are the same!")
    else:
        print("The second and fourth digits aren't the same")

dsame()