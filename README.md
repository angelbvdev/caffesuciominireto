# ☕ Cafe Sales ETL & Data Quality Pipeline

## Descripción del Proyecto
Este proyecto consiste en un pipeline de **Ingeniería de Datos (ETL)** diseñado para procesar, limpiar y estandarizar datos crudos de transacciones de ventas de una cafetería.

El objetivo principal es transformar un dataset "sucio" (con errores de sistema, tipos de datos incorrectos y valores nulos) en un activo de información confiable (Capa Silver) listo para análisis de negocio o ingestión en un Data Warehouse.

## Estructura del Dataset
El proceso toma un archivo CSV crudo (`dirty_cafe_sales.csv`) y genera un archivo limpio (`clean_cafe_sales.csv`).

### Problemas identificados en la fuente (Raw Data):
* **Integridad:** Valores nulos (`NaN`), placeholders de error (`ERROR`, `UNKNOWN`) y celdas vacías.
* **Tipos de Dato:** Columnas numéricas contaminadas con texto (ej. precios con strings).
* **Consistencia:** Formatos de texto mixtos (mayúsculas/minúsculas) y espacios en blanco.
* **Lógica de Negocio:** Cálculos de `Total Spent` erróneos en origen.

## Tecnologías Utilizadas
* **Python 3.12**
* **Pandas:** Para manipulación y transformación de dataframes.
* **NumPy:** Para manejo eficiente de valores numéricos y nulos.

## Lógica de Limpieza (Data Lineage)
El script aplica las siguientes reglas de negocio para asegurar la calidad del dato:

1.  **Estandarización de Nulos:** Se unificaron `UNKNOWN`, `ERROR` y `nan` bajo un mismo estándar (`np.nan`).
2.  **Casting de Tipos:**
    * Conversión forzada de `Price` y `Quantity` a numérico (los errores se convierten a nulos).
    * Parsing de `Transaction Date` a formato `datetime` ISO 8601.
3.  **Reglas de Integridad (Filtering):**
    * Se descartan transacciones sin `Item` (producto) o `Date` (fecha), ya que son inútiles para el análisis histórico.
    * Se descartan transacciones sin `Price` o `Quantity`.
4.  **Reglas de Enriquecimiento (Imputation):**
    * **Recálculo:** Se ignora la columna original `Total Spent` y se recalcula como `Quantity * Price` para garantizar precisión matemática.
    * **Categorías:** Los valores nulos en `Location` y `Payment Method` se imputan como "Unknown" para preservar el conteo de la transacción.
5.  **Limpieza de Texto:** `Trim` de espacios y formato `Title Case` para consistencia.

## Cómo ejecutar el proyecto

### Prerrequisitos
Tener instalado Python y la librería Pandas:
```bash
pip install pandas numpy