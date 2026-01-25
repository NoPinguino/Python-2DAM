import tkinter as tk

root = tk.Tk()
root.geometry("700x400")


def guardar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()

    texto = f"Nombre: {nombre} | Edad: {edad}"
    resultado.config(text=texto)


etiqueta_nombre = tk.Label(root, text="Nombre: ", font=("Arial", 16)).pack()
entry_nombre = tk.Entry(root, font=("Arial", 16))
entry_nombre.pack()


etiqueta_edad = tk.Label(root, text="Edad: ", font=("Arial", 16)).pack()
entry_edad = tk.Entry(root, font=("Arial", 16))
entry_edad.pack()


btn_resultado = tk.Button(text="Ver resultados", font=("Arial", 16), command=guardar)
btn_resultado.pack(pady=10)

resultado = tk.Label(root, text="", font=("Arial", 16))
resultado.pack()

root.mainloop()
