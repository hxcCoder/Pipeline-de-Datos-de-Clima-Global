import pandas as pd
from google.cloud import bigquery
from google.oauth2 import service_account

def load_data_to_bigquery(dataframe: pd.DataFrame, table_id: str, project_id: str):
    """
    Carga un DataFrame de pandas a una tabla en Google BigQuery.
    """
    try:
        # Crea un cliente de BigQuery, pasando explícitamente el Project ID
        client = bigquery.Client(project=project_id)

        job = client.load_table_from_dataframe(dataframe, table_id)
        job.result()  # Espera a que el trabajo termine

        print(f"✅ Datos cargados correctamente en la tabla: {table_id}")

    except Exception as e:
        print(f"❌ Error al cargar datos a BigQuery: {e}")