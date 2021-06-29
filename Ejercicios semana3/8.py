# Ejercicios

#8. Confeccionar un programa que lea n pares de datos, cada par de datos corresponde a la
#medida de la base y la altura de un triángulo. El programa deberá informar:
#a) De cada triángulo la medida de su base, su altura y su superficie.
#b) La cantidad de triángulos cuya superficie es mayor a 12.
 
#Algoritmo:
"""
-Escriba el numero n de triangulos que desea ingresar
-Escribir la base y altura separados por un espacio
    multiplicar ambos valores y dividirlos por 2
    

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

def traingles():

    triangles = {}
    areas = []

    n = int(input("Enter the number of triangles: "))

    for x in range(1, n+1):
        
        triangle = input("Enter the base and the height of the triangle (separed by one space) : ")
        triangles["triangle"+ str(x)] = triangle.split()
        area = float(triangles["triangle"+ str(x)][0])*float(triangles["triangle"+ str(x)][1])/2
        triangles["triangle"+ str(x)].append(area)

        if area >= 12.0:
            areas.append(area)

    for x in range(1, n+1):

        print("la base del triangulo {} es ({}), la altura es ({}) y su superficie es ({})".format(x,triangles["triangle"+ str(x)][0],triangles["triangle"+ str(x)][1],triangles["triangle"+ str(x)][2]))

    print("({}) triangulos tienen una superficie mayor a 12".format(len(areas)))

traingles()