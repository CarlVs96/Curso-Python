#Generar x pares dado un limite. Funcion
def generaPares(limite):
	listaPares = []
	for i in range(0, limite*2, 2):
		listaPares.append(i)
	return listaPares

limiteIn=int(input("Introduce cuantos pares necesitas: "))
print(generaPares(limiteIn))
#Generar x pares dado un limite. Generador
#La ventaja es que no se crean los valores hasta que no se solicitan. Lo cual es mas eficiente.
def generaParesGen(limite):

	for i in range(0, limite*2, 2):
		yield i

limiteIn=int(input("Introduce cuantos pares necesitas: "))
devuelvePares=generaParesGen(limiteIn)

print(next(devuelvePares))
print("Codigo..")
print(next(devuelvePares))
print("Codigo..")
print(next(devuelvePares))