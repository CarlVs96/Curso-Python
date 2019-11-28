#Continue salta a la siguiente iteraciond esde donde lo lea

for letra in "Python":
	if letra == "h":
		continue

	print("Viendo la letra: ", letra)

#Contar cuantos caracteres tiene

nombre="Carlos Villén Villar"
print(len(nombre))
#Ahora sin los espacios
contador = 0

for i in nombre:
	if i==" ":
		continue
	contador+=1

print(contador)

#Instruccion pass devuelve un null. Se usa para dejar en desarrollo la mayoria de veces.

#Else. Solo lo leeria si ha completado todas las vueltas de bucle y no se ha detenido (break) el bucle

email=input("Introduce tu email: ")

for i in email:
	if i=="@":
		arroba=True
		break
else:
	arroba=False

print(arroba)

