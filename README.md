# retail-data-pipeline
End-to-end data pipeline: Data extraction, cleaning (ETL) with Python/Pandas, and interactive sales dashboard in Power BI.
# 📊 Retail Intelligence Pipeline: ETL & Data Visualization

Un proyecto completo de análisis de datos que abarca desde la extracción y limpieza de datos crudos utilizando **Python (Pandas)**, hasta la creación de un dashboard interactivo para la toma de decisiones comerciales en **Power BI**.

## 🛠️ Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Librerías ETL:** Pandas, Logging
* **Inteligencia de Negocios (BI):** Power BI

## ⚙️ Arquitectura del Proyecto

El proyecto se divide en dos fases principales:

### 1. Procesamiento de Datos (Data Engineering)
El script `etl_ventas.py` simula un entorno de ingesta de datos del mundo real. Realiza las siguientes operaciones sobre datos sucios de ventas:
* Eliminación de valores nulos (NaN) y artefactos de exportación (encabezados duplicados).
* *Type Casting*: Conversión estricta de cadenas de texto a valores numéricos (`float`, `int`) y objetos `datetime`.
* *Feature Engineering*: Generación de nuevas variables de valor para el negocio, incluyendo cálculo de ingresos (`Total_Venta`), extracción de franjas horarias (`Hora_Compra`) y *parsing* de direcciones para obtener la `Ciudad`.

### 2. Visualización e Insights (Data Analysis)
El archivo resultante (`ventas_limpias_dashboard.csv`) se conecta a Power BI para responder preguntas críticas de negocio:
* Identificación de los productos más rentables (Principio de Pareto).
* Análisis geoespacial de concentración de clientes.
* Identificación de horas pico para optimización de campañas de marketing.

## 🚀 Cómo ejecutar el proyecto
1. Clona este repositorio.
2. Asegúrate de tener Pandas instalado: `pip install pandas`
3. Ejecuta el pipeline de limpieza:
   ```bash
   python etl_ventas.py
