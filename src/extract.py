import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

def get_data_from_api(city_name: str) -> dict:
    """
    Obtiene datos de clima de una API para una ciudad específica.
    La clave API se obtiene de una variable de entorno.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY") 
    
    if not api_key:
        print("Error: La variable de entorno OPENWEATHER_API_KEY no está configurada.")
        return {}

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza un error para códigos HTTP como 401 o 404
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return {}