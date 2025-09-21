password  = "password123"
intento = input("Introduce la contraseña: ")
while intento != password:
    print("CONTRASEÑA INCORRECTA")
    intento = input("Introduce la contraseña: ")
print(f"La contraseña era {intento}")