# Ejercicios

# 11. Leer tres números enteros de dos dígitos cada uno y determinar en cuál de ellos se encuentra el mayor dígito.
 
#Algoritmo:
"""
-Ingresar los 3 numeros
-Comparar los digitos de cada numero y determinar cual es mayor
    Si el primer digito del primer numero es el mayor
        imprimir (el primer digito del primer numero es el mayo)
    sinosi el segundo digito del primer numero es el mayor
        imprimir (el segundo digito del primer numero es el mayor)
    
    Sinosi el primer digito del segundo numero es el mayor
        imprimir (el primer digito del segundo numero es el mayo)
    sinosi el segundo digito del primer numero es el mayor
        imprimir (el segundo digito del segundo numero es el mayor)
    
    Sinosi el primer digito del tercer numero es el mayor
        imprimir (el primer digito del tercer numero es el mayo)
    sinosi el segundo digito del tercer numero es el mayor
        imprimir (el segundo digito del tercer numero es el mayor)
 
 
 
"""
#Resultado esperado:
"""
Input = 12 23 45

Output = el segundo digito del tercer numero es el mayor

---------------------------------------------------------------
Input = 45 23 12

Output = el segundo digito del primer numero es el mayor

---------------------------------------------------------------
Input = 23 54 12

Output = el primer digito del segundo numero es el mayor

---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def greater_number():
    number1 = input("Enter two-digit number: ")
    number2 = input("Enter two-digit number: ")
    number3 = input("Enter two-digit number: ")

    if int(number1[0]) > int(number1[1]) and int(number1[0]) > int(number2[0]) and int(number1[0]) > int(number2[1]) and int(number1[0]) > int(number3[0]) and int(number1[0]) > int(number3[1]):
        print("The firts digit of the first number is the grater")
    elif int(number1[1]) > int(number1[0]) and int(number1[1]) > int(number2[0]) and int(number1[1]) > int(number2[1]) and int(number1[1]) > int(number3[0]) and int(number1[1]) > int(number3[1]):
        print("The second digit of the first number is the grater")
    
    elif int(number2[0]) > int(number1[0]) and int(number2[0]) > int(number1[1]) and int(number2[0]) > int(number2[1]) and int(number2[0]) > int(number3[0]) and int(number2[0]) > int(number3[1]):
        print("The first digit of the second number is the grater")
    elif int(number2[1]) > int(number1[0]) and int(number2[1]) > int(number1[1]) and int(number2[1]) > int(number2[0]) and int(number2[1]) > int(number3[0]) and int(number2[1]) > int(number3[1]):
        print("The second digit of the second number is the grater")
    
    elif int(number3[0]) > int(number1[0]) and int(number3[0]) > int(number1[1]) and int(number3[0]) > int(number2[0]) and int(number3[0]) > int(number2[1]) and int(number3[0]) > int(number3[1]):
        print("The first digit of the thrid number is the grater")
    elif int(number3[1]) > int(number1[0]) and int(number3[1]) > int(number1[1]) and int(number3[1]) >int( number2[0]) and int(number3[1]) > int(number2[1]) and int(number3[1]) > int(number3[0]):
        print("The second digit of the thrid number is the grater")


greater_number()