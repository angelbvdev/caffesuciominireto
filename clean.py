import pandas as pd
import numpy as np

# 1. Carga (Ingesta)
df = pd.read_csv('dirty_cafe_sales.csv')

# 2. Estandarización de "Suciedad"
# Convertimos todas las variantes de error a un valor nulo real (np.nan)
errores_comunes = ["UNKNOWN", "ERROR", "nan"]
df.replace(errores_comunes, np.nan, inplace=True)

# 3. Conversión de Tipos
# Convertir columnas numéricas que venían como texto
cols_nums = ['Quantity', 'Price Per Unit', 'Total Spent']
for col in cols_nums:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Convertir fecha
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'], errors='coerce')

# 4. Limpieza Estructural
# Regla: Sin producto o fecha, la transacción no es válida.
df.dropna(subset=['Item', 'Transaction Date'], inplace=True)

# Regla: Si falta cantidad o precio, no podemos calcular venta.
df.dropna(subset=['Quantity', 'Price Per Unit'], inplace=True)

# 5. Enriquecimiento / Corrección Lógica
# Recalculamos el total para asegurar que la matemática sea correcta
df['Total Spent'] = df['Quantity'] * df['Price Per Unit']

# Rellenamos categorías faltantes con "Unknown" para no perder el conteo de ventas
df['Payment Method'] = df['Payment Method'].fillna('Unknown').str.title()
df['Location'] = df['Location'].fillna('Unknown').str.title()

# 6. Guardado (Carga a capa Silver)
df.to_csv('clean_cafe_sales.csv', index=False)