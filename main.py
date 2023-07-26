from PIL import Image, ImageColor

import os

def validar_tamano(imagen_path, min_tamano_kb, max_tamano_kb):
    tamano_kb = os.path.getsize(imagen_path) / 1024  # Convertir bytes a kilobytes
    return min_tamano_kb <= tamano_kb <= max_tamano_kb

def validar_dimensiones(imagen_path, alto_min, alto_max, ancho_min, ancho_max):
    img = Image.open(imagen_path)
    ancho, alto = img.size
    return alto_min <= alto <= alto_max and ancho_min <= ancho <= ancho_max

def validar_resolucion_dpi(imagen_path, dpi_min, dpi_max):
    img = Image.open(imagen_path)
    dpi = img.info.get('dpi', (300, 300))[0]  # Tomar el valor DPI horizontal (puedes cambiar a [1] para vertical)
    return dpi_min <= dpi <= dpi_max

def validar_posicion_punto(x, y, x_min, x_max, y_min, y_max):
    return x_min <= x <= x_max and y_min <= y <= y_max

# ...

def validar_color_hex(color_hex_or_rgb, r_min, r_max, g_min, g_max, b_min, b_max):
    # If the input is already an RGB tuple, use it directly
    if isinstance(color_hex_or_rgb, tuple) and len(color_hex_or_rgb) == 3:
        r, g, b = color_hex_or_rgb
    else:
        # Otherwise, assume it's a hexadecimal color value and convert it to an RGB tuple
        try:
            r, g, b = tuple(int(color_hex_or_rgb[i:i + 2], 16) for i in (1, 3, 5))
        except ValueError:
            return False

    return r_min <= r <= r_max and g_min <= g <= g_max and b_min <= b <= b_max


# ...
def validar_imagen(imagen_path):
    # Parámetros de validación de imagen
    tamano_min_kb = 4
    tamano_max_kb = 50
    alto_min, alto_max = 288, 288
    ancho_min, ancho_max = 240, 240
    dpi_min, dpi_max = 300, 300

    # Parámetros de validación de ojos y boca
    ojo_izq_x_min, ojo_izq_x_max = 24, 120
    ojo_izq_y_min, ojo_izq_y_max = 55, 180
    ojo_der_x_min, ojo_der_x_max = 80, 185
    ojo_der_y_min, ojo_der_y_max = 50, 180
    boca_x_min, boca_x_max = 50, 161
    boca_y_min, boca_y_max = 70, 252

    # Parámetros de validación de fondo blanco
    fondo_blanco_hex = "#ffffff"
    fondo_blanco_r_min, fondo_blanco_r_max = 220, 255
    fondo_blanco_g_min, fondo_blanco_g_max = 220, 255
    fondo_blanco_b_min, fondo_blanco_b_max = 220, 255

    img = Image.open(imagen_path)

    if not validar_tamano(imagen_path, tamano_min_kb, tamano_max_kb):
        return False
    if not validar_dimensiones(imagen_path, alto_min, alto_max, ancho_min, ancho_max):
        return False
    if not validar_resolucion_dpi(imagen_path, dpi_min, dpi_max):
        return False

    # Aquí puedes agregar la validación para los ojos y la boca si es necesario

    # Validación del fondo blanco (únicamente si se necesita)
    if img.mode == "RGB":
        pixels = img.getdata()
        colores_fondo = [pixel for pixel in pixels if validar_color_hex(pixel, fondo_blanco_r_min, fondo_blanco_r_max,
                                                                        fondo_blanco_g_min, fondo_blanco_g_max,
                                                                        fondo_blanco_b_min, fondo_blanco_b_max)]
        fondo_blanco = len(colores_fondo) > 0
    else:
        fondo_blanco = False

    return fondo_blanco

# Ejemplo de uso:
ruta_imagen = "./archivos_fotos/foto2_c.jpg"
es_valida = validar_imagen(ruta_imagen)
if es_valida:
    print("La imagen cumple con los parámetros de validación.")
else:
    print("La imagen no cumple con los parámetros de validación.")



