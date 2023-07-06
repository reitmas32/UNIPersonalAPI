from PIL import Image, ImageDraw, ImageFont

def generateImage(name: str) -> str:

    # Abrir la imagen existente
    imagen = Image.open("assets/cumple.jpg")

    # Crear un objeto ImageDraw para escribir en la imagen
    dibujo = ImageDraw.Draw(imagen)

    # Cargar la fuente y definir el tamaño del texto
    fuente = ImageFont.truetype("assets/fonts/Alanta.ttf", size=100, encoding="UTF-8")

    # Definir el texto a escribir
    texto = name

    # Obtener las dimensiones de la imagen
    ancho, alto = imagen.size

    # Obtener el ancho y la altura del texto

    ancho_texto, alto_texto = dibujo.textsize(text=texto, font=fuente)

    # Calcular la posición del texto centrado en la imagen
    posicion_x = (ancho - ancho_texto) // 2
    posicion_y = (alto - 330) // 2

    # Escribir el texto en la imagen
    dibujo.text((posicion_x, posicion_y), texto, fill=(115, 115, 115), font=fuente)

    # Guardar la imagen con el texto como un nuevo archivo
    imagen.save(f"assets/happy_birthday_cards/cumple_{name}.jpg")

    return f"assets/happy_birthday_cards/cumple_{name}.jpg"
