nombreUsuario=input("Introduce tu nombre de usuario: ")
print("Tu nombre es: ", nombreUsuario.upper())
print("Tu nombre es: ", nombreUsuario.lower())
print("Tu nombre es: ", nombreUsuario.capitalize())
print("Tu nombre es: ", nombreUsuario.upper())
print("Tu nombre es: ", nombreUsuario.upper())
print("Tu nombre es: ", nombreUsuario.upper())
print("Tu nombre es: ", nombreUsuario.upper())

edad=input("Introduce la edad: ")

while edad.isdigit()==False:
	print("Edad incorrecta. Introduce un valor numerico.")
	edad=input("Introduce la edad: ")

if int(edad) < 18:
	print("No puedes pasar")
else:
	print("Puedes pasar")