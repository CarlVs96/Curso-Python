def devuelveMax (num1,num2):
	if num1>num2:
		return num1
	else:
		return num2

primerNumero  = int(input("Introduce un numero: "))
segundoNumero = int(input("Introduce otro numero: "))

mayor = devuelveMax(primerNumero,segundoNumero)

print("El numero mayor es: ", mayor)