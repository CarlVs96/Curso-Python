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

#Clase que hereda de vehiculos

class Moto(Vehiculos):
	hCaballito=""
	def caballito(self):
		self.hCaballito="Voy haciendo el caballito"
	#Sobrescritura de metodos. Sobreescribimos el metodo estado, para incluir un nuevo apartado
	def estado(self):
		print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ", self.enMarcha,
			"\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena, "\n", self.hCaballito)

class Furgoneta(Vehiculos):
	def carga(self, cargar):
		self.cargado=cargar
		if self.cargado:
			return "La furgoneta esta cargada"
		else:
			return "La furgoneta esta libre"
class VElectricos(Vehiculos):
	def __init__(self, marca, modelo):
		super().__init__(marca, modelo)
		self.autonomia=100

	def cargarEnergia(self):
		self.cargando=True

#Herencia multiple
class BicicletaElectrica(VElectricos, Vehiculos):
	pass

miMoto=Moto("Yamaha","RX100")

#miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Renault", "Kangoo")
miFurgoneta.arrancar()
miFurgoneta.estado()
print(miFurgoneta.carga(True))

#Preferencia al constructor que antes pongas en la clase heredada de la herencia multiple
#En este caso "Vehiculos"
#"Orbea","HC1030"
#super(), Llama al metodo de la clase padre. crear un objeto con las propiedades de la segunda clase dada (Modificado en la clase )
miBici=BicicletaElectrica("Orbea","HC1030")
miBici.estado()