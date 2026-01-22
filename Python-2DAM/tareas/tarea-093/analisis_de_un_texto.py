#frase = input("Ingresa una frase: ")
frase = "No soy gay pero soy peruano y tengo una fantasia donde Perú invade Chile y Chile tiene que exportar esclavos femboys para satisfacer oficiales peruanos de alto rango. Me imagino que soy un comandante poderoso, alto, con una mandibula cuadrada y con musculos masivos. Mi femboy es un pequeño chileno timido con piel palida que viene a mi habitacion. Lo agarro con mis poderosos brazos y lo beso a la fuerza, presionando su pecho contra el mio. Lo tiro contra la cama  y despues lo abrazo con mis grandes y fuertes brazos peruanos haciendolo dormir en mi pecho. Algun otro hetero tiene este tipo de fantasias"
frase = frase.lower().split()

print("Diccionario de palabras: ")
diccionario_palabras = {}
for palabra in frase:
    if palabra in diccionario_palabras:
        diccionario_palabras[palabra] = diccionario_palabras[palabra] + 1
    else:
        diccionario_palabras[palabra] = 1

for entrada in sorted(diccionario_palabras):
    print(entrada, ":", diccionario_palabras[entrada])

print()

print("Diccionario de longitudes: ")
diccionario_longitud = {}
for palabra in frase:
    if len(palabra) in diccionario_longitud:
        diccionario_longitud[len(palabra)] += 1
    else:
        diccionario_longitud[len(palabra)] = 1
for longitud in sorted(diccionario_longitud):
    print(longitud, ":", diccionario_longitud[longitud])