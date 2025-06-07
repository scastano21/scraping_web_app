import streamlit as st
import pandas as pd
import os
import subprocess

# Ejecutar scraping si no existe el CSV
csv_path = "data/producto.csv"
if not os.path.exists(csv_path):
    st.warning("Archivo CSV no encontrado. Ejecutando scraping...")
    subprocess.run(["python", "scraping.py"])

# Mostrar título y datos
st.title("Precio del Samsung Galaxy S23 Ultra")

try:
    df = pd.read_csv(csv_path)
    st.write(df)
except FileNotFoundError:
    st.error("No se pudo generar el archivo producto.csv. Verifica el scraping.")

