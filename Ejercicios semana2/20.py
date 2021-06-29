# Ejercicios

#20. Hacer un algoritmo que calcule el total a pagar por la compra de camisas. Si se compran 
#tres camisas o más se aplica un descuento del 20% sobre el total de la compra y si son 
#menos de tres camisas un descuento del 10%
 
#Algoritmo:
"""
-definir el valor de las camisas
-ingresar el numero de camisas a pagar
    si se compran mas de 3 camisas
        imprimir el valor de las camisas con el descuento del 20% aplicado
    si se compran menos de 3 camisas
        imprimir el valor de las camisas con el descuento del 10%

"""
#Resultado esperado:
"""
Input = 5

Output = Con un valor por camisa de (20000) el costo de las (5) camisas es de 80000

---------------------------------------------------------------
Input = 2

Output = Con un valor por camisa de (20000) el costo de las (2) camisas es de 36000
---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def shirtprice():
    number = int(input("Ingrese el total de camisetas a pagar: "))
    shirtprice = 20000
    
    if number >= 3:
        cost = (number*shirtprice) - (number*shirtprice*0.2)
        print("With a value of ({}$) for shirt, the cost of ({}) shirts is {}$".format(shirtprice,number,cost))
    elif number <3 and number >0:
        cost = (number*shirtprice) - (number*shirtprice*0.1)
        print("With a value of ({}$) for shirt, the cost of ({}) shirts is {}$".format(shirtprice,number,cost))
    else:
        print("Enter a valid shirts number")

shirtprice()