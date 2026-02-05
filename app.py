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
        st.error(f"Database connection error: {e}")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    df["Price"] = pd.to_numeric(df["Price"], errors='coerce')
    df = df.dropna(subset=["Price"])
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(by="Date")
    df["Day"] = df["Date"].dt.date
    st.subheader("Data Table")
    st.dataframe(df)

    df_daily = df.groupby("Day")["Price"].mean().reset_index()

    fig = px.line(df_daily, x="Day", y="Price", title="Price Variation")
    fig.update_traces(line_shape="spline", mode="lines+markers")

    fig.update_layout(
        yaxis=dict(
            title="Price (R$)",
            tickformat=",.0f", 
            range=[df_daily["Price"].min() * 0.98, df_daily["Price"].max() * 1.02]
        ),
        xaxis=dict(tickformat="%d/%m"),
        template="plotly_dark",
        height=500
    )
    st.plotly_chart(fig, use_container_width=True)

    predictor = PricePredictor()
    p_drop, p_rise = predictor.calculate_probabilities()
    
    st.subheader("Price Prediction")
    c1, c2 = st.columns(2)
    c1.metric("Probability to FALL", f"{p_drop}%", delta="- Trend", delta_color="normal")
    c2.metric("Probability to RISE", f"{p_rise}%", delta="+ Trend", delta_color="inverse")
else:
    st.warning("No data found.")
