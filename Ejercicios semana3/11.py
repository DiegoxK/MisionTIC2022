# Ejercicios

#11. Confeccionar un programa que permita ingresar un valor del 1 al 10 y nos muestre la
#tabla de multiplicar del mismo (los primeros 12 términos)
#Ejemplo: Si ingreso 3 deberá aparecer en pantalla los valores 3, 6, 9, hasta el 36.

 
#Algoritmo:
"""


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

def multiplicationtable():
    
    number = int(input("Enter a number: "))
    list = []
    total = 0
    for x in range(1, 13):
        total += number
        list.append(total)
    print("The table of {} is:".format(number))
    for x in range(12):
        print("{} x {} = {}".format(number,x+1,list[x]))

multiplicationtable()