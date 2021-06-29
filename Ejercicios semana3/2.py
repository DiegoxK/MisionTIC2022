# Ejercicios

#2. Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio
#de las personas.
 
#Algoritmo:
"""
-Ingresar la cantidad de alturas y almacenarlas en una lista
    mientras el input no sea == exit
        sumar el valor del primer indice de la lista con el segundo
    hallar el promedio con el resultado de la suma dividido la cantidad de datos dentro de la lista
    

"""
#Resultado esperado:
"""
---------------------------------------------------------------

Input1 = 1.65
Input2 = 1.87
Input3 = 1.60
Input4 = 1.50

Output = 1.555

---------------------------------------------------------------



---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def heightavegare():
    
    try:
        number = input("Enter the height, type exit to finish: ")
        variables = {"index":0,"total":0}
        heights = []
        
        while number !="exit":

            heights.append(float(number))
            number = input("Enter the height, type exit to finish: ")
            variables["total"] += heights[variables["index"]]
            variables["index"] += 1

        average = variables["total"]/len(heights)
        print(heights)
        print("The height average is {}".format(average))

    except:
        print("Enter a number!")
        heightavegare()

heightavegare()