🚀 Pipeline de Datos de Clima Global

📋 Descripción del Proyecto
Este proyecto es un pipeline de datos automatizado que extrae, transforma y carga (ETL) datos de clima en tiempo real de múltiples ciudades alrededor del mundo. Los datos son procesados y almacenados en una base de datos en la nube (Google BigQuery) para su posterior análisis y visualización.

⚙️ Arquitectura del Pipeline
El flujo de trabajo sigue un proceso de ETL claro y modular:

Extracción (Extract): Se obtienen datos de la API de OpenWeatherMap. El script maneja la autenticación de la API de forma segura a través de variables de entorno.

Transformación (Transform): Los datos JSON son limpiados, estandarizados y convertidos en un DataFrame de pandas. Se unifican los datos de múltiples ciudades en un solo DataFrame.

Carga (Load): El DataFrame final se sube a una tabla en Google BigQuery. El script se autentica automáticamente con las credenciales de la CLI de Google Cloud, asegurando una conexión segura a la base de datos en la nube.

🛠️ Tecnologías Utilizadas
Python: Lenguaje de programación principal.

Pandas: Para la transformación y manipulación de datos.

Requests: Para hacer llamadas a la API de clima.

Google Cloud BigQuery: Base de datos en la nube para el almacenamiento de datos.

Google Cloud CLI: Para la autenticación segura y la gestión del proyecto.

Power BI: Herramienta de Business Intelligence para la visualización de datos.

📊 Dashboard de Análisis
El resultado final del pipeline es un dashboard interactivo que visualiza los datos de clima globales, demostrando la capacidad de convertir datos crudos en información valiosa. A continuación, se puede ver un ejemplo del dashboard creado en Power BI.

Ver Dashboard Completo en PDF

🚀 Cómo Ejecutar el Proyecto
Para ejecutar el pipeline localmente, asegúrate de tener las librerías necesarias instaladas y las credenciales de Google Cloud configuradas.

Clona este repositorio.

Instala las dependencias: pip install -r requirements.txt

Ejecuta el script principal: python main.py
