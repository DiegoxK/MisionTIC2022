
def pago_matricula():
    
    estudiante = input("Ingrese el tipo de estudiante: ")
    Salario = 908526
    if estudiante == "pregrado":
        matricula = (2*Salario) + (2*Salario*0.1)
        print("El costo por su matricula es de "+str(matricula))
    elif estudiante == "especializacion":
        matricula = (3*Salario) + (3*Salario*0.1) + (120000)
        print("El costo por su matricula es de "+str(matricula))
    elif estudiante == "posgrado":
        voto = input("¿Usted voto? ")
        if voto == "si":
            matricula = (5*Salario) - (5*Salario*0.1)
            print("El costo por su matricula es de "+str(matricula))
        else:
            matricula = (5*Salario)
            print("El costo por su matricula es de "+str(matricula))        

pago_matricula()