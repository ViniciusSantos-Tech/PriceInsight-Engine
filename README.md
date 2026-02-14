<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:4A90E2,100:000000&height=180&section=header&text=PriceInsight-Engine&fontSize=50&fontColor=ffffff" />
</p>

> [!WARNING]
> This project is under constant development. Due to frequent updates, errors may occur. The **Price Prediction** logic and the implementation of the **Linear Regression** library were developed with significant assistance from **Generative AI**. This is a functional study and results should be interpreted as experimental.

## 📋 The Project
**PriceInsight-Engine** is a data-focused pipeline designed to automate hardware price tracking. The core objective is to replace rigid, easily-broken scraping rules with an **AI Semantic Layer** for data extraction. 
## 🟦 System Interface
<p align="center">
  <img src="assents/photo1.png" alt="Price Dashboard" width="900px" style="border-radius: 15px; border: 2px solid #00FFFF;">
</p>

The system captures raw HTML from e-commerce sites, leverages an LLM to identify and extract the correct price, stores it in a cloud PostgreSQL database, and displays the results in a real-time dashboard featuring trend forecasting.

### 🌐 Live Access
You can test the application directly at:
**[https://priceinsight-engine.streamlit.app/](https://priceinsight-engine.streamlit.app/)**

---

## 🏗️ Architecture & Logic
The project is divided into modular components to ensure a maintainable data flow:

| Category | Badges |
| :--- | :--- |
| **Data & AI** | ![Python](https://img.shields.io/badge/python-v3.10+-blue?style=flat-square) ![Llama 3.3](https://img.shields.io/badge/AI-Llama%203.3%20(Groq)-orange?style=flat-square) ![Scikit-learn](https://img.shields.io/badge/ML-Scikit--learn-F7931E?style=flat-square&logo=scikit-learn) |
| **Infra & DB** | ![PostgreSQL](https://img.shields.io/badge/db-PostgreSQL-336791?style=flat-square&logo=postgresql) ![Powered by Railway](https://img.shields.io/badge/powered%20by-Railway-0b3d8d?style=flat-square&logo=railway) ![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-red?style=flat-square) |
| **Frontend** | ![Streamlit](https://img.shields.io/badge/frontend-Streamlit-FF4B4B?style=flat-square&logo=streamlit) ![Plotly](https://img.shields.io/badge/viz-Plotly-3F4F75?style=flat-square&logo=plotly) |

### 1. Data Collection (Scraping)
The `scrap.py` module utilizes `Requests` and `BeautifulSoup` to fetch e-commerce content.
* **Optimization:** Unnecessary tags like `<script>`, `<style>`, and `<nav>` are decomposed to save processing power and LLM tokens.
* **Bot Evasion:** Uses browser-mimicking headers to bypass common anti-bot protections.

### 2. Intelligent Processing (AI Layer)
Instead of regex-based rules, `ai_processor.py` sends cleaned text to **Llama-3.3-70b** via **Groq**.
* **Task:** The AI extracts only the numerical cash price and enforces strict naming conventions (e.g., `RTX5090` without spaces) to prevent dashboard duplication.
* **Validation:** Responses are parsed into a strict JSON structure before reaching the database.

### 3. Persistence (Database)
Managed by `database.py` and `crud.py`, the system uses **SQLAlchemy** to interface with a **PostgreSQL** database.
* **Integrity:** Includes robust session management with `rollback()` and `close()` routines to prevent connection leaks.
* **Temporal Tracking:** The database automatically records entry dates using UTC timestamps.

### 4. Forecasting (Statistics)
The `prevision.py` module uses `Scikit-learn` to perform **Linear Regression** on historical price data.
* **Trend Analysis:** It calculates the "slope" of price changes to estimate the probability of price drops or rises.
* **Safety:** Returns a neutral 50/50 probability if insufficient data (fewer than 3 records) is available.

### 5. Visualization (Dashboard)
The `app.py` file builds the web interface using **Streamlit**.
* **Interactive Charts:** Renders interactive line charts via **Plotly** with spline smoothing.
* **Real-time Metrics:** Displays dynamic prediction cards calculated on-the-fly based on the latest database updates.

---

## 🛠️ Technical Stack
* **Language:** Python 3.10+
* **AI:** Groq API (Llama 3.3-70b)
* **Infrastructure:** Railway (Cloud Database)
* **Libraries:** SQLAlchemy, Scikit-learn, Pandas, Streamlit, Plotly, BeautifulSoup4

---

## 🟦🔵 Environment Setup
To run this project locally, configure a `.env` file with the following variables:
```env
GROQ_API_KEY=your_groq_api_token
DATABASE_URL=your_postgresql_railway_url
