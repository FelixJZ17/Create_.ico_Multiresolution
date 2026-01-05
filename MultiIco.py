from PIL import Image

def crear_ico(ruta_imagen, nombre_salida):
    img = Image.open(ruta_imagen)
    # Definimos los tamaños estándar de Windows
    tamanos = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    # Guardamos incluyendo todas las capas
    img.save(nombre_salida, format='ICO', sizes=tamanos)
    print(f"Icono multiresolución guardado como {nombre_salida}")

if __name__ == "__main__":
    # CAMBIA "tu_imagen.png" por el nombre de tu archivo real
    crear_ico("ico.png", "app_icon.ico")