## PROYECTO MODULAR PYTHON

### 1) Objetivo

- Analizar un dataset con información de **Smartphones** más viejos y más actuales para entender mejor el mercado y además entender bien como funciona la limpieza de datos, construcción de características y generación de visualizaciones.

### 2) Dataset

- Fuente: [Smartphone Sale Dataset in Kaggle](https://www.kaggle.com/datasets/yaminh/smartphone-sale-dataset)
- Nº filas/columnas: 3114 Filas y 12 Columnas
- Variables clave: Las columnas más importantes a nivel categórico son, **Brands** y **Models**

### 3) Preguntas

- Q1: ¿Cómo se distribuyen los datos después de la limpieza?
- Q2: ¿Qué características nuevas se pueden derivar?
- Q3: ¿Qué insights se obtienen de las visualizaciones?
- Q4: ¿Que marca acumula más variedad de modelos únicos?
- Q5: ¿Cómo se distribuyen los precios de venta entre las distintas marcas?
- Q6: ¿Existe relación visible entre el precio de venta y el rating de los usuarios?

### 4) Data issues & fixes

- Valores nulos y duplicados → Eliminación o tratamiento de estos en src/cleaner.py.
- Camera en Yes o No → Transoformación a True o False.
- Precios inconsistentes → Tratamiento y Recálculo de precios y descuentos para que se queden en la franja que les toca.
- Formatos innecesarios → Conversión de tipos de datos y transformación de a MB de muchos campos.

### 5) Pipeline

- raw → clean → utils(validate) → export → (feature opcional) recommend

### 6) Hallazgos (Falta)

- Insight 1: Distribución de datos limpia (con referencia a gráfico generado)
- Insight 2: Características derivadas mejoran el análisis
- Insight 3: Visualizaciones revelan patrones clave

### 7) Contenido del proyecto

- `src/` contiene funciones reutilizables (`cleaner`, `export_csv`, `load_csv`, `recommender`, `utils(validation)`)
- `main.py` ejecuta el pipeline end-to-end
- `notebooks/graphics.ipynb` contiene los gráficos y las conclusiones de estos

### 8) Cómo ejecutar

- `pip install -r requirements.txt`
- Ejecutar pipeline: `python main.py`
- Abrir y ejecutar con el dataset limpio: `notebooks/graphics.ipynb` (Para ver graficos y conclusiones)
- (Opcional) Abrir y ejecutar: `notebooks/eda.ipynb`

### 9) Conclusión

Este proyecto demuestra que antes de extraer cualquier conclusión útil de un dataset, la calidad del dato es lo primero. Un dataset de 3114 smartphones con valores nulos, formatos inconsistentes y duplicados no cuenta nada por sí solo; solo después de pasar por el pipeline de limpieza, validación y transformación los datos se vuelven fiables y analizables.

El resultado es un conjunto de datos estructurado desde el que se puede responder preguntas reales sobre el mercado de smartphones: qué marcas dominan, en qué rangos de precio se concentra la oferta o qué relación existe entre almacenamiento, rating y precio final. El módulo de recomendación es una consecuencia directa de esa limpieza: sin datos coherentes en columnas como `Storage`, `Rating` o `Selling Price`, filtrar por criterios del usuario no tendría ningún sentido.

En definitiva, el valor del proyecto no está solo en las visualizaciones o en el recomendador, sino en haber construido un pipeline reproducible y modular que convierte datos crudos en información accionable.

## Estructura del proyecto

Estructura:

```
mod_proy_py/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── eda.ipynb
│   └── graphics.ipynb
├── src/
│   ├── cleaner.py
│   ├── export_csv.py
│   ├── load_csv.py
│   ├── recommender.py
│   └── utils.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt

```
