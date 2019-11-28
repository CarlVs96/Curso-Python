#Unir texto con variables con f, python lee el formato asi
for i in range(5):
	print(f"Valor de la variable {i}")

print("-----------------------------")
#Moverse por el bucle desde donde se quiera hasta donde se quiera y de cuanto en cuanto
for i in range(5,50,3):
	print(f"Valor de la variable {i}")

print("-----------------------------")
#Funcion len. Devolver longitud de un string
for i in range(len("Carlos")):
	print("Hola")

print("-----------------------------")
#Evaluar email
valido=False
email=input("Introduce email: ")

for i in range(len(email)):
	if email[i] == "@":
		valido=True
if  valido:
	print("Email valido")
else:
	print("Email incorrecto")