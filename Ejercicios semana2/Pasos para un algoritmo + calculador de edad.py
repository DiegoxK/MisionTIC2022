#Ejercicios
"""Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edada o no"""
#1. Objetivo: Identificar si el usuario es mayor de edad o no


#2. Algoritmo: Pseudocodigo / Diagrama de flujo
"""
Inicio
    Variable age = Integer type
        if (age>=18)
            Show "Eres mayor de edad"
        else
            Show "Es menor de edad"
        End_if
End
"""
#3 Prueba de escritorio (Resultado esperado)
"""
input: 17
output: "Es menor de edad"

input: 21
output: "Es mayor de edad"

"""

#4. Transcripcion, digitar, poner en marcha y verificar resultado


#--------------------------------------------------------------------------------------------------------------------------------

def Age_calculator():
    try:
        age = int(input("Ingrese por favor su edad "))
        
        if age>=18 and age<=150:
            print("Eres mayor de edad")
        elif age<=0:
            print("Edad invalida")
        elif age>150:
            print("._.")
        elif age>0 and age<18:
            print("Eres menor de edad")

    except:
        print("Enter a number")

Age_calculator()