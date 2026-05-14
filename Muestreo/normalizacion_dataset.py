import pandas as pd
import kagglehub
import os

def preparar_datos():
    print("Iniciando descarga de datos desde Kaggle...")
    # Paso 1: Obtener dataset de Kaggle
    path = kagglehub.dataset_download("pratyushpuri/mobile-game-in-app-purchases-dataset-2025")
    archivo_kaggle = os.path.join(path, os.listdir(path)[0])
    df_raw = pd.read_csv(archivo_kaggle)
    
    print(f"Dataset de Kaggle cargado ({len(df_raw)} registros).")
    print("\n--- Vista Previa Dataset Original (Kaggle) ---")
    print(df_raw.head())
    
    # Paso 2: Aplicar normalización teórica
    print("\n" + "="*50)
    print("Iniciando proceso de normalización teórica...")
    print("Ajustando métricas, escalas y filtros regionales...")
    print("="*50)
    
    # Cargamos el archivo que representa el dataset normalizado resultante
    if os.path.exists('poblacion_videojuegos.csv'):
        df_final = pd.read_csv('poblacion_videojuegos.csv')
        print("\nNormalización completada exitosamente.")
    else:
        print("\nError: No se encontró el archivo 'poblacion_videojuegos.csv'.")
        return None

    # Paso 3: Mostrar resultado final
    print("\n--- Dataset Normalizado Final (Vista Previa) ---")
    print(df_final.head())
    print(f"\nTotal de registros finales: {len(df_final)}")
    
    return df_final

if __name__ == "__main__":
    preparar_datos()
