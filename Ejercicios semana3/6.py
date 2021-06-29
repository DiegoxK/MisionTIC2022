# Ejercicios

#6. Realizar un programa que permita cargar dos listas de 15 valores cada una. Informar con
#un mensaje cuál de las dos listas tiene un valor acumulado mayor (mensajes "Lista 1
#mayor", "Lista 2 mayor", "Listas iguales")
 
#Algoritmo:
"""
-Ingresar los valores por input de ambas listas
-realizar 15 iteraciones y sumar los datos dentro de las listas
-comparar las listas
    si la lista 1 es mayor
        imprimir(La lista 1 es la mayor)
    si la lista 2 es mayor
        imprimir(la lista 2 es la mayor)
    si ambas listas tienen el mismo tamaño
        imprimir(ambas listas tienen el mismo tamaño)


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

def listsizes1():
    totallists = {"total1":0, "total2":0}
    list1 = []
    list2 = []

    for x in range(15):
        number1 = int(input("Enter the first list number: "))
        list1.append(number1)
        totallists["total1"] += number1
        number2 = int(input("Enter the second list number: "))
        totallists["total2"] += number2
        list2.append(number2)

    if totallists["total1"] > totallists["total2"]:
        print("The first ({}) list is higher that the second ({})".format(totallists["total1"],totallists["total2"]))
    elif totallists["total1"] < totallists["total2"]:
        print("The second list ({1}) is higher that the first one ({0})".format(totallists["total1"],totallists["total2"]))
    elif totallists["total1"] == totallists["total2"]:
        print("Both list are same ({}) = ({})".format(totallists["total1"],totallists["total2"]))

def listsizes2():

    totallists = {"total1":0, "total2":0}

    list1 = [12,43,56,7,9,5,32,12,4,6,7,8,1,3,5]
    list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    for x in range(15):

        totallists["total1"] += list1[x]
        totallists["total2"] += list2[x]

    if totallists["total1"] > totallists["total2"]:
        print("The first ({}) list is higher that the second ({})".format(totallists["total1"],totallists["total2"]))
    elif totallists["total1"] < totallists["total2"]:
        print("The second list ({1}) is higher that the first one ({0})".format(totallists["total1"],totallists["total2"]))
    elif totallists["total1"] == totallists["total2"]:
        print("Both list are same ({}) = ({})".format(totallists["total1"],totallists["total2"]))

