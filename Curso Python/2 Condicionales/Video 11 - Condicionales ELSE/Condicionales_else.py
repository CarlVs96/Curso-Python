print("Verificación de acceso")
edadUsuario = int(input("Introduce tu edad: "))

if edadUsuario < 18:
	print("No puedes acceder")
elif edadUsuario > 100:
	print("Edad incorrecta")
else: 
	print("Puedes acceder")

print ("El programa ha finalizado")

print("---------------------------------------------")

print("Verificación de notas")
notaUsuario = float(input("Introduce tu nota: "))

if notaUsuario >= 0 and notaUsuario < 5:
	print("Insuficiente")
elif notaUsuario >= 5 and notaUsuario < 6:
	print("Suficiente")
elif notaUsuario >= 6 and notaUsuario < 7:
	print("Bien")
elif notaUsuario >= 7 and notaUsuario < 9:
	print("Notable")
elif notaUsuario >= 9 and notaUsuario <= 10:
	print("Sobresaliente")
else: 
	print("Nota incorrecta")

print ("El programa ha finalizado")