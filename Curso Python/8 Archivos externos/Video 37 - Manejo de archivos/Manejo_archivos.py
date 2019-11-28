from io import open
#SIEMPRE CREAR -> ABRIR -> MANIPULAR -> CERRAR
#Modo escritura
"""archivo_texto=open("archivo.txt", "w")
frase = "Una tarde estupenda para estudiar Python \neste Lunes"
archivo_texto.write(frase)
archivo_texto.close()"""

#Modo lectura
"""archivo_texto=open("archivo.txt", "r")
texto=archivo_texto.read()
archivo_texto.close()
print(texto)"""

#Modo readlines. Leer info almacenada linea a linea, almacena en una lista
"""archivo_texto=open("archivo.txt", "r")
lineas_texto=archivo_texto.readlines()
archivo_texto.close()
print(lineas_texto)
print(lineas_texto[0])
print(lineas_texto[1])"""

#Modo append, para incluir mas datos al archivo
archivo_texto=open("archivo.txt", "a")
archivo_texto.write("\nDia que hace mucho calor.")
archivo_texto.close()
