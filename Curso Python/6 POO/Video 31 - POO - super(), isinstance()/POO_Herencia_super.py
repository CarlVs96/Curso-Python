#Programa 2 clases, persona y empleado.
#super()
class Persona():
	def __init__(self, nombre, edad, lugarResidencia):
		self.nombre = nombre
		self.edad = edad
		self.lugarResidencia = lugarResidencia

	def descripcion(self):
		print("Nombre: ", self.nombre, "Edad: ", self.edad, "Lugar de residencia: ", self.lugarResidencia)

class Empleado(Persona):
	def __init__(self, salario, antiguedad, nombreEmpleado, edadEmpleado, residenciaEmpleado):
		super().__init__(nombreEmpleado, edadEmpleado, residenciaEmpleado)
		self.salario = salario
		self.antiguedad = antiguedad
	
	def descripcion(self):
		super().descripcion()
		print("Salario: ", self.salario,"Antiguedad: ", self.antiguedad)

carlos=Empleado(1500, 1, "Carlos", 22, "Jaén")
carlos.descripcion()
#isinstance(). Informa si un objeto es instancia de una clase. True o False
print(isinstance(carlos, Empleado))
print(isinstance(carlos, Persona))