<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A90E2,100:000000&height=180&section=header&text=PriceInsight-Engine&fontSize=50&fontColor=ffffff" />
</p>

> [!WARNING]
> This project is a functional study of Data ETL (Extract, Transform, Load) pipelines using LLMs for data cleaning.

## 📋 The Project
**PriceInsight-Engine** is a tool built to solve a specific problem: manual price monitoring of high-end hardware. Instead of dealing with fragile Regex patterns to parse HTML, this engine uses **Generative AI** to interpret web data and extract pricing information reliably.

The project demonstrates how to connect a Python scraper to a cloud database (PostgreSQL) and visualize historical trends in a web dashboard.

---

## 🏗️ Architecture & Logic
I designed this pipeline to be modular. Each file has a single responsibility:

### 1. Extraction (Scraping Layer)
The script targets e-commerce platforms using the `Requests` library. 
* **Challenge:** Anti-bot mechanisms.
* **Solution:** Implementation of browser-mimicking headers to ensure the HTML is returned instead of a `403 Forbidden` error.

### 2. Transformation (AI Semantic Layer)
This is the core of the project. Instead of searching for a specific HTML tag that might change tomorrow, the raw text is sent to the **Llama-3.3-70b** model via **Groq**.
* **Prompt Engineering:** The AI is instructed to ignore installment prices and "from/to" traps, returning only the raw numeric value for cash payments.
* **Data Sanitization:** The engine ensures the output is a clean JSON, ready for database insertion without further string manipulation.

### 3. Storage (Persistence Layer)
Data is stored in a **PostgreSQL** database (hosted on Railway).
* **ORM:** I used **SQLAlchemy** to handle the database schema and sessions.
* **Schema:** The `History` table tracks the product name, the price (as a cleaned string for safety), and an automatic UTC timestamp.

### 4. Presentation (Analytics Layer)
A **Streamlit** dashboard provides the interface.
* It performs SQL queries to fetch historical data.
* Uses **Pandas** for on-the-fly data type conversion.
* Renders a **Plotly** spline chart to show price volatility over time.

## 🟦 System Interface
<p align="center">
  <img src="assents/streamlitphoto1.png" alt="Price Dashboard" width="900px" style="border-radius: 15px; border: 2px solid #00FFFF;">
  <br>
  <img src="https://img.shields.io/badge/Pipeline-Active-00FFFF?style=for-the-badge&logo=rocket" />
</p>

## 🛠️ Technical Stack
* **Language:** Python 3.10+
* **AI:** Groq API (Llama 3.3 model)
* **Scraping:** BeautifulSoup4 & Requests
* **Database:** PostgreSQL & SQLAlchemy ORM
* **Frontend:** Streamlit & Plotly

---

## 🟦🔵​ Environment Setup
To run this locally, you need a `.env` file with:
```env
GROQ_API_KEY=your_api_key
DATABASE_URL=your_postgresql_url
