import tkinter as tk

root = tk.Tk()
root.title("Mi app.")
root.geometry("600x400")


def cambiar():
    etiqueta.config(text="ON")


etiqueta = tk.Label(root, text="OFF", pady=50)
etiqueta.pack()

btn_cambiar = tk.Button(root, text="Cambiar", command=cambiar)
btn_cambiar.pack()

root.mainloop()
