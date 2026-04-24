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
st.title("⭐ Ratings Analysis")

# Remove null ratings AFTER filtering
df = df.dropna(subset=["Customer_Rating", "Driver_Ratings"])

# ---------------------------
# KPI SECTION
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Avg Customer Rating", round(df["Customer_Rating"].mean(), 2) if len(df) > 0 else 0)
col2.metric("Avg Driver Rating", round(df["Driver_Ratings"].mean(), 2) if len(df) > 0 else 0)
col3.metric("Highest Customer Rating", df["Customer_Rating"].max() if len(df) > 0 else 0)
col4.metric("Lowest Driver Rating", df["Driver_Ratings"].min() if len(df) > 0 else 0)

# Optional debug
st.caption(f"Filtered Rows: {len(df)}")

st.divider()

# ---------------------------
# CUSTOMER RATINGS
# ---------------------------
fig1 = px.histogram(df, x="Customer_Rating", nbins=10, title="Customer Ratings")
st.plotly_chart(fig1, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("Ratings are concentrated around 4.0–4.5, indicating generally positive ride experiences.")
st.write("Low ratings are limited, suggesting minimal dissatisfaction.")

# ---------------------------
# DRIVER RATINGS
# ---------------------------
fig2 = px.histogram(df, x="Driver_Ratings", nbins=10, title="Driver Ratings")
st.plotly_chart(fig2, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("Driver ratings also cluster around 4.0–4.5, showing consistent service quality.")
st.write("Variation is minimal across drivers.")

# ---------------------------
# VEHICLE TYPE COMPARISON
# ---------------------------
avg = df.groupby("Vehicle_Type")[["Customer_Rating", "Driver_Ratings"]].mean().reset_index()

fig3 = px.bar(
    avg,
    x="Vehicle_Type",
    y=["Customer_Rating", "Driver_Ratings"],
    barmode="group",
    title="Ratings by Vehicle Type"
)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("Ratings are consistent across all vehicle types, indicating standardized service quality.")
st.write("No segment significantly outperforms others.")