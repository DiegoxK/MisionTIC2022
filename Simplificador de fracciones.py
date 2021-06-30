def divisores():
    
    try:
        number1 = int(input("Numerador: "))
        number2 = int(input("Denominador: "))
        check = 0
        print(" ")
        if number1 >= number2:
            range_numer = [x for x in range(2,number1)]
        elif number2 > number1:
            range_numer = [x for x in range(2,number2)]

        for x in range_numer:
            if number1%x == 0 and number2%x == 0:
                check += 1
                simp1 = number1//x
                simp2 = number2//x
                print("Divisible en común por ({})".format(x))

        if check == 0:
            print("Los numeros ({}), ({}) no tienen divisores en común".format(number1,number2)) 
        else:
            print(" \nNumero simplificado = {}/{}\n ".format(simp1,simp2))

        divisores()
    except:
        print("Ingrese un numero")
        divisores()
    
divisores()

