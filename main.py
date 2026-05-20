from src.load_csv import load_csv
from src.cleaner import clean_dataframe
from src.export_csv import export_csv
from src.recommender import recommend
from src.utils import validate_all

df = load_csv("data/raw/Sales.csv")
df_clean = clean_dataframe(df)

print("\n¿Qué quieres hacer?")

exportar = input("¿Exportar el archivo limpio? (s/n): ").strip().lower()
if exportar == "s":
    try:
        validate_all(df_clean)
        export_csv(df_clean, "data/processed/clean_sales.csv")
    except AssertionError as e:
        print(f"Error de validación, no se exportará el archivo: {e}")

recomendar = input("¿Quieres una recomendación de móvil? (s/n): ").strip().lower()
if recomendar == "s":
    results = recommend(df_clean)
    print(results.head())