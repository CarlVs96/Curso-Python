from tkinter import *

raiz = Tk() #Ventana
raiz.title("Real Madrid") # Titulo de la ventana
raiz.resizable(True, False) #Permiso booleano para redimensionar a lo ancho o a lo largo.
raiz.iconbitmap("real-madrid.ico") #Ponerle icono a la ventana.
raiz.geometry("650x350") #Tamaño por defecto ventana
raiz.config(bg="white") #Bastantes parametros que cambiar, por ejemplo fondo




raiz.mainloop() #Bucle infinito para la escucha de intrucciones. SIEMPRE EN ULTIMO LUGAR