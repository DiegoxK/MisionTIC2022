# Ejercicios

# 1.Leer un número entero y determinar si es un número terminado en 4. 
 
#Algoritmo:
"""
-Ingresar el numero en forma de string

    -Si el ultimo indice del caracter = 4
        Imprimir(El ultimo digito del numero es un cuatro!)
    -Sino
        Imprimir(El ultimo digito del numero no es un cuatro)
"""
#Resultado esperado:
"""
Input = 1234
Output = El ultimo digito del numero es un cuatro!
---------------------------------------------------------------

Input = 1235
Output = El ultimo digito del numero no es un cuatro

"""
#Transcripcion y verificacion del resultado:

def fourlast():

    caracter = input("Ingrese un valor numerico: ")
    
    if caracter[-1] == "4":

        print("the last number is four")
    else:
        print("the last numbers is not four")

fourlast()

