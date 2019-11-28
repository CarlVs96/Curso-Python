import pickle

class Vehiculos():
	#Constructor
	def __init__(self, marca, modelo):
		self.marca = marca
		self.modelo = modelo
		self.enMarcha = False
		self.acelera = False
		self.frena = False

	def arrancar(self):
		self.enMarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar(self):
		self.frena=True

	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha,
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

coche1 = Vehiculos("Mazda","MX5")
coche2 = Vehiculos("Seat","Leon")
coche3 = Vehiculos("Renault","Megane")

coches=[coche1, coche2, coche3]

#Guardar en archivo de forma serializada
fichero=open("losCoches", "wb") #Escritura binaria/bytes
pickle.dump(coches, fichero)
fichero.close()
del fichero

#Abrir el fichero y leer el archivo serializado

ficheroApertura = open("losCoches", "rb")
misCoches = pickle.load(ficheroApertura)
ficheroApertura.close()
#Mostrar la serializacion
for i in misCoches:
	print(i.estado())