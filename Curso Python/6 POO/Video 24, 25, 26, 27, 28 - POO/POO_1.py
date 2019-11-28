class Coche():

	#Constructor estado inicial
	def __init__(self):
		#Propiedades
		#Encapsulacion de variable __. Solo accesible desde dentro de la clase. Un coche no puede tener 2 ruedas
		self.__largoChasis=250
		self.__anchoChasis=120
		self.__ruedas=4
		self.__enMarcha=False

	#Metodos (Comportamientos, que es capaz de hacer, arrancar, girar, acelerar frenar)
	#Funciones que pertenecen a una clase
	def arrancar(self, arrancamos):
		self.__enMarcha=arrancamos
		if self.__enMarcha:
			chequeo=self.__chequeoInterno()

		if(self.__enMarcha and chequeo):
			return "El coche esta en marcha"
		elif self.__enMarcha and chequeo==False:
			return "Algo en el chequeo ha ido mal, no podemos arrancar"
		else:
			return "El coche esta parado"

	def estadoCoche(self):
		print("El coche tiene: ", self.__ruedas, " ruedas. ",
		"Un ancho de: ", self.__anchoChasis, ". "
		"Y un largo de: ", self.__largoChasis)

#Metodo encapsulado, solo accesible desde dentro
	def __chequeoInterno(self):
		print("Realizando chequeo interno")

		self.gasolina="Ok"
		self.aceite="Ok"
		self.puertas="Cerradas"

		if (self.gasolina=="Ok" and self.aceite=="Ok" and self.puertas=="Cerradas"):
			return True
		else:
			return False


miCoche=Coche()

print(miCoche.arrancar(True))
miCoche.estadoCoche()

print("------------A continuación creamos el segundo objeto.------------")

miCoche2=Coche()

print(miCoche2.arrancar(False))
#Dado que la variable ruedas está encapsulada, no puede modificarse
#miCoche2.__ruedas=2

miCoche2.estadoCoche()
#miCoche2.__chequeoInterno(). No funciona porque no es accesible, está encapsulado