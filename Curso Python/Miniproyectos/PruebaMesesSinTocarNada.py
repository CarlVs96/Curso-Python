class TrabajoFindGrado():
	"""Si funciona empiezo"""
	
	grado= "Ing Infor"


	def __init__(self, hora):
		self.hora = hora

	def aprobar(self, nota):
		if nota < 5 or self.hora > 2240:
			print("No apruebas macho")
		else:
			print("Va, es posible que apruebes")


carlos= TrabajoFindGrado(2300)

carlos.aprobar(6)

carlos.hora=2200
carlos.aprobar(6)

print(TrabajoFindGrado.grado)

print(carlos.grado)
carlos.grado="Magisterio"
print(carlos.grado.upper())
print(TrabajoFindGrado.grado)