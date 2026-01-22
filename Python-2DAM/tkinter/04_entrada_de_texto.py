import tkinter as tk

root = tk.Tk()
root.geometry("400x300")


def mostrar():
    etiqueta.config(text=entrada.get())


entrada = tk.Entry(root)
entrada.pack()

boton = tk.Button(root, text="Mostrar label.", command=mostrar)
boton.pack()

etiqueta = tk.Label(root, text="")
etiqueta.pack()

root.mainloop()
