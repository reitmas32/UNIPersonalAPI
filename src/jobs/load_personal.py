from config import *
from models.personal import Personal
import config as CONFIG
import datetime

def load_personal():

    CONFIG.PERSONAL_LIST = []

    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Respuestas de formulario 2').execute()

    values = result.get('values', [])

    for value in values[1:]:

        if(len(value) >= 13):
            personal = Personal(
                nombre=value[CONFIG.NOMBRE],
                apellidos=value[CONFIG.APELLIDOS],
                nombre_corto=value[CONFIG.NOMBRE_CORTO], 
                fecha_de_nacimiento=value[CONFIG.FECHA_DE_NACIMIENTO], 
                numero_de_cuenta=value[CONFIG.NUMERO_DE_CUENTA], 
                correo=value[CONFIG.CORREO], 
                telefono=value[CONFIG.TELEFONO], 
                carrera=value[CONFIG.CARRERA], 
                rfc=value[CONFIG.RFC], 
                curp=value[CONFIG.CURP], 
                estatus=value[CONFIG.ESTATUS], 
                modalidad=value[CONFIG.MODALIDAD],
                update=value[CONFIG.UPDATE]
            )
            CONFIG.PERSONAL_LIST.append(personal)

    personal_dict = {}
    for personal in CONFIG.PERSONAL_LIST:
        personal_dict.setdefault(personal.numero_de_cuenta, []).append(personal)

    # Paso 2: Encontrar el objeto con la fecha "update" más reciente para cada "numero_de_cuenta"
    filtered_list = []
    for cuenta, personal_objs in personal_dict.items():
        latest_update = None
        latest_personal = None
        for personal in personal_objs:
            update_date = datetime.datetime.strptime(personal.update, '%d/%m/%Y %H:%M:%S')
            if latest_update is None or update_date > latest_update:
                latest_update = update_date
                latest_personal = personal
        filtered_list.append(latest_personal)

    CONFIG.PERSONAL_LIST = filtered_list

    CONFIG.bot.send_message(CONFIG.GROUP_ID, f'Se cargo el personal hay : {len(CONFIG.PERSONAL_LIST)}, personas activas en Sala 2')
