# Ejercicios

# 17 Leer un número entero de 4 dígitos y determinar si tiene mas dígitos pares o impares.  
 
#Algoritmo:
"""
-Ingresar el numero 
-revisar cada digito y ver si es par o impar
imprimir (El primer dijito es () El segundo digito es (), el tercer digito es () y el cuarto digito es ())


"""
#Resultado esperado:
"""
Input = 4164

Output = "El primer dijito es par El segundo digito es impar, el tercer digito es par y el cuarto digito es par"

---------------------------------------------------------------

---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def even_odd():
    number = input("Enter a four digit number: ")

    number1 = (int(number[0]))%2
    number2 = (int(number[1]))%2
    number3 = (int(number[2]))%2
    number4 = (int(number[3]))%2
    
    if number1 == 0:
        evenodd1 = "even"
    elif number1 > 0:
        evenodd1 = "odd"

    if number2 == 0:
        evenodd2 = "even"
    elif number2 > 0:
        evenodd2 = "odd"

    if number3 == 0:
        evenodd3 = "even"
    elif number3 > 0:
        evenodd3 = "odd"

    if number4 == 0:
        evenodd4 = "even"
    elif number4 > 0:
        evenodd4 = "odd"
    
    print("The first digit ({}) is {}, the second digit ({}) is {}, the third digit ({}) is {}, the four digit ({}) is {}".format(number[0],evenodd1,number[1],evenodd2,number[2],evenodd3,number[3],evenodd4,))

even_odd()