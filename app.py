import streamlit as st
import pandas as pd
import os

# Ejecutar scraping si no existe el CSV
if not os.path.exists("data/producto.csv"):
    import subprocess
    subprocess.run(["python", "scraping.py"])

# Mostrar datos
st.title("Precio del Samsung Galaxy S23 Ultra")
df = pd.read_csv("data/producto.csv")
st.write(df)
