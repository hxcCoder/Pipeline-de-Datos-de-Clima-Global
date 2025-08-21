import pandas as pd

def transform_data(raw_data: dict) -> pd.DataFrame:
    """
    Transforma los datos JSON de la API en un DataFrame limpio.
    """
    if not raw_data:
        return pd.DataFrame()  # Devuelve un DataFrame vacío si no hay datos

    # Transforma el JSON en un DataFrame
    df_clima = pd.json_normalize(raw_data)

    # Selecciona solo las columnas que te interesan
    df_limpio = df_clima[['name', 'main.temp', 'main.humidity', 'wind.speed']]

    # Renombra las columnas para que sean más claras
    df_limpio.columns = ['ciudad', 'temperatura_k', 'humedad', 'velocidad_viento']
    
    return df_limpio