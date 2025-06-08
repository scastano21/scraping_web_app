# Scraping Web App - Samsung Galaxy S23 Ultra

Esta aplicación web realiza **scraping en vivo** del producto *Samsung Galaxy S23 Ultra* desde [Mercado Libre Colombia](https://www.mercadolibre.com.co/p/MCO24594025). Extrae dinámicamente el nombre y el precio del producto y los muestra en una interfaz desarrollada con **Streamlit**.

##  Tecnologías utilizadas

- Python 3.10
- Requests & BeautifulSoup (Scraping)
- Streamlit (Interfaz web)
- Git y GitHub (Control de versiones)
- GitHub Actions (CI/CD)
- Render.com (Despliegue en la nube)

##  Aplicación en línea

 [Ver aplicación desplegada](https://scraping-web-app.onrender.com)

## Estructura del proyecto

```
scraping_web_app/
├── app.py                 # App principal Streamlit
├── requirements.txt       # Dependencias del proyecto
├── tests/
│   └── test_scraping.py   # Pruebas básicas para CI
├── .github/
│   └── workflows/
│       └── ci.yml         # Pipeline CI/CD de GitHub Actions
```

## CI/CD con GitHub Actions

Cada vez que se hace push o merge a la rama `main`, GitHub Actions ejecuta:
- Instalación de dependencias
- Pruebas automatizadas (pytest)

El flujo está definido en `.github/workflows/ci.yml`.

## Cómo ejecutar localmente

1. Clona el repositorio:
```bash
git clone https://github.com/scastano21/scraping_web_app.git
cd scraping_web_app
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta la aplicación:
```bash
streamlit run app.py
```

## Créditos y fuentes

- [Mercado Libre Colombia - Samsung S23 Ultra](https://www.mercadolibre.com.co/p/MCO24594025)
- [Streamlit Docs](https://docs.streamlit.io)
- [Render Docs](https://render.com/docs)
- [GitHub Actions Docs](https://docs.github.com/actions)

---

Desarrollado por **Sebastián Castaño Cossio** 
