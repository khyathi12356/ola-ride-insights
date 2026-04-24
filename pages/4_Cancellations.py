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
st.title("❌ Cancellation Analysis")

# Split data AFTER filtering
cust = df[df["Booking_Status"] == "Canceled by Customer"]
driver = df[df["Booking_Status"] == "Canceled by Driver"]

# ---------------------------
# KPI
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

total_cancel = len(cust) + len(driver)

col1.metric("Customer Cancels", len(cust))
col2.metric("Driver Cancels", len(driver))
col3.metric("Total Cancellations", total_cancel)
col4.metric(
    "Cancellation Rate %",
    round((total_cancel / len(df)) * 100, 2) if len(df) > 0 else 0
)

# Optional debug
st.caption(f"Filtered Rows: {len(df)}")

st.divider()

# ---------------------------
# CUSTOMER REASONS
# ---------------------------
cust_reason = cust["Canceled_Rides_by_Customer"].dropna()
cust_reason = cust_reason.str.strip()

cust_reason = cust_reason[
    (~cust_reason.str.lower().str.contains("not applicable")) &
    (cust_reason != "")
]

cust_reason = cust_reason.value_counts().reset_index()
cust_reason.columns = ["Reason", "Count"]

if cust_reason.empty:
    st.warning("No valid customer cancellation reasons found")
else:
    fig1 = px.bar(
        cust_reason,
        x="Reason",
        y="Count",
        color="Count",
        text="Count",
        title="Customer Cancellation Reasons"
    )
    st.plotly_chart(fig1, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("The biggest issue is driver-related friction before pickup, especially drivers not moving or asking customers to cancel.")
st.write("User-side reasons exist but are significantly less impactful.")

# ---------------------------
# DRIVER REASONS
# ---------------------------
driver_reason = driver["Canceled_Rides_by_Driver"].dropna()
driver_reason = driver_reason.str.strip()

driver_reason = driver_reason[
    (~driver_reason.str.lower().str.contains("not applicable")) &
    (driver_reason != "")
]

driver_reason = driver_reason.value_counts().reset_index()
driver_reason.columns = ["Reason", "Count"]

if driver_reason.empty:
    st.warning("No valid driver cancellation reasons found")
else:
    fig2 = px.bar(
        driver_reason,
        x="Reason",
        y="Count",
        color="Count",
        text="Count",
        title="Driver Cancellation Reasons"
    )
    st.plotly_chart(fig2, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("Driver-side issues like personal constraints and customer-related challenges drive most cancellations.")
st.write("Safety concerns and ride conditions also contribute, highlighting operational gaps.")