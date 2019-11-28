i=1
while i<=10:
	print("Ejecución: " + str(i))
	i=i+1

print("Terminó la Ejecución")

print("---------------------")

edad=int(input("Introduce edad: "))
while (100<edad or edad<0):
	if (edad < 0):
		print("Has introducido una edad negativa. Prueba de nuevo")
	else:
		print("Has introducido una edad mayor que 100. Prueba de nuevo")
	edad=int(input("Introduce edad: "))
print("Edad correcta: ", edad)

print("---------------")

#Ejemplo para salir de bucles infinitos
#Programa raiz cuadrada de un numero
import math

print("Programa de calculo de raiz cuadrada")
numero = int(input("Introduce un numero: "))
intentos = 0

while numero < 0:
	print("No hay raices de numero negativos")

	if intentos==2:
		print("Demasiados intentos. Finalizando programa")
		break

	numero = int(input("Introduce un numero: "))
	if numero<0:
		intentos+=1

if intentos<2:
	solucion=math.sqrt(numero)
	print("La raiz cuadrada de ", numero, "es ", solucion)