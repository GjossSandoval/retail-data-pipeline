import pandas as pd
import logging

# Configuración de logs para la terminal
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

def extraer_ciudad(direccion):
    """Extrae la ciudad de una dirección completa."""
    try:
        # Ejemplo: "917 1st St, Dallas, TX 75001" -> Separa por comas y toma el índice 1 (" Dallas")
        ciudad = direccion.split(',')[1].strip()
        estado = direccion.split(',')[2].split(' ')[1] # Extrae el TX, MA, CA
        return f"{ciudad} ({estado})"
    except:
        return "Desconocida"

def procesar_datos_ventas(archivo_entrada, archivo_salida):
    logging.info(f"Iniciando extracción y limpieza del archivo: {archivo_entrada}")
    
    # 1. EXTRAER (Extract)
    df = pd.read_csv(archivo_entrada)
    logging.info(f"Filas originales: {len(df)}")
    
    # 2. TRANSFORMAR (Transform)
    # 2.1 Eliminar filas completamente vacías (valores nulos)
    df = df.dropna(how='all')
    
    # 2.2 Eliminar encabezados repetidos (pasa mucho al unir varios CSVs)
    df = df[df['Order Date'] != 'Order Date']
    
    # 2.3 Corregir tipos de datos (de texto a números y fechas)
    df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'])
    df['Price Each'] = pd.to_numeric(df['Price Each'])
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    
    # 2.4 Enriquecer el dataset (Crear columnas calculadas para el negocio)
    df['Total_Venta'] = df['Quantity Ordered'] * df['Price Each']
    df['Mes'] = df['Order Date'].dt.month
    df['Hora_Compra'] = df['Order Date'].dt.hour
    df['Ciudad'] = df['Purchase Address'].apply(extraer_ciudad)
    
    # 3. CARGAR (Load) - Exportar el "Dato Maestro"
    df.to_csv(archivo_salida, index=False)
    
    logging.info("Limpieza completada con éxito.")
    logging.info(f"Filas finales limpias: {len(df)}")
    logging.info(f"Archivo listo para Power BI guardado como: {archivo_salida}")

if __name__ == "__main__":
    # Nombres de los archivos
    input_csv = 'ventas_crudas.csv'
    output_csv = 'ventas_limpias_dashboard.csv'
    
    procesar_datos_ventas(input_csv, output_csv)