import streamlit as st
import plotly.express as px
from utils.db import run_query

df = run_query("SELECT * FROM rides")

st.title("💰 Revenue Insights")

# KPI
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Revenue", f"{df['Booking_Value'].sum():,.0f}")
col2.metric("Avg Booking Value", round(df["Booking_Value"].mean(), 2))
col3.metric("Successful Revenue", f"{df[df['Booking_Status']=='Success']['Booking_Value'].sum():,.0f}")
col4.metric("Top Paying Customer", df.groupby("Customer_ID")["Booking_Value"].sum().idxmax())

st.divider()

fig = px.pie(
    df,
    names="Payment_Method",
    values="Booking_Value",
    title="Revenue by Payment Method"
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("### 📊 Insight")
st.write("A large share of revenue comes from “Cash” and UPI payments, indicating gaps in payment tracking or categorization whereas Unknown here refers to the cancelled rides where no payment happening.")
st.write("Digital methods like UPI contribute significantly, while card payments remain very low, suggesting limited adoption.")

top_customers = df.groupby("Customer_ID")["Booking_Value"].sum().reset_index().sort_values(by="Booking_Value", ascending=False).head(5)

fig2 = px.bar(
    top_customers,
    x="Customer_ID",
    y="Booking_Value",
    title="Top Customers"
)
st.plotly_chart(fig2, use_container_width=True) 

st.markdown("### 📊 Insight")
st.write("Revenue is somewhat concentrated, with the top customer contributing noticeably more than others.")
st.write("However, the remaining top customers show similar spending levels, indicating a fairly balanced high-value customer base.")