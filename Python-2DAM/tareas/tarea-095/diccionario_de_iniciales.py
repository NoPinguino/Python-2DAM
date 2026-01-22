#frase = input("Ingresa una frase: ")
frase = "No soy gay pero soy peruano y tengo una fantasia donde Perú invade Chile y Chile tiene que exportar esclavos femboys para satisfacer oficiales peruanos de alto rango. Me imagino que soy un comandante poderoso, alto, con una mandibula cuadrada y con musculos masivos. Mi femboy es un pequeño chileno timido con piel palida que viene a mi habitacion. Lo agarro con mis poderosos brazos y lo beso a la fuerza, presionando su pecho contra el mio. Lo tiro contra la cama  y despues lo abrazo con mis grandes y fuertes brazos peruanos haciendolo dormir en mi pecho. Algun otro hetero tiene este tipo de fantasias"
frase = frase.lower().split()

print("Diccionario de iniciales: ")
diccionario_iniciales = {}
for palabra in frase:
    if palabra[0] in diccionario_iniciales:
        diccionario_iniciales[palabra[0]] += 1
    else:
        diccionario_iniciales[palabra[0]] = 1

for longitud in sorted(diccionario_iniciales):
    print(longitud, ":", diccionario_iniciales[longitud])