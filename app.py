import pandas as pd
import streamlit as st
from database import engine
import plotly.express as px

st.set_page_config(page_title='Price Monitor', layout='wide')
st.title("Monitor Monitoring")

def load_dates():
    query = 'SELECT "Id", "Product", "Price", "Date" FROM public."History" ORDER BY "Date" ASC'
    try:
        with engine.connect() as connection:
            df = pd.read_sql(query, connection)
            return df
    except Exception as e:
        st.error(f"Error to connect database: {e}")
        return pd.DataFrame()

df = load_dates()

if not df.empty:
    df["Price"] = pd.to_numeric(df["Price"], errors='coerce')
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values(by="Date")
    df = df.dropna(subset=["Price"])

    st.subheader("Recent data")
    st.dataframe(df)

    df["Day"] = df["Date"].dt.date
    st.subheader("Price variation over time")
    
    df_diario = df.groupby("Day")["Price"].mean().reset_index()

    fig = px.line(df_diario, x="Day", y="Price", render_mode="svg")
    fig.update_traces(line_shape="spline")
    fig.update_layout(
        yaxis=dict(range=[500, 1000]),
        xaxis=dict(
            tickmode='linear',
            dtick=86400000.0,
            tickformat="%d/%m"
        ),
        margin=dict(l=0, r=0, t=50, b=0),
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

    if st.button("Update"):
        st.cache_data.clear()
        st.rerun()

else:
    st.warning("Database is empty")

