import tkinter as tk

root = tk.Tk()
root.geometry("400x300")


def sumar():
    suma = int(entrada_num1.get()) + int(entrada_num2.get())
    etiqueta.config(text=suma)


entrada_num1 = tk.Entry(root)
entrada_num1.pack(pady=6)

entrada_num2 = tk.Entry(root)
entrada_num2.pack(pady=6)

boton = tk.Button(root, text="Calcular", font=("Arial", 16), command=sumar)
boton.pack()

etiqueta = tk.Label(root, text="", font=("Arial", 16))
etiqueta.pack()

root.mainloop()
