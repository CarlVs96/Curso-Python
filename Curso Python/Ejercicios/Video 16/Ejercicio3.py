contadorArrobas = 0
contadorPuntos = 0

email=input("Introduce un mail válido: ")

for i in range(len(email)):
	if email[i]=="@":
		contadorArrobas+=1
	if email[i]==".":
		contadorPuntos+=1

if contadorArrobas == 1 and contadorPuntos>=1:
	print("El email es válido")
else:
	if contadorArrobas != 1:
		print("El email no es correcto, ya que tiene", contadorArrobas, "arrobas")
	else:
		print("El email no es correcto ya que no hay puntos en el email")