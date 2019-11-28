print("Optativas 2019:")
print("1. Inf. Gráfica - 2. Pruebas de Software - 3. Usabilidad y accesibilidad")

asignatura       = input("Escribe el numero de la asignatura escogida: ")
listaAsignaturas = {"1":"Inf. Gráfica", "2":"Pruebas de Software", "3":"Usabilidad y accesibilidad"}

if asignatura in ("1","2","3"):
	print("La asignatura elegida es: " + listaAsignaturas[asignatura] )
else:
	print("La asignatura no existe")

"""Funciones para pasar todo a minusculas y minusculas: - lower()
														- upper()"""