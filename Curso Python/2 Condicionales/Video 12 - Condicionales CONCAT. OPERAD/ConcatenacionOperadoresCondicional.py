#Evaluar el salario de una serie de personas que trabajan en una empresa
salarioPresidente = int(input("Introduce salario presidente: "))
print("Salario presidente: " + str(salarioPresidente))

salarioDirector = int(input("Introduce salario director: "))
print("Salario director: " + str(salarioDirector))

salarioJefeArea = int(input("Introduce salario jefe area: "))
print("Salario jefe area: " + str(salarioJefeArea))

salarioAdministrativo = int(input("Introduce salario administrativo: "))
print("Salario administrativo: " + str(salarioAdministrativo))

if salarioAdministrativo<salarioJefeArea<salarioDirector<salarioPresidente:
	print("Todo correcto")
else:
	print("Huele un poco raro aqui")