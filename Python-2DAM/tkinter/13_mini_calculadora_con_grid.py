import tkinter as tk

root = tk.Tk()
root.geometry("450x800")
root.title("Mini-Calculadora")

for i in range(6):
    root.rowconfigure(i, weight=1)
for i in range(4):
    root.columnconfigure(i, weight=1)

BTN_BASE = {
    "font": ("Arial", 16, "bold"),
    "bd": 0,
    "relief": "flat",
    "cursor": "hand2",
    "activeforeground": "#ffffff",
}

BTN_NUMBER = {
    **BTN_BASE,
    "bg": "#e0e0e0",
    "fg": "#000000",
    "activebackground": "#d5d5d5",
}

BTN_OPERATOR = {
    **BTN_BASE,
    "bg": "#ff9500",
    "fg": "#ffffff",
    "activebackground": "#e08900",
}

BTN_ACTION = {
    **BTN_BASE,
    "bg": "#c0c0c0",
    "fg": "#000000",
    "activebackground": "#b0b0b0",
}

entrada_calculadora = 0

# ─── Resultado ───
lbl_resultado = tk.Label(
    root,
    text=f"{entrada_calculadora}",
    font=("Arial", 36, "bold"),
    bg="#ffffff",
    fg="#333333",
    relief="ridge",
)
lbl_resultado.grid(row=0, column=0, columnspan=4, sticky="nsew")

# FILA 2
btn_ac = tk.Button(root, text="AC", **BTN_ACTION)
btn_ac.grid(row=1, column=0, sticky="nsew")

btn_masmenos = tk.Button(root, text="+/-", **BTN_ACTION)
btn_masmenos.grid(row=1, column=1, sticky="nsew")

btn_porcentaje = tk.Button(root, text="%", **BTN_ACTION)
btn_porcentaje.grid(row=1, column=2, sticky="nsew")

btn_dividir = tk.Button(root, text="÷", **BTN_OPERATOR)
btn_dividir.grid(row=1, column=3, sticky="nsew")

# FILA 3
btn_7 = tk.Button(root, text="7", **BTN_NUMBER)
btn_7.grid(row=2, column=0, sticky="nsew")

btn_8 = tk.Button(root, text="8", **BTN_NUMBER)
btn_8.grid(row=2, column=1, sticky="nsew")

btn_9 = tk.Button(root, text="9", **BTN_NUMBER)
btn_9.grid(row=2, column=2, sticky="nsew")

btn_multiplicar = tk.Button(root, text="x", **BTN_OPERATOR)
btn_multiplicar.grid(row=2, column=3, sticky="nsew")

# FILA 4
btn_4 = tk.Button(root, text="4", **BTN_NUMBER)
btn_4.grid(row=3, column=0, sticky="nsew")

btn_5 = tk.Button(root, text="5", **BTN_NUMBER)
btn_5.grid(row=3, column=1, sticky="nsew")

btn_6 = tk.Button(root, text="6", **BTN_NUMBER)
btn_6.grid(row=3, column=2, sticky="nsew")

btn_resta = tk.Button(root, text="-", **BTN_OPERATOR)
btn_resta.grid(row=3, column=3, sticky="nsew")

# FILA 5
btn_1 = tk.Button(root, text="1", **BTN_NUMBER)
btn_1.grid(row=4, column=0, sticky="nsew")

btn_2 = tk.Button(root, text="2", **BTN_NUMBER)
btn_2.grid(row=4, column=1, sticky="nsew")

btn_3 = tk.Button(root, text="3", **BTN_NUMBER)
btn_3.grid(row=4, column=2, sticky="nsew")

btn_suma = tk.Button(root, text="+", **BTN_OPERATOR)
btn_suma.grid(row=4, column=3, sticky="nsew")

# FILA 6
btn_0 = tk.Button(root, text="0", **BTN_NUMBER)
btn_0.grid(row=5, column=0, columnspan=2, sticky="nsew")

btn_punto = tk.Button(root, text=".", **BTN_ACTION)
btn_punto.grid(row=5, column=2, sticky="nsew")

btn_igual = tk.Button(root, text="=", **BTN_OPERATOR)
btn_igual.grid(row=5, column=3, sticky="nsew")

root.mainloop()
