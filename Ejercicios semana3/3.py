# Ejercicios

#3. En una empresa trabajan n empleados cuyos sueldos oscilan entre $100 y $500, realizar
#un programa que lea los sueldos que cobra cada empleado e informe cuántos empleados
#cobran entre $100 y $300 y cuántos cobran más de $300. Además el programa deberá
#informar el importe que gasta la empresa en sueldos al personal.
 
#Algoritmo:
"""
-Ingresar el sueldo de los trabajadores
-ingresar los sueldos en una lista
    cuando el input sea == exit
        por cada dato en la lista
        si el dato es menor que 300 y mayor que 100
            guardarlo en otra lista
        si el dato es mayor o igual que 300 y menor que 500
            guardarlo en otra lista
        sumar cada saldo almacenado en la primera lista lista
        imprimir (importe)
        imprimir (cantidad de datos de todas las listas y datos respectivos)

"""
#Resultado esperado:
"""
---------------------------------------------------------------

Input1 = 100
input2 = 500
input3 = 400
input4 = 300

Output ="El importe fue de 1300$"
        "1 trabajadores cobran entre 100$ y 300$"
        "3 trabajadores cobran mas de 300$"

---------------------------------------------------------------



---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def salaryamount():

    lists = {"salaries":[],"list_a":[],"list_b":[]}
    amount = 0
    salary = input("Enter the salary, enter exit to finish: ")
    
    while salary != "exit":
        lists["salaries"].append(int(salary))
        amount += int(salary)
        salary = input("Enter the salary, enter exit to finish: ")

    for x in lists["salaries"]:
        if x >= 100 and x < 300:
            lists["list_a"].append(x)
        elif x >= 300 and x <= 500:
            lists["list_b"].append(x)

    print("The amount is {}".format(amount))
    print("{} workers get paid between 100$ and 300$".format(len(lists["list_a"])))
    print("{} workers get paid between 300$ and 500$".format(len(lists["list_b"])))

salaryamount()