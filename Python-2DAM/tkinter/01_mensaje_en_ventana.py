import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Mi app.")
root.geometry("600x400")


def saludar():
    messagebox.showinfo("Saludo", "¡Hola mundo!")


tk.Label(root, text="Hola mundo", font=("Arial", 14)).pack(padx=60, pady=60)
boton = tk.Button(root, text="Saludar", command=saludar).pack(pady=20)


root.mainloop()
