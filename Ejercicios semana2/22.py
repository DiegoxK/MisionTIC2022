# Ejercicios

#22. Verificar si un texto que termina en punto es un palíndromo (capicúa). Un texto es 
#palíndromo si se lee lo mismo de izquierda a derecha o de derecha a izquierda. Ej: “Amor 
#a roma”
 
#Algoritmo:
"""
-ingresar el texto
-verificar si el texto es un palindromo
    si el texto es un palindromo
        imprimir (el texto () es un palindromo)
    sino el texto es un palindromo
        imprimir (el texto () no es un palindromo)

"""
#Resultado esperado:
"""
---------------------------------------------------------------

Input1 = Azuza

Output = el texto (Azuza) es un palindromo

---------------------------------------------------------------

Input = Aguadepanela

Output = el texto (Aguadepanela) no es un palindromo

---------------------------------------------------------------
"""
#Transcripcion y verificacion del resultado:

def palindrom():

    word = input("Enter a word: ").lower()
    lenw = len(word)
    x = -1
    palindrome = (word[lenw + x])
    lenp = len(palindrome)

    while lenp < lenw:
        x -= 1
        palindrome += (word[lenw + x])
        lenp = len(palindrome)

    if palindrome == word:
        print("The word ({}) is a polindrome!".format(word))
    else:
        print("The word ({}) is not a polindrome".format(word))

palindrom()