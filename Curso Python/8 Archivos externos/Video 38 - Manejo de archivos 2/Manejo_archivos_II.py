from io import open

archivo_texto=open("archivo.txt", "r+") # Lectura y escritura
#Modificar posicion del puntero. seek(numero del caracter)
archivo_texto.write("Hola")
print(archivo_texto.read())
#Aqui el puntero se ubica al final, ya que ha leido justo antes
print(archivo_texto.read())

archivo_texto.seek(0)
print(archivo_texto.read())

archivo_texto.seek(11)
print(archivo_texto.read())

#Leer hasta la posicion que le indiquemos

#Reposicionamos
archivo_texto.seek(0)
print(archivo_texto.read(11))

