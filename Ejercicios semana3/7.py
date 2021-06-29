# Ejercicios

#7. Desarrollar un programa que permita cargar n números enteros y luego nos informe
#cuántos valores fueron pares y cuántos impares.
#Emplear el operador “%” en la condición de la estructura condicional (este operador
#retorna el resto de la división de dos valores, por ejemplo 11%2 retorna un 1):
# if valor%2==0:
 
#Algoritmo:
"""
-ingresar valores hasta que se digite "Exit"
-filtrar los valores en 2 listas 
    si valor%2==0:
    agregar el valor a una lista de pares
    si valor%2 != 0:
    agregar el valor a una lista de impares
imprimir(() Valores son pares, () valores son impares)
"""
#Resultado esperado:
"""
---------------------------------------------------------------

Input1 = 13, 12 , 14


Output = (2) valores son pares, (1) valores son impares

---------------------------------------------------------------



---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def even_and_odd():

    lists = {"evenlist":[],"oddlist":[]}
    number = input("Enter a number, enter (exit) to finish: ")

    while number != "exit":
        
        if int(number)%2 == 0:
            lists["evenlist"].append(number)
        elif int(number)%2 != 0:
            lists["oddlist"].append(number)

        number = input("Enter a number, enter (exit) to finish: ")

    print("({}) values are even and ({}) values are odd!".format(len(lists["evenlist"]),len(lists["oddlist"])))
    
even_and_odd()