import streamlit as st
import plotly.express as px
from utils.db import run_query

df = run_query("SELECT * FROM rides")

st.title("🚗 Vehicle Analysis")

# ---------------- KPI SECTION (UPDATED ONLY) ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", len(df))
col2.metric("Vehicle Types", df["Vehicle_Type"].nunique())
col3.metric("Avg Distance (km)", round(df["Ride_Distance"].mean(), 2))

# FIX: safer mode calculation (prevents crash if nulls exist)
top_vehicle = df["Vehicle_Type"].mode()
col4.metric("Top Vehicle Type", top_vehicle[0] if not top_vehicle.empty else "N/A")

st.divider()

# ---------------- EXISTING CODE (UNCHANGED) ----------------

# Vehicle count
vehicle_count = df["Vehicle_Type"].value_counts().reset_index()
vehicle_count.columns = ["Vehicle_Type", "Count"]

fig1 = px.bar(
    vehicle_count,
    x="Vehicle_Type",
    y="Count",
    color="Count",
    text="Count",
    title="Vehicle Demand"
)
st.plotly_chart(fig1, use_container_width=True)

# Avg distance
avg_dist = df.groupby("Vehicle_Type")["Ride_Distance"].mean().reset_index()

fig2 = px.bar(
    avg_dist,
    x="Vehicle_Type",
    y="Ride_Distance",
    color="Ride_Distance",
    title="Avg Ride Distance"
)
st.plotly_chart(fig2, use_container_width=True)