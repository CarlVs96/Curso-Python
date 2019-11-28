print("Introduce una contraseña con 8 o más caracteres y sin espacios")
password=input("Contraseña: ")

validez=True
if len(password)>=8:
	for i in range(len(password)):
		if password[i]==" ":
			validez = False
else:
	validez = False

if validez:
	print("Contraseña OK")
else:
	print("Contraseña errónea")