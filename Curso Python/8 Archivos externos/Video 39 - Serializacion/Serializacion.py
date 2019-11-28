import pickle

#Crear archivo binario
"""listaNombres = ["Pedro", "Ana", "Maria", "Isabel"]

ficheroBinario = open("listaNombres", "wb") #Escritura binaria

#Volcar informacion 
pickle.dump(listaNombres, ficheroBinario)

ficheroBinario.close()

del(ficheroBinario)"""

#Rescatar archivo binario

fichero = open("listaNombres","rb")
#Carga informacion load()

lista = pickle.load(fichero)

print(lista)