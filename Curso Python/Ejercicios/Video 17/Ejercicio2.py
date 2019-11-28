acumulador=0

numero=int(input("Introduce un numero positivo: "))
while numero>0:
	acumulador=numero+acumulador
	numero=int(input("Introduce un numero positivo: "))

print("Has introducido un numero negativo, el total acumulado es: ", str(acumulador))