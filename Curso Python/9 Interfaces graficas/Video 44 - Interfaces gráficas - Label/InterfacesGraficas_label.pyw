from tkinter import *

root=Tk()
miFrame=Frame(root, width=500, height=400)
miFrame.pack()

miImagen=PhotoImage(file="opciones label.png") #Para usar imagenes
#Si no vas a volver a usar un label, puedes prescindir de almacenar en variable
Label(miFrame, image=miImagen).place(x=0, y=0)
Label(miFrame, text="Hola que tal", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200) # Ubicar texto en cualquier lugar dentro de la interfaz con coordenadas


root.mainloop()