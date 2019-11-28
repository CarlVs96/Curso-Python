from tkinter import *

raiz = Tk()

miFrame=Frame(raiz, width=1200, height=600)
miFrame.pack()

nombreLabel=Label(miFrame, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10) #padY Vertical.Margen con demas elementos
apellidoLabel=Label(miFrame, text="Apellido: ")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10) #padX Vertical.Margen con demas elementos
direccionLabel=Label(miFrame, text="Direccion: ")
direccionLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10) #Sticky, alinear con puntos cardinales N NW W
contraseñaLabel=Label(miFrame, text="Contraseña: ")
contraseñaLabel.grid(row=3, column=0, sticky="e")

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1)
cuadroNombre.config(fg="red", justify="center") #fg color fuente. justify. alineacion texto
cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1)
cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1)
cuadroContraseña=Entry(miFrame, show="*") #Show. para poner el caracter deseado
cuadroContraseña.grid(row=3, column=1)


raiz.mainloop()