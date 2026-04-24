import streamlit as st
import plotly.express as px
from utils.db import run_query

# Load data
df = run_query("SELECT * FROM rides")

# ---------------------------
# GET GLOBAL SLICERS
# ---------------------------
vehicle_filter = st.session_state.get("vehicle_type", [])
status_filter = st.session_state.get("booking_status", [])
payment_filter = st.session_state.get("payment_method", [])

# ---------------------------
# APPLY FILTERS
# ---------------------------
if vehicle_filter:
    df = df[df["Vehicle_Type"].isin(vehicle_filter)]

if status_filter:
    df = df[df["Booking_Status"].isin(status_filter)]

if payment_filter:
    df = df[df["Payment_Method"].isin(payment_filter)]

# ---------------------------
# PAGE TITLE
# ---------------------------
st.title("📊 Overview Dashboard")

# ---------------------------
# KPI METRICS
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", len(df))
col2.metric("Revenue", f"₹ {df['Booking_Value'].sum():,.0f}")
col3.metric("Avg Rating", round(df["Customer_Rating"].mean(), 2))
col4.metric(
    "Cancelled %",
    round(
        (df["Booking_Status"]
         .str.contains("Canceled", case=False, na=False)
         .mean()) * 100, 2
    )
)

# Optional debug (professional touch)
st.caption(f"Filtered Rows: {len(df)}")

st.divider()

# ---------------------------
# RIDE VOLUME TREND
# ---------------------------
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
st.write("Ride demand remains steady across all hours with mild peaks during mid-day and evening hours.")
st.write("This indicates consistent usage but also an opportunity to optimize pricing and driver availability.")

# ---------------------------
# BOOKING STATUS PIE
# ---------------------------
fig2 = px.pie(df, names="Booking_Status", title="Booking Status Breakdown")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("Only ~62% of bookings are successfully completed, indicating a significant drop-off in ride fulfillment.")
st.write("Driver availability and cancellations are the primary contributors to failed bookings.")