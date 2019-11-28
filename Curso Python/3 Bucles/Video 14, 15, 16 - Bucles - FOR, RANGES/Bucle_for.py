for i  in [1,2,3]:
	print("Hola")

for i  in ["primavera","verano","otoño","invierno"]:
	print(i)
#Para que no haga salto de linea
for i in ["Hola","que","tal"]:
	print(i, end=" ")
print()

#Iteraccion tantas como caracteres
#Comprobar si un email es correcto por tener arroba y punto

email=False
miEmail=input("Introduce email: ")

for i in miEmail:
	if i == "@":
		for j in miEmail:
			if j == ".":
				email = True
			
#if email == True:
if email:
	print("El email es correcto")
else:
	print("El email es incorrecto")

#Rangos
for i in range(5):
	print("Hola")