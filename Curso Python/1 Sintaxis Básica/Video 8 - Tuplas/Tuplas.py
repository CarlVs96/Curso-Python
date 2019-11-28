miTupla = ("Juan", 13, 1, 1995) #Sin parentesis tambien seria tupla
miLista = list(miTupla) #Pasar tupla a lista
print(miTupla[1])
print(miLista)

paraPasarATupla = ["Elementos", 2]
nuevaTupla = tuple(paraPasarATupla) #Pasar lista a tupla
print(nuevaTupla)

pruebaNombre = "Juan"

print(pruebaNombre in miTupla)
print("Juan" in paraPasarATupla)
#Contar cuantas veces está un elemento
print(miTupla.count(13))
#Saber longitud de una tupla
print(len(miTupla))

#Tupla unitaria
tuplaUnitaria = ("Carlos",) #Importante la coma, si no, no es tupla y contaria la longitud del str
print(len(tuplaUnitaria))

#Desempaquetado de tuplas
nombre, dia, mes, anio = miTupla
print(nombre)
#Busqueda de posicion
print(miTupla.index(1995)) #Igual que en las listas, devuelve la posicion

