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
st.title("💰 Revenue Insights")

# ---------------------------
# KPI
# ---------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"{df['Booking_Value'].sum():,.0f}")
col2.metric("Avg Booking Value", round(df["Booking_Value"].mean(), 2))
col3.metric(
    "Successful Revenue",
    f"{df[df['Booking_Status']=='Success']['Booking_Value'].sum():,.0f}"
)

top_customer = df.groupby("Customer_ID")["Booking_Value"].sum()
col4.metric("Top Paying Customer", top_customer.idxmax() if not top_customer.empty else "N/A")

# Optional debug
st.caption(f"Filtered Rows: {len(df)}")

st.divider()

# ---------------------------
# REVENUE BY PAYMENT METHOD
# ---------------------------
fig = px.pie(
    df,
    names="Payment_Method",
    values="Booking_Value",
    title="Revenue by Payment Method"
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("Cash and UPI contribute a major share of revenue, while card usage remains low.")
st.write("‘Unknown’ mainly represents canceled rides where no transaction occurred.")

# ---------------------------
# TOP CUSTOMERS
# ---------------------------
top_customers = (
    df.groupby("Customer_ID")["Booking_Value"]
    .sum()
    .reset_index()
    .sort_values(by="Booking_Value", ascending=False)
    .head(5)
)

fig2 = px.bar(
    top_customers,
    x="Customer_ID",
    y="Booking_Value",
    title="Top Customers"
)
st.plotly_chart(fig2, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("Revenue shows moderate concentration among top users.")
st.write("However, spending across top customers remains relatively balanced.")