# Ejercicios

#23. Diseñe una calculadora que sume, reste, multiplique y divida, la cual le pida al usuario 
#mediante input el valor del primer número, el valor del segundo número y la operación a 
#realizar, hay que tener en cuenta la validación de los valores de entrada,
 
#Algoritmo:
"""
-ingresar como input los numeros a sumar y como se van a operar
    si el input es una letra
        imprimir (Ingrese un valor numerico)
    si el input de operacion es = suma
        imprimir (El resultado de la suma entre () y () es: ())
    si el input de operacion es = resta
        imprimir (El resultado de la resta entre () y () es: ())
    si el input de operacion es = mult
        imprimir (El resultado de la multiplicacion entre () y () es: ())
    si el input de operacion es = div
        si el segundo input es = 0
            imprimir (No se puede dividir entre 0)
        sino
            imprimir (El resultado de la division entre () y () es: ())
    
"""
#Resultado esperado:
"""
---------------------------------------------------------------

Input1 = 1
Input1 = 1
Input1 = sum

Output = El resultado de la suma entre (1) y (1) es: (2)

---------------------------------------------------------------

Input1 = 3
Input1 = 2
Input1 = mult

Output = El resultado de la multiplicacion entre (3) y (2) es: (6)
---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def calculator():
    try:
        number1 = int(input("Enter the first value: "))
        number2 = int(input("Enter the second value: "))
        operation = input("Enter the operation you want to realize: ")

        if operation == "sum":
            sum = number1 + number2
            print("The result of the sum betwen ({}) and ({}) is ({}):".format(number1,number2,sum))
        if operation == "sub":
            subtraction = number1 - number2
            print("The result of the substraction betwen ({}) and ({}) is ({}):".format(number1,number2,subtraction))
        if operation == "mult":
            multiplication = number1 * number2
            print("The result of the multiplication betwen ({}) and ({}) is ({}):".format(number1,number2,multiplication))
        if operation == "div":
            if number2 == 0:
                print("Can not divide by 0!")
            else:
                division = number1 / number2
                print("The result of the division betwen ({}) and ({}) is ({}):".format(number1,number2,division))
    except:
        print("Enter a numeric value!")
        calculator()

calculator()