##🚀 Global Weather Data Pipeline

###📋 Resumen del Proyecto
Este proyecto es un pipeline de datos automatizado diseñado para extraer, transformar y cargar (ETL) datos de clima en tiempo real de múltiples ciudades alrededor del mundo. La información procesada se almacena en Google BigQuery, una base de datos en la nube, para su posterior análisis y visualización.

El objetivo principal es demostrar la capacidad de construir una solución de datos de extremo a extremo, desde la adquisición de datos de una API hasta la presentación de resultados en un dashboard interactivo.

###⚙️ Arquitectura del Pipeline
El sistema opera a través de un proceso de tres etapas:

Extract (Extracción): El script se conecta a la API de OpenWeatherMap para obtener datos crudos y en tiempo real de una lista predefinida de ciudades.

Transform (Transformación): Los datos JSON son procesados y estandarizados utilizando Pandas. Los datos de todas las ciudades son unificados en un solo DataFrame, listo para su almacenamiento.

Load (Carga): El DataFrame final se carga en una tabla de Google BigQuery. La autenticación se maneja de forma segura usando la CLI de Google Cloud, eliminando la necesidad de claves en el código.

📈 Resultados y Dashboard de Análisis
El producto final del pipeline es un dashboard interactivo en Power BI que permite analizar y comparar la temperatura, humedad y velocidad del viento de las diferentes ciudades.

Puedes ver el dashboard completo en formato PDF: Ver Dashboard Completo en PDF

🛠️ Tecnologías Utilizadas
Python: Lenguaje principal.

Pandas: Manipulación y transformación de datos.

Requests: Para interactuar con la API.

Google BigQuery: Almacenamiento de datos en la nube.

Google Cloud CLI: Autenticación.

Power BI: Visualización y análisis de datos.

Git & GitHub: Control de versiones.

🚀 Guía de Inicio Rápido
Para ejecutar este proyecto localmente, sigue estos pasos:

Clona el repositorio: git clone https://github.com/tu_usuario/tu_repositorio.git

Instala las dependencias: pip install -r requirements.txt

Configura tu clave de API: Crea un archivo .env en la raíz del proyecto y añade tu clave: OPENWEATHER_API_KEY="tu_clave_aqui"

Autentica con Google Cloud: Asegúrate de que tu gcloud CLI esté autenticado.

Ejecuta el pipeline: python main.py
