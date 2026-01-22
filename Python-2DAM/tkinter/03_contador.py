import tkinter as tk

root = tk.Tk()
root.title("Mi app.")
root.geometry("600x400")

contador = 0


def aumentar():
    global contador
    contador += 1
    etiqueta.config(text=contador)


def disminuir():
    global contador
    contador -= 1
    etiqueta.config(text=contador)


etiqueta = tk.Label(root, text=contador, pady=50)
etiqueta.pack()

btn_sumar = tk.Button(root, text="MAS", command=aumentar).pack()
btn_restar = tk.Button(root, text="MENOS", command=disminuir).pack()

root.mainloop()
