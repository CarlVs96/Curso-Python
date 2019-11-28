miDiccionario = {"Alemania":"Berlin","Francia":"Paris","Reino Unido":"Londres","España":"Madrid"}
miDiccionario["Italia"] = "Lisboa"
print(miDiccionario)
print(miDiccionario["España"])
#Corregir datos en python. Sobrescribiendo
miDiccionario["Italia"] = "Roma"
print(miDiccionario)
#Eliminar elementos
del miDiccionario["Reino Unido"]
print(miDiccionario)

#---------------------------
#Pueden ser de distintos tipos
segundoDiccionario = {"Carlos":"Villén", 23:"Michael Jordan", "Mosqueteros":3}
print(segundoDiccionario)
print(segundoDiccionario[23])
#---------------------------
#Se pueden asignar valores desde tuplas o listas
miTupla = [1, 2, 3]
diccionarioDorsales = {miTupla[0]:"Casillas", miTupla[1]:"Salgado", miTupla[2]:"Roberto Carlos"}
print(diccionarioDorsales)
print(diccionarioDorsales[1])
#Sacar claves, valores y longitud
print(diccionarioDorsales.keys())
print(diccionarioDorsales.values())
print(len(diccionarioDorsales))