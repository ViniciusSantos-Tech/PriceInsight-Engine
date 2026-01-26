<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FFFF,100:000000&height=220&section=header&text=PriceInsight%20Engine&fontSize=70&fontColor=ffffff&animation=fadeIn" />
</p>

<h3 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=00FFFF&center=true&vCenter=true&width=600&lines=Automated+Price+Intelligence;AI-Powered+Data+Parsing+(Gemma+3);PostgreSQL+%2B+Streamlit+Visualization;Advanced+Data+Engineering+Pipeline" />
</h3>

<p align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%" />
</p>

## ⚡ The Project
**PriceInsight-Engine** is a sophisticated data pipeline designed to monitor market volatility. It bridges the gap between unstructured web data and structured business intelligence by leveraging **Local LLMs** to bypass traditional scraping limitations.

---

## 📸 System Interface
<p align="center">
  <img src="assets/streamlitphoto1.png" alt="Price Dashboard" width="900px" style="border-radius: 15px; border: 2px solid #00FFFF;">
  <br>
  <img src="https://img.shields.io/badge/Pipeline-Active-00FFFF?style=for-the-badge&logo=rocket" />
</p>

---

## 🏗️ System Architecture
The engine operates on a 4-layer architecture:

1.  **Ingestion Layer:** Custom scrapers extract raw HTML/Text from e-commerce targets.
2.  **Processing Layer:** **Ollama (Gemma 3)** acts as a semantic parser, converting messy text into validated JSON structures.
3.  **Storage Layer:** A **PostgreSQL** instance manages historical data, ensuring ACID compliance and relational integrity.
4.  **Presentation Layer:** A **Streamlit** dashboard provides real-time analytics with spline-interpolated trend lines.



---

## 🧠 Intelligence Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Ollama-Gemma3-black?style=for-the-badge&logo=ollama&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</p>

---

## 🛠️ Installation & Environment Setup

### 1. Prerequisites
- Python 3.10+
- PostgreSQL installed and running
- Ollama with `gemma3:4b` model

### 2. Clone & Install
```bash
git clone [https://github.com/your-username/PriceInsight-Engine.git](https://github.com/your-username/PriceInsight-Engine.git)
cd PriceInsight-Engine
pip install -r requirements.txt
