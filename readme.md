# 🌍 Global Weather Data Pipeline

### 📋 Resumen del Proyecto
Este proyecto implementa un **pipeline de datos automatizado (ETL)** para extraer, transformar y cargar información meteorológica en tiempo real de múltiples ciudades alrededor del mundo.  

Los datos son almacenados en **Google BigQuery** y posteriormente analizados mediante un **dashboard interactivo en Power BI**.  

El objetivo principal es **demostrar una solución de datos de extremo a extremo**, desde la adquisición de datos vía API hasta la presentación visual para la toma de decisiones.  

---

## ⚙️ Arquitectura del Pipeline
El sistema se compone de tres etapas principales:

1. **Extract (Extracción)**  
   - Conexión a la API de **OpenWeatherMap**.  
   - Obtención de datos en tiempo real para una lista predefinida de ciudades.  

2. **Transform (Transformación)**  
   - Procesamiento de datos en formato **JSON** utilizando **Pandas**.  
   - Normalización y unificación en un único **DataFrame**.  

3. **Load (Carga)**  
   - Carga del DataFrame en **Google BigQuery**.  
   - Autenticación gestionada de forma segura mediante **Google Cloud CLI** (sin exponer claves en el código).  

---

## 📊 Resultados y Dashboard
El producto final incluye un **dashboard interactivo en Power BI** con métricas como:  

- 🌡️ **Temperatura**  
- 💧 **Humedad**  
- 🌬️ **Velocidad del viento**  

📑 Puedes ver el dashboard completo aquí:  
👉 [Dashboard en PDF](./Dashboard_Clima.pdf)  

---

## 🛠️ Tecnologías Utilizadas
- **Python** → Lenguaje principal.  
- **Pandas** → Limpieza y transformación de datos.  
- **Requests** → Consumo de la API.  
- **Google BigQuery** → Almacenamiento en la nube.  
- **Google Cloud CLI** → Autenticación.  
- **Power BI** → Visualización y análisis.  
- **Git & GitHub** → Control de versiones y colaboración.  

---

## 🚀 Guía de Inicio Rápido
Ejecuta el proyecto en tu entorno local siguiendo estos pasos:

```bash
# 1. Clona el repositorio
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

# 2. Instala las dependencias
pip install -r requirements.txt

# 3. Configura tu clave de API en un archivo .env
echo OPENWEATHER_API_KEY="tu_clave_aqui" > .env

# 4. Autentica Google Cloud CLI
gcloud auth login

# 5. Ejecuta el pipeline
python main.py


