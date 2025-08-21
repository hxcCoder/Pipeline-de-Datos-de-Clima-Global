# main.py
from src.extract import get_data_from_api
from src.transform import transform_data
from src.load import load_data_to_bigquery
import pandas as pd

if __name__ == "__main__":
    
    print("--- 🚀 Iniciando pipeline de datos ---")

    # Lista de ciudades para obtener los datos
    ciudades = ["Santiago", "London", "Paris", "Tokyo"]
    
    # Creamos una lista para guardar los DataFrames de cada ciudad
    all_dfs = []

    for ciudad in ciudades:
        print(f"Buscando datos para: {ciudad}")
        # Paso 1: Extracción de datos
        datos_crudos = get_data_from_api(city_name=ciudad)
        
        if datos_crudos:
            print(f"✅ Datos de {ciudad} obtenidos correctamente.")
            # Paso 2: Transformación de datos
            df_limpio = transform_data(datos_crudos)
            all_dfs.append(df_limpio)
        else:
            print(f"❌ Fallo al obtener los datos de {ciudad}.")

    if all_dfs:
        # Concatenamos todos los DataFrames en uno solo
        final_df = pd.concat(all_dfs, ignore_index=True)
        print("\n--- DataFrame Unificado ---")
        print(final_df)
        print("---------------------------")

        # Paso 3: Carga de datos en la nube
        project_id = "tu-proyecto"
        dataset_id = "tu-dataset"
        table_name = "tu-tabla" # O 'datos_clima_global'
        table_id = f"{project_id}.{dataset_id}.{table_name}"
        
        load_data_to_bigquery(final_df, table_id, project_id)
    else:
        print("❌ Ningún dato pudo ser extraído. El pipeline ha terminado.")

    print("\n--- ✅ Pipeline finalizado ---")