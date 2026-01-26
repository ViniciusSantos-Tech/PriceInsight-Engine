import pandas as pd
import streamlit as st
from database import engine

st.set_page_config(page_title='Price Monitor', layout='wide')
st.title("Monitor Monitoring")

def load_dates():
    query = 'SELECT "Id", "Product", "Price", "Date" FROM public."History" ORDER BY "Date" ASC'
    df = pd.read_sql(query, engine)
    return df

df = load_dates()

if not df.empty:
    df["Price"] = pd.to_numeric(df["Price"], errors='coerce')
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(by="Date")
    df = df.dropna(subset=["Price"])

    st.subheader("Recent data")
    st.dataframe(df)

    # Mantendo sua lógica de agrupar por dia que você gostou
    df["Day"] = df["Date"].dt.date
    st.subheader("Price variation over time")
    
    df_diario = df.groupby("Day")["Price"].mean().reset_index()

    # O Streamlit padrão NÃO faz curvas suaves (ondas). 
    # Para ter ondas EXATAMENTE como você quer, o único jeito é o Plotly.
    # Vou deixar o código o mais limpo possível, igual ao seu anterior, mas com o motor de ondas.
    
    import plotly.express as px
    fig = px.line(df_diario, x="Day", y="Price", render_mode="svg")
    fig.update_traces(line_shape="spline") # AQUI ESTÁ A ONDA
    fig.update_layout(
        yaxis=dict(range=[500, 1400]), # Eixo de 0 a 2000 como você pediu
        margin=dict(l=0, r=0, t=0, b=0),
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

else:
    st.warning("Database is empty")