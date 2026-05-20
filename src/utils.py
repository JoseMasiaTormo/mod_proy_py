import pandas as pd

# Verifica que el DataFrame no esté vacío
def validate_not_empty(df: pd.DataFrame) -> None:
    assert not df.empty, "El Dataframe está vacío."

# Verifica que todas las columnas esperadas estén presentes en el DataFrame
def validate_required_columns(df: pd.DataFrame) -> None:
    required = ["Brands", "Models", "Colors", "Memory", "Storage", "Camera", "Rating", "Selling Price", "Original Price", "Mobile", "Discount", "discount percentage"]
    missing = [col for col in required if col not in df.columns]
    assert not missing, f"Columnas faltantes: {missing}"

# Verifica que los precios de venta y originales no sean negativos
def validate_no_negative_prices(df: pd.DataFrame) -> None:
    for col in ["Selling Price", "Original Price"]:
        if col in df.columns:
            assert (df[col] >= 0).all(), f"'{col}' contiene valores negativos."

# Verifica que el rating esté dentro del rango válido (0-5)
def validate_rating_range(df: pd.DataFrame) -> None:
    if "Rating" in df.columns:
        assert df["Rating"].between(0, 5).all(), "La columna 'Rating' debe estar entre 0 y 5."

# Verifica que el descuento no supere el precio original
def validate_discount_coherence(df: pd.DataFrame) -> None:
    if "Discount" in df.columns and "Original Price" in df.columns:
        assert (df["Discount"] <= df["Original Price"]).all(), \
            "La columna 'Discount' debe ser menor o igual que 'Selling Price'."

# Verifica que la columna Camera sea de tipo booleano
def validate_camera_boolean(df: pd.DataFrame) -> None:
    if "Camera" in df.columns:
        assert df["Camera"].dtype == bool, "La columna 'Camera' debe ser de tipo booleano."

# Verifica que Memory y Storage sean columnas numéricas
def validate_memory_and_storage_numeric(df: pd.DataFrame) -> None:
    for col in ["Memory", "Storage"]:
        if col in df.columns:
            assert pd.api.types.is_numeric_dtype(df[col]), \
                f"La columna '{col}' debe ser de tipo numérico."

def validate_all(df: pd.DataFrame) -> None:
    """
    Valida que el DataFrame cumpla con todas las condiciones requeridas.
    """
    validate_not_empty(df)
    validate_required_columns(df)
    validate_no_negative_prices(df)
    validate_rating_range(df)
    validate_discount_coherence(df)
    validate_camera_boolean(df)
    validate_memory_and_storage_numeric(df)
    print("Todas las validaciones han pasado correctamente.")