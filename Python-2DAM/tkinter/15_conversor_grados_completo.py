import tkinter as tk

root = tk.Tk()
root.geometry("600x400")
root.title("Conversor a Fahrenheit")

# Configurar grid
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)


# ─── Función ───
def convertir():
    try:
        celsius = float(entrada.get())
        fahrenheit = celsius * 9 / 5 + 32
        lbl_resultado.config(text=f"{fahrenheit:.2f} °F")
    except ValueError:
        lbl_resultado.config(text="Introduce un número válido")


# ─── Entrada ───
entrada = tk.Entry(root, font=("Arial", 24), justify="center")
entrada.grid(row=0, column=0, padx=40, pady=20, sticky="ew")

# ─── Botón ───
btn_calc = tk.Button(
    root,
    text="Convertir a Fahrenheit",
    font=("Arial", 16, "bold"),
    height=2,
    command=convertir,
)
btn_calc.grid(row=1, column=0, padx=40, pady=10, sticky="ew")

# ─── Resultado ───
lbl_resultado = tk.Label(
    root, text="", font=("Arial", 18), bg="#f0f0f0", relief="ridge", height=2
)
lbl_resultado.grid(row=2, column=0, padx=40, pady=20, sticky="ew")

# ─── Enter para convertir ───
entrada.bind("<Return>", lambda event: convertir())

root.mainloop()
