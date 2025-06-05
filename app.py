import streamlit as st
import pandas as pd

st.title("Precio del Samsung Galaxy S23 Ultra")

df = pd.read_csv("data/producto.csv")
st.write(df)
