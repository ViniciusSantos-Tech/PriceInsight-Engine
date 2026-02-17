import pandas as pd
import streamlit as st
from database import engine
import plotly.express as px
from prevision import PricePredictor

st.set_page_config(page_title='Price Monitor', layout='wide')
st.title("Price Monitoring Dashboard")

def load_data():
    query = 'SELECT "Id", "Product", "Price", "Date" FROM public."History" ORDER BY "Date" ASC'
    try:
        with engine.connect() as connection:
            df = pd.read_sql(query, connection)
            return df
    except Exception as e:
        st.error(f"Database error: {e}")
        return pd.DataFrame()

df = load_data()
if not df.empty:
    df["Price"] = pd.to_numeric(df["Price"], errors='coerce')
    df = df.dropna(subset=["Price"])
    df["Date"] = pd.to_datetime(df["Date"])
    df["Day"] = df["Date"].dt.date
    df_daily = df.groupby(["Day", "Product"])["Price"].mean().reset_index()
    fig = px.line(
        df_daily, 
        x="Day", 
        y="Price", 
        color="Product",
        title="Price Variation: RTX 5090 vs RTX 4090",
        color_discrete_map={"RTX5090": "green", "RTX4090": "blue"},
        render_mode="svg"
    )
    fig.update_traces(line_shape="spline", mode="lines+markers")
    fig.update_layout(
        yaxis=dict(
            title="Price (R$)", 
            tickformat=",.0f",
            range=[df_daily["Price"].min() * 0.95, df_daily["Price"].max() * 1.05],
            gridcolor='rgba(255, 255, 255, 0.1)'
        ),
        xaxis=dict(
            title="Date", 
            tickformat="%d/%m",
            gridcolor='rgba(255, 255, 255, 0.1)'
        ),
        template="plotly_dark",
        height=500,
        plot_bgcolor='rgba(0,0,0,0)', 
        paper_bgcolor='rgba(0,0,0,0)',
    )
    
    st.plotly_chart(fig, use_container_width=True)
    predictor = PricePredictor()
    
    for product in ["RTX5090", "RTX4090"]:
        st.divider()
        st.subheader(f"Prediction for {product}")
        p_drop, p_rise = predictor.calculate_probabilities(product)
        c1, c2 = st.columns(2)
        c1.metric("Drop Probability", f"{p_drop}%", delta="- Trend")
        c2.metric("Rise Probability", f"{p_rise}%", delta="+ Trend", delta_color="inverse")
else:
    st.warning("No data available.")
