email=input("Introduce tu email: ")
if email.startswith("@") or email.endswith("@") or email.count("@")!=1:
	print("El email no es correcto.")
else:
	print("El email es correcto.")