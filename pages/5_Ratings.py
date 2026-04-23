import streamlit as st
import plotly.express as px
from utils.db import run_query

df = run_query("SELECT * FROM rides")

st.title("⭐ Ratings Analysis")

df = df.dropna(subset=["Customer_Rating", "Driver_Ratings"])

# KPI SECTION 
col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg Customer Rating", round(df["Customer_Rating"].mean(), 2))
col2.metric("Avg Driver Rating", round(df["Driver_Ratings"].mean(), 2))
col3.metric("Highest Customer Rating", df["Customer_Rating"].max())
col4.metric("Lowest Driver Rating", df["Driver_Ratings"].min())

st.divider()

# EXISTING CODE 

fig1 = px.histogram(df, x="Customer_Rating", nbins=10, title="Customer Ratings")
st.plotly_chart(fig1, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("Ratings are concentrated around 4.0–4.5, indicating most customers report positive ride experiences.")
st.write("Low ratings are minimal, suggesting dissatisfaction exists but is not widespread.")

fig2 = px.histogram(df, x="Driver_Ratings", nbins=10, title="Driver Ratings")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("Driver ratings also cluster tightly around 4.0–4.5, reflecting consistently good service quality.")
st.write("The small spread shows limited performance variation across drivers.")

avg = df.groupby("Vehicle_Type")[["Customer_Rating", "Driver_Ratings"]].mean().reset_index()

fig3 = px.bar(
    avg,
    x="Vehicle_Type",
    y=["Customer_Rating", "Driver_Ratings"],
    barmode="group"
)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("Customer and driver ratings are nearly identical across all vehicle types, indicating uniform experience regardless of category.")
st.write("No vehicle segment stands out, suggesting service quality is standardized rather than differentiated.")