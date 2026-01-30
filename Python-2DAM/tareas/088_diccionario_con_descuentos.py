productos = {
    "Leche": 1.15,
    "Pan": 0.55,
    "Cereales": 2.30,
    "Patata": 1.65,
    "Chuleta": 3.70,
}
productos_descuentos = {}
descuento = 10
for k in productos.keys():
    productos_descuentos[k] = round(productos[k] * (1 - descuento/100), 2)

print("PRODUCTOS CON DESCUENTO APLICADO:")
for k in productos_descuentos.keys():
    print(f"{k}: {productos_descuentos[k]}")