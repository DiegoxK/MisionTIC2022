# Ejercicios

#9. Desarrollar un programa que solicite la carga de 10 números e imprima la suma de los
#últimos 5 valores ingresados.

 
#Algoritmo:
"""
-Escriba el numero n de triangulos que desea ingresar
-Escribir la base y altura separados por un espacio
    multiplicar ambos valores y dividirlos por 2
    

"""
#Resultado esperado:
"""
---------------------------------------------------------------

Input1 =


Output = 

---------------------------------------------------------------



---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def sum():
    total = 0
    for x in range(1, 11):
        number = int(input("Enter a number: "))
        if x >= 5:
            total += number
    print(total)

sum()