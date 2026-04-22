import streamlit as st
import plotly.express as px
from utils.db import run_query

df = run_query("SELECT * FROM rides")

st.title("⭐ Ratings Analysis")

df = df.dropna(subset=["Customer_Rating", "Driver_Ratings"])

# ---------------- KPI SECTION (ADDED ONLY) ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg Customer Rating", round(df["Customer_Rating"].mean(), 2))
col2.metric("Avg Driver Rating", round(df["Driver_Ratings"].mean(), 2))
col3.metric("Highest Customer Rating", df["Customer_Rating"].max())
col4.metric("Lowest Driver Rating", df["Driver_Ratings"].min())

st.divider()

# ---------------- EXISTING CODE (UNCHANGED) ----------------

fig1 = px.histogram(df, x="Customer_Rating", nbins=10, title="Customer Ratings")
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.histogram(df, x="Driver_Ratings", nbins=10, title="Driver Ratings")
st.plotly_chart(fig2, use_container_width=True)

avg = df.groupby("Vehicle_Type")[["Customer_Rating", "Driver_Ratings"]].mean().reset_index()

fig3 = px.bar(
    avg,
    x="Vehicle_Type",
    y=["Customer_Rating", "Driver_Ratings"],
    barmode="group"
)
st.plotly_chart(fig3, use_container_width=True)