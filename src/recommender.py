import pandas as pd

def recommend(df: pd.DataFrame) -> pd.DataFrame:
    """
    Pide presupuesto, almacenamiento mínimo en MB y rating mínimo,
    y devuelve los móviles que cumplen todos los criterios.

    Args
    df: DataFrame ya limpio

    Devuelve:
    DataFrame con las coincidencias, o vacío si no hay ninguna.
    """
    try:
        budget = float(input("Presupuesto máximo (en la moneda del dataset): "))
        storage = float(input("Almacenamiento mínimo (en MB): "))
        rating = float(input("Rating mínimo: "))
    except ValueError:
        raise ValueError("Los valores introducidos no son válidos. Deben ser números.")

    matches = df[
        (df["Selling Price"] <= budget) &
        (df["Storage"] >= storage) &
        (df["Rating"] >= rating)
    ][["Mobile", "Selling Price", "Storage", "Rating"]]

    if matches.empty:
        print("No se encontraron móviles que cumplan los criterios.")
    else:
        print(f"{len(matches)} coincidencia(s) encontrada(s).")

    return matches