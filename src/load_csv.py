import os
import pandas as pd

def load_csv(path: str) -> pd.DataFrame:
    """
    Lee un CSV y devuelve un DataFrame.

    Args:
        path (str): Ruta al archivo CSV.

    Returns:
        pd.DataFrame: DataFrame con los datos del CSV.
        FileNotFoundError: Si el archivo no se encuentra en la ruta proporcionada.
        ValuerError: Si el archivo está vacio.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"El archivo {path} no existe.")
    
    if os.path.getsize(path) == 0:
        raise ValueError(f"El archivo {path} esta vacio.")
    
    df = pd.read_csv(path)
    
    if df.empty:
        raise ValueError(f"El archivo {path} esta vacio.")
    
    return df
