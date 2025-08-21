# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en la imagen
WORKDIR /app

# Copia los archivos de requerimientos y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código de tu proyecto al contenedor
COPY . .

# Establece las variables de entorno para la clave API
# El valor de la clave será provisto por Cloud Run de forma segura
ENV OPENWEATHER_API_KEY=""
ENV GOOGLE_APPLICATION_CREDENTIALS="/etc/gcloud/creds.json"

# Comando para ejecutar tu script
CMD ["python", "main.py"]