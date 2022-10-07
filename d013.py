""" from tkinter import *

root = Tk()

root.title("Curso de Tkinter")

entrada = Entry(root)
entrada.insert(0, "Escriba su nombre.")
entrada.bind("<Button-1>",lambda e: entrada.delete(0, END))
entrada.pack()

def pulsar_boton():
    nombre = entrada.get()
    Label(root, text=f"{nombre}").pack()

Button(root, text="Enviar", command=pulsar_boton).pack()

root.mainloop() """

#Ejercicios

""" from tkinter import *

root = Tk()

def btn1():
    Label(root, text="Pulsaste el boton 1").pack()

def btn2():
    Label(root, text="Pulsaste el boton 2").pack()

def btn3():
    Label(root, text="Pulsaste el boton 3").pack()

def btn4():
    Label(root, text="Pulsaste el boton 4").pack()


Button(root, text="Boton 1", command=btn1).pack()
Button(root, text="Boton 2", command=btn2).pack()
Button(root, text="Boton 3", command=btn3).pack()
Button(root, text="Boton 4", command=btn4).pack()


root.mainloop() """

from tkinter import *

root = Tk()

root.title("Curso de Tkinter")

Label(root, text="Nombre:").grid(row=0, column=0)
 
Label(root, text="Edad:").grid(row=1, column=0)

#Nombre
entrada1 = Entry(root)
entrada1.grid(row=0, column=1)
#Edad
entrada2 = Entry(root)
entrada2.grid(row=1, column=1)

def btn():
    nombre = entrada1.get()
    edad = entrada2.get()
    Label(root, text=f"Hola {nombre}, tienes {edad} años").grid(row=3, column=1)

Button(root, text="Enviar", command=btn).grid(row=2, column=1)

root.mainloop()