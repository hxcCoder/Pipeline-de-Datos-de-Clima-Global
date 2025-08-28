# 🌍 Global Weather Data Pipeline

### 📋 Project Overview
This project implements an automated data pipeline (ETL) to extract, transform, and load real-time weather data from multiple cities around the world.

The data is stored in Google BigQuery and subsequently analyzed using an interactive Power BI dashboard.

The main objective is to demonstrate an end-to-end data solution, from data acquisition via API to visual presentation for decision-making.

---
## ⚙️ Pipeline Architecture
The system consists of three main stages:

1. **Extract**
- Connection to the **OpenWeatherMap** API.
- Obtaining real-time data for a predefined list of cities.

2. **Transform**
- Processing data in **JSON** format using **Pandas**.
- Normalization and unification into a single **DataFrame**.

3. **Load**
- Loading the DataFrame into **Google BigQuery**.
- Authentication managed securely using the **Google Cloud CLI** (without exposing keys in the code).

---

## 📊 Results and Dashboard
The final product includes an interactive Power BI dashboard with metrics such as:

- 🌡️ **Temperature**
- 💧 **Humidity**
- 🌬️ **Wind Speed**

📑 You can view the full dashboard here:
👉 [PDF Dashboard](./Dashboard_Clima.pdf)

---

## 🛠️ Technologies Used
- **Python** → Main language.
- **Pandas** → Data cleansing and transformation.
- **Requests** → API consumption.
- **Google BigQuery** → Cloud storage.
- **Google Cloud CLI** → Authentication.
- **Power BI** → Visualization and analysis.
- **Git & GitHub** → Version control and collaboration.

---

## 🚀 Quick Start Guide
Run the project in your local environment by following these steps:

```bash
# 1. Clone the repository
git clone https://github.com/your_user/your_repository.git
cd your_repository

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set your API key in an .env file
echo OPENWEATHER_API_KEY="your_key_here" > .env

# 4. Authenticate Google Cloud CLI
gcloud auth login

# 5. Run the pipeline
python main.py


