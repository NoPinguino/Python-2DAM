palabras = ["Hugo","Wassim","Misael","Wassim","Hugo"]
palindroma = False
if palabras == palabras[::-1]:
    palindroma = True
if palindroma:
    print("La lista es palindroma.")
else:
    print("La lista no es palindroma.")
