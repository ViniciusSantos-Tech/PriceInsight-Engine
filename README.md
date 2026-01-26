<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:00FFFF,100:000000&height=220&section=header&text=PriceInsight%20Engine&fontSize=70&fontColor=ffffff&animation=fadeIn" />
</p>

<h3 align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=00FFFF&center=true&vCenter=true&width=600&lines=Automated+Price+Intelligence;AI-Powered+Data+Parsing+(Gemma+3);PostgreSQL+%2B+Streamlit+Visualization;The+Future+of+Market+Analysis" />
</h3>

<p align="center">
  <img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/aqua.png" width="100%" />
</p>

## ⚡ The Project
**PriceInsight-Engine** não é apenas um script, é um organismo completo de monitoramento de mercado. Ele caça dados brutos, utiliza **Inteligência Artificial local** para entender preços e transforma tudo em gráficos de tendência brutais.

---

## 📸 Dashboard Live Preview
<p align="center">
  <img src="assets/streamlitphoto1.png" alt="Price Dashboard" width="900px" style="border-radius: 15px; border: 2px solid #00FFFF;">
  <br>
  <img src="https://img.shields.io/badge/Status-Data%20Flowing-00FFFF?style=for-the-badge&logo=rocket" />
</p>
---

## 🧠 Intelligence Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Ollama-Gemma3-black?style=for-the-badge&logo=ollama&logoColor=white" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" />
</p>

---

## 🛠️ Operational Flow

<p align="left">
  🔹 <b>Data Extraction:</b> Scraper de alta precisão via BeautifulSoup/Selenium.<br>
  🔹 <b>AI Inference:</b> Processamento de linguagem natural com Gemma 3 para extração de JSON limpo.<br>
  🔹 <b>Persistent Storage:</b> Histórico completo armazenado em PostgreSQL via SQLAlchemy.<br>
  🔹 <b>Deep Analytics:</b> Visualização de curvas spline e correlação de moedas em tempo real.
</p>

---

## 🚀 Setup & Launch

```bash
# Clone o motor
git clone [https://github.com/seu-usuario/PriceInsight-Engine.git](https://github.com/seu-usuario/PriceInsight-Engine.git)

# Instale os módulos
pip install -r requirements.txt

# Configure suas credenciais (Local Only)
echo "DATABASE_URL=postgresql://user:pass@localhost:5432/db" > .env

# Inicie o Dashboard
streamlit run app.py
