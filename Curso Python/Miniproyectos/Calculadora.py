def suma(num1, num2):
	resultado = num1 + num2
	return resultado
def resta(num1, num2):
	resultado = num2 - num1
	return resultado

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el segundo numero: "))

if numero1 > numero2:
	print(suma(numero1, numero2))
else:
	print(resta(numero1, numero2))