import streamlit as st
import plotly.express as px
from utils.db import run_query

df = run_query("SELECT * FROM rides")

st.title("📊 Overview Dashboard")

# KPIs
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", len(df))
col2.metric("Revenue", f"₹ {df['Booking_Value'].sum():,.0f}")
col3.metric("Avg Rating", round(df["Customer_Rating"].mean(), 2))
col4.metric(
    "Cancelled %",
    round((df["Booking_Status"].str.contains("Canceled", case=False, na=False).mean()) * 100, 2)
)

st.divider()


# Ride volume trend (corrected)
df_hour = df.groupby("Hour").size().reset_index(name="Ride_Count")

fig = px.line(
    df_hour,
    x="Hour",
    y="Ride_Count",
    markers=True,
    title="Ride Demand by Hour"
)

st.plotly_chart(fig, use_container_width=True)


st.markdown("### 📊 Insight")
st.write("Ride demand remains steady across all hours with only mild peaks during mid-day (~12 to 1 PM) and evening hours (~3 to 5 PM), showing no sharp peak periods.")
st.write("This indicates consistent usage but also a missed opportunity to optimize pricing and driver availability during high-demand moments.")

# BOOKING STATUS 
fig2 = px.pie(df, names="Booking_Status", title="Booking Status Breakdown")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("Only ~62 percent of bookings are successfully completed, meaning nearly 4 out of 10 rides fail—this points to a major reliability issue in the system.")
st.write("The biggest contributors are **driver unavailability (17.9%)** and cancellations from both drivers and customers (~20 percent combined), indicating supply-demand mismatch and poor fulfillment experience.")