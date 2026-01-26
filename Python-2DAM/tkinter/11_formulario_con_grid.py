import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
root.title("Mi primer formulario.")

for i in range(3):
    root.rowconfigure(i, weight=1)
for i in range(2):
    root.columnconfigure(i, weight=1)


lbl_nombre = tk.Label(text="Introduce el nombre: ")
lbl_edad = tk.Label(text="Introduce la edad: ")
entry_nombre = tk.Entry(root)
entry_edad = tk.Entry(root)
btn_enviar = tk.Button(text="ENVIAR FORMULARIO")

lbl_nombre.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
lbl_edad.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
entry_nombre.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)
entry_edad.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

btn_enviar.grid(row=2, column=0, columnspan=2, sticky="nsew", padx=20, pady=20)


root.mainloop()
