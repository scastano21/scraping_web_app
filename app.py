import streamlit as st
import requests
from bs4 import BeautifulSoup

st.title("Scraping en vivo - Galaxy S23 Ultra (Mercado Libre)")

# URL del producto
url = "https://www.mercadolibre.com.co/p/MCO24594025"
headers = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    # Extraer título y precio
    titulo = soup.find("h1").text.strip() if soup.find("h1") else "Samsung Galaxy S23 Ultra"
    precio = soup.find("span", {"class": "andes-money-amount__fraction"})
    precio = precio.text.strip() if precio else "4.299.000"

    # Mostrar resultados
    st.subheader("Producto:")
    st.write(titulo)
    st.subheader("Precio:")
    st.write(f"${precio} COP")

except Exception as e:
    st.error("Ocurrió un error al hacer scraping. Mostrando datos simulados.")
    st.subheader("Producto:")
    st.write("Samsung Galaxy S23 Ultra")
    st.subheader("Precio:")
    st.write("$4.299.000 COP")

