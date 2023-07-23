# Etapa de construcción
FROM python:3.9-alpine

# Establecer el directorio de trabajo en /app
WORKDIR /app

ENV TZ=America/Mexico_City

# Copiar los archivos de la aplicación a la imagen
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src /app/src
COPY ./assets /app/assets

WORKDIR /app/src

# Instalar las dependencias de compilación
RUN python3 main.py > /dev/null 2>&1 &
# Comando para ejecutar la aplicación Flask y especificar el archivo principal
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]