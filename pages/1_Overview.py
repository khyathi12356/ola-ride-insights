import streamlit as st
import plotly.express as px

df = st.session_state["df"]

st.title("📊 Business Overview")

# ---------------- KPI SECTION ----------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Rides", len(df))
col2.metric("Total Revenue", f"₹ {df['Booking_Value'].sum():,.0f}")
col3.metric("Avg Rating", round(df["Customer_Rating"].mean(), 2))
col4.metric("Cancellation Rate", f"{df['Is_Cancelled'].mean()*100:.1f}%")

st.divider()

# ---------------- RIDE VOLUME ----------------
rides = df.groupby("Hour")["Booking_ID"].count().reset_index()

fig1 = px.area(
    rides,
    x="Hour",
    y="Booking_ID",
    title="📈 Ride Demand by Hour",
    markers=True
)

st.plotly_chart(fig1, use_container_width=True)

# ---------------- STATUS ----------------
status = df["Booking_Status"].value_counts().reset_index()
status.columns = ["Status", "Count"]

fig2 = px.pie(status, names="Status", values="Count", title="📌 Booking Status Distribution")

st.plotly_chart(fig2, use_container_width=True)