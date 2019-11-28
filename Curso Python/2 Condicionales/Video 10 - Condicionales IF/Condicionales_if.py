print("Programa de evaluación de notas")

nota_alumno=int(input("Introduce la nota del alumno: "))

def evaluacion(nota):
	valoracion = "Aprobado"
	if nota < 5:
		valoracion = "Suspenso"	
	return valoracion

print(evaluacion(nota_alumno))
