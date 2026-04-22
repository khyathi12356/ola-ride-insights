import streamlit as st
import pandas as pd

st.set_page_config(page_title="OLA Analytics", layout="wide")

df = pd.read_csv("cleaned_ola_data.csv")

st.title("🚖 OLA Ride Analytics Dashboard")

# -------------------------
# GLOBAL FILTERS (SLICERS)
# -------------------------
st.sidebar.header("🎛 Filters")

vehicle = st.sidebar.multiselect(
    "Vehicle Type",
    df["Vehicle_Type"].unique(),
    default=df["Vehicle_Type"].unique()
)

payment = st.sidebar.multiselect(
    "Payment Method",
    df["Payment_Method"].unique(),
    default=df["Payment_Method"].unique()
)

status = st.sidebar.multiselect(
    "Booking Status",
    df["Booking_Status"].unique(),
    default=df["Booking_Status"].unique()
)

df_filtered = df[
    (df["Vehicle_Type"].isin(vehicle)) &
    (df["Payment_Method"].isin(payment)) &
    (df["Booking_Status"].isin(status))
]

st.session_state["df"] = df_filtered

st.success("Filters applied globally ✔ Navigate pages from sidebar")