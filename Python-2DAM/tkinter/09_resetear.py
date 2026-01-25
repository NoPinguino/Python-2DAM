import tkinter as tk


def limpiar():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)


root = tk.Tk()
root.geometry("600x400")
root.title("Limpiar campos")

entrada1 = tk.Entry(root)
entrada1.pack(pady=10)
entrada2 = tk.Entry(root)
entrada2.pack(pady=10)

btn_delete = tk.Button(root, text="LIMPIAR", command=limpiar)
btn_delete.pack()

root.mainloop()
