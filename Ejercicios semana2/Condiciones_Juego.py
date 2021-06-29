#MisionTic Cuestionario
print("Juego MisionTic2022")

total_preguntas = 4
puntaje = 0

#Primera pregunta
respuesta = input("1. ¿Cual es el nombre de la plataforma MisionTic2022?")
if respuesta.lower() == "imaster":
	puntaje = puntaje + 1 #Tambien puedes usar (puntaje += 1)
	print("Correcto")
else:
	print("incorrecto")
#Segunda pregunta
respuesta = input("2. ¿En que año estamos?")
if respuesta == "2021":
	puntaje = puntaje + 1
	print("Correcto")
else:
	print("incorrecto")
#Tercera pregunta
respuesta = input("3. ¿Cuanto es 8 + 4 + 1 - 4 - 2?")
if respuesta == "7" or respuesta.lower() == "siete":
	puntaje = puntaje + 1
	print("Correcto")
else:
	print("incorrecto")
#Cuarta pregunta
respuesta = input("4. ¿Cual es el mejor lenguaje de programacion?")
if respuesta.lower() == "python":
	puntaje = puntaje + 1
	print("Correcto")
else:
	print("incorrecto")
#porcentaje
porcentaje = int((puntaje/total_preguntas)*100)

print("Resultado final fue {} de {}, con un porcentaje de {}%".format(puntaje,total_preguntas,porcentaje))
