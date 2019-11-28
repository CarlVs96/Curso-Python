"""Evaluar si un alumno que entra a un colegio tiene derecho a beca o no
	- Evaluaremos si la distancia es mayor a 40 km
	- Si tiene mas hermanos en el centro, si son 3 mas prioridad
	- Salario familiar menor o igual a 20000  <- Tendra mas importancia"""
print("Programa becas")

distanciaEscuela = int(input("Introduce la distancia al centro en km: "))
print(distanciaEscuela)
hermanos         = int(input("Introduce el numero de hermanos en el centro: "))
print(hermanos)
salario          = int(input("Introduce el salario anual bruto: "))
print(salario)

if distanciaEscuela > 40 and hermanos > 2 or salario <= 20000:
	print("Privilegiado beca")
else:
	print("Lo sentimos, no tienes derecho a beca")