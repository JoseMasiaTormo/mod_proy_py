import pandas as pd
import numpy as np
import re

def parse_memory_to_mb(value):
    """
    Convierte valores como '8 GB' a número en MB
    Devuelve 0 si el valor es NaN o no puede ser convertido
    """
    if pd.isna(value):
        return 0
    value = str(value).strip().upper()
    match = re.match(r"([\d.]+)\s*(GB|MB)?", value)
    if not match:
        return 0
    number = float(match.group(1))
    unit = match.group(2) if match.group(2) else "MB"
    if unit == "GB":
        number *= 1024
    return number # Aquí ya se encuentra en MB

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    
    # 1. Quitar los espacios en los nombres de columnas
    df.columns = df.columns.str.strip()
    
    # 2. Quitar espacios en los valores de texto
    str_cols = df.select_dtypes(include=['object']).columns
    for col in str_cols:
        df[col] = df[col].str.strip()
        
    # 3. Eliminar duplicados por modelo
    if "Models" in df.columns:
        df = df.drop_duplicates(subset=["Models"], keep="first")
        
    # 4. Converir Memory y Storage a float en MB
    for col in ["Memory", "Storage"]:
        if col in df.columns:
            df[col] = df[col].apply(parse_memory_to_mb)
            
    # 5. Unificar formatos de texto
    # Capitalizar correctamente columnas categóricas
    for col in ["Brands", "Models", "Colors", "Camera"]:
        if col in df.columns:
            df[col] = df[col].str.title()
            
    # Camera: normalizar booleano True/False
    if "Camera" in df.columns:
        df["Camera"] = df["Camera"].str.strip().str.capitalize()
        df["Camera"] = df["Camera"].map({"Yes": True, "No": False})
        
    # 6. Convertir tipos numéricos explícitamente
    numeric_cols = ["Rating", "Selling Price", "Original Price", "Discount", "discount percentage"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
            
    # 7. Tratar Nulos
    # Numéricos se rellenan con 0
    num_cols_all = df.select_dtypes(include=[np.number]).columns
    df[num_cols_all] = df[num_cols_all].fillna(0)
    
    # Categoricas se rellenan con "Unknown"
    cat_cols_all = df.select_dtypes(include=['object']).columns
    for col in cat_cols_all:
        df[col] = df[col].fillna("Unknown")
        
    # 8. Validar Precios
    # Selling Price y Original Price deben ser mayores o iguales a 0
    for price_col in ["Selling Price", "Original Price"]:
        if price_col in df.columns:
            invalid_mask = df[price_col] < 0
            if invalid_mask.any():
                print(f"[WARN] {invalid_mask.sum()} filas con {price_col} negativo -> se ponen a 0")
                df.loc[invalid_mask, price_col] = 0
    
    # Discount no puede ser mayor que Original Price
    if "Discount" in df.columns and "Original Price" in df.columns:
        bad_discount_mask = df["Discount"] > df["Original Price"]
        if bad_discount_mask.any():
            print(f"[WARN] {invalid_mask.sum()} filas con Discount mayor que Original Price -> se corrigen")
            df.loc[bad_discount_mask, "Discount"] = 0
            df.loc[bad_discount_mask, "discount percentage"] = 0.0
            
    # Recalcular discount percentage donde sea posible
    if all(c in df.columns for c in ["Discount", "Original Price", "discount percentage"]):
        mask = df["Original Price"] > 0
        df.loc[mask, "discount percentage"] = (df.loc[mask, "Discount"] / df.loc[mask, "Original Price"] * 100).round(6)
    
    return df