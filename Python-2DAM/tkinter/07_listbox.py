import tkinter as tk


def seleccionado(event):
    # event.widget es el Listbox que disparó el evento
    index = listbox.curselection()  # devuelve una tupla de índices seleccionados
    if index:  # si hay algo seleccionado
        valor = listbox.get(index)
        print("Seleccionaste:", valor)


root = tk.Tk()
root.geometry("700x400")

listbox = tk.Listbox(root)
listbox.pack(pady=20)

# Añadimos algunos elementos
for item in ["Manzana", "Banana", "Cereza"]:
    listbox.insert(tk.END, item)

# Bind para detectar selección
listbox.bind("<<ListboxSelect>>", seleccionado)

root.mainloop()
