import os
import pandas as pd

def export_csv(df: pd.DataFrame, path: str) -> None:
    """
    Exporta un DataFrame a un archivo CSV.
    
    Args:
        df (pd.DataFrame): DataFrame a exportar.
        path (str): Ruta al archivo CSV.
        
    Lanza:
        ValueError: Si el DataFrame está vacio.
    """

    if df.empty:
        raise ValueError("El DataFrame esta vacio.")
    
    dir_path = os.path.dirname(path)
    if dir_path and not os.path.exists(dir_path):
        os.makedirs(dir_path)

    df.to_csv(path, index=False)
    print(f"Archivo exportado correctamente: {path}")