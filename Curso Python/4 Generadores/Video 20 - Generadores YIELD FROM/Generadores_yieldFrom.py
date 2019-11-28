#Funcion generador que devuelva ciudades
#El asterisco significa que se va a recibir un numero indeterminado de elementos. Y en forma de tupla
def devuelveCiudades(*ciudades):
	for elemento in ciudades:
		for subElemento in elemento:
			yield subElemento

ciudadesDevueltas=devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))

print("----------------------")

#Simplificar esto con yield from
def devuelveCiudades(*ciudades):
	for elemento in ciudades:
		#for subElemento in elemento:
		yield from elemento

ciudadesDevueltas=devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))