# Ejercicios

# 10. Leer un número entero de tres dígitos y determinar si algún dígito es múltiplo de los otros
 
#Algoritmo:
"""
-Ingresar el numero
-Hallar el indice de los digitos en cada numero
-comprobar cada numero con los otros 2 en busca de un multiplo de si mismo

    si el segundo numero se encuentra entre los multiplos del primero
        imprimir (el segundo digito es multiplo del primero)
    sino el segundo numero se encuentra entre los multiplos del primero
        imprimir (el segundo digito no es multiplo del primero)
    si el tercer numero se ecuentra entre los multiplos del priemro
        imprimir (el tercer digito es multiplo del primero)
    sino el tercer numero no se ecuentra entre los multiplos del primero
        imprimir (el tercer digito o es multiplo del primero)

    si el primer numero se encuentra entre los multiplos del segundo
        imprimir (el primer digito es multiplo del segundo)
    sino el primer numero se encuentra entre los multiplos del segundo
        imprimir (el primer digito no es multiplo del segundo)
    si el tercer numero se ecuentra entre los multiplos del segundo
        imprimir (el tercer digito es multiplo del segundo)
    sino el tercer numero no se ecuentra entre los multiplos del segundo
        imprimir (el tercer digito o es multiplo del segundo)
 
 ETC
 
"""
#Resultado esperado:
"""
Input = 123

Output = 

El segundo digito es multiplo del primero
El tercer digito es multiplo del primero

El primer digito no es multiplo del segundo
El tercer digito no es multiplo del segundo

El primer digito no es multiplo del tercero
el segundo digito no es multiplo del tercero

---------------------------------------------------------------

"""
#Transcripcion y verificacion del resultado:

def multiple_numbers():
    input_number = input("Enter a three digit number: ")
    input_number[0], input_number[1], input_number[2]
    multiples_of_1 = [1,2,3,4,5,6,7,8,9]
    multiples_of_2 = [2,4,6,8]
    multiples_of_3 = [3,6,9]
    multiples_of_4 = [4,8]
    multiples_of_5 = [5]
    multiples_of_6 = [6]
    multiples_of_7 = [7]
    multiples_of_8 = [8]
    multiples_of_9 = [9]
    print("---------------------------------------------------------------------------------\nFirt digit combrobation\n")
    #Comprobacion de los multiplos del 1
    if input_number[0] == "1":
        if int(input_number[1]) in multiples_of_1:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[0]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[0]))
        if int(input_number[2]) in multiples_of_1:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[0]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[0]))

    #Comprobacion de los multiplos del 2
    if input_number[0] == "2":
        if int(input_number[1]) in multiples_of_2:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[0]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[0]))
        if int(input_number[2]) in multiples_of_2:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[0]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[0]))

    #Comprobacion de los multiplos del 3
    if input_number[0] == "3":
        if int(input_number[1]) in multiples_of_3:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[0]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[0]))
        if int(input_number[2]) in multiples_of_3:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[0]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[0]))

    #Comprobacion de los multiplos del 4
    if input_number[0] == "4":
        if int(input_number[1]) in multiples_of_4:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[0]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[0]))
        if int(input_number[2]) in multiples_of_4:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[0]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[0]))

    #Comprobacion de los multiplos del 5
    if input_number[0] == "5":
        if int(input_number[1]) in multiples_of_5:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[0]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[0]))
        if int(input_number[2]) in multiples_of_5:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[0]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[0]))

    #Comprobacion de los multiplos del 6
    if input_number[0] == "6":
        if int(input_number[1]) in multiples_of_6:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[0]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[0]))
        if int(input_number[2]) in multiples_of_6:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[0]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[0]))

    #Comprobacion de los multiplos del 7
    if input_number[0] == "7":
        if int(input_number[1]) in multiples_of_7:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[0]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[0]))
        if int(input_number[2]) in multiples_of_7:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[0]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[0]))

    #Comprobacion de los multiplos del 8
    if input_number[0] == "8":
        if int(input_number[1]) in multiples_of_8:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[0]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[0]))
        if int(input_number[2]) in multiples_of_8:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[0]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[0]))

    #Comprobacion de los multiplos del 9
    if input_number[0] == "9":
        if int(input_number[1]) in multiples_of_9:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[0]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[0]))
        if int(input_number[2]) in multiples_of_9:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[0]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[0]))
    print("---------------------------------------------------------------------------------\nSecond digit combrobation\n")
    #Comprobacion de los multiplos del 1 en el segundo indice
    if input_number[1] == "1":
        if int(input_number[0]) in multiples_of_1:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[1]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[1]))
        if int(input_number[2]) in multiples_of_1:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[1]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[1]))

    #Comprobacion de los multiplos del 2 en el segundo indice
    if input_number[1] == "2":
        if int(input_number[0]) in multiples_of_2:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[1]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[1]))
        if int(input_number[2]) in multiples_of_2:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[1]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[1]))

    #Comprobacion de los multiplos del 3 en el segundo indice
    if input_number[1] == "3":
        if int(input_number[0]) in multiples_of_3:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[1]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[1]))
        if int(input_number[2]) in multiples_of_3:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[1]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[1]))

    #Comprobacion de los multiplos del 4 en el segundo indice
    if input_number[1] == "4":
        if int(input_number[0]) in multiples_of_4:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[1]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[1]))
        if int(input_number[2]) in multiples_of_4:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[1]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[1]))

    #Comprobacion de los multiplos del 5 en el segundo indice
    if input_number[1] == "5":
        if int(input_number[0]) in multiples_of_5:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[1]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[1]))
        if int(input_number[2]) in multiples_of_5:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[1]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[1]))
            
    #Comprobacion de los multiplos del 6 en el segundo indice
    if input_number[1] == "6":
        if int(input_number[0]) in multiples_of_6:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[1]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[1]))
        if int(input_number[2]) in multiples_of_6:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[1]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[1]))

    #Comprobacion de los multiplos del 7 en el segundo indice
    if input_number[1] == "7":
        if int(input_number[0]) in multiples_of_7:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[1]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[1]))
        if int(input_number[2]) in multiples_of_7:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[1]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[1]))

    #Comprobacion de los multiplos del 8 en el segundo indice
    if input_number[1] == "8":
        if int(input_number[0]) in multiples_of_8:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[1]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[1]))
        if int(input_number[2]) in multiples_of_8:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[1]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[1]))

    #Comprobacion de los multiplos del 9 en el segundo indice
    if input_number[1] == "9":
        if int(input_number[0]) in multiples_of_9:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[1]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[1]))
        if int(input_number[2]) in multiples_of_9:
            print("The third number ({}) is multiple of {}!".format(input_number[2],input_number[1]))
        else:
            print("The third number ({}) is not multiple of {}!".format(input_number[2],input_number[1]))
    print("---------------------------------------------------------------------------------\nThird digit combrobation\n")            
    #Comprobacion de los multiplos del 1 en el tercer indice
    if input_number[2] == "1":
        if int(input_number[0]) in multiples_of_1:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[2]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[2]))
        if int(input_number[1]) in multiples_of_1:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[2]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[2]))
                            
    #Comprobacion de los multiplos del 2 en el tercer indice
    if input_number[2] == "2":
        if int(input_number[0]) in multiples_of_2:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[2]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[2]))
        if int(input_number[1]) in multiples_of_2:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[2]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[2]))
                      
    #Comprobacion de los multiplos del 3 en el tercer indice
    if input_number[2] == "3":
        if int(input_number[0]) in multiples_of_3:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[2]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[2]))
        if int(input_number[1]) in multiples_of_3:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[2]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[2]))
                            
    #Comprobacion de los multiplos del 4 en el tercer indice
    if input_number[2] == "4":
        if int(input_number[0]) in multiples_of_4:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[2]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[2]))
        if int(input_number[1]) in multiples_of_4:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[2]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[2]))
                            
    #Comprobacion de los multiplos del 5 en el tercer indice
    if input_number[2] == "5":
        if int(input_number[0]) in multiples_of_5:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[2]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[2]))
        if int(input_number[1]) in multiples_of_5:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[2]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[2]))
                            
    #Comprobacion de los multiplos del 6 en el tercer indice
    if input_number[2] == "6":
        if int(input_number[0]) in multiples_of_6:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[2]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[2]))
        if int(input_number[1]) in multiples_of_6:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[2]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[2]))
                            
    #Comprobacion de los multiplos del 7 en el tercer indice
    if input_number[2] == "7":
        if int(input_number[0]) in multiples_of_7:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[2]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[2]))
        if int(input_number[1]) in multiples_of_7:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[2]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[2]))
                            
    #Comprobacion de los multiplos del 8 en el tercer indice
    if input_number[2] == "8":
        if int(input_number[0]) in multiples_of_8:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[2]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[2]))
        if int(input_number[1]) in multiples_of_8:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[2]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[2]))
                            
    #Comprobacion de los multiplos del 9 en el tercer indice
    if input_number[2] == "9":
        if int(input_number[0]) in multiples_of_9:
            print("The first number ({}) is multiple of {}!".format(input_number[0],input_number[2]))
        else:
            print("The first number ({}) is not multiple of {}!".format(input_number[0],input_number[2]))
        if int(input_number[1]) in multiples_of_9:
            print("The second number ({}) is multiple of {}!".format(input_number[1],input_number[2]))
        else:
            print("The second number ({}) is not multiple of {}!".format(input_number[1],input_number[2]))


multiple_numbers()
