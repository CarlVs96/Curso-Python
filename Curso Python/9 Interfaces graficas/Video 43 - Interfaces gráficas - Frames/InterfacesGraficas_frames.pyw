from tkinter import *

raiz = Tk() #Ventana
raiz.title("Real Madrid") # Titulo de la ventana
#raiz.resizable(True, False) #Permiso booleano para redimensionar a lo ancho o a lo largo.
raiz.iconbitmap("real-madrid.ico") #Ponerle icono a la ventana.
#raiz.geometry("650x350") #Tamaño por defecto ventana. Comentado porque se adapta a su contenido. El frame
raiz.config(bg="white") #Bastantes parametros que cambiar, por ejemplo fondo

#Frame
miFrame = Frame()
miFrame.pack(side="left", anchor="n") #Anchor son cordenadas norte sur este oeste
miFrame.config(bg="light blue", width = 650, height = 300) # Si redimensionas se ve color de raiz
miFrame.config(bd=35, relief=SUNKEN) #borde
miFrame.config(cursor="pirate") #Tipo de cursor hand2, pirate, etc..

raiz.mainloop() #Bucle infinito para la escucha de intrucciones. SIEMPRE EN ULTIMO LUGAR