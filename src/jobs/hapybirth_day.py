import datetime
from models.job import Job
import config as CONFIG

from tools.generate_image_birtday import generateImage

def felicitar_cumple():
    fecha_actual = datetime.datetime.now().strftime('%d-%m')

    for personal in CONFIG.PERSONAL_LIST:
        nombre = personal.nombre_corto
        fecha_nacimiento = personal.fecha_de_nacimiento
        fecha_nacimiento_date = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y")
        fecha_nacimiento_dm = datetime.datetime.strftime(fecha_nacimiento_date, "%d-%m")
        print(f'Hoy {fecha_actual}, Cumple {fecha_nacimiento_dm}')
        if fecha_nacimiento_dm == fecha_actual:
            image = generateImage(name=nombre)
            mensaje = f'¡Feliz cumpleaños, {nombre}!'
            with open(image, 'rb') as photo:
                CONFIG.bot.send_photo(CONFIG.GROUP_ID, photo)
                CONFIG.bot.send_message(CONFIG.GROUP_ID, mensaje)
