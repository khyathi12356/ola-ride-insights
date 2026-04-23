import streamlit as st
import plotly.express as px
from utils.db import run_query

df = run_query("SELECT * FROM rides")

st.title("🚗 Vehicle Analysis")

# KPI
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", len(df))
col2.metric("Vehicle Types", df["Vehicle_Type"].nunique())
col3.metric("Avg Distance (km)", round(df["Ride_Distance"].mean(), 2))

top_vehicle = df["Vehicle_Type"].mode()
col4.metric("Top Vehicle Type", top_vehicle[0] if not top_vehicle.empty else "N/A")

st.divider()

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

st.markdown("### 📊 Insight")
st.write("Demand is fairly evenly distributed across all vehicle types, with Prime Sedan slightly leading as the most preferred option.")
st.write("This indicates no heavy dependency on a single category, but a slight customer preference toward premium comfort rides.")

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

st.markdown("### 📊 Insight")
st.write("Auto rides have significantly shorter trip distances, while all other vehicle types average around 14 to 16 km.")
st.write("This suggests autos are mainly used for short trips, whereas bikes and cars serve medium to longer-distance travel needs.")