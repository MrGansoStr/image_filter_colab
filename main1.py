from PIL import Image, ImageFilter

def redimensionar_imagen(imagen_path, nuevo_ancho, nuevo_alto):
    img = Image.open(imagen_path)
    img_resized = img.resize((nuevo_ancho, nuevo_alto), Image.LANCZOS)
    return img_resized


def ajustar_dpi(imagen, nuevo_dpi):
    imagen.info['dpi'] = (nuevo_dpi, nuevo_dpi)
    return imagen

def cambiar_fondo_blanco(imagen, fondo_hex="#ffffff"):
    fondo_blanco = Image.new('RGB', imagen.size, color=fondo_hex)
    img_composite = Image.alpha_composite(fondo_blanco.convert('RGBA'), imagen.convert('RGBA'))
    return img_composite

# Ejemplo de uso:
ruta_imagen = "./archivos_fotos/fot2_corregida.jpg"

# No need to validate the image if you are directly correcting it
img_corregida = redimensionar_imagen(ruta_imagen, 240, 288)
img_corregida = ajustar_dpi(img_corregida, 300)
img_corregida = cambiar_fondo_blanco(img_corregida)

# Convert the image to RGB mode before saving as JPEG
img_corregida_rgb = img_corregida.convert('RGB')

# Guardar la imagen corregida con un nuevo nombre o en una ubicación diferente
ruta_imagen_corregida = "./archivos_fotos/fot2_corregida.jpg"
img_corregida_rgb.save(ruta_imagen_corregida)

print("La imagen ha sido corregida y guardada en:", ruta_imagen_corregida)
