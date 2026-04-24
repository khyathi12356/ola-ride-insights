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
st.title("🚗 Vehicle Analysis")

# ---------------------------
# KPI
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", len(df))
col2.metric("Vehicle Types", df["Vehicle_Type"].nunique())
col3.metric("Avg Distance (km)", round(df["Ride_Distance"].mean(), 2))

top_vehicle = df["Vehicle_Type"].mode()
col4.metric("Top Vehicle Type", top_vehicle[0] if not top_vehicle.empty else "N/A")

# Optional debug
st.caption(f"Filtered Rows: {len(df)}")

st.divider()

# ---------------------------
# VEHICLE DEMAND
# ---------------------------
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
st.write("Demand is fairly evenly distributed across all vehicle types, with Prime Sedan slightly leading.")
st.write("This indicates balanced usage with slight preference for premium rides.")

# ---------------------------
# AVG DISTANCE
# ---------------------------
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
st.write("Auto rides have shorter distances, while other vehicles average 14–16 km.")
st.write("This shows autos are used for short trips, while cars/bikes handle longer rides.")