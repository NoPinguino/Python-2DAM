import tkinter as tk
import tkinter.font as tkFont

# -----------------------------
# 1 => Ventana principal
# -----------------------------
root = tk.Tk()
root.geometry("600x400")
root.title("Tablas de multiplicar")


# -----------------------------
# 2 => Función para calcular la tabla de multiplicar
# -----------------------------
def calcular():
    # Limpiar los widgets anteriores dentro del frame 'resultados'
    for w in resultados.winfo_children():
        w.destroy()

    try:
        # Obtener el número de la entrada
        num = int(entrada.get())
    except ValueError:
        num = "Error: entrada no válida"

    # Crear etiquetas con cada resultado
    # Usamos 'pack' con 'anchor="center"' para centrar horizontalmente
    for i in range(11):
        if num == "Error: entrada no válida":
            tk.Label(resultados, font=myFont, text=f"{num}").pack(
                anchor="center", pady=2
            )  # 'pady' agrega un pequeño espacio vertical
        else:
            tk.Label(resultados, font=myFont, text=f"{i} x {num} = {i * num}").pack(
                anchor="center", pady=2
            )  # 'pady' agrega un pequeño espacio vertical


# -----------------------------
# 3 => Entrada y botón
# -----------------------------
entrada = tk.Entry(root, font=("Arial", 14))
entrada.pack(pady=10)

tk.Button(root, text="CALCULAR", command=calcular).pack(pady=5)

# -----------------------------
# 4 => Contenedor scrolleable: Canvas + Scrollbar
# -----------------------------

# Creamos un canvas que contendrá el frame con los resultados
canvas = tk.Canvas(root)
canvas.pack(side="left", fill="both", expand=True)

# Scrollbar vertical asociada al canvas
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

# Configuramos el canvas para que el scrollbar controle la vista
canvas.configure(yscrollcommand=scrollbar.set)

# -----------------------------
# 5 => Frame donde pondremos los resultados
# -----------------------------
# Este frame "reside" dentro del canvas
resultados = tk.Frame(canvas)
canvas.create_window((0, 0), window=resultados)


# -----------------------------
# 6 => Ajuste automático del scroll
# -----------------------------
def ajustar_scroll(event):
    # Cada vez que el tamaño de 'resultados' cambia, actualizamos el scrollregion
    canvas.configure(scrollregion=canvas.bbox("all"))


resultados.bind("<Configure>", ajustar_scroll)

# -----------------------------
# 7 => Fuente para los resultados
# -----------------------------
myFont = tkFont.Font(size=18)

# -----------------------------
# 8 => Ejecutar la ventana
# -----------------------------
root.mainloop()
