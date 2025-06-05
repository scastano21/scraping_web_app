import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.mercadolibre.com.co/p/MCO24594025"
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

titulo = soup.find("h1").text.strip() if soup.find("h1") else "No encontrado"
precio = soup.find("span", {"class": "andes-money-amount__fraction"}).text if soup.find("span", {"class": "andes-money-amount__fraction"}) else "No disponible"

with open("data/producto.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Producto", "Precio"])
    writer.writerow([titulo, precio])
