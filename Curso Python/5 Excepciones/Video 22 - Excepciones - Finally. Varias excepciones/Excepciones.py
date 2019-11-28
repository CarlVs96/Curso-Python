def divide():
	try:	
		op1=float(input("Introduce el primer número: "))
		op2=float(input("Introduce el segundo número: "))

		print("La división es: ", op1/op2)

	except ValueError:
		print("El valor no es numerico.")
	except ZeroDivisionError:
		print("No se puede dividir entre 0.")

	finally: #Lo que incluya se ejecuta se ejecute o no la excepcion
		print("Calculo finalizado")

divide()

#Excepción generalizada sin especificar el error. No es recomendable
def divideDos():
	try:	
		op1=float(input("Introduce el primer número: "))
		op2=float(input("Introduce el segundo número: "))

		print("La división es: ", op1/op2)

	except:
		print("Ha ocurrido un error.")

	print("Calculo finalizado")

divideDos()
