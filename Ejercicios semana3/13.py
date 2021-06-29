# Ejercicios

#13. Escribir un programa que pida ingresar coordenadas (x,y) que representan puntos en el
#plano.
#Informar cuántos puntos se han ingresado en el primer, segundo, tercer y cuarto
#cuadrante. Al comenzar el programa se pide que se ingrese la cantidad de puntos a
#procesar

 
#Algoritmo:
"""
Ingresar la cantidad N de puntos que se desear verificar
Definir un diccionario con las llaves {Primer, Segundo, Tercer, Cuarto}
-ingresar mediante input y espacios las coordenadas de cada punto
    Segun el signo del indice de cada eje en el punto
        ingresarlos a al diccionario en su respectiva llave

"""
#Resultado esperado:
"""
---------------------------------------------------------------
Input = 4

Input1 =2 5
Input2 =-4 5
Input3 =-4 -4
Input4 =2 -5

Output = Se han ingresado (1) Elementos en el primer cuadrante, (1) En el segundo, (1) en el tercero y (1) en el cuarto

---------------------------------------------------------------



---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def cords():

    points = {'first':0,'second':0,'third':0,'fourth':0}
    n = int(input('Enter the number of points you want to check: '))
    
    for x in range(1,n+1):
        cords = input("Enter the point {} (X and Y must be separated by spacing): ".format(x)).split()

        if int(cords[0]) > 0 and int(cords[1]) > 0:
            points['first'] +=1
        elif int(cords[0]) < 0 and int(cords[1]) > 0:
            points['second'] +=1
        elif int(cords[0]) > 0 and int(cords[1]) < 0:
            points['fourth'] +=1
        elif int(cords[0]) < 0 and int(cords[1]) < 0:
            points['third'] +=1

    print('They have entered ({}) coordinates of the first quadrant, ({}) of the second, ({}) of the third, and ({}) of the fourth'.format(points['first'],points['second'],points['third'],points['fourth']))

cords()