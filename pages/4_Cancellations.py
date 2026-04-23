import streamlit as st
import plotly.express as px
from utils.db import run_query

df = run_query("SELECT * FROM rides")

st.title("❌ Cancellation Analysis")

cust = df[df["Booking_Status"] == "Canceled by Customer"]
driver = df[df["Booking_Status"] == "Canceled by Driver"]

# KPIs 
col1, col2, col3, col4 = st.columns(4)

total_cancel = len(cust) + len(driver)

col1.metric("Customer Cancels", len(cust))
col2.metric("Driver Cancels", len(driver))
col3.metric("Total Cancellations", total_cancel)
col4.metric("Cancellation Rate %", round((total_cancel / len(df)) * 100, 2))

st.divider()

# CUSTOMER REASONS 
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
    st.plotly_chart(fig1, width='stretch')

st.markdown("### 📊 Insight")
st.write("The biggest issue is “driver not moving toward pickup,” followed by “driver asked to cancel,” showing strong driver-related friction before rides even start.")
st.write("Secondary reasons like plan changes, AC issues, and wrong address are much lower, indicating operational reliability matters more than user-side factors.")

# DRIVER REASONS 
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
    st.plotly_chart(fig2, width='stretch')

st.markdown("### 📊 Insight")
st.write("Most cancellations come from personal/car-related issues and customer-related problems, suggesting driver readiness and rider behavior both drive drop-offs.")
st.write("Health concerns (customer coughing) and overcrowding also contribute notably, highlighting safety and policy enforcement as key factors.")