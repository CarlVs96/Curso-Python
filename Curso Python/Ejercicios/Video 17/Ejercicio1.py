primerNumero = int(input("Introduce un numero: "))
segundoNumero = int(input("Introduce un número mayor: "))

#if primerNumero<segundoNumero:
while primerNumero < segundoNumero:
	primerNumero = segundoNumero
	segundoNumero = int(input("Introduce otro numero mayor: "))

print("Has introducido un numero menor")