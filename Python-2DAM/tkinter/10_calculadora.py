import tkinter as tk


def conseguir_nums() -> tuple[float, float]:
    num1 = float(entrada_1.get())
    num2 = float(entrada_2.get())
    entrada_1.delete(0, tk.END)
    entrada_2.delete(0, tk.END)
    return num1, num2


def establecer_resultado(resultado: float):
    lbl_resultado.config(text=f"{resultado}")


def sumar():
    num1, num2 = conseguir_nums()
    establecer_resultado(num1 + num2)


def restar():
    num1, num2 = conseguir_nums()
    establecer_resultado(num1 - num2)


def multiplicar():
    num1, num2 = conseguir_nums()
    establecer_resultado(num1 * num2)


def dividir():
    num1, num2 = conseguir_nums()
    establecer_resultado(num1 / num2)


root = tk.Tk()
root.geometry("420x320")
root.title("Calculadora")
root.configure(bg="#f2f2f2")

contenedor = tk.Frame(root, bg="#f2f2f2")
contenedor.pack(expand=True, fill="both", padx=20, pady=20)

for i in range(4):
    contenedor.columnconfigure(i, weight=1)
    contenedor.rowconfigure(i, weight=1)

# ─── Entradas ──────────────────────────────────────
entrada_1 = tk.Entry(
    contenedor, font=("Arial", 14), justify="center", relief="flat"
)  # justify center para centrar
entrada_1.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=5)

entrada_2 = tk.Entry(
    contenedor, font=("Arial", 14), justify="center", relief="flat"
)  # justify center para centrar
entrada_2.grid(row=1, column=0, columnspan=4, sticky="nsew", pady=5)

# ─── Resultado ─────────────────────────────────────
lbl_resultado = tk.Label(
    contenedor,
    text="0",
    font=("Arial", 20, "bold"),
    bg="#ffffff",
    fg="#333333",  # foreground: color del texto
    relief="ridge",  # relief: estilos de borde (ridge es uno de ellos)
    padx=10,
    pady=10,
)
lbl_resultado.grid(row=2, column=0, columnspan=4, sticky="nsew", pady=10)

# ─── Botones ───────────────────────────────────────

tk.Button(
    contenedor,
    text="+",
    bg="#4caf50",
    activebackground="#43a047",
    command=sumar,
).grid(row=3, column=0, sticky="nsew", padx=4, pady=4)

tk.Button(
    contenedor,
    text="-",
    bg="#2196f3",
    activebackground="#1e88e5",
    command=restar,
).grid(row=3, column=1, sticky="nsew", padx=4, pady=4)

tk.Button(
    contenedor,
    text="×",
    bg="#ff9800",
    activebackground="#fb8c00",
    command=multiplicar,
).grid(row=3, column=2, sticky="nsew", padx=4, pady=4)

tk.Button(
    contenedor,
    text="÷",
    bg="#f44336",
    activebackground="#e53935",
    command=dividir,
).grid(row=3, column=3, sticky="nsew", padx=4, pady=4)

root.mainloop()
