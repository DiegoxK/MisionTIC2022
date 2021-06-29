# Ejercicios

#19. A un trabajador le pagan según sus horas trabajadas por una tarifa de pago por hora. Si la 
#cantidad de horas trabajadas es mayor 40 horas. La tarifa se incrementa en un 50% para las 
#horas extras. Calcular el salario del trabajador dadas las horas trabajadas y la tarifa 
#ingresadas por el usuario.
 
#Algoritmo:
"""
-Ingresar la tarifa y las horas trabajadas

    si el numero de horas > 40 
        sumar el 50% a la tarifa y aplicar la nueva tarifa
        imprimir(El salario del trabajador es ())
    
    sino
        imprimir(El salario del trabajador es ())


"""
#Resultado esperado:
"""
Input = 20000
        50

Output = 1100000

---------------------------------------------------------------
Input = 20000
        40
Output = 800000
---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def salary():
    rate = int(input("Enter the daily rate: "))
    hours = int(input("Enter the hours of work: "))
    
    if hours > 40:
        salary = (rate*40) + ((rate + rate*0.5) * (hours-40))
        print("With a rate of ({}) per hour, your salary is: {}$".format(rate,salary))
    else:
        salary = (rate*hours)
        print("With a rate of ({}) per hour, your salary is: {}$".format(rate,salary))

salary()