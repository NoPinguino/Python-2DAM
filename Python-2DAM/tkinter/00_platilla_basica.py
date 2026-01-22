import tkinter as tk

root = tk.Tk()
root.title("Mi app.")
root.geometry("600x400")

tk.Label(root, text="Hola mundo", font=("Arial", 14)).pack()

root.mainloop()
