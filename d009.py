""" from tkinter import *

root = Tk()
mensaje = Label(root, text="Este es un projecto hecho con tkinter para aprender python")
mensaje2 = Label(root, text="Hola como estas?")

root.title("Python day 9")
root.geometry("800x600+400+200")
mensaje.grid(row=1, column=0)
mensaje2.grid(row=0, column=0)

root.mainloop() """

#Ejercicios

""" from tkinter import *

root = Tk()
mensaje = Label(root, text="Mensaje uno").grid(row=0, column=0)
mensaje2 = Label(root, text="Mensaje dos").grid(row=0, column=1)

root.title("Ejercicio")
root.geometry("600x450+50+75")

root.mainloop() """