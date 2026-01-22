import tkinter as tk

root = tk.Tk()
root.title("Radio buttons.")
root.geometry("700x400")


def cambiar():
    etiqueta.config(fg=color.get())


color = tk.StringVar(value="black")

for c in ["red", "green", "blue"]:
    tk.Radiobutton(
        root, text=c, font=("Arial", 16), value=c, variable=color, command=cambiar
    ).pack()


etiqueta = tk.Label(
    root, text="Hola este tiempo cambia de color", font=("Arial", 16, "bold")
)
etiqueta.pack(pady=8)


root.mainloop()
