import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account
import telebot

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#API_KEY_GOOGLE_SHEET
KEY = os.getenv('KEY_DIR')

#ID_SHEET
SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')
BOT_TOKEN_API = os.getenv('BOT_TOKEN_API')
GROUP_ID = os.getenv('GROUP_ID')

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

UPDATE = 0
NOMBRE = 1
APELLIDOS = 2
NOMBRE_CORTO = 3
FECHA_DE_NACIMIENTO = 4
NUMERO_DE_CUENTA = 5
CORREO = 6
TELEFONO = 7
CARRERA = 8
RFC = 9
CURP = 10
ESTATUS = 11
MODALIDAD = 12

PERSONAL_LIST = []

DELTA_ZONE = 0


bot = telebot.TeleBot(BOT_TOKEN_API)
