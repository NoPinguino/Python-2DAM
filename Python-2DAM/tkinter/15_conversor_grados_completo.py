import tkinter as tk

root = tk.Tk()
root.geometry("600x450")
root.title("Conversor de Temperatura")

# Configurar grid
for i in range(4):
    root.rowconfigure(i, weight=1)
root.columnconfigure(0, weight=1)

# ─── Variable de modo ───
modo = tk.StringVar(value="CtoF")


# ─── Función ───
def convertir():
    try:
        valor = float(entrada.get())

        if modo.get() == "CtoF":
            resultado = valor * 9 / 5 + 32
            lbl_resultado.config(text=f"{resultado:.2f} °F")
        else:
            resultado = (valor - 32) * 5 / 9
            lbl_resultado.config(text=f"{resultado:.2f} °C")

    except ValueError:
        lbl_resultado.config(text="Introduce un número válido")


# ─── Entrada ───
entrada = tk.Entry(root, font=("Arial", 24), justify="center")
entrada.grid(row=0, column=0, padx=40, pady=10, sticky="ew")

# ─── Selector ───
frame_opciones = tk.Frame(root)
frame_opciones.grid(row=1, column=0)

tk.Radiobutton(
    frame_opciones,
    text="Celsius -> Fahrenheit",
    variable=modo,
    value="CtoF",
    font=("Arial", 12),
).pack(side="left", padx=20)

tk.Radiobutton(
    frame_opciones,
    text="Fahrenheit -> Celsius",
    variable=modo,
    value="FtoC",
    font=("Arial", 12),
).pack(side="left", padx=20)

# ─── Botón ───
btn_calc = tk.Button(
    root,
    text="Convertir",
    font=("Arial", 16, "bold"),
    height=2,
    command=convertir,
)
btn_calc.grid(row=2, column=0, padx=40, pady=10, sticky="ew")

# ─── Resultado ───
lbl_resultado = tk.Label(
    root,
    text="",
    font=("Arial", 18),
    bg="#f0f0f0",
    relief="ridge",
    height=2,
)
lbl_resultado.grid(row=3, column=0, padx=40, pady=20, sticky="ew")

# ─── Enter para convertir ───
entrada.bind("<Return>", lambda event: convertir())

root.mainloop()
