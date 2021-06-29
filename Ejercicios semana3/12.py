#12. Realizar un programa que lea los lados de n triángulos, e informar:
#a) De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles 
#(dos lados iguales), o escaleno (ningún lado igual)
#b) Cantidad de triángulos de cada tipo.



def triangles():
    triangles = {}
    type_triangles = {"isosceles":0, "equilatero":0, "escaleno":0}
    n = int(input("Digite la cantidad de triangulos: ")) #5

    for i in range(1,n+1):
        datos = input("Digite los lados del triangulo (separados por espacios): ") #2 5 5
        triangles['triangle'+str(i)] = datos.split() #([2,5,5])
        if len(set(triangles['triangle'+str(i)])) == 3:
            print("Este triangulo es escaleno!")
            type_triangles["escaleno"] += 1
        elif len(set(triangles['triangle'+str(i)])) == 2:
            print("Este triangulo es isosceles!")
            type_triangles["isosceles"] += 1
        elif len(set(triangles['triangle'+str(i)])) == 1:
            print("Este triangulo es equilatero")
            type_triangles["equilatero"] += 1
    
    return type_triangles
    
print(triangles())