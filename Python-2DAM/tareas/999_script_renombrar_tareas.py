import os
import shutil

BASE_DIR = os.getcwd()

for item in os.listdir(BASE_DIR):
    ruta_carpeta = os.path.join(BASE_DIR, item)

    # Solo carpetas tipo tarea-XXX
    if os.path.isdir(ruta_carpeta) and item.startswith("tarea-"):
        numero = item.replace("tarea-", "")

        for archivo in os.listdir(ruta_carpeta):
            if archivo.endswith(".py"):
                origen = os.path.join(ruta_carpeta, archivo)
                nuevo_nombre = f"{numero}_{archivo}"
                destino = os.path.join(BASE_DIR, nuevo_nombre)

                print(f"MOVIENDO: {origen} -> {destino}")
                shutil.move(origen, destino)

        # Elimina la carpeta si queda vacía
        if not os.listdir(ruta_carpeta):
            os.rmdir(ruta_carpeta)
